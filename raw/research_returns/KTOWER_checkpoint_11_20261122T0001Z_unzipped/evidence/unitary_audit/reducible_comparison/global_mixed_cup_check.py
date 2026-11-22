#!/usr/bin/env python3
"""Exact degree-two matrix identities; not a cohomology or existence proof."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sympy as sp

s, t = sp.symbols("s t")
ug, vg, wg, uh, vh, wh, alpha, beta, d, a = sp.symbols(
    "ug vg wg uh vh wh alpha beta d a"
)
I = sp.eye(3)
X = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
Y = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, -1, 0]])
Z = X * Y - Y * X
J = sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])


def trunc(value):
    poly = sp.Poly(sp.expand(value), s, t)
    return sp.expand(sum(coef * s**i * t**j
                         for (i, j), coef in poly.terms() if i < 2 and j < 2))


def trmat(matrix):
    return matrix.applyfunc(trunc)


def exp2(matrix):
    return trmat(I + matrix + matrix * matrix / 2)


def equal(left, right):
    return trmat(left - right) == sp.zeros(3)


Lg = s * ug * X + t * vg * Y + s * t * wg * Z
Lh_action = s * alpha * uh * X + t * beta * vh * Y + s * t * alpha * beta * wh * Z
mixed = (ug * beta * vh - vg * alpha * uh) / 2
Lgh = (s * (ug + alpha * uh) * X + t * (vg + beta * vh) * Y
       + s * t * (wg + alpha * beta * wh + mixed) * Z)
checks = {
    "bracket": Z == sp.diag(1, -2, 1),
    "outer_X_negative": -J * X.T * J == -X,
    "outer_Y_positive": -J * Y.T * J == Y,
    "outer_Z_negative": -J * Z.T * J == -Z,
    "BCH_cocycle_identity": equal(exp2(Lg) * exp2(Lh_action), exp2(Lgh)),
    "determinant_one": trunc(exp2(Lg).det()) == 1,
    "ordinary_negative_coboundary_removal": equal(
        exp2(t * d * Y) * exp2(Lg.subs(vg, beta * d - d)) * exp2(-t * beta * d * Y),
        exp2(s * ug * X + s * t * (wg - d * (1 + beta) * ug / 2) * Z),
    ),
    "away_positive_coboundary_removal": equal(
        exp2(s * a * X) * exp2(Lg.subs(ug, alpha * a - a)) * exp2(-s * alpha * a * X),
        exp2(t * vg * Y + s * t * (wg + a * (1 + alpha) * vg / 2) * Z),
    ),
}
assert all(checks.values()), checks
script = Path(__file__).resolve()
report = {
    "verified_utc": datetime.now(timezone.utc).isoformat(),
    "model": "GPT-6 Astra Pro",
    "effort": "not exposed",
    "script_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
    "ring": "Q[ug,vg,wg,uh,vh,wh,alpha,beta,d,a,s,t]/(s^2,t^2)",
    "scope": "Exact matrix identities only; cohomological and arithmetic assertions require the written proof",
    "checks": checks,
}
script.with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"all_pass": True, "checks": len(checks), "script_sha256": report["script_sha256"]}))
