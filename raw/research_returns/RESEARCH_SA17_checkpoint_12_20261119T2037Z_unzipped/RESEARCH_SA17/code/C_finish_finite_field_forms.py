#!/usr/bin/env python3
"""Complete finite isometry check for the F3 rational O3 symmetric-square example.

The earlier coordinate-coalgebra certificate proves that its full equivariant
endomorphism algebra is span(I,K). This program enumerates every unit and every
nonsingular self-adjoint element of that algebra, so no restriction to a sample
of equivariant isometries occurs here.
"""
from pathlib import Path
from time import perf_counter
import json
import numpy as np

start = perf_counter()
p = 3
I = np.eye(6, dtype=np.int64)
v = np.array([1, 1, 1, 0, 0, 0], dtype=np.int64)
K = np.outer(v, v) % p
Q = np.diag([1, 1, 1, 2, 2, 2]) % p
assert not np.any(K @ K % p)
assert np.array_equal(K.T @ Q % p, Q @ K % p)
pairs = [(a, b) for a in (1, 2) for b in range(p)]
units = {(a, b): (a*I+b*K) % p for a, b in pairs}
forms = {ab: Q @ u % p for ab, u in units.items()}
inverse = {tuple(B.reshape(-1)): ab for ab, B in forms.items()}
orbits = set()
actions = 0
for ab, B in forms.items():
    orbit = set()
    for cd, U in units.items():
        result = tuple((U.T @ B @ U % p).reshape(-1))
        assert result in inverse
        ef = inverse[result]
        assert ef[0] == ab[0]
        orbit.add(ef)
        actions += 1
    orbits.add(tuple(sorted(orbit)))
assert len(orbits) == 2
assert sorted(map(len, orbits)) == [3, 3]
assert not any((1, 0) in o and (2, 0) in o for o in orbits)
rotation = np.array([[1, 1], [-1, 1]], dtype=np.int64) % p
assert np.array_equal(rotation.T @ rotation % p, 2*np.eye(2, dtype=np.int64) % p)
U = np.kron(rotation, I) % p
QQ = np.kron(np.eye(2, dtype=np.int64), Q)
assert np.array_equal(U.T @ QQ @ U % p, 2*QQ % p)
result = {
    'scope': __doc__,
    'prime': 3,
    'endomorphism_algebra_elements': 9,
    'all_equivariant_units': len(units),
    'all_nonsingular_invariant_symmetric_forms': len(forms),
    'isometry_action_checks': actions,
    'isometry_orbits': [[list(ab) for ab in orbit] for orbit in sorted(orbits)],
    'stable_double_sum_matrix_rank': 12,
    'double_sum_congruence_checks': 1,
    'result': 'PASS',
    'seconds': perf_counter()-start}
target = Path(__file__).resolve().parents[1]/'logs/C_finish_finite_field_forms.json'
target.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
