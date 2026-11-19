#!/usr/bin/env python3
"""Exact integral C5-module data for the profinite lift work note.

The Gaschuetz lift, extension class and actual cusp maps are proved in
root_bass_unit_profinite_lift.md. This checks the literal integral matrices.
"""
from time import perf_counter
import sympy as sp

started = perf_counter()
z = sp.Symbol('z')
u = -2 + z + 3*z**2 + z**3 - 2*z**4
v = 1 + z - 2*z**2 + 3*z**3 - 2*z**4
assert sp.rem(u*v, z**5-1, z) == 1
assert u.subs(z, 1) == v.subs(z, 1) == 1
T = sp.zeros(5)
for j in range(5):
    T[(j+1) % 5, j] = 1
U = sum((u.coeff(z, i) * T**i for i in range(5)), sp.zeros(5))
V = sum((v.coeff(z, i) * T**i for i in range(5)), sp.zeros(5))
assert U*V == V*U == sp.eye(5)
assert U.det() == 1
assert U*T == T*U
assert U*sp.ones(5, 1) == sp.ones(5, 1)
assert sp.ones(1, 5)*U == sp.ones(1, 5)
Gamma = sp.diag(sp.eye(1), U)
Gamma_inv = sp.diag(sp.eye(1), V)
assert Gamma*Gamma_inv == sp.eye(6)
t = sp.eye(6)[:, 0]
y = sp.eye(6)[:, 1:]
infty = -t - sum((y[:, j] for j in range(5)), sp.zeros(6, 1))
assert Gamma*t == t and Gamma*infty == infty
# Every image of a y-cusp is distinct from every actual cusp vector or
# its negative. The displayed first vector already gives the obstruction.
cusps = [t] + [y[:, j] for j in range(5)] + [infty]
for j in range(5):
    assert all(Gamma*y[:, j] != eps*c for c in cusps for eps in (-1, 1))
push = sp.zeros(2, 6)
push[0, 0] = 5
for j in range(1, 6):
    push[1, j] = 1
assert push*Gamma == push
print('UNIT_COEFFICIENTS', [int(u.coeff(z, i)) for i in range(5)])
print('INVERSE_COEFFICIENTS', [int(v.coeff(z, i)) for i in range(5)])
print('CIRCULANT', U.tolist())
print('DETERMINANT', U.det())
print('FIXED_EXTENSION_GENERATOR', list(Gamma*t))
print('FIRST_CUSP_IMAGE', list(Gamma*y[:, 0]))
print('BASE_ABELIANIZATION_PUSHFORWARD', push.tolist())
print('PASSED: integral unit and inverse, C5 equivariance, fixed extension generator, fixed infinity cusp, and explicit failure to preserve the other actual cusp classes.')
print('SCOPE: these matrices concern one affine cover; no Galois or all-cover transporter is produced.')
print('ACTUAL_WALL_SECONDS', format(perf_counter()-started, '.9f'))
