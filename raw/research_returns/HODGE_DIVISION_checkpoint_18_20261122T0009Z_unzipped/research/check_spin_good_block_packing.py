"""Independent finite verification of the elementary 3--6 block packing lemma."""
from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
from itertools import product
import hashlib,json,time
R=Path(__file__).resolve().parent
start=time.perf_counter();stamp=datetime.now(timezone.utc).isoformat()
weights=(3,4,5,6)
minimal=[]
for counts in product(range(4),repeat=4):
    total=sum(a*b for a,b in zip(counts,weights))
    if total>=8 and all(not c or total-w<8 for c,w in zip(counts,weights)):
        minimal.append(counts)
assert max(sum(a*b for a,b in zip(c,weights)) for c in minimal)==12
assert [c for c in minimal if sum(a*b for a,b in zip(c,weights))==12]==[(0,0,0,2)]
@lru_cache(None)
def maximum_groups(counts):
    result=0
    for pattern in minimal:
        if all(a>=b for a,b in zip(counts,pattern)):
            remaining=tuple(a-b for a,b in zip(counts,pattern))
            result=max(result,1+maximum_groups(remaining))
    return result
cases=0;worst=-1;witness=None
for a in range(34):
 for b in range((100-3*a)//4+1):
  for c in range((100-3*a-4*b)//5+1):
   for d in range((100-3*a-4*b-5*c)//6+1):
    counts=(a,b,c,d);total=3*a+4*b+5*c+6*d
    groups=maximum_groups(counts)
    if groups<8 and total>worst:worst,witness=total,counts
    if total>=91:assert groups>=8
    cases+=1
assert worst==90 and maximum_groups((0,0,0,15))==7
result={'status':'PASS','started_utc':stamp,'elapsed_seconds':time.perf_counter()-start,
        'all_count_vectors_through_total100':cases,'minimal_cover_patterns':minimal,
        'max_total_without_eight_groups':worst,'witness':witness,
        'scope':'Exact finite supplement; the universal maximal-packing argument is a separate written proof. Good dimensions must be exactly in{3,4,5,6}.',
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'spin_good_block_packing_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
