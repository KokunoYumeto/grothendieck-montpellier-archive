#!/usr/bin/env python3
"""Finite arithmetic checks for MA-CH-003/004; not an analytic proof."""
import json
import math
from pathlib import Path


def valuation(n, p):
    assert n != 0
    n = abs(n)
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def gf4_mul(a, b):
    # F_2[T]/(T^2+T+1), with binary coefficients.
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        if a & 4:
            a ^= 7
        b >>= 1
    return out


def gf4_pow(a, n):
    out = 1
    for _ in range(n):
        out = gf4_mul(out, a)
    return out


assert all(269 % p for p in range(2, math.isqrt(269) + 1))
assert 269 % 3 == 2
f_at_minus_one = -1 - 269
derivative_at_minus_one = 3
assert valuation(f_at_minus_one, 3) == 3
assert valuation(derivative_at_minus_one, 3) == 1
assert valuation(f_at_minus_one, 3) > 2 * valuation(derivative_at_minus_one, 3)
roots = [a for a in range(4) if gf4_pow(a, 3) ^ 1 == 0]
assert roots == [1, 2, 3]
# Derivative of X^3-1 in characteristic 2 is X^2.
assert all(gf4_pow(a, 2) != 0 for a in roots)
assert 3 * 269**2 == 217083

data = {
    "status": "PASS",
    "scope": "Finite arithmetic certificate only; complete mathematical proofs are in modules/characters.tex.",
    "p": 269,
    "p_is_prime": True,
    "p_mod_3": 2,
    "v3_f_minus_one": 3,
    "v3_derivative_minus_one": 1,
    "strong_hensel_strict_inequality": "3 > 2",
    "gf4_polynomial": "T^2+T+1",
    "gf4_distinct_roots_x3_minus_1": roots,
    "conductor_norm_from_proved_local_exponents": 269**2,
    "arithmetic_conductor": 217083,
    "prime_ideal_norm_for_gap": 4,
    "prime_gap_exact": "log(4)/sqrt(4) = log(2)",
}
destination = Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(data, indent=2) + "\n")
print(json.dumps(data))
