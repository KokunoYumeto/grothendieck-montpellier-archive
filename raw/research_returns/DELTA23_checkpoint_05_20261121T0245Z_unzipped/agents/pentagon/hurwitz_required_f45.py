#!/usr/bin/env python3
"""D23.P25: required final pair value with every inverse kept literal."""
from pathlib import Path
import json
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIVE = HERE.parent / 'five_level_six'
base = np.load(HERE / 'hurwitz_cubic216_four_13.npz')
raw = np.load(ROOT / 'records/hurwitz_product_fixed_cover.npz')
raw_values = np.load(HERE / 'hurwitz_raw_simultaneous_covariance.npz')
first = np.load(FIVE / 'hurwitz_first_pair_covariance.npz')
mixed = np.load(ROOT / 'records/hurwitz_solvable_fiber_filter.npz')


def setup(gens):
    a, b, c = gens
    d = a[b[c[a[b[a]]]]]
    di = np.argsort(d)
    x1, x2, x3 = a[a], b[b], c[c]
    u, v = a[b[a]], c[b[c]]
    x4, x5 = u[u], v[v]
    assert np.array_equal(d[x1[di]], x3)
    assert np.array_equal(d[x2[di]], x2)
    assert np.array_equal(d[x4[di]], x5)
    full = a[b[c]]
    full = full[full[full[full]]]
    assert np.array_equal(d[d], full)
    return d, di, np.array([x1, x2, x3, x4, x5])


db, dib, xb = setup(base['generators'])
dr, dir_, xr = setup(raw['generators'])


def required(d, di, F, R):
    # H=[D,FR]=D F R D^-1 R^-1 F^-1.
    H = d[F[R[di[np.argsort(R)[np.argsort(F)]]]]]
    p2 = d[np.argsort(R)[di]]
    p3 = d[np.argsort(F)[di]]
    pentagon = R[p2[p3[H[F]]]]
    assert np.array_equal(pentagon, np.arange(len(F)))
    return H


base_H, raw_H, labels = [], [], []
for row, candidate in enumerate(mixed['base_indices']):
    candidate = int(candidate)
    F = first[f'F_1_{candidate}']
    R = mixed['R_witnesses'][row]
    H = required(db, dib, F, R)
    Hr = required(dr, dir_, raw_values[f'rawF_{candidate}'], raw_values[f'rawR_{candidate}'])
    assert np.array_equal(Hr[::6] // 6, H)
    base_H.append(H)
    raw_H.append(Hr)
    labels.append(candidate)
np.savez_compressed(HERE / 'hurwitz_required_f45.npz', candidate_indices=labels,
                    base_H=base_H, raw_H=raw_H, base_D=db, raw_D=dr,
                    base_X=xb, raw_X=xr)
out = {'statement': 'D23.P25', 'required_value': '[D, F R] = D F R D^-1 R^-1 F^-1',
       'commutator_convention': 'a b a^-1 b^-1',
       'reversing_half_twist_conjugacies': 'PASS',
       'D_squared_equals_full_twist_in_both_actions': True,
       'recorded_witness_count': len(labels),
       'literal_five_factor_products_with_required_H': 'all identity',
       'raw_required_H_projects_to_base': True,
       'scope': 'Required value only; membership in the pair45 derived image and common-word/gentle compatibility are separate.',
       'result': 'PASS'}
(HERE / 'hurwitz_required_f45.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
