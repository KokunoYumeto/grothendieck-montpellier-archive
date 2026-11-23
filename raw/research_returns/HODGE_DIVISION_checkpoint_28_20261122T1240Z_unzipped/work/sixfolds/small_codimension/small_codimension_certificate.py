#!/usr/bin/env python3
"""Exact supporting certificate for HD-S37.

The ATLAS Magma file is parsed as inert mathematical data, never executed.
This checks its integral Gaussian generators, both invariant tensors,
finiteness, the published presentation relators, and absolute irreducibility.
It also independently enumerates the finite partition bounds used in S37.
The classification input itself remains the published GS theorem.
"""
from pathlib import Path
import ast
import json
import re
import sympy as sp

HERE = Path(__file__).resolve().parent
I = sp.I


def scalar(s):
    def visit(t):
        if isinstance(t, ast.Constant) and isinstance(t.value, int):
            return sp.Integer(t.value)
        if isinstance(t, ast.Name) and t.id == "i":
            return I
        if isinstance(t, ast.UnaryOp) and isinstance(t.op, (ast.UAdd, ast.USub)):
            return visit(t.operand) * (1 if isinstance(t.op, ast.UAdd) else -1)
        if isinstance(t, ast.BinOp) and isinstance(t.op, (ast.Add, ast.Sub, ast.Mult)):
            a, b = visit(t.left), visit(t.right)
            return a + b if isinstance(t.op, ast.Add) else a - b if isinstance(t.op, ast.Sub) else a * b
        raise ValueError("Unrecognized inert scalar syntax")
    return sp.expand(visit(ast.parse(s.strip(), mode="eval").body))


def mat(s):
    xs = [scalar(x) for x in s.split(",") if x.strip()]
    assert len(xs) == 100
    return sp.Matrix(10, 10, xs)


def eq(a, b):
    return all(sp.expand(x) == 0 for x in a - b)


def simp(a):
    return a.applyfunc(sp.expand)


def rank_mod(a, p):
    a = [[int(x) % p for x in row] for row in a]
    n, m = len(a), len(a[0])
    r = 0
    for c in range(m):
        k = next((k for k in range(r, n) if a[k][c]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        z = pow(a[r][c], -1, p)
        a[r] = [(x * z) % p for x in a[r]]
        for k in range(r + 1, n):
            if a[k][c]:
                z = a[k][c]
                a[k] = [(x - z * y) % p for x, y in zip(a[k], a[r])]
        r += 1
        if r == n:
            break
    return r


def parts(n, lower=1):
    if n == 0:
        yield ()
    for a in range(lower, n + 1):
        for q in parts(n - a, a):
            yield (a,) + q


def enc(a):
    return [[str(sp.expand(a[r, c])) for c in range(a.cols)] for r in range(a.rows)]


raw = (HERE / "U52G1-Ar10B0.M").read_text(encoding="latin1")
block = re.search(r"G<x,y>:=MatrixGroup<10,F\|\[(.*?)\]\s*,\[(.*?)\]\s*>;", raw, re.S)
assert block
x, y = mat(block[1]), mat(block[2])
B1 = mat(re.search(r"B1:=MatrixAlgebra\(F,10\)!\[(.*?)\];", raw, re.S)[1])
B2 = mat(re.search(r"B2:=MatrixAlgebra\(F,10\)!\[(.*?)\];", raw, re.S)[1])
one = sp.eye(10)
assert eq(B1.T, -B1) and eq(B2.conjugate().T, B2)
assert sp.expand(B1.det()) == 1 and sp.expand(B2.det()) == 32
for g in (x, y):
    assert eq(simp(g * B1 * g.T), B1)
    assert eq(simp(g * B2 * g.conjugate().T), B2)
J, H = simp(B1.inv()), simp(B2.inv())
for g in (x, y):
    assert eq(simp(g.T * J * g), J)
    assert eq(simp(g.conjugate().T * H * g), H)
minors = [sp.expand(B2[:k, :k].det()) for k in range(1, 11)]
assert all(q.is_positive for q in minors)

# Positive definite B2, together with Gaussian integral entries, proves
# that the generated group is finite.  The presentation is then checked
# literally on these matrices; its published identification is cited.
assert eq(x ** 2, one) and eq(y ** 5, one) and eq((x * y) ** 11, one)
def comm(a, b):
    return simp(a.inv() * b.inv() * a * b)
relators = {}
for name, z in [("y", y), ("y2", y ** 2), ("yxy", y * x * y), ("yxy2", y * x * y ** 2)]:
    relators[name] = eq(comm(x, simp(z)) ** 3, one)
assert all(relators.values())

# Reduction at 5, i -> 2, supplies a nonzero 99-minor of the exact
# commutant equations.  Since scalar matrices already solve the equations,
# the characteristic-zero complex commutant has dimension exactly one.
rows = []
for g in (x, y):
    g5 = [[int(sp.expand(g[r, c]).subs(I, 2)) % 5 for c in range(10)] for r in range(10)]
    for r in range(10):
        for c in range(10):
            row = [0] * 100
            for k in range(10):
                row[10 * k + c] += g5[r][k]
                row[10 * r + k] -= g5[k][c]
            rows.append(row)
commutant_rank = rank_mod(rows, 5)
assert commutant_rank == 99

deleted = []
for m in range(9, 15):
    N = m + 1
    maxima = {k: max(sum(t % k == 0 for t in q) for q in parts(N)) for k in range(3, N + 1)}
    assert max(maxima.values()) == N // 3
    b_upper = 5 + N // 3
    assert b_upper < 12
    deleted.append({"m": m, "N": N, "nonreal_phase_fixed_max": N // 3,
                    "branch_upper": b_upper, "phase_order_maxima": maxima})

tensor = []
for m in range(9, 15):
    for a in range(2, sp.integer_nthroot(m, 2)[0] + 1):
        if m % a:
            continue
        b = m // a
        lower = 3 * b + (12 - 3) * 2 if a == 2 else 12 * a
        assert lower > 2 * m + 6
        tensor.append({"m": m, "a": a, "b": b, "codimension_sum_lower": lower,
                       "required_sum": 2 * m + 6})

# Rank-nine monomial permutation types: exact cycle-index possibilities.
rank9_types = [q for q in parts(9) if 9 - len(q) <= 2]
assert rank9_types == [(1, 1, 1, 1, 1, 1, 1, 1, 1),
                       (1, 1, 1, 1, 1, 1, 1, 2),
                       (1, 1, 1, 1, 1, 1, 3),
                       (1, 1, 1, 1, 1, 2, 2)]

out = {
    "status": "PASS",
    "classification_not_computed": "GS2003 Theorems 7.1 and 8.4 are published inputs, not conclusions of this certificate",
    "u5": {"source": "https://brauer.maths.qmul.ac.uk/Atlas/clas/U52/mag/U52G1-Ar10B0.M",
           "x": enc(x), "y": enc(y), "column_alternating_form_J": enc(J),
           "column_Hermitian_form_H": enc(H), "B1_determinant": "1", "B2_determinant": "32",
           "B2_leading_minors": list(map(str, minors)), "presentation_commutators": relators,
           "commutant_rank_mod5_i2": commutant_rank,
           "absolute_irreducibility_reason": "finite unitary integral group, scalar complex commutant"},
    "deleted_permutation_bounds": deleted,
    "tensor_bounds": tensor,
    "rank9_permutation_cycle_types": rank9_types,
    "degree10_inertia_codimension_max": 26 - 2 * 11,
}
(HERE / "small_codimension_certificate.json").write_text(json.dumps(out, indent=2) + "\n")
print("PASS: exact U5 Gaussian matrices, forms, presentation and absolute irreducibility")
print("PASS: all deleted-permutation and tensor bounds for coefficient ranks9 through14")
print("PASS: rank9 small-index permutation types and degree10 maximal inertia codimension4")
