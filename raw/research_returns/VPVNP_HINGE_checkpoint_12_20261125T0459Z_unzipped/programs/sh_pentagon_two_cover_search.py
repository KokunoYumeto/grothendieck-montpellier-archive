#!/usr/bin/env python3
"""Exploratory complex few-term covers K3,2(q) -> K3(q) x EPR(q).

Numerical overlap alone never certifies an identity.  All best local
tables are preserved for possible subsequent exact reconstruction.
"""
import itertools
import json
import sys
import time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize


def tensors(q):
    source=np.zeros((q*q,)*3+(q**3,)*2,dtype=complex)
    target=np.zeros((q*q,)*3+(q,)*2,dtype=complex)
    for v in itertools.product(range(q),repeat=6):
        L=tuple(v[2*i]*q+v[2*i+1] for i in range(3))
        R=((v[0]*q+v[2])*q+v[4],(v[1]*q+v[3])*q+v[5])
        source[L+R]=1
    for a,b,c,z in itertools.product(range(q),repeat=4):
        target[a*q+b,a*q+c,b*q+c,z,z]=1
    return source,target


def main():
    cfg=json.loads(Path(sys.argv[1]).read_text());base=Path(sys.argv[2])
    q,A=cfg['wire_dimension'],cfg['terms'];src,target=tensors(q)
    ins=[q*q]*3+[q**3]*2;outs=[q*q]*3+[q]*2
    size=q**4;nc=A*(5*size+1);target_n=float(np.vdot(target,target).real)
    rng=np.random.default_rng(cfg['seed'])
    forward='ai,bj,ck,dl,em,ijklm->abcde'
    sample=[np.zeros((o,i),complex) for o,i in zip(outs,ins)]
    fpath=np.einsum_path(forward,*sample,src,optimize='greedy')[0]
    terms=['ai','bj','ck','dl','em'];back=[]
    for i in range(5):
        expr='abcde,'+','.join(terms[j] for j in range(5) if j!=i)+',ijklm->'+terms[i]
        args=[np.zeros_like(target)]+[sample[j] for j in range(5) if j!=i]+[src]
        back.append((expr,np.einsum_path(expr,*args,optimize='greedy')[0]))
    def unpack(x):
        z=x[:nc]+1j*x[nc:]
        raw=z[:A*5*size].reshape(A,5,size)
        norms=np.linalg.norm(raw,axis=2)
        mats=[[raw[a,i].reshape(outs[i],ins[i])/norms[a,i] for i in range(5)] for a in range(A)]
        cr=z[A*5*size:];cn=np.linalg.norm(cr);cs=cr/cn
        return raw,norms,mats,cr,cn,cs
    def evaluate(x,gradient=True):
        raw,norms,mats,cr,cn,cs=unpack(x)
        zs=[np.einsum(forward,*ms,src,optimize=fpath) for ms in mats]
        y=sum(c*z for c,z in zip(cs,zs));ov=np.vdot(target,y);yn=float(np.vdot(y,y).real)
        fid=float(abs(ov)**2/(yn*target_n));loss=1-fid
        if not gradient:
            return dict(loss=loss,fidelity=fid,output_norm2=yn,
                        cancellation_ratio=float(sum(abs(c)*np.linalg.norm(z) for c,z in zip(cs,zs))/np.sqrt(yn)),
                        parameter_norm=float(np.linalg.norm(x))),mats,cs
        gy=2*(abs(ov)**2*y-yn*ov*target)/(yn*yn*target_n)
        gm=np.zeros_like(raw);gc=np.empty(A,dtype=complex)
        for a in range(A):
            gc[a]=np.vdot(zs[a],gy)
            for i,(expr,path) in enumerate(back):
                args=[gy*np.conj(cs[a])]+[mats[a][j].conj() for j in range(5) if j!=i]+[src]
                g=np.einsum(expr,*args,optimize=path).ravel()
                f=mats[a][i].ravel()
                gm[a,i]=(g-f*np.vdot(f,g).real)/norms[a,i]
        gc=(gc-cs*np.vdot(cs,gc).real)/cn
        g=np.concatenate((gm.ravel(),gc));return loss,np.concatenate((g.real,g.imag))
    probe=rng.normal(size=2*nc);loss,g=evaluate(probe);errors=[]
    for j in rng.choice(2*nc,12,replace=False):
        xp=probe.copy();xm=probe.copy();xp[j]+=1e-5;xm[j]-=1e-5
        fd=(evaluate(xp)[0]-evaluate(xm)[0])/(2e-5);errors.append(abs(fd-g[j]))
    assert max(errors)<1e-7,max(errors)
    runs=[];best=1.;setup=dict(config=cfg,source_nonzeros=int(np.count_nonzero(src)),
                              target_nonzeros=int(np.count_nonzero(target)),gradient_max_error=max(errors))
    print(json.dumps(setup),flush=True)
    for trial in range(cfg['restarts']):
        x=rng.normal(size=2*nc);start=time.monotonic()
        result=minimize(evaluate,x,jac=True,method='L-BFGS-B',
                        options=dict(maxiter=cfg['maxiter'],maxls=50,maxcor=30,gtol=1e-10,ftol=1e-15))
        stats,mats,cs=evaluate(result.x,False)
        stats.update(trial=trial,nit=int(result.nit),nfev=int(result.nfev),
                     message=str(result.message),seconds=time.monotonic()-start)
        runs.append(stats);print(json.dumps(stats),flush=True)
        if stats['loss']<best:
            best=stats['loss'];save={'source':src,'target':target,'coefficients':cs,'parameters':result.x}
            for a in range(A):
                for i in range(5):save[f'map_{a}_{i}']=mats[a][i]
            np.savez_compressed(str(base)+'_best.npz',**save)
        Path(str(base)+'_summary.json').write_text(json.dumps(setup|dict(runs=runs,best_loss=best,
            scope='Exploratory local search only; no exact or border cover certified.'),indent=2))


if __name__=='__main__':main()
