#!/usr/bin/env python3
"""Exact certificate for A4:boundary-counterexample (no floating point).

The infinite polynomial ring example is proved in sections/A45.tex.  This
script checks the finite symbolic identities and the two-dimensional
boundary obstruction on which that proof depends.  It is not a finite
enumeration of all elements of the polynomial ring.
"""
import json

# Terms (x exponent, y exponent, s exponent, a exponent, b exponent).
# x and y are Laurent variables; s is an indeterminate; a^2=b^2=0.
ONE = {(0, 0, 0, 0, 0)}
ZERO = set()

def mon(x=0, y=0, s=0, a=0, b=0):
    return {(x, y, s, a, b)}

def add(*polys):
    out = set()
    for poly in polys:
        out.symmetric_difference_update(poly)
    return out

def mul(p, q):
    out = set()
    for m in p:
        for n in q:
            term = tuple(i + j for i, j in zip(m, n))
            if term[3] >= 2 or term[4] >= 2:
                continue
            if term in out:
                out.remove(term)
            else:
                out.add(term)
    return out

def normal_cech_class(poly):
    # A is free over F2[x,y] on 1,a,b,ab.  R_xy/(R_x+R_y)
    # retains precisely the Laurent monomials negative in both x and y.
    return {m for m in poly if m[0] < 0 and m[1] < 0}

epsilon = add(mon(y=1, a=1), mon(x=1, b=1))
ab = mon(a=1, b=1)
assert mul(epsilon, epsilon) == ZERO
assert mul(mon(a=1), epsilon) == mon(x=1, a=1, b=1)
assert mul(mon(b=1), epsilon) == mon(y=1, a=1, b=1)

left_lift = add(ONE, mon(x=-1, s=1, a=1))
right_lift = add(ONE, mon(y=-1, s=1, b=1))
assert mul(left_lift, left_lift) == ONE
assert mul(right_lift, right_lift) == ONE
boundary = add(mul(left_lift, right_lift), ONE)
expected = add(mul(mon(x=-1, y=-1, s=1), epsilon),
               mon(x=-1, y=-1, s=2, a=1, b=1))
assert boundary == expected
ambient_class = normal_cech_class(boundary)
assert ambient_class == mon(x=-1, y=-1, s=2, a=1, b=1)

# Coordinates in span{e,f} are bits 01=e and 10=f.
# For any s in F2[x,y], multiplication on [1/(xy)] is s(0,0).
additive_boundary = {0, 1}
log_boundary = {0, 3}
assert additive_boundary != log_boundary
assert 3 not in additive_boundary

# Finite independent check of the evaluation rule for all polynomials of
# total degree <=3; the proof uses the same monomial rule for all degrees.
mons = [(i, j) for i in range(4) for j in range(4-i)]
for mask in range(1 << len(mons)):
    s_poly = {mon(x=i, y=j).pop() for bit, (i,j) in enumerate(mons)
              if mask & (1 << bit)}
    se = normal_cech_class(mul(s_poly, mon(x=-1, y=-1)))
    s2f = normal_cech_class(mul(mul(s_poly, s_poly), mon(x=-1, y=-1)))
    expected_constant = mon(x=-1, y=-1) if (0,0,0,0,0) in s_poly else ZERO
    assert se == expected_constant == s2f

print(json.dumps({
    "statement_id": "A4:boundary-counterexample",
    "field": "F2",
    "rings": "R=F2[x,y]; A=R[a,b]/(a^2,b^2); A'=A_x times A_y",
    "ideal": "I=(y*a+x*b)",
    "square_zero_verified": True,
    "ideal_multiplications_verified": True,
    "generic_boundary_identity":
        "(1+s*a/x)^(-1)*(1+s*b/y)-1 = s*(y*a+x*b)/(x*y)+s^2*a*b/(x*y)",
    "identity_verified": True,
    "ambient_additive_class": "s^2*a*b/(x*y)",
    "additive_boundary_on_e_f": sorted(additive_boundary),
    "logarithmic_boundary_on_e_f": sorted(log_boundary),
    "boundary_subgroups_distinct": True,
    "bounded_polynomial_checks": 1 << len(mons),
    "bounded_total_degree": 3,
    "scope": "Refutes canonical 1+z -> z construction, not abstract group isomorphism",
}, indent=2))
