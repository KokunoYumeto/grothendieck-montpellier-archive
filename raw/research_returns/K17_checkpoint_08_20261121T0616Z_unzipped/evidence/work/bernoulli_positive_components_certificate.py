"""Exact small Bernoulli numbers and complete bounded prime support.

Uses the defining rational recurrence, not numerical approximations.
Every asserted prime is verified by division through its square root.
"""
from fractions import Fraction
from math import comb, isqrt, prod
from pathlib import Path
from hashlib import sha256
import json

FACTORS = {
    2: {}, 4: {}, 6: {}, 8: {}, 10: {5: 1},
    12: {691: 1}, 14: {7: 1}, 16: {3617: 1},
    18: {43867: 1}, 20: {283: 1, 617: 1},
    22: {11: 1, 131: 1, 593: 1},
    24: {103: 1, 2294797: 1},
    26: {13: 1, 657931: 1},
    28: {7: 1, 9349: 1, 362903: 1},
    30: {5: 1, 1721: 1, 1001259881: 1},
    32: {37: 1, 683: 1, 305065927: 1},
}


def trial_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, isqrt(n) + 1, 2))


bernoulli = [Fraction(1)]
for n in range(1, 33):
    bernoulli.append(-sum((comb(n + 1, k) * bernoulli[k]
                          for k in range(n)), Fraction(0)) / (n + 1))
assert bernoulli[1] == Fraction(-1, 2)
assert all(bernoulli[n] == 0 for n in range(3, 33, 2))

# A second exact identity checks the recurrence through power sums.
# Faulhaber's formula for sum_{a=0}^{h-1} a^n at three distinct h.
for n in range(1, 33):
    for h in (2, 5, 11):
        rhs = sum((comb(n + 1, k) * bernoulli[k] * h ** (n + 1 - k)
                   for k in range(n + 1)), Fraction(0)) / (n + 1)
        assert rhs == sum(a ** n for a in range(h))

rows = []
for n, factors in FACTORS.items():
    b = bernoulli[n]
    assert prod(p ** v for p, v in factors.items()) == abs(b.numerator)
    assert all(p < 2 ** 31 and trial_prime(p) for p in factors)
    rows.append({'index': n, 'numerator': b.numerator,
                 'denominator': b.denominator,
                 'absolute_numerator_factorization': factors,
                 'all_factors_prime_below_2pow31': True})

report = {
    'status': 'PASS: complete exact Bernoulli prime support for even indices2..32',
    'convention': 'B1=-1/2; defining recurrence and three exact power-sum checks',
    'small_prime_proof': 'trial division through each integer square root',
    'largest_prime_factor': max(p for factors in FACTORS.values() for p in factors),
    'rows': rows,
    'source_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
