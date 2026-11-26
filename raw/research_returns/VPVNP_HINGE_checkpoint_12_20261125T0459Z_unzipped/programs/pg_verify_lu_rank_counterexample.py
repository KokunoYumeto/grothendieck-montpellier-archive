"""Independent integer verification of the27-qubit LU commutation-rank witness.

Uses the explicit mathematical input and the27 supplied weight matrices only.
No random search or NumPy routines from the discovery program are imported.
The orthogonal-complement basis uses descending pivot coordinates, different
from the discovery calculation; weighted forms are assembled entry by entry.
"""
from pathlib import Path
import json, hashlib

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / 'inputs/rt_lu_rank_probe.json'
WEIGHTS = ROOT / 'outputs/rt_lu_rank_probe.json'
data = json.loads(INPUT.read_text())
weights_data = json.loads(WEIGHTS.read_text())
G = [[int(c) for c in s] for s in data['basis']]
n = 27
assert len(G) == 6 and all(len(row) == n for row in G)
P = weights_data['witness']['matrices']
d = 6
assert len(P) == n and all(len(A) == d and all(len(row) == d for row in A) for A in P)


def xor_rows(a, b):
    return [x ^ y for x, y in zip(a, b)]


def rank(matrix):
    work = [row[:] for row in matrix]
    pivots = []
    for column in range(len(work[0])):
        found = next((j for j in range(len(pivots), len(work))
                      if work[j][column]), None)
        if found is None:
            continue
        k = len(pivots)
        work[k], work[found] = work[found], work[k]
        for j in range(len(work)):
            if j != k and work[j][column]:
                work[j] = xor_rows(work[j], work[k])
        pivots.append(column)
        if len(pivots) == len(work):
            break
    return len(pivots), pivots


support = []
for mask in range(64):
    x = [0] * n
    for i in range(6):
        if mask >> i & 1:
            x = xor_rows(x, G[i])
    quadratic = sum(x[i-1] * x[j-1]
                    for i, j in data['quadratic_edges_one_based']) % 2
    phase = sum(a*b for a,b in zip(data['phase_exponents_mod8'], x)) % 8
    assert phase == 4 * quadratic
    support.append(tuple(x))
assert len(set(support)) == 64

# Descending-pivot row reduction gives a different nullspace basis.
reduced = [row[:] for row in G]
pivots = []
for column in range(n-1, -1, -1):
    found = next((j for j in range(len(pivots), 6)
                  if reduced[j][column]), None)
    if found is None:
        continue
    k = len(pivots)
    reduced[k], reduced[found] = reduced[found], reduced[k]
    for j in range(6):
        if j != k and reduced[j][column]:
            reduced[j] = xor_rows(reduced[j], reduced[k])
    pivots.append(column)
assert len(pivots) == 6
H = []
for free in range(n):
    if free in pivots:
        continue
    row = [0] * n
    row[free] = 1
    for i, pivot in enumerate(pivots):
        row[pivot] = reduced[i][free]
    H.append(row)
assert len(H) == 21 and rank(H)[0] == 21
assert all(sum(a*b for a,b in zip(g,h)) % 2 == 0 for g in G for h in H)

Q = [[0] * n for _ in range(n)]
for i, j in data['quadratic_edges_one_based']:
    Q[i-1][j-1] = Q[j-1][i-1] = 1
X = G + [[0] * n for _ in H]
Z = [ [[0] * n for _ in G] + H,
      [[sum(g[k]*Q[k][v] for k in range(n)) % 2 for v in range(n)] for g in G] + H ]

results = []
for state in range(2):
    generators = [X[i] + Z[state][i] for i in range(n)]
    assert rank(generators)[0] == n
    C = []
    for v in range(n):
        C.append([[(X[i][v]*Z[state][j][v] + Z[state][i][v]*X[j][v]) % 2
                   for j in range(n)] for i in range(n)])
    assert all(sum(C[v][i][j] for v in range(n)) % 2 == 0
               for i in range(n) for j in range(n))
    M = [[0] * (d*n) for _ in range(d*n)]
    for a in range(d):
        for b in range(d):
            for i in range(n):
                for j in range(n):
                    M[a*n+i][b*n+j] = sum(P[v][a][b]*C[v][i][j] for v in range(n)) % 2
    r, columns = rank(M)
    results.append({'state': state, 'weighted_rank': r, 'pivot_columns': columns,
                    'matrix_sha256': hashlib.sha256(bytes(x for row in M for x in row)).hexdigest()})
assert [x['weighted_rank'] for x in results] == [36, 37]
weight_ranks = [rank(A)[0] for A in P]
assert max(weight_ranks) == 1
output = {
    'status': 'PASS independent exact LU rank counterexample',
    'input_sha256': hashlib.sha256(INPUT.read_bytes()).hexdigest(),
    'weight_artifact_sha256': hashlib.sha256(WEIGHTS.read_bytes()).hexdigest(),
    'support_size': 64, 'phase_equations_mod8_checked': 64,
    'stabilizer_dimension': 27, 'orthogonal_complement_dimension': 21,
    'weight_ranks': weight_ranks, 'results': results,
    'scope': 'Complex local diagonal unitaries relate the two stabilizer states; weighted binary commutation rank increases36to37. No LC-inequivalence assertion is needed.',
}
p = ROOT / 'outputs/pg_lu_rank_counterexample_verification.json'
t = p.with_suffix('.json.tmp')
t.write_text(json.dumps(output, indent=2) + '\n')
t.replace(p)
print(json.dumps({k:v for k,v in output.items() if k != 'results'}, indent=2))
print('Independent weighted ranks:', [x['weighted_rank'] for x in results])
