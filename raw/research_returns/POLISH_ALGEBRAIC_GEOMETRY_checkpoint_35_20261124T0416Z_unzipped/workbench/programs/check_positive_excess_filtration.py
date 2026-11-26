#!/usr/bin/env python3
"""Check the independent finite-cover genus arithmetic by finite differences.

The reconstruction sums the curve Riemann--Roch terms directly. This program
instead proves the proposed sum by its polynomial initial value and first
finite difference, using exact multivariate rational coefficients. It does
not certify the geometric filtration or any theorem about surfaces.

Run: python3 workbench/programs/check_positive_excess_filtration.py
Expected: two symbolic identities and 240 explicit sums pass.
"""
from fractions import Fraction
from math import comb
import json

# Exponents are in the order p,n,d,g. All coefficients are rational.
ZERO = (0, 0, 0, 0)

def clean(a):
    return {e: Fraction(c) for e, c in a.items() if c}

def add(a, b, scale=1):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, Fraction(0)) + scale*c
    return clean(out)

def mul(a, b):
    out = {}
    for x, cx in a.items():
        for y, cy in b.items():
            e = tuple(u+v for u, v in zip(x, y))
            out[e] = out.get(e, Fraction(0)) + cx*cy
    return clean(out)

def shift_p(a):
    out = {}
    for e, c in a.items():
        for j in range(e[0]+1):
            f = (j, *e[1:])
            out[f] = out.get(f, Fraction(0)) + c*comb(e[0], j)
    return clean(out)

def specialize_p(a, value):
    out = {}
    for e, c in a.items():
        f = (0, *e[1:])
        out[f] = out.get(f, Fraction(0)) + c*value**e[0]
    return clean(out)

one = {ZERO: Fraction(1)}
p = {(1, 0, 0, 0): Fraction(1)}
n = {(0, 1, 0, 0): Fraction(1)}
d = {(0, 0, 1, 0): Fraction(1)}
g = {(0, 0, 0, 1): Fraction(1)}
nd = mul(n, d)
G = add(g, one, -1)
G = add(G, G)
delta = add(G, mul(p, nd), -1)
F = {e: c/2 for e, c in mul(add(p, one, -1), delta).items()}

# F(p)=p_a(B_T)-g. Adding the next graded term changes F by g-1-pnd.
initial = specialize_p(F, 1)
increment = add(add(g, one, -1), mul(p, nd), -1)
difference = add(add(shift_p(F), F, -1), increment, -1)
assert initial == {}
assert difference == {}

count = 0
for pp in (2, 3, 5, 7, 11):
    for nn in (1, 2, 3, 5):
        for dd in (1, 2, 4):
            for gg in (0, 1, 3, 10):
                chi = sum(1-gg+j*nn*dd for j in range(pp))
                defect = 1-chi-gg
                predicted = Fraction(pp-1, 2)*(2*gg-2-pp*nn*dd)
                assert defect == predicted
                count += 1
assert count == 240
print(json.dumps({
    'result': 'PASS',
    'method': 'Exact polynomial initial value and first finite difference',
    'symbolic_identities': 2,
    'explicit_sums': count,
    'identity': 'p_a(B_T)-g=(p-1)*(2g-2-p*n*d)/2',
    'scope': 'Arithmetic only; no geometric filtration or surface theorem certified'
}, sort_keys=True, indent=2))
