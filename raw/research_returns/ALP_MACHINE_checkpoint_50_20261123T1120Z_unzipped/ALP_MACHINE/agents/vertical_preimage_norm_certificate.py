#!/usr/bin/env python3
"""Exact arithmetic and normalization diagnostics for ALP-LIFT-38."""
from datetime import datetime,timezone
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
import sympy as s

checks=0
def check(value):
 global checks
 assert value
 checks+=1
def kap(j,q):
 z=F(1)
 for i in range(1,j+1):z*=1-F(1,q**i)
 return z

# General-measure scaling with all local Gram measures retained.
a0,a1,a2,z0,z1=s.symbols('a0 a1 a2 z0 z1',positive=True)
check(s.simplify(4*a0*a1**2*a2*(z0/a0)*(z1/a1)-4*a1*a2*z0*z1)==0)
check(s.simplify((a2/a0)*(a0*a1)**2-a0*a1**2*a2)==0)

# The Q string is restored precisely once, then divided only in the local factor.
phase_cases=0
for q in (2,3,5,7):
 for r in (1,2,3):
  for t in (r,r+1,r+3):
   b=r+t;N=b+t
   c0=kap(b,q)/kap(t,q);c1=kap(N,q)/kap(t,q)
   A=q**(r*t)*kap(b,q)/(kap(r,q)*kap(t,q))
   B=q**(2*r*t)*kap(N,q)/(kap(r,q)*kap(2*t,q))
   for u,v in ((0,1),(1,1),(1,2),(2,1),(3,2)):
    z=F(u,v);cos=(1-z*z)/(1+z*z)
    labs=F(1)
    for i in range(1,t+1): labs/=1-2*cos*F(1,q**i)+F(1,q**(2*i))
    raw_pair=kap(r,q)**2*F(1,q**(3*r*t))
    composed=c0*c1*A**(-2)*B**(-1)*labs
    aq=F(1,q**(4*r*t))*kap(r,q)**3*kap(2*t,q)/kap(b,q)
    cq=F(1,q**(r*t))*kap(r,q)*kap(2*t,q)/kap(b,q)
    check(composed==aq*labs)
    check(composed/(raw_pair*labs)==cq)
    check(aq>F(1,256*q**(4*r*t)))
    check(cq>F(1,16*q**(r*t)))
    phase_cases+=1

# Direct finite-dimensional surrogate of orthogonal multiplicity summands.
# This verifies the claimed inverse operator identity, without making a theta claim.
O=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],
            [s.Rational(4,5), s.Rational(3,5)], [0,0]])
check(O.T*O==s.eye(2))
for x,y in ((2,3),(s.Rational(1,7),s.Rational(2,5)),(11,1)):
 U=O*s.diag(x,y)
 R=U*(U.T*U).inv()
 check(U.T*R==s.eye(2))
 check(R.T*R==s.diag(s.Rational(1)/s.sympify(x)**2,
                    s.Rational(1)/s.sympify(y)**2))

actual=[]
for name,a,t,f,C,Graw,Gunit,Hraw,Hunit,Hmass,Hinf in [
 ('J14',42,1759,42,277221,6433607334,149943150,6433884556,150220372,89369,65463713280),
 ('J56',168,1633,168,1171821,46338383784,3973204872,46339555606,3974376694,87227,263998748160)]:
 r=a+1;b=r+t;N=b+t
 check(C+1+Graw==Hraw and C+1+Gunit==Hunit)
 check(16*b+17*N==Hmass)
 check(8*f*F(1,2**t)<F(1,2))
 check((t+1)%2==0)
 # Each actual denominator parity agrees with k at both odd-gap edges.
 for n in (r,b):
  for l in range(n):check((n-1+l-(t+n-l))%2==0)
 check(b<2**11 and N<2**12 and 28<2**5)
 # Conservative genuine HC bounds from EG1,EG4,EG5 and DataTheta.Dpar.
 eu=2**955+2**485+28
 ellu=2**485
 check(4*ellu*(a-1)<2**495)
 check(eu+(4*a+3)*ellu+t+2<2**956)
 computed=960*f*(a*(a+1)+b*(b-1))//2
 check(computed==Hinf)
 actual.append(dict(host=name,r=r,t=t,b=b,N=N,f=f,
   raw_finite_exponent=Hraw,unit_finite_exponent=Hunit,
   mass_exponent=Hmass,formal_degree_dimension_exponent=Hinf,
   raw_total_exponent=Hraw+Hmass+Hinf,
   unit_total_exponent=Hunit+Hmass+Hinf,
   raw_Qnorm_inverse_exponent=2*r*t,
   unit_Qnorm_inverse_exponent=str(F(r*t,2))))

proof=Path(__file__).with_name('vertical_preimage_norm_bound.md')
data=dict(finding='ALP-LIFT-38',status='PASS',
 completed_utc=datetime.now(timezone.utc).isoformat(),assertions=checks,
 exact_Q_phase_cases=phase_cases,actual=actual,
 proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
 scope='Exact Haar scaling, single Euler cancellation, local factors, inverse identity, actual costs and parity/HC bounds. Formal-degree formula and global Rallis assembly require the written proof; no global theta matrix or integral preimage computation.')
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
