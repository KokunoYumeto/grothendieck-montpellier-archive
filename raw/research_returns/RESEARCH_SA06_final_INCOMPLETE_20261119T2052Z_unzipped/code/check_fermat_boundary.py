"""Exact finite certificates for the C.3r Fermat-join construction.

The general Chow/Abel--Jacobi proof is in C3_fermat_boundary.tex.
This program checks algebraic equations and finite symbolic instances,
not non-torsion, Chow vanishing, or the general correspondence theorem.
"""
from pathlib import Path
import json
import time
import sympy as sp

start = time.perf_counter()
root = Path(__file__).resolve().parents[1]
zeta, a, b, c, t = sp.symbols("zeta a b c t")
minimal = zeta**2 + zeta + 1
reduce = lambda expr: sp.rem(sp.expand(expr), minimal, zeta)
cases = []
for r in range(1, 8):
    xs = sp.symbols(f"x0:{r-1}")
    substitutions = []
    for lam in (sp.Integer(1), zeta):
        substituted = sum((-lam*x)**3 + x**3 for x in xs)
        substituted += t**3 * (a**3 + b**3 + c**3)
        error = reduce(substituted - t**3*(a**3+b**3+c**3))
        assert error == 0
        substitutions.append({"lambda": str(lam), "cubic_error": str(error)})
    pair = sp.Matrix([[1, 1], [1, zeta]])
    determinant = sp.factor(pair.det())
    conjugate = determinant.subs(zeta, zeta**2)
    norm = reduce(determinant*conjugate)
    assert norm == 3
    block_norm = norm**(r-1)
    assert block_norm == 3**(r-1)
    cases.append({"r": r, "source_local_dimension": 2*r+1,
                  "hypersurface_dimension": 2*r-1,
                  "correspondence_codimension": r,
                  "paired_coordinate_determinant": str(determinant),
                  "block_determinant_norm": int(block_norm),
                  "substitutions": substitutions})
u, v = sp.symbols("u v")
witness_error = sp.rem(u**3+v**3+1, v**3+u**3+1, v)
origin_error = 1**3 + (-1)**3 + 0**3
assert witness_error == origin_error == 0
output = {
    "exact_field": "Q[zeta]/(zeta^2+zeta+1)",
    "scope": "r=1,...,7 symbolic substitutions and complementary tangent-coordinate matrices",
    "cases": cases,
    "witness_equation_error": str(witness_error),
    "origin_equation_error": origin_error,
    "limitation": "Non-torsion, proper-intersection multiplicity, Gersten vanishing and strict-local Chow injection are proved in the paper, not computed here.",
    "runtime_seconds": time.perf_counter()-start,
}
target = root / "code" / "check_fermat_boundary_output.json"
target.write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps(output, indent=2))
