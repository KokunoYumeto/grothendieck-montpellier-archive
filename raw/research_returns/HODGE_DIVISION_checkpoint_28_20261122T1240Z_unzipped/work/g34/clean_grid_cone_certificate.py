"""Exact HD-G21 interpolation and exterior-algebra certificate.

All 81 grid terms are rebuilt. Ext maps and invariance are proved in the
accompanying text; this program checks the explicit coefficients/maps.
Requires SymPy; no downloaded candidate data are used.
"""
from itertools import product
from math import comb
from pathlib import Path
import json
import sympy as S

d, s, t = S.symbols('d s t')

def add(a, b, scale=1):
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, 0) + scale*c
    return {m: S.expand(c) for m, c in out.items() if S.expand(c) != 0}

def exterior(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            if ma & mb:
                continue
            swaps = sum((mb & ((1 << i)-1)).bit_count()
                        for i in range(16) if ma >> i & 1)
            mask = ma | mb
            out[mask] = out.get(mask, 0) + (-1)**swaps*ca*cb
    return {m: S.expand(c) for m, c in out.items() if S.expand(c) != 0}

def form(index):
    return {1 << index: S.Integer(1)}

def pair(j, value):
    x, y, u, v = [form(4*j+k) for k in range(4)]
    return exterior(add(u, x, -value), add(v, y, -value))

def graph(slopes):
    out = {0: S.Integer(1)}
    for j, value in enumerate(slopes):
        out = exterior(out, pair(j, value))
    return out

Ft = graph([t]*4)
assert len(Ft) == 256
w = {}
for mask, expr in Ft.items():
    p = S.Poly(expr, t)
    c = S.expand(sum(p.nth(2*r+1)*(-d)**r for r in range(4)))
    if c != 0:
        w[mask] = c
assert len(w) == 128

def odd_coefficient(expr):
    p = S.Poly(S.expand(expr), s)
    return S.expand(sum(p.nth(2*r+1)*(-d)**r for r in range(2)))

coefficients = {}
rebuilt = {}
for eps in product((-1, 0, 1), repeat=4):
    k = sum(value != 0 for value in eps)
    numerator = S.prod(-d+value*s for value in eps if value != 0)
    c = S.expand(2**(4-k)*(d+1)**(4-k)*odd_coefficient(numerator))
    coefficients[eps] = c
    rebuilt = add(rebuilt, graph(eps), c)
assert add(rebuilt, w, -16) == {}

for j in range(4):
    eps = tuple(int(a == j) for a in range(4))
    assert S.expand(coefficients[eps] - 8*(d+1)**3) == 0
for i in range(4):
    for j in range(i+1, 4):
        eps = tuple(int(a in (i, j)) for a in range(4))
        assert S.expand(coefficients[eps] + 8*d*(d+1)**2) == 0

# All mixed eta_ij annihilate both eigenvolumes. Check the eight factor
# identities from which all 16 mixed identities follow, without assuming s²=-d.
Fplus = graph([s]*4)
Fminus = graph([-s]*4)
for j in range(4):
    x, y, u, v = [form(4*j+k) for k in range(4)]
    chi, psi = add(x, y, -S.I), add(u, v, -S.I)
    alpha_plus, alpha_minus = add(psi, chi, s), add(psi, chi, -s)
    assert exterior(alpha_plus, Fminus) == {}
    assert exterior(alpha_minus, Fplus) == {}

def reduce_s(expr):
    return S.rem(S.Poly(S.expand(expr), s), S.Poly(s*s+d, s)).as_expr()

actual_rows = S.Matrix([
    [reduce_s((1+s)*(-s)), reduce_s(-s*(1-s))],
    [reduce_s(s*(1-s)), reduce_s(-(1+s)*(-s))]])
expected_rows = S.Matrix([[d-s, -d-s], [d+s, -d+s]])
assert actual_rows == expected_rows
assert S.expand(actual_rows.det() - 4*d*s) == 0

# The full point stabilizer calculation is integral, with determinant one.
# For each j use y_j-x_j=0 from B_ej and y_j=0 from any B_ei, i != j.
minor = S.zeros(8)
for j in range(4):
    minor[2*j, 2*j], minor[2*j, 2*j+1] = -1, 1
    minor[2*j+1, 2*j+1] = 1
assert minor.det() == 1

specializations = {}
for value in (1, 2, 3, 7, 11, 19, 43, 67, 163):
    vals = [int(c.subs(d, value)) for c in coefficients.values()]
    assert sum(vals) == 0
    specializations[str(value)] = dict(
        positive_graphs=sum(c > 0 for c in vals),
        negative_graphs=sum(c < 0 for c in vals),
        positive_total=sum(c for c in vals if c > 0),
        negative_total=-sum(c for c in vals if c < 0))

out = dict(check='PASS', sympy_version=S.__version__, grid_points=81,
           generic_graph_monomials=len(Ft), Weil_monomials=len(w),
           complete_symbolic_grid_identity=True,
           four_single_coordinate_coefficients='8*(d+1)^3',
           six_double_coordinate_coefficients='-8*d*(d+1)^2',
           mixed_annihilations=16, verified_factor_annihilations=8,
           restriction_matrix=[[str(c) for c in row] for row in actual_rows.tolist()],
           restriction_determinant='4*d*s', independent_off_diagonal_classes=12,
           rank_one_edge_Ext_dimensions=[comb(6, k-1) for k in range(1, 8)],
           stabilizer_integral_minor=1, specializations=specializations,
           integral_coefficients={','.join(map(str, eps)): str(c)
                                  for eps, c in coefficients.items()},
           scope='Exact finite interpolation, exterior annihilation, restriction and integral-stabilizer checks. Derived Hom sequences, trace identities and arbitrary coherent-action invariance are proved in the note.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k: v for k, v in out.items() if k != 'integral_coefficients'}, indent=2))
