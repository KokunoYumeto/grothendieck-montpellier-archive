from pathlib import Path
import json
from zero_twist_all_positive import coefficient_partition,partition_polytopes,LABELS
from five_row_cycle_trace import multiplicities
cases={(),(1,1,1,1,1)}
for x,b,k in ((1,0,0),(0,2,0),(3,1,1),(0,5,2),(0,8,3),(0,10,4),(0,18,7),(1,20,8)):
 if 2*b+x<5*k:continue
 for d in (0,1):
  lam=(d+3*b+2*x-5*k,d+b+x,d+b+x,d+x,d)
  for e in (0,2):
   L=(lam[0]+5*e,)+lam[1:];cases.add(L)
   for extra in (0,1):
    H=L[0]+extra;cases.add(tuple(H-v for v in reversed(L)))
checks=0;provider=0
for lam in sorted(cases):
 expected=multiplicities(lam)
 for mu,v in zip(LABELS,expected):
  got=coefficient_partition(lam,mu)
  assert got==v,(lam,mu,got,v)
  checks+=1
  if mu==(5,):partition_polytopes(lam,mu);provider+=1
assert coefficient_partition((5,1,1,1,1,1),(5,))==0
r={'statement':'G-033','partition_inputs':len(cases),'actual_coefficients':checks,'provider_calls':provider,'excess_rows_zero':True,'outcome':'PASS'}
Path('work/root/ZERO_WALL_PARTITION_ENTRY_CHECK.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
