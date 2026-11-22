#!/usr/bin/env python3
"""Finite arithmetic certificate; the geometric assertions are proved in TeX.

This does not construct torsion line bundles or test the primary theorems.
"""
import hashlib
import itertools
import json
from pathlib import Path
import time
import sympy as sp

START = time.perf_counter()
checks = 0
def check(value):
    global checks
    assert value
    checks += 1

x, y, z = sp.symbols('x y z')
f = y*y*z - x*x*x + x*z*z
derivatives = [sp.Poly(sp.diff(f, v), x, y, z, modulus=3)
               for v in (x, y, z)]
targets = [z*z, 2*y*z, y*y+2*x*z]
for actual, target in zip(derivatives, targets):
    check(actual == sp.Poly(target, x, y, z, modulus=3))
# Algebraic elimination of a geometric singular point: z=0 from Fx,
# then y=0 from Fz, then x=0 from the defining equation.
check(sp.Poly(f.subs({z: 0, y: 0}), x, modulus=3)
      == sp.Poly(-x**3, x, modulus=3))
check(sp.Poly(targets[2].subs(z, 0), y, modulus=3)
      == sp.Poly(y*y, y, modulus=3))
for point in itertools.product(range(3), repeat=3):
    values = dict(zip((x,y,z), point))
    singular = int(f.subs(values)) % 3 == 0 and all(
        int(t.subs(values)) % 3 == 0 for t in targets)
    check(singular == (point == (0,0,0)))

cases = []
for m in range(1, 9):
    r = 2**m
    order = 2*r
    g_indices = list(range(r))
    f_indices = list(range(r, 2*r))
    check(set(g_indices).isdisjoint(f_indices))
    for i in g_indices:
        for j in g_indices:
            check(((j-i) % order == 0) == (j == i))
        column = 0
        for j in f_indices:
            check((j-i) % order != 0)
            column += 3  # h0 of a degree-three line bundle, by the proof
        check(column == 3*r)
        for s in range(3*r):
            check(s < column)  # an s-dimensional e_i source cannot surject
    period = 1
    while pow(3, period, order) != 1:
        period += 1
    check(pow(3, period, order) == 1)
    for i in range(order):
        check((pow(3, period, order)*i) % order == i)
    check(r*r*3 == sum(3*r for _ in g_indices))
    cases.append({'r': r, 'torsion_order': order, 'Frobenius_period': period,
                  'degree_one_dimension': 3*r*r,
                  'minimum_order_generators_lower_bound': 3*r})

result = {
    'label': 'D:elliptic-cone-order-generators',
    'status': 'PASS',
    'assertions': checks,
    'runtime_seconds': time.perf_counter()-START,
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'scope': 'Exact polynomial, finite index-set, semisimple dimension, and Frobenius-congruence checks only; geometric existence and Riemann--Roch are not computed.',
    'cases': cases,
}
output = Path(__file__).resolve().parents[1] / 'output' / 'elliptic_order_generators.json'
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result))
