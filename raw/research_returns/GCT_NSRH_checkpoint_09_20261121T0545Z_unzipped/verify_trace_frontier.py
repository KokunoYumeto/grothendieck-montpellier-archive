#!/usr/bin/env python3
"""Exact identity and fixed-point certificate for F54 Parts 2--3.
Row-action blocks use P1=[[D,0],[a,0]], P2=[[0,a],[0,D]].
The all-n separation and impossibility proofs are in the accompanying report.
"""
import sys
import sympy as s

v, a = s.symbols("v a")
delta = v + v**-1
D = delta**2
Delta = s.factor((D-1)*(D-4)/D**2)
k = s.Rational(2500,189)
aa = 3-v
cc = -v**3+2*v**2+4*v-8+k*Delta
dd = cc+k*Delta
zz = 6*v**3-6*v**2-14*v+30-6*k*Delta
SH = 1+v+2*v**2+2*v**3
SK = 20+4*v+16*v**2+4*v**3
assert s.cancel(aa+zz+2*cc+2*dd-SH) == 0
assert s.cancel(20*aa+4*zz+16*cc+4*dd-SK) == 0
assert tuple(s.cancel(f.subs(v,2)) for f in (aa,zz,cc,dd)) == (1,2,4,8)
assert tuple(s.cancel(f.subs(v,1)) for f in (aa,zz,cc,dd)) == (2,16,-3,-3)

P1 = s.Matrix([[D,0],[a,0]])
P2 = s.Matrix([[0,a],[0,D]])
Z = (P1+P2)/D-(P1*P2+P2*P1)/D**2
assert (Z-(1-a*a/D**2)*s.eye(2)).applyfunc(s.cancel) == s.zeros(2)
assert (P1*P1-D*P1).applyfunc(s.cancel) == s.zeros(2)
z1, z2 = (D-1)/D, 4*(D-1)/D**2
X = Z*(z1*s.eye(2)-Z)/z2
assert X.subs(a,delta).applyfunc(s.cancel) == s.zeros(2)
assert (X.subs(a,D-2)-Delta*s.eye(2)).applyfunc(s.cancel) == s.zeros(2)

print("Python:", sys.version.split()[0])
print("SymPy:", s.__version__)
print("Delta factorization:", Delta)
print("H identity trace residual: 0")
print("K identity trace residual: 0")
print("N(a) central Z, quadratic P1 relation, and marked X branch identities: PASS")
for value in (1,2,4,8):
    print("v =", value, "Delta =", s.cancel(Delta.subs(v,value)),
          "(a,z,c,d) =", tuple(s.cancel(f.subs(v,value)) for f in (aa,zz,cc,dd)))
print("v=4, d-a =", s.cancel((dd-aa).subs(v,4)))
print("v=4, lower bound for z =", s.cancel((6*v**3-6*v**2-14*v+30-6*k).subs(v,4)))
print("v=8, upper bound for d-a =", s.cancel((-v**3+2*v**2+5*v-11+2*k).subs(v,8)))
print("v=4, marked-H retuning residual =", s.cancel((2*Delta*dd-2*Delta.subs(v,2)*v**3).subs(v,4)))
print("These exact computations supplement, but do not replace, the symbolic proofs in the report.")

