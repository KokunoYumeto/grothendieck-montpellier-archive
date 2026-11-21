#!/usr/bin/env python3
"""Independent rational-interval check of BI18; no author code imported."""
from fractions import Fraction as F
from pathlib import Path
import json

def floor(x):
    return x.numerator // x.denominator

def ceiling(x):
    return -floor(-x)

def by_ceiling_intervals(c, factor=4):
    a = (1-c)/factor
    slope = 12*a-2
    assert slope > 0
    upper = floor(F(6)/slope)
    ans = set()
    for k in range(1, ceiling(a*upper)+1):
        lo = max(3, floor(F(k-1)/a)+1, 6*k-3)
        hi = min(upper, floor(F(k)/a))
        ans.update(range(lo, hi+1))
    return upper, sorted(ans)

small = []
for q, claimed in [(29,87),(31,45),(32,33),(37,21),(41,15),(43,15)]:
    assert q+9 > 0 and (q+9)**2 <= 81*q
    u, a = by_ceiling_intervals(F(9,q))
    assert max(a) == claimed
    small.append({'q':q,'continuous_max':u,'possible_degrees':a})

# Strict c<1/5 gives minimum support at least floor(e/5)+1.
# Enumerate its constant-value blocks, without the author's degree loop.
large = []
for k in range(1,4):
    lo = max(3,5*(k-1),6*k-3)
    hi = min(14,5*k-1)
    large.extend(range(lo,hi+1))
assert large == [3,4,9]
assert by_ceiling_intervals(F(0))[1] == [3,4]
assert by_ceiling_intervals(F(9,16),2) == (9,[3,4,9])

# ESD refinement: split by degree parity and by its support ceiling.
c = F(9,19); a=(1-c)/4
esd_upper=floor(F(12)/(3-5*c))
esd=[]
for parity in (0,1):
    for k in range(1,ceiling(a*esd_upper)+1):
        lo=max(3,floor(F(k-1)/a)+1,10*k+parity-6)
        hi=min(esd_upper,floor(F(k)/a))
        esd.extend(e for e in range(lo,hi+1) if e%2==parity)
esd=sorted(esd)
assert esd_upper==19
assert esd==[4,5,6,7,14,15]

out={'status':'PASS','method':'exact ceiling-interval enumeration, independent of author code',
     'small_fields':small,'q_ge_47':large,'extraspecial':[3,4],
     'scalar_q_ge_16':[3,4,9],'esd_q19_upper':esd_upper,'esd_q19_degrees':esd,
     'scope':'Finite rational arithmetic only; the published character estimate is an explicit input.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
