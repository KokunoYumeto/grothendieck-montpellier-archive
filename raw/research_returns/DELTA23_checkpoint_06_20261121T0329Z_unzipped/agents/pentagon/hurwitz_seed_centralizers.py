#!/usr/bin/env python3
"""D23.P22: exact centralizers of the two remaining local seeds in S.

The proof identifies the full stabilizers in <A,z3> with the two displayed
commuting-generator pairs. This computes their centralizers in the actual
simple permutation group S, retaining every element for the global builder.
"""
from pathlib import Path
import json
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parent
FIVE = HERE.parent / 'five_level_six'
raw = np.load(HERE / 'hurwitz_cubic216_four_13.npz')
A, B, C = raw['generators']
Z = A[B[A]]
Z = Z[Z]
assert np.array_equal(A[Z], Z[A])
stab = np.load(FIVE / 'hurwitz_block_stabilizer.npz')
base = stab['base']
loc = {int(v): i for i, v in enumerate(base)}
trans = np.load(FIVE / 'hurwitz_block_correlations.npz')['transversals']
H = PermutationGroup([Permutation(p.tolist()) for p in stab['stabilizer']])
S = H.derived_subgroup()
assert H.order() == 6531840 and S.order() == 3265920


def local(p, block):
    normalized = np.argsort(trans[block])[p[trans[block][base]]]
    assert set(map(int, normalized)) == set(map(int, base))
    return np.array([loc[int(v)] for v in normalized], dtype=np.int16)


outputs, saved = [], {}
for block, first, expected in [(0, A, 18), (1, A[A[A]], 8)]:
    operators = [local(first, block), local(Z[Z], block)]
    K = S.centralizer(PermutationGroup([Permutation(p.tolist()) for p in operators]))
    assert K.order() == expected
    values = np.array([p.array_form for p in K.generate_schreier_sims()], dtype=np.int16)
    assert len(values) == expected
    for v in values:
        assert S.contains(Permutation(v.tolist()))
        assert all(np.array_equal(v[p], p[v]) for p in operators)
    saved[f'operators_{block}'] = np.array(operators)
    saved[f'centralizer_{block}'] = values
    outputs.append({
        'block': block,
        'operators': ['A' if block == 0 else 'A^3', 'z3^2'],
        'operator_orders': [int(Permutation(p.tolist()).order()) for p in operators],
        'centralizer_order_in_S': expected,
        'all_listed_elements_checked_in_S_and_commuting': True,
    })

# Keep deterministic seed numbering used in the already checked global list.
old0 = np.load(HERE / 'hurwitz_fixed_block_centralizers.npz')['centralizer_0']
old1 = np.load(HERE / 'hurwitz_six_block_centralizer.npz')['centralizer_1']
for block, old in [(0, old0), (1, old1)]:
    assert {p.tobytes() for p in old} == {p.tobytes() for p in saved[f'centralizer_{block}']}
    saved[f'centralizer_{block}'] = old

np.savez_compressed(HERE / 'hurwitz_seed_centralizers.npz', **saved)
out = {'statement': 'D23.P22', 'ambient_simple_group_order': int(S.order()),
       'cases': outputs, 'result': 'PASS'}
(HERE / 'hurwitz_seed_centralizers.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
