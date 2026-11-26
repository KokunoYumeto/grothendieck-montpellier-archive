#!/usr/bin/env python3
"""Numerical search for a BORDER restriction K3,3(2) -> 2K3(2).

Exact restriction is excluded by SH19.  A small residual here is only
exploratory evidence; it is never treated as an exact identity or proof.
All local parameters are retained for the best run.
"""
import itertools
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.optimize import minimize


def graph_tensors(q):
    dim = q**4
    src = np.zeros((dim,)*3, dtype=np.complex128)
    target = np.zeros_like(src)
    directed = [(i,j) for i in range(3) for j in range(3) if i != j]
    undirected = [(0,1),(0,2),(1,2)]
    for vals in itertools.product(range(q), repeat=6):
        x = dict(zip(directed,vals))
        ix = []
        for i in range(3):
            ns = [j for j in range(3) if j != i]
            ix.append(((x[i,ns[0]]*q+x[i,ns[1]])*q+x[ns[0],i])*q+x[ns[1],i])
        src[tuple(ix)] = 1
        left = dict(zip(undirected, vals[:3]))
        right = dict(zip(undirected, vals[3:]))
        ix = []
        for i in range(3):
            es = [tuple(sorted((i,j))) for j in range(3) if j != i]
            ix.append(((left[es[0]]*q+left[es[1]])*q+right[es[0]])*q+right[es[1]])
        target[tuple(ix)] = 1
    return src, target


def main():
    config = json.loads(Path(sys.argv[1]).read_text())
    outbase = Path(sys.argv[2])
    q = config['wire_dimension']
    h = q*q
    dim = h*h
    src, target = graph_tensors(q)
    target_norm2 = float(np.vdot(target,target).real)
    shape = (3,2,h,h,q)
    nc = int(np.prod(shape))

    def unpack(x):
        return (x[:nc]+1j*x[nc:]).reshape(shape)

    def evaluate(x, gradient=True):
        par = unpack(x)
        fs = [np.einsum('acx,bdx->abcd',p[0],p[1],optimize=True).reshape(dim,dim)
              for p in par]
        y = np.einsum('ai,bj,ck,ijk->abc',*fs,src,optimize=True)
        a = np.vdot(target,y)
        b = float(np.vdot(y,y).real)
        if b < 1e-300:
            return 1.0,np.zeros_like(x)
        fidelity = float(abs(a)**2/(b*target_norm2))
        loss = 1-fidelity
        if not gradient:
            return dict(loss=loss,fidelity=fidelity,output_norm2=b,
                        parameter_norm=float(np.linalg.norm(x)),
                        target_overlap=[float(a.real),float(a.imag)])
        gy = 2*(abs(a)**2*y-b*a*target)/(b*b*target_norm2)
        gf = [np.einsum('abc,bj,ck,ijk->ai',gy,fs[1].conj(),fs[2].conj(),src,optimize=True),
              np.einsum('abc,ai,ck,ijk->bj',gy,fs[0].conj(),fs[2].conj(),src,optimize=True),
              np.einsum('abc,ai,bj,ijk->ck',gy,fs[0].conj(),fs[1].conj(),src,optimize=True)]
        gp = np.empty_like(par)
        for i in range(3):
            g = gf[i].reshape(h,h,h,h)
            gp[i,0] = np.einsum('abcd,bdx->acx',g,par[i,1].conj(),optimize=True)
            gp[i,1] = np.einsum('abcd,acx->bdx',g,par[i,0].conj(),optimize=True)
        return loss,np.concatenate((gp.real.ravel(),gp.imag.ravel()))

    rng = np.random.default_rng(config['seed'])
    probe = rng.normal(size=2*nc)
    loss, grad = evaluate(probe)
    errors = []
    for j in rng.choice(len(probe),size=12,replace=False):
        xp = probe.copy(); xm = probe.copy()
        xp[j] += 1e-5; xm[j] -= 1e-5
        fd = (evaluate(xp)[0]-evaluate(xm)[0])/(2e-5)
        errors.append(abs(fd-grad[j]))
    assert max(errors) < 1e-7, max(errors)
    print(json.dumps(dict(kind='setup',config=config,source_nonzeros=int(np.count_nonzero(src)),
                          target_nonzeros=int(np.count_nonzero(target)),
                          gradient_max_error=max(errors))),flush=True)
    best_loss = 1.0
    all_runs = []
    for trial in range(config['restarts']):
        x = rng.normal(size=2*nc)/np.sqrt(h*h*q)
        if config.get('real_only',False):
            x[nc:] = 0
        started = time.monotonic()
        res = minimize(evaluate,x,jac=True,method='L-BFGS-B',
                       options=dict(maxiter=config['maxiter'],maxls=50,
                                    ftol=1e-15,gtol=1e-10,maxcor=30))
        metrics = evaluate(res.x,gradient=False)
        metrics.update(trial=trial,nit=int(res.nit),nfev=int(res.nfev),
                       message=str(res.message),seconds=time.monotonic()-started)
        all_runs.append(metrics)
        print(json.dumps(metrics),flush=True)
        if metrics['loss'] < best_loss:
            best_loss = metrics['loss']
            np.savez_compressed(str(outbase)+'_best.npz',parameters=unpack(res.x),
                                q=q,source=src,target=target)
        Path(str(outbase)+'_summary.json').write_text(json.dumps(dict(
            config=config,gradient_max_error=max(errors),runs=all_runs,best_loss=best_loss,
            status='exploratory numerical search; no border identity certified'),indent=2))


if __name__ == '__main__':
    main()
