#!/usr/bin/env python3
"""Exact matrix/linearization checks for projector_results.tex.

This checks the Cayley slice and the stated elementary cotangent examples.
It does not check the deformation-functor, Selmer, or source-length proofs.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
x, y, q, t, u, z = sp.symbols("x y q t u z")
eye = sp.eye(3)
J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
K = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
D = sp.diag(-1, 1, -1)
X = sp.Matrix([[0, 1, 0], [0, 0, -1], [0, 0, 0]])
Y = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, -1, 0]])
Yplus = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
W = x * X + y * Y
H = (eye - W / 2).inv() * (eye + W / 2)
Hminus = H.subs({x: -x, y: -y}, simultaneous=True)
T = sp.diag(t, 1, 1 / t)
M0 = sp.diag(q, 1, 1 / q)


def canonical(value):
    return sp.cancel(sp.together(value))


def kappa(M):
    return K * M.inv().T * K


def kappa_lie(M):
    return -K * M.T * K


def marking(M):
    return sp.Matrix([M[0, 1] - M[1, 2], M[1, 0] - M[2, 1]])


checks = []


def check(name, left, right):
    difference = left - right
    if isinstance(difference, sp.MatrixBase):
        entries = list(difference)
    else:
        entries = [difference]
    residual = [canonical(value) for value in entries]
    assert all(value == 0 for value in residual), (name, residual)
    checks.append({"name": name, "pass": True, "entries": len(entries)})


check("K equals minus D J", K, -D * J)
check("X lies in so(J)", X * J + J * X.T, sp.zeros(3))
check("Y lies in so(J)", Y * J + J * Y.T, sp.zeros(3))
check("Cayley preserves J", H * J * H.T, J)
check("Cayley inverse stays in the same cross-section", H * Hminus, eye)
check("kappa sends Cayley coordinates to their negatives", kappa(H), Hminus)
check("Cayley cross-section is torus equivariant", T * H * T.inv(),
      H.subs({x: t * x, y: y / t}, simultaneous=True))
check("base matrix is kappa fixed", kappa(M0), M0)
check("rational Selmer root is kappa odd", kappa_lie(Y), -Y)
check("principal adjoint root is kappa even", kappa_lie(Yplus), Yplus)

orbit = H * M0 * Hminus
old_mark = marking(orbit).applyfunc(canonical)
odd_mark = ((old_mark - marking(kappa(orbit))) / 2).applyfunc(canonical)
old_jac = old_mark.jacobian([x, y]).subs({x: 0, y: 0})
odd_jac = odd_mark.jacobian([x, y]).subs({x: 0, y: 0})
expected_jac = sp.diag(1 / q - q, q - 1 / q)
check("old marking Jacobian", old_jac, expected_jac)
check("odd marking Jacobian", odd_jac, expected_jac)
check("marking Jacobian determinant", old_jac.det(), -(q**2 - 1)**2 / q**2)

# The examples use z for the symbolic nonzero coefficient pi^n.
relations_vertical = [z * u, u**2]
vertical_linear = [sp.diff(f, u).subs(u, 0) for f in relations_vertical]
check("vertical example has unsquared normal coefficient z",
      sp.Matrix(vertical_linear), sp.Matrix([z, 0]))
flat_relation = u * (u**2 - z**2)
check("flat reduced example has normal coefficient minus z squared",
      sp.diff(flat_relation, u).subs(u, 0), -z**2)
check("flat example has the three generic roots",
      sp.Matrix([flat_relation.subs(u, a) for a in [0, z, -z]]), sp.zeros(3, 1))

result = {
    "scope": "Exact rational matrix identities and elementary linear terms only; no deformation or Selmer proof automation.",
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "checks": checks,
    "check_count": len(checks),
    "all_pass": all(record["pass"] for record in checks),
    "Cayley_denominator": str(sp.factor((eye - W / 2).det())),
    "Jacobian": [[str(canonical(expected_jac[i, j])) for j in range(2)] for i in range(2)],
    "Jacobian_determinant": str(sp.factor(expected_jac.det())),
    "vertical_example_odd_cotangent_length": "n for O[[u]]/(pi^n*u,u^2)",
    "flat_example_odd_cotangent_length": "2*n at u=0 for O[[u]]/(u*(u^2-pi^(2*n)))",
}
target = HERE / "projector_matrix_check.json"
target.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"checks": len(checks), "all_pass": result["all_pass"],
                  "script_sha256": result["script_sha256"]}, sort_keys=True))
