#!/usr/bin/env python3
"""Exact algebra in two explicit proper semialgebraic Thom tests."""
from time import perf_counter
started = perf_counter()
from sympy import Matrix, Rational, symbols, diff, expand, factor

x, t, z, k = symbols("x t z k")
b = Matrix([x, x*t])
jac = b.jacobian([x, t])
assert jac.det() == x
sphere_rank = Matrix([[1, 0, 0], [t, x, 0], [2*x, 2*t, 2*z]]).det()
assert sphere_rank == 2*x*z
assert b.subs(x, 0) == Matrix([0, 0])

g = (t*t-x)**2 + x*x/Rational(4)
f = x*g
fx, ft = diff(f, x), diff(f, t)
assert expand(fx - Rational(15,4)*(x-Rational(2,5)*t*t)*
              (x-Rational(2,3)*t*t)) == 0
assert expand(ft - 4*x*t*(t*t-x)) == 0
assert expand(g - t**4/Rational(5) -
              Rational(5,4)*(x-Rational(4,5)*t*t)**2) == 0
assert expand(g - x*x/Rational(4) - (t*t-x)**2) == 0

# H=(x*g,t*sqrt(g)); its second coordinate squared is t^2*g.
u, v_squared = x*g, t*t*g
g_after_H = v_squared**2 - 2*u*v_squared + Rational(5,4)*u*u
assert expand(g_after_H - g**3) == 0

P = 1-4*k+Rational(15,4)*k*k
values = [P.subs(k, q) for q in [Rational(1,4),Rational(1,2),1]]
assert values == [Rational(15,64),Rational(-1,16),Rational(3,4)]
assert expand(fx.subs(x,Rational(2,5)*t*t)) == 0
assert factor(ft.subs(x,Rational(2,5)*t*t)) == Rational(24,25)*t**5

print("BLOWDOWN b(x,t)=(x,xt)")
print("JACOBIAN DETERMINANT:", jac.det())
print("SPHERE CHART RANK CERTIFICATE:", sphere_rank)
print("COLLAPSED FIBRE: x=0 maps to (0,0)")
print("PRODUCT TEST: g=(t^2-x)^2+x^2/4, f=x*g")
print("f_x =", factor(fx))
print("f_t =", factor(ft))
print("WEIGHTED HOMEOMORPHISM: g(H)=g^3")
print("POSITIVE BOUNDS: g>=x^2/4 and g>=t^4/5")
print("RETRACTION SIGN POLYNOMIAL VALUES:", values)
print("a_f WITNESS: x=(2/5)t^2, f_x=0, f_t=(24/25)t^5")
print("PASS: both exact algebraic obstruction certificates")
print(f"RUNTIME_SECONDS: {perf_counter()-started:.9f}")
