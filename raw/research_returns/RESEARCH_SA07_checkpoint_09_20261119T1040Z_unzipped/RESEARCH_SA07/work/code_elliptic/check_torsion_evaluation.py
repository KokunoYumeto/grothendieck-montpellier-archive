#!/usr/bin/env python3
"""Exact certificate for work/agent_elliptic.md §38.2.

Inputs are printed below.  The coefficient involution is sqrt(2) -> -sqrt(2),
fixing Q.  The symbolic calculation uses an arbitrary invertible 2-by-2
matrix B and arbitrary A, with sigma(B)=P^{-1}B and sigma(A)=A.
"""
import json
import time
from datetime import datetime, timezone
from pathlib import Path
import sympy as s

started = datetime.now(timezone.utc)
t0 = time.perf_counter()
lines = []
def record(label, value):
    lines.append(f'{label}: {value}')
def zero(M):
    return M.applyfunc(s.simplify) == s.zeros(*M.shape)

r = s.sqrt(2)
A = s.Matrix([[0, 2], [1, 0]])
B = s.Matrix([[1, r], [1, -r]])
P = s.Matrix([[0, 1], [1, 0]])
sigma_B = B.xreplace({r: -r})
Q = s.simplify(B*A*B.inv())
sigma_Q = Q.xreplace({r: -r})
record('input A', A.tolist())
record('input B', B.tolist())
record('input P', P.tolist())
record('det B', s.factor(B.det()))
record('Q = B A B^-1', Q.tolist())
checks = {
    'sigma(B) = P^-1 B': zero(sigma_B-P.inv()*B),
    'Q = diag(sqrt(2),-sqrt(2))': zero(Q-s.diag(r,-r)),
    'sigma(Q) = -Q': zero(sigma_Q+Q),
    'sigma(Q) = P^-1 Q P': zero(sigma_Q-P.inv()*Q*P),
    'P sigma(Q) P^-1 = Q': zero(P*sigma_Q*P.inv()-Q),
    'Q P differs from P Q': not zero(Q*P-P*Q),
}
record('Q P - P Q', (Q*P-P*Q).tolist())

b11,b12,b21,b22 = s.symbols('b11 b12 b21 b22')
a11,a12,a21,a22 = s.symbols('a11 a12 a21 a22')
Bs = s.Matrix([[b11,b12],[b21,b22]])
As = s.Matrix([[a11,a12],[a21,a22]])
Qs = Bs*As*Bs.inv()
sigma_Bs = P.inv()*Bs
sigma_Qs = sigma_Bs*As*sigma_Bs.inv()
checks['symbolic conjugation under sigma(B)=P^-1B'] = zero(
    sigma_Qs-P.inv()*Qs*P)
checks['symbolic semilinear descent identity'] = zero(
    P*sigma_Qs*P.inv()-Qs)
checks['linear commutation defect identity'] = zero(
    (P.inv()*Qs*P-Qs)-P.inv()*(Qs*P-P*Qs))
record('symbolic hypothesis', 'det(B) != 0; sigma(A)=A; sigma(B)=P^-1 B')
for label, passed in checks.items():
    record(label, 'PASS' if passed else 'FAIL')
assert all(checks.values())
elapsed = time.perf_counter()-t0
record('total checks', len(checks))
record('elapsed seconds', f'{elapsed:.6f}')
record('sympy version', s.__version__)
record('result', 'PASS')
output = '\n'.join(lines)+'\n'
print(output, end='')
Path(__file__).with_suffix('.out').write_text(output)
metadata = {
    'script': 'work/code_elliptic/check_torsion_evaluation.py',
    'claim': 'ELL-ROUTE-38 exact torsion-evaluation matrix identities',
    'started_utc': started.isoformat(),
    'elapsed_seconds': elapsed,
    'inputs': {
        'A': [[0,2],[1,0]],
        'B': [['1','sqrt(2)'],['1','-sqrt(2)']],
        'P': [[0,1],[1,0]],
        'coefficient_automorphism': 'sqrt(2) maps to -sqrt(2)',
        'symbolic_hypothesis': 'B invertible, sigma(A)=A, sigma(B)=P^-1 B'
    },
    'checks': checks,
    'sympy_version': s.__version__,
    'status': 'PASS',
    'scope': 'Finite exact linear algebra only; no H1 arithmetic bridge asserted.'
}
Path(__file__).with_suffix('.json').write_text(json.dumps(metadata, indent=2)+'\n')
