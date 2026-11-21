from pathlib import Path
from itertools import product
import json
from one_twist_all_positive import coefficient_partition,partition_route,partition_polytopes,LABELS,transpose
from five_row_cycle_trace import multiplicities
cases=[(0,0,0),(0,1,0),(2,0,1),(0,1,1),(7,0,2),(3,6,3),(1,10,4),(0,14,6),(0,16,7),(0,21,9),(1,16,7),(2,23,10)]
checks=0;shapes=0;poly=0
for x,b,k in cases:
 if 2*b+x+3<5*k:continue
 for d,stable,other in product((0,1),(0,3),(False,True)):
  lam=(d+3*b+2*x+4-5*k+5*stable,d+b+x+1,d+b+x,d+x,d)
  if other:
   H=lam[0];lam=tuple(H-z for z in reversed(lam))
  expected=multiplicities(lam)
  for j,mu in enumerate(LABELS):
   got=coefficient_partition(lam,mu)
   assert got==expected[j],(lam,mu,got,expected[j],partition_route(lam,mu))
   checks+=1
  result=partition_polytopes(lam,(5,));assert 'formula' in result
  shapes+=1;poly+=1
receipt=dict(statement='G-034',partition_shapes=shapes,actual_coefficients=checks,polytope_providers=poly,both_adjacent_walls=True,stable_first_row_shifts=[0,3],determinant_parameters=[0,1],outcome='PASS')
Path('work/root/ONE_WALL_PARTITION_ENTRY_CHECK.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt),flush=True)
