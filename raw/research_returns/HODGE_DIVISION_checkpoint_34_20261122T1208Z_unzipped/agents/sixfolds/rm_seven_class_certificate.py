#!/usr/bin/env python3
"""Exact class independence and full Chern character for SF-E815.

This proves only the listed exterior/polynomial and integral matrix identities.
It does not execute a geometric construction or verify categorical descent.
"""
from pathlib import Path
import hashlib
import json
import sympy as sp

r=Path(__file__).resolve().parent
u=sp.sqrt(2)
x,y=sp.symbols('x y')
rows=[(a,b) for a in range(3) for b in range(3)]
classes=[(0,0),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
names=['0','X','-X','Z+','-Z+','Z-','-Z-']
weights=sp.Matrix([24,2,2,1,1,1,1])

def trunc(p):
    p=sp.Poly(sp.expand(p),x,y)
    return sp.expand(sum(c*x**a*y**b for (a,b),c in p.terms() if a<=2 and b<=2))
def expclass(a,b):
    z=(a+b*u)*x+(a-b*u)*y
    return trunc(sum(z**j/sp.factorial(j) for j in range(5)))
chars=[expclass(a,b) for a,b in classes]
C=sp.Matrix([[sp.expand(p).coeff(x,a).coeff(y,b) for p in chars] for a,b in rows])
rowids=list(C.T.rref()[1])
minor=sp.simplify(C.extract(rowids,range(7)).det())
assert len(rowids)==7 and minor!=0
char=sp.simplify(sum(weights[j]*chars[j] for j in range(7)))
target=32+8*(x*x+y*y)+2*x*x*y*y
assert sp.expand(char-target)==0
square=trunc(char*char)
chi=4*sp.expand(square).coeff(x,2).coeff(y,2)
assert chi==1024
cross=expclass(-2,-2)
crosschi=4*sp.expand(cross).coeff(x,2).coeff(y,2)
assert crosschi==16
cross_x_z=expclass(0,1)
cross_x_z_chi=4*sp.expand(cross_x_z).coeff(x,2).coeff(y,2)
assert cross_x_z_chi==4
weighted_x_z=weights[1]*weights[3]*cross_x_z_chi
assert weighted_x_z==8 and chi/weighted_x_z==128
S=sp.diag(1,1,-1,-1)
U=sp.diag(sp.Matrix([[1,1],[1,-1]]),sp.Matrix([[1,1],[1,-1]]))
assert U*U==2*sp.eye(4) and U*S==S*U
Zp=(sp.eye(4)+U)*S
Zm=(sp.eye(4)-U)*S
assert S.det()==1 and Zp.det()==1 and Zm.det()==1
E=sp.zeros(8)
E[:4,4:]=Zp
E[4:,:4]=-Zp
assert E.det()==1
out={
 'result':'PASS',
 'coefficient_field':'Q(sqrt(2)) with the positive real root',
 'ring':'Q(sqrt(2))[x,y]/(x^3,y^3), integral(x^2 y^2)=4',
 'class_names':names,'class_coordinates_X_Y':classes,'weights':list(map(int,weights)),
 'row_order':rows,'character_matrix':[[str(v) for v in C.row(i)] for i in range(9)],
 'rank':7,'minor_row_indices_zero_based':rowids,'minor_determinant':str(minor),
 'full_character':str(char),'target':str(target),'Euler_self':int(chi),
 'opposite_Zplus_pair_Euler':int(crosschi),
 'X_Zplus_unweighted_pair_Euler':int(cross_x_z_chi),
 'X_Zplus_weighted_pair_Euler_at_k1':int(weighted_x_z),
 'refined_minimum_invariant_Euler':128,'refined_minimum_invariant_End':63,
 'U_squared':'2 I4','det_X':int(S.det()),'det_Zplus':int(Zp.det()),'det_Zminus':int(Zm.det()),
 'theta_pairing_det':int(E.det()),
 'limitation':'No categorical action, trace injectivity, or derived existence assertion is certified by this script.'
}
(r/'rm_seven_class_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:out[k] for k in ['result','rank','minor_row_indices_zero_based','minor_determinant','full_character','Euler_self','opposite_Zplus_pair_Euler']},indent=2))
