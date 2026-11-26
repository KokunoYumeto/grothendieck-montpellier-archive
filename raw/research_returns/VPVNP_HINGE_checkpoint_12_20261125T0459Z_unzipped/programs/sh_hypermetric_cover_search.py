#!/usr/bin/env python3
"""Exploratory few-term K_{r,r-1}(q) -> K_r(q)*K_{r-1}(q) covers.

Evaluates the factored source; numerical overlaps are not certificates.
"""
import itertools
import json
import string
import sys
import time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize


def main():
    cfg=json.loads(Path(sys.argv[1]).read_text());base=Path(sys.argv[2])
    q,r,A=cfg['wire_dimension'],cfg['left_parties'],cfg['terms'];n=2*r-1
    outdims=[q**(r-1)]*r+[q**(r-2)]*(r-1)
    shape=[(outdims[i],)+(q,)*(r-1 if i<r else r) for i in range(n)]
    target=np.zeros(outdims,dtype=complex)
    edges=list(itertools.combinations(range(r),2))+list(itertools.combinations(range(r,n),2))
    incident=[[j for j,e in enumerate(edges) if i in e] for i in range(n)]
    for assignment in itertools.product(range(q),repeat=len(edges)):
        idx=[]
        for js in incident:
            value=0
            for j in js:value=value*q+assignment[j]
            idx.append(value)
        target[tuple(idx)]=1
    wire=[[string.ascii_lowercase[i*(r-1)+j] for j in range(r-1)] for i in range(r)]
    factors=[]
    for i in range(r):factors.append(string.ascii_uppercase[i]+''.join(wire[i]))
    for j in range(r-1):factors.append(string.ascii_uppercase[r+j]+''.join(wire[i][j] for i in range(r)))
    output=string.ascii_uppercase[:n];forward=','.join(factors)+'->'+output
    samples=[np.zeros(s,complex) for s in shape]
    fpath=np.einsum_path(forward,*samples,optimize='greedy')[0]
    back=[]
    for i in range(n):
        expr=output+','+','.join(factors[j] for j in range(n) if j!=i)+'->'+factors[i]
        args=[np.zeros_like(target)]+[samples[j] for j in range(n) if j!=i]
        back.append((expr,np.einsum_path(expr,*args,optimize='greedy')[0]))
    size=q**(2*r-2);nc=A*(n*size+1);tn=float(np.vdot(target,target).real)
    rng=np.random.default_rng(cfg['seed'])
    def unpack(x):
        z=x[:nc]+1j*x[nc:];raw=z[:A*n*size].reshape(A,n,size)
        norms=np.linalg.norm(raw,axis=2)
        mats=[[raw[a,i].reshape(shape[i])/norms[a,i] for i in range(n)] for a in range(A)]
        cr=z[A*n*size:];cn=np.linalg.norm(cr);cs=cr/cn
        return raw,norms,mats,cr,cn,cs
    def evaluate(x,gradient=True):
        raw,norms,mats,cr,cn,cs=unpack(x)
        zs=[np.einsum(forward,*ms,optimize=fpath) for ms in mats]
        y=sum(c*z for c,z in zip(cs,zs));ov=np.vdot(target,y);yn=float(np.vdot(y,y).real)
        loss=1-float(abs(ov)**2/(yn*tn))
        if not gradient:
            return dict(loss=loss,fidelity=1-loss,output_norm2=yn,
                        cancellation_ratio=float(sum(abs(c)*np.linalg.norm(z) for c,z in zip(cs,zs))/np.sqrt(yn)),
                        parameter_norm=float(np.linalg.norm(x))),mats,cs
        gy=2*(abs(ov)**2*y-yn*ov*target)/(yn*yn*tn)
        gm=np.zeros_like(raw);gc=np.empty(A,dtype=complex)
        for a in range(A):
            gc[a]=np.vdot(zs[a],gy)
            for i,(expr,path) in enumerate(back):
                args=[gy*np.conj(cs[a])]+[mats[a][j].conj() for j in range(n) if j!=i]
                g=np.einsum(expr,*args,optimize=path).ravel();f=mats[a][i].ravel()
                gm[a,i]=(g-f*np.vdot(f,g).real)/norms[a,i]
        gc=(gc-cs*np.vdot(cs,gc).real)/cn
        g=np.concatenate((gm.ravel(),gc));return loss,np.concatenate((g.real,g.imag))
    probe=rng.normal(size=2*nc);loss,g=evaluate(probe);errors=[]
    for j in rng.choice(2*nc,6,replace=False):
        xp=probe.copy();xm=probe.copy();xp[j]+=1e-5;xm[j]-=1e-5
        fd=(evaluate(xp)[0]-evaluate(xm)[0])/(2e-5);errors.append(abs(fd-g[j]))
    assert max(errors)<1e-7,max(errors)
    setup=dict(config=cfg,gradient_max_error=max(errors),target_shape=outdims,
               target_nonzeros=int(np.count_nonzero(target)),forward_expression=forward)
    print(json.dumps(setup),flush=True);runs=[];best=1.
    for trial in range(cfg['restarts']):
        x=rng.normal(size=2*nc);start=time.monotonic()
        result=minimize(evaluate,x,jac=True,method='L-BFGS-B',
                        options=dict(maxiter=cfg['maxiter'],maxls=40,maxcor=25,gtol=1e-10,ftol=1e-14))
        stats,mats,cs=evaluate(result.x,False)
        stats.update(trial=trial,nit=int(result.nit),nfev=int(result.nfev),
                     message=str(result.message),seconds=time.monotonic()-start)
        runs.append(stats);print(json.dumps(stats),flush=True)
        if stats['loss']<best:
            best=stats['loss'];save={'target':target,'coefficients':cs,'parameters':result.x}
            for a in range(A):
                for i in range(n):save[f'map_{a}_{i}']=mats[a][i]
            np.savez_compressed(str(base)+'_best.npz',**save)
        Path(str(base)+'_summary.json').write_text(json.dumps(setup|dict(runs=runs,best_loss=best,
            scope='Exploratory local search only; no exact or border cover certified.'),indent=2))


if __name__=='__main__':main()
