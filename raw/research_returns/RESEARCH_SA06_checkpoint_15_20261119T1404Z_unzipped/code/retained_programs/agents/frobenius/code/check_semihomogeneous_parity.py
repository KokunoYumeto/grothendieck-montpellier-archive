#!/usr/bin/env python3
"""Exact exterior-algebra identities and bounded arithmetic checks.

The bounded enumeration checks necessary conditions only; the accompanying
proof establishes the valuation conclusions for every rank and coefficient.
"""
from collections import defaultdict
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from time import perf_counter
import json
import sympy as sp

start = perf_counter()

def wedge(f, g):
    out = defaultdict(lambda: 0)
    for u, x in f.items():
        for v, y in g.items():
            if set(u).intersection(v):
                continue
            sign = (-1)**sum(i > j for i in u for j in v)
            out[tuple(sorted(u+v))] += sign*x*y
    return {u:sp.expand(x) for u,x in out.items() if sp.expand(x) != 0}

def add(*items):
    out = defaultdict(lambda: 0)
    for f in items:
        for u,x in f.items():
            out[u] += x
    return {u:sp.expand(x) for u,x in out.items() if sp.expand(x) != 0}

def scale(c, f):
    return {u:c*x for u,x in f.items()}

def power(f, n):
    out = {():1}
    for _ in range(n):
        out = wedge(out, f)
    return out

ell1 = {(0,1):1, (2,3):2}
ell2 = {(4,5):2, (6,7):1}
P = {(i,i+4):1 for i in range(4)}
a,b,c = sp.symbols('a b c')
D = add(scale(a,ell1), scale(b,P), scale(c,ell2))
top = tuple(range(8))
chi = sp.factor(power(D,4)[top]/24)
assert chi == (2*a*c-b*b)**2
assert not add(power(P,3), scale(3,wedge(wedge(ell1,ell2),P)))

basis = [power(ell1,2),wedge(ell1,P),wedge(ell1,ell2),
         power(P,2),wedge(P,ell2),power(ell2,2)]
pairing = sp.Matrix([[wedge(u,v).get(top,0) for v in basis] for u in basis])
assert pairing.det() != 0

def two_integral(q):
    return q.denominator % 2 == 1

def even_two_integral(q):
    return two_integral(q/2)

count = 0
for r in range(1,129):
    for aa in range(-8,9):
        if 2*(r-1)*aa*aa % r:
            continue
        for cc in range(-8,9):
            if 2*(r-1)*cc*cc % r:
                continue
            for bb in range(-8,9):
                delta = 2*aa*cc-bb*bb
                if delta*delta % (r**3):
                    continue
                count += 1
                coeffs = [Fraction((r-1)*bb*bb,2*r),
                          Fraction((r-1)*aa*bb,r),
                          Fraction((r-1)*bb*cc,r),
                          Fraction((r-1)*aa*cc,r)]
                assert all(two_integral(x) for x in coeffs)
                scalar = Fraction(-(r-1)*(r-2)*bb*delta,r*r)
                assert even_two_integral(scalar)

record = {
    'utc': datetime.now(timezone.utc).isoformat(),
    'seconds': perf_counter()-start,
    'chi_formula':str(chi),
    'P_cubed_equals_minus_three_ell1_ell2_P':True,
    'degree_two_basis':['ell1^2','ell1 P','ell1 ell2','P^2','P ell2','ell2^2'],
    'intersection_matrix':[[int(x) for x in row] for row in pairing.tolist()],
    'intersection_determinant':int(pairing.det()),
    'rank_range':[1,128],
    'coefficient_range':[-8,8],
    'necessary_condition_tuples_checked':count,
    'all_parity_checks_passed':True,
    'scope':'Bounded check is supplementary; no existence of bundles is inferred.'
}
root = Path(__file__).resolve().parents[1]
(root/'output'/'check_semihomogeneous_parity.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
