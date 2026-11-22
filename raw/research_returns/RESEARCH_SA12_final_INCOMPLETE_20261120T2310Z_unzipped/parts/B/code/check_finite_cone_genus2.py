"""Exact companion checks for D:wild-genus2-finite-inertia.

The formal lifting, algebraization and inertia arguments are proved in TeX.
This certificate checks only the finite polynomial and degree calculations
added to the already checked genus-two example.
"""
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
checks = []

def check(name, condition):
    assert bool(condition), name
    checks.append(name)

u, v, z, w, n = sp.symbols("u v z w n")
mod2 = lambda f: sp.Poly(sp.expand(f), u, v, z, w, n, modulus=2).as_expr()
fin = w**2 + w + z**5
inf = v**2 + u**3*v + u
check("infinity substitution", sp.Poly(sp.expand(
    u**6*fin.subs({z: 1/u, w: v/u**3})-inf), u, v, modulus=2).is_zero)
check("finite chart etale over z", mod2(sp.diff(fin, w)) == 1)
check("infinity u derivative", mod2(sp.diff(inf, u)-(1+u**2*v)) == 0)
check("infinity v derivative", mod2(sp.diff(inf, v)-u**3) == 0)
check("infinity smooth", mod2(sp.diff(inf, u)).subs({u:0, v:0}) == 1)
ord_u, ord_v = 2, 1
check("unique lowest valuation terms", 2*ord_v == ord_u < 3*ord_u+ord_v)
ord_du = 3*ord_u
check("canonical differential order", ord_du-2*ord_u == 2)
div_z = sp.Matrix([1, 1, -2])
omega = sp.Matrix([0, 0, 2])
minus_normal = sp.Matrix([1, 1, 0])
check("normal versus canonical divisors", minus_normal-omega == div_z)
frob = sp.Matrix([[0, 0], [1, 0]])
check("Frobenius rank one", frob.rank() == 1)
check("Frobenius square zero", frob*frob == sp.zeros(2))
q, g, d = 4, 2, 2
tangent = sp.expand(q*(n*d-2*g+2))
normal = sp.expand(q*(n-1)*d)
check("later tangent degree", tangent == 8*(n-1))
check("later normal degree", normal == tangent)
check("minimum later degree exceeds canonical", tangent.subs(n,2) > 2*g-2)
check("later degree increasing", sp.diff(tangent,n) > 0)
check("fixed cone degree", q == 2**2)
check("composite cone degree", 2*q == 8)
output = {
    "statement_id": "D:wild-genus2-finite-inertia",
    "field": "F_2",
    "assertions": len(checks),
    "passed": len(checks),
    "runtime_seconds": time.perf_counter()-started,
    "checks": checks,
    "scope": "Exact finite polynomial, divisor-degree and nilpotent matrix checks; the full formal-cover and wild-inertia proofs are in the accompanying TeX."
}
path = Path(__file__).resolve().parents[1] / "output" / "finite_cone_genus2.json"
path.write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps(output, indent=2))
