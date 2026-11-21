#!/usr/bin/env python3
"""Finite exact checks for A030; the arbitrary-n proof is in the TeX file.

Differentiate the defining permutation sum of the permanent directly, then
compare its integer Hessian determinant with the closed block formula.
No formula for Hessian entries or for its rank is used to build the matrix.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp


def permanent_jet(n: int, t: int):
    r = n * n
    value = 0
    gradient = [0] * r
    hessian = [[0] * r for _ in range(r)]
    for permutation in itertools.permutations(range(n)):
        coordinates = [i * n + permutation[i] for i in range(n)]
        factors = [t if i == 0 and permutation[i] == 0 else 1 for i in range(n)]
        value += math.prod(factors)
        for i, coordinate in enumerate(coordinates):
            gradient[coordinate] += math.prod(factors[j] for j in range(n) if j != i)
        for i in range(n):
            for j in range(i + 1, n):
                coefficient = math.prod(factors[k] for k in range(n) if k != i and k != j)
                hessian[coordinates[i]][coordinates[j]] += coefficient
                hessian[coordinates[j]][coordinates[i]] += coefficient
    return value, gradient, sp.Matrix(hessian)


def expected_hessian_determinant(n: int, t: int):
    k = n - 1
    b = math.factorial(n - 2)
    c = math.factorial(n - 3) * (t + n - 3)
    return b ** (4 * k) * k ** (2 * k + 2) * c ** ((k - 1) ** 2)


def determinant_hessian_at_identity(n: int):
    # Independently differentiate the signed permutation sum at the identity.
    r = n * n
    hessian = [[0] * r for _ in range(r)]
    for permutation in itertools.permutations(range(n)):
        sign = (-1) ** sum(permutation[i] > permutation[j] for i in range(n) for j in range(i + 1, n))
        coordinates = [i * n + permutation[i] for i in range(n)]
        factors = [int(permutation[i] == i) for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                coefficient = sign * math.prod(factors[k] for k in range(n) if k != i and k != j)
                hessian[coordinates[i]][coordinates[j]] += coefficient
                hessian[coordinates[j]][coordinates[i]] += coefficient
    return sp.Matrix(hessian)


def main():
    rows = []
    for n in range(3, 7):
        t = 1 - n
        value, gradient, hessian = permanent_jet(n, t)
        determinant = int(hessian.det(method="domain-ge"))
        expected = expected_hessian_determinant(n, t)
        assert value == 0
        assert gradient[0] == math.factorial(n - 1)
        assert determinant == expected != 0
        q = n * n * (n - 2)
        theta_11 = q * determinant * gradient[0]
        assert theta_11 != 0
        determinant_constant = int(determinant_hessian_at_identity(n).det(method="domain-ge"))
        expected_constant = (n - 1) * (-1) ** (n * (n + 1) // 2 - 1)
        assert determinant_constant == expected_constant
        row = {
            "n": n, "t": t, "permanent": value,
            "gradient_11": gradient[0],
            "permanent_hessian_determinant": determinant,
            "permanent_hessian_rank": n * n,
            "rank_justification": "nonzero exact determinant",
            "theta_11": theta_11,
            "determinant_hessian_at_identity": determinant_constant,
            "lambda": [n + q + 1, 3] + [2] * (n * n - 2),
            "outer_degree": n * n + 1,
        }
        rows.append(row)
        print(row, flush=True)

    general_point_checks = []
    for n, t in [(3, 0), (3, 1), (3, 3), (4, 0), (4, 1), (4, -1)]:
        value, gradient, hessian = permanent_jet(n, t)
        actual = int(hessian.det(method="domain-ge"))
        expected = expected_hessian_determinant(n, t)
        assert actual == expected
        general_point_checks.append({"n": n, "t": t, "determinant": actual})

    source = Path(__file__)
    result = {
        "finding": "A030",
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "model": "GPT-6 Astra Pro",
        "effort": "not exposed",
        "run": "GCT_KRON_20261120",
        "method": "Exact differentiation of the defining permutation sums; integer determinant elimination.",
        "scope": "Finite checks supplement the general proof and the cited Mignon--Ressayre proposition.",
        "script_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "smooth_zero_checks": rows,
        "general_point_checks": general_point_checks,
        "result": "PASS",
    }
    target = source.with_name("HESSIAN_OBSTRUCTION_CERTIFICATE.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(target, flush=True)


if __name__ == "__main__":
    main()
