"""Exact small checks of the enhanced padded Fermat moment map/stabilizer.
These supplement, and do not replace, the uniform proof of G16.
"""
from math import factorial,comb
from pathlib import Path
import json
import sympy as sp


def run(m,n):
    a=n-m;zero=(0,0,0,0);aux=(a,0,0,0);w={}
    for i in range(4):
        beta=[0]*4;beta[0]=a;beta[i]+=m
        w[(tuple(beta),aux)]=1 if i==0 else sp.sqrt(comb(n,m))
    def add(out,key,val):out[key]=sp.simplify(out.get(key,0)+val)
    def act(i,j):
        out={}
        for (b,c),v in w.items():
            if b[j]:
                z=list(b);z[j]-=1;z[i]+=1;add(out,(tuple(z),c),b[j]*v)
            if c[i]:
                z=list(c);z[i]-=1;z[j]+=1;add(out,(b,tuple(z)),-c[i]*v)
        return {k:v for k,v in out.items() if v!=0}
    def normkey(key):
        b,c=key
        return sp.Rational(sp.prod(factorial(x) for x in b),factorial(n))*sp.Rational(sp.prod(factorial(x) for x in c),factorial(a))
    def inner(u,v):return sp.simplify(sum(sp.conjugate(x)*v.get(k,0)*normkey(k) for k,x in u.items()))
    columns=[]
    for i in range(4):
      for j in range(4):
        if i!=j:columns.append(act(i,j))
    for i in range(3):
        p=act(i,i);q=act(i+1,i+1)
        columns.append({k:sp.simplify(p.get(k,0)-q.get(k,0)) for k in set(p)|set(q)})
    moments=[inner(w,c) for c in columns]
    assert all(v==0 for v in moments)
    assert inner(w,w)==4
    keys=sorted(set(w).union(*(set(c) for c in columns)))
    M=sp.Matrix([[c.get(k,0) for c in columns] for k in keys])
    affine_rank=M.rank()
    augmented_rank=M.row_join(sp.Matrix([w.get(k,0) for k in keys])).rank()
    assert (affine_rank,augmented_rank)==(15,16)
    return {'m':m,'n':n,'a':a,'norm_squared':4,'all15_moments_zero':True,
            'Lie_orbit_rank':affine_rank,'Lie_orbit_plus_tensor_rank':augmented_rank}

results=[run(m,n) for m,n in [(3,4),(4,8),(5,11)]]
Path(__file__).with_name('enhanced_padding_check.json').write_text(json.dumps({'all_passed':True,'results':results},indent=2)+'\n')
print(json.dumps({'all_passed':True,'cases':results}))
