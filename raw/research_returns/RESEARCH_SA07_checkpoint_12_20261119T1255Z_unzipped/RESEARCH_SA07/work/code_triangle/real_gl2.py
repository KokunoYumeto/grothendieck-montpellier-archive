"""Exact rational-function check for the real GL2 period triangle.

Inputs: an indeterminate invertible comparison matrix A and rational real
Frobenius diag(1,-1). All computations are symbolic over Q(a,b,c,d), not
numerical transcendence tests. SymPy version and wall time are recorded.
"""
import time
import sympy as s

started = time.perf_counter()
a, b, c, d = s.symbols('a b c d')
A = s.Matrix([[a, b], [c, d]])
f = s.diag(1, -1)
D = s.factor(A.det())
R = s.simplify(A * f * A.inv())
h = s.factor(-R[0, 0] / R[1, 0])
beta = s.Matrix([[1, h], [0, 1]])
Z = s.simplify(beta * A)
gamma = s.simplify(Z.inv())
quadratic_relation = s.factor(Z[0, 0]*Z[1, 1] + Z[0, 1]*Z[1, 0])
assert quadratic_relation == 0
assert s.simplify(gamma * beta * A) == s.eye(2)
assert s.simplify(beta * R[:, 0])[0] == 0
J = s.Matrix(list(Z)).jacobian([a, b, c, d])
rank = J.rank()
assert rank == 3
j = s.Rational(1728) * 4 * (-1)**3 / (4 * (-1)**3 + 27)
disc = -16 * (4 * (-1)**3 + 27)
assert j == s.Rational(-6912, 23)
assert disc == -368
print('SymPy:', s.__version__)
print('Arithmetic: exact in Q(a,b,c,d)')
print('Open chart: (ad-bc)*c*d != 0')
print('A =', A)
print('det(A) =', D)
print('A*f*A^-1 =', R)
print('h =', h)
print('beta*A =', Z)
print('gamma =', gamma)
print('z11*z22 + z12*z21 =', quadratic_relation)
print('Jacobian rank of beta*A =', rank)
print('Example E: y^2=x^3-x+1')
print('Discriminant =', disc)
print('j =', j)
print('j integral:', j.q == 1)
print('All exact assertions passed.')
print('Wall seconds:', format(time.perf_counter()-started, '.6f'))
