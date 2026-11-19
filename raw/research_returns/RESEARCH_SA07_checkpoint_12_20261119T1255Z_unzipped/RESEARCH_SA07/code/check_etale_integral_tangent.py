#!/usr/bin/env python3
"""Exact finite certificates accompanying elliptic work note section 47.

Inputs: E*: y^2=4x^3-4x-1, p=5; binomial polynomials of degrees 1..25.
The all-degree derivative and formal-group statements are proved in the note.
"""
import datetime
import hashlib
import json
import pathlib
import time
import sympy as S

start = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.perf_counter()
x, T, y, t, a = S.symbols("x T y t a")
p = 5
P = 4*x**3 - 4*x - 1
P2 = S.Poly(S.expand(P**2), x)
H = int(P2.coeff_monomial(x**4)) % p
K = int(P2.coeff_monomial(x**3)) % p
assert (H, K) == (3, 2)
points = 1 + sum(1 for xx in range(p) for yy in range(p)
                 if (yy*yy - int(P.subs(x, xx))) % p == 0)
assert points == 8

def reduce_curve(f):
    f = S.rem(S.Poly(S.expand(f), y), S.Poly(y*y-P, y)).as_expr()
    return S.Poly(f, x, y, t, a, modulus=p).as_expr()

def D(f):
    return reduce_curve(y*S.diff(f, x) + (6*x*x-2)*S.diff(f, y)
                        - (x+a)*S.diff(f, t))

power_outputs = {}
for f in (x, y, t):
    value = f
    for _ in range(p):
        value = D(value)
    # V=-d/dt, hence -(K+aH)V contributes +(K+aH)d/dt.
    expected = reduce_curve(H*D(f) + (K+a*H)*S.diff(f, t))
    assert reduce_curve(value - expected) == 0
    power_outputs[str(f)] = str(value)

for r in range(1, 26):
    B = S.prod(T-j for j in range(r))/S.factorial(r)
    derivative = S.diff(B, T).subs(T, 0)
    assert derivative == S.Rational((-1)**(r-1), r)

assert (K + H*1) % p == 0
assert K % p != 0
elapsed = time.perf_counter() - tick
record = {
    "start_utc": start, "elapsed_seconds": elapsed,
    "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    "inputs": {"curve": str(P), "p": p, "binomial_degrees": [1,25]},
    "H": H, "K": K, "point_count": points, "trace": p+1-points,
    "D_to_fifth_on_coordinates": power_outputs,
    "p_closed_slope": 1,
    "binomial_derivative_formula_checks": 25,
    "status": "PASS",
}
print(json.dumps(record, indent=2))
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(record, indent=2)+'\n')
