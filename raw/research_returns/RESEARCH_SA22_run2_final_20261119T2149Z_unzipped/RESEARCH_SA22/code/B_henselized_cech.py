"""Finite polynomial checks for the henselized-Cech idempotent obstruction.

These exact identities do not replace the field-valuation and henselization
arguments in notes/B_henselized_affine_descent.md.
"""
from pathlib import Path
import json
import time
from datetime import datetime, timezone
import sympy as s

started = time.perf_counter()
u, v, a, x, t = s.symbols("u v a x t")
f = u**2-u-a
g = v**2-v-a
delta = u-v
d = 2*u-1
checks = {
    "idempotent_numerator_exact_relation": s.expand(delta**2-d*delta-(g-f)) == 0,
    "discriminant_identity_mod_quadratic": s.expand((2*u-1)**2-(1+4*a)-4*f) == 0,
    "closed_fibre_numerator_zero": delta.subs({u:0,v:0}) == 0,
    "closed_fibre_denominator_unit": d.subs(u,0) == -1,
    "conjugate_numerator_equals_denominator": s.expand(delta.subs(v,1-u)-d) == 0,
    "diagonal_numerator_zero": delta.subs(v,u) == 0,
    "odd_valuation_prime_is_distinct_from_x": s.rem(x,x+4*t,x) == -4*t,
}
payload = {
    "timestamp_utc": datetime.now(timezone.utc).isoformat(),
    "elapsed_seconds": time.perf_counter()-started,
    "method": "Exact SymPy polynomial expansion and substitution over Q",
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "limitations": "Does not certify the independent valuation, henselization, v-descent, or cohomological arguments.",
}
out = Path(__file__).resolve().parents[1]/"logs"/"B_henselized_cech.json"
out.write_text(json.dumps(payload,indent=2)+"\n")
print(json.dumps(payload,indent=2))
assert all(checks.values())
