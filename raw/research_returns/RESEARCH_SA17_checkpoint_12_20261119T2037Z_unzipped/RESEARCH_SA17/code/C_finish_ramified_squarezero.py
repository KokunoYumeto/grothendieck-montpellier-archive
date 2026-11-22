#!/usr/bin/env python3
"""Exact Tate checks of the ramified-DVR witness, ramification indices1--6."""
from pathlib import Path
import numpy as np
import json
import time

exec(Path('code/C_finish_dualnumber_ring.py').read_text().split('\nobjects =')[0])
start = time.perf_counter()
out = []
for e in range(1, 7):
    P = np.zeros((e, e), dtype=np.int64)
    for j in range(e-1):
        P[j+1, j] = 1
    P[0, e-1] = 2
    C = np.linalg.matrix_power(P, e-1)
    assert np.array_equal(P @ C, 2*eye(e))
    z = np.zeros_like(P)
    T = np.block([[eye(e), P], [z, -eye(e)]])
    U = np.block([[eye(e), z], [-C, -eye(e)]])
    assert np.array_equal(T @ T, eye(2*e))
    assert np.array_equal(U @ U, eye(2*e))
    assert not np.any(T @ U+U @ T)
    d = h_data(T, U)
    assert d['h'] == 2 and d['chi'][0] == 1
    J = T @ U
    assert np.array_equal(J @ J, -eye(2*e))
    assert not np.any(J @ T+T @ J)
    assert not np.any(J @ U+U @ J)
    out.append({'ramification_index': e, 'underlying_Z2_rank': 2*e,
                'total_Tate_F2_dimension': d['h'], 'u_minus_1_parity': d['chi'][0],
                'sign_conjugacy': True})
report = {'scope': 'A_e=Z_2[pi]/(pi^e-2), e=1,...,6; actual Tate kernels/images '
                   'on underlying Z_2 lattice',
          'statement_id': 'C:ramified_squarezero_criterion',
          'arithmetic': 'exact integer matrices and F2',
          'witnesses': out, 'runtime_seconds': round(time.perf_counter()-start, 6)}
Path('logs/C_finish_ramified_squarezero.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
