"""Exact computational checks for S-05; no floating point or optimizer used."""
import itertools
import json
from pathlib import Path
import sympy as s

A = s.Matrix([[1, 1], [1, -1]])
vectors = s.Matrix([[1, 0], [0, 1], [s.Rational(3, 5), s.Rational(4, 5)],
                    [s.Rational(3, 5), -s.Rational(4, 5)]])
X = vectors * vectors.T  # Exact displayed Gram factor proves PSD.
assert all(X[i, i] == 1 for i in range(4))
L = sum(A[i, j] * X[i, j + 2] for i in range(2) for j in range(2))
assert L == s.Rational(14, 5)
values = [sum(A[i, j] * signs[i] * signs[2 + j]
              for i in range(2) for j in range(2))
          for signs in itertools.product([-1, 1], repeat=4)]
assert max(values) == 2
assert min(values) == -2
x1, x2, y1, y2 = s.symbols("x1 x2 y1 y2")
f = x1 * (y1 + y2) + x2 * (y1 - y2)
H0 = ((x1**2 - 1) * (y1 + y2)**2
      + (x2**2 - 1) * (y1 - y2)**2
      + (2 + 2*x1*x2) * (y1**2 - 1)
      + (2 - 2*x1*x2) * (y2**2 - 1))
assert s.expand(f**2 - 4 - H0) == 0
assert s.expand(2 - f - (2-f)**2 / 4 + H0 / 4) == 0
result = {
    "statement": "S-05",
    "arithmetic": "exact SymPy rationals and symbolic polynomial expansion",
    "gram_factor": str(vectors),
    "gram_diagonal": [str(X[i, i]) for i in range(4)],
    "primal_value": str(L),
    "sign_optimum_by_exhaustion": str(max(values)),
    "sos_identity_remainder": "0",
    "rank": A.rank(),
    "outcome": "PASS",
}
output = json.dumps(result, indent=2) + "\n"
Path(__file__).with_name("agent_sdp_checks_result.json").write_text(output)
print(output)
