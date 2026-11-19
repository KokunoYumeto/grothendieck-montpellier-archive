"""Exact finite-field rank witness for the four-section obstruction matrix."""
from itertools import product
from pathlib import Path
import json
import random
import time

start = time.perf_counter()
base = Path(__file__).resolve().parents[1]
mon3 = [e for e in product(range(3), repeat=4) if sum(e) == 3]
mon4 = [e for e in product(range(3), repeat=4) if sum(e) == 4]
assert (len(mon3), len(mon4)) == (16, 19)
def rank_mod(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    nr, nc, rank = len(a), len(a[0]), 0
    pivots = []
    for j in range(nc):
        k = next((i for i in range(rank, nr) if a[i][j]), None)
        if k is None: continue
        a[rank], a[k] = a[k], a[rank]
        inv = pow(a[rank][j], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(nr):
            if i != rank and a[i][j]:
                v = a[i][j]
                a[i] = [(x - v*y) % p for x, y in zip(a[i], a[rank])]
        pivots.append(j)
        rank += 1
        if rank == nr: break
    return rank, pivots
rng = random.Random(190811)
records = []
for trial in range(12):
    coeff = [[[rng.randrange(-5,6) for k in range(3)] for j in range(4)] for i in range(4)]
    rows = []
    for i in range(4):
        for a in mon3:
            row = []
            for k in range(3):
                for b in mon4:
                    value = 0
                    for j in range(4):
                        aa = list(a); aa[j] += 1
                        if tuple(aa) == b: value += coeff[i][j][k]
                    row.append(value)
            rows.append(row)
    rank, pivots = rank_mod(rows, 101)
    records.append({"trial": trial, "coefficients_i_j_k": coeff, "rank_mod_101": rank,
                    "matrix_dimensions": [len(rows),len(rows[0])], "pivot_columns": pivots})
    if rank == 57: break
record = {"monomials_degree3": mon3, "monomials_degree4": mon4,
          "trials": records, "full_column_rank_found": rank == 57,
          "runtime_seconds": time.perf_counter()-start,
          "scope": "A finite-field rank-57 witness proves a nonzero rational polynomial minor; it does not by itself prove basepoint freeness or any cycle statement."}
path = base / "output" / "test_quartic_obstruction_rank.json"
path.write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
