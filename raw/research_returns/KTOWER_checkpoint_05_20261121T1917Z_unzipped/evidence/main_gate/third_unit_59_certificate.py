"""Exact p=59 comparison for KT-COMPOSITUM-PRATIONAL-OBSTRUCTION.

Independent conductor-sum computation: no prefix formula or broad scan.
Only the Python standard library and exact integer/rational arithmetic.
"""
from fractions import Fraction
from math import comb, isqrt, prod
from pathlib import Path
import json


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def legendre(a, q):
    residue = pow(a % q, (q - 1) // 2, q)
    return -1 if residue == q - 1 else residue


def character(a, odd_prime_factors):
    if a % 2 == 0:
        return 0
    result = 1 if a % 4 == 1 else -1
    for q in odd_prime_factors:
        result *= legendre(a, q)
    return result


def third_residue(p, conductor, odd_prime_factors):
    assert conductor == 4 * prod(odd_prime_factors)
    assert all(is_prime(q) for q in odd_prime_factors)
    assert conductor % p
    modulus = p * p
    numerator = 0
    for a in range(1, conductor * p + 1):
        if a % p:
            teich = pow(a, p, modulus)
            numerator += a * character(a, odd_prime_factors) * pow(teich, p - 3, modulus)
    numerator %= modulus
    assert numerator % p == 0
    return numerator // p * pow(conductor, -1, p) % p


def main():
    p = 59
    assert is_prime(p)
    bernoulli = [Fraction(1)]
    for n in range(1, 45):
        bernoulli.append(-sum(Fraction(comb(n + 1, j)) * bernoulli[j]
                              for j in range(n)) / (n + 1))
    beta = bernoulli[44] / 44
    assert beta == Fraction(-2530297234481911294093, 2760)
    assert beta.denominator % p
    assert beta.numerator % p == 0 and beta.numerator % (p * p) != 0
    plus = third_residue(p, 244, [61])
    minus = third_residue(p, 228, [3, 19])
    assert (plus, minus) == (13, 5)
    report = {
        'result': 'PASS',
        'scope': 'Single exact comparison at p=59; no general third-unit claim',
        'p': p,
        'prime_trial_division_through': isqrt(p),
        'B44': str(bernoulli[44]),
        'B44_over_44': str(beta),
        'valuation_59': 1,
        'direct_mod_p_squared_residues': {'-244': plus, '-228': minus},
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
