"""Exact checks used in the Part D arguments; no numerical transcendence tests."""
from itertools import product
import sympy as s

j = s.symbols('j')
A = -3*j/(j-1728)
B = -2*j/(j-1728)
j_computed = s.cancel(1728*4*A**3/(4*A**3+27*B**2))
print('j invariant of specified model:', j_computed)
assert j_computed == j
print('4A^3+27B^2:', s.factor(4*A**3+27*B**2))

a = s.symbols('a', nonzero=True)
base_parameter = a + 1/a
print('inversion fixes s:', s.cancel(base_parameter.subs(a,1/a)-base_parameter))
print('quadratic equation residual:', s.cancel(a*a-base_parameter*a+1))
print('nontrivial cocycle character:', s.cancel(a/(1/a)))

ideal_basis = s.Matrix([[2,1],[0,1]])
print('index of (2,1+sqrt(-5)):', abs(ideal_basis.det()))
norm_two = [(u,v) for u,v in product(range(-1,2),range(-1,2)) if u*u+5*v*v==2]
print('integer norm-two solutions (bounds follow from nonnegative summands):', norm_two)
assert norm_two == []

primes = [3,5,7,11,13]
indices=[]
for p in primes:
    squares = {pow(x,2,p) for x in range(1,p)}
    indices.append((p-1)//len(squares))
print('unit-square indices modulo odd primes:', list(zip(primes,indices)))
print('finite-product quotient size:', s.prod(indices))
assert indices == [2]*len(primes)

for r in [1,2,3,4]:
    print(f'r={r}: dim common determinant group={3*r+1}; dim flag stabilizer={2*r+1}')

print('All exact checks passed.')
