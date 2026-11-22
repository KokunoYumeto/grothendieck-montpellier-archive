"""Finite identities only for the Artin--Schreier branch countermodel.

This does not certify henselian algebraization, coherent extension, or the
all-prime irreducibility proof.  Those are the separately written arguments.
"""
from datetime import datetime, timezone
from pathlib import Path
import json
import time
import sympy as sp

start = time.perf_counter()
started = datetime.now(timezone.utc).isoformat()
q, y, x, z, t = sp.symbols("q y x z t")
checks = []
cases = []
cutoff = 20

def check(label, condition):
    condition = bool(condition)
    checks.append({"check": label, "passed": condition})
    if not condition:
        raise AssertionError(label)

def modp(expr, generators, p):
    return sp.Poly(sp.expand(expr), *generators, modulus=p)

for p in (2, 3, 5):
    exponents = []
    exponent = 1
    while exponent <= cutoff:
        exponents.append(exponent)
        exponent *= p
    u = -sum(q**e for e in exponents)
    residue = modp(u**p-u-q, (q,), p)
    check(f"p={p}: exact truncated-root error", residue == modp(-q**exponent, (q,), p))
    check(f"p={p}: all error degrees exceed cutoff", all(monomial[0] > cutoff for monomial, coeff in residue.terms()))
    check(f"p={p}: simple derivative", modp(sp.diff(y**p-y-q, y), (y, q), p) == modp(-1, (y, q), p))
    for a in range(p):
        check(f"p={p}: translation a={a}", modp((u+a)**p-(u+a)-q, (q,), p) == residue)
    product = sp.prod(y-u-a for a in range(p))
    check(f"p={p}: product of branches", modp(product-((y-u)**p-(y-u)), (y, q), p).is_zero)
    check(f"p={p}: other branch detects strict ideal", modp((u+1)-u, (q,), p) == modp(1, (q,), p))
    reciprocal = sp.Poly(t*z**p+x*z**(p-1)-x, z)
    coeffs = reciprocal.all_coeffs()
    check(f"p={p}: reciprocal leading x-valuation zero", sp.Poly(coeffs[0], x).degree() == 0 and coeffs[0] == t)
    check(f"p={p}: reciprocal lower coefficients divisible by x", all(sp.expand(c).subs(x, 0) == 0 for c in coeffs[1:]))
    check(f"p={p}: reciprocal constant x-valuation one", coeffs[-1] == -x)
    cases.append({"p": p, "cutoff": cutoff, "root_exponents": exponents,
                  "first_error_degree": exponent, "truncated_root": str(u),
                  "exact_error_mod_p": str(residue.as_expr()),
                  "reciprocal_polynomial": str(reciprocal.as_expr())})

result = {
    "started_utc": started,
    "completed_utc": datetime.now(timezone.utc).isoformat(),
    "runtime_seconds": time.perf_counter()-start,
    "scope": "Finite p=2,3,5 polynomial identities and coefficient valuations only; not the henselian/coherent-extension theorem.",
    "passed": sum(c["passed"] for c in checks), "failed": sum(not c["passed"] for c in checks),
    "cases": cases, "checks": checks,
}
target = Path(__file__).resolve().parents[1] / "output" / "henselian_branch_countermodel_certificate.json"
target.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
