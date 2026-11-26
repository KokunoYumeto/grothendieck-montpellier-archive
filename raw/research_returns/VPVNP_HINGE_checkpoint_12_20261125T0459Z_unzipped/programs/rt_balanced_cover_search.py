#!/usr/bin/env python3
"""Normalized dense complex K33 covers; every numerical result is exploratory."""
from pathlib import Path
import json, sys, time
import numpy as np
from scipy.optimize import minimize
from sh_border_k33_search import graph_tensors

cfg=json.loads(Path(sys.argv[1]).read_text())
out=Path(sys.argv[2])
q,A=cfg['wire_dimension'],cfg['terms']
h=q*q; d=h*h; sz=h*h*q
src,target=graph_tensors(q)
tn=float(np.vdot(target,target).real)
nc=A*(6*sz+1)
rng=np.random.default_rng(cfg['seed'])

def unpack(x):
    z=x[:nc]+1j*x[nc:]
    raw=z[:A*6*sz].reshape(A,3,2,sz)
    norms=np.linalg.norm(raw,axis=-1)
    p=(raw/norms[...,None]).reshape(A,3,2,h,h,q)
    cr=z[A*6*sz:]; cn=np.linalg.norm(cr); c=cr/cn
    return raw,norms,p,cr,cn,c

def evaluate(x,gradient=True):
    raw,norms,p,cr,cn,c=unpack(x)
    fs=[[np.einsum('acx,bdx->abcd',p[a,i,0],p[a,i,1],optimize=True).reshape(d,d)
         for i in range(3)] for a in range(A)]
    zs=[np.einsum('ai,bj,ck,ijk->abc',*f,src,optimize=True) for f in fs]
    y=sum(ca*z for ca,z in zip(c,zs))
    ov=np.vdot(target,y); yn=float(np.vdot(y,y).real)
    if yn<=1e-290:
        return (1.,np.zeros_like(x)) if gradient else ({'loss':1.,'output_norm2':yn},p,c)
    loss=1-float(abs(ov)**2/(yn*tn))
    if not gradient:
        return {'loss':loss,'fidelity':1-loss,'output_norm2':yn,
                'cancellation_ratio':float(sum(abs(ca)*np.linalg.norm(z) for ca,z in zip(c,zs))/np.sqrt(yn))},p,c
    gy=2*(abs(ov)**2*y-yn*ov*target)/(yn*yn*tn)
    gp=np.zeros_like(p);gc=np.zeros(A,dtype=complex)
    for a in range(A):
        g=gy*np.conj(c[a]); f=fs[a]
        gf=[np.einsum('abc,bj,ck,ijk->ai',g,f[1].conj(),f[2].conj(),src,optimize=True),
            np.einsum('abc,ai,ck,ijk->bj',g,f[0].conj(),f[2].conj(),src,optimize=True),
            np.einsum('abc,ai,bj,ijk->ck',g,f[0].conj(),f[1].conj(),src,optimize=True)]
        for i in range(3):
            gg=gf[i].reshape(h,h,h,h)
            gp[a,i,0]=np.einsum('abcd,bdx->acx',gg,p[a,i,1].conj(),optimize=True)
            gp[a,i,1]=np.einsum('abcd,acx->bdx',gg,p[a,i,0].conj(),optimize=True)
        gc[a]=np.vdot(zs[a],gy)
    projected=gp.reshape(A,3,2,sz)
    normalized=p.reshape(A,3,2,sz)
    radial=np.real(np.sum(normalized.conj()*projected,axis=-1))
    projected=(projected-normalized*radial[...,None])/norms[...,None]
    gc=(gc-c*np.vdot(c,gc).real)/cn
    gradient=np.concatenate((projected.ravel(),gc))
    return loss,np.concatenate((gradient.real,gradient.imag))

probe=rng.normal(size=2*nc)
loss,g=evaluate(probe)
errors=[]
for j in rng.choice(2*nc,size=12,replace=False):
    xp=probe.copy();xm=probe.copy();xp[j]+=1e-5;xm[j]-=1e-5
    fd=(evaluate(xp)[0]-evaluate(xm)[0])/(2e-5)
    errors.append(abs(fd-g[j]))
assert max(errors)<1e-7,max(errors)
setup={'config':cfg,'gradient_max_error':max(errors),'target_nonzeros':int(np.count_nonzero(target))}
print(json.dumps(setup),flush=True)
runs=[]; best=1.
for trial in range(cfg['restarts']):
    x=rng.normal(size=2*nc)
    start=time.monotonic()
    res=minimize(evaluate,x,jac=True,method='L-BFGS-B',
                 options={'maxiter':cfg['maxiter'],'maxls':50,'maxcor':30,'ftol':1e-15,'gtol':1e-11})
    metrics,maps,coeff=evaluate(res.x,False)
    metrics.update({'trial':trial,'nit':int(res.nit),'nfev':int(res.nfev),
                    'message':str(res.message),'seconds':time.monotonic()-start})
    runs.append(metrics);print(json.dumps(metrics),flush=True)
    if metrics['loss']<best:
        best=metrics['loss']
        np.savez_compressed(str(out)+'_best.npz',maps=maps,coefficients=coeff,
                            raw_parameters=res.x,source=src,target=target)
    Path(str(out)+'_summary.json').write_text(json.dumps(setup|{'runs':runs,'best_loss':best,
        'scope':'Exploratory finite local optimization only; no exact or border identity or impossibility certified.'},indent=2)+'\n')
