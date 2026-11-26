#!/usr/bin/env python3
"""Check the internal A1 first jets by evaluation in dual-number algebras.

Run: python workbench/programs/check_internal_cartier_jets.py
Expected: PASS, 128 units, 1536 assertions.
This finite computation checks the displayed local identities, not the
global Euler splitting or the theorem for arbitrary formal power series.
"""
import itertools
import json

# A polynomial over F2 is its set of exponent triples (x,y,epsilon).
# epsilon^2=0 is imposed by multiplication, so no differentiation routine
# or symbolic algebra package is used.
ONE = frozenset({(0, 0, 0)})
ZERO = frozenset()
X = frozenset({(1, 0, 0)})
Y = frozenset({(0, 1, 0)})
EPS = frozenset({(0, 0, 1)})


def add(*polys):
    result = set()
    for poly in polys:
        result.symmetric_difference_update(poly)
    return frozenset(result)


def mul(a, b):
    result = set()
    for i in a:
        for j in b:
            mon = tuple(v + w for v, w in zip(i, j))
            if mon[2] < 2:
                if mon in result:
                    result.remove(mon)
                else:
                    result.add(mon)
    return frozenset(result)


def power(a, n):
    result = ONE
    for _ in range(n):
        result = mul(result, a)
    return result


def evaluate(coefficients, a, b, c):
    # Basis modulo AC=B^2 through maximal-ideal degree two.
    basis = [ONE, a, b, c, power(a, 2), mul(a, b),
             mul(a, c), mul(b, c), power(c, 2)]
    return add(*(term for bit, term in zip(coefficients, basis) if bit))


def eps_part(poly):
    return frozenset((i, j, 0) for i, j, e in poly if e == 1)


def x_coefficient(poly, degree):
    return frozenset((0, j, 0) for i, j, e in poly if i == degree and e == 0)


def homogeneous_part(poly, degree):
    return frozenset(m for m in poly if m[0] + m[1] == degree and m[2] == 0)


assertions = 0
def check(condition):
    global assertions
    assert condition
    assertions += 1


units = 0
for bits in itertools.product((0, 1), repeat=7):
    lam, nu, aa, ab, ac, bc, cc = bits
    coefficients = [1, lam, 1, nu, aa, ab, ac, bc, cc]
    # Resolution chart A=x, B=xy, C=xy^2.
    u = evaluate(coefficients, X, mul(X, Y), mul(X, power(Y, 2)))
    xp, yp = add(X, EPS), add(Y, EPS)
    da = eps_part(evaluate(coefficients, xp, mul(xp, Y),
                           mul(xp, power(Y, 2))))
    dz = eps_part(evaluate(coefficients, X, mul(X, yp),
                           mul(X, power(yp, 2))))
    p2 = add(ONE if lam else ZERO, Y, power(Y, 2) if nu else ZERO)
    check(x_coefficient(u, 0) == ONE)
    check(x_coefficient(da, 0) == p2)
    check(p2 != ZERO)
    check(x_coefficient(dz, 0) == ZERO)
    check(x_coefficient(dz, 1) == ONE)
    check(add(mul(da, dz), mul(dz, da)) == ZERO)
    check(x_coefficient(mul(X, da), 1) == p2)
    # Pullback A=x^2, B=xy, C=y^2, evaluated in the same dual ring.
    du = eps_part(evaluate(coefficients, power(xp, 2), mul(xp, Y),
                           power(Y, 2)))
    dw = eps_part(evaluate(coefficients, power(X, 2), mul(X, yp),
                           power(yp, 2)))
    check(homogeneous_part(du, 0) == ZERO)
    check(homogeneous_part(dw, 0) == ZERO)
    check(homogeneous_part(du, 1) == Y)
    check(homogeneous_part(dw, 1) == X)
    check(add(mul(X, du), mul(Y, dw)) == ZERO)
    units += 1

assert units == 128 and assertions == 1536
print(json.dumps({
    "status": "PASS",
    "units": units,
    "assertions": assertions,
    "method": "exhaustive F2 dual-number substitutions; no differentiation routine",
    "scope": "all normalized units through maximal-ideal degree two with nonzero B coefficient",
    "not_proved_by_program": "arbitrary formal-series identities or global Cartier non-descent",
}, indent=2))
