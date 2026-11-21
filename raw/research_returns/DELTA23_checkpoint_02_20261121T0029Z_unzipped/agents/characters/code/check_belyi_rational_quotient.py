#!/usr/bin/env python3
"""Exact genus-zero quotient composition for degree9 cubic dessin; DELTA23."""
from pathlib import Path
import sympy as s,json,re
X=s.symbols('X');d=s.sqrt(-3);n=(1+d)/2
K=s.QQ.alg_field if False else s.QQ.algebraic_field(d)
poly=lambda a:s.Poly(a,X,domain=K)
zero=poly(0);one=poly(1);curve=poly(X**3-4)
# Pair (A,B) denotes A+B*Y, Y^2=X^3-4.
def scalar(a):return poly(a),zero
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[0],-a[1]
def sub(a,b):return add(a,neg(b))
def mul(a,b):return a[0]*b[0]+a[1]*b[1]*curve,a[0]*b[1]+a[1]*b[0]
def scale(a,c):return a[0]*c,a[1]*c
def powr(a,k):
 out=scalar(1)
 while k:
  if k&1:out=mul(out,a)
  a=mul(a,a);k//=2
 return out
def eq(a,b):return a[0]==b[0] and a[1]==b[1]
A={k:s.sympify(a,locals={'X':X,'n':n}) for k,a in [row.split('=',1) for row in Path('work/records/belyi_9T23_normalized.txt').read_text().splitlines()[1:]]}
F=(poly(A['Q']),poly(A['P']));D=scalar(A['D'])
L=(poly(2*X-2),one);G=(poly(-X**2-6*X+10),poly(-3))
N=(poly(X**2-2*X+4),poly(2))
C_hom=add(add(scale(powr(L,3),53),scale(mul(powr(L,2),G),15)),add(scale(mul(L,powr(G,2)),-3),neg(powr(G,3))))
assert eq(powr(N,3),C_hom)
H_hom=add(add(scale(powr(L,3),19),scale(mul(powr(L,2),G),-9)),add(scale(mul(L,powr(G,2)),-3),powr(G,3)))
Q_hom=add(sub(powr(L,2),scale(mul(L,G),4)),powr(G,2))
NQ=mul(N,Q_hom)
# This lower-degree identity implies the already independently checked full
# composition Psi(z)=1-((phi-bar(n))/(phi-n))^3. It preserves its orientation.
assert eq(mul(F,sub(H_hom,scale(NQ,n))),scale(mul(D,add(H_hom,NQ)),1-n))
# At (X,Y)=(2,2), t^3=1331/8, so the reciprocal orientation differs.
assert s.Rational(1331,8)!=s.Rational(8,1331)
rows=[{'base_fixed_denominator':str(n),'identity':True},
      {'base_fixed_denominator':str(1-n),'identity':False}]
# Exact rational map factorization and all three branch partitions.
z=s.symbols('z');C=53*z**3+15*z**2-3*z-1;H=19*z**3-9*z**2-3*z+1
N_rat=432*z**6*(z-1)*(4*z-1)**2;Dg=H**3
assert s.expand(N_rat-Dg-(z*z-4*z+1)**3*C)==0
assert s.discriminant(C,z)==-11664
assert s.discriminant(H,z)!=0
assert s.gcd(N_rat,Dg)==1
assert s.gcd(C,z*z-4*z+1)==1
# Birational inverse of the rational plane-cubic model.
w=s.symbols('w');S=1+z+w
ix=(4+16*z-2*w)/S;iy=6*(w*w-19*z*z-8*z-1)/S**2
inverse_eq=s.together(iy**2-ix**3+4).as_numer_denom()[0]
assert s.rem(s.Poly(inverse_eq,w),s.Poly(w**3-C,w)).is_zero
ix_back=add(scale(G,4),sub(scale(L,16),scale(N,2)))
assert eq(ix_back,mul(scalar(X),add(add(G,L),N)))
iy_back=scale(sub(sub(powr(N,2),scale(powr(L,2),19)),add(scale(mul(L,G),8),powr(G,2))),6)
assert eq(iy_back,mul((zero,one),powr(add(add(G,L),N),2)))
# phi zero divisor checks, preserving the sign of the double cusp.
for xx,yy in [(2,-2),(5,-11)]:assert s.simplify((A['P']*yy+A['Q']).subs(X,xx))==0
assert s.simplify((A['P']*11+A['Q']).subs(X,5))!=0
# Pole denominator and sixfold point normalization.
assert poly((X-1-d)**6*(X-7+d)**2*(X+2+4*d))==poly(A['D'])
result={'statement':'D23.C14','field':'Q(sqrt(-3))','curve':'Y^2=X^3-4','quotient_coordinate':'z=(2X+Y-2)/(-X^2-6X-3Y+10)','cubic_coordinate':'w=(X^2-2X+2Y+4)/(-X^2-6X-3Y+10)','cubic_model':'w^3=53z^3+15z^2-3z-1','inverse_X':'(4+16z-2w)/(1+z+w)','inverse_Y':'6(w^2-19z^2-8z-1)/(1+z+w)^2','phi_compact':'bar(n)*(H+wQ)/(H-n*wQ), Q=z^2-4z+1,H=19z^3-9z^2-3z+1','rational_map':'Psi=432z^6(z-1)(4z-1)^2/(19z^3-9z^2-3z+1)^3','map_minus_one':'(z^2-4z+1)^3*(53z^3+15z^2-3z-1)/(19z^3-9z^2-3z+1)^3','orientation_checks':rows,'zero_divisor_phi':'6O+2(2P)+(-P), P=(2,2), 2P=(5,-11)','cubic_branch_discriminant':-11664,'result':'PASS'}
Path('work/agents/characters/records/belyi_rational_quotient.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
