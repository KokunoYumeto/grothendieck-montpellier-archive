"""Exact finite verification of the two source-audit counterexamples.

This script checks the displayed identities only; the general algebraic
arguments and source-scope conclusions are proved in I22_source_audit.tex.
"""
import json
from pathlib import Path
import sympy as sp

x1, x2, x3, x4 = sp.symbols('x1 x2 x3 x4')
N = sp.Matrix([[0, 1], [0, 0]])
M = sp.Matrix([[0, 0], [1, 0]])
E11, E22 = N*M, M*N
I = sp.eye(2)

W1 = (M+x1*N)*(M+x2*N)
assert W1 == x1*E11+x2*E22
assert W1[0, 1] == 0
assert N[0, 1] == 1
assert sp.Matrix.hstack(*(sp.Matrix(A).reshape(4, 1)
                         for A in (N, M, E11, E22))).rank() == 4

W2 = sp.expand(x1*E11*(I+x2*N)*(I+x3*N)*x4*E22)
assert sp.expand(W2-x1*x4*(x2+x3)*N) == sp.zeros(2)
assert W2[0, 1] != 0
assert W2[0, 0] == W2[1, 1] == 0
assert N*N == sp.zeros(2)
assert sp.Matrix([[0, 1], [1, 0]]).det() == -1

data = {
    'first_matrix_product': str(W1),
    'first_scalar_output': str(W1[0, 1]),
    'generated_matrix_unit_span_rank': 4,
    'second_matrix_product': str(W2),
    'second_scalar_output': str(W2[0, 1]),
    'second_simple_quotient_coordinates': [0, 0],
    'radical_square': str(N*N),
    'status': 'PASS: exact displayed identities; not a general proof certificate',
}
out = Path(__file__).with_name('I22_computation_checks.json')
out.write_text(json.dumps(data, indent=2)+'\n')
print(json.dumps(data, indent=2))
