#!/usr/bin/env python3
from pathlib import Path
from math import gcd,factorial
from datetime import datetime,timezone
from time import perf_counter
import json
import numpy as np
start=perf_counter();print('Started UTC',datetime.now(timezone.utc).isoformat())
records=[]
for r in range(4,21):
 m=r-1;h=2*m;units=[a for a in range(h) if gcd(a,h)==1]
 I=np.eye(r,dtype=np.int64);c=np.zeros((r,r),dtype=np.int64)
 for j in range(m-1):c[j+1,j]=1
 c[0,m-1]=-1;c[-1,-1]=-1
 powers=[I]
 for a in range(1,h):powers.append(powers[-1]@c)
 assert np.array_equal(powers[-1]@c,I)
 rho=np.array(list(range(m,0,-1))+[0],dtype=np.int64)
 delta=[]
 for j in range(r):
  d=I.copy()
  if j!=r-1:d[j,j]=d[-1,-1]=-1
  delta.append(d)
 B=[];N=[]
 for j,d in enumerate(delta):
  for a in units:
   # P^vee=Z^r union (Z+1/2)^r, tested in doubled coordinates.
   residual=(d@rho-a*rho)%h
   if np.all(residual==0) or np.all(residual==m):B.append((j,a))
   if np.array_equal(d@c@d,powers[a]):N.append((j,a))
 assert B==[(0,1),(r-1,1)] and N==[(r-1,1)]
 pairs=[(b,a) for b,u in B for a,v in N if u==v];assert len(pairs)==2
 M=2**m*factorial(m);Phi=h*4*len(units);W=r*M
 C=W*W//Phi;F=2*M*M//Phi
 assert C*Phi==W*W and F*Phi==2*M*M and F*r*r==2*C
 records.append({'rank':r,'coxeter_number':h,'fixed_Weyl_order':M,'Phi_order':Phi,'B_t_twisted_intersection':B,'A_twisted_intersection':N,'inner_classes':C,'C2_classes':F,'trivial_classes':C-F})
 print('D'+str(r),'inner',C,'C2-fixed-for-end-node-involution',F,'ratio2/r^2',flush=True)
print('PASS: exhaustive twisted-coboundary intersection checks for ranks4 through20')
print('Elapsed seconds',perf_counter()-start)
(Path(__file__).resolve().parents[1]/'logs/type_d_outer_stabilizers.json').write_text(json.dumps(records,indent=2))
