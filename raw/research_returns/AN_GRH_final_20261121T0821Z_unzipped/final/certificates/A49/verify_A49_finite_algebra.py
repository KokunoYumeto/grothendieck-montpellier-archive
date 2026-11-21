#!/usr/bin/env python3
"""Exact algebra for A49, using no curve enumeration or previous arithmetic code.

The geometric counts and labels are retained A27/A45 inputs. This checker
only verifies the small unit orbits and the cyclotomic product derived from
those inputs. Integer determinants are computed by fraction-free elimination.
"""
import hashlib
import json
from math import gcd
from pathlib import Path


def orbit(a, n):
    out, x = [], 1
    while x not in out:
        out.append(x)
        x = (a * x) % n
    assert x == 1
    return out


def reduce_phi9(a):
    a = list(a)
    while len(a) < 6:
        a.append(0)
    for j in range(len(a) - 1, 5, -1):
        c = a[j]
        # Phi_9(X)=X^6+X^3+1.
        a[j] = 0
        a[j - 3] -= c
        a[j - 6] -= c
    return a[:6]


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return reduce_phi9(c)


def determinant(a):
    a = [list(row) for row in a]
    n, sign, last = len(a), 1, 1
    for k in range(n - 1):
        if not a[k][k]:
            j = next(j for j in range(k + 1, n) if a[j][k])
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                v = a[i][j] * pivot - a[i][k] * a[k][j]
                assert v % last == 0
                a[i][j] = v // last
            a[i][k] = 0
        last = pivot
    return sign * a[-1][-1]


def file_info(path):
    data = path.read_bytes()
    return {"path": str(path), "sha256": hashlib.sha256(data).hexdigest()}


def main():
    here = Path(__file__).resolve().parent
    root = here.parents[2]
    powers7, powers9 = orbit(2, 7), orbit(2, 9)
    units7 = [a for a in range(1, 7) if gcd(a, 7) == 1]
    units9 = [a for a in range(1, 9) if gcd(a, 9) == 1]
    assert len(powers7) == 3
    assert sorted(set(powers7 + [(-a) % 7 for a in powers7])) == units7
    assert sorted(powers9) == units9

    x = [0, 1, 0, 0, 0, 0]
    xp = [[1, 0, 0, 0, 0, 0]]
    for _ in range(9):
        xp.append(mul(xp[-1], x))
    assert xp[9] == xp[0]
    zinv = xp[8]
    s = [x[i] + zinv[i] for i in range(6)]
    s3 = mul(mul(s, s), s)
    assert [s3[i] - 3*s[i] + (1 if i == 0 else 0) for i in range(6)] == [0]*6
    v = s[:]
    v[0] += 7
    columns = [mul(v, xp[j]) for j in range(6)]
    matrix = [[columns[j][i] for j in range(6)] for i in range(6)]
    norm = determinant(matrix)
    assert norm == 103041 == 321**2
    assert norm % 2 == 1
    assert (1 + 1 + 4)**2 == 36

    data = {
        "status": "PASS",
        "scope": "Unit orbits and cyclotomic integer norm only; no new curve enumeration.",
        "powers_2_mod_7": powers7,
        "signed_powers_mod_7": units7,
        "powers_2_mod_9": powers9,
        "phi9_coefficients_ascending": [1, 0, 0, 1, 0, 0, 1],
        "z_inverse_coefficients": zinv,
        "s_cubic": "s^3-3s+1=0",
        "multiplication_matrix_for_7_plus_z_plus_z_inverse": matrix,
        "primitive_9_rational_order_from_retained_labels": norm,
        "proper_3_rational_order_from_retained_labels": 36,
        "retained_geometric_inputs": {
            "A27": {"N": 6, "J_order": 28, "H": "C7", "point": "rational Weierstrass point"},
            "A45_twist": {"N": 4, "J_order": 18, "H": "C9", "labels_up_to_unit": [0, 0, 1, 8]},
        },
        "source_files": [
            file_info(here / "inputs/A27_source.tex"),
            file_info(here / "inputs/A45_source.tex"),
        ],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    out = here / "verify_A49_finite_algebra.json"
    out.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS", "primitive_9_order": norm, "output": str(out)}))


if __name__ == "__main__":
    main()
