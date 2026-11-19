#!/usr/bin/env python3
"""Exact integral cohomology of three-variable multidegrees of D_N."""
from math import factorial
from itertools import product,combinations
from functools import lru_cache
from fractions import Fraction
from pathlib import Path
import json,time
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.domains import ZZ
start=time.perf_counter()
@lru_cache(None)
def comp(w,n):
 if n==1:return ((w,),)
 return tuple((a,)+b for a in range(w+1) for b in comp(w-a,n-1))
def lattice(alpha,q,N):
 s=len(alpha);wedges=list(combinations(range(s),q));columns=[]
 if q==0:return sp.eye(1)
 for aa in product(*(comp(a,q+1) for a in alpha)):
  wt=[sum(aa[i][j] for i in range(s)) for j in range(q+1)]
  if wt[0]!=0 and wt[0]<N:continue
  if any(w<N for w in wt[1:]):continue
  col=[]
  for J in wedges:
   A=sp.Matrix(q,q,lambda j,k:aa[J[k]][j+1])
   v=Fraction(int(A.det()),1)
   for i,a in enumerate(alpha):
    v*=factorial(a-(i in J))
    for x in aa[i]:v/=factorial(x)
   assert v.denominator==1
   col.append(v.numerator)
  if any(col):columns.append(col)
 if not columns:return sp.zeros(len(wedges),0)
 return hermite_normal_form(sp.Matrix(len(wedges),len(columns),lambda i,j:columns[j][i]))
def dmap(s,q):
 src=list(combinations(range(s),q));dst=list(combinations(range(s),q+1))
 D=sp.zeros(len(dst),len(src))
 for a,J in enumerate(src):
  for i in range(s):
   if i not in J:
    K=tuple(sorted(J+(i,)))
    D[dst.index(K),a]=(-1)**sum(j<i for j in J)
 return D
rows=[]
for N in [2,3]:
 for alpha in product(range(1,5),repeat=3):
  if sum(alpha)>9 or sum(alpha)<N:continue
  B=[lattice(alpha,q,N) for q in range(4)]
  ds=[]
  for q in range(3):
   V=dmap(3,q)*B[q]
   if B[q+1].cols:
    D=B[q+1].gauss_jordan_solve(V)[0]
    assert all(x.q==1 for x in D)
   else:
    assert V==sp.zeros(V.rows,V.cols)
    D=sp.zeros(0,B[q].cols)
   ds.append(D)
  hom={}
  for q in range(1,4):
   prev=ds[q-1];nex=ds[q] if q<3 else sp.zeros(0,B[q].cols)
   assert nex*prev==sp.zeros(nex.rows,prev.cols)
   smith=smith_normal_form(prev,domain=ZZ)
   tors=[abs(int(smith[j,j])) for j in range(min(smith.shape)) if abs(smith[j,j])>1]
   free=B[q].cols-prev.rank()-nex.rank()
   if free or tors:hom[q]={'free':free,'torsion':tors}
  rows.append({'N':N,'alpha':alpha,'ranks':[b.cols for b in B],
               'cohomology':hom,'lattice_bases':[b.tolist() for b in B] if hom else [],
               'differentials':[d.tolist() for d in ds] if hom else []})
def conv(x):
 if isinstance(x,sp.Integer):return int(x)
 raise TypeError(type(x))
out={'cases':rows,'elapsed_seconds':time.perf_counter()-start,'description':__doc__}
Path('SA08_work/logs/D_tail_vertical_threevars.json').write_text(json.dumps(out,indent=2,default=conv)+'\n')
print(json.dumps({'cases':len(rows),'elapsed_seconds':out['elapsed_seconds'],
                  'nonzero':[{'N':r['N'],'alpha':r['alpha'],'cohomology':r['cohomology']} for r in rows if r['cohomology']]}))
