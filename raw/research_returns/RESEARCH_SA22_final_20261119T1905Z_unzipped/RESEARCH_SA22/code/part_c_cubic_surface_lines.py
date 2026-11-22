#!/usr/bin/env python3
"""Exact 27-line incidence certificate for the Fermat cubic surface.

The field F4 has a primitive cube root w.  For characteristic !=3 the
same ranks follow from the union-of-matchings argument in the proof:
the only residual equation is (w^a-w^b)x=0 on an even cycle.  This script
certifies the finite incidence calculation, not that all-field argument.
"""
import itertools
import json
import time
from datetime import datetime, timezone
from pathlib import Path
import sympy as sp

start = time.perf_counter()
began = datetime.now(timezone.utc).isoformat()

def mul(a, b):
    z = 0
    while b:
        if b & 1:
            z ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return z

def inv(a):
    assert a
    return mul(a, a)

def rank(rows):
    a = [list(row) for row in rows]
    rr = 0
    for c in range(4):
        pivot = next((i for i in range(rr, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        f = inv(a[rr][c])
        a[rr] = [mul(v, f) for v in a[rr]]
        for i in range(len(a)):
            if i != rr and a[i][c]:
                f = a[i][c]
                a[i] = [x ^ mul(f, y) for x, y in zip(a[i], a[rr])]
        rr += 1
    return rr

partitions = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
roots = [1, 2, 3]
lines = []
for p, pairs in enumerate(partitions):
    for a, b in itertools.product(range(3), repeat=2):
        rows = []
        for (i, j), exponent in zip(pairs, (a, b)):
            row = [0] * 4
            row[i], row[j] = 1, roots[exponent]
            rows.append(row)
        assert rank(rows) == 2
        lines.append({"partition": p, "exponents": [a, b], "rows": rows})

G = sp.zeros(27)
counts = {"meeting_pairs": 0, "disjoint_pairs": 0}
for i in range(27):
    G[i, i] = -1
    for j in range(i):
        r = rank(lines[i]["rows"] + lines[j]["rows"])
        assert r in (3, 4), "duplicate line or unexpected rank"
        intersection = int(r == 3)
        G[i, j] = G[j, i] = intersection
        counts["meeting_pairs" if intersection else "disjoint_pairs"] += 1

pivots = list(G.rref()[1])
submatrix = G.extract(pivots, pivots)
assert len(pivots) == 7
assert submatrix.det() != 0
assert sum(counts.values()) == 351
assert all(sum(G[i, j] == 1 for j in range(27)) == 10 for i in range(27))

out = {
    "started_utc": began,
    "runtime_seconds": time.perf_counter() - start,
    "line_count": len(lines),
    "unordered_pairs_checked": 351,
    **counts,
    "each_line_meets": 10,
    "rational_gram_rank": len(pivots),
    "selected_indices_zero_based": pivots,
    "selected_lines": [{k: v for k, v in lines[i].items() if k != "rows"} for i in pivots],
    "selected_gram_matrix": [[int(v) for v in row] for row in submatrix.tolist()],
    "selected_gram_determinant": int(submatrix.det()),
    "full_gram_matrix": [[int(v) for v in row] for row in G.tolist()],
    "scope": "Exact F4 incidence and rational intersection-matrix certificate. All-characteristic !=3 validity is proved by even-cycle consistency separately.",
}
destination = Path(__file__).with_name("part_c_cubic_surface_lines_output.json")
destination.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({k: v for k, v in out.items() if k != "full_gram_matrix"}, indent=2))
