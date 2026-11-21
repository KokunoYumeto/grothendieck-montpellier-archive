"""Second modular determinant calculation on the selected square minors.

Uses NumPy int64 elimination with unnormalized pivot rows, independently
of the C++ rectangular normalized-row elimination that selected columns.
Also validates all recorded pencil parameters and evaluation point orders.
"""
from pathlib import Path
import json
import hashlib
from math import comb
import numpy as np


def determinant_mod(a, prime):
    a = np.array(a, dtype=np.int64, copy=True)
    determinant = 1
    for j in range(len(a)):
        where = np.flatnonzero(a[j:, j])
        if not len(where):
            return 0
        k = j+int(where[0])
        if k != j:
            a[[j, k]] = a[[k, j]]
            determinant = -determinant
        pivot = int(a[j, j])
        determinant = determinant*pivot % prime
        factors = a[j+1:, j]*pow(pivot, -1, prime) % prime
        a[j+1:, j+1:] = (a[j+1:, j+1:]-factors[:, None]*a[j, j+1:]) % prime
        a[j+1:, j] = 0
    return determinant % prime


root = Path(__file__).with_name('permanent_range')
results = []
for n in range(1, 17):
    stem = root/f'permanent_range_n{n}'
    manifest = json.loads(stem.with_suffix('.json').read_text())
    assert manifest['n'] == n and manifest['prime'] == 101
    assert manifest['rows'] == comb(n+3, 3)
    assert manifest['columns'] == 4*n*n
    assert manifest['attempt_zero_based'] == 0
    expected_points = [(a,b,c,n-a-b-c) for a in range(n,-1,-1)
                       for b in range(n-a,-1,-1)
                       for c in range(n-a-b,-1,-1)]
    assert list(map(tuple,manifest['evaluation_points'])) == expected_points
    state = 20261121+1009*n
    expected_pencil = []
    for _ in range(4*n*n):
        state = (1664525*state+1013904223) % 2**32
        expected_pencil.append((state >> 16) % 101)
    assert manifest['pencil_coefficients_flat_i_j_k'] == expected_pencil
    raw = stem.with_suffix('.u8').read_bytes()
    assert len(raw) == manifest['rows']*manifest['columns']
    matrix = np.frombuffer(raw, dtype=np.uint8).reshape(manifest['rows'],manifest['columns'])
    assert int(matrix.max()) < 101
    selected = manifest['selected_columns_zero_based']
    assert len(selected) == manifest['rows'] and selected == sorted(set(selected))
    value = determinant_mod(matrix[:, selected], 101)
    assert value == manifest['selected_minor_determinant_mod_prime'] != 0
    record = {'n': n, 'rank': manifest['rows'], 'minor_mod101': value,
              'matrix_sha256': hashlib.sha256(raw).hexdigest(),
              'independent_elimination_matches': True}
    results.append(record)
    print(json.dumps(record), flush=True)
(root/'minor_recheck_results.json').write_text(json.dumps(results, indent=2)+'\n')
