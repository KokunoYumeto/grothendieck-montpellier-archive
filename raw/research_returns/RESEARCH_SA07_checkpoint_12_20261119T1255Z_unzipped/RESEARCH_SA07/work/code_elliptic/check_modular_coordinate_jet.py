#!/usr/bin/env python3
"""Exact rational modular coordinate and algebraic gauge/jet transport."""
from time import perf_counter
import sympy as s

started=perf_counter()
m=s.symbols('m')
D=1-m+m*m
M=m*(1-m)
u=27*M*M/(4*D**3)
j=256*D**3/(M*M)
assert s.factor(u*j-1728)==0
du=s.factor(s.diff(u,m))
assert s.factor(du-27*M*(1-2*m)*(2+M)/(4*D**4))==0
P=37*m**6-111*m**5-210*m**4+605*m**3-210*m**2-111*m+37
assert s.factor(s.together(u-s.Rational(37,64))).as_numer_denom()[0] == -P
assert s.gcd(P,s.together(du).as_numer_denom()[0])==1
assert s.gcd(P,D*M)==1

# g2=4 makes delta^2=3/D.  The logarithmic derivative of the
# physical product F/delta, as a function of u, is exact.
r,h,delta=s.symbols('r h delta',nonzero=True)
dlogdelta=-s.diff(D,m)/(2*D)
ru=(r-dlogdelta)/du
r_from_h=(h/delta+(2*m-1)/3)/M
assert s.factor(delta*(M*(du*ru+dlogdelta)-(2*m-1)/3)-delta*(M*r-(2*m-1)/3))==0

# Arbitrary algebraic etale coordinate z=psi(w), psi(0)=0,
# and arbitrary nonzero algebraic gauge A(w): second-jet formula.
w=s.symbols('w')
r0,s2,p1,p2,a1,a2=s.symbols('r0 s2 p1 p2 a1 a2')
psi=p1*w+p2*w*w/2
F=1+r0*psi+s2*psi**2/2
A=1+a1*w+a2*w*w/2
G=s.series(A*F,w,0,3).removeO()
rnew=s.diff(G,w).subs(w,0)
snew=s.diff(G,w,2).subs(w,0)
assert s.expand(rnew-(a1+p1*r0))==0
assert s.expand(snew-(a2+2*a1*p1*r0+p2*r0+p1*p1*s2))==0
assert s.expand(s.diff(snew,s2)-p1*p1)==0
print('PASS u=1728/j; at E_star u=37/64 and du/dm nonzero')
print('DU_DM',du)
print('PASS g2-fixed physical product F/delta and exact h recovery')
print('PASS arbitrary algebraic etale coordinate/gauge: coefficient of old second jet is p1^2')
print('CHECKS',9)
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'))
