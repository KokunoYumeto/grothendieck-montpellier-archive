"""Exact necessary-profile diagnostic at q128; does not construct a cover."""
from pathlib import Path
import json

PROFILE=[(1,32,4),(2,8,11),(2,32,1),(2,256,2),(2,8192,2),
 (4,128,1),(8,2,11),(32,1,8),(32,2,1),(32,32,1),(64,64,1),
 (256,2,2),(8192,2,2)]
q=128
items=[(r,s) for r,s,c in PROFILE for _ in range(c)]
assert sum(r for r,s in items)==sum(s for r,s in items)==17408
assert sum(min(r,s) for r,s in items)==176
assert sum(min(r,3*s) for r,s in items)>=2*q
assert sum(min(3*r,s) for r,s in items)>=2*q
for t in range(1,q+1):
 assert sum(min(r,t*t*s) for r,s in items)>=t*q
 assert sum(min(t*t*r,s) for r,s in items)>=t*q
for big in (0,1):
 small=1-big;total=sum(t[big] for t in items)
 for i,t in enumerate(items):
  if t[small]<=2:
   residual=q*(q-1)//2
   if t[small]==1:
    rho=min(q,2**((t[big].bit_length()-1)//2))
    residual=q*q-rho*(rho+1)//2
   assert total-t[big]>=residual
  for u in items[i+1:]:
   if t[small]+u[small]<=2:
    assert total-t[big]-u[big]>=q*(q-1)//2
A=B=0
for r,s in items:
 k=(r*s).bit_length()-1
 if k%2:B+=2**(k//2)
 else:A+=2**(k//2)
assert (A,B)==(712,128)
assert 10**2>2*7**2 and 712*7+128*10<900*7
assert 24**2<2*17**2 and 900**17<2**168
out={'status':'PASS exact necessary-profile verification; not a tensor cover',
 'q':q,'profile':PROFILE,'cost':'712+128*sqrt(2)','sum_R':17408,
 'sum_S':17408,'sum_min':176,'all_unbalanced_t':128,
 'rank_two_and_refined_rank_one_removals':'all applicable singletons/pairs checked',
 'strict_cost_comparison':'712+128sqrt(2)<900<128^sqrt(2)',
 'local_maps':'not constructed'}
p=Path(__file__).resolve().parents[1]/'outputs/pg_cycle_q128_profile_exact.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
