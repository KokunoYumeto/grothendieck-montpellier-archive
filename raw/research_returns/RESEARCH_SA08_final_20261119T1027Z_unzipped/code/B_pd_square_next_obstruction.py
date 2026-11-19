"""Compute the next possible repair obstruction from the saved square complex.

This calculates a group, not the actual obstruction class of any target.
"""
from pathlib import Path
import json
import time
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT = Path(__file__).resolve().parents[1]
start = time.monotonic()
saved = json.loads((ROOT / "logs/B_pd_square_normalization.json").read_text())
item = next(row for row in saved["results"] if row["r"] == 2)
rows = item["functors"]["gamma"]
rank = {row["n"]: row["rank"] for row in rows}
differential = {}
for row in rows:
    n = row["n"]
    differential[n] = sp.Matrix(
        rank.get(n - 1, 0), rank[n], lambda i, j: row["boundary"][i][j]
    )


def components(total):
    return [(a, total - a) for a in rank if total - a in rank]


def total_rank(total):
    return sum(rank[a] * rank[b] for a, b in components(total))


def tensor_boundary(total):
    source = components(total)
    target = components(total - 1)
    offsets = {}
    at = 0
    for a, b in target:
        offsets[(a, b)] = at
        at += rank[a] * rank[b]
    result = sp.zeros(total_rank(total - 1), total_rank(total))
    column = 0
    for a, b in source:
        width = rank[a] * rank[b]
        if (a - 1, b) in offsets:
            block = sp.kronecker_product(differential[a], sp.eye(rank[b]))
            row = offsets[(a - 1, b)]
            result[row:row + block.rows, column:column + width] += block
        if (a, b - 1) in offsets:
            block = (-1)**a * sp.kronecker_product(sp.eye(rank[a]), differential[b])
            row = offsets[(a, b - 1)]
            result[row:row + block.rows, column:column + width] += block
        column += width
    return result


def smith(matrix):
    if not matrix.rows or not matrix.cols:
        return matrix, sp.eye(matrix.rows), sp.eye(matrix.cols)
    d, s, t = smith_normal_decomp(DomainMatrix.from_Matrix(matrix).convert_to(ZZ))
    d, s, t = d.to_Matrix(), s.to_Matrix(), t.to_Matrix()
    assert d == s * matrix * t
    assert abs(int(s.det())) == abs(int(t.det())) == 1
    return d, s, t


ds = {n: tensor_boundary(n) for n in range(4, 10)}
for n in range(5, 10):
    assert ds[n - 1] * ds[n] == sp.zeros(ds[n - 1].rows, ds[n].cols)
# Hom(P tensor P, Z[7]) has cocycles killed by d8^t and coboundaries d7^t.
outgoing, incoming = ds[8].T, ds[7].T
diag, out_left, change = smith(outgoing)
out_rank = sum(diag[i, i] != 0 for i in range(min(diag.shape)))
inc = change.inv() * incoming
assert inc[:out_rank, :] == sp.zeros(out_rank, incoming.cols)
quotient, quotient_left, quotient_right = smith(inc[out_rank:, :])
values = [abs(int(quotient[i, i])) for i in range(min(quotient.shape))]
group = {
    "free_rank": outgoing.cols - out_rank - sum(v != 0 for v in values),
    "torsion": [v for v in values if v > 1],
}
assert group == {"free_rank": 0, "torsion": [2, 2]}
report = {
    "statement": "Hom_D(Z)(N Gamma^2 K(Z,2) tensor N Gamma^2 K(Z,2), Z[7])",
    "group": group,
    "scope": "Possible second-stage relation obstruction group; no nonzero actual class asserted.",
    "tensor_ranks": {n: total_rank(n) for n in range(4, 9)},
    "boundaries": {
        n: [list(map(int, ds[n].row(i))) for i in range(ds[n].rows)]
        for n in range(4, 10)
    },
    "smith_certificate": {
        "outgoing": outgoing.tolist(),
        "outgoing_diagonal": diag.tolist(),
        "outgoing_left": out_left.tolist(),
        "outgoing_right": change.tolist(),
        "kernel_incoming": inc[out_rank:, :].tolist(),
        "quotient_diagonal": quotient.tolist(),
        "quotient_left": quotient_left.tolist(),
        "quotient_right": quotient_right.tolist(),
        "identities_verified": "D=S*M*T and det(S),det(T)=+-1 in both decompositions",
    },
    "seconds": time.monotonic() - start,
}
(ROOT / "logs/B_pd_square_next_obstruction.json").write_text(json.dumps(report, indent=2, default=int) + "\n")
print(json.dumps({k: v for k, v in report.items() if k not in ("boundaries", "smith_certificate")}, indent=2))
