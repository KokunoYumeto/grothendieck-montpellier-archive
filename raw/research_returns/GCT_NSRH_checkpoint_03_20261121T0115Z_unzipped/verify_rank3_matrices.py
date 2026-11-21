"""Exact symbolic certificate for the actual r=3 tensor-lattice calculations.

All representation matrices act on the RIGHT on ROW vectors.  A matrix B
whose rows are new basis vectors transforms an action matrix P to B*P*B^-1.
The output is an exact rational-function identity certificate, not a floating
point test, a proof-assistant proof, or a claim about designated canonical bases.
"""

from datetime import datetime, timezone
from pathlib import Path
import hashlib
import sys

import sympy as sp


def is_zero_matrix(matrix):
    return all(sp.cancel(entry) == 0 for entry in matrix)


def certify(name, actual, expected):
    difference = actual - expected
    assert is_zero_matrix(difference), (name, difference)
    print(f"{name}: PASS (entrywise exact rational-function equality)")
    print(f"  expected = {expected}")


print("Exact r=3 right-row-action matrix certificate")
print(f"UTC: {datetime.now(timezone.utc).isoformat()}")
print(f"Python: {sys.version.split()[0]}; SymPy: {sp.__version__}")
print(f"Script SHA-256: {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}")
print("Convention: row action; new row-basis matrix B gives B*P*B^-1.")

# Actual ordinary tensor weight block (112,121,211), from the source action.
v = sp.symbols("v", nonzero=True)
delta = v + 1 / v
D = delta**2
c1_3 = sp.Matrix([[delta, 0, 0], [0, v, 1], [0, 1, 1 / v]])
c2_3 = sp.Matrix([[v, 1, 0], [1, 1 / v, 0], [0, 0, delta]])
B3 = sp.Matrix(
    [[v**2, v, 1], [-1 - v**-2, v, 1], [-v**-1, -v**-2, delta]]
)
assert sp.cancel(B3.det() - (D - 1) ** 2) == 0
print("det B3 = (D-1)^2: PASS")
certify(
    "B3*c1*B3^-1",
    B3 * c1_3 * B3.inv(),
    sp.Matrix([[delta, 0, 0], [0, delta, 0], [0, 1, 0]]),
)
certify(
    "B3*c2*B3^-1",
    B3 * c2_3 * B3.inv(),
    sp.Matrix([[delta, 0, 0], [0, 0, 1], [0, 0, delta]]),
)

# The other mixed weight block (122,212,221) interchanges c1,c2;
# interchange the standard rows to recover the same standard matrices.
J3 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
certify(
    "other mixed weight c1",
    J3 * B3 * c2_3 * B3.inv() * J3,
    sp.Matrix([[delta, 0, 0], [0, delta, 0], [0, 1, 0]]),
)
certify(
    "other mixed weight c2",
    J3 * B3 * c1_3 * B3.inv() * J3,
    sp.Matrix([[delta, 0, 0], [0, 0, 1], [0, 0, delta]]),
)

# Use an independent symbol d for delta to make the remaining identities
# polynomial/rational identities before substituting delta=v+v^-1.
d = sp.symbols("delta", nonzero=True)
Dsym = d**2
c1 = sp.Matrix([[d, 0], [1, 0]])
c2 = sp.Matrix([[0, 1], [0, d]])
I2 = sp.eye(2)
P1 = sp.kronecker_product(c1, c1) + sp.kronecker_product(c1 - d * I2, c1 - d * I2)
P2 = sp.kronecker_product(c2, c2) + sp.kronecker_product(c2 - d * I2, c2 - d * I2)
B4 = sp.Matrix(
    [[d, -1, -1, d], [0, -1, 1, 0], [2 - Dsym, -d, -d, Dsym], [-Dsym, d, d, Dsym - 2]]
)
assert sp.factor(B4.det() - 8 * (Dsym - 1) ** 2) == 0
print("det B4 = 8(D-1)^2: PASS")
certify(
    "B4*P1*B4^-1",
    B4 * P1 * B4.inv(),
    sp.Matrix([[Dsym, 0, 0, 0], [0, 0, 0, 0], [0, 0, Dsym, 0], [0, 0, Dsym - 2, 0]]),
)
certify(
    "B4*P2*B4^-1",
    B4 * P2 * B4.inv(),
    sp.Matrix([[Dsym, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, Dsym - 2], [0, 0, 0, Dsym]]),
)

# Source N(a) row module to the standard row Morita module on its branch.
a, Dformal = sp.symbols("a D", nonzero=True)
q = a / Dformal
z = 1 - q**2
Sa = sp.Matrix([[1, 0], [-q**2, q]])
N1 = sp.Matrix([[Dformal, 0], [a, 0]])
N2 = sp.Matrix([[0, a], [0, Dformal]])
assert sp.cancel(Sa.det() - q) == 0
print("det S_a = a/D: PASS")
certify("S_a*(N1/D)*S_a^-1", Sa * (N1 / Dformal) * Sa.inv(), sp.diag(1, 0))
certify(
    "S_a*(N2/D)*S_a^-1",
    Sa * (N2 / Dformal) * Sa.inv(),
    sp.Matrix([[1 - z, 1], [z * (1 - z), z]]),
)

# Separate consistency check of the ordinary H3 splitting algebra map.
words = [I2, c1, c2, c1 * c2, c2 * c1, c1 * c2 * c1]
plus = [1, d, d, d**2, d**2, d**3]
minus = [1, 0, 0, 0, 0, 0]
evaluation = sp.Matrix([plus, minus] + [[w[i, j] for w in words] for i in range(2) for j in range(2)])
assert sp.factor(evaluation.det() + d * (d**2 - 1) ** 3) == 0
print("ordinary H3 evaluation determinant = -delta*(D-1)^3: PASS")

print("All exact matrix identities passed.")
print("Regularity uses that 2, delta, D-1, D-2 are units in the stated R0.")
print("No numerical approximation or finite parameter sampling was used.")
