#!/usr/bin/env python3
"""Exhaustive finite 3-local lattice test for the broader numerical lift gate.

The modules are embedded in Q[T], bottom vector 1.  gr M_i=I_i
forces characteristic leading-coefficient ideals i!/(n+i)! in degree n.
Relative to the binomial basis beta_n the new lattice index is C(n+i,i).
This enumerates every such filtered Z_(3)-lattice through weight 5 (i=1)
or 6 (i=2), including all lower coefficient choices modulo 3. It checks
all R-actions staying within the degree cutoff and all pairings whose
total weight is at most6. It does not assume evaluation-ideal form.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
import json,time
start=time.perf_counter()
p=3
checks=0

def vp(x):
    if not x:return 999
    x=F(x);a=x.numerator;b=x.denominator;v=0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v

def mul(x,y):
    z=[F(0)]*(len(x)+len(y)-1)
    for a,u in enumerate(x):
      for b,v in enumerate(y):
        if not u or not v:continue
        for c in range(max(a,b),a+b+1):
          coefficient=factorial(c)//(factorial(c-a)*factorial(c-b)*factorial(a+b-c))
          z[c]+=u*v*coefficient
    return z

def member(x,basis):
    global checks
    checks+=1
    z=list(x)+[F(0)]*max(0,len(basis)-len(x))
    if len(z)>len(basis) and any(z[len(basis):]):return False
    for n in range(min(len(z),len(basis))-1,-1,-1):
        a=z[n]/basis[n][n]
        if vp(a)<0:return False
        for j in range(n+1):z[j]-=a*basis[n][j]
    return True

def generate(i,D):
    bs=[[]]
    counts=[]
    for n in range(D+1):
        e=vp(comb(n+i,i));index=p**e
        nxt=[]
        for B in bs:
            for aa in product(range(index),repeat=n):
                v=[F(0)]*(n+1);v[n]=F(1,index)
                for j,a in enumerate(aa):
                    for k,c in enumerate(B[j]):v[k]+=F(a,index)*c
                C=B+[v]
                good=True
                for j,u in enumerate(C):
                    for a in range(1,n-j+1):
                        beta=[F(0)]*a+[F(1)]
                        if not member(mul(u,beta),C):good=False;break
                    if not good:break
                if good:nxt.append(C)
        bs=nxt;counts.append(len(bs))
    return bs,counts

B1,ct1=generate(1,4)
B2,ct2=generate(2,4)
assert ct1==[1,1,9,3,3]
assert ct2==[1,3,3,3,3]
compatible=[]
for a,A in enumerate(B1):
  for b,B in enumerate(B2):
    good=True
    for n,u in enumerate(A):
      for m,v in enumerate(A):
        if n+m>4:continue
        # Scalar2 is a 3-local unit, so it does not alter membership.
        if not member(mul(u,v),B):good=False;break
      if not good:break
    if good:compatible.append((a,b))
assert not compatible

def enc(B):return [[str(c) for c in v] for v in B]
out={'prime':p,'M1_weight_cutoff':5,'M2_weight_cutoff':6,
     'M1_counts_by_degree':ct1,'M2_counts_by_degree':ct2,
     'M1_bases':[enc(b) for b in B1],
     'M2_bases':[enc(b) for b in B2],
     'compatible_pair_indices':compatible,'membership_checks':checks,
     'elapsed_seconds':time.perf_counter()-start,
     'description':__doc__}
target=Path('SA08_work/logs/D_filtered_lattice_gate.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['M1_counts_by_degree','M2_counts_by_degree',
  'compatible_pair_indices','membership_checks','elapsed_seconds']}))
