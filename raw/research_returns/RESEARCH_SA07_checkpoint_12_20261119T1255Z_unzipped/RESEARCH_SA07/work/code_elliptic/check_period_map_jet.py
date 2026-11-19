#!/usr/bin/env python3
"""Exact actual-period jet maps and the chain-rule sign in BPT2026 §4.2.3.

This verifies algebraic identities, not pointwise transcendence.
"""
from time import perf_counter
import sympy as s

started = perf_counter()
m, delta, K, L, Kp, Lp = s.symbols('m delta K L Kp Lp', nonzero=True)
M = m*(1-m)
p = (1-2*m)/M
q = -1/(4*M)
Kpp = -p*Kp-q*K
Lpp = -p*Lp-q*L
W = K*Lp-Kp*L
tau = s.I*L/K
taup = s.I*W/K**2
taupp = -p*taup-2*Kp*taup/K
r = Kp/K+Lp/L
assert s.factor(r-(taup/tau-taupp/taup-p)) == 0
h = delta*(M*r-(2*m-1)/3)
c = -delta*M*W/(K*L)
assert s.factor(c+delta*M*taup/tau) == 0
assert s.factor(h-delta*(M*(taup/tau-taupp/taup)+s.Rational(2,3)*(2*m-1))) == 0
assert s.factor(taupp/taup-((s.Rational(2,3)*(2*m-1)-(h+c)/delta)/M)) == 0

# Formal chain rule d/dj=(1/j')d/dtau.
t = s.symbols('t')
j = s.Function('j')(t)
J = s.diff(j,t)
J2 = s.diff(j,t,2)
v1 = s.sqrt(J)
v2 = t*s.sqrt(J)
R1 = J2/J**s.Rational(3,2)
R2plus = t*R1+2/s.sqrt(J)
R2printed = t*R1-2/s.sqrt(J)
assert s.simplify(2*s.diff(v1,t)/J-R1) == 0
assert s.simplify(2*s.diff(v2,t)/J-R2plus) == 0
assert s.simplify(2*s.diff(v2,t)/J-R2printed-4/s.sqrt(J)) == 0

# Modular transformation of the corrected pair, using ad-bc=1.
a,b,cc,d,x,z = s.symbols('a b cc d x z', nonzero=True)
v = cc*t+d
R1g = v*x+2*cc/z
R2 = t*x+2/z
assert s.expand(R1g-(cc*R2+d*x)) == 0
R2g = (a*t+b)*R1g/v+2/(v*z)
numerator = s.factor((R2g-(a*R2+b*x))*v*z/2)
assert s.expand(numerator-(1-a*d+b*cc)) == 0

# At fixed algebraic m, the map (r,s2) <-> (h,c^2) is invertible.
r0,s2,c2 = s.symbols('r0 s2 c2')
h0 = delta*(M*r0-(2*m-1)/3)
s2_formula = (r0**2-2*p*r0-4*q)/2-c2/(2*delta**2*M**2)
c2_recovered = delta**2*M**2*(r0**2-2*p*r0-4*q-2*s2)
assert s.factor(c2_recovered.subs(s2,s2_formula)-c2) == 0
assert s.factor((h0/delta+(2*m-1)/3)/M-r0) == 0

print('PASS actual tau first/second jet, h and c identities')
print('PASS BPT2026 displayed derivative correction: R2 has plus 2/sqrt(jprime)')
print('PASS corrected pair transforms as standard SL2 pair')
print('PASS exact coefficient-field recovery (r,s2) <-> (h,c^2)')
print('CHECKS',11)
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
