#!/usr/bin/env python3
"""Exact finite determinant checks for AM-K014.

This directly uses the finite Pluecker determinant K14.6, without the
first-frame-shift shortcut. It is a certificate for the stated low jets;
the all-order identification is the cited tau/sigma theorem plus the
specialization proved in jacobian_reduced_theta.md.
"""
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import sympy as sp

BASE = Path(__file__).resolve().parent
v1, v2, v3 = sp.symbols("v1 v2 v3")


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None:
        maximum = n
    for first in range(min(n, maximum), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def nongap(j):
    """One-based increasing nongaps at infinity on y^2=x^7-1."""
    return 2 * (j - 1) if j <= 4 else j + 2


@lru_cache(None)
def a_inverse_coefficient(m, exponent):
    if exponent < 0 or exponent % 14:
        return sp.Integer(0)
    k = exponent // 14
    if k == 0:
        return sp.Integer(1)
    if m == 0:
        return sp.Integer(0)
    value = sp.Rational(m, k) * (-1) ** (k - 1) * sp.binomial(7 * k - m - 1, k - 1)
    assert value.is_Integer
    return value


def pluecker(mu, extra_tail=0):
    length = max(3, len(mu)) + extra_tail
    padded = mu + (0,) * (length - len(mu))
    matrix = sp.Matrix(length, length, lambda i, j:
        a_inverse_coefficient(nongap(j + 1) // 2,
                              padded[i] - (i + 1) - (2 - nongap(j + 1))))
    if any(not any(matrix[i, j] for j in range(length)) for i in range(length)):
        return sp.Integer(0)
    if any(not any(matrix[i, j] for i in range(length)) for j in range(length)):
        return sp.Integer(0)
    return matrix.det(method="domain-ge")


@lru_cache(None)
def p_complete(n):
    if n < 0:
        return sp.Integer(0)
    return sp.expand(sum(
        v1 ** a * v2 ** b * v3 ** (n - 5 * a - 3 * b) /
        (sp.factorial(a) * sp.factorial(b) * sp.factorial(n - 5 * a - 3 * b))
        for a in range(n // 5 + 1)
        for b in range((n - 5 * a) // 3 + 1)))


def schur(mu):
    length = len(mu)
    return sp.expand(sp.Matrix(length, length,
        lambda i, j: p_complete(mu[i] - i + j)).det(method="domain-ge"))


@lru_cache(None)
def p_at_v1_one(n):
    return 1 / sp.factorial(n // 5) if n >= 0 and n % 5 == 0 else sp.Integer(0)


def schur_at_v1_one(mu):
    length = len(mu)
    return sp.Matrix(length, length,
        lambda i, j: p_at_v1_one(mu[i] - i + j)).det(method="domain-ge")


expected_s321 = v1*v3 - v2**2 - v2*v3**3/3 + v3**6/45
assert sp.expand(schur((3, 2, 1)) - expected_s321) == 0
assert pluecker((3, 2, 1)) == 1
assert pluecker((3, 2, 1), extra_tail=3) == 1

weight20 = []
count = 0
total = sp.Integer(0)
for mu in partitions(20):
    count += 1
    xi = pluecker(mu)
    if xi:
        assert pluecker(mu, extra_tail=2) == xi
        value = schur_at_v1_one(mu)
        total += xi * value
        weight20.append({"partition": list(mu), "xi": str(xi),
                         "S_mu_at_v1_1_v2_v3_0": str(value),
                         "contribution_v1_fourth": str(xi * value)})
assert count == 627
assert total == sp.Rational(1, 3)
nonzero_contributions = [r for r in weight20 if r["contribution_v1_fourth"] != "0"]
assert len(nonzero_contributions) == 4
assert [(r["xi"], r["S_mu_at_v1_1_v2_v3_0"]) for r in nonzero_contributions] == [
    ("-1", "-1/6"), ("3", "-1/2"), ("-6", "-1/2"), ("8", "-1/6")]

u1, u2, u3 = sp.symbols("u1 u2 u3")
q_start = sp.expand(4 * expected_s321.subs({v1:u1/2, v2:u2/2, v3:u3/2}) +
                    4 * total * (u1/2)**4)
jets = {
    "d1_d3": sp.diff(q_start, u1, u3).subs({u1:0,u2:0,u3:0}),
    "d2_squared": sp.diff(q_start, u2, 2).subs({u1:0,u2:0,u3:0}),
    "d1_fourth": sp.diff(q_start, u1, 4).subs({u1:0,u2:0,u3:0}),
    "d3_sixth": sp.diff(q_start, u3, 6).subs({u1:0,u2:0,u3:0}),
}
assert jets == {"d1_d3":1,"d2_squared":-2,"d1_fourth":2,"d3_sixth":1}

result = {
    "checked_utc":datetime.now(timezone.utc).isoformat(),
    "method":"Direct finite determinant K14.6 and Jacobi-Trudi Schur determinants, exact rational arithmetic",
    "S321":str(expected_s321),
    "weight20_partitions_exhaustively_checked":count,
    "weight20_nonzero_Pluecker_coordinates":weight20,
    "weight20_coefficient_v1_fourth":str(total),
    "sigma_q_selected_terms":str(q_start),
    "sigma_q_actual_Hurwitz_jets":{k:str(v) for k,v in jets.items()},
    "scope":"Exact low-order certificate. The all-order actual theta identification and integrality use AM-K014's proof and cited tau/sigma theorem.",
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "status":"PASS",
}
destination = BASE / "jacobian_sigma_determinant_certificate.json"
destination.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
