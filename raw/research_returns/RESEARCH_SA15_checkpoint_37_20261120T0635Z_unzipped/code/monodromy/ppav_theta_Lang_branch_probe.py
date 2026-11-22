#!/usr/bin/env python3
"""Exact formal Lang branch along s=e0+t*e_(1,0), initial one-pair vector.
Laurent polynomials in the four theta coefficients over F2; exploratory only.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time
start=time.perf_counter();N=31
zero=frozenset();one=frozenset({(0,0,0,0)})
def add(*ps):
 z=set()
 for p in ps:z.symmetric_difference_update(p)
 return frozenset(z)
def mul(p,q):
 z=set()
 for a in p:
  for b in q:
   c=tuple(x+y for x,y in zip(a,b))
   if c in z:z.remove(c)
   else:z.add(c)
 return frozenset(z)
def sq(p):return frozenset(tuple(2*x for x in a) for a in p)
def mon(i,power=1):
 a=[0]*4;a[i]=power;return frozenset({tuple(a)})
def show(p):return ' + '.join('*'.join(f'a{i}^{e}' for i,e in enumerate(a) if e) or '1' for a in sorted(p)) or '0'
pts=[(x,y) for x in range(3) for y in range(3)]
def di(p,q):
 dx=(q[0]-p[0])%3;dy=(q[1]-p[1])%3
 return 0 if dx==0 else 1+dy*pow(dx,-1,3)%3
def basisM(k):
 M=[[zero]*9 for _ in range(9)]
 for i,p in enumerate(pts):
  for j,q in enumerate(pts):
   if i!=j and ((-p[0]-q[0])%3,(-p[1]-q[1])%3)==pts[k]:M[i][j]=mon(di(p,q))
 return M
M0=basisM(0);Mb=basisM(3)
v=[[zero]*9 for _ in range(N+1)];v[0][1]=v[0][2]=mon(0,-1)
for n in range(1,N+1):
 B=M0 if n%2==0 else Mb;u=v[n//2]
 v[n]=[add(*(mul(B[i][j],sq(u[j])) for j in range(9))) for i in range(9)]
lines=[[pts.index((x,y)) for x in range(3)] for y in range(3)]
coef=[]
for n in range(N+1):
 out=zero
 for line in lines:
  i,j,k=line
  for a in range(n+1):
   for b in range(n-a+1):out=add(out,mul(mul(v[a][i],v[b][j]),v[n-a-b][k]))
 if out:coef.append({'order':n,'coefficient':show(out),'terms':[list(a) for a in sorted(out)]})
r={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'through_order':N,'deformation':'s=e_(0,0)+t*e_(1,0)','initial_vector':'v_(0,1)=v_(0,2)=a0^-1, all others0','P_horizontal_coefficients':coef,'scope':'Formal exact Laurent identities; no universal nonvanishing or full-image inference.'}
(Path(__file__).resolve().parents[1]/'outputs/ppav_theta_Lang_branch_probe.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
