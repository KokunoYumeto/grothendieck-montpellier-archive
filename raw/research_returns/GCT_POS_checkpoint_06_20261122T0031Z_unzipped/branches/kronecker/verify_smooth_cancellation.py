"""Exact algebraic certificates for K-022, including the uniform identity."""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

root = Path(__file__).resolve().parent
t, u, x = sp.symbols('t u x')
weights = (1, 2, 3, 5, 7)
pairs = list(combinations(range(5), 2))
variables = sp.symbols('p12 p13 p14 p15 p23 p24 p25 p34 p35 p45')
p = dict(zip(pairs, variables))
pfaffians = []
for i, j, k, l in combinations(range(5), 4):
    pfaffians.append(p[i, j] * p[k, l] - p[i, k] * p[j, l] + p[i, l] * p[j, k])
fixed_pairs = [pair for pair in pairs if sum(weights[i] for i in pair) % 8 == 0]
assert fixed_pairs == [(0, 4), (2, 3)]
restriction = {p[pair]: 0 for pair in pairs if pair not in fixed_pairs}
assert {sp.expand(f.subs(restriction)) for f in pfaffians} == {0, p[0, 4] * p[2, 3]}

phi8 = t ** 4 + 1
local_receipts = []
for fixed_pair, sign in zip(fixed_pairs, (1, -1)):
    point = {variable: int(pair == fixed_pair) for pair, variable in p.items()}
    jacobian = sp.Matrix(pfaffians).jacobian(variables).subs(point)
    assert jacobian.rank() == 3
    tangent_basis = jacobian.nullspace()
    assert len(tangent_basis) == 7
    tangent_weights = []
    for vector in tangent_basis:
        nonzero = [j for j, value in enumerate(vector) if value]
        assert len(nonzero) == 1
        tangent_weights.append(sum(weights[i] for i in pairs[nonzero[0]]))
    moving = sorted(weight for weight in tangent_weights if weight % 8)
    assert len(moving) == 6
    determinant = sp.rem(sp.prod(1 - t ** weight for weight in moving), phi8, t)
    local = sp.invert(determinant, phi8, t)
    expected = sign * (t + t ** 3) / 16
    assert sp.rem(local - expected, phi8, t) == 0
    local_receipts.append({'pair_one_based': [i + 1 for i in fixed_pair],
                           'jacobian_rank': 3, 'moving_weights': moving,
                           'local_coefficient': str(expected)})

S = sum(weights)
P = 1 - sum(t ** (S - weight) for weight in weights) + sum(t ** (S + weight) for weight in weights) - t ** (2 * S)
D = sp.prod(1 - t ** (weights[i] + weights[j]) for i, j in pairs)
Q = sum(coefficient * t ** j for j, coefficient in enumerate(
    [1, 1, 1, 2, 1, 1, 2, 1, 3, 4, 3, 4, 3, 1, 2, 1, 1, 2, 1, 1, 1]))
assert sp.expand(P - (1 - t) ** 3 * sp.cyclotomic_poly(2, t) * sp.cyclotomic_poly(3, t)
                 * sp.cyclotomic_poly(4, t) * sp.cyclotomic_poly(8, t) ** 2 * Q) == 0
exponents = {1: 7, 2: 5, 3: 3, 4: 3, 5: 2, 6: 2, 7: 1, 9: 1, 10: 1, 12: 1}
reduced_D = (1 - t) ** 7 * sp.prod(sp.cyclotomic_poly(order, t) ** exponent
                                  for order, exponent in exponents.items() if order != 1)
assert sp.expand(P * reduced_D - Q * D) == 0
assert sp.gcd(Q, reduced_D) == 1
assert sp.gcd(phi8, reduced_D) == 1

uniform_P = 1 - (u ** 9 / t + u ** 8 + u ** 7 * t + u ** 7 / t + u ** 5 * t) \
    + (u ** 9 * t + u ** 10 + u ** 11 / t + u ** 11 * t + u ** 13 / t) - u ** 18
uniform_factor = (u ** 2 - 1) * (u ** 2 + 1) ** 2 / t * (
    t ** 2 * u ** 5 + u ** 7 - t * (u ** 12 - u ** 10 + 2 * u ** 8
                                   - 2 * u ** 6 + 2 * u ** 4 - u ** 2 + 1))
assert sp.expand(uniform_P - uniform_factor) == 0
first_product = 4 * (1 + x ** 2) * (1 + x ** -2) * (1 - sp.I * x) * (1 - sp.I / x)
second_product = 4 * (1 + x ** 2) * (1 + x ** -2) * (1 + sp.I * x) * (1 + sp.I / x)
assert sp.simplify(first_product + 4 * sp.I * (x + 1 / x) ** 3) == 0
assert sp.simplify(second_product - 4 * sp.I * (x + 1 / x) ** 3) == 0
for M in (8, 16, 32, 64, 128):
    m = M // 4
    a = (1, m, 2 * m - 1, 2 * m + 1, 4 * m - 1)
    assert [pair for pair in pairs if sum(a[i] for i in pair) % M == 0] == fixed_pairs
    numerator = 1 - sum(t ** (9 * m - ai) for ai in a) + sum(t ** (9 * m + ai) for ai in a) - t ** (18 * m)
    assert sp.expand(numerator - uniform_P.subs(u, t ** m)) == 0
    assert sp.rem(numerator, sp.cyclotomic_poly(M, t) ** 2, t) == 0

receipt = {'status': 'PASS', 'uniform_numerator_identity': 'PASS',
           'uniform_opposite_moving_determinants': 'PASS',
           'M8_complete_fixed_scheme': 'two reduced lines with equation p15*p34=0',
           'M8_locals': local_receipts, 'M8_reduced_denominator_cyclotomic_exponents': exponents,
           'M8_reduced_numerator_coefficients': [int(Q.coeff(t, j)) for j in range(21)],
           'finite_uniform_specializations': [8, 16, 32, 64, 128]}
(root / 'smooth_cancellation_checks.json').write_text(json.dumps(receipt, indent=2))
print('PASS K-022: exact two smooth fixed curves, opposite local residues, reduced M8 Hilbert series, uniform factor identity and moving products.')
