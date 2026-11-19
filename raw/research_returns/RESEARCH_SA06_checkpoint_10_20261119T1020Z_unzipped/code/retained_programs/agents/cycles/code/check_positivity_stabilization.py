"""Exact finite sign, degree and SL2-string checks for C.1o--p.

The universal geometric statements are proved in the LaTeX fragment.
This program does not compute any Chow or Griffiths group.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
root = Path(__file__).resolve().parents[1]
x, t, b = sp.symbols("x t b", nonzero=True)
identities = []
for d in range(25):
    gamma = sum((-x / b) ** j * t ** (d-j) for j in range(d+1))
    product = sp.Poly(sp.expand((x+b*t)*gamma), t)
    reduced = sum(coefficient*t**monomial[0]
                  for monomial, coefficient in product.terms()
                  if monomial[0] <= d)
    expected = (-1)**d * b**(-d) * x**(d+1)
    assert sp.simplify(reduced-expected) == 0
    assert sp.Poly(gamma, t).coeff_monomial(t**d) == 1
    identities.append(d)

dimension_cases = 0
for n in range(25):
    for i in range(n//2+1):
        d = n-2*i
        middle = n-i
        assert n+d == 2*middle
        assert i+d == middle
        assert i+d+1 == n-i+1
        dimension_cases += 1

string_cases = 0
first_tests = {4: set(), 5: set()}
for g in range(1, 17):
    for s in range(-g, g+1):
        for a in range(g+1):
            length = g+s-2*a
            if length < 0 or a+length > g:
                continue
            string_cases += 1
            if s <= 0:
                assert 2*a <= g
                assert g-2*a+1 > length
            for r in range(a, a+length+1):
                if 2*r > g:
                    continue
                killed = r-a+g-2*r+1 > length
                assert killed == (a > r+s-1)
                if s >= 1:
                    assert not killed
            if g in first_tests and s <= 0 and a >= 2 and a+length < g:
                first_tests[g].add((a, s, length))

assert first_tests[4] == {(2, 0, 0)}
assert first_tests[5] == {(2, -1, 0), (2, 0, 1)}
record = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "polynomial_identity_d": identities,
    "dimension_cases": dimension_cases,
    "sl2_string_cases": string_cases,
    "first_tests": {str(g): sorted(v) for g, v in first_tests.items()},
    "runtime_seconds": time.perf_counter()-started,
    "status": "PASS",
    "limitation": "Finite exact sign/index checks only; no Chow or Griffiths group is computed and no universal vanishing is inferred."
}
(root/"output/check_positivity_stabilization.json").write_text(
    json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
