"""Fraction-only certificate of u_F(C_64)>=359.

Uses the proved all-field slice/crossing/removal inequalities. No numerical
optimization, external solver, original-source program or Lean is involved.
The 540 high-resource branches are exhausted using sqrt(2)>140/99.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib,json

ALPHA=Q(140,99)
BUDGET=Q(359)
HIGH=[(2048,1),(4096,1),(4096,2),(1,2048),(1,4096),(2,4096)]
TS=[3,4,7,9]
DUAL=[Q(4201,169740),Q(4201,169740),Q(17,99),Q(8,33),Q(8,33)]
for z in [Q(2,231),Q(5,84),Q(32,495),Q(40,2829)]:DUAL.extend([z,z])
BASE=[4096,4096,88,128,128]+[64*t for t in TS for _ in range(2)]

def cost(t):
 k=(t[0]*t[1]).bit_length()-1
 assert t[0]*t[1]==2**k
 return Q(2**(k//2))*(ALPHA if k%2 else 1)

def column(t):
 r,s=t
 return [r,s,min(r,s),min(r,3*s),min(3*r,s)]+[
  x for k in TS for x in (min(r,k*k*s),min(k*k*r,s))]

HCOST=list(map(cost,HIGH))
ALL=[(2**a,2**b) for a in range(13) for b in range(13)
     if cost((2**a,2**b))<BUDGET]
LOW=[t for t in ALL if max(t)<=1024*min(t)]
assert set(ALL)-set(LOW)==set(HIGH)
assert ALPHA*ALPHA<2
assert Q(99,70)**2>2 and 2**297<359**35
for t in LOW:assert sum(a*b for a,b in zip(DUAL,column(t)))<=cost(t)

def bounds(items):
 lo=BASE[:]
 for big in (0,1):
  small=1-big
  for i,t in enumerate(items):
   if t[small]<=2:
    residual=2016
    if t[small]==1:
     rho=min(64,2**((t[big].bit_length()-1)//2))
     residual=4096-rho*(rho+1)//2
    lo[big]=max(lo[big],residual+t[big])
   for u in items[i+1:]:
    if t[small]+u[small]<=2:
     lo[big]=max(lo[big],2016+t[big]+u[big])
 cols=[column(t) for t in items]
 return [max(0,x-sum(c[i] for c in cols)) for i,x in enumerate(lo)]

records=[];grouped=defaultdict(list)
for counts in product(*(range(int(BUDGET//w)+1) for w in HCOST)):
 hc=sum(c*w for c,w in zip(counts,HCOST))
 if hc>=BUDGET:continue
 items=[t for t,c in zip(HIGH,counts) for _ in range(c)]
 lo=bounds(items)
 bound=hc+sum(a*b for a,b in zip(DUAL,lo))
 assert bound>359
 records.append({'counts':counts,'high_cost_lower':str(hc),'low_bounds':lo,'cost_lower':str(bound)})
 grouped[sum(counts)].append(bound)
assert len(records)==540
minimum=min(Q(r['cost_lower']) for r in records)
assert minimum==Q(422523176,1089165)>387
out={'status':'PASS exact Fraction-only finite certificate','q':64,
 'budget':str(BUDGET),'sqrt2_lower':str(ALPHA),'high_types':HIGH,
 'high_cost_lower':list(map(str,HCOST)),'low_type_count':len(LOW),
 'dual_coefficients':list(map(str,DUAL)),'t_values':TS,
 'nprofiles':len(records),'minimum_bound':str(minimum),
 'summary':[{'high_terms':k,'nprofiles':len(v),'minimum_bound':str(min(v))}
            for k,v in sorted(grouped.items())],'records':records}
p=Path(__file__).resolve().parents[1]/'outputs/pg_cycle_q64_simple_exact.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
print('sha256',hashlib.sha256(p.read_bytes()).hexdigest())
