#!/usr/bin/env python3
"""Necessary finite source surjectivity for the eighteen actual-source candidates.

No invariant-kernel hypothesis is used: composing an actual automorphism
of the free profinite C2*C3 with any finite quotient must be onto.
"""
from pathlib import Path
import json, pickle, sys, time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CHAR = HERE.parent / 'characters'
sys.path.insert(0, str(CHAR / 'code'))
from hurwitz_mixed72_s3_core import induced
from hurwitz_mixed_reflection_map import Reflection

start = time.monotonic()
data = np.load(CHAR / 'records/hurwitz_full_mixed_s3_compact.npz')
sub = data['subset']; n = len(sub)
ix = np.full(1344, -1, dtype=int); ix[sub] = np.arange(n)
x, y = data['x'], data['y']
s, r, X, Y = induced(x, y)
N = len(s); I = np.arange(N); tau = s[r]
source = PermutationGroup([Permutation(g.tolist()) for g in [s, r]])
order = int(source.order())
with (HERE / 'hurwitz_mixed_source_group_state.pkl').open('wb') as stream:
    pickle.dump((list(source.args), source.__dict__), stream)
print('source E order', order, 'elapsed', time.monotonic() - start, flush=True)
theta = Reflection()
base = np.load(ROOT / 'records/hurwitz_pentagon45_fibers.npz')
labels = np.load(CHAR / 'records/hurwitz_full_mixed_s3_membership.npz')['passing_labels']
rows, fs, ss, rr = [], [], [], []
tau_powers = [I]
while True:
    p = tau[tau_powers[-1]]
    if np.array_equal(p, I):
        break
    tau_powers.append(p)
assert len(tau_powers) <= 24
known = []
for i, j in labels:
    a0 = base[f'R_{i}'][j]; t0 = theta(a0)
    a, t = ix[a0[sub]], ix[t0[sub]]
    ai, ti, xi, yi = np.argsort(a), np.argsort(t), np.argsort(x), np.argsort(y)
    blocks = [a, ai, t[ai], ti, xi[t[x]], y[a[ti[yi]]]]
    f = np.concatenate([k*n + g for k, g in enumerate(blocks)])
    sf, fr = s[f], np.argsort(f)[r]
    assert np.array_equal(sf[sf], I) and np.array_equal(fr[fr[fr]], I)
    assert np.array_equal(sf[fr], tau)
    same = None
    for old_i, old_sf, old_order in known:
        for k, tp in enumerate(tau_powers):
            if np.array_equal(tp[old_sf[np.argsort(tp)]], sf):
                same = (old_i, k, old_order)
                break
        if same is not None:
            break
    if same is not None:
        got = same[2]
        method = {'tau_conjugate_to_row': same[0], 'tau_power': same[1]}
    else:
        H = PermutationGroup([Permutation(g.tolist()) for g in [sf, fr]])
        got = int(H.order())
        known.append((len(rows), sf, got))
        method = {'fresh_stabilizer_chain': True}
    row = {'candidate': int(i), 'R_fiber_index': int(j),
           'new_generator_group_order': got, 'surjective': got == order, **method}
    rows.append(row); fs.append(f); ss.append(sf); rr.append(fr)
    print(row, 'elapsed', time.monotonic() - start, flush=True)
    (HERE / 'hurwitz_mixed_source_generation.json').write_text(json.dumps({
        'source_order': order, 'source_degree': N, 'tau_order': len(tau_powers),
        'cases': rows, 'elapsed_seconds': time.monotonic() - start,
        'scope': 'Necessary source surjectivity only; no quotient-kernel invariance or profinite realization claim.'}, indent=2) + '\n')
np.savez_compressed(HERE / 'hurwitz_mixed_source_generation.npz', s=s, r=r, x=X, y=Y,
                    labels=labels, f=fs, new_s=ss, new_r=rr)
print('finished', len(rows), 'cases;', sum(r['surjective'] for r in rows), 'surjective', flush=True)
