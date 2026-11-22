#!/usr/bin/env python3
"""Finite exploratory Lang-vector ranks at a=1. No geometric claim."""
import json,time
from pathlib import Path
import sympy as sp
started=time.perf_counter()
u=sp.symbols('u0:3')
Mo=sp.Matrix([[u[0],u[2],u[1]],[u[2],u[1],u[0]],[0,u[2],u[1]+u[2]]])
Ms=sp.Matrix([[u[1],u[0],0],[u[2],0,u[0]],[0,u[2],u[1]]])
Ro=sp.Matrix([[1,0,1],[0,0,1],[0,1,1]])
J=sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
R=sp.kronecker_product(Ro,J)
coeff=[sp.kronecker_product(Mo.diff(u[i]),Ms.diff(u[j])) for i in range(3) for j in range(3)]
def rows(A):return [sum((int(A[i,j])%2)<<j for j in range(9)) for i in range(9)]
def mul(A,v):return sum(((r&v).bit_count()%2)<<i for i,r in enumerate(A))
Rrows=rows(R);Rtrows=rows(R.T)
Rtinv={mul(Rtrows,v):v for v in range(512)}
Acoeff=[rows(R*C) for C in coeff]
def Amat(v):
 out=[0]*9
 for i,C in enumerate(Acoeff):
  if (v>>i)&1:out=[x^y for x,y in zip(out,C)]
 return out
def det(v):
 b=[(v>>i)&1 for i in range(9)]
 return (b[0]*b[4]*b[8]^b[0]*b[5]*b[7]^b[1]*b[3]*b[8]^b[1]*b[5]*b[6]^b[2]*b[3]*b[7]^b[2]*b[4]*b[6])
def Q(v):return (v&mul(Rrows,v)).bit_count()%2
def rank(rows):
 piv={}
 for r in rows:
  while r:
   i=r.bit_length()-1
   if i in piv:r^=piv[i]
   else:piv[i]=r;break
 return len(piv)
stats={};example=None
for v in range(1,512):
 w=Rtinv[v];A=Amat(w);r=rank(A)
 sols=[s for s in range(512) if mul(A,s)==v]
 good=[s for s in sols if det(s) and Q(s)]
 key=f'rank{r}_D{det(w)}'
 st=stats.setdefault(key,dict(vectors=0,compatible=0,unit_compatible=0))
 st['vectors']+=1;st['compatible']+=bool(sols);st['unit_compatible']+=bool(good)
 if good and not det(w) and example is None:example=dict(v=v,w=w,s=good[0])
out=dict(status='EXPLORATORY_COMPLETE',scope='F2 a=1 only; no geometric dimension inference',stats=stats,bad_rank_unit_example=example,runtime_seconds=time.perf_counter()-started)
Path(__file__).resolve().parents[1].joinpath('outputs/explore_mixed_Lang_rank_strata.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
