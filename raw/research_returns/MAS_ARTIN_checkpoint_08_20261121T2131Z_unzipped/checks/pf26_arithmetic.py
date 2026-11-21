"""Exact integer checks for MA-PF-002 and MA-PF-005.

These finite computations supplement the written proofs; they do not certify
PF26's divisor, norm, or factoring algorithms.
"""
import json
from math import isqrt
from pathlib import Path


def is_prime(n):
    return n >= 2 and all(n % a for a in range(2, isqrt(n) + 1))


def valuation(n, r):
    assert n > 0
    v = 0
    while n % r == 0:
        n //= r
        v += 1
    return v


def order(p, r):
    a = p % r
    s = 1
    while a != 1:
        a = (a * p) % r
        s += 1
    return s


primes = [p for p in range(2, 2001) if is_prime(p)]
small_primes = [r for r in range(3, 50) if is_prime(r)]
pairs = 0
for p in primes:
    for r in small_primes:
        if p == r:
            continue
        s = order(p, r)
        a = valuation(pow(p, s) - 1, r)
        b = valuation(pow(p, r - 1) - 1, r)
        assert a == b
        assert (a > 1) == (pow(p, r - 1, r * r) == 1)
        pairs += 1

cubic_checks = 0
for p in primes:
    if p <= 3:
        continue
    for m in range(1, 9):
        old = (p - 1) * m % 3 != 0 and valuation(pow(p, order(p, 3)) - 1, 3) > 1
        new = p % 9 == 8 and m % 3 != 0
        assert old == new
        cubic_checks += 1

p = 269
B = 20 + 4 * (p.bit_length() + 1)
assert is_prime(p) and B == 60
assert p * p - 1 == 72360 == (3 ** 3) * 2680
assert valuation(p * p - 1, 3) == 3
assert p < B ** 200000
out = {
    "statement_ids": ["MA-PF-002", "MA-PF-005"],
    "type": "exact integer computation, supplementary to proofs",
    "valuation_pairs_checked": pairs,
    "p_range": "prime p <= 2000",
    "r_range": "odd prime r < 50, r != p",
    "cubic_equivalences_checked": cubic_checks,
    "m_range": "1 <= m <= 8",
    "example": {
        "p": p,
        "prime_trial_division_remainders": {str(a): p % a for a in range(2, isqrt(p) + 1)},
        "d": 3,
        "m": 1,
        "B": B,
        "valuation_3_p_squared_minus_1": 3,
        "arithmetic_residual_set": [3],
        "PF26_branch": "small characteristic, unconditional scalar search",
    },
    "all_assertions_passed": True,
    "scope_limit": "No implementation or formal verification of the PF26 norm or factoring algorithm.",
}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
