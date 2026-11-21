#!/usr/bin/env python3
"""Exact finite checks for SF-E806.

This verifies the integral exterior identities, obstruction-tensor rank, and
the complete exponent-two lifting case.  The argument for all 2-adic
valuations is the written divided-square lemma, not this finite calculation.
No sheaf construction or formal proof-assistant verification is claimed.
Only the Python standard library is used.
"""

from itertools import combinations
from math import gcd
from functools import reduce
from fractions import Fraction
from pathlib import Path
import hashlib
import json

N = 8


def clean(x):
    return {k: v for k, v in x.items() if v}


def add(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, 0) + v
    return clean(out)


def scale(c, x):
    return clean({k: c * v for k, v in x.items()})


def wedge(x, y):
    out = {}
    for a, ca in x.items():
        for b, cb in y.items():
            if set(a) & set(b):
                continue
            sign = (-1) ** sum(i > j for i in a for j in b)
            key = tuple(sorted(a + b))
            out[key] = out.get(key, 0) + sign * ca * cb
    return clean(out)


def divided_square(x):
    y = wedge(x, x)
    assert all(c % 2 == 0 for c in y.values())
    return clean({k: c // 2 for k, c in y.items()})


def gf2_rank(rows):
    basis = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in basis:
                row ^= basis[p]
            else:
                basis[p] = row
                break
    return len(basis)


def contradiction_witness(rows, rhs, nvars):
    """Return a checked left-kernel witness or None."""
    pivots = {}
    for i, (row, value) in enumerate(zip(rows, rhs)):
        witness = 1 << i
        while row:
            p = row.bit_length() - 1
            if p in pivots:
                rr, vv, ww = pivots[p]
                row ^= rr
                value ^= vv
                witness ^= ww
            else:
                pivots[p] = (row, value, witness)
                break
        if not row and value:
            combined_row = 0
            combined_rhs = 0
            for j, (rj, bj) in enumerate(zip(rows, rhs)):
                if (witness >> j) & 1:
                    combined_row ^= rj
                    combined_rhs ^= bj
            assert combined_row == 0 and combined_rhs == 1
            assert all(row < (1 << nvars) for row in rows)
            return witness
    return None


e = [{(i,): 1} for i in range(N)]
s = e[:4]
t = e[4:]
omega = add(wedge(s[0], s[1]), wedge(s[2], s[3]))
tau = add(wedge(t[0], t[1]), wedge(t[2], t[3]))
mixed = add(
    wedge(s[0], t[1]), wedge(t[0], s[1]),
    wedge(s[2], t[3]), wedge(t[2], s[3]),
)

# Old integral a,b generators expressed in the new integral S,T coordinates.
a = [add(s[0], scale(-1, t[0])), t[0],
     add(s[2], scale(-1, t[2])), t[2]]
b = [add(s[1], scale(-1, t[1])), t[1],
     add(s[3], scale(-1, t[3])), t[3]]
theta = add(*(wedge(a[i], b[i]) for i in range(4)))
U = [[1, 1, 0, 0], [1, -1, 0, 0],
     [0, 0, 1, 1], [0, 0, 1, -1]]
assert [[sum(U[i][k] * U[k][j] for k in range(4))
         for j in range(4)] for i in range(4)] == [
             [2 if i == j else 0 for j in range(4)] for i in range(4)]
theta_U = add(*(scale(U[i][j], wedge(a[i], b[j]))
                for i in range(4) for j in range(4)))
assert theta == add(omega, scale(-1, mixed), scale(2, tau))
assert theta_U == add(omega, scale(-2, tau))
Q = add(wedge(theta, theta), divided_square(theta_U))
q_mod2 = {k: c % 2 for k, c in Q.items() if c % 2}
assert q_mod2 == {(0, 1, 2, 3): 1}
assert reduce(gcd, (abs(c) for c in Q.values())) == 1
Q22 = {k: c for k, c in Q.items() if sum(i < 4 for i in k) == 2}
assert all(c % 2 == 0 for c in Q22.values())
R = {k: (c // 2) % 2 for k, c in Q22.items() if (c // 2) % 2}
expected = add(divided_square(mixed), wedge(omega, tau))
expected_mod2 = {k: c % 2 for k, c in expected.items() if c % 2}
assert R == expected_mod2
S2 = list(combinations(range(4), 2))
T2 = list(combinations(range(4, 8), 2))
R_matrix = [[R.get(a_pair + b_pair, 0) for b_pair in T2] for a_pair in S2]
R_rows = [sum(c << j for j, c in enumerate(row)) for row in R_matrix]
R_rank = gf2_rank(R_rows)
assert R_rank == 6
mixed_square = divided_square(mixed)
mixed_matrix = [[mixed_square.get(ap + bp, 0) % 2 for bp in T2] for ap in S2]
mixed_rank = gf2_rank([sum(c << j for j, c in enumerate(row))
                      for row in mixed_matrix])
assert mixed_rank == 6

# Local normal form for the separate extension SF-E807.  These substitutions
# check its formula, not its assertion for all even squarefree radicands.
local_checks = []
for delta in (2, 6, 10, 14, 22, 26, 30, 34, 38):
    theta_local = mixed
    theta_u_local = add(omega, scale(delta, tau))
    q_local = add(wedge(theta_local, theta_local),
                  scale(Fraction(1, delta), wedge(theta_u_local, theta_u_local)))
    h = delta // 2
    formula = add(scale(2, divided_square(mixed)),
                  scale(Fraction(1, h), divided_square(omega)),
                  scale(2, wedge(omega, tau)),
                  scale(4 * h, divided_square(tau)))
    assert q_local == formula

    def mod2_odd_denominator(c):
        c = Fraction(c)
        assert c.denominator % 2
        return c.numerator % 2

    local_mod2 = {key: mod2_odd_denominator(c) for key, c in q_local.items()
                  if mod2_odd_denominator(c)}
    assert local_mod2 == {(0, 1, 2, 3): 1}
    local22 = {key: c for key, c in q_local.items()
               if sum(i < 4 for i in key) == 2}
    local_R = {key: mod2_odd_denominator(Fraction(c) / 2)
               for key, c in local22.items()
               if mod2_odd_denominator(Fraction(c) / 2)}
    assert local_R == R
    local_checks.append({"delta": delta, "formula_checked": True, "R_rank": 6})

# A direct mod-four lift check for all nondegenerate alternating forms on S.
# The general lemma first proves that every e=2 solution must reduce to one
# of these forms; that structural fact is not assumed as a computational
# enumeration of all 2^28 ambient two-forms.
two_keys = list(combinations(range(N), 2))
four_keys = list(combinations(range(N), 4))
lift_checks = []
for mask in range(1 << len(S2)):
    ell0 = {pair: 1 for j, pair in enumerate(S2) if (mask >> j) & 1}
    ell0_square = divided_square(ell0)
    if ell0_square.get((0, 1, 2, 3), 0) % 2 != 1:
        continue
    difference = add(Q, scale(-1, ell0_square))
    assert all(c % 2 == 0 for c in difference.values())
    rhs = [(difference.get(key, 0) // 2) % 2 for key in four_keys]
    columns = [wedge(ell0, {key: 1}) for key in two_keys]
    rows = [sum((column.get(key, 0) % 2) << j
                for j, column in enumerate(columns)) for key in four_keys]
    witness = contradiction_witness(rows, rhs, len(two_keys))
    assert witness is not None
    rank = gf2_rank(rows)
    augmented_rank = gf2_rank([
        row | (value << len(two_keys)) for row, value in zip(rows, rhs)])
    assert augmented_rank == rank + 1
    lift_checks.append({
        "S_form_mask": mask,
        "coefficient_rank": rank,
        "augmented_rank": augmented_rank,
        "left_kernel_contradiction_witness_hex": hex(witness),
        "witness_checked": True,
    })
assert len(lift_checks) == 28

# SF-E808: odd radicands with discriminant divisible by four.
def contract(form, index):
    return {
        tuple(i for i in key if i != index):
        c * ((-1) ** key.index(index))
        for key, c in form.items() if index in key
    }


odd_normal_checks = []
odd_mod2 = None
for delta in (3, 7, 11, 19, 23, 31, 43, 47):
    theta_u_local = add(omega, scale(delta, tau))
    q_local = add(divided_square(mixed),
                  scale(Fraction(1, delta), divided_square(theta_u_local)))
    formula = add(divided_square(mixed),
                  scale(Fraction(1, delta), divided_square(omega)),
                  wedge(omega, tau),
                  scale(delta, divided_square(tau)))
    assert q_local == formula
    reduced = {key: mod2_odd_denominator(c) for key, c in q_local.items()
               if mod2_odd_denominator(c)}
    if odd_mod2 is None:
        odd_mod2 = reduced
    assert reduced == odd_mod2
    odd_normal_checks.append({"delta": delta, "formula_checked": True})
chi = {key: c % 2 for key, c in contract(odd_mod2, 0).items() if c % 2}
assert chi == {
    (1, 2, 3): 1, (1, 6, 7): 1, (2, 5, 7): 1, (3, 5, 6): 1
}
chi_columns = [wedge(v, chi) for v in e]
chi_rows = [sum((col.get(key, 0) % 2) << j
                for j, col in enumerate(chi_columns)) for key in four_keys]
chi_rank = gf2_rank(chi_rows)
assert chi_rank == 8
odd_five_keys = list(combinations(range(N), 5))
odd_q_columns = [wedge(v, odd_mod2) for v in e]
odd_q_wedge_rank = gf2_rank([
    sum((col.get(key, 0) % 2) << j for j, col in enumerate(odd_q_columns))
    for key in odd_five_keys])
assert odd_q_wedge_rank == 8

report = {
    "statement": "SF-E806",
    "status": "PASS",
    "arithmetic": "exact integer exterior algebra and F_2 row elimination",
    "basis": ["s0", "s1", "s2", "s3", "t0", "t1", "t2", "t3"],
    "U_squared": "2 I_4",
    "integral_theta_identities": True,
    "Q_primitive": True,
    "Q_mod2": "s0 s1 s2 s3",
    "mixed_divided_square_tensor_rank": mixed_rank,
    "obstruction_tensor_R_rank": R_rank,
    "R_matrix_over_F2": R_matrix,
    "nondegenerate_S_forms": 28,
    "mod4_lifts_inconsistent": len(lift_checks),
    "lift_checks": lift_checks,
    "SF_E807_local_normal_form_checks": local_checks,
    "SF_E808_local_normal_form_checks": odd_normal_checks,
    "SF_E808_contraction_wedge_rank": chi_rank,
    "SF_E808_four_form_wedge_rank": odd_q_wedge_rank,
    "scope": (
        "The certificate checks the finite tensor and e=2 lift computation. "
        "The all-positive-rank assertion uses the written two-adic lifting "
        "lemma; no bounded enumeration is asserted to prove all ranks."
    ),
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
target = Path(__file__).with_name("rm_sqrt2_lattice_certificate_output.json")
target.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({
    "statement": report["statement"],
    "status": report["status"],
    "R_rank": R_rank,
    "inconsistent_mod4_lifts": len(lift_checks),
    "output": str(target),
}))
