#!/usr/bin/env python3
"""Check all P26 survivors against complete canonical linear raw covariance."""
from pathlib import Path
import json
import pickle
import numpy as np
from hurwitz_marked_raw_lift import MarkedRawLift

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIVE = HERE.parent / 'five_level_six'
raw = np.load(ROOT / 'records/hurwitz_product_fixed_cover.npz')
base = np.load(HERE / 'hurwitz_cubic216_four_13.npz')
A, B, C = raw['generators']
a, b, c = base['generators']
Z = A[B[A]]; Z = Z[Z]
I = np.arange(8064)
Vs = np.load(HERE / 'hurwitz_global_conjugators.npz')['mixed72_V_1']
linear = np.load(HERE / 'hurwitz_raw_linear_lifts.npz')['potentials_1']
first = np.load(HERE / 'hurwitz_raw_simultaneous_covariance.npz')
data = np.load(ROOT / 'records/hurwitz_pentagon45_fibers.npz')
p26 = json.loads((HERE / 'hurwitz_raw_pentagon45.json').read_text())
p26_values = np.load(HERE / 'hurwitz_raw_pentagon45.npz')
with (FIVE / 'hurwitz_full_mixed_groups_state.pkl').open('rb') as f:
    lift = MarkedRawLift(pickle.load(f)[0], [C[C], Z])
block_map = np.load(HERE / 'hurwitz_cubic216_four_13_block0.npz')['block_map']
orb = np.empty(12, dtype=int)
for j, points in enumerate([[0, 9], [1, 2, 3, 4, 5, 6], [7, 8, 10], [11]]):
    orb[points] = j
point_orbit = orb[block_map]


def edges(V, potential, q, raw_q, target):
    assert np.array_equal(target // 6, V[q[np.argsort(V)]][I // 6])
    rhs = (target[::6][V] % 6 - raw_q[::6] % 6
           - potential[q] + potential) % 6
    return [(int(point_orbit[i]), int(point_orbit[q[i]]), int(rhs[i]))
            for i in range(1344)]


def solve(relations):
    graph = [[] for _ in range(4)]
    for u, v, e in relations:
        graph[u].append((v, e))
        graph[v].append((u, -e % 6))
    value = np.full(4, -1, dtype=int)
    components = 0
    for start in range(4):
        if value[start] >= 0:
            continue
        value[start] = 0
        components += 1
        queue = [start]
        for u in queue:
            for v, e in graph[u]:
                new = (int(value[u]) + e) % 6
                if value[v] < 0:
                    value[v] = new
                    queue.append(v)
                elif value[v] != new:
                    return None, None
    assert all((value[v] - value[u] - e) % 6 == 0 for u, v, e in relations)
    return value, components


rows, saved = [], {}
for ordinal, item in enumerate(p26['cases']):
    if not item['raw_pentagon']:
        continue
    i, j = item['candidate'], item['R_fiber_index']
    V = Vs[i]
    F = first[f'rawF_{i}']
    R = lift.lift(data[f'R_{i}'][j])
    H = p26_values['marked_H'][ordinal]
    newB, newC = np.argsort(F)[B[F]], R[C[np.argsort(R)]]
    p = linear[i]
    relation = edges(V, p, b, B, newB) + edges(V, p, c, C, newC)
    shift, components = solve(relation)
    row = dict(item, raw_full_covariance=shift is not None,
               free_phase_components=components)
    if shift is not None:
        phase = (p + shift[point_orbit]) % 6
        rawV = 6 * V[I // 6] + (I % 6 + phase[I // 6]) % 6
        assert np.array_equal(rawV[A], A[rawV])
        assert np.array_equal(rawV[Z], Z[rawV])
        assert np.array_equal(rawV[B], newB[rawV])
        assert np.array_equal(rawV[C], newC[rawV])
        assert np.array_equal(rawV[raw['deck']], raw['deck'][rawV])
        for name, value in [('V', rawV), ('F', F), ('R', R), ('H', H)]:
            saved[f'{name}_{i}_{j}'] = value
    rows.append(row)
    print(row, flush=True)

np.savez_compressed(HERE / 'hurwitz_raw_survivor_covariance.npz', **saved)
assert len(rows) == 18 and all(r['raw_full_covariance'] and r['free_phase_components'] == 1 for r in rows)
out = {'statement': 'D23.P27', 'cases': rows, 'tested_pairs': len(rows),
       'passing_pairs': sum(r['raw_full_covariance'] for r in rows),
       'scope': 'Complete P26 eighteen-pair list, canonical linear raw lifts and full A/B/C/deck covariance. Does not imply actual GT realization.',
       'result': 'PASS'}
(HERE / 'hurwitz_raw_survivor_covariance.json').write_text(json.dumps(out, indent=2) + '\n')
print({k: v for k, v in out.items() if k != 'cases'})
