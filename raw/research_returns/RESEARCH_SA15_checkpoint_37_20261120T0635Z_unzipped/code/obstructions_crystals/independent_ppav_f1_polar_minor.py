"""Reconstruct the fixed f=1 polar-action minor from the displayed tensor.

Independent polynomial implementation, exact over F2[a,b].
"""
from pathlib import Path
from datetime import datetime, timezone
from sympy.polys.rings import ring
from sympy.polys.domains import GF
import itertools, json, time

started = time.perf_counter()
R, a, b = ring('a,b', GF(2))
triples = list(itertools.combinations(range(1, 10), 3))
discard = {(1, 2, 3), (3, 4, 5), (3, 5, 6)}
kept = [t for t in triples if t not in discard]
index = {t: i for i, t in enumerate(kept)}
tensor = {}
for words, coefficient in [
    ('158 167 179 247 259 268 349 367 457', R.one),
    ('148 157', a), ('126 135', b),
]:
    for word in words.split():
        tensor[tuple(map(int, word))] = coefficient
matrix = [[R.zero for _ in range(81)] for _ in range(81)]
for target in range(1, 10):
    for source in range(1, 10):
        j = 9 * (target - 1) + source - 1
        for triple, value in tensor.items():
            if source not in triple:
                continue
            t = tuple(sorted(target if i == source else i for i in triple))
            if len(set(t)) == 3 and t not in discard:
                matrix[index[t]][j] += value

rows, columns, pivots = list(range(81)), list(range(81)), []
while columns:
    pivot = next(((i, j) for i in rows for j in columns if matrix[i][j] == R.one), None)
    if pivot is None:
        break
    i, j = pivot
    pivots.append({'triple': kept[i], 'column_Eij': [j // 9 + 1, j % 9 + 1]})
    rows.remove(i)
    columns.remove(j)
    for k in rows:
        multiplier = matrix[k][j]
        if multiplier:
            for ell in columns:
                matrix[k][ell] += multiplier * matrix[i][ell]
            matrix[k][j] = R.zero
assert len(pivots) == 77 and len(rows) == len(columns) == 4
determinant = R.zero
for permutation in itertools.permutations(range(4)):
    term = R.one
    for i, j in enumerate(permutation):
        term *= matrix[rows[i]][columns[j]]
    determinant += term
assert determinant == b**4

author_path = Path(__file__).resolve().parents[2] / 'monodromy/outputs/ppav_two_rank_one_polar_uniform_minor.json'
author = json.loads(author_path.read_text())
from_author = {}
for triple, exponents in author['polar_terms']:
    value = R.zero
    for i, j, k in exponents:
        assert k == 0
        value += a**i * b**j
    from_author[tuple(v + 1 for v in triple)] = value
assert tensor == from_author
assert author['deleted_original_triples'] == [list(t) for t in sorted(discard)]

result = {
    'status': 'PASS', 'actual_utc': datetime.now(timezone.utc).isoformat(),
    'runtime_seconds': time.perf_counter() - started, 'ring': 'F2[a,b]',
    'tensor_terms': len(tensor), 'fixed_deleted_rows': sorted(discard),
    'unit_pivot_count': len(pivots), 'remaining_size': 4,
    'residual_matrix': [[str(matrix[i][j]) for j in columns] for i in rows],
    'determinant': str(determinant), 'unit_pivots': pivots,
    'independent_tensor_matches_full_pfaffian_output': True,
    'scope': 'Universal fixed-minor identity, reconstructed from displayed tensor using SymPy ring arithmetic; no specialization and no inference beyond b!=0.'
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'unit_pivots'}, indent=2))
