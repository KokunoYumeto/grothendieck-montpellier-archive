from pathlib import Path
from itertools import islice
import json
from one_twist_all_positive import route,coefficient,polytopes,cone_tags,LABELS,upper
from fixed_twist_arrangement import coefficients as exact
from five_row_cycle_trace import multiplicities
cases=[]
for k in (0,1,2,3,4,6,7,8,10):
 for b in sorted({0,max(0,k-1),k,2*k-2,2*k-1,2*k,2*k+1,2*k+2,3*k-6,3*k-5,3*k-4,3*k-3}):
  if b<0:continue
  shift=max(0,5*k-2*b-3);t=3*k-5-b
  xs={shift,max(shift,t),max(shift,t+1)}
  for x in sorted(xs):cases.append((x,b,k))
checks=0;actual=0;branches={};matrix_checks=0
for x,b,k in cases:
 vals=exact(x,b,k,1) if k else None
 for d in (0,1):
  for j,mu in enumerate(LABELS):
   name,args=route(x,b,k,d,mu);branches[name]=branches.get(name,0)+1
   got=coefficient(x,b,k,d,mu)
   if vals is None:
    lam=(d+3*b+2*x+4,d+b+x+1,d+b+x,d+x,d)
    expected=multiplicities(lam)[j];actual+=1
   else:expected=vals[6-j if (d+b+x+1)%2 else j]
   assert got==expected,(x,b,k,d,mu,name,got,expected)
   checks+=1
   if name in ('A','B') and mu in ((5,),(1,1,1,1,1)):
    for tag in cone_tags(name,*args):
     if not tag['constant']:continue
     p=upper.constraints(tag)
     for v in islice(upper.witnesses(tag),3):
      assert all(lo<=z<=hi for lo,z,hi in zip(p['lower_bounds'],v,p['upper_bounds']))
      assert all(sum(a*b for a,b in zip(row,v))==rhs for row,rhs in zip(p['A_eq'],p['b_eq']))
      assert all(sum(a*b for a,b in zip(row,v))>=rhs for row,rhs in zip(p['A_ge'],p['b_ge']))
      matrix_checks+=1
# Exercise emitted matrices from every selected provider once.
seen=set()
for x,b,k in cases:
 name,args=route(x,b,k,0,(5,))
 if name not in seen:
  result=polytopes(x,b,k,0,(5,));assert result['branch']==name;seen.add(name)
assert seen==set(branches)
receipt={'statement':'G-034','coefficient_checks':checks,'direct_k0_actual_coefficients':actual,'branches':branches,'new_cone_witness_matrix_checks':matrix_checks,'all_polytope_provider_routes_exercised':sorted(seen),'outcome':'PASS'}
Path('work/root/ONE_WALL_ALL_ROUTES_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
