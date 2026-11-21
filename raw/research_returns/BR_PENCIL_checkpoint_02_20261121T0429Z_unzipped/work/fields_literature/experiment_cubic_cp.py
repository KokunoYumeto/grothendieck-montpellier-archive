#!/usr/bin/env python3
"""Exploratory floating-point CP fits; NOT a rank certificate."""
from pathlib import Path
import json,time,sys
import numpy as np
from scipy.optimize import least_squares
from adjacent_cubic import entries

DS=(2,4,4,4)
target=np.zeros(DS)
for ix,v in entries(-1).items():target[ix]=v

def setup(rank):
    splits=np.cumsum([0]+[d*rank for d in DS])
    def unpack(x):return [x[splits[i]:splits[i+1]].reshape((DS[i],rank)) for i in range(4)]
    def residual(x):return (np.einsum('ir,jr,kr,lr->ijkl',*unpack(x))-target).ravel()
    def jacobian(x):
        fs=unpack(x);blocks=[]
        for h in range(4):
            J=np.zeros(DS+(DS[h],rank))
            for i in range(DS[h]):
                for r in range(rank):
                    factors=[fs[j][:,r] if j!=h else np.eye(DS[h])[i] for j in range(4)]
                    J[...,i,r]=np.einsum('i,j,k,l->ijkl',*factors)
            blocks.append(J.reshape((np.prod(DS),DS[h]*rank)))
        return np.concatenate(blocks,axis=1)
    return unpack,residual,jacobian

def main():
    rank=int(sys.argv[1]) if len(sys.argv)>1 else 8
    maxseeds=int(sys.argv[2]) if len(sys.argv)>2 else 8
    unpack,fun,jac=setup(rank)
    rng=np.random.default_rng(20261121)
    known=json.loads(Path(__file__).with_name('adjacent_det9_upper.json').read_text())
    old=[np.array([a['factors'][h] for a in known['atoms']],dtype=float).T for h in range(4)]
    old[0]*=np.array([a['numerator']/2 for a in known['atoms']])[None,:]
    results=[];start=time.time()
    for seed in range(maxseeds):
        if seed<9 and rank==8:
            fs=[np.delete(f,seed,axis=1) for f in old]
            for f in fs:f+=rng.normal(size=f.shape)*.03
        else:fs=[rng.normal(size=(d,rank))*.7 for d in DS]
        x=np.concatenate([f.ravel() for f in fs])
        res=least_squares(fun,x,jac=jac,method='lm',max_nfev=3000,ftol=1e-13,xtol=1e-13,gtol=1e-13)
        f=unpack(res.x)
        rec={'rank':rank,'seed':seed,'residual_norm':float(np.linalg.norm(fun(res.x))),'largest_factor':float(max(np.max(np.abs(v)) for v in f)),'evaluations':res.nfev,'seconds_total':time.time()-start,'factors':[v.tolist() for v in f]}
        results.append(rec)
        Path(__file__).with_name(f'experiment_cubic_cp{rank}.json').write_text(json.dumps(results,indent=2)+'\n')
        print({k:v for k,v in rec.items() if k!='factors'},flush=True)
        if rec['residual_norm']<1e-10:break

if __name__=='__main__':main()
