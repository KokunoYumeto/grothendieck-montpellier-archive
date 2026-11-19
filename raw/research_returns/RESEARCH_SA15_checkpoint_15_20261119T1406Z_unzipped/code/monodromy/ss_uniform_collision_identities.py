#!/usr/bin/env python3
"""Exact algebra supporting the uniform collision-incidence candidate.

The program does not certify the geometric dimension, flatness or
irreducibility arguments; those are separate written proofs.
"""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp

started=perf_counter()
F,T,U,v,h,A,B,k,r,p,e,Z=sp.symbols('F T U v h A B k r p e Z')
variables=(F,T,U,v,h,A,B,k,r,p,e,Z)
def mod2(expression, vv=variables):
    return sp.Poly(sp.expand(expression),*vv,modulus=2).as_expr()
q=h*v*v+h*h*v+U**3+B*h*h*U+F*F*T+A*h*F*F+F*T*T
AQ=sp.Matrix([[0,1,0,0,A],[1,0,0,0,0],[0,0,1,0,0],
              [0,0,0,0,1],[0,0,B,1,0]])
zz=sp.Matrix([F,T,U,v,h])
assert mod2((zz.applyfunc(lambda x:x*x).T*AQ*zz)[0]-q)==0
assert mod2(AQ.det())==1
assert all(mod2(sp.diff(q,z)-(AQ.T*zz.applyfunc(lambda x:x*x))[i])==0
           for i,z in enumerate(zz))

# Eliminate the nonzero translated value and the limiting first value.
vplane=r*T+e*h+p*k*h+Z*U
restricted=mod2(q.subs({F:k*h,v:vplane},simultaneous=True))
CP=sp.Matrix([[0,0,r*r+k],[0,1,Z*Z],
              [r+k*k,Z+B,(e+p*k)**2+(e+p*k)+A*k*k]])
tt=sp.Matrix([T,U,h])
assert mod2(restricted-(tt.applyfunc(lambda x:x*x).T*CP*tt)[0])==0
assert mod2(CP.det()-(k+r*r)*(k*k+r))==0
ordinary_limit=mod2(q.subs({h:0,v:0},simultaneous=True))
assert ordinary_limit==mod2(U**3+F*F*T+F*T*T)
CI=sp.Matrix([[0,1,0],[1,0,0],[0,0,1]])
assert CI.det()==-1
flex_limit=mod2(q.subs({A:0,B:0,F:k*h,T:k*h,v:h},simultaneous=True))
assert flex_limit==U**3

# The six first-jet rows at O and at an arbitrary finite translation have
# an explicit unit minor; no finite-field specialization is used.
a,b,c,d=sp.symbols('a b c d')
pp=sp.Matrix([1,a,b]);qq=sp.Matrix([1,c,d])
dp=sp.Matrix([0,1,a*a]);dq=sp.Matrix([0,1,c*c])
rows=[]
for j in (8,5,7):rows.append([int(i==j) for i in range(9)])
for left,right in ((pp,qq),(dp,qq),(pp,dq)):
    rows.append(list(sp.kronecker_product(left,right)))
jets=sp.Matrix(rows)
minor=jets[:,[8,5,7,0,3,1]]
assert sp.Poly(minor.det(),a,b,c,d,modulus=2).as_expr()==1

# Actual rational elliptic addition to order three in the flex case.
# In Y=1 coordinates z+z^2=t^3, and the finite flex has c^4+c=0.
t=sp.symbols('t')
gb=sp.groebner([d*d+d+c**3,c**4+c],d,c,modulus=2)
def flexred(expr):return gb.reduce(sp.expand(expr))[1]
z=t**3+t**6+t**12
den=t+c*z
numx=z*(1+d*z)**2+t*den**2+c*z*den**2
xc=c+t+c*c*t*t
yc=d+c*c*t+c*t*t+t**3
numy=(1+d*z)*numx+den**3+(1+d*z)*t*den**2+z*den**3
for expr,bound in ((numx-xc*z*den**2,9),(numy-yc*z*den**3,10)):
    for exponent in range(bound):
        assert flexred(sp.expand(expr).coeff(t,exponent))==0
ell=sp.expand(d*d+c*c*xc+yc)
assert all(flexred(ell.coeff(t,i))==int(i==3) for i in range(4))
# Check the actual section on both branches, rather than asserting its
# already simplified coefficient.  At O a local section basis is (z,t,1).
C=T+h*a; EE=U+h*c*c; DD=v+U*c+h*d*d+F*a*a
BB=T*c*c+EE*a; AA=T*d*d+DD*a+F*b
SS=sp.Matrix([[AA,BB,C],[DD,EE,h],[F,0,0]])
gf=sp.groebner([b*b+b+a**3,d*d+d+c**3,a**4+a,c**4+c],
                b,d,a,c,F,T,U,v,h,k,modulus=2)
def bothflexred(expr):return gf.reduce(sp.expand(expr))[1]
local_first=sp.Matrix([k**3*t**9,k*t**3,1])
local_second=sp.Matrix([z,t,1])
source_series=sp.expand((local_first.T*SS*local_second)[0])
assert all(bothflexred(source_series.coeff(t,i))==0 for i in range(3))
assert bothflexred(source_series.coeff(t,3)-(h*k+F))==0
translated_first=sp.Matrix([1,a+k*t**3,b+a*a*k*t**3])
translated_second=sp.Matrix([1,xc,yc])
translated_series=sp.expand((translated_first.T*SS*translated_second)[0])
assert all(bothflexred(translated_series.coeff(t,i))==0 for i in range(3))
assert bothflexred(translated_series.coeff(t,3)-(T+v*k))==0
actual=sp.together(h*translated_series.coeff(t,3).subs(k,F/h))
assert bothflexred(actual-h*T-v*F)==0

out={
  'status':'PASS',
  'scope':'Universal polynomial identities only; the accompanying incidence proof remains a separately audited mathematical argument.',
  'contact_cubic_matrix':[[str(x) for x in row] for row in AQ.tolist()],
  'contact_cubic_matrix_determinant':1,
  'plane_cubic_matrix':[[str(x) for x in row] for row in CP.tolist()],
  'plane_cubic_determinant':'(k+r^2)*(k^2+r)',
  'same_difference_limit':'U^3+F^2*T+F*T^2',
  'exceptional_order3_triple_limit':'U^3',
  'six_jet_unit_minor_columns':[8,5,7,0,3,1],
  'six_jet_unit_minor':[[str(x) for x in row] for row in minor.tolist()],
  'flex_translation_ell_coefficients':[0,0,0,1],
  'source_branch_degree3_coefficient':'h*k+F',
  'translated_branch_degree3_coefficient':'T+v*k',
  'flex_contact_leading_coefficient':'T+v*F/h',
  'elapsed_seconds':perf_counter()-started
}
dest=Path(__file__).resolve().parent.parent/'outputs'/'ss_uniform_collision_identities.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
