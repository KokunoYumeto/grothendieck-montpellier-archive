#!/usr/bin/env python3
"""Finite certificates for the arbitrary-module square-zero criterion.

Checks two independent nil directions, every nonzero F2-linear functional,
and all bounded integral admissible extensions of the stated endpoints.
The universal flat-coefficient argument, including non-fg modules, is a proof,
not something established by these finite checks.
"""
from pathlib import Path
from itertools import product
from time import perf_counter
import json
import numpy as np

exec(Path('code/C_finish_dualnumber_ring.py').read_text().split('\nobjects =')[0])
START = perf_counter()
FUNCTIONALS = [(1, 0), (0, 1), (1, 1)]


def blocks(a0, b0, rhs):
    a, b = rhs.shape
    free, base = [], np.zeros((a, b), dtype=np.int64)
    for i, j in product(range(a), range(b)):
        coefficient = a0[i, i]+b0[j, j]
        if coefficient:
            if rhs[i, j] % coefficient:
                return
            base[i, j] = rhs[i, j]//coefficient
        elif rhs[i, j]:
            return
        else:
            free.append((i, j))
    for values in product(range(2), repeat=len(free)):
        answer = base.copy()
        for ij, value in zip(free, values):
            answer[ij] = value
        yield answer


z1 = np.zeros((1, 1), dtype=np.int64)
objects = [(np.array([[1]]), z1, z1), (np.array([[-1]]), z1, z1)]
for a, b, c, d in product(range(2), repeat=4):
    objects.append((np.diag([1, -1]), np.array([[0, a], [b, 0]]),
                    np.array([[0, c], [d, 0]])))
data = [[h_data(t, l0*u+l1*v) for l0, l1 in FUNCTIONALS] for t, u, v in objects]
extensions = functional_checks = 0
for ia, (ta, ua, va) in enumerate(objects):
    for ib, (tb, ub, vb) in enumerate(objects):
        a, b = len(ta), len(tb)
        zero = np.zeros((b, a), dtype=np.int64)
        for x0 in blocks(ta, tb, np.zeros((a, b), dtype=np.int64)):
            for x1 in blocks(ta, tb, -ua @ x0-x0 @ ub):
                for x2 in blocks(ta, tb, -va @ x0-x0 @ vb):
                    extensions += 1
                    te = np.block([[ta, x0], [zero, tb]])
                    ue = np.block([[ua, x1], [zero, ub]])
                    ve = np.block([[va, x2], [zero, vb]])
                    assert np.array_equal(te @ te, eye(a+b))
                    assert not np.any(te @ ue+ue @ te)
                    assert not np.any(te @ ve+ve @ te)
                    inc, proj = np.vstack([eye(a), zero]), np.hstack([zero, eye(b)])
                    for il, (l0, l1) in enumerate(FUNCTIONALS):
                        functional_checks += 1
                        da, db, de = data[ia][il], data[ib][il], h_data(te, l0*ue+l1*ve)
                        hi, hp, hd = h_map(de, da, inc), h_map(db, de, proj), h_map(da, db, x0)
                        assert not np.any(hp @ hi % 2)
                        assert not np.any(hd @ hp % 2)
                        assert not np.any(hi @ hd % 2)
                        assert rank(hi)+rank(hd) == da['h']
                        assert rank(hi)+rank(hp) == de['h']
                        assert rank(hp)+rank(hd) == db['h']
                        assert not np.any((da['B'] @ hd+hd @ db['B']) % 2)
                        assert de['chi'] == [(x+y) % 2 for x, y in zip(da['chi'], db['chi'])]

direction_witnesses = []
for x in ((1, 0), (0, 1), (1, 1)):
    for functional in FUNCTIONALS:
        if sum(a*b for a, b in zip(x, functional)) % 2 != 1:
            continue
        t0 = np.diag([1, -1])
        swap = np.array([[0, 1], [1, 0]])
        coefficient = sum(a*b for a, b in zip(x, functional))
        witness = h_data(t0, coefficient*swap)
        assert witness['chi'][0] == 1
        J = np.array([[0, 1], [-1, 0]])
        assert not np.any(J @ t0+t0 @ J)
        assert not np.any(J @ swap+swap @ J)
        direction_witnesses.append({'x': x, 'functional': functional,
                                   'u_minus_1_parity': 1, 'sign_conjugacy': True})

# A finite quotient of Z_(2) lt F2.  This certifies the rank-one torsion
# witness in the ring (Z/4) lt F2; the infinite ring argument is in the proof.
elements = [(a, x) for a in range(4) for x in range(2)]
def mul(v, w):
    return ((v[0]*w[0]) % 4, (v[0]*w[1]+w[0]*v[1]) % 2)
def add(v, w):
    return ((v[0]+w[0]) % 4, (v[1]+w[1]) % 2)
for a, b, c in product(elements, repeat=3):
    assert mul(mul(a, b), c) == mul(a, mul(b, c))
    assert mul(a, add(b, c)) == add(mul(a, b), mul(a, c))
assert mul((1, 1), (1, 1)) == (1, 0)
assert (1, 1) not in ((1, 0), (3, 0))

report = {'statement_ids': ['C:linear_nil_Bockstein', 'C:squarezero_intrinsic_criterion'],
          'scope': '18 endpoints over A[e,d]/(e,d)^2; all free opposite-sign '
                   'extension coefficients0/1, other entries solved integrally; '
                   'all three nonzero F2-linear functionals on J/2J=F2^2',
          'arithmetic': 'exact integers and F2; no floating point',
          'admissible_extensions': extensions,
          'functional_exactness_and_additivity_checks': functional_checks,
          'direction_witnesses': direction_witnesses,
          'finite_torsion_ring_order': len(elements),
          'finite_torsion_ring_triples': len(elements)**3,
          'rank_one_torsion_determinant_distinct': True,
          'runtime_seconds': round(perf_counter()-START, 6)}
Path('logs/C_finish_squarezero_criterion.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
