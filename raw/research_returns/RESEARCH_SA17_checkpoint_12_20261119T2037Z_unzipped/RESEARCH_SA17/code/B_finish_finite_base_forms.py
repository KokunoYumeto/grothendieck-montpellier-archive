#!/usr/bin/env python3
"""Exhaustive Z/9 form certificate for the rational O3 symmetric square.

The paper proves the full equivariant endomorphism algebra is
E=(Z/9)[I,K], K=q trace and K^2=3K, using sign changes, permutations,
and a rotation over the faithfully flat algebra (Z/9)[z]/(z^2+1).
This program checks that rotation and then exhausts the entire algebra,
its idempotents, its units, and all invariant nonsingular symmetric forms.
It does not implement the general finite-base polynomial-equality algorithm.
"""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
from math import gcd
import json
import numpy as np

start = perf_counter()
mod = 9
I = np.eye(6, dtype=np.int64)
q = np.array([1, 1, 1, 0, 0, 0], dtype=np.int64)
K = np.outer(q, q) % mod
Q = np.diag([1, 1, 1, 2, 2, 2]).astype(np.int64)
assert np.array_equal(K @ K % mod, 3*K % mod)
assert not np.any(K @ K @ K % mod)
assert np.array_equal(K.T @ Q % mod, Q @ K % mod)

# Arithmetic in (Z/9)[z]/(z^2+1), with pairs a+bz.
def add(x, y):
    return ((x[0]+y[0]) % mod, (x[1]+y[1]) % mod)

def mul(x, y):
    return ((x[0]*y[0]-x[1]*y[1]) % mod,
            (x[0]*y[1]+x[1]*y[0]) % mod)

u, v = (0, 4), (0, 1)
assert add(mul(u, u), mul(v, v)) == (1, 0)
assert mul(u, v) == (5, 0)
assert gcd(5, mod) == 1

isotropic = np.array([1, 1, 4], dtype=np.int64)
partner = np.array([5, 4, 7], dtype=np.int64)
assert int(isotropic @ isotropic) % mod == 0
assert int(partner @ partner) % mod == 0
assert int(isotropic @ partner) % mod == 1

elements = {(a, b): (a*I+b*K) % mod for a in range(mod) for b in range(mod)}
assert len({tuple(x.reshape(-1)) for x in elements.values()}) == 81
idempotents = [ab for ab, x in elements.items()
               if np.array_equal(x @ x % mod, x)]
assert idempotents == [(0, 0), (1, 0)]

units = {}
for ab, x in elements.items():
    inverse = next((cd for cd, y in elements.items()
                    if np.array_equal(x @ y % mod, I)), None)
    assert (inverse is not None) == (gcd(ab[0], mod) == 1)
    if inverse is not None:
        units[ab] = x
assert len(units) == 54
forms = {ab: Q @ x % mod for ab, x in units.items()}
assert all(np.array_equal(B.T, B) for B in forms.values())
form_index = {tuple(B.reshape(-1)): ab for ab, B in forms.items()}
assert len(form_index) == 54
orbits = set()
actions = 0
for ab, B in forms.items():
    orbit = set()
    for U in units.values():
        image = tuple((U.T @ B @ U % mod).reshape(-1))
        assert image in form_index
        ef = form_index[image]
        assert ef[0] % 3 == ab[0] % 3
        orbit.add(ef)
        actions += 1
    orbits.add(tuple(sorted(orbit)))
assert actions == 2916
assert len(orbits) == 2
assert sorted(map(len, orbits)) == [27, 27]
assert not any((1, 0) in o and (2, 0) in o for o in orbits)

rotation = np.array([[1, 1], [-1, 1]], dtype=np.int64) % mod
assert np.array_equal(rotation.T @ rotation % mod, 2*np.eye(2, dtype=np.int64))
U = np.kron(rotation, I) % mod
QQ = np.kron(np.eye(2, dtype=np.int64), Q)
assert np.array_equal(U.T @ QQ @ U % mod, 2*QQ % mod)

result = {
    "scope": __doc__,
    "ring": "Z/9",
    "model": "GPT-6 Astra (OpenAI, ChatGPT Pro mode)",
    "run": "RESEARCH_SA17_FINISH-20261119",
    "agent": "dieudonne",
    "utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "endomorphism_algebra_elements": len(elements),
    "idempotents": idempotents,
    "all_equivariant_units": len(units),
    "all_nonsingular_invariant_symmetric_forms": len(forms),
    "isometry_action_comparisons": actions,
    "isometry_orbits": [[list(ab) for ab in orbit] for orbit in sorted(orbits)],
    "orbit_sizes": sorted(map(len, orbits)),
    "faithfully_flat_rotation_checks": 3,
    "hyperbolic_pair_checks": 3,
    "double_sum_congruence_dimension": 12,
    "double_sum_congruence_checks": 1,
    "seconds": perf_counter()-start,
    "result": "PASS"
}
target = Path(__file__).resolve().parents[1]/"logs/B_finish_finite_base_forms.json"
target.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps({key: value for key, value in result.items()
                  if key not in {"scope", "isometry_orbits"}}, indent=2))
