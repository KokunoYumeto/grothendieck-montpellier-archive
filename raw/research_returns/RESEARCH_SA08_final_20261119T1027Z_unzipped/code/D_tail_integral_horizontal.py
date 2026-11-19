#!/usr/bin/env python3
"""Integral normalized horizontal homology of the form-one tail image.

For each multidegree, generators are a df.  A variable missing from a
multidegree is exactly a degeneracy, so projecting to full support computes
the actual normalized quotient of the image lattice, not its reduction.
"""
from math import comb
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,time
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.domains import ZZ
started=time.perf_counter()

@lru_cache(None)
def compositions(w,n):
    if n==1:return ((w,),)
    return tuple((a,)+b for a in range(w+1) for b in compositions(w-a,n-1))

def multidegrees(w,n):
    if n>w:return []
    return [(x[0],)+tuple(a+1 for a in x[1:]) for x in compositions(w-n,n+1)]

@lru_cache(None)
def block(alpha,N):
    n=len(alpha)-1;w=sum(alpha);cols=[]
    for a in product(*(range(x+1) for x in alpha)):
        aw=sum(a)
        if w-aw<N:continue
        if aw<N and any(a[1:]):continue
        f=tuple(x-y for x,y in zip(alpha,a));v=[]
        for j in range(1,n+1):
            if not f[j]:v.append(0);continue
            c=1
            for i in range(n+1):c*=comb(alpha[i]-(i==j),a[i])
            v.append(c)
        if any(v):cols.append(v)
    return hermite_normal_form(sp.Matrix(n,len(cols),lambda i,j:cols[j][i])) if cols else sp.zeros(n,0)

@lru_cache(None)
def basis(w,n,N):
    alphas=multidegrees(w,n);blocks=[block(a,N) for a in alphas]
    rows=[];offset=0
    for a,B in zip(alphas,blocks):
        rows.append((a,B,offset));offset+=B.cols
    return rows,offset

def face_term(alpha,j,n,i):
    # alpha counts the differential in coordinate j.
    exps=list(alpha);exps[j]-=1
    def target(t):
        if t==0:return 0
        if i==0:return 0 if t==1 else t-1
        if i==n:return None if t==n else t
        return t if t<=i else t-1
    jj=target(j)
    if jj in (None,0):return None
    out=[0]*n;c=(-1)**i
    for t,a in enumerate(exps):
        if not a:continue
        z=target(t)
        if z is None:return None
        c*=comb(out[z]+a,a);out[z]+=a
    out[jj]+=1
    if any(x==0 for x in out[1:]):return None
    return tuple(out),jj,c

def differential(w,n,N):
    source,ns=basis(w,n,N)
    if n<=1:return sp.zeros(0,ns)
    target,nt=basis(w,n-1,N);target_map={a:(B,o) for a,B,o in target}
    D=sp.zeros(nt,ns)
    for alpha,B,offset in source:
        by_target={}
        for j in range(1,n+1):
            for i in range(n+1):
                z=face_term(alpha,j,n,i)
                if z is None:continue
                beta,jj,c=z
                if beta not in by_target:by_target[beta]=sp.zeros(n-1,B.cols)
                by_target[beta][jj-1,:]+=c*B[j-1,:]
        for beta,V in by_target.items():
            C,o=target_map[beta]
            X=C.gauss_jordan_solve(V)[0]
            assert all(x.q==1 for x in X),(w,n,N,alpha,beta,X)
            D[o:o+C.cols,offset:offset+B.cols]+=X
    return D

rows=[]
for N in [2,3]:
  for w in range(N,8):
    ds={n:differential(w,n,N) for n in range(1,min(w,4)+1)}
    for n in range(2,min(w,4)+1):
        assert ds[n-1]*ds[n]==sp.zeros(ds[n-1].rows,ds[n].cols)
    hom={}
    for n in range(1,min(w,3)+1):
        d=ds[n];nex=ds.get(n+1,sp.zeros(d.cols,0))
        S=smith_normal_form(nex,domain=ZZ)
        diag=[abs(int(S[j,j])) for j in range(min(S.shape)) if S[j,j]]
        free=d.cols-d.to_DM().rank()-len(diag)
        tors=[x for x in diag if x>1]
        hom[n]={'free':free,'torsion':tors}
    row={'N':N,'weight':w,'normalized_ranks':{n:ds[n].cols for n in ds},'homology':hom}
    rows.append(row)
    Path('SA08_work/logs/D_tail_integral_horizontal.json').write_text(json.dumps({'description':__doc__,'cases':rows,'elapsed_seconds':time.perf_counter()-started},indent=2)+'\n')
    print(json.dumps(row),flush=True)
out={'description':__doc__,'cases':rows,'elapsed_seconds':time.perf_counter()-started}
Path('SA08_work/logs/D_tail_integral_horizontal.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cases':len(rows),'elapsed_seconds':out['elapsed_seconds']}))
