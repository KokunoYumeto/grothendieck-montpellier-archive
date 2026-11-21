"""Independent integer-pair verification of the explicit Weil projector coefficients.
No symbolic polynomial package is used. Input: projectors.json.
"""
from pathlib import Path
import json
import math

root = Path(__file__).parent
rows = json.loads((root / 'projectors.json').read_text())

def mul(a, b):
    x, y = a
    z, w = b
    return x*z-y*w, x*w+y*z-y*w

def add(a, b):
    return a[0]+b[0], a[1]+b[1]

def evaluate(c, x):
    r = (0, 0)
    for k in reversed(c):
        r = add(mul(r, x), (k, 0))
    return r

certificate = []
for row in rows:
    n = row['n']
    delta = row['denominator']
    coefficients = row['integer_coefficients_ascending']
    values = []
    for j, eigenvalue in enumerate(row['eigenvalues_a_plus_b_omega']):
        value = evaluate(coefficients, tuple(eigenvalue))
        expected = (delta if j in (0, 2*n) else 0, 0)
        assert value == expected
        values.append(list(value))
    bound = sum(abs(c)*7**(n*j) for j, c in enumerate(coefficients))
    assert bound == row['weighted_coefficient_sum']
    degree = bound * math.factorial(n) * 2**n
    assert degree == row['degree_bound_each_sign_after_clearing']
    certificate.append({
        'n': n,
        'method': 'Integer-pair Horner evaluation in Z[omega], independently coded without symbolic polynomial routines',
        'numerator_evaluations': values,
        'weighted_B': bound,
        'D': degree,
        'passed': True,
    })
(root / 'projector_independent_check.json').write_text(json.dumps(certificate, indent=2)+'\n')
print(json.dumps(certificate, indent=2))
