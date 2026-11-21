#!/usr/bin/env python3
"""Exact global V candidates from P21, F32 and commuting A,z3.

The two free seeds range through exact centralizers in S. This builds
actual permutations on all 1344 points and applies C25's necessary
mixed72 restrictions. It does not construct an associator.
"""
from pathlib import Path
import itertools
import json
import numpy as np

HERE = Path(__file__).resolve().parent
FIVE = HERE.parent / 'five_level_six'
CHAR = HERE.parent / 'characters'
raw = np.load(HERE / 'hurwitz_cubic216_four_13.npz')
A, B, C = raw['generators']
Z = A[B[A]]
Z = Z[Z]
assert np.array_equal(A[Z], Z[A])
blocks = np.load(HERE / 'hurwitz_cubic216_four_13_block0.npz')
block_map, qA = blocks['block_map'], blocks['generators'][0]
qZ = qA[blocks['generators'][1][qA]]
qZ = qZ[qZ]
base = np.load(FIVE / 'hurwitz_block_stabilizer.npz')['base']
trans = np.load(FIVE / 'hurwitz_block_correlations.npz')['transversals']
seeds = np.load(HERE / 'hurwitz_seed_centralizers.npz')
first = np.load(HERE / 'hurwitz_first_four_block_lifts.npz')
mixed = np.load(CHAR / 'records/hurwitz_mixed72_partial.npz')
assert seeds['centralizer_0'].shape == (18, 112)
assert seeds['centralizer_1'].shape == (8, 112)


def transport_orbit(seed):
    transports = {seed: np.arange(1344)}
    queue = [seed]
    for i in queue:
        for g, q in [(A, qA), (Z, qZ)]:
            j = int(q[i])
            if j not in transports:
                transports[j] = g[transports[i]]
                queue.append(j)
    return transports


orbit0 = transport_orbit(0)
orbit1 = transport_orbit(1)
assert set(orbit0) == {0, 9}
assert set(orbit1) == set(range(1, 7))


def put_seed(out, seed, local, transports):
    points = trans[seed][base]
    images = points[local]
    for g in transports.values():
        out[g[points]] = g[images]


outputs, saved = [], {'A': A, 'B': B, 'C': C, 'Z3': Z}
for a3 in [0, 1]:
    known = first[f'V_{a3}_0_{0 if a3 == 0 else 2}']
    candidates, labels, mixed_pass, mixed_labels = [], [], [], []
    for i0, i1 in itertools.product(range(18), range(8)):
        v = np.full(1344, -1, dtype=np.int16)
        v[first['subset']] = first['subset'][known]
        put_seed(v, 0, seeds['centralizer_0'][i0], orbit0)
        put_seed(v, 1, seeds['centralizer_1'][i1], orbit1)
        assert np.all(v >= 0) and len(set(map(int, v))) == 1344
        assert np.array_equal(block_map[v], block_map)
        assert np.array_equal(v[A], A[v]) and np.array_equal(v[Z], Z[v])
        candidates.append(v)
        labels.append([i0, i1])
        match_ids = []
        for component in [9, 10]:
            orbit = mixed[f'component_{component}_orbit']
            desired = mixed[f'component_{component}_unique_V']
            matches = [i for i, u in enumerate(desired) if np.array_equal(v[orbit], orbit[u])]
            if not matches:
                break
            assert len(matches) == 1
            match_ids.append(matches[0])
        if len(match_ids) == 2 and tuple(match_ids) in {(0, 0), (1, 3), (2, 1), (3, 2)}:
            mixed_pass.append(v)
            mixed_labels.append([i0, i1] + match_ids)
    assert len(candidates) == 144 and len({v.tobytes() for v in candidates}) == 144
    saved[f'all_V_{a3}'] = np.array(candidates)
    saved[f'all_labels_{a3}'] = np.array(labels)
    saved[f'mixed72_V_{a3}'] = np.array(mixed_pass)
    saved[f'mixed72_labels_{a3}'] = np.array(mixed_labels)
    outputs.append({
        'rho': 0, 'a2': 0, 'a3': a3,
        'global_A_Z3_commuting_candidates': 144,
        'passing_both_mixed72_restrictions_and_their_joint_graph': len(mixed_pass),
        'label_columns': ['block0_seed', 'block1_seed', 'component9_V', 'component10_V'],
        'passing_labels': mixed_labels,
    })
out = {
    'statement': 'D23.P22',
    'A_Z3_block_orbits': [[0, 9], [1, 2, 3, 4, 5, 6], [7, 8, 10], [11]],
    'seed_centralizer_orders': [18, 8],
    'cases': outputs,
    'scope': 'Necessary actual-source conjugators; no actual associator or mixed full-GT existence is claimed.',
    'result': 'PASS',
}
np.savez_compressed(HERE / 'hurwitz_global_conjugators.npz', **saved)
(HERE / 'hurwitz_global_conjugators.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps({**out, 'cases': [{k: v for k, v in row.items() if k != 'passing_labels'} for row in outputs]}, indent=2))
