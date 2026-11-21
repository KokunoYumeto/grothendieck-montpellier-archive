#!/usr/bin/env python3
"""Exact finite algebra checks for KT-POLARIZED-EXTENSION-GRAPH-OBSTRUCTION.

This is not a Galois or automorphy computation.  The proof of the
profinite-group statements is in polarized_extension_graph.tex.
"""
from fractions import Fraction
import json
from pathlib import Path


def matunit(i, j):
    return [[int((a, b) == (i, j)) for b in range(3)] for a in range(3)]


def add(a, b, s=1):
    return [[a[i][j] + s * b[i][j] for j in range(3)] for i in range(3)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def bracket(a, b):
    return add(mul(a, b), mul(b, a), -1)


def scale(a, s):
    return [[s * x for x in row] for row in a]


def theta(a):
    return [[-a[2-j][2-i] for j in range(3)] for i in range(3)]


def rank(rows):
    rows = [[Fraction(x) for x in row] for row in rows]
    r = 0
    for j in range(len(rows[0])):
        k = next((k for k in range(r, len(rows)) if rows[k][j]), None)
        if k is None:
            continue
        rows[r], rows[k] = rows[k], rows[r]
        pivot = rows[r][j]
        rows[r] = [x / pivot for x in rows[r]]
        for k in range(len(rows)):
            if k != r:
                a = rows[k][j]
                rows[k] = [x - a*y for x, y in zip(rows[k], rows[r])]
        r += 1
    return r


u12, u23, u21, u32 = (matunit(*ij) for ij in [(0, 1), (1, 2), (1, 0), (2, 1)])
x = add(u12, u23)
y = add(u21, u32, -1)
z = bracket(x, y)
assert z == [[1, 0, 0], [0, -2, 0], [0, 0, 1]]
assert theta(x) == scale(x, -1)
assert theta(y) == y
assert bracket(z, x) == scale(add(u12, u23, -1), 3)
assert bracket(z, y) == scale(add(u21, u32), -3)
simple = [u12, u23, u21, u32]
span = simple + [bracket(u12, u23), bracket(u32, u21), bracket(u12, u21), bracket(u23, u32)]
lie_rank = rank([sum(m, []) for m in span])
assert lie_rank == 8

# Concrete residual instance ell=11, e=2; 2 is primitive, q=2^2 has order 5.
ell, e, zeta = 11, 2, 2
q = pow(zeta, e, ell)
order = next(d for d in range(1, ell) if pow(q, d, ell) == 1)
assert order == 5
rows = []
for h_exponent in range(ell-1):
    for c_sign in [-1, 1]:
        value = pow(zeta, h_exponent, ell)
        dim = int(value == q and c_sign == -1) + int(value == pow(q, -1, ell) and c_sign == 1)
        rows.append(dict(h_exponent=h_exponent, c_sign=c_sign, h1_dimension=dim))
assert sum(r['h1_dimension'] for r in rows) == 2
vanishing = {
    'eta': (0, -1),
    'eta_psi_inverse': (-e, -1),
    'eta_psi_inverse_squared': (-2*e, -1),
    'psi': (e, 1),
    'psi_squared': (2*e, 1),
}
for label, (exponent, sign) in vanishing.items():
    row = next(r for r in rows if r['h_exponent'] == exponent % (ell-1) and r['c_sign'] == sign)
    assert row['h1_dimension'] == 0, label
report = {
    'scope': 'Abstract polarized profinite extension graph, not an arithmetic counterexample',
    'lie_algebra_rank': lie_rank,
    'theta_x_is_minus_x': True,
    'theta_y_is_y': True,
    'bracket_x_y': z,
    'ell': ell,
    'e': e,
    'residual_psi_order': order,
    'h1_characters': rows,
    'five_named_vanishings': list(vanishing),
    'all_checks_pass': True,
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps({'all_checks_pass': True, 'lie_algebra_rank': lie_rank, 'output': str(output)}))
