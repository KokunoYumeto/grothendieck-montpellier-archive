#!/usr/bin/env python3
"""Canonical linear lifts to the product-fixed8064 Hurwitz cover.

Each112-point projective block has three exact linear framings, with224
nonzero singular vectors in each. A linear deck-equivariant lift is fixed
up to one constant C6 deck shift per block. Test exact A,z3 commutation.
"""
from pathlib import Path
import itertools
import json
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
raw = np.load(ROOT / 'records/hurwitz_product_fixed_cover.npz')
base = np.load(HERE / 'hurwitz_cubic216_four_13.npz')
block_map = np.load(HERE / 'hurwitz_cubic216_four_13_block0.npz')['block_map']
tuples = raw['group_elements'][raw['tuples']]
I2 = np.eye(2, dtype=int)
deck = raw['deck']


def rref(a):
    a = np.array(a, dtype=int, copy=True) % 3
    row, pivots = 0, []
    for col in range(a.shape[1]):
        nz = np.flatnonzero(a[row:, col])
        if not len(nz):
            continue
        j = row + int(nz[0])
        a[[row, j]] = a[[j, row]]
        a[row] = a[row] * int(a[row, col]) % 3
        for k in range(a.shape[0]):
            if k != row and a[k, col]:
                a[k] = (a[k] - a[k, col] * a[row]) % 3
        pivots.append(col)
        row += 1
        if row == a.shape[0]:
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def inverse(a):
    n = len(a)
    v, piv = rref(np.c_[a, np.eye(n, dtype=int)])
    assert piv[:n] == list(range(n))
    return v[:, n:]


def coordinates(t):
    fixed = [inverse(I2 - g[2:].reshape(2, 2)) @ g[:2] % 3 for g in t]
    return np.concatenate([(v - fixed[3]) % 3 for v in fixed[:3]])


frames = []
for j in range(12):
    points = np.flatnonzero(block_map == j)
    rows = np.array([6 * int(v) + e for v in points for e in range(6)])
    partitions = {}
    for row in rows:
        key = tuple(map(int, tuples[row, :, 2:].ravel()))
        partitions.setdefault(key, []).append(int(row))
    assert len(partitions) == 3 and {len(v) for v in partitions.values()} == {224}
    key = min(partitions)
    chosen = np.array(partitions[key])
    coords = np.array([coordinates(tuples[row]) for row in chosen])
    assert len({tuple(v) for v in coords}) == 224 and rank(coords) == 6
    cindex = {tuple(v): int(row) for v, row in zip(coords, chosen)}
    assert all(tuple(-v % 3) in cindex for v in coords)
    bypoint = {int(p): [int(i) for i in np.flatnonzero(chosen // 6 == p)] for p in points}
    assert {len(v) for v in bypoint.values()} == {2}
    ids = []
    for i, v in enumerate(coords):
        if rank(coords[ids + [i]]) > len(ids):
            ids.append(i)
        if len(ids) == 6:
            break
    assert len(ids) == 6
    # The deck cube preserves this framing and negates its difference vectors.
    d3 = deck[deck[deck[chosen]]]
    assert np.array_equal(np.array([cindex[tuple(-v % 3)] for v in coords]), d3)
    frames.append((points, chosen, coords, cindex, bypoint, ids, inverse(coords[ids].T)))

cache = {}


def canonical_block_lift(V, j):
    points, chosen, coords, cindex, bypoint, ids, inv_basis = frames[j]
    key = (j, V[points].tobytes())
    if key in cache:
        return cache[key]
    images = np.array([coords[bypoint[int(V[int(chosen[i] // 6)])][0]] for i in ids]).T
    good = []
    for signs in itertools.product([1, 2], repeat=5):
        M = images @ np.diag((1,) + signs) @ inv_basis % 3
        if rank(M) != 6:
            continue
        moved = coords @ M.T % 3
        if not all(tuple(v) in cindex for v in moved):
            continue
        targets = np.array([cindex[tuple(v)] for v in moved])
        if not np.array_equal(targets // 6, V[chosen // 6]):
            continue
        good.append((M, targets))
    assert len(good) == 1
    M, targets = good[0]
    raw_map = {}
    src, dst = chosen.copy(), targets.copy()
    for e in range(3):
        for x, y in zip(src, dst):
            raw_map[int(x)] = int(y)
        src, dst = deck[src], deck[dst]
    assert len(raw_map) == 672
    phase = np.array([raw_map[6 * int(p)] % 6 for p in points])
    for p, e in zip(points, phase):
        for k in range(6):
            assert raw_map[6 * int(p) + k] == 6 * int(V[p]) + (k + int(e)) % 6
    cache[key] = (phase, M)
    return phase, M


A, B, C = raw['generators']
Z = A[B[A]]
Z = Z[Z]
a, b, c = base['generators']
z = a[b[a]]
z = z[z]
operators = [(a, A[::6] % 6), (z, Z[::6] % 6)]
candidates = np.load(HERE / 'hurwitz_global_conjugators.npz')
saved, outputs = {}, []
for bit in [0, 1]:
    passing, potentials, shifts, failures = [], [], [], []
    for idx, V in enumerate(candidates[f'mixed72_V_{bit}']):
        phase = np.zeros(1344, dtype=int)
        for j in range(12):
            phase[frames[j][0]] = canonical_block_lift(V, j)[0]
        edges, valid = [], True
        for q, e in operators:
            for j in range(12):
                points = frames[j][0]
                k = int(block_map[q[points[0]]])
                assert np.all(block_map[q[points]] == k)
                rhs = (e[V[points]] - e[points] - phase[q[points]] + phase[points]) % 6
                if len(set(map(int, rhs))) != 1:
                    valid = False
                    failures.append({'candidate': idx, 'reason': 'nonconstant block discrepancy', 'block': j})
                    break
                edges.append((j, k, int(rhs[0])))
            if not valid:
                break
        shift = np.full(12, -1, dtype=int)
        if valid:
            for start in range(12):
                if shift[start] >= 0:
                    continue
                shift[start] = 0
                queue = [start]
                for i in queue:
                    for j, k, e in edges:
                        if j != i:
                            continue
                        value = (int(shift[i]) + e) % 6
                        if shift[k] < 0:
                            shift[k] = value
                            queue.append(k)
                        elif shift[k] != value:
                            valid = False
                            failures.append({'candidate': idx, 'reason': 'block-cycle obstruction', 'edge': [j, k, e]})
                            break
                    if not valid:
                        break
                if not valid:
                    break
        if valid:
            potential = (phase + shift[block_map]) % 6
            rawV = 6 * V[np.arange(8064) // 6] + (np.arange(8064) % 6 + potential[np.arange(8064) // 6]) % 6
            assert np.array_equal(rawV[A], A[rawV]) and np.array_equal(rawV[Z], Z[rawV])
            assert np.array_equal(rawV[deck], deck[rawV])
            passing.append(idx)
            potentials.append(potential)
            shifts.append(shift)
    saved[f'passing_{bit}'] = np.array(passing)
    saved[f'potentials_{bit}'] = np.array(potentials)
    saved[f'block_shifts_{bit}'] = np.array(shifts)
    outputs.append({'a3': bit, 'input_count': 72, 'canonical_linear_lift_count': len(passing),
                    'passing_indices': passing, 'failures': failures})
    print({'a3': bit, 'passing': len(passing), 'indices': passing}, flush=True)

np.savez_compressed(HERE / 'hurwitz_raw_linear_lifts.npz', **saved)
out = {'statement': 'D23.P23 probe', 'linear_framings_per_projective_block': 3,
       'nonzero_vectors_per_framing': 224, 'canonical_projective_lifts_cached': len(cache),
       'cases': outputs, 'scope': 'Exact linear/deck/commutingA,z3 lift test, not full raw GT covariance.', 'result': 'PASS'}
(HERE / 'hurwitz_raw_linear_lifts.json').write_text(json.dumps(out, indent=2) + '\n')
print('PASS')
