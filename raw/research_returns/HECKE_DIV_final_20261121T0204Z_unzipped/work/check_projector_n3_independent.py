"""Independent integer-pair verification of the sixfold Weil projector.

No symbolic algebra is used. Eigenvalues are reconstructed, not trusted as input.
"""
from pathlib import Path
import json
import math

root = Path(__file__).parent
row = json.loads((root / 'projector_n3.json').read_text())

def mul(a, b):
    x, y = a
    z, w = b
    return x*z-y*w, x*w+y*z-y*w

def power(a, n):
    out = (1, 0)
    for _ in range(n):
        out = mul(out, a)
    return out

def horner(coefficients, value):
    out = (0, 0)
    for coefficient in reversed(coefficients):
        x, y = mul(out, value)
        out = x+coefficient, y
    return out

n = row['n']
assert n == 3
a, abar = (3, 1), (2, -1)
assert mul(a, abar) == (7, 0)
eigenvalues = [mul(power(a, j), power(abar, 2*n-j)) for j in range(2*n+1)]
assert eigenvalues == [tuple(x) for x in row['eigenvalues_a_plus_b_omega']]
assert len(set(eigenvalues)) == 2*n+1
delta = row['denominator']
coefficients = row['integer_coefficients_ascending']
values = [horner(coefficients, z) for z in eigenvalues]
assert values == [(delta if j in (0, 2*n) else 0, 0) for j in range(2*n+1)]
weighted = sum(abs(c)*7**(n*j) for j,c in enumerate(coefficients))
assert weighted == row['weighted_coefficient_sum']
graph_degree = math.factorial(n)*2**n
assert graph_degree == row['graph_degree'] == 48
assert weighted*graph_degree == row['degree_bound_each_sign_after_clearing']
assert math.gcd(delta, *coefficients) == 1
certificate = {
    'n': n,
    'method': 'Independent integer-pair powers and Horner evaluation in Z[omega]; no symbolic algebra',
    'eigenvalues_reconstructed': eigenvalues,
    'numerator_values': values,
    'delta': delta,
    'weighted_B': weighted,
    'graph_degree': graph_degree,
    'graph_seed_degree': weighted*graph_degree,
    'a_to_six': power(a, 6),
    'passed': True,
}
(root / 'projector_n3_independent_check.json').write_text(json.dumps(certificate, indent=2)+'\n')
print(json.dumps(certificate, indent=2))
