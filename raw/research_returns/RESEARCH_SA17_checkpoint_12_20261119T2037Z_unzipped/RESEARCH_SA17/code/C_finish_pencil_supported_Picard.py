#!/usr/bin/env python3
"""Exact polynomial certificate for the displayed pencil module only.

The conductor, Picard quotient and supported-category arguments are proved
in the TeX source; they are not inferred from this symbolic calculation.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import sympy as s

started = time.perf_counter()
pi, b, c, h, U, W = s.symbols('pi b c h U W')
X = s.Matrix([[-pi*h, pi*(c+h)-h*h+pi*b*h],
              [pi*pi, pi*h-pi*pi*b]])
I = s.eye(2)
f = U*U+pi*pi*b*U-pi**3*(c+h)
Phi, Psi = U*I-X, (U+pi*pi*b)*I+X
tests = {}

def matrix_zero(name, value):
    entries = [s.expand(v) for v in value]
    assert all(v == 0 for v in entries), (name, entries)
    tests[name] = {'entries': len(entries), 'result': 'PASS'}

def scalar_zero(name, value):
    assert s.expand(value) == 0, (name, s.expand(value))
    tests[name] = {'entries': 1, 'result': 'PASS'}

matrix_zero('Cayley_Hamilton', X*X+pi*pi*b*X-pi**3*(c+h)*I)
matrix_zero('Phi_Psi', Phi*Psi-f*I)
matrix_zero('Psi_Phi', Psi*Phi-f*I)
scalar_zero('trace', s.trace(X)+pi*pi*b)
scalar_zero('determinant', X.det()+pi**3*(c+h))
normal = s.Poly(W*W+pi*b*W-pi*(c+h), W)
for column, basis_element in enumerate([pi, h+W]):
    actual = pi*W*basis_element
    given = pi*X[0,column]+(h+W)*X[1,column]
    remainder = s.rem(s.Poly(s.expand(actual-given), W), normal).as_expr()
    scalar_zero(f'U_action_column_{column+1}', remainder)

root = Path(__file__).resolve().parents[1]
source = root/'notes/C_pencil_supported_Picard_proposed.tex'
record = {
    'date': datetime.now(timezone.utc).isoformat(),
    'status': 'PASS',
    'certificate': 'Exact integral polynomial identities with 2 represented by pi^2*b',
    'tests': tests,
    'identities': len(tests),
    'scalar_entries': sum(row['entries'] for row in tests.values()),
    'elapsed_seconds': time.perf_counter()-started,
    'source': str(source.relative_to(root)),
    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'limitations': 'Symbolic identities only. Does not certify the conductor/Picard/derived-category proof or any Swan-category transfer.'
}
target=root/'logs/C_finish_pencil_supported_Picard.json'
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
