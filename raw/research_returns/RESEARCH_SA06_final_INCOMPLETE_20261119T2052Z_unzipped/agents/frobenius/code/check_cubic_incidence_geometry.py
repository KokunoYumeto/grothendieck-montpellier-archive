"""Exact finite certificate for the F_125 cubic/quartic incidence input.

This checks the finite identities used by the accompanying geometric proof.
It does not claim to prove the proposed higher-Chow kernel.
"""
from datetime import datetime, timezone
import json
from pathlib import Path
from time import perf_counter
import sympy as sp

started = datetime.now(timezone.utc)
tic = perf_counter()
ell, y, r = sp.symbols("lambda y r")
field_poly = ell**3 + ell + 1
checks = []


def check(name, condition, evidence=None):
    checks.append({"name": name, "passed": bool(condition), "evidence": evidence})
    if not condition:
        raise AssertionError(name)


def reduce_field(poly):
    return sp.Poly(sp.rem(poly, field_poly, ell, domain=sp.GF(5)), ell,
                   modulus=5).as_expr()


values = [int(field_poly.subs(ell, a)) % 5 for a in range(5)]
check("cubic field polynomial has no F5 root", all(values), values)
power12 = reduce_field(ell**12)
check("lambda^12 = 2-lambda", reduce_field(ell**12 - (2-ell)) == 0,
      str(power12))
for a in (1, 3, 4):
    check(f"lambda^12 differs from {a}", reduce_field(ell**12-a) != 0,
          str(reduce_field(ell**12-a)))

branch_resultant = sp.Poly(
    sp.resultant(y**3-1, (1+y)**3+r, y), r, modulus=5).as_expr()
check("common-branch resultant", sp.Poly(
    branch_resultant-(r-2)*(r-1)**2, r, modulus=5).is_zero,
    str(branch_resultant))
check("A branch transverse", int(sp.resultant(y**3-1, 1+y, y)) % 5 != 0,
      int(sp.resultant(y**3-1, 1+y, y)) % 5)

z0,z1,z2,s,t = sp.symbols("z0 z1 z2 s t")
w = [z1*s, -z0*s, ell*z2*t, -z0*t]
a0 = w[0]*z0+w[1]*z1
a1 = w[2]*z0+ell*w[3]*z2
check("first kernel equation", sp.expand(a0) == 0)
check("second kernel equation", sp.expand(a1) == 0)
A = z1**3-z0**3
B = ell**3*z2**3-z0**3
check("restricted Fermat cubic", sp.expand(sum(v**3 for v in w)
                                         -A*s**3-B*t**3) == 0)
check("p does not divide cubic cover degree", 3 % 5 != 0)

x0,x1,w0,w1,w2,w3 = sp.symbols("x0 x1 w0 w1 w2 w3")
g = [x0*w0+x1*w2, x0*w1, ell*x1*w3]
monomials = [x0*w0,x0*w1,x0*w2,x0*w3,
             x1*w0,x1*w1,x1*w2,x1*w3]
M = sp.Matrix([[sp.expand(v).coeff(m) for v in g] for m in monomials])
minor = M[[0,1,7],:].det()
check("three canonical coefficients independent", minor == ell, str(minor))
on_D = [sp.expand(v.subs({w0:-s,w1:s,w2:-t,w3:t})) for v in g]
check("restriction of g0", sp.expand(on_D[0]+x0*s+x1*t) == 0)
check("restriction of g1", on_D[1] == x0*s)
check("restriction of g2", on_D[2] == ell*x1*t)
check("restriction rank two", sp.Matrix(
    [[-1,1,0],[-1,0,ell]]).rank() == 2)

finished = datetime.now(timezone.utc)
payload = {
    "started_utc": started.isoformat(),
    "finished_utc": finished.isoformat(),
    "runtime_seconds": perf_counter()-tic,
    "field": "F5[lambda]/(lambda^3+lambda+1)",
    "a0": "z0*w0+z1*w1",
    "a1": "z0*w2+lambda*z2*w3",
    "checks": checks,
    "passed": all(c["passed"] for c in checks),
    "scope": "Finite identities for the elementary all-geometric-point smoothness proof; no higher-Chow conclusion.",
}
out = Path(__file__).resolve().parents[1]/"output"/"C3bi_cubic_incidence_geometry.json"
out.write_text(json.dumps(payload, indent=2)+"\n")
print(json.dumps(payload, indent=2))
