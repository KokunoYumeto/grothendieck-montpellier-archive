from pathlib import Path
from itertools import product,islice
import json
from generic_twist_lower_positive import *
from fixed_twist_arrangement import traces as actual_traces
from five_row_cycle_trace import multiplicities

def shape(x,b,k,c,d=0):return(d+3*b+2*x+4*c-5*k,d+b+x+c,d+b+x,d+x,d)
receipt={}
for branch in ('A','B'):
 direct=actual=continuation=matrix=0;seeds=[]
 for X,T,K,C in product((0,1),(0,1),(0,1),(0,1,2,3)):
  Z=(X,T,K,C);x,b,k,c=physical(branch,Z)
  expected=actual_traces(x,b,k,c);got=traces(branch,Z)
  assert got==expected,(branch,Z,got,expected)
  direct+=7
  if K==0 and C in (2,3):
   for d in (0,1):
    lam=shape(x,b,k,c,d);expected=multiplicities(lam)
    proposed=tuple(coefficient(branch,Z,d,mu) for mu in LABELS)
    assert proposed==expected,(branch,Z,d,proposed,expected)
    actual+=7
 positions=([(0,0,0,2),(0,1,0,2),(0,2,0,2),(0,0,0,3)] if branch=='A' else [(0,0,1,2),(0,1,0,2),(0,3,0,2),(0,5,0,2)])
 for Z in positions:
  x,b,k,c=physical(branch,Z);expected=multiplicities(shape(x,b,k,c))
  if (b+x+c)%2:expected=expected[::-1]
  values=tuple(fixed_value(branch,mu,Z) for mu in LABELS)
  assert values==expected and min(values)>0,(branch,Z,values,expected)
  seeds.append(dict(coordinates=Z,effective_multiplicities=values,output=shape(x,b,k,c)))
 for Z in ((59,59,59,59),(60,0,0,0),(0,60,0,0),(0,0,60,0),(0,0,0,60),(60,60,60,60),(61,62,63,64),(120,180,240,60)):
  x,b,k,c=physical(branch,Z)
  for d,mu in product((0,1),LABELS):
   label=transpose(mu) if(d+b+x+c)%2 else mu
   assert coefficient(branch,Z,d,mu)==fixed_value(branch,label,Z)
   continuation+=1
  if Z in ((60,0,0,0),(0,60,0,0),(0,0,60,0),(0,0,0,60),(60,60,60,60)):
   for mu in LABELS:
    for tag in tags(branch,Z,0,mu):
     p=constraints(tag);assert len(p['variables'])<=11
     for point in islice(witnesses(tag),2):
      assert all(lo<=z<=hi for lo,z,hi in zip(p['lower_bounds'],point,p['upper_bounds']))
      assert all(sum(a*z for a,z in zip(row,point))==rhs for row,rhs in zip(p['A_eq'],p['b_eq']))
      assert all(sum(a*z for a,z in zip(row,point))>=rhs for row,rhs in zip(p['A_ge'],p['b_ge']))
      matrix+=1
 receipt[branch]=dict(full_restriction_traces=direct,actual_balanced_coefficients=actual,continuation_parity=continuation,literal_witnesses=matrix,seeds=seeds,outcome='PASS')
 print(branch,json.dumps(receipt[branch]),flush=True)
Path('work/root/GENERIC_TWIST_LOWER_RECEIPT.json').write_text(json.dumps({'statement':'G-035-candidate','cones':receipt,'outcome':'PASS','scope':'no full60^4 base box replay; actual modules prove order-zero signs; finite seeds and invariant multiplication prove support'},indent=2)+'\n')
