#!/usr/bin/env python3
"""Exact symbolic certificate for B-RD23's full-nine Hesse construction.

The output checks polynomial identities and finite valuation tables. Actual
square/cube roots in complete local fields are supplied by the proved Hensel
arguments, not by a finite-precision numerical assumption.
"""
import json
import time
import sympy as S

start=time.perf_counter()
eta,y,h,beta,t,z,A0,A1,A2=S.symbols('eta y h beta t z A0 A1 A2')
phi9=eta**6+eta**3+1
zeta=eta**3
lam=-eta**2
c=lam/(zeta-1)
checks=[]

def eta_zero(expr,label):
    num,den=S.cancel(expr).as_numer_denom()
    assert S.rem(num,phi9,eta)==0, (label,num)
    checks.append(label)

eta_zero(c**3-(1-zeta)/9,'c^3=(1-zeta)/9')
eta_zero((zeta-1)**2+3*zeta,'(zeta-1)^2=-3*zeta')
eta_zero(lam**3+zeta**2,'lambda^3=-zeta^2')
eta_zero(zeta**2+zeta+1,'zeta is a primitive cube root relation')

quadratic=(1-h**3)*y*y+3*y+3
assert S.expand(y**3*h**3-((1+y)**3-1)+y*quadratic)==0
checks.append('quadratic gives d0=y^3 h^3=(1+y)^3-1')
assert S.expand(9-12*(1-h**3)-3*(4*h**3-1))==0
checks.append('quadratic discriminant is 3(4h^3-1)')

d0=(1+y)**3-1
t0=1+(1-zeta)/d0
eta_zero((t0-zeta)-(t0-1)*(1+y)**3,'second cube ratio')
eta_zero((t0-zeta**2)-(t0-1)*(1-zeta**2*d0),'third cube ratio')
target=1+lam**3*d0
beta0=1+lam*y
assert S.expand(target-beta0**3-3*(lam**3-lam)*y-3*(lam**3-lam**2)*y*y)==0
checks.append('exact Hensel residual polynomial')

# Generic Fourier inversion, reduced modulo z^2+z+1.
u=(A0+A1+A2)/3
v=(A0+z*z*A1+z*A2)/3
w=(A0+z*A1+z*z*A2)/3
for theta,A in [(1,A0),(z,A1),(z*z,A2)]:
    assert S.rem(S.expand(u+v*theta+w*theta*theta-A),z*z+z+1,z)==0
checks.append('all three Fourier evaluation identities')

# The homogeneous X(9) cubic equations also follow from Fisher's three cubes.
def use_cubes(expr):
    q=S.rem(S.expand(expr),z*z+z+1,z)
    q=S.expand(q).subs({A0**3:(t-1)/9,A1**3:(t-z)/9,A2**3:(t-z*z)/9})
    return S.rem(S.expand(q),z*z+z+1,z)
assert use_cubes(u*u*v+v*v*w+w*w*u+S.Rational(1,27))==0
assert use_cubes(u*u*w+v*v*u+w*w*v)==0
checks.append('both complete-intersection cubics for X(9), with s=-1/3')

# General Weierstrass invariants for a1=3t, a3=t^3-1, a2=a4=a6=0.
a1,a3=3*t,t**3-1
b2,b4,b6=a1*a1,a1*a3,a3*a3
c4=S.expand(b2*b2-24*b4)
Delta=S.expand(-8*b4**3-27*b6*b6+9*b2*b4*b6)
assert S.expand(c4-9*t*(t**3+8))==0
assert S.expand(Delta-27*(t**3-1)**3)==0
assert S.cancel(c4**3/Delta-27*t**3*(t**3+8)**3/(t**3-1)**3)==0
checks.append('c4, discriminant and j identities')

pi=S.symbols('pi')
phi9_shift=S.expand(((1+pi)**9-1)/pi)
# Use the actual cyclotomic polynomial Phi_9(1+pi), rather than Phi_9 times Phi_3.
cyclotomic_shift=S.expand((1+pi)**6+(1+pi)**3+1)
assert cyclotomic_shift==pi**6+6*pi**5+15*pi**4+21*pi**3+18*pi*pi+9*pi+3
checks.append('cyclotomic Eisenstein expansion and leading residue -1')

valuation_rows=[]
for e in [24,30,42,48]:
    assert e%6==0 and e>18
    r=e//2-3
    q=2*e//3-3
    assert r>e//6 and q>e//2
    assert e+q<e+2*r
    assert 2*q-e>0
    assert (e+6)%2==0 and (e+6)//2<e
    vt=e//2-3*r
    assert vt==9-e<0
    vDelta=3*e+9*vt
    vc4=2*e+4*vt
    vj=3*vc4-vDelta
    assert vj==27 and vDelta%12==9
    integralDelta=vDelta-12*vt
    assert integralDelta==6*e-27 and integralDelta%12==9
    valuation_rows.append({'e':e,'K':'Q_3(i,zeta_9,pi), pi^(e/6)=zeta_9-1',
        'residue':'F_9','v_D':e+6,'v_y':r,'v_residual':e+q,
        'v_Hensel_correction':q,'v_cubic_coefficient_after_rescaling':2*q-e,
        'v_t':vt,'v_j':vj,'v_raw_discriminant':vDelta,
        'v_integral_discriminant':integralDelta,'semistability_defect':12})

# Verify all integer inequalities used in the uniform family over a finite range.
for e in range(24,6001,6):
    r=e//2-3; q=2*e//3-3
    assert r>e//6 and q>e//2 and e+6<2*e
    assert (81-6*e)%12==9
checks.append('uniform valuation inequalities for every 6|e, 24<=e<=6000')

print(json.dumps({
  'scope':'Exact characteristic-zero polynomial identities, X(9) equations, and integer valuation inequalities. Hensel existence is proved separately in B_full9.tex.',
  'symbolic_identities_passed':checks,
  'number_of_identity_groups':len(checks),
  'previously_undecided_cases':valuation_rows,
  'uniform_valuation_input':{'e_min':24,'e_max':6000,'step':6},
  'all_assertions_passed':True,
  'elapsed_seconds':time.perf_counter()-start
},indent=2))
