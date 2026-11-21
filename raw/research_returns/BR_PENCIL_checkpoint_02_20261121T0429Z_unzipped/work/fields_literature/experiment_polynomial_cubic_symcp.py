#!/usr/bin/env python3
"""Exploratory partial-symmetric CP fits; never a proof or certificate."""
from itertools import combinations_with_replacement
from pathlib import Path
from math import factorial
import json,sys,time
import numpy as np
from scipy.optimize import least_squares

HERE=Path(__file__).resolve().parent
MON=np.array(list(combinations_with_replacement(range(12),3)),dtype=int)
N=len(MON)
WEIGHT=np.array([np.sqrt(factorial(3)/np.prod([factorial(list(m).count(j)) for j in set(m)])) for m in MON])

def parity(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))

TARGET=np.zeros((2,N))
for a in range(2):
    for m,word in enumerate(MON):
        rows=tuple(j//4 for j in word);cols=tuple(j%4 for j in word)
        if set(rows)=={0,1,2} and set(cols)=={0,1,2+a}:TARGET[a,m]=parity(rows)*parity(cols)

def setup(rank):
    def unpack(x):return x[:2*rank].reshape((2,rank)),x[2*rank:].reshape((12,rank))
    def residual(x):
        A,V=unpack(x);P=np.prod(V[MON],axis=1)
        return ((A@P.T-TARGET)*WEIGHT).ravel()
    def jacobian(x):
        A,V=unpack(x);P=np.prod(V[MON],axis=1)
        D=np.zeros((N,12,rank))
        for h in range(3):
            value=V[MON[:,(h+1)%3]]*V[MON[:,(h+2)%3]]
            D[np.arange(N),MON[:,h]]+=value
        JA=np.zeros((2,N,2,rank));JA[0,:,0,:]=P;JA[1,:,1,:]=P
        JV=np.einsum('ar,mir->amir',A,D)
        return np.concatenate([(JA*WEIGHT[None,:,None,None]).reshape((2*N,2*rank)),
                               (JV*WEIGHT[None,:,None,None]).reshape((2*N,12*rank))],axis=1)
    return unpack,residual,jacobian

def initial(t):
    data=json.loads((HERE/'polynomial_cubic_upper_certificate.json').read_text())['det']['atoms']
    A=np.zeros((2,len(data)));V=np.zeros((12,len(data)))
    for r,atom in enumerate(data):
        A[:,r]=np.array(atom['first_factor'])*atom['scalar_coefficient']*t**atom['scalar_degree']
        for coordinate,degree,value in atom['vector']:V[coordinate,r]+=value*t**degree
    for r in range(len(data)):
        an=np.linalg.norm(A[:,r]);vn=np.linalg.norm(V[:,r]);balanced=(an*vn**3)**.25
        A[:,r]*=balanced/an;V[:,r]*=balanced/vn
    return A,V

def main():
    rank=int(sys.argv[1]) if len(sys.argv)>1 else 29
    seeds=int(sys.argv[2]) if len(sys.argv)>2 else 3
    unpack,fun,jac=setup(rank);rng=np.random.default_rng(20261121);results=[];start=time.time()
    for seed in range(seeds):
        if rank==29:
            A,V=initial(.35+.1*(seed%3));drop=(seed*6)%30
            A=np.delete(A,drop,axis=1);V=np.delete(V,drop,axis=1)
            A+=rng.normal(size=A.shape)*.002;V+=rng.normal(size=V.shape)*.002
        else:A=rng.normal(size=(2,rank))*.4;V=rng.normal(size=(12,rank))*.4
        x=np.concatenate((A.ravel(),V.ravel()))
        fit=least_squares(fun,x,jac=jac,method='lm',max_nfev=1500,ftol=1e-12,xtol=1e-12,gtol=1e-12)
        A,V=unpack(fit.x)
        rec={'rank':rank,'seed':seed,'residual':float(np.linalg.norm(fun(fit.x))),
             'max_factor':float(max(np.max(abs(A)),np.max(abs(V)))),
             'nfev':fit.nfev,'seconds':time.time()-start,'A':A.tolist(),'V':V.tolist()}
        results.append(rec)
        (HERE/f'experiment_polynomial_cubic_sym{rank}.json').write_text(json.dumps(results,indent=2)+'\n')
        print({k:v for k,v in rec.items() if k not in ('A','V')},flush=True)
        if rec['residual']<1e-9:break

if __name__=='__main__':main()
