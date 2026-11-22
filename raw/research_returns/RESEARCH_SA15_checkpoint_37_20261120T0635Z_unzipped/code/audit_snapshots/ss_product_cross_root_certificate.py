"""Exact relative-Cartier and cross-block identities on the supersingular cubic."""
from pathlib import Path
from datetime import datetime, timezone
import json, time
import sympy as sp

start = time.perf_counter()
a, b, x, y, X, Y, r, s, t = sp.symbols('a b x y X Y r s t')
ring = sp.groebner([y*y+y+x**3, b*b+b+a**3], y, b, x, a,
                  modulus=2, order='lex')
checks = []
def zero(expr, label):
    assert ring.reduce(sp.expand(expr))[1] == 0, label
    checks.append(label)

# The two degree-three spaces have bases 1,x,(y+b+1)/(x+a)
# and 1,x,(y+b)/(x+a). Multiply products by x+a.
products = sp.Matrix([
    [x+a, x*(x+a), y+b],
    [x*(x+a), x*x*(x+a), x*(y+b)],
    [y+b+1, x*(y+b+1), x*x+a*x+a*a]])
zero((y+b)*(y+b+1)-(x+a)*(x*x+a*x+a*a),
     'rational product cancellation')
constant = sp.Matrix([
    [a, X, Y+b],
    [X, a*X, X*X],
    [Y+b+1, X*X, X+a*a]])
cartier = sp.Matrix([
    [1, a, X],
    [a, X, Y+b],
    [X, Y+b+1, a]])
# Relative Frobenius fixes the ground-field coefficients and sends
# target coordinates X,Y to x^2,y^2. Its Cartier projection extracts x.
for i in range(3):
    for j in range(3):
        square_part = constant[i,j].subs({X:x*x, Y:y*y}, simultaneous=True)
        odd_part = cartier[i,j].subs({X:x*x, Y:y*y}, simultaneous=True)
        zero(products[i,j]-square_part-x*odd_part,
             f'relative p-basis decomposition {i},{j}')

A0 = cartier.subs({X:0, Y:0})
R = cartier.diff(X)
A2 = cartier.diff(Y)
assert R == sp.Matrix([[0,0,1],[0,1,0],[1,0,0]])
assert R*R == sp.eye(3)
checks.append('universal invertible X coefficient')
expr = sp.expand((r*A0+s*R+t*A2).det() - (r*r*t+r*t*t+s**3))
for _, coefficient in sp.Poly(expr, r,s,t).terms():
    zero(coefficient, 'twisted elliptic determinant coefficient')
schur = A0*R*A2+A2*R*A0
expected = sp.Matrix([[0,1,a],[1,0,0],[a,0,1]])
for entry in schur-expected:
    zero(entry, 'one-trivial-factor Schur entry')
assert expected.det() == -1
checks.append('one-trivial-factor Schur determinant unit')

B0 = sp.Matrix([[0,1,0],[1,0,0],[0,0,0]])
B1 = sp.Matrix([[0,0,1],[0,0,0],[1,0,0]])
B2 = sp.Matrix([[0,0,0],[0,0,1],[0,1,0]])
untwisted = sum((sp.kronecker_product(B,B) for B in (B0,B1,B2)), sp.zeros(9))
minor = untwisted.minor_submatrix(0,0).det()
assert int(minor) % 2 == 1
assert all(untwisted[i,i] == 0 for i in range(9))
assert untwisted == untwisted.T
checks.append('untwisted alternating 9-space has a unit 8-minor')
assert sp.kronecker_product(R,R).det() in (-1,1)
checks.append('two-nontrivial-factor cross block is invertible')
output = {'status':'PASS', 'actual_utc':datetime.now(timezone.utc).isoformat(),
          'runtime_seconds':time.perf_counter()-start, 'checks':checks,
          'check_count':len(checks),
          'twisted_determinant':'r^2*t+r*t^2+s^3',
          'one_trivial_schur':[[str(v) for v in expected.row(i)] for i in range(3)],
          'untwisted_8_minor':int(minor),
          'scope':'Universal polynomial identities and displayed minors only. The geometric basis, relative-Frobenius conventions, odd-etale character decomposition and open-intersection argument require the accompanying proof. No fixed nonproduct-surface inference.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
