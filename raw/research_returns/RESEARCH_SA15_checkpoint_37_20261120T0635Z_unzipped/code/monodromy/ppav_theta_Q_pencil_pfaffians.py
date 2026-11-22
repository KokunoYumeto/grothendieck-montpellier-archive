#!/usr/bin/env python3
"""Exact universal GF(2) Pfaffian calculation on a Q-isotropic theta pencil.
Exploratory algebra only; this script does not establish monodromy.
"""
from pathlib import Path
from datetime import datetime, timezone
from functools import lru_cache
import json,time
import sympy as S
start=time.perf_counter()
a=S.symbols('a0:4');z=S.symbols('z');gens=(*a,z)
def red(x): return S.Poly(S.expand(x),*gens,modulus=2).as_expr()
pts=[(x,y) for x in range(3) for y in range(3)]
def direction(p,q):
 dx=(q[0]-p[0])%3;dy=(q[1]-p[1])%3
 if dx==0:return 0
 slope=dy*pow(dx,-1,3)%3
 return 1+slope
s=[1,1,z,z,0,0,0,0,0]
M=[[S.Integer(0) for j in range(9)] for i in range(9)]
for i,p in enumerate(pts):
 for j,q in enumerate(pts):
  if i==j:continue
  r=((-p[0]-q[0])%3,(-p[1]-q[1])%3)
  k=pts.index(r)
  M[i][j]=a[direction(p,q)]*s[k]
@lru_cache(None)
def pf(indices):
 if not indices:return S.Integer(1)
 i=indices[0]
 return red(sum(M[i][j]*pf(tuple(k for k in indices[1:] if k!=j)) for j in indices[1:]))
full=tuple(range(9))
pf8=pf(tuple(range(1,9)))
q_expected=red(a[0]*(a[1]**3+a[2]**3+a[3]**3)*z)
assert red(pf8-q_expected)==0
num1=pf(tuple(i for i in full if i not in (0,1,2)))
num2=pf(tuple(i for i in full if i not in (0,1,3)))
num=red(num1+num2)
for i in range(9):
 assert red(sum(M[i][j]*s[j] for j in range(9)))==0
 assert red(pf(tuple(j for j in range(9) if j!=i))-q_expected*s[i])==0
r={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,'status':'PASS','direction_order':['vertical','horizontal','slope1','slope2'],'pencil':'s=(1,1,z,z,0,0,0,0,0)','Q_identically_zero':True,'pf8_delete0':str(pf8),'pf6_delete012':str(num1),'pf6_delete013':str(num2),'inverse_pairing_numerator':str(num),'inverse_pairing_numerator_zero':num==0,'scope':'Exact Pfaffian identities on one isotropic pencil; no uniform stable-rank or monodromy conclusion.'}
out=Path(__file__).resolve().parents[1]/'outputs/ppav_theta_Q_pencil_pfaffians.json'
out.write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
