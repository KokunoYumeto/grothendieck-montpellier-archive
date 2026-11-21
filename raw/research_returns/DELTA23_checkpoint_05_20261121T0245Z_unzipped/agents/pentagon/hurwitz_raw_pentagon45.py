#!/usr/bin/env python3
"""D23.P26: compare required rawH45 with its unique marked lift.

F36 proves the complete first-pair value is F_V for an actual normalized
element. H8 exhausts its 216-element mixed fiber before this raw test.
Passing is a necessary finite condition, not an actual GT lift assertion.
"""
from pathlib import Path
import json
import pickle
import numpy as np
from hurwitz_marked_raw_lift import MarkedRawLift

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIVE = HERE.parent / 'five_level_six'
raw = np.load(ROOT / 'records/hurwitz_product_fixed_cover.npz')
A, B, C = raw['generators']
Z = A[B[A]]; Z = Z[Z]
Zp = C[B[C]]; Zp = Zp[Zp]
D = A[B[C[A[B[A]]]]]
Di = np.argsort(D)
with (FIVE / 'hurwitz_full_mixed_groups_state.pkl').open('rb') as f:
    state34 = pickle.load(f)[0]
with (HERE / 'hurwitz_pair45_base_state.pkl').open('rb') as f:
    state45 = pickle.load(f)[0]
lift34 = MarkedRawLift(state34, [C[C], Z])
lift45 = MarkedRawLift(state45, [Z, Zp])
data = np.load(ROOT / 'records/hurwitz_pentagon45_fibers.npz')
values = np.load(HERE / 'hurwitz_raw_simultaneous_covariance.npz')
first = np.load(FIVE / 'hurwitz_first_pair_covariance.npz')
base_generators = np.load(HERE / 'hurwitz_cubic216_four_13.npz')['generators']
for p, q in zip([A, B, C], base_generators):
    assert np.array_equal(p // 6, q[np.arange(8064) // 6])
assert lift45.G.order() == 13374150672384
raw45_orders = json.loads((HERE / 'hurwitz_raw_pair45.json').read_text())
assert raw45_orders['base']['order'] == raw45_orders['raw']['order'] == 13374150672384
assert raw45_orders['base']['derived_order'] == raw45_orders['raw']['derived_order'] == 557256278016
deck = raw['deck']
deck_powers = [np.arange(8064)]
for k in range(1, 6):
    deck_powers.append(deck[deck_powers[-1]])
rows, labels, requireds, lifts, defects = [], [], [], [], []
for candidate in data['base_indices']:
    candidate = int(candidate)
    F = values[f'rawF_{candidate}']
    assert np.array_equal(F // 6, first[f'F_1_{candidate}'][np.arange(8064) // 6])
    for j, (Rbase, Hbase) in enumerate(zip(data[f'R_{candidate}'], data[f'H_{candidate}'])):
        R, H = lift34.lift(Rbase), lift45.lift(Hbase)
        required = D[F[R[Di[np.argsort(R)[np.argsort(F)]]]]]
        assert np.array_equal(required[::6] // 6, Hbase)
        factor2 = D[np.argsort(R)[Di]]
        factor3 = D[np.argsort(F)[Di]]
        pentagon = R[factor2[factor3[H[F]]]]
        assert np.array_equal(pentagon[::6] // 6, np.arange(1344))
        power = next((k for k, p in enumerate(deck_powers) if np.array_equal(pentagon, p)), None)
        yes = np.array_equal(required, H)
        assert yes == bool(np.array_equal(pentagon, np.arange(8064)))
        assert np.array_equal(pentagon[pentagon], np.arange(8064))
        rows.append({'candidate': candidate, 'R_fiber_index': j,
                     'centralizer_index': int(data[f'centralizer_indices_{candidate}'][j]),
                     'raw_pentagon': bool(yes), 'defect_global_deck_power': power,
                     'defect_distinct_phases': sorted(set(map(int, pentagon[::6] % 6)))})
        labels.append([candidate, j])
        requireds.append(required); lifts.append(H); defects.append(pentagon)
        print(rows[-1], flush=True)
np.savez_compressed(HERE / 'hurwitz_raw_pentagon45.npz', labels=labels,
                    required_H=requireds, marked_H=lifts, pentagon_defects=defects)
passing_candidates = sorted({r['candidate'] for r in rows if r['raw_pentagon']})
assert len(rows) == 36 and passing_candidates == [1, 19, 23, 27, 53, 61]
assert all(sum(r['raw_pentagon'] for r in rows if r['candidate'] == i) == 3 for i in passing_candidates)
# The identity associator is an actual equal-sign control on the raw marking.
identity = np.arange(8064)
assert np.array_equal(D[identity[identity[Di[identity[identity]]]]], identity)
out = {'statement': 'D23.P26', 'tested_base_pairs': len(rows),
       'raw_pentagon_pass_count': sum(r['raw_pentagon'] for r in rows), 'cases': rows,
       'passing_candidate_indices': passing_candidates,
       'identity_associator_control': True,
       'scope': 'All36 complete H8 base45-membership pairs. F36 forces the unique first value F_V for an actual normalized element. Exactly18 raw pairs survive; no actual GT realization is asserted.',
       'result': 'PASS'}
(HERE / 'hurwitz_raw_pentagon45.json').write_text(json.dumps(out, indent=2) + '\n')
print({k: v for k, v in out.items() if k != 'cases'})
