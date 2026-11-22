"""Universal local transition identities only; no cup nonvanishing inference."""
from pathlib import Path
import datetime
import json
import time
from sympy import Matrix, Poly, symbols, together

started = time.perf_counter()
a, b, c, h, z, g, fi = symbols('a b c h z g fi')
variables = (a, b, c, h, z, g, fi)
checks = []

def zero(name, expression):
    numerator = together(expression).as_numer_denom()[0]
    assert Poly(numerator, *variables, modulus=2).is_zero, (name, numerator)
    checks.append(name)

M = Matrix([[a, a*c+b*h], [b, b*c+a]])
N = a*a+b*b*h
Qi = Matrix([[h, 1], [1, 0]])
Qj = Matrix([[h+c*c, 1], [1, 0]])
squareM = M.applyfunc(lambda x:x*x)
zero('determinant_norm', M.det()-N)
normalized = Qi.inv()*squareM*Qj/N
target = Matrix([[1, b*b/N], [0, 1]])
for i in range(2):
    for j in range(2):
        zero(f'normalized_transition_{i}_{j}', normalized[i,j]-target[i,j])

# The Frobenius-nilpotence implication requires a global cohomological
# argument; this program verifies only its displayed differential identity.
gamma = b*b/N
zero('gamma_dh_identity', gamma.diff(h)-gamma*gamma)
zero('gamma_da_zero', gamma.diff(a))
zero('gamma_db_zero', gamma.diff(b))

# If a cocycle gamma has square coboundary f_j-f_i, these are the exact
# change-of-frame identities yielding Sym^2 U = U plus O and U tensor U = U plus U.
sym = Matrix([[1,g,g*g],[0,1,0],[0,0,1]])
Pi = Matrix([[1,0,fi],[0,1,0],[0,0,1]])
Pj = Matrix([[1,0,fi+g*g],[0,1,0],[0,0,1]])
sym_target = Matrix([[1,g,0],[0,1,0],[0,0,1]])
sym_new = Pi.inv()*sym*Pj
for i in range(3):
    for j in range(3):
        zero(f'symmetric_square_frame_{i}_{j}',sym_new[i,j]-sym_target[i,j])

record = {'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'elapsed_seconds':time.perf_counter()-started,'identities':checks,
          'scope':'Universal local transition and differential identities; the symmetric-square calculation is conditional on a square-coboundary cocycle. No global extension-class, restricted-cup, or rank lower bound follows from these computations alone.'}
dest=Path(__file__).with_suffix('.output.json')
assert not dest.exists()
dest.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
