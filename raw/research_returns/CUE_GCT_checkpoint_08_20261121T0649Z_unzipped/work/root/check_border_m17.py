#!/usr/bin/env python3
"""Independent selected-minor and scaling-relation check for the m=17 border.

The full entry reconstruction is a separately recorded author calculation.
This script reconstructs the integer input and point ordering, checks the
bilinear scaling identity on all rows, and uses fraction-free elimination.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import numpy as np

base = Path(__file__).resolve().parents[2]
folder = base / 'work/rectangular/border_ternary'
meta = folder / 'border_dense_m17.json'
d = json.loads(meta.read_text())
m, p = d['m'], d['prime']
assert (m, p, d['rows'], d['columns']) == (17, 1021, 190, 139)
state = 20330804
coeff = []
for _ in range(3*m*m + 6*m):
    state = (1664525*state + 1013904223) & 0xffffffff
    coeff.append((state >> 8) % p)
assert coeff == d['pencil_A'] + d['pencil_u'] + d['pencil_v']
points = [[a,b,m+1-a-b] for a in range(m+1,-1,-1)
          for b in range(m+1-a,-1,-1)]
assert points == d['points']
raw = (folder / 'border_dense_m17.u16').read_bytes()
J = np.frombuffer(raw, dtype='<u2').reshape(190,139).astype(np.int64)
assert np.all(J < p)
cols = [j for j in range(139) if j != 104]
assert d['selected_rows'] == list(range(138))
assert cols == d['selected_columns']
B = J[:138,cols].copy()
previous, sign = 1, 1
for k in range(137):
    if not B[k,k]:
        rows = np.flatnonzero(B[k+1:,k])
        assert len(rows)
        j = k+1+int(rows[0])
        B[[k,j]] = B[[j,k]]
        sign = -sign
    pivot = int(B[k,k])
    B[k+1:,k+1:] = ((pivot*B[k+1:,k+1:]
                     - B[k+1:,k,None]*B[None,k,k+1:])
                    * pow(previous,-1,p)) % p
    B[k+1:,k] = 0
    previous = pivot
det = sign*int(B[-1,-1]) % p
assert det == 501
relation = np.zeros(139, dtype=np.int64)
relation[3:3+3*m] = d['pencil_u']
relation[3+3*m:3+6*m] = -np.array(d['pencil_v'], dtype=np.int64)
assert np.any(relation % p)
assert np.all(J @ relation % p == 0)
out = {
    'checked_utc': datetime.now(timezone.utc).isoformat(),
    'who': 'GPT-6 Astra Pro; root; effort not exposed; CUE_GCT_20261121_R1',
    'status': 'PASS', 'm': m, 'prime': p,
    'matrix_shape': [190,139], 'rank': 138,
    'selected_minor_mod_prime': det,
    'method': 'fraction-free Bareiss recurrence modulo1021; explicit swap signs',
    'all_input_coefficients_and_points_reconstructed': True,
    'scaling_relation_checked_on_all_rows': True,
    'matrix_sha256': hashlib.sha256(raw).hexdigest(),
    'certificate_sha256': hashlib.sha256(meta.read_bytes()).hexdigest(),
    'deduction': 'Conditional border induction plus R24 gives c18=1262 and epsilon18=0.',
    'scope': 'Independent minor and relation check; all-entry Ryser reconstruction is separately credited to the author.'
}
(base/'work/root/border_m17_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
