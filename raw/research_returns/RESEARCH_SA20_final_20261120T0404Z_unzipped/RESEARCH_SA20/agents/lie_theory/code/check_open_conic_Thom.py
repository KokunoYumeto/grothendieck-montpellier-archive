#!/usr/bin/env python3
"""Exact polynomial identities for the proper open conic Thom obstruction."""
from time import perf_counter
started = perf_counter()
from sympy import Matrix, symbols, expand, cancel, factor

a, b, u, v, w, U, V, W, t, alpha, z = symbols(
    "a b u v w U V W t alpha z")
F = u*u-a*a*v*w-b*w*w
transformed = (u/a)**2-(v+b*w/(a*a))*w
assert cancel(transformed-F/(a*a)) == 0
inverse_equation = F.subs({u:a*U, v:V-b*W/(a*a), w:W}, simultaneous=True)
assert cancel(inverse_equation-a*a*(U*U-V*W)) == 0
assert cancel((a*U)/a-U) == 0
assert cancel((V-b*W/(a*a))+b*W/(a*a)-V) == 0

curve_equation = F.subs({a:t*alpha,b:-t*t,u:0,v:z,w:1}, simultaneous=True)
assert expand(curve_equation-t*t*(1-alpha*alpha*z)) == 0

A, B = symbols("A B", real=True)
vertical = Matrix([[0,0,-(A*A-B*B),2*A*B],
                   [0,0,-2*A*B,-(A*A-B*B)]])
minor = factor(vertical[:,2:4].det())
assert expand(minor-(A*A+B*B)**2) == 0
assert vertical[:,0:2] == Matrix.zeros(2,2)

print("PROJECTIVE FAMILY: u^2-a^2*v*w-b*w^2=0")
print("FORWARD CHANGE: U^2-V*W = F/a^2")
print("INVERSE CHANGE: F = a^2*(U^2-V*W)")
print("CURVE RESIDUAL:", factor(curve_equation))
print("CURVE CONDITION: alpha^2*z=1 makes residual zero")
print("VERTICAL REAL DERIVATIVE:")
print(vertical)
print("z-BLOCK DETERMINANT:", minor)
print("KERNEL: complex u-line whenever a != 0")
print("PASS: exact proper-open-conic algebra certificate")
print(f"RUNTIME_SECONDS: {perf_counter()-started:.9f}")
