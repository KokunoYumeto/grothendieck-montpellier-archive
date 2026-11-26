"""Exact rank-one metric and systematic CSS graph-state calculations.

No search result is interpreted as a graph-resource conversion.  The input
is the already checked Ji--Chen--Wei--Ying LU pair and root's explicit
weighted-rank witness.  All calculations below are over the integers/F2.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
cfg_path = ROOT / "inputs/sh_lu_operational_reduction.json"
cfg = json.loads(cfg_path.read_text())
state_path = ROOT / cfg["state_input"]
weight_path = ROOT / cfg["weight_input"]
state = json.loads(state_path.read_text())
weight = json.loads(weight_path.read_text())
G = [[int(c) for c in row] for row in state["basis"]]
A, B = weight["A"], weight["B"]
n, k = len(G[0]), len(G)


def rank(rows):
    work = [row[:] for row in rows]
    r = 0
    for c in range(len(work[0])):
        hit = next((i for i in range(r, len(work)) if work[i][c]), None)
        if hit is None:
            continue
        work[r], work[hit] = work[hit], work[r]
        for i in range(len(work)):
            if i != r and work[i][c]:
                work[i] = [x ^ y for x, y in zip(work[i], work[r])]
        r += 1
        if r == len(work):
            break
    return r


def matvec(M, v):
    return tuple(sum(x*y for x, y in zip(row, v)) % 2 for row in M)


labels = []
P = []
for v in range(n):
    g = [row[v] for row in G]
    a, b = matvec(A, g), matvec(B, g)
    p = [[x*y for y in b] for x in a]
    labels.append((a, b) if any(a) and any(b) else None)
    P.append(p)
assert all(rank(p) <= 1 for p in P)
pair_checks = []
for v in range(n):
    for w in range(v+1, n):
        actual = rank([[x ^ y for x, y in zip(p, q)]
                       for p, q in zip(P[v], P[w])])
        if labels[v] is None or labels[w] is None:
            expected = int((labels[v] is None) != (labels[w] is None))
        else:
            expected = sum(x != y for x, y in zip(labels[v], labels[w]))
        assert actual == expected
        pair_checks.append([v+1, w+1, actual])

# The cut decomposition has coefficient 1/2 for each nonzero left or right
# factor label, treating a zero matrix as belonging to none of these cuts.
cut_sets = []
for part in range(2):
    distinct = sorted({lab[part] for lab in labels if lab is not None})
    for lab in distinct:
        cut_sets.append([v+1 for v in range(n)
                         if labels[v] is not None and labels[v][part] == lab])
for v, w, d in pair_checks:
    assert sum((v in C) != (w in C) for C in cut_sets) == 2*d

# RREF supplies physical pivot sites.  The row operations only change the
# coordinates of the same binary support subspace.
R = [row[:] for row in G]
pivots = []
for c in range(n):
    hit = next((i for i in range(len(pivots), k) if R[i][c]), None)
    if hit is None:
        continue
    r = len(pivots)
    R[r], R[hit] = R[hit], R[r]
    for i in range(k):
        if i != r and R[i][c]:
            R[i] = [x ^ y for x, y in zip(R[i], R[r])]
    pivots.append(c)
    if len(pivots) == k:
        break
assert len(pivots) == k
free = [v for v in range(n) if v not in pivots]
edges0 = [[pivots[i]+1, v+1] for i in range(k) for v in free if R[i][v]]


def support(mask):
    return [sum(((mask >> i) & 1)*R[i][v] for i in range(k)) % 2
            for v in range(n)]


def q(mask):
    x = support(mask)
    return sum(x[a-1]*x[b-1] for a, b in state["quadratic_edges_one_based"]) % 2


linear = [q(1 << i) for i in range(k)]
quad = [[i, j] for i in range(k) for j in range(i+1, k)
        if q((1 << i) | (1 << j)) ^ linear[i] ^ linear[j]]
for mask in range(1 << k):
    predicted = (sum(linear[i]*((mask >> i) & 1) for i in range(k))
                 + sum(((mask >> i) & 1)*((mask >> j) & 1) for i, j in quad)) % 2
    assert predicted == q(mask)
edges_extra = [[pivots[i]+1, pivots[j]+1] for i, j in quad]
out = {
    "status": "PASS exact metric and systematic graph-state reductions; no resource advantage claimed",
    "input_sha256": hashlib.sha256(cfg_path.read_bytes()).hexdigest(),
    "state_sha256": hashlib.sha256(state_path.read_bytes()).hexdigest(),
    "weight_sha256": hashlib.sha256(weight_path.read_bytes()).hexdigest(),
    "rank_one_metric": {
        "zero_sites_one_based": [v+1 for v, lab in enumerate(labels) if lab is None],
        "factor_labels": labels,
        "cut_coefficient": [1, 2],
        "cut_sets_one_based": cut_sets,
        "checked_pairs": len(pair_checks),
        "distances": pair_checks,
    },
    "systematic_css": {
        "pivots_one_based": [p+1 for p in pivots],
        "hadamard_sites_one_based": [v+1 for v in free],
        "systematic_rows": ["".join(map(str, row)) for row in R],
        "source_graph_edges_one_based": edges0,
        "target_extra_edges_one_based": edges_extra,
        "target_local_Z_sites_one_based": [pivots[i]+1 for i in range(k) if linear[i]],
        "source_edge_count": len(edges0),
        "target_extra_edge_count": len(edges_extra),
        "checked_quadratic_values": 1 << k,
    },
}
dest = ROOT / cfg["output"]
tmp = dest.with_suffix(".json.tmp")
tmp.write_text(json.dumps(out, separators=(",", ":")) + "\n")
tmp.replace(dest)
print(json.dumps({"status": out["status"], "zero_sites": out["rank_one_metric"]["zero_sites_one_based"],
                  "cuts": len(cut_sets), "pairs": len(pair_checks),
                  "pivots": out["systematic_css"]["pivots_one_based"],
                  "source_edges": len(edges0), "target_extra_edges": edges_extra,
                  "target_local_Z_sites": out["systematic_css"]["target_local_Z_sites_one_based"]}, indent=2))
