#!/usr/bin/env python3
"""Exact standalone GF(8) witness for the equal-coefficient theta tensor."""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
import json,time
start=time.perf_counter()
def mul(a,b):
 r=0
 while b:
  if b&1:r^=a
  b>>=1;a<<=1
  if a&8:a^=11
 return r
def pw(a,n):
 r=1
 while n:
  if n&1:r=mul(r,a)
  n>>=1;a=mul(a,a)
 return r
def dot(a,b):
 r=0
 for x,y in zip(a,b):r^=mul(x,y)
 return r
s=[0,5,3,3,6,0,4,7,5]
pts=[(x,y) for x in range(3) for y in range(3)]
M=[[0]*9 for _ in range(9)]
for i,p in enumerate(pts):
 for j,q in enumerate(pts):
  if i!=j:M[i][j]=s[pts.index(((-p[0]-q[0])%3,(-p[1]-q[1])%3))]
@lru_cache(None)
def pf(ids):
 if not ids:return 1
 r=0;i=ids[0]
 for j in ids[1:]:r^=mul(M[i][j],pf(tuple(k for k in ids[1:] if k!=j)))
 return r
pivot=1;p8=pf(tuple(i for i in range(9) if i!=pivot));q=mul(p8,pw(s[pivot],6))
assert q and dot(s,[pw(x,2) for x in s])==0
A=[M[i][:]+[pw(s[i],2)] for i in range(9)];row=0;piv=[]
for col in range(9):
 i=next((j for j in range(row,9) if A[j][col]),None)
 if i is None:continue
 A[row],A[i]=A[i],A[row];scale=pw(A[row][col],6);A[row]=[mul(scale,x) for x in A[row]]
 for j in range(9):
  if j!=row and A[j][col]:
   scale=A[j][col];A[j]=[x^mul(scale,y) for x,y in zip(A[j],A[row])]
 piv.append(col);row+=1
assert row==8 and all(not any(r[:9]) and not r[9] for r in A[row:])
u=[0]*9
for i,col in enumerate(piv):u[col]=A[i][9]
assert all(dot(r,u)==pw(x,2) for r,x in zip(M,s))
eta=dot(s,[pw(x,2) for x in u]);assert eta
r={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'status':'PASS','field_modulus':'x^3+x+1','integer_encoding':'a0+2*a1+4*a2 means a0+a1*x+a2*x^2','alpha':[1,1,1,1],'s':s,'preimage_u':u,'q':q,'eta':eta,'matrix_rank':row,'scope':'Exact M(s)u=s^[2], Q(s)=0, q(s)!=0 and s^t u^[2]!=0; one normal-form witness, not a finite sampling argument.'}
(Path(__file__).resolve().parents[1]/'outputs/ppav_theta_equal_cubes_F8_witness.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
