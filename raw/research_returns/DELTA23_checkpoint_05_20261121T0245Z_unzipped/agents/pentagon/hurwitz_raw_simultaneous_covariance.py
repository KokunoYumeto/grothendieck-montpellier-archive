#!/usr/bin/env python3
"""Unique raw first/mixed lifts and the remaining constant deck equations.

The B test is exhaustive for each V. The C test in this certificate uses
the recorded common-word R witness; failure for a witness alone is not
failure for its whole R fiber.
"""
from pathlib import Path
import json
import pickle
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIVE = HERE.parent / 'five_level_six'
raw = np.load(ROOT / 'records/hurwitz_product_fixed_cover.npz')
base = np.load(HERE / 'hurwitz_cubic216_four_13.npz')
A, B, C = raw['generators']
a, b, c = base['generators']
z = a[b[a]]; z = z[z]
Z = A[B[A]]; Z = Z[Z]
I = np.arange(8064)


class MarkedLift:
    def __init__(self, stored, raw_generators):
        args, state = stored
        self.G = PermutationGroup(args)
        self.G.__dict__.update(state)
        self.memo = {}
        for p, q in zip(self.G.generators, raw_generators):
            assert np.array_equal(q[::6] // 6, np.array(p.array_form))
            self.memo[p] = q
            self.memo[p**-1] = np.argsort(q)

    def product(self, factors):
        out = I.copy()
        for p in factors:
            out = out[self.strong(p)]
        return out

    def strong(self, p):
        if p.is_identity:
            return I
        if p in self.memo:
            return self.memo[p]
        if p in self.G._strong_gens_slp:
            out = self.product(self.G._strong_gens_slp[p])
        elif p**-1 in self.G._strong_gens_slp:
            out = np.argsort(self.strong(p**-1))
        else:
            out = self.product(self.G.generator_product(p, original=False))
        assert np.array_equal(out[::6] // 6, np.array(p.array_form))
        self.memo[p] = out
        self.memo[p**-1] = np.argsort(out)
        return out

    def lift(self, value):
        p = Permutation(value.tolist())
        assert self.G.contains(p)
        return self.strong(p)


with (FIVE / 'hurwitz_first_groups_state.pkl').open('rb') as f:
    first_state = pickle.load(f)[0]
with (FIVE / 'hurwitz_full_mixed_groups_state.pkl').open('rb') as f:
    mixed_state = pickle.load(f)[0]
first_lift = MarkedLift(first_state, [A[A], B[B]])
mixed_lift = MarkedLift(mixed_state, [C[C], Z])
Fvalues = np.load(FIVE / 'hurwitz_first_pair_covariance.npz')
witnesses = np.load(ROOT / 'records/hurwitz_solvable_fiber_filter.npz')
Vs = np.load(HERE / 'hurwitz_global_conjugators.npz')
linear = np.load(HERE / 'hurwitz_raw_linear_lifts.npz')
block_map = np.load(HERE / 'hurwitz_cubic216_four_13_block0.npz')['block_map']
orbits = [[0, 9], [1, 2, 3, 4, 5, 6], [7, 8, 10], [11]]
orb = np.empty(12, dtype=int)
for j, points in enumerate(orbits):
    orb[points] = j
point_orbit = orb[block_map]


def phase_edges(V, potential, q, raw_q, target):
    assert np.array_equal(target[::6] // 6, V[q[np.argsort(V)]])
    old_phase = raw_q[::6] % 6
    new_phase = target[::6] % 6
    rhs = (new_phase[V] - old_phase - potential[q] + potential) % 6
    return [(int(point_orbit[i]), int(point_orbit[q[i]]), int(rhs[i])) for i in range(1344)]


def solve(edges):
    values = np.full(4, -1, dtype=int)
    components = 0
    for start in range(4):
        if values[start] >= 0:
            continue
        values[start] = 0
        components += 1
        queue = [start]
        for i in queue:
            for u, v, e in edges:
                if u != i:
                    continue
                w = (int(values[i]) + e) % 6
                if values[v] < 0:
                    values[v] = w
                    queue.append(v)
                elif values[v] != w:
                    return None, None
    return values, components


rows, saved = [], {}
for row, candidate in enumerate(witnesses['base_indices']):
    candidate = int(candidate)
    V = Vs['mixed72_V_1'][candidate]
    F = Fvalues[f'F_1_{candidate}']
    R = witnesses['R_witnesses'][row]
    rawF, rawR = first_lift.lift(F), mixed_lift.lift(R)
    newB = np.argsort(rawF)[B[rawF]]
    newC = rawR[C[np.argsort(rawR)]]
    potential = linear['potentials_1'][candidate]
    bedges = phase_edges(V, potential, b, B, newB)
    bshift, bcomponents = solve(bedges)
    both, components = solve(bedges + phase_edges(V, potential, c, C, newC))
    item = {'candidate': candidate, 'raw_B_pass': bshift is not None,
            'raw_B_free_phase_components': bcomponents,
            'recorded_R_raw_BC_pass': both is not None,
            'raw_BC_free_phase_components': components}
    if both is not None:
        t = (potential + both[point_orbit]) % 6
        rawV = 6 * V[I // 6] + (I % 6 + t[I // 6]) % 6
        assert np.array_equal(rawV[A], A[rawV])
        assert np.array_equal(rawV[Z], Z[rawV])
        assert np.array_equal(rawV[B], newB[rawV])
        assert np.array_equal(rawV[C], newC[rawV])
        saved[f'rawV_{candidate}'] = rawV
        saved[f'rawF_{candidate}'] = rawF
        saved[f'rawR_{candidate}'] = rawR
    rows.append(item)
    print(item, flush=True)

out = {'statement': 'D23.P24 probe', 'cases': rows,
       'raw_B_pass_count': sum(r['raw_B_pass'] for r in rows),
       'recorded_R_raw_BC_pass_count': sum(r['recorded_R_raw_BC_pass'] for r in rows),
       'scope': 'All36 normalized mixed V, exhaustive rawB phases, one checked same-word R witness per V for rawC.',
       'result': 'PASS'}
np.savez_compressed(HERE / 'hurwitz_raw_simultaneous_covariance.npz', **saved)
(HERE / 'hurwitz_raw_simultaneous_covariance.json').write_text(json.dumps(out, indent=2) + '\n')
print({k: v for k, v in out.items() if k != 'cases'})
