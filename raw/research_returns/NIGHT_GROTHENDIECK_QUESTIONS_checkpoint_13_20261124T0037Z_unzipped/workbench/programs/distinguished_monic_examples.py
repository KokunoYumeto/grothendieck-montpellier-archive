#!/usr/bin/env python3
"""Exact algebra certificate for the residue-two distinguished-monic example.
Run: python distinguished_monic_examples.py
Requires Python 3 and SymPy. Checks identities, not categorical nonvanishing.
"""
import json
import sympy as S

t,theta=S.symbols('t theta')
f=theta**3+theta+1
F=t**3+2*t+4
q=2*theta
c=-theta*(theta+1)
s=1+q
a=q-c*t/s
U=c*c/(s*s)+c*t
g=lambda x:x*x+2*x
assert S.cancel(g(a)+c*F-t*t*U)==0
Ts=[S.Matrix([[1+a,-t**i],[U*t**(2-i),-1-a]]) for i in range(3)]
I=S.eye(2)
for T in Ts:
    assert all(S.cancel(x)==0 for x in T*T-I+c*F*I)
plus=S.diag(t,1);minus=S.diag(1,t)
for i in range(2):
    assert all(S.cancel(x)==0 for x in plus*Ts[i]-Ts[i+1]*plus)
    assert all(S.cancel(x)==0 for x in minus*Ts[i+1]-Ts[i]*minus)
assert plus*minus==t*I==minus*plus
left=S.Matrix.vstack(minus,plus)
right=S.Matrix.hstack(plus,-minus)
left_inverse=S.Matrix([[1,0,0,0],[0,0,0,1]])
right_inverse=S.Matrix([[0,0],[0,1],[-1,0],[0,0]])
assert right*left==S.zeros(2)
assert left_inverse*left==I
assert right*right_inverse==I
assert S.cancel(S.det(S.Matrix.hstack(S.Matrix([0,1]),Ts[0]*S.Matrix([0,1])))-1)==0
assert S.cancel(S.det(S.Matrix.hstack(S.Matrix([1,0]),Ts[2]*S.Matrix([1,0])))-U)==0
fp=S.Poly(f,theta,modulus=2)
assert fp.is_irreducible
assert S.gcd(fp,fp.diff()).degree()==0
cbar=S.rem(S.Poly(c,theta,modulus=2),fp)
sbar=S.rem(S.Poly(s,theta,modulus=2),fp)
assert cbar.degree()==2 and sbar.as_expr()==1
assert S.gcd(cbar,fp).degree()==0
assert S.rem(cbar**7,fp).as_expr()==1
print(json.dumps({
 'status':'PASS',
 'example':'p=2, F=t^3+2t+4, r=1, N=2',
 'extension_polynomial':str(f),
 'root_identity':'g(a)+cF=t^2 U',
 'involution_identity':'T_i^2=I-cF I for i=0,1,2',
 'mesh':'equivariance, zero composite, and both coefficient splittings verified',
 'endpoints':'cyclic determinant 1 at i=0 and unit U at i=2',
 'residue_extension':'irreducible separable degree 3 over F2; cbar nonconstant hence degree 3',
 'scope':'Exact symbolic identities only. Additivity, nonzero detector, exact torsion order, generic vanishing, and full-group splitting require the mathematical proof.'
},indent=2))
