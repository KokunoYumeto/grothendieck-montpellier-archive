"""Exact rational checks accompanying the whole-proof quartic refinement audit."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

s = sum((F(39, 20)**j / factorial(j) for j in range(9)), F(0))
assert s - 7 == F(3130848254169, 114688000000000) > 0
assert F(239, 960) == (F(39, 10) + F(1, 12)) / 16 < F(1, 4)
assert F(1, 216) + F(1, 81) == F(11, 648) < F(1, 32)
assert 1 + F(64, 343) + F(1, 2401) == 1 + F(449, 2401) < F(4, 3)
data = {'status': 'PASS', 'exponential_partial_sum_minus_7': str(s-7),
        'coefficient': str(F(239, 960)), 'dimension_envelope': str(F(11, 648)),
        'factor_bound': str(1+F(449, 2401)),
        'scope': 'Exact finite rational identities; infinite dimension estimate is proved algebraically in the accompanying review.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(data, indent=2)+'\n')
print(json.dumps(data, indent=2))
