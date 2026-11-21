from pathlib import Path
from itertools import product
import json
from outer_five_positive import *
from five_row_cycle_trace import multiplicities
from normalized_below_positive import NAMES,RAW,boundary_physical
from generic_twist_lower_positive import physical as lower_physical

def shape(x,b,k,c,d):return(d+3*b+2*x+4*c-5*k,d+b+x+c,d+b+x,d+x,d)
bases=[(0,0,0,0),(2,1,0,2),(2,0,1,1),(0,1,1,1),(2,2,2,2),(0,4,2,1),(3,6,3,1),(0,8,3,2),(0,10,4,0),(0,11,5,1),(0,12,6,2)]
for name in NAMES:
 for z in (0,1):bases.append(boundary_physical(name,(z,)*RAW[name]['dimension']))
for branch in ('A','B'):
 for C in (0,1,2,3):bases.append(lower_physical(branch,(0,0,0,C)))
for X,B,K,C in ((0,0,0,2),(1,2,1,3),(0,1,3,4)):
 bases.append((X,C+3*K+10+B,C+K+4,C))
for X,B,K,U in ((0,0,0,0),(1,2,0,3),(0,0,1,0),(2,1,2,1)):
 bases.append((X,K+B+1,K+U+1,K+2*U+1))
shapes=set()
for x,b,k,c in bases:
 if 2*b+x+3*c<5*k:continue
 for d,comp,extra in product((0,1),(False,True),(0,2)):
  lam=shape(x,b,k,c,d)
  if comp:
   H=lam[0]+1;lam=tuple(H-z for z in reversed(lam))
  lam=(lam[0]+5*extra,)+lam[1:]
  shapes.add(lam)
checks=0;routes={};examples={};complements=stable=0
for lam in sorted(shapes,key=lambda z:(sum(z),z)):
 expected=multiplicities(lam)
 for j,mu in enumerate(LABELS):
  got=coefficient_partition(lam,mu);r=partition_route(lam,mu)
  assert got==expected[j],(lam,mu,got,expected[j],r)
  route=r['selected'][0]
  if route=='below':
   name,args=r['below_selected'];route+=':'+name
   if name=='lower':route+=':'+args[0]
  routes[route]=routes.get(route,0)+1;examples.setdefault(route,lam)
  checks+=1;complements+=r['complement'];stable+=r['stable_power']>0
# Exercise every reached formula provider and its declared structural bounds.
def leaf_polytopes(v):
 if isinstance(v,list):
  for x in v:yield from leaf_polytopes(x)
 elif isinstance(v,dict):
  if 'variables' in v:yield v
  elif 'polytopes' in v:yield from leaf_polytopes(v['polytopes'])
  elif 'formula' in v:yield from leaf_polytopes(v['formula'])
polychecks=0;max_tags=0;max_variables=0
for route,lam in examples.items():
 for mu in LABELS:
  ps=list(leaf_polytopes(partition_polytopes(lam,mu)))
  assert len(ps)<=152,(route,len(ps))
  assert all(len(p['variables'])<=11 for p in ps)
  max_tags=max(max_tags,len(ps));max_variables=max(max_variables,max((len(p['variables']) for p in ps),default=0));polychecks+=1
for mu in LABELS:
 assert coefficient_partition((5,5,5,5,5,5),mu)==0
 assert coefficient_partition((),mu)==int(mu==(5,))
r=dict(statement='G-036',original_partition_cases=len(shapes),actual_coefficients=checks,routes=routes,complement_calls=complements,stable_calls=stable,polytope_provider_checks=polychecks,max_emitted_tags=max_tags,max_variables=max_variables,overlength_zeros=7,degree_zero_cases=7,outcome='PASS')
Path('work/root/OUTER_FIVE_POSITIVE_ROUTING_RECEIPT.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r),flush=True)
