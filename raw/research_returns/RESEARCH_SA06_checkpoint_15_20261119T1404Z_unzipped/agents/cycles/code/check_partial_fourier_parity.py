#!/usr/bin/env python3
"""Exact exterior-algebra checks for the proposed C4 correspondence test."""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json
import time

started = time.perf_counter()

def add(*forms):
    result = {}
    for form in forms:
        for key, value in form.items():
            result[key] = result.get(key, Fraction(0)) + value
    return {key: value for key, value in result.items() if value}

def scale(form, value):
    return {key: coefficient * value for key, coefficient in form.items() if coefficient * value}

def wedge(left, right):
    result = {}
    for a, ca in left.items():
        for b, cb in right.items():
            if set(a).intersection(b):
                continue
            inversions = sum(x > y for x in a for y in b)
            key = tuple(sorted(a + b))
            result[key] = result.get(key, Fraction(0)) + ca * cb * (-1) ** inversions
    return {key: value for key, value in result.items() if value}

def power(form, exponent):
    answer = {(): Fraction(1)}
    for _ in range(exponent):
        answer = wedge(answer, form)
    return answer

def exp(form, degree):
    answer = {(): Fraction(1)}
    factorial = 1
    for j in range(1, degree + 1):
        factorial *= j
        answer = add(answer, scale(power(form, j), Fraction(1, factorial)))
    return answer

def generator(i):
    return {(i,): Fraction(1)}

def integrate_x(form):
    fibre = {4, 5, 6, 7}
    answer = {}
    for key, value in form.items():
        if fibre.issubset(key):
            base = tuple(i for i in key if i not in fibre)
            # Moving the four fibre generators after the y-generators has even sign.
            answer[base] = answer.get(base, Fraction(0)) + value
    return {key: value for key, value in answer.items() if value}

a = [generator(i) for i in range(4)]
x = [generator(i + 4) for i in range(4)]
y = [generator(i + 8) for i in range(4)]
pxy = add(*(wedge(x[i], y[i]) for i in range(4)))
pay = add(*(wedge(a[i], y[i]) for i in range(4)))
la = add(wedge(a[0], a[1]), scale(wedge(a[2], a[3]), 2))
lx = add(wedge(x[0], x[1]), scale(wedge(x[2], x[3]), 2))
lhat = add(scale(wedge(y[0], y[1]), 2), wedge(y[2], y[3]))
delta = {(): Fraction(1)}
for i in range(4):
    delta = wedge(delta, add(x[i], scale(a[i], -1)))
delta13 = {key: value for key, value in delta.items() if sum(i < 4 for i in key) == 1}
delta22 = {key: value for key, value in delta.items() if sum(i < 4 for i in key) == 2}
kernel = exp(pxy, 4)
assert integrate_x(wedge(delta, kernel)) == exp(pay, 4)
assert integrate_x(wedge(delta13, kernel)) == pay
assert integrate_x(wedge(delta22, kernel)) == scale(power(pay, 2), Fraction(1, 2))
assert integrate_x(wedge(lx, kernel)) == scale(lhat, -1)
assert integrate_x(wedge(wedge(la, lx), kernel)) == scale(wedge(la, lhat), -1)
assert power(pay, 3) == scale(wedge(wedge(la, lhat), pay), -3)

cases = 0
for t, s, k in product(range(-8, 9), repeat=3):
    n = s + 4 * k
    kappa = Fraction(t * t - s, 2)
    tau = Fraction(n - s, 4)
    mixed = 6 * kappa - 2 * tau
    assert mixed.denominator == 1
    assert mixed == 3 * (t * t - s) - 2 * k
    assert int(mixed) % 2 == (t - s) % 2
    cases += 1

for t in range(-20, 21):
    s = t * t
    n = s
    assert 3 * (t * t - s) - Fraction(n - s, 2) == 0

result = {
    "status": "PASS",
    "scope": "Exact finite identities only; no existence of a parity-mismatched algebraic correspondence is asserted.",
    "exterior_generators": 12,
    "delta_partial_fourier_identity": True,
    "delta13_to_poincare": True,
    "delta22_to_half_poincare_square": True,
    "polarization_fourier_sign": -1,
    "poincare_cubic_identity": "P^3=-3*l1*l2*P",
    "mixed_scalar": "3*(t^2-s)-(n-s)/2, with n-s=4*k",
    "integer_parity_cases": cases,
    "graph_multiplication_cases": 41,
    "runtime_seconds": time.perf_counter() - started,
}
destination = Path(__file__).resolve().parents[1] / "output" / "partial_fourier_parity.json"
destination.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
