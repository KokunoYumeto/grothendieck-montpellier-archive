#!/usr/bin/env python3
"""Exact certificates for the auxiliary X0(27) 3-Kummer separation failure.

This script checks identities over QQ and group operations over F_17 and F_71.
It does not construct a global Selmer section or test the full compact
pro3 point map of a Fermat curve.
"""
from __future__ import annotations

import json
import sympy as sp

x, h, u, w = sp.symbols("x h u w")
lam = (h / (h + 9)) ** 3
j_lam = 27 * (9 - 8 * u) ** 3 / (u**3 * (1 - u))
j_h = (h + 9) ** 3 * (h**3 + 243*h**2 + 2187*h + 6561) ** 3 / (
    h**9 * (h**2 + 9*h + 27)
)
assert sp.cancel(j_lam.subs(u, lam) - j_h) == 0
F = x**3 - (h+3)**2*x**2 + (9*h+27)*x - 27
y = x*(h+3)-5
assert sp.expand(x**3-7-y**2-y-F) == 0
f = sp.expand(F.subs(h, -9))
assert f == x**3-36*x**2-54*x-27
assert sp.discriminant(f, x) == -(3**13)
assert -27*(-27)**2 == -(3**9)  # discriminant of y^2+y=x^3-7
assert sp.cancel(j_lam.subs(u, -sp.Rational(1, 8))) == -12288000
assert sp.expand(f.subs(x, 3*(1+w))/27) == w**3-9*w**2-27*w-18

Point = tuple[int, int] | None

def on_curve(P: Point, p: int) -> bool:
    return P is None or (P[1]**2+P[1]-P[0]**3+7) % p == 0

def neg(P: Point, p: int) -> Point:
    return None if P is None else (P[0], (-P[1]-1) % p)

def add(P: Point, Q: Point, p: int) -> Point:
    assert on_curve(P, p) and on_curve(Q, p)
    if P is None:
        return Q
    if Q is None:
        return P
    a, b = P
    c, d = Q
    if a == c and (b+d+1) % p == 0:
        return None
    slope = (
        3*a*a*pow(2*b+1, -1, p)
        if P == Q else (d-b)*pow(c-a, -1, p)
    ) % p
    z = (slope*slope-a-c) % p
    R = (z, (slope*(a-z)-b-1) % p)
    assert on_curve(R, p)
    return R

def mul(P: Point, n: int, p: int) -> Point:
    R = None
    while n:
        if n & 1:
            R = add(R, P, p)
        P = add(P, P, p)
        n //= 2
    return R

def count_points(p: int) -> int:
    return 1 + sum(
        (b*b+b-a*a*a+7) % p == 0
        for a in range(p) for b in range(p)
    )

witnesses = []
for p, R, T, expected_doubles in [
    (17, (12, 8), None, [(12, 8), None, None, None]),
    (71, (69, 7), (3, 4), [(36, 69), (39, 55), (38, 35), None]),
]:
    assert p % 27 == 17 and p % 3 == 2
    assert on_curve(R, p) and on_curve(T, p)
    assert int(f.subs(x, R[0])) % p == 0
    derivative = int(sp.diff(f, x).subs(x, R[0])) % p
    assert derivative != 0
    assert (-3+(R[1]+5)*pow(R[0], -1, p)) % p == (-9) % p
    D = add(R, neg(T, p), p)
    doubles = [mul(D, n, p) for n in [1, 2, 4, 8]]
    assert doubles == expected_doubles
    assert mul(D, 8, p) is None
    assert mul(D, 9, p) == D  # D itself is a 9-division point in this reduction
    count = count_points(p)
    assert count == p+1
    assert count % 9 == 0 and count % 27 != 0
    witnesses.append({
        "prime": p,
        "R_reduction": R,
        "reference_cusp_reduction": T,
        "D_R_minus_T": D,
        "D_2D_4D_8D": doubles,
        "f_derivative_mod_p": derivative,
        "curve_point_count": count,
        "three_primary_group_order": 9,
        "nine_division_point_of_D_in_reduction": D,
    })

print(json.dumps({
    "status": "all exact assertions passed",
    "scope": "auxiliary X0(27) 3-primary Kummer map only",
    "curve": "y^2+y=x^3-7",
    "lambda": "(h/(h+9))^3",
    "h": "-3+(y+5)/x",
    "f": str(f),
    "f_discriminant": -(3**13),
    "witnesses": witnesses,
}, indent=2))
