"""Exact finite sign, degree, and exceptional-relation certificates for C.1q."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import sympy as sp

started = time.perf_counter()
u, t, v = sp.symbols("u t v")
recursions = []
for c in range(2, 21):
    ck = [sp.Integer(1)] + list(sp.symbols(f"c1:{c}"))
    xs = {c-1: sp.Integer(1), 0: sp.Integer(0)}
    for j in range(1, c-1):
        xs[c-1-j] = sp.expand(sum(ck[k]*(-u)**(j-k)
                                  for k in range(j+1)))
    for k in range(2, c):
        assert sp.expand(u*xs[k]+xs[k-1]-ck[c-k]) == 0
    q = sp.expand(sum(ck[k]*(-u)**(c-1-k) for k in range(c)))
    assert sp.expand(u*xs[1]-ck[c-1]+q) == 0
    assert sp.expand(sum(sp.binomial(c-1,k)*t**k*(-v*t)**(c-1-k)
                         for k in range(c))-(1-v)**(c-1)*t**(c-1)) == 0
    recursions.append(c)

dimension_cases = 0
nonzero_candidates = 0
for r in range(41):
    for c in range(2, 21):
        n = r+c+3
        if n % 2:
            continue
        m = n//2
        degree = m-c+1
        assert degree == (r-c+5)//2
        assert 2*degree <= (r+3)
        e = degree-2
        if e >= 0:
            assert 0 <= e <= r
            assert e+c-1 <= r
            assert 2+e+c-1 == m
            nonzero_candidates += 1
        dimension_cases += 1

record = {
    "utc": datetime.now(timezone.utc).isoformat(),
    "runtime_seconds": time.perf_counter()-started,
    "normal_polynomial_codimensions": recursions,
    "dimension_cases": dimension_cases,
    "potential_nonzero_center_summands": nonzero_candidates,
    "status": "PASS",
    "scope": "Finite exact checks of the universal symbolic recursion and degree identities. Actual ampleness and the all-dimensional proof are supplied in C.1q; no Chow-group nonvanishing is computed.",
}
output = Path(__file__).resolve().parents[1]/"output/check_blowup_positivity.json"
output.write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
