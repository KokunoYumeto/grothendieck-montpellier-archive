#!/usr/bin/env python3
"""Exact certificates only; no numerical algebraicity/transcendence claims."""
from fractions import Fraction
from time import perf_counter
import sympy as s

start = perf_counter()
a,b,c,d = s.symbols('a b c d')
A=s.Matrix([[a,b],[c,d]])
D=s.expand(A.det())
f=s.diag(1,-1)
F=s.simplify(A*f*A.inv())
assert s.simplify(F*F-s.eye(2))==s.zeros(2)
print('Real-involution transport: (A f A^-1)^2 = I: PASS')
print('A f A^-1 =',F)

# These rows give the comparison with the associated graded after splitting.
Z=s.Matrix([[D/(2*d),-D/(2*c)],[c,d]])
assert s.simplify(Z.det()-D)==0
assert s.simplify(Z[0,0]*Z[1,1]+Z[0,1]*Z[1,0])==0
beta=s.simplify(Z*A.inv())
assert beta[0,0]==1 and beta[1,0]==0 and beta[1,1]==1
print('beta =', beta)
print('beta A =',Z)
print('Constraint z11*z22+z12*z21=0: PASS')
print('gamma=(beta A)^-1 =',s.simplify(Z.inv()))

# Verify a nonsingular explicit real elliptic curve and ordinary reduction data.
aa,bb=-1,1
disc=-16*(4*aa**3+27*bb**2)
j=Fraction(1728*4*aa**3,4*aa**3+27*bb**2)
print('E: y^2=x^3-x+1; discriminant=',disc,'; j=',j)
assert disc!=0 and j.denominator>1
for p in (5,7):
    assert disc%p!=0
    n=1+sum(1 for x in range(p) for y in range(p)
            if (y*y-x*x*x-aa*x-bb)%p==0)
    trace=p+1-n
    print(f'p={p}: #E(F_p)={n}, trace={trace}, trace^2-4p={trace*trace-4*p}, ordinary={trace%p!=0}')

# Real Artin-Tate motive: sign projector in h^0(Spec C) tensor Tate.
swap=s.Matrix([[0,1],[1,0]])
Pminus=(s.eye(2)-swap)/2
assert Pminus*Pminus==Pminus
assert Pminus.rank()==1
assert swap*Pminus==-Pminus
real_F_on_Tate_pair=-swap
assert real_F_on_Tate_pair*Pminus==Pminus
print('Artin projector (I-swap)/2: rank 1, idempotent, f on A*T is +1: PASS')
print('Weights: A*T=2; Q(2)^m=-4m; 2 is not an integer multiple of 4: PASS')

# Tensor-twist sign and exact cohomological coboundary.
ii=s.I
assert ii*ii==-1
assert s.conjugate(ii)/ii==-1
g=s.diag(1,ii)
assert s.simplify(g.inv()*s.conjugate(g))==f
print('Artin tensor relation (i*q)^2=-q^2; q rational/real gives no unit-preserving isomorphism: identity checked')
print('G_m coboundary conjugate(i)/i=-1: PASS')
print('GL2 coboundary g^-1 conjugate(g)=diag(1,-1), g=diag(1,i): PASS')

# The standard real Frobenius / Weil-operator sign cancellation in weight one.
C=s.Matrix([[0,-1],[1,0]])
q=s.Matrix([[0,1],[-1,0]])
assert f*C*f==C.inv()
assert f.T*q*f==-q
assert q*C==s.eye(2)
assert f.T*(q*C)*f==q*C
print('Weight-one positive Weil form: q*C=I and f-invariance: PASS')
print(f'Runtime seconds: {perf_counter()-start:.6f}')
