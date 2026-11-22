#!/usr/bin/env python3
"""Finite point-count and Jacobian-identity checks for C027; not cohomology verification."""
from itertools import product
from pathlib import Path
import json

systems=[
 ('one_free',1,[lambda x:x[0]*x[0]-x[0]]),
 ('one_true',1,[lambda x:x[0]*x[0]-x[0],lambda x:x[0]-1]),
 ('one_false',1,[lambda x:x[0]*x[0]-x[0],lambda x:x[0]]),
 ('inconsistent',1,[lambda x:x[0]*x[0]-x[0],lambda x:x[0],lambda x:x[0]-1]),
 ('two_free',2,[lambda x:x[0]*x[0]-x[0],lambda x:x[1]*x[1]-x[1]]),
 ('two_or',2,[lambda x:x[0]*x[0]-x[0],lambda x:x[1]*x[1]-x[1],lambda x:(1-x[0])*(1-x[1])]),
 ('two_equal',2,[lambda x:x[0]*x[0]-x[0],lambda x:x[1]*x[1]-x[1],lambda x:x[0]-x[1]])]
rows=[]; tested=0;jacobian_checks=0
for name,v,fs in systems:
 h=len(fs);N=sum(all(f(x)==0 for f in fs) for x in product((0,1),repeat=v))
 for p in (2,3,5,7):
  counts=[0,0]
  for x in product(range(p),repeat=v):
   values=[f(x)%p for f in fs]
   for y in product(range(p),repeat=h):
    rhs=sum(a*b for a,b in zip(y,values))%p
    for t in range(p):
     tested+=1
     if (t*t-t-rhs)%p==0:
      counts[0]+=1
      assert ((2*t-1)**2-4*rhs)%p==1%p
      jacobian_checks+=1
     if p!=2 and (t*t+1-rhs)%p==0:
      counts[1]+=1
      assert (-t*t+rhs)%p==1%p
      jacobian_checks+=1
  assert counts[0]==p**(v+h)+N*p**h
  assert counts[0]%(2**(h+1))==2**h*(N%2) if p==2 else counts[0]%2==(1+N)%2
  if p!=2:
   chi=1 if p%4==1 else -1
   assert counts[1]==p**(v+h)+N*chi*p**h
   assert counts[1]%2==(1+N)%2
  rows.append(dict(system=name,p=p,v=v,h=h,N=N,untwisted=counts[0],twisted=counts[1] if p!=2 else None))
r=dict(status='pass',point_assignments=tested,jacobian_identities=jacobian_checks,finite_field_system_cases=len(rows),cases=rows,limitations='Finite examples only; no mechanical cohomology, geometric-integrality, analytic-continuation or complexity verification.')
Path(__file__).with_name('FINITE_CHECK_CAYLEY_RESULTS.json').write_text(json.dumps(r,indent=2)+'\n')
print({k:v for k,v in r.items() if k!='cases'})
