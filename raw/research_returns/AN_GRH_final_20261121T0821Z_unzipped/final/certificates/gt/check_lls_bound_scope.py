#!/usr/bin/env python3
"""Exact evaluation of the LLS Theorem 1.1 upper-bound expression.

This checks the size of the theorem's bound, not an actual least generator.
The two explicit factorizations are deliberately supplied, not inferred.
"""
from fractions import Fraction as F
from math import prod
from pathlib import Path
import csv
from verify_gt_units import log_interval


def enclose(lo, hi, denominator=10**8):
    a = lo.numerator * denominator // lo.denominator
    b = -((-hi.numerator * denominator) // hi.denominator)
    return F(a, denominator), F(b, denominator)


def log_rational(x):
    k = 0
    r = x
    while r >= 2:
        r /= 2
        k += 1
    assert 1 <= r < 2
    t = (r - 1) / (r + 1)
    power = t
    s = F(0)
    terms = 32
    for j in range(terms):
        s += 2 * power / (2 * j + 1)
        power *= t * t
    tail = 2 * power / ((2 * terms + 1) * (1 - t*t))
    l2, h2 = log_interval(2, terms)
    return enclose(k*l2+s, k*h2+s+tail)


def evaluate(primes, outer_lo, outer_hi):
    q = prod(primes)
    l, h = enclose(*log_interval(q, 32))
    ll, _ = log_rational(l)
    _, lh = log_rational(h)
    sl = sh = F(0)
    for p in primes:
        pl, ph = enclose(*log_interval(p, 32))
        sl += pl / (p - 1)
        sh += ph / (p - 1)
    al = max(F(0), 2*ll - F(8,5) - sh)
    ah = max(F(0), 2*lh - F(8,5) - sl)
    bl = max(F(0), 2*ll + 3 + 2*len(primes)*ll*ll/h - 2*ah)
    bh = max(F(0), 2*lh + 3 + 2*len(primes)*lh*lh/l - 2*al)
    ratio_lo = (l+bl)**2 / h**2
    ratio_hi = (h+bh)**2 / l**2
    assert ratio_lo > 2
    assert F(outer_lo) < ratio_lo <= ratio_hi < F(outer_hi)
    # The ratio assertion is exact; displayed decimal approximations are not
    # used in its verification.
    print(f'q={q}; prime factors={primes}; exact comparison (log q+B(q))^2 > 2(log q)^2: PASS')
    print(f'ratio approximately [{float(ratio_lo):.9f}, {float(ratio_hi):.9f}]')
    return {
        'N': q,
        'prime_factorization': '*'.join(map(str, primes)),
        'certified_strict_ratio_lower': outer_lo,
        'certified_strict_ratio_upper': outer_hi,
        'ratio_greater_than_2_exactly_verified': 'True',
        'scope': 'LLS Theorem 1.1 bound expression, not actual least generator',
    }


if __name__ == '__main__':
    rows = [
        evaluate([2, 3, 5, 7, 11, 13], '4.98743', '4.98744'),
        evaluate([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43], '2.02303', '2.02304'),
    ]
    destination = Path(__file__).resolve().parent / 'LLS_BOUND_EXPRESSION_CHECKS.tsv'
    with destination.open('w', newline='') as f:
        writer = csv.DictWriter(f, delimiter='\t', fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
