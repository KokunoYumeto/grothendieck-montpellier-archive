#!/usr/bin/env python3
"""Independently rebuild the 5-by-2 Koszul minors and the full graph cover.

Only certificate row/column indices and claimed determinants are read.
No rank search or matrix-construction routine of the author is imported.
"""
from itertools import combinations, permutations
from pathlib import Path
import json
import sys

def determinant(matrix):
    a = [list(row) for row in matrix]
    n, previous, sign = len(a), 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        d = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * d - a[i][k] * a[k][j]
                assert num % previous == 0
                a[i][j] = num // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = d
    return sign * a[-1][-1]

def matrix_entry(edges, sign, row, col):
    output_pair, output_variable = list(combinations(range(5), 2))[row // 10], row % 10
    input_first, input_variable = col // 10, col % 10
    if input_first not in output_pair:
        return 0
    h = next(x for x in output_pair if x != input_first)
    i, j = edges[h]
    # Ordered quadratic coefficients on x_(i,0),x_(i,1),x_(j,0),x_(j,1).
    q = {(2*i,2*j+1):1, (2*j+1,2*i):1,
         (2*i+1,2*j):sign, (2*j,2*i+1):sign}
    wedge_sign = -1 if h > input_first else 1
    return wedge_sign * q.get((output_variable, input_variable), 0)

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "root" / "five_by_two_extra.json"
    data = json.loads(path.read_text())
    all_edges = list(combinations(range(5), 2))
    labeled = {tuple(es) for es in combinations(all_edges, 5)
               if set(v for e in es for v in e) == set(range(5))}
    assert len(labeled) == 222
    covered = set()
    summary = []
    for rec in data:
        edges = [tuple(e) for e in rec["edges"]]
        assert [all_edges[i] for i in rec["subset"]] == edges
        orbit = {tuple(sorted(tuple(sorted((p[i],p[j]))) for i,j in edges))
                 for p in permutations(range(5))}
        assert len(orbit) == rec["orbit_size"]
        assert not (covered & orbit)
        covered |= orbit
        values = {}
        for family, sign in (("det", -1), ("per", 1)):
            cert = rec["families"][family]["threshold_certificate"]
            assert cert["p"] == 1 and cert["cost"] == 4
            rows, cols = cert["rows"], cert["cols"]
            assert len(rows) == len(cols) == cert["size"] == 41
            assert len(set(rows)) == len(set(cols)) == 41
            mat = [[matrix_entry(edges, sign, r, c) for c in cols] for r in rows]
            value = determinant(mat)
            assert value == cert["determinant_Z"]
            assert abs(value) in ((1,) if family == "per" else (1,4))
            values[family] = value
        summary.append({"edges": edges, "orbit_size": len(orbit), "minor_order": 41, "determinants": values})
    assert covered == labeled and len(data) == 5
    print(json.dumps({"status":"PASS", "all_labeled_graphs":len(labeled), "orbits":summary}, indent=2))

if __name__ == "__main__":
    main()
