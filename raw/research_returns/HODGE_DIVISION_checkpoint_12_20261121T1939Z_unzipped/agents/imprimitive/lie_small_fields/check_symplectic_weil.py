#!/usr/bin/env python3
"""Exact finite arithmetic after the proved all-rank bounds. No table input."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

assert F(26,15)**2 > 3
assert F(9,16) < F(3,5)
q3n4 = (27*F(26,15)+1)/80
q3n3 = (9*F(26,15)+1)/26
assert q3n4 == F(239,400) < F(3,5)
assert q3n3 == F(83,130) < F(2,3)
assert F(18,80) < F(3,5)
exceptional = []
for a in (13,14):
    # nu > a/6, and nu is an integer.
    low = a//6+1
    assert low == 3 and F(low,a) >= F(1,5)
    exceptional.append({'degree':a,'minimum_integer_nu':low})
for a in (4,5):
    assert F(1,a) >= F(1,5)
possible = [e for e in range(4,16) if 12*((e+4)//5) <= 2*e+6]
assert possible == [4,5,9,10,15]
# q^n<=31, q odd prime power and n>=2: q<6, so only q=3,5;
# n<4, except q=3,n=3. These are all possibilities, not samples.
pairs = [(3,2),(3,3),(5,2)]
degrees = []
survivors = []
for q,n in pairs:
    for s in (-1,1):
        a = (q**n+s)//2
        item = {'q':q,'n':n,'sign':s,'degree':a,
                'necessary_branch_inequality':12*((a+4)//5)<=2*a+6}
        degrees.append(item)
        if item['necessary_branch_inequality']:
            survivors.append([q,n,a])
assert survivors == [[3,2,4],[3,2,5]]
assert 4**2 > 15
p=Path(__file__).with_name('symplectic_weil_section.tex')
out={'status':'PASS','scope':'exact finite arithmetic after proved uniform bounds; not group enumeration or independent peer review',
     'rational_q3_n4_upper':str(q3n4),'rational_q3_n3_upper':str(q3n3),
     'exceptional_integer_bounds':exceptional,'possible_total_degrees':possible,
     'complete_small_prime_power_cases':degrees,'survivors':survivors,
     'proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
