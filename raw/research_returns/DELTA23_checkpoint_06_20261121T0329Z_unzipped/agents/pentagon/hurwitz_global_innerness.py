#!/usr/bin/env python3
"""D23.P20: the exact binary normalizer obstruction and local A-coupling."""
from pathlib import Path
import itertools
import json
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIVE = HERE.parent / 'five_level_six'

record = json.loads((FIVE / 'hurwitz_block_correlations.json').read_text())
raw = np.load(HERE / 'hurwitz_cubic216_four_13.npz')
block = np.load(HERE / 'hurwitz_cubic216_four_13_block0.npz')
correlations = np.load(FIVE / 'hurwitz_block_correlations.npz')
stabilizer = np.load(FIVE / 'hurwitz_block_stabilizer.npz')
lifts = np.load(ROOT / 'records/hurwitz_h1_orthogonal_lifts.npz')
qs = block['generators']
triples = [tuple(t) for t in record['parallel_triples']]
triple_actions = []
for q in qs:
    a = np.array([triples.index(tuple(sorted(q[list(t)]))) for t in triples])
    assert np.array_equal(a[a[a]], np.arange(4))
    triple_actions.append(a)
seen = {0}
todo = [0]
for x in todo:
    for a in triple_actions:
        y = int(a[x])
        if y not in seen:
            seen.add(y)
            todo.append(y)
assert seen == set(range(4))

checks = []
for t in triples[1:]:
    a = np.zeros(12, dtype=int)
    a[list(triples[0])] = 1
    a[list(t)] = 1
    checks.append(a)
checks = np.array(checks)
normalizer_vectors = []
for bits in itertools.product([0, 1], repeat=12):
    v = np.array(bits)
    normalizes = all(not (checks @ (v + v[np.argsort(q)]) % 2).any() for q in qs)
    belongs = not (checks @ v % 2).any()
    assert normalizes == belongs
    if normalizes:
        normalizer_vectors.append(v)
assert len(normalizer_vectors) == 512

# A transitive permutation centralizer is determined by one point image.
centralizers = []
for image_zero in range(12):
    p = np.full(12, -1, dtype=int)
    p[0] = image_zero
    queue = [0]
    valid = True
    for x in queue:
        for q in qs:
            y, z = int(q[x]), int(q[p[x]])
            if p[y] == -1:
                p[y] = z
                queue.append(y)
            elif p[y] != z:
                valid = False
                break
        if not valid:
            break
    if valid and len(set(map(int, p))) == 12:
        centralizers.append(p)
assert len(centralizers) == 1 and np.array_equal(centralizers[0], np.arange(12))

# Couple the four exact H3 local lists using the unmodified first generator.
base = stabilizer['base']
loc = {int(v): i for i, v in enumerate(base)}
trans = correlations['transversals']
known = [7, 8, 10, 11]
a, qa = raw['generators'][0], qs[0]
local_a = {
    j: np.array([loc[int(v)] for v in np.argsort(trans[qa[j]])[a[trans[j][base]]]])
    for j in known
}
cases = []
for a3 in [0, 1]:
    values = {j: lifts[f'case_{a3}_{j}_permutations'] for j in known}
    allowed = []
    for indices in itertools.product(range(3), repeat=4):
        v = {j: values[j][i] for j, i in zip(known, indices)}
        if all(np.array_equal(v[int(qa[j])][local_a[j]], local_a[j][v[j]]) for j in known):
            allowed.append(indices)
    expected = [(i, i, i, j) for i in range(3) for j in range(3)]
    assert allowed == expected
    cases.append({'rho': 0, 'a3': a3, 'block_order': known, 'allowed_indices': allowed})

out = {
    'statement': 'D23.P20',
    'parallel_triples': triples,
    'triple_actions': [a.tolist() for a in triple_actions],
    'triple_actions_have_order3_and_are_transitive': True,
    'binary_code_size': 512,
    'normalizing_sign_vectors_exactly_equal_the_code': True,
    'normalizing_vectors_with_four_known_signs_zero': sum(not v[known].any() for v in normalizer_vectors),
    'degree12_centralizer_order': 1,
    'local_A_coupling': cases,
    'scope': 'Exact binary and local coupling checks; actual innerness uses P18/P19, F30 and H3 as stated in the proof.',
    'result': 'PASS',
}
assert out['normalizing_vectors_with_four_known_signs_zero'] == 32
(HERE / 'hurwitz_global_innerness.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
