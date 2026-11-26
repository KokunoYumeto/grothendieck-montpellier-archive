#!/usr/bin/env python3
"""Exploratory complex covers of K3(q)*K2(q) from K32(q).

Uses the six-edge factorization, avoiding a dense source tensor.
No floating-point result is an identity certificate.
"""
import itertools
import json
import sys
import time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize


def main():
    cfg=json.loads(Path(sys.argv[1]).read_text());base=Path(sys.argv[2])
    q,A=cfg['wire_dimension'],cfg['terms']
    target=np.zeros((q*q,)*3+(q,)*2,dtype=complex)
    for x,y,z,u in itertools.product(range(q),repeat=4):
        target[x*q+y,x*q+z,y*q+z,u,u]=1
    shape=[(q*q,q,q)]*3+[(q,q,q,q)]*2
    size=q**4;nc=A*(5*size+1);tn=float(np.vdot(target,target).real)
    rng=np.random.default_rng(cfg['seed'])
    factors=['iab','jcd','kef','uace','vbdf'];forward=','.join(factors)+'->ijkuv'
    samples=[np.zeros(s,complex) for s in shape]
    fpath=np.einsum_path(forward,*samples,optimize='optimal')[0]
    back=[]
    for i in range(5):
        expr='ijkuv,'+','.join(factors[j] for j in range(5) if j!=i)+'->'+factors[i]
        args=[np.zeros_like(target)]+[samples[j] for j in range(5) if j!=i]
        back.append((expr,np.einsum_path(expr,*args,optimize='optimal')[0]))
    def unpack(x):
        z=x[:nc]+1j*x[nc:];raw=z[:A*5*size].reshape(A,5,size)
        norms=np.linalg.norm(raw,axis=2)
        mats=[[raw[a,i].reshape(shape[i])/norms[a,i] for i in range(5)] for a in range(A)]
        cr=z[A*5*size:];cn=np.linalg.norm(cr);cs=cr/cn
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
                args=[gy*np.conj(cs[a])]+[mats[a][j].conj() for j in range(5) if j!=i]
                g=np.einsum(expr,*args,optimize=path).ravel();f=mats[a][i].ravel()
                gm[a,i]=(g-f*np.vdot(f,g).real)/norms[a,i]
        gc=(gc-cs*np.vdot(cs,gc).real)/cn
        g=np.concatenate((gm.ravel(),gc));return loss,np.concatenate((g.real,g.imag))
    probe=rng.normal(size=2*nc);loss,g=evaluate(probe);errors=[]
    for j in rng.choice(2*nc,8,replace=False):
        xp=probe.copy();xm=probe.copy();xp[j]+=1e-5;xm[j]-=1e-5
        fd=(evaluate(xp)[0]-evaluate(xm)[0])/(2e-5);errors.append(abs(fd-g[j]))
    assert max(errors)<1e-7,max(errors)
    setup=dict(config=cfg,gradient_max_error=max(errors),target_nonzeros=int(np.count_nonzero(target)))
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
                for i in range(5):save[f'map_{a}_{i}']=mats[a][i]
            np.savez_compressed(str(base)+'_best.npz',**save)
        Path(str(base)+'_summary.json').write_text(json.dumps(setup|dict(runs=runs,best_loss=best,
            scope='Exploratory local search only; no exact or border cover certified.'),indent=2))


if __name__=='__main__':main()
