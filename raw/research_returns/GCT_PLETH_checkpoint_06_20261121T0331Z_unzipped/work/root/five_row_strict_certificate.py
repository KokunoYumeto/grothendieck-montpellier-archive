#!/usr/bin/env python3
"""G-028: exact minimal seeds, zero-sum generators, rays and map ranks."""
from pathlib import Path
from itertools import product, permutations
import json
from five_row_cycle_trace import multiplicities,traces,partition_from_gaps,SIZES,CHARS
from first_power_zero_twist import complete_values

HERE=Path(__file__).resolve().parent
seeds=[]
for parity in product(range(2),repeat=4):
    base=tuple(1+p for p in parity)
    candidates=[u for u in product(range(5),repeat=4) if sum(u)<=4
                and sum((i+1)*(base[i]+2*u[i]) for i in range(4))%5==0]
    minimal=[u for u in candidates if not any(v!=u and all(a<=b for a,b in zip(v,u)) for v in candidates)]
    for u in minimal:
        gaps=tuple(b+2*v for b,v in zip(base,u));lam=partition_from_gaps(gaps)
        seeds.append({'parity':parity,'increment':u,'gaps':gaps,'partition':lam,
                      'inner':sum(lam)//5,'traces':traces(lam),'multiplicities':multiplicities(lam)})
assert len(seeds)==76
bad=[s for s in seeds if min(s['multiplicities'])==0]
expected_bad={(1,1,1,1),(1,1,1,6),(1,2,2,1),(6,1,1,1),(2,1,1,2)}
assert {s['gaps'] for s in bad}==expected_bad
assert min(min(s['multiplicities'][1:6]) for s in seeds)==1
vs=[v for v in product(range(6),repeat=4) if 1<=sum(v)<=5
    and sum((i+1)*v[i] for i in range(4))%5==0]
generators=[v for v in vs if not any(u!=v and all(a<=b for a,b in zip(u,v)) for u in vs)]
assert len(generators)==14
increment_cases=[]
failures=[]
for s in bad:
    for v in generators:
        gaps=tuple(g+2*t for g,t in zip(s['gaps'],v));lam=partition_from_gaps(gaps)
        row={'seed_gaps':s['gaps'],'increment':v,'gaps':gaps,'partition':lam,
             'traces':traces(lam),'multiplicities':multiplicities(lam)}
        increment_cases.append(row)
        if min(row['multiplicities'])==0:failures.append((s['gaps'],v))
assert set(failures)=={((1,1,1,1),(5,0,0,0)),((1,1,1,1),(0,0,0,5)),
                       ((1,1,1,6),(0,0,0,5)),((6,1,1,1),(5,0,0,0))}
classes=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
ray=[]
for cycles in classes:
    h=complete_values(cycles,5);value=0
    for p in permutations(range(3)):
        sign=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
        term=sign
        for i in range(3):
            index=(3,2,1)[i]-i+p[i]
            term*=h[index] if index>=0 else 0
        value+=term
    ray.append(value)
assert tuple(ray)==(64,0,0,-2,0,0,-1)
ray_multiplicities=tuple(sum(s*c*t for s,c,t in zip(SIZES,row,ray))//120 for row in CHARS)
assert ray_multiplicities==(0,2,3,3,3,2,0)
canonical=[]
for lam,expected in (((12,7,3,2,1),2),((12,5,4,3,1),1),
                     ((10,8,4,2,1),3),((9,7,6,3,0),2)):
    values=multiplicities(lam);assert values[0]==expected
    canonical.append({'partition':lam,'target_multiplicity':expected,
                      'known_CIM_kernel_multiplicity':1,'actual_image_multiplicity':expected-1,
                      'traces':traces(lam),'multiplicities':values})
result={'statement':'G-028','seeds':seeds,'zero_sum_generators':generators,
        'bad_seed_increment_cases':increment_cases,'bad_increments':failures,
        'ray_S321_traces':ray,'ray_multiplicities':ray_multiplicities,
        'strict_degree_five_kernel_components':canonical}
(HERE/'FIVE_ROW_STRICT_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'seeds':len(seeds),'all_label_positive_seeds':76-len(bad),
                  'bad_seed_increment_cases':len(increment_cases),'bad_increments':len(failures),
                  'zero_sum_generators':len(generators),'ray_traces':ray,
                  'degree_five_image_multiplicities':[r['actual_image_multiplicity'] for r in canonical]}))
