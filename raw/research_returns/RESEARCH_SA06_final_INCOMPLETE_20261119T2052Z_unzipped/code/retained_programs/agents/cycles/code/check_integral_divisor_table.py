"""Exact polynomial checks for C.3bh; the Picard and universal proofs are separate."""
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
import json
import sympy as sp

started = datetime.now(timezone.utc).isoformat()
tic = perf_counter()
x, y, z = sp.symbols("x y z")
odd = y*y*z-x**3+x*z*z
two = y*y*z+y*z*z+x**3
checks = []

def check(name, value, explanation):
    if not bool(value):
        raise AssertionError(name)
    checks.append({"name": name, "passed": True, "explanation": explanation})

check("odd_transverse_section", sp.expand(odd.subs(y, 0)+x*(x-z)*(x+z)) == 0,
      "Three distinct lines over every field of characteristic different from two.")
check("char2_transverse_section", sp.expand(two.subs(x, 0)-y*z*(y+z)) == 0,
      "Three distinct lines in characteristic two.")
check("odd_x_zero_hyperplane", odd.subs(x, 0) == y*y*z,
      "The hyperplane x=0 cuts 2P+O; subtracting z=0 gives div(x/z)=2P-2O.")
check("odd_infinity_hyperplane", odd.subs(z, 0) == -x**3,
      "The line at infinity cuts 3O.")
check("char2_y_zero_hyperplane", two.subs(y, 0) == x**3,
      "The hyperplane y=0 cuts 3P.")
check("char2_infinity_hyperplane", two.subs(z, 0) == x**3,
      "Subtracting the infinity hyperplane gives div(y/z)=3P-3O.")
check("distinct_named_points", (0, 0, 1) != (0, 1, 0),
      "The Abel isomorphism in the written proof makes P-O nonzero.")

report = {"statement": "C.3bh", "started_at_utc": started,
          "runtime_seconds": perf_counter()-tic,
          "scope": "Seven exact homogeneous-polynomial/coordinate identities only. No finite sample is used for the all-prime Picard or all-dimension theorem.",
          "checks": checks, "passed": len(checks), "failed": 0}
encoded = json.dumps(report, indent=2)
out = Path(__file__).resolve().parents[1]/"output"/"check_integral_divisor_table.json"
out.write_text(encoded+"\n")
print(encoded)
