"""Exact deck-character count for the Schoen generic fibre in C28."""
from collections import Counter
from itertools import product
from pathlib import Path

characters=Counter()
orbits=Counter()
seen=set()
rank_two=[]
for a in product(range(5),repeat=4):
    if sum(a)%5:
        continue
    r=sum(x!=0 for x in a)
    characters[r]+=1
    if not r or a in seen:
        continue
    orbit={tuple(k*x%5 for x in a) for k in range(1,5)}
    assert len(orbit)==4
    seen.update(orbit)
    orbits[r]+=1
    if r==4:
        rank_two.append(orbit)
assert characters=={0:1,2:24,3:48,4:52}
assert orbits=={2:6,3:12,4:13}
assert sum(orbits[r]*2*(r-2) for r in orbits)==76
# Supplementary exact fact useful for a separate monodromy calculation.
assert all(any(sum(a)==10 for a in orbit) for orbit in rank_two)
result=(f'Characters: {dict(characters)}\n'
        f'Rational orbits: {dict(orbits)}\n'
        'Genus: 76\n'
        'Every rank-two orbit has a sum-ten representative.\n'
        'All exact checks PASS\n')
Path('work/check_C28_characters_output.txt').write_text(result)
print(result)
