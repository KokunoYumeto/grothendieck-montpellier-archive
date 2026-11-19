#!/usr/bin/env python3
"""Exact finite certificate for A5.002 (the 121/036--037 recursion).

No geometric recognition routine is used.  We give all simplices, check the
circle maps, and compute rational homology by exact integer boundary matrices.
Run from any directory; outputs go to the adjacent ../logs directory.
"""
from itertools import combinations
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "logs"
OUT.mkdir(exist_ok=True)
g = [0, 1, 2, 1, 2]
A = [f"a{i}" for i in range(5)]
B = [f"b{i}" for i in range(3)]
triangles = []
for i in range(5):
    j = (i + 1) % 5
    assert g[i] != g[j]
    triangles += [tuple(sorted((B[g[i]], A[i], A[j]))),
                  tuple(sorted((B[g[i]], B[g[j]], A[j])))]
assert len(set(triangles)) == 10

def closure(maximal):
    return {tuple(sorted(s)) for t in maximal
            for k in range(1, len(t) + 1) for s in combinations(t, k)}

def betti(complex_):
    by_dim = [[s for s in sorted(complex_) if len(s) == d + 1]
              for d in range(max(map(len, complex_)))]
    rank = [0]
    for d in range(1, len(by_dim)):
        rows = {s: i for i, s in enumerate(by_dim[d - 1])}
        matrix = sp.zeros(len(rows), len(by_dim[d]))
        for j, simplex in enumerate(by_dim[d]):
            for k in range(d + 1):
                face = simplex[:k] + simplex[k + 1:]
                matrix[rows[face], j] = (-1) ** k
        rank.append(int(matrix.rank()))
    rank.append(0)
    return [len(by_dim[d]) - rank[d] - rank[d + 1]
            for d in range(len(by_dim))]

K = closure(triangles)
bottom_edges = [tuple(sorted((B[i], B[(i+1) % 3]))) for i in range(3)]
top_edges = [tuple(sorted((A[i], A[(i+1) % 5]))) for i in range(5)]
assert betti(closure(bottom_edges)) == [1, 1]
assert betti(closure(top_edges)) == [1, 1]
assert betti(K) == [1, 1, 0]

records = []
for edge in bottom_edges:
    pages = [t for t in triangles if set(edge) <= set(t)]
    link_edge = sorted(set(t) - set(edge) for t in pages)
    assert all(len(s) == 1 for s in link_edge)
    # Stellar subdivision of this edge, followed by the actual vertex link.
    midpoint = "p"
    subdivided = []
    for t in triangles:
        if set(edge) <= set(t):
            other = (set(t) - set(edge)).pop()
            subdivided += [tuple(sorted((edge[0], midpoint, other))),
                           tuple(sorted((edge[1], midpoint, other)))]
        else:
            subdivided.append(t)
    subdivided_complex = closure(subdivided)
    link_midpoint = {tuple(v for v in s if v != midpoint)
                     for s in subdivided_complex if midpoint in s and len(s) > 1}
    b = betti(link_midpoint)
    assert b == [1, len(pages) - 1]
    records.append({"bottom_edge": edge, "number_of_pages": len(pages),
                    "edge_link_vertices": [sorted(s) for s in link_edge],
                    "midpoint_link_simplices": sorted(link_midpoint),
                    "midpoint_link_betti": b,
                    "local_H2_rank": b[1]})

certificate = {"id": "A5.002", "vertex_map_A_to_B": g,
               "top_edges": top_edges, "bottom_edges": bottom_edges,
               "mapping_cylinder_maximal_simplices": sorted(triangles),
               "f_vector": [sum(len(s) == n for s in K) for n in (1, 2, 3)],
               "mapping_cylinder_betti": betti(K), "bottom_local_types": records}
(OUT / "A5_mapping_cylinder.json").write_text(json.dumps(certificate, indent=2)+"\n")
lines = ["A5.002 exact mapping-cylinder certificate",
         "g(a_0),...,g(a_4) = " + str(g),
         "f-vector = " + str(certificate["f_vector"]),
         "Betti(X;Q) = " + str(betti(K))]
for row in records:
    lines.append("edge %s: pages=%d; Betti(link(midpoint))=%s; rank H_2(X,X-p)=%d"
                 % ("-".join(row["bottom_edge"]), row["number_of_pages"],
                    row["midpoint_link_betti"], row["local_H2_rank"]))
lines.append("PASS: the one-piece bottom circle has nonconstant local H_2 rank (0,2,0).")
text = "\n".join(lines)+"\n"
(OUT / "A5_mapping_cylinder.txt").write_text(text)
print(text, end="")
