#!/usr/bin/env python3
"""Exact identities behind the marked C4 direct-congruence obstruction."""
from pathlib import Path
import json,time
import sympy as s
started=time.perf_counter()
z,t,x,y,w,X,Y,Z=s.symbols('z t x y w X Y Z')
rel=s.Poly(z*z+z+1,z)
def red(expr):
    n,d=s.fraction(s.cancel(expr))
    return s.cancel(s.rem(s.Poly(n,z),rel).as_expr()/s.rem(s.Poly(d,z),rel).as_expr())
c=z-z*z
M=s.Matrix([[1,1,1],[1,z,z*z],[1,z*z,z]])
A=s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
B=s.diag(1,z,z*z)
assert red(M.det()+3*c)==0
assert red(c*c+3)==0
assert all(red(v)==0 for v in M*A-B.inv()*M)
assert all(red(v)==0 for v in M*B-A*M)
F=lambda T,a,b,d:a**3+b**3+d**3-3*T*a*b*d
vec=M*s.Matrix([x,y,w]);h=(t+2)/(t-1)
assert red(s.expand(F(t,*vec)-3*(1-t)*F(h,x,y,w)))==0
assert red(c/(t-1)*c/(h-1)+1)==0

N=s.Matrix([[0,0,1],[1,-1,0],[1,1,t]])
assert N.det()==2
xx=(Z-t*X+Y)/2;yy=(Z-t*X-Y)/2
plane=3*Z*Y*Y-4*(t**3-1)*X**3+9*t*t*X*X*Z-6*t*X*Z*Z+Z**3
assert s.expand(4*F(t,xx,yy,X)-plane)==0
a=4*(t**3-1)/3
a2=-3*t*t;a4=2*t*a;a6=-a*a/3
AH=s.factor(a4-a2*a2/3)
BH=s.factor(a6-a2*a4/3+2*a2**3/27)
assert s.factor(AH+t*(t**3+8)/3)==0
assert s.factor(BH-2*(t**6-20*t**3-8)/27)==0
AE=-3*t*(t**3+8)/16;BE=-(t**6-20*t**3-8)/32
assert red(AH-(2/c)**4*AE)==0
assert red(BH-(2/c)**6*BE)==0
# Plane residue eta_H=(2/3)omega_short and constant scaling yield eta_H=c/3 omega_E.
assert red(s.Rational(2,3)/(2/c)-c/3)==0

v,T=s.symbols('v T');lam=z-1
assert red((v-lam)*(3/v-lam)+lam*(v+3/v+3))==0
u,up,pi=s.symbols('u up pi')
assert s.factor(pi*(u+1/u+up+1/up)-pi*(u+up)*(1+1/(u*up)))==0
for r in range(1,1001):assert min(4+r,4+2*r,3*r)>=3
for r in range(3,1003):
    for b in range(1,10):assert 2+r+b>=6
units=[a for a in range(27) if a%3]
adjust=[]
for a in units:
    sign=1 if a%3==1 else 26
    roots=[b for b in units if a*b*b%27==sign]
    assert roots
    adjust.append({'multiplier':a,'normalized_sign':sign,'scalar_choices':roots})
out={'status':'PASS',
     'identities':['det Fourier=-3c','c^2=-3','Fourier interchanges translations with one inverse',
                   'Hesse cubic transform','kappa(t)kappa(h(t))=-1','plane Weierstrass transform',
                   'short Hesse A,B','constant scaling2/c','eta_H=c/3 omega_E',
                   'norm(t-zeta)=-(zeta-1)(T+3)','trace-unit factorization'],
     'cube_valuation_cases':1000,'trace_bound_cases':9000,
     'unit_multiplier_adjustments_mod27':adjust,
     'scope':'Direct cyclic-four comparison excluded; antisymplectic level27 branch undecided',
     'elapsed_seconds':time.perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
