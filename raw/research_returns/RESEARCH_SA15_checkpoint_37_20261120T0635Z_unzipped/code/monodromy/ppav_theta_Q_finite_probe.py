#!/usr/bin/env python3
"""Exploratory GF(8) ranks of the universal nonordinary theta matrix on Q=0.
No universal theorem is inferred from this bounded probe.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,random,time
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
  a=mul(a,a);n>>=1
 return r
def dot(a,b):
 r=0
 for x,y in zip(a,b):r^=mul(x,y)
 return r
def mm(A,B):return [[dot(x,y) for y in zip(*B)] for x in A]
def rank(A):
 A=[r[:] for r in A];row=0
 for j in range(len(A[0])):
  p=next((i for i in range(row,len(A)) if A[i][j]),None)
  if p is None:continue
  A[row],A[p]=A[p],A[row];q=pw(A[row][j],6);A[row]=[mul(q,x) for x in A[row]]
  for i in range(len(A)):
   if i!=row and A[i][j]:
    q=A[i][j];A[i]=[x^mul(q,y) for x,y in zip(A[i],A[row])]
  row+=1
 return row
pts=[(x,y) for x in range(3) for y in range(3)]
def di(p,q):
 dx=(q[0]-p[0])%3;dy=(q[1]-p[1])%3
 return 0 if not dx else 1+dy*pow(dx,-1,3)%3
def matrix(a,s):
 M=[[0]*9 for _ in range(9)]
 for i,p in enumerate(pts):
  for j,q in enumerate(pts):
   if i==j:continue
   k=pts.index(((-p[0]-q[0])%3,(-p[1]-q[1])%3))
   M[i][j]=mul(a[di(p,q)],s[k])
 return M
def relative(M,s):
 k=next(i for i,x in enumerate(s) if x);iv=pw(s[k],6);s=[mul(iv,x) for x in s];M=[[mul(iv,x) for x in row] for row in M]
 ids=[i for i in range(9) if i!=k]
 return [[M[i][j]^mul(pw(s[j],2),M[i][k]) for j in ids] for i in ids]
random.seed(19441119)
rows=[]
for a in ([1,1,1,1],[1,1,1,0],[1,1,0,0],[1,2,3,4],[1,1,1,2]):
 counts={};witness=None
 for tr in range(500):
  s=[random.randrange(8) for _ in range(8)];q=0
  for x in s:q^=pw(x,3)
  s.append(pw(q,5))
  assert sum([])==0
  M=matrix(a,s)
  if rank(M)!=8:continue
  A=relative(M,s);B=A
  seq=[rank(A)]
  for j in range(3):
   B=mm(A,[[pw(x,2) for x in row] for row in B]);seq.append(rank(B))
  key=','.join(map(str,seq));counts[key]=counts.get(key,0)+1
  if seq[-1]==7 and witness is None:witness={'s':s,'ranks':seq}
 rows.append({'alpha':a,'counts':counts,'rank7_witness':witness})
r={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'field':'GF(8), modulus x^3+x+1','rows':rows,'scope':'Bounded exploratory ranks only; no universal conclusion.'}
(Path(__file__).resolve().parents[1]/'outputs/ppav_theta_Q_finite_probe.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
