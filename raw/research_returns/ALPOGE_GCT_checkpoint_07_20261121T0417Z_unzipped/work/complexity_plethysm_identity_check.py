"""Exact polynomial identities used in the independent review of PLE-F8.

This is a symbolic algebra check, not a formal proof-assistant certificate.
The algebraic independence, injectivity, and graded-surjectivity arguments
are reviewed separately in cross_positivity_checks.tsv.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp


a, b, c, d = sp.symbols("a b c d")
h = a*c - b*b
j = a*a*d - 3*a*b*c + 2*b**3
delta = a*a*d*d - 6*a*b*c*d + 4*a*c**3 + 4*b**3*d - 3*b*b*c*c
u = h*h*delta
v = a*j*delta**2
w = a*a*h*delta**3
z = w - 2*u*u


def raising(f):
    return a*sp.diff(f, b) + 2*b*sp.diff(f, c) + 3*c*sp.diff(f, d)


expressions = {
    "E(a)": raising(a),
    "E(h)": raising(h),
    "E(j)": raising(j),
    "E(delta)": raising(delta),
    "j^2+4h^3=a^2*delta": j*j + 4*h**3 - a*a*delta,
    "v^2+4uw=a^4*delta^5": v*v + 4*u*w - a**4*delta**5,
    "w^2=u(v^2+4uw)": w*w - u*(v*v + 4*u*w),
    "z^2=uv^2+4u^4": z*z - u*v*v - 4*u**4,
}
results = {name: sp.Poly(sp.expand(expr), a, b, c, d).is_zero
           for name, expr in expressions.items()}
results["specialization u=0"] = sp.expand(u.subs({a: 1, b: 0, c: 0})) == 0
results["specialization v=d^5"] = sp.expand(v.subs({a: 1, b: 0, c: 0})) == d**5

expected_degrees = {"a": (a, (1, 3)), "h": (h, (2, 2)),
                   "j": (j, (3, 3)), "delta": (delta, (4, 0)),
                   "u": (u, (8, 4)), "v": (v, (12, 6)),
                   "w": (w, (16, 8)), "z": (z, (16, 8))}
for name, (expr, expected) in expected_degrees.items():
    monomials = sp.Poly(sp.expand(expr), a, b, c, d).monoms()
    pairs = {(sum(m), 3*m[0] + m[1] - m[2] - 3*m[3]) for m in monomials}
    results[f"bidegree {name}={expected}"] = pairs == {expected}

report = {
    "statement_id": "PLE-F8-IDENTITIES",
    "date": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro",
    "effort": "inherited/undisclosed",
    "run": "/root/complexity",
    "method": "Exact expanded polynomials over Z, using SymPy",
    "sympy_version": sp.__version__,
    "checks": results,
    "outcome": "PASS" if all(results.values()) else "FAIL",
}
output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
assert all(results.values())
