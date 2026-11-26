#!/usr/bin/env python3
"""Small curve counts and integral gamma-polynomial certificates.

Run with Python 3 and SymPy: python fixed_invariants_replay.py
The curve computations enumerate F_4-points. Gamma polynomials are calculated
from Adams' generating series and compared with the Stirling-number formula.
"""
import json
from math import factorial, gcd
from functools import reduce
import sympy as sp
from sympy.functions.combinatorial.numbers import stirling


def add(a, b):
    return a ^ b


def mul(a, b):
    v = 0
    while b:
        if b & 1:
            v ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # omega^2+omega+1
    return v


def power(a, n):
    v = 1
    while n:
        if n & 1:
            v = mul(v, a)
        a = mul(a, a)
        n >>= 1
    return v


def trace(a):
    return add(a, mul(a, a))


def curve_example(kind):
    points = []
    for x in range(4):
        a = trace(mul(3, x))
        b = trace(x)
        assert (a, b) == (x & 1, x >> 1)
        sat = a if kind == 'x1' else (a | b)
        P = 1 ^ sat
        # Degree 25 monic polynomial, evaluated as a circuit.
        f = add(mul(2, P), mul(add(power(x, 4), x), power(x, 21)))
        for y in range(4):
            if add(mul(y, y), y) == f:
                points.append([x, y])
    S = 2 if kind == 'x1' else 3
    assert len(points) == 2 * S
    return {'formula': kind, 'S': S, 'field_polynomial': 'u^2+u+1',
            'degree': 25, 'genus': 12, 'affine_points': points,
            'projective_points': len(points) + 1,
            'absolute_F_basis_rule': [2*j if 2*j <= 12 else 0 for j in range(1, 13)],
            'q_F_basis_rule': [4*j if 4*j <= 12 else 0 for j in range(1, 13)]}


def gamma_examples():
    s, t = sp.symbols('s t')
    # sum_{m>=1} (-1)^(m-1) s^m; apply s d/ds v-1 times.
    series = s/(1+s)
    rows = []
    for v in range(1, 10):
        gamma = sp.cancel(series.subs(s, t/(1-t)))
        predicted = sum((-1)**(j-1)*factorial(j-1)*int(stirling(v, j, kind=2))*t**j
                        for j in range(1, v+1))
        assert sp.cancel(gamma-predicted) == 0
        coefficients = [int(sp.expand(predicted).coeff(t, j)) for j in range(1, v+1)]
        ds = [reduce(gcd, map(abs, coefficients[i-1:])) for i in range(1, v+1)]
        assert ds[-1] == factorial(v-1)
        if v >= 3 and v % 2:
            assert ds[-1] // ds[-2] == 2
        rows.append({'v': v, 'gamma_coefficients': coefficients, 'filtration_gcds': ds})
        series = sp.cancel(s*sp.diff(series, s))
    return rows


if __name__ == '__main__':
    curves = [curve_example(kind) for kind in ['x1', 'x1_or_x2']]
    assert curves[0]['absolute_F_basis_rule'] == curves[1]['absolute_F_basis_rule']
    assert curves[0]['q_F_basis_rule'] == curves[1]['q_F_basis_rule']
    print(json.dumps({'curve_examples': curves, 'gamma_examples': gamma_examples()}, indent=2))
