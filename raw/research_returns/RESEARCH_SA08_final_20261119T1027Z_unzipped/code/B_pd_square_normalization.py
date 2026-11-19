"""Exact normalized square functors on K(Z,r), for the C3 repair gate.

Dold--Kan basis elements are monotone surjections [n] -> [r], encoded
by their r cut positions. In a square functor the degenerate submodule
is a coordinate summand: a pair is nondegenerate exactly when its
two cut sets cover {1,...,n}. All matrix entries are integers.
"""
from itertools import combinations
from pathlib import Path
import json
import time
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]


def basis(r, n, kind):
    cuts = list(combinations(range(1, n + 1), r))
    cover = set(range(1, n + 1))
    pairs = []
    for a in cuts:
        for b in cuts:
            if kind == "gamma" and a > b:
                continue
            if kind == "exterior" and a >= b:
                continue
            if set(a) | set(b) == cover:
                pairs.append((a, b))
    return pairs


def face(cuts, n, i, r):
    values = [sum(c <= j for c in cuts) for j in range(n + 1) if j != i]
    if not values or values[0] != 0 or values[-1] != r:
        return None
    if any(values[j] - values[j - 1] not in (0, 1) for j in range(1, n)):
        return None
    out = tuple(j for j in range(1, n) if values[j] > values[j - 1])
    return out if len(out) == r else None


def boundary(r, n, kind):
    source = basis(r, n, kind)
    target = basis(r, n - 1, kind)
    rows = {value: i for i, value in enumerate(target)}
    result = sp.zeros(len(target), len(source))
    for col, (a, b) in enumerate(source):
        for i in range(n + 1):
            aa, bb = face(a, n, i, r), face(b, n, i, r)
            if aa is None or bb is None:
                continue
            coefficient = (-1) ** i
            if kind == "exterior":
                if aa == bb:
                    continue
                if aa > bb:
                    aa, bb = bb, aa
                    coefficient *= -1
            elif kind == "gamma":
                if a != b and aa == bb:
                    coefficient *= 2
                if aa > bb:
                    aa, bb = bb, aa
            row = rows.get((aa, bb))
            if row is not None:
                result[row, col] += coefficient
    return result


def smith(matrix):
    if not matrix.rows or not matrix.cols:
        return matrix, sp.eye(matrix.rows), sp.eye(matrix.cols)
    dm = DomainMatrix.from_Matrix(matrix).convert_to(ZZ)
    diagonal, left, right = smith_normal_decomp(dm)
    diagonal, left, right = (v.to_Matrix() for v in (diagonal, left, right))
    assert diagonal == left * matrix * right
    assert abs(int(left.det())) == 1
    assert abs(int(right.det())) == 1
    return diagonal, left, right


def homology(outgoing, incoming):
    assert outgoing.cols == incoming.rows
    assert outgoing * incoming == sp.zeros(outgoing.rows, incoming.cols)
    diagonal, _, change = smith(outgoing)
    rank = sum(diagonal[i, i] != 0 for i in range(min(diagonal.shape)))
    transformed = change.inv() * incoming
    assert transformed[:rank, :] == sp.zeros(rank, incoming.cols)
    kernel_incoming = transformed[rank:, :]
    assert all(value.q == 1 for value in kernel_incoming)
    quotient, _, _ = smith(kernel_incoming)
    entries = [abs(int(quotient[i, i])) for i in range(min(quotient.shape))]
    image_rank = sum(value != 0 for value in entries)
    return {
        "free_rank": outgoing.cols - rank - image_rank,
        "torsion": [value for value in entries if value > 1],
    }


def vertical(r, n):
    exterior = basis(r, n, "exterior")
    tensor = basis(r, n, "tensor")
    gamma = basis(r, n, "gamma")
    ti = {value: i for i, value in enumerate(tensor)}
    gi = {value: i for i, value in enumerate(gamma)}
    left = sp.zeros(len(tensor), len(exterior))
    right = sp.zeros(len(gamma), len(tensor))
    for col, (a, b) in enumerate(exterior):
        left[ti[(b, a)], col] += 1
        left[ti[(a, b)], col] -= 1
    for col, (a, b) in enumerate(tensor):
        pair = (a, b) if a <= b else (b, a)
        right[gi[pair], col] = 2 if a == b else 1
    return left, right


start = time.monotonic()
output = []
for r in range(1, 5):
    item = {"r": r, "functors": {}, "vertical_checks": []}
    matrices = {}
    for kind in ("gamma", "exterior", "tensor"):
        matrices[kind] = {
            n: boundary(r, n, kind) for n in range(r, 2 * r + 2)
        }
        rows = []
        for n in range(r, 2 * r + 1):
            outgoing = matrices[kind][n]
            incoming = matrices[kind][n + 1]
            group = homology(outgoing, incoming)
            rows.append({
                "n": n, "rank": outgoing.cols, "homology": group,
                "basis": basis(r, n, kind),
                "boundary": [list(map(int, outgoing.row(i))) for i in range(outgoing.rows)],
            })
        item["functors"][kind] = rows
    for n in range(r, 2 * r + 1):
        left, right = vertical(r, n)
        h2 = homology(left, sp.zeros(left.cols, 0))
        h3 = homology(right, left)
        h4 = homology(sp.zeros(0, right.rows), right)
        assert h2 == h3 == {"free_rank": 0, "torsion": []}
        expected = {"free_rank": 0, "torsion": [2] if n == r else []}
        assert h4 == expected
        if n > r:
            prev_left, prev_right = vertical(r, n - 1)
            assert matrices["tensor"][n] * left == prev_left * matrices["exterior"][n]
            assert matrices["gamma"][n] * right == prev_right * matrices["tensor"][n]
        item["vertical_checks"].append({"n": n, "H2": h2, "H3": h3, "H4": h4})
    output.append(item)

report = {
    "scope": "Exact finite normalized complexes for square functors on K(Z,r), 1<=r<=4.",
    "seconds": time.monotonic() - start,
    "all_chain_and_vertical_checks_passed": True,
    "results": output,
}
(ROOT / "logs/B_pd_square_normalization.json").write_text(json.dumps(report, indent=2) + "\n")
summary = []
for item in output:
    summary.append({
        "r": item["r"],
        "homology": {
            kind: {
                row["n"]: row["homology"] for row in rows
                if row["homology"]["free_rank"] or row["homology"]["torsion"]
            }
            for kind, rows in item["functors"].items()
        },
    })
print(json.dumps({"seconds": report["seconds"], "results": summary}, indent=2))
