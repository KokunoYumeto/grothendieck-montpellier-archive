"""Independent reconstruction from the displayed polar tensor, not its Pfaffian code.

Uses SymPy's polynomial-ring implementation and a fixed 81-by-81 minor.
This is a uniform polynomial calculation over F2[a,b,c], not sampling.
"""
from pathlib import Path
from datetime import datetime, timezone
import itertools, json, time
from sympy.polys.rings import ring
from sympy.polys.domains import GF

started = time.perf_counter()
R, a, b, c = ring('a,b,c', GF(2))
triples = list(itertools.combinations(range(1, 10), 3))
discard = {(4, 6, 7), (4, 7, 8), (5, 7, 8)}
kept = [t for t in triples if t not in discard]
row_index = {t: i for i, t in enumerate(kept)}
tensor = {}
for text, coefficient in [
    ('129 138 156 179 236 259 268 349 367 457', R.one),
    ('134 148 157', a), ('146', b), ('126 135', c),
]:
    for word in text.split():
        tensor[tuple(map(int, word))] = coefficient

matrix = [[R.zero for _ in range(81)] for _ in range(81)]
for target in range(1, 10):
    for source in range(1, 10):
        column = 9 * (target - 1) + source - 1
        for triple, coefficient in tensor.items():
            if source not in triple:
                continue
            replaced = tuple(sorted(target if j == source else j for j in triple))
            if len(set(replaced)) != 3 or replaced in discard:
                continue
            i = row_index[replaced]
            matrix[i][column] += coefficient

rows, columns, pivots = list(range(81)), list(range(81)), []
while columns:
    pivot = next(((i, j) for i in rows for j in columns
                  if matrix[i][j] == R.one), None)
    assert pivot is not None, 'No unit pivot: the claimed certificate did not reconstruct.'
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
assert len(pivots) == 81

# Compare the independently transcribed tensor with the author's complete
# Pfaffian computation, while never opening the author's output for writing.
author_path = Path(__file__).resolve().parents[2] / 'monodromy/outputs/ppav_supersingular_polar_uniform_lie.json'
author = json.loads(author_path.read_text())
from_author = {}
for triple, exponents in author['polar_terms']:
    value = R.zero
    for i, j, k in exponents:
        value += a**i * b**j * c**k
    from_author[tuple(x + 1 for x in triple)] = value
assert from_author == tensor
assert author['remaining_rows'] == [triples.index(t) for t in sorted(discard)] + [84]

result = {
    'status': 'PASS', 'actual_utc': datetime.now(timezone.utc).isoformat(),
    'runtime_seconds': time.perf_counter() - started,
    'ring': 'F2[a,b,c]', 'tensor_terms': len(tensor),
    'fixed_deleted_rows': sorted(discard), 'unit_pivot_count': len(pivots),
    'determinant': 1, 'independent_tensor_matches_full_pfaffian_output': True,
    'unit_pivots': pivots,
    'scope': 'Universal fixed-minor identity reconstructed from the displayed tensor using a different polynomial implementation; no geometric theorem is inferred from finite samples.'
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'unit_pivots'}, indent=2))
