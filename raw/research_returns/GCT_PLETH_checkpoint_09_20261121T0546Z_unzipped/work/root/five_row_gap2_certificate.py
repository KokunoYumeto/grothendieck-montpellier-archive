#!/usr/bin/env python3
"""G-025: every minimal congruence seed and all exact class traces."""
from pathlib import Path
from itertools import product
from math import gcd, isqrt
import json
import sys
from five_row_cycle_trace import multiplicities,traces,partition_from_gaps

HERE=Path(__file__).resolve().parent
seeds=[]
for parity in product(range(2),repeat=4):
    base=tuple(2+p for p in parity)
    candidates=[u for u in product(range(5),repeat=4)
                if sum(u)<=4 and sum((i+1)*(base[i]+2*u[i]) for i in range(4))%5==0]
    minimal=[u for u in candidates
             if not any(v!=u and all(a<=b for a,b in zip(v,u)) for v in candidates)]
    for u in minimal:
        gaps=tuple(b+2*v for b,v in zip(base,u))
        lam=partition_from_gaps(gaps);values=multiplicities(lam)
        assert min(values)>=2,(parity,u,values)
        seeds.append(dict(parity=parity,increment=u,gaps=gaps,partition=lam,
                          inner=sum(lam)//5,traces=traces(lam),multiplicities=values))
assert len(seeds)==76
result={'seeds':seeds,'failures':[]}
target=HERE/'FIVE_ROW_GAP2_SEEDS.json'
if target.exists():assert json.loads(target.read_text())==json.loads(json.dumps(result))
target.write_text(json.dumps(result,indent=2)+'\n')

sys.path.insert(0,str(HERE.parent/'rectangular'))
from verify_outer4_chambers import actual
source=actual((4,),5,(8,6,4,2))
target_multiplicity=actual((5,),4,(8,6,4,2))
assert (source,target_multiplicity)==(1,3)
prime=1000003
assert all(prime%d for d in range(2,isqrt(prime)+1))
assert gcd(prime,24*120**4)==1
receipt={'statement':'G-025','seed_count':len(seeds),
         'minimum_multiplicity':min(min(row['multiplicities']) for row in seeds),
         'largest_seed_inner':max(row['inner'] for row in seeds),
         'n4_source_multiplicity':source,'n4_target_multiplicity':target_multiplicity,
         'polarization_modulus':prime,'modulus_prime_by_trial_division':True,
         'polarization_denominators_invertible':True}
(HERE/'FIVE_ROW_GAP2_CERTIFICATE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,sort_keys=True))
