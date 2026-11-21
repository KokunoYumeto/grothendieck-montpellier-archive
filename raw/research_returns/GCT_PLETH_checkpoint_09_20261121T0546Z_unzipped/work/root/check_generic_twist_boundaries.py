from pathlib import Path
from itertools import product,islice
import json
from normalized_below_positive import *
from fixed_twist_arrangement import traces as exact
from five_row_cycle_trace import multiplicities
receipt={}
for name in NAMES:
 n=RAW[name]['dimension'];trace_checks=actual_checks=cont=matrix=0
 for Z in product((0,1,3),repeat=n):
  x,b,k,c=boundary_physical(name,Z);v=boundary_traces(name,Z);want=exact(x,b,k,c)
  assert v==want,(name,Z,v,want)
  assert route(x,b,k,c,0,(5,))[0]==name,(name,Z,route(x,b,k,c,0,(5,)))
  trace_checks+=7
  if max(Z)<=1:
   for d in (0,1):
    lam=(d+3*b+2*x+4*c-5*k,d+b+x+c,d+b+x,d+x,d);want=multiplicities(lam)
    got=tuple(coefficient(x,b,k,c,d,mu) for mu in LABELS)
    assert got==want,(name,Z,d,got,want)
    actual_checks+=7
 for Z in [(59,)*n,(60,)*n,tuple(60*(i+1) for i in range(n))]+[tuple(60 if i==j else 0 for i in range(n)) for j in range(n)]:
  x,b,k,c=boundary_physical(name,Z)
  for d,mu in product((0,1),LABELS):
   label=upper.transpose(mu) if(d+b+x+c)%2 else mu
   assert coefficient(x,b,k,c,d,mu)==boundary_value(name,label,Z)
   cont+=1
   if d==0:
    for tag in boundary_tags(name,label,Z):
     p=constraints(tag);assert len(p['variables'])<=11
     for point in islice(witnesses(tag),2):
      assert all(lo<=z<=hi for lo,z,hi in zip(p['lower_bounds'],point,p['upper_bounds']))
      assert all(sum(a*z for a,z in zip(row,point))==rhs for row,rhs in zip(p['A_eq'],p['b_eq']))
      assert all(sum(a*z for a,z in zip(row,point))>=rhs for row,rhs in zip(p['A_ge'],p['b_ge']))
      matrix+=1
 receipt[name]=dict(full_restriction_traces=trace_checks,actual_balanced_coefficients=actual_checks,continuation_parity=cont,literal_witnesses=matrix,outcome='PASS')
 print(name,json.dumps(receipt[name]),flush=True)
Path('work/root/GENERIC_TWIST_BOUNDARIES_RECEIPT.json').write_text(json.dumps({'statement':'G-035-candidate','boundaries':receipt,'outcome':'PASS'},indent=2)+'\n')
