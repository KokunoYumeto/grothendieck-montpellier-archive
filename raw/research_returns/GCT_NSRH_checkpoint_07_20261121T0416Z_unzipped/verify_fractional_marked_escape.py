#!/usr/bin/env python3
"""Exact block-identity checks for the fractional marked-trace model.
The all-extension nonvanishing and scope statements are proved in the report.
"""
import sys
import sympy as S

t, v = S.symbols("t v")
s = S.sqrt(2)
D = (v + 1/v)**2
Delta = S.factor((D-1)*(D-4)/D**2)
eta = S.Rational(189, 625)
assert S.cancel(Delta.subs(v, 2)-eta) == 0

g = 2*(1+t)**2
h = S.factor(eta*g/Delta.subs(v, t*t))
lam = h/2 - 1 - 2*s
u = 1 + (g-h)/20
h_reduced = 2*eta*(t**4+1)**4/((t-1)**2*(t*t+1)**2*(t**8+t**4+1))
assert S.cancel(h-h_reduced) == 0
assert S.cancel(Delta.subs(v,t*t)*h-eta*g) == 0
assert S.cancel(36+20*u+h-(56+g)) == 0

assert S.simplify(h.subs(t,s)-(6+4*s)) == 0
assert S.simplify(lam.subs(t,s)-2) == 0
assert S.simplify(u.subs(t,s)-1) == 0
assert S.simplify(h.subs(t,-1)-S.Rational(126,625)) == 0
assert S.simplify(u.subs(t,-1)-S.Rational(6187,6250)) == 0
assert S.simplify(lam.subs(t,-1)+S.Rational(562,625)+2*s) == 0

F4 = S.diag(1,s,s,lam)
Ev = S.kronecker_product(S.Matrix([[0,1],[0,0]]), S.eye(2))
fb = F4.subs(t,s).applyfunc(S.simplify)
minus_plus = S.Matrix([0,0,1,0])
plus_plus = S.Matrix([1,0,0,0])
assert (fb*Ev-Ev*fb)*minus_plus == (1-s)*plus_plus

Dt = D.subs(v,t*t)
a = Dt-2
P1 = S.Matrix([[Dt,0],[a,0]])
P2 = S.Matrix([[0,a],[0,Dt]])
F8 = S.kronecker_product(F4,S.eye(2))
for Pi in (P1,P2):
    Ri = S.kronecker_product(S.eye(4),Pi)
    assert (F8*Ri-Ri*F8) == S.zeros(8)
assert S.simplify(F4.det()-2*lam) == 0

print("Python:",sys.version.split()[0])
print("SymPy:",S.__version__)
print("Cancelled h:",h)
print("At collision (h,u,lambda):",
      tuple(S.simplify(x.subs(t,-1)) for x in (h,u,lam)))
print("At base (h,u,lambda):",
      tuple(S.simplify(x.subs(t,s)) for x in (h,u,lam)))
print("At t=2, lambda:",S.simplify(lam.subs(t,2)))
print("n>=3 lambda lower bound:",
      S.simplify(eta*(1+2*s)**2-1-2*s))
print("Marked trace, identity trace, right commutation, left failure: PASS")
print("All-n nonvanishing is established separately by the report's inequalities.")

