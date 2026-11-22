#!/usr/bin/env python3
"""Reconstructed exact mod-2 gluing calculation for the genus-five Prym method."""
from itertools import product
from math import gcd
from pathlib import Path
from time import perf_counter
from datetime import datetime, timezone
import json
start=perf_counter()
vectors=list(product(range(2),repeat=4))
def pairing(x,y): return (x[0]*y[1]+x[1]*y[0]+x[2]*y[3]+x[3]*y[2])%2
J=[[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]
zero=(0,0,0,0); e1=(1,0,0,0); f1=(0,1,0,0); e2=(0,0,1,0); f2=(0,0,0,1)
def add(x,y):return tuple((a+b)%2 for a,b in zip(x,y))
def mul(a,x):return tuple(a*t%2 for t in x)
hist={2:0,4:0}; cases=0
for columns in product(vectors,repeat=4):
 if any(pairing(columns[i],columns[j])!=J[i][j] for i in range(4) for j in range(4)):
  continue
 cases+=1
 G=[[columns[j][i] for j in range(4)] for i in range(4)]
 P=[(0,col[1],col[2],col[3]) for col in columns]
 inc=[]; out=[]
 for x,y in product(range(2),repeat=2):
  if (x+y*G[1][0])%2==0 and all(y*G[1][j]%2==0 for j in range(1,4)):
   inc.append((x,y))
 for u,v in product(range(2),repeat=2):
  if (add(mul(u,f1),mul(v,P[0]))==zero and mul(v,P[1])==zero
      and add(mul(u,e2),mul(v,P[2]))==zero
      and add(mul(u,f2),mul(v,P[3]))==zero):
   out.append((u,v))
 I=[(2,0),(0,2)]+inc; O=[(2,0),(0,2)]+out
 scalar_gcd=0
 for x,y in I:
  for u,v in O: scalar_gcd=gcd(scalar_gcd,abs(x*u+y*v))
 assert scalar_gcd in (2,4)
 assert scalar_gcd==(2 if tuple(G[1])==e1 else 4)
 hist[scalar_gcd]+=1
assert cases==720 and hist=={2:48,4:672}
record={
 'utc':datetime.now(timezone.utc).isoformat(),'seconds':perf_counter()-start,
 'symplectic_markings':cases,'composite_integer_ideals':{str(k)+'Z':v for k,v in hist.items()},
 'all_composites_even':True,'all_checks_passed':True,
 'reconstruction':'Fresh reconstruction/rerun after scratch reset. Original run 09:37:18.986283 UTC took 0.013099318s; this program and runtime are a separate reproducible certificate.',
 'scope':'Conditional on the exact geometric Prym lattice premise stated in the report; no arbitrary-Jacobian obstruction.'}
root=Path(__file__).resolve().parents[1]
(root/'output'/'check_genus5_hom_parity.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
