"""Exact finite-series verification for the C11 reduced-theta example.
This checks rational coefficients, not a formal proof or an asymptotic radius.
"""
import sympy as sp
T, Z = sp.symbols('T Z')
x = (1 + sp.sqrt(1 + 4*T**4))/(2*T**2)
y = -x/T
omega = sp.series(sp.diff(x, T)/(2*y), T, 0, 10).removeO()
lam = sp.integrate(omega, T)
wp = Z**-2 + Z**2/sp.Integer(5) + Z**6/sp.Integer(75)
log_sigma_regular = -Z**4/sp.Integer(60) - Z**8/sp.Integer(4200)
assert sp.expand(sp.diff(sp.log(Z) + log_sigma_regular, Z, 2) + wp) == 0
sigma = sp.series(Z*sp.exp(log_sigma_regular), Z, 0, 10).removeO()
formal_theta = sp.series(sigma.subs(Z, lam), T, 0, 10).removeO()
assert sigma == Z-Z**5/sp.Integer(60)-Z**9/sp.Integer(10080)
assert formal_theta == T-5*T**5/sp.Integer(12)+1411*T**9/sp.Integer(2016)
assert 1411 % 7 != 0 and 2016 % 49 != 0 and 2016 % 7 == 0
print('omega/dT =', omega)
print('lambda(T) =', lam)
print('sigma(Z) =', sigma)
print('theta(lambda(T)) =', formal_theta)
print('v_7 coefficient(T^9) = -1')
print('theta^(9)(0) =', sp.factorial(9)*sigma.coeff(Z, 9))
