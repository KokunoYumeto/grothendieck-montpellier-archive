#!/usr/bin/env python3
"""Exact symbolic certificates for A.4.25--26; SymPy rational arithmetic."""
import sympy as s

A, B, a, b, k, f, df = s.symbols('A B a b k f df')
Da = df/B + k*(A/B-a)*f
Db = df/B + k*(A/B-b)*f
assert s.expand(Da-Db-k*(b-a)*f) == 0
print('A.4.25 operator defect:', s.factor(Da-Db))

u, u0, bar_u0, h, c = s.symbols('u u0 bar_u0 h c')
eta0 = h*u0+c*bar_u0
lhs_exponent = -c*bar_u0*(u+u0/2)-h*(u+u0)**2/2
rhs_exponent = -h*u**2/2-eta0*(u+u0/2)
assert s.expand(lhs_exponent-rhs_exponent) == 0
print('A.4.26 torsion Gaussian exponent difference:', s.expand(lhs_exponent-rhs_exponent))
s0, s1, s2 = s.symbols('s0 s1 s2')
T = s.series(s.exp(-h*u*u/2)*(s0+s1*u+s2*u*u),u,0,3).removeO()
t2 = s.expand(T).coeff(u,2)
assert s.simplify(2*(s2-t2)/s0-h) == 0
print('Torsion coefficient [u^2]:', t2)
print('Recovered h:', s.simplify(2*(s2-t2)/s0))

g2, g3, v, z = s.symbols('g2 g3 v z')
sigma = lambda w: w-g2*w**5/s.Integer(240)-g3*w**7/s.Integer(840)
theta = s.series(s.exp(-h*u*u/2)*sigma(u),u,0,6)
assert theta.removeO().expand().coeff(u,3) == -h/2
print('Reduced theta through degree 5:', theta)
# The auxiliary z tracks total degree in (u,v), retaining the Laurent degree -1.
K = s.exp(-h*z*z*u*v)*sigma(z*(u+v))/(sigma(z*u)*sigma(z*v))
Kseries = s.series(K,z,0,3)
assert s.simplify(Kseries.removeO().coeff(z,-1)-(1/u+1/v)) == 0
assert s.simplify(Kseries.removeO().coeff(z,1)+h*(u+v)) == 0
print('Kronecker total-degree expansion:', Kseries)
print('All exact identities passed.')
