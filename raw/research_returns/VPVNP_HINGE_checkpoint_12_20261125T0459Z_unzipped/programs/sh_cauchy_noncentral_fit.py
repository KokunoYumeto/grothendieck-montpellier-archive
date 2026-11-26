"""Bounded construction attempt on the FULL all-spin1/2 sector for r4.

Every local map is an arbitrary2x2 multiplicity matrix, identically on
both spin weights.  Two terms per crown class are fitted.  A numerical
residual is never an identity or an impossibility certificate.
"""
from pathlib import Path
import hashlib,itertools,json,time
import numpy as np

W=Path(__file__).resolve().parents[1]
ip=W/'inputs/sh_cauchy_noncentral_fit.json';cfg=json.loads(ip.read_text())
rng=np.random.default_rng(cfg['seed'])
ports=[tuple(j for j in range(4)if j!=i)for i in range(4)]
local={1:[(0,1)],2:[(0,-1),(1,1)],4:[(1,-1)],
       6:[(2,1)],5:[(2,-1),(3,1)],3:[(3,-1)]}

def target_edges():
    return [(s+i,ports[i].index(j),s+j,ports[j].index(i))
            for s in(0,4)for i in range(4)for j in range(i+1,4)]

def crown_edges(p):
    return [(i,ports[i].index(j),4+p[j],ports[p[j]].index(p[i]))
            for i in range(4)for j in range(4)if i!=j]

def project(edges):
    ans=np.zeros(4**8,dtype=np.int32)
    for word in range(1<<12):
        masks=[0]*8;sign=1
        for e,(u,a,v,b)in enumerate(edges):
            bit=(word>>e)&1;masks[u]|=bit<<a;masks[v]|=(1-bit)<<b
            if bit:sign=-sign
        opts=[local.get(x)for x in masks]
        if any(x is None for x in opts):continue
        terms=[(0,sign)]
        for i,row in enumerate(opts):
            terms=[(z+(choice<<(2*i)),c*s)for z,c in terms for choice,s in row]
        for z,c in terms:ans[z]+=c
    return ans.reshape((4,)*8,order='F').copy()

perms=list(itertools.permutations(range(4)))
target=project(target_edges());crowns=np.stack([project(crown_edges(p))for p in perms])
np.savez_compressed(W/'inputs/sh_cauchy_all_mixed_sector_arrays.npz',target=target,crowns=crowns)
h=target.astype(float);norm=np.sum(h*h)
indices=np.repeat(np.arange(24),cfg['terms_per_matching']);A=len(indices)
base=crowns[indices].astype(float)
raw=rng.normal(size=(A,8,2,2));alpha=rng.normal(size=A)*0.01

def apply_axis(x,M,v):
    moved=np.moveaxis(x,v+1,-1)
    y=np.matmul(moved.reshape(A,-1,4),np.swapaxes(M,1,2)).reshape(moved.shape)
    return np.moveaxis(y,-1,v+1)

def evaluate(raw,alpha,gradient=True):
    norms=np.sqrt(np.sum(raw*raw,axis=(-1,-2),keepdims=True)+1e-30)
    mats=raw/norms*2**0.5
    history=[base];m4=[]
    for v in range(8):
        M=np.zeros((A,4,4));M[:,:2,:2]=mats[:,v];M[:,2:,2:]=mats[:,v]
        m4.append(M);history.append(apply_axis(history[-1],M,v))
    terms=history[-1];prediction=np.einsum('a,a...->...',alpha,terms)
    residual=prediction-h;value=float(np.sum(residual*residual)/norm)
    if not gradient:return value,mats
    ga=2*np.sum(terms*residual,axis=tuple(range(1,9)))/norm
    gy=2*alpha.reshape((A,)+(1,)*8)*residual/norm;gm=np.zeros_like(raw)
    for v in range(7,-1,-1):
        xx=np.moveaxis(history[v],v+1,-1).reshape(A,-1,4)
        yy=np.moveaxis(gy,v+1,-1).reshape(A,-1,4)
        dM=np.matmul(np.swapaxes(yy,1,2),xx)
        gm[:,v]=dM[:,:2,:2]+dM[:,2:,2:]
        gy=apply_axis(gy,np.swapaxes(m4[v],1,2),v)
    gr=2**0.5/norms*(gm-raw*np.sum(gm*raw,axis=(-1,-2),keepdims=True)/(norms*norms))
    return value,gr,ga,mats

value,gr,ga,_=evaluate(raw,alpha);eps=1e-5;errs=[]
for which in ('raw','alpha'):
    rr=raw.copy();aa=alpha.copy()
    if which=='raw':rr[0,0,0,0]+=eps
    else:aa[0]+=eps
    plus=evaluate(rr,aa,False)[0]
    if which=='raw':rr[0,0,0,0]-=2*eps
    else:aa[0]-=2*eps
    minus=evaluate(rr,aa,False)[0]
    errs.append(abs((plus-minus)/(2*eps)-(gr[0,0,0,0]if which=='raw'else ga[0])))
assert max(errs)<1e-6,errs
moment=[np.zeros_like(raw),np.zeros_like(alpha)];variance=[np.zeros_like(raw),np.zeros_like(alpha)]
start=time.time();best=float('inf');trace=[];best_data=None
for step in range(cfg['steps']):
    value,gr,ga,mats=evaluate(raw,alpha)
    if value<best:
        best=value;best_data={'maps':mats.copy(),'coefficients':alpha.copy(),'matching_indices':indices}
    for j,(param,grad)in enumerate(((raw,gr),(alpha,ga))):
        moment[j]=.9*moment[j]+.1*grad;variance[j]=.999*variance[j]+.001*grad*grad
        param-=cfg['learning_rate']*(moment[j]/(1-.9**(step+1)))/(np.sqrt(variance[j]/(1-.999**(step+1)))+1e-8)
    if step%10==0:
        rec={'step':step,'seconds':time.time()-start,'relative_squared_residual':value,'best':best}
        trace.append(rec);print(json.dumps(rec),flush=True)
    if time.time()-start>=cfg['time_limit_seconds']:break
np.savez_compressed(W/'outputs/sh_cauchy_noncentral_fit_best.npz',**best_data)
out={'status':'BOUNDED NUMERICAL CONSTRUCTION ATTEMPT ONLY; no exact identity or nonexistence conclusion',
     'input_sha256':hashlib.sha256(ip.read_bytes()).hexdigest(),'terms':A,'steps_completed':step+1,
     'seconds':time.time()-start,'best_relative_squared_residual':best,'trace':trace,
     'gradient_finite_difference_errors':errs,
     'scope':'full all-spin1/2 sector, including every spin-weight component; arbitrary noncentral2x2 multiplicity maps; other sectors not included'}
p=W/cfg['output'];tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,separators=(',',':'))+'\n');tmp.replace(p)
print(json.dumps({k:v for k,v in out.items()if k!='trace'},indent=2))
