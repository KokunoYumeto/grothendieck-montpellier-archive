#!/usr/bin/env python3
"""Independent dense matrix trace for the formerly missing E8(a2) exponent."""
from pathlib import Path
from time import perf_counter
from datetime import datetime,timezone
import json
import sympy as sp
from exceptional_jacobian import RootLie,OUT
started=perf_counter();print('Started UTC',datetime.now(timezone.utc).isoformat())
r=json.loads((OUT/'jacobian_E8_22202022.json').read_text())
L=RootLie('E8')
e={L.idx[tuple(a['basis'])]:sp.Rational(a['coefficient']) for a in r['e']}
A=sp.SparseMatrix(L.n,L.n,{(i,j):c for j,col in enumerate(L.adj(e)) for i,c in col.items()})
minus_theta=tuple(-x for x in max(L.roots,key=sum));y=L.idx[minus_theta]
B=sp.SparseMatrix(L.n,L.n,{(i,j):c for j in range(L.n) for i,c in L.table[y][j]})
# SymPy's exponentiation by squaring and exact trace are separate from the
# column-dictionary repeated multiplication used for the all-orbit table.
value=20*sp.trace((A**19)*B)
assert value==3617744486400
print('E8(a2), d Tr(ad x)^20 at e on e_minus_theta =',value)
print('PASS: independent sparse exponentiation by squaring and trace')
print('Elapsed seconds',perf_counter()-started)
