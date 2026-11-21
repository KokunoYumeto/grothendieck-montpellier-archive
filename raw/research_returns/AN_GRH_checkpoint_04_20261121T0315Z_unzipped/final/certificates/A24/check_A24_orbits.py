#!/usr/bin/env python3
"""Exact small residue-field checks for A24; no geometric existence assertion."""
import json
from fractions import Fraction
from pathlib import Path


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def pair_mul(v, w, p):
    # beta^2 = beta - 4, pairs represent a+b*beta.
    a, b = v
    c, d = w
    return ((a*c - 4*b*d) % p, (a*d+b*c+b*d) % p)


def pair_pow(v, exponent, p):
    out = (1, 0)
    while exponent:
        if exponent & 1:
            out = pair_mul(out, v, p)
        v = pair_mul(v, v, p)
        exponent //= 2
    return out


def mat_mul(a, b, p):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) % p
                       for j in range(2)) for i in range(2))


def mat_pow(a, exponent, p):
    out = ((1, 0), (0, 1))
    while exponent:
        if exponent & 1:
            out = mat_mul(out, a, p)
        a = mat_mul(a, a, p)
        exponent //= 2
    return out


rows = []
for p, expected in [(7, 24), (11, 60), (13, 84)]:
    assert prime_factors(p) == [p]
    assert pow((-15) % p, (p-1)//2, p) == p-1
    beta = (0, 1)
    matrix = ((0, (-4) % p), (1, 1))
    assert pair_pow(beta, p+1, p) == (4 % p, 0)
    assert pair_pow(beta, expected, p) == (1, 0)
    assert mat_pow(matrix, expected, p) == ((1, 0), (0, 1))
    witnesses = []
    for q in prime_factors(expected):
        exponent = expected // q
        pair = pair_pow(beta, exponent, p)
        mat = mat_pow(matrix, exponent, p)
        assert pair != (1, 0)
        assert mat != ((1, 0), (0, 1))
        assert (mat[0][0], mat[1][0]) == pair
        witnesses.append({'prime_divisor': q, 'exponent': exponent,
                          'quadratic_pair': pair, 'matrix': mat})
    assert pair_pow(beta, expected//2, p) == (p-1, 0)
    assert expected*(expected-1) > 2*(p*p-1)
    rows.append({'ell': p, 'beta_order': expected,
                 'signed_beta_group_order': expected,
                 'signed_uniform_lower_bound': 2*(p-1),
                 'sidon_left': expected*(expected-1),
                 'sidon_right': 2*(p*p-1), 'witnesses': witnesses})

split_classes = []
for a in [1, 2, 4, 7, 8, 11, 13, 14]:
    chi3 = 1 if a % 3 == 1 else -1
    chi5 = 1 if a % 5 in (1, 4) else -1
    if chi3*chi5 == 1:
        split_classes.append(a)
assert split_classes == [1, 2, 4, 8]
assert 4159 % 15 in split_classes

forced_ratio = (Fraction(-1, 6)/Fraction(5, 6)
                * Fraction(-1, 20)/Fraction(19, 20))
assert forced_ratio == Fraction(1, 95)
signed_density_factor = Fraction(3, 2)*Fraction(1, 2)*(1+forced_ratio)
primitive_density_factor = Fraction(1, 2)*(1+forced_ratio)
assert signed_density_factor == Fraction(72, 95)
assert primitive_density_factor == Fraction(48, 95)

result = {
    'status': 'PASS',
    'polynomial': 'T^2-T+4',
    'scope': 'Exact finite arithmetic only; the uniform proof does not depend on these small-prime checks.',
    'small_residue_orders': rows,
    'split_classes_mod15': split_classes,
    'A13_witness_residue_mod15': 4159 % 15,
    'forced_Euler_factor_ratio': str(forced_ratio),
    'conditional_signed_split_density_factor_times_Artin_constant': str(signed_density_factor),
    'conditional_primitive_split_density_factor_times_Artin_constant': str(primitive_density_factor),
    'density_scope': 'Only rational-factor algebra checked computationally; natural densities require the cited Lenstra theorem and stated Dedekind-GRH families.'
}
target = Path(__file__).with_suffix('.json')
target.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'status': 'PASS', 'output': str(target),
                  'small_orders': [[r['ell'], r['beta_order']] for r in rows],
                  'density_factors': [str(signed_density_factor), str(primitive_density_factor)]}, indent=2))
