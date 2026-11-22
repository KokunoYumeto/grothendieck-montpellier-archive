#!/usr/bin/env python3
"""Exact arithmetic accompanying D-BI-20.

Published degree expressions are transcribed mathematical inputs, not a
reconstruction of their classification proofs. All comparisons use integers
or Fractions. No period-rank assertion is inferred from these computations.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd, isqrt
from pathlib import Path
import json


def ceil(x):
    return -(-x.numerator // x.denominator)


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def prime_power(n):
    for p in range(2, n + 1):
        if prime(p):
            r = n
            while r % p == 0:
                r //= p
            if r == 1:
                return True
    return False


@lru_cache(None)
def phi(n, q):
    a = q ** n - 1
    for d in range(1, n):
        if n % d == 0:
            b = phi(d, q)
            assert a % b == 0
            a //= b
    return a


def classical_at_minimum_rank(q):
    # Hoffman Table 1. Each family increases with its displayed rank.
    return {
        'PSL_n_n3': F(q**3 - 1, q - 1) - 2,
        'PSp_2n_n2': (F(q**2 - 1, 2) if q % 2 else
                       F((q**2 - 1)*(q**2 - q), 2*(q+1))),
        'odd_orthogonal_n3': F(q**6 - 1, q**2 - 1) - 2,
        'plus_orthogonal_n4': F((q**4 - 1)*(q**3 + q), q**2 - 1) - 2,
        'minus_orthogonal_n4': F((q**4 + 1)*(q**3 - q), q**2 - 1) - 1,
        'PSU_even_n2': F(q**4 - 1, q + 1),
        'PSU_odd_n1': F(q**3 - q, q + 1),
    }


def exceptional_minima(q):
    # Luebeck Theorem 2.1 and first degrees of Sections 5.3--5.10.
    # q here is the actual field size, including in the twisted rows.
    ph = lambda n: phi(n, q)
    assert q % 3
    out = {
        'G2': q**3 + (1 if q % 3 == 1 else -1),
        '3D4': q*ph(12),
        'F4': (ph(3)*ph(6)*ph(12) if q % 2 else
               F(q*ph(1)**2*ph(3)**2*ph(8), 2)),
        '2E6': q*ph(8)*ph(18),
        'E6': q*ph(8)*ph(9),
        'E7': q*ph(7)*ph(12)*ph(14),
        'E8': q*ph(4)**2*ph(8)*ph(12)*ph(20)*ph(24),
    }
    if q == 32:
        # Luebeck Sections 5.1, 5.5 use u=sqrt(q).
        sq = isqrt(q//2)
        assert 2*sq*sq == q
        out['2B2'] = (q-1)*sq
        out['2F4'] = (q-1)*sq*(q+1)**2*(q*q-q+1)
    return {k: F(v) for k, v in out.items()}


qs = [q for q in range(28, 47) if prime_power(q)]
assert qs == [29, 31, 32, 37, 41, 43]
expected_upper = [87, 45, 33, 21, 15, 15]
rows = []
for q, U in zip(qs, expected_upper):
    # 9/q >= 1/(sqrt(q)-1) iff (q+9)^2 <=81q.
    assert (q + 9)**2 <= 81*q
    continuous = (6*q)//(q-27)
    allowed = [e for e in range(3, continuous+1)
               if 12*ceil(F(e*(q-9), 4*q)) <= 2*e+6]
    assert max(allowed) == U
    low = F(q*q-1, 2)
    cr = classical_at_minimum_rank(q)
    assert all(a >= low > U for a in cr.values())
    er = exceptional_minima(q)
    assert all(a > U for a in er.values())
    assert all(a >= q*(q-1) for k,a in er.items() if k != '2B2')
    d0 = (q-1)//gcd(2,q-1)
    assert d0*d0 > U  # excludes every t>=2, since e=a^t
    rows.append({'q':q,'continuous_upper':continuous,
                 'allowed_total_degrees':allowed,'maximum':U,
                 'classical_coarse_lower':str(low),
                 'classical_minimum_rank_rows':{k:str(v) for k,v in cr.items()},
                 'exceptional_first_degrees':{k:str(v) for k,v in er.items()},
                 'PSL2_projective_minimum':d0,'minimum_square':d0*d0})

byq = {r['q']:r for r in rows}
for q in (41,43):
    assert byq[q]['PSL2_projective_minimum'] > byq[q]['maximum']
degrees37 = [1,18,19,36,37,38]
assert not (set(degrees37) & set(byq[37]['allowed_total_degrees']))
assert byq[37]['allowed_total_degrees'] == [3,4,5,9,10,15,21]
assert [x for x in range(29) if x*x % 29 == 28] == [12,17]
assert not [x for x in range(31) if x*x % 31 == 30]

result = {
    'status':'PASS',
    'scope':'Exact arithmetic only; published degree tables are explicit inputs',
    'fields':rows,
    'SL2_37_character_degrees':degrees37,
    'SL2_37_allowed_degree_intersection':[],
    'square_root_minus_one_mod29':[12,17],
    'minus_one_nonsquare_mod31':True,
    'cover_exceptions_input':[4,9],
    'universal_arguments_not_computational_samples':[
        'equal factor degrees from transitive conjugation',
        'semisimple inverse conjugacy by centralizer determinant surjectivity',
        'inverse conjugacy for q even or q congruent1 mod4',
        'class-inverting diagonal automorphism for q31',
        'no additional automorphisms on the perfect central cover',
        'scalar-only normalizer when the core character is nonreal'],
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','fields':qs,'upper_bounds':expected_upper,
                  'SL2_37_intersection':[], 'output':str(out)}))
