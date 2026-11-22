#!/usr/bin/env python3
"""Exact characteristic-two Pfaffian/polar calculations in RS17 normal form.
Exploratory invariant-theory probe; does not identify an actual Cartier model.
"""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
import itertools,json,time
start=time.perf_counter()
zero=frozenset(); one=frozenset({(0,)*9})
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
def var(i):
 e=[0]*9;e[i]=1;return frozenset({tuple(e)})
def matrix(T):
 M=[[zero]*9 for _ in range(9)]
 for a,b,c in T:
  for i,j,k in ((a,b,c),(a,c,b),(b,c,a)):
   M[i][j]=M[j][i]=add(M[i][j],var(k))
 return M
def cubic(T):
 M=matrix(T)
 @lru_cache(None)
 def pf(I):
  if not I:return one
  i=I[0];return add(*(mul(M[i][j],pf(tuple(k for k in I[1:] if k!=j))) for j in I[1:]))
 out=[]
 for i in range(9):
  p=pf(tuple(j for j in range(9) if j!=i));q=set()
  for e in p:
   assert e[i]>0
   f=list(e);f[i]-=1;q.add(tuple(f))
  out.append(frozenset(q))
 assert all(q==out[0] for q in out)
 return out[0]
def show(q):return ['*'.join(f'x{i}' if e==1 else f'x{i}^{e}' for i,e in enumerate(m) if e) for m in sorted(q)]
base=['267','258','348','169','357','249','178','456']
pars=[(3,'257'),(6,'247'),(9,'148'),(12,'147'),(15,'235'),(18,'145'),(24,'134'),(30,'123')]
rows=[]
for vals in ({15:1},{3:1,15:1},{9:1,15:1},{3:1,9:1,15:1},{15:1,24:1},{15:1,18:1}):
 T={tuple(int(i)-1 for i in s) for s in base+[s for c,s in pars if vals.get(c)]}
 q=cubic(T);B={tuple(i for i,e in enumerate(m) if e) for m in q if max(m)==1};qb=cubic(B)
 rows.append({'parameters':vals,'q':show(q),'polar_terms':[[i+1 for i in t] for t in sorted(B)],'polar_pfaffian_cubic':show(qb),'polar_pfaffian_identically_zero':not qb})
r={'utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'rows':rows,'scope':'Exact polynomial identities only. No claimed actual-Cartier identification or complete stability test.'}
(Path(__file__).resolve().parents[1]/'outputs/ppav_polar_normalform_probe.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
