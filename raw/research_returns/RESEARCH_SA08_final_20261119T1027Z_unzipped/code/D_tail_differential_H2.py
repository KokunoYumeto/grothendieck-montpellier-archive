#!/usr/bin/env python3
"""Exact H2 tests for the form-one differential image of standard tails."""
from math import comb,factorial
from itertools import product
from functools import lru_cache
from pathlib import Path
import json,time
start=time.perf_counter()

@lru_cache(None)
def comp(w,n):
    if n==1:return ((w,),)
    return tuple((a,)+b for a in range(w+1) for b in comp(w-a,n-1))

@lru_cache(None)
def idx(w,n):
    return {(a,j):i for i,(a,j) in enumerate((a,j) for a in comp(w-1,n+1)
                                           for j in range(1,n+1))}

def gen(a,f,w,n,p):
    out=[0]*len(idx(w,n))
    for j in range(1,n+1):
        if not f[j]:continue
        b=list(f);b[j]-=1
        e=tuple(a[k]+b[k] for k in range(n+1))
        c=1
        for k in range(n+1):c*=comb(e[k],a[k])
        out[idx(w,n)[e,j]]=c%p
    return out

def face(e,n,i):
    out=[0]*n;c=1
    for j,a in enumerate(e):
        if not a:continue
        if j==0:t=0
        elif i==0:t=0 if j==1 else j-1
        elif i==n:
            if j==n:return 0,tuple(out)
            t=j
        else:t=j if j<=i else j-1
        c*=comb(out[t]+a,a);out[t]+=a
    return c,tuple(out)

def boundary(a,f,w,n,p):
    out=[0]*len(idx(w,n-1))
    for i in range(n+1):
        ca,aa=face(a,n,i);cf,ff=face(f,n,i)
        if not ca or not cf:continue
        v=gen(aa,ff,w,n-1,p)
        c=(-1)**i*ca*cf
        out=[(x+c*y)%p for x,y in zip(out,v)]
    return out

def insert(v,B,p):
    v=list(v)
    for j,b in sorted(B.items()):
        c=v[j]
        if c:v=[(a-c*z)%p for a,z in zip(v,b)]
    if not any(v):return False
    j=next(j for j,a in enumerate(v) if a)
    c=pow(v[j],-1,p);B[j]=[c*x%p for x in v]
    return True

def gens(N,w,n):
    for a in range(w-N+1):
        aa=comp(a,n+1) if a>=N else [(a,)+(0,)*n]
        for av in aa:
            for fv in comp(w-a,n+1):yield av,fv

rows=[]
for N in [2,3]:
  for p in [2,3,5]:
    for w in range(N,10):
        B2={};d2={}
        for a,f in gens(N,w,2):
            insert(gen(a,f,w,2,p),B2,p)
            insert(boundary(a,f,w,2,p),d2,p)
        kernel_dim=len(B2)-len(d2)
        d3={};count=0
        for a,f in gens(N,w,3):
            count+=1;insert(boundary(a,f,w,3,p),d3,p)
            if len(d3)==kernel_dim:break
        assert len(d3)<=kernel_dim
        rows.append({'N':N,'p':p,'weight':w,'dim_D2':len(B2),
                     'rank_d2':len(d2),'rank_d3':len(d3),
                     'H2_dimension':kernel_dim-len(d3),
                     'd3_generators_processed':count})
out={'cases':rows,'elapsed_seconds':time.perf_counter()-start,'description':__doc__}
Path('SA08_work/logs/D_tail_differential_H2.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'case_count':len(rows),'elapsed_seconds':out['elapsed_seconds'],
                  'nonzero':[r for r in rows if r['H2_dimension']]}))
