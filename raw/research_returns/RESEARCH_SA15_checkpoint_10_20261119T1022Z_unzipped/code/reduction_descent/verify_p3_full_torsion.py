#!/usr/bin/env python3
"""Exact Q(zeta_3) certificate for E: y^2+y=x^3.
Inputs are hard-coded in this file. No numerical approximation or CAS lookup is used.
The accompanying proof identifies the local field with Q_3(zeta_3), e=2.
"""
from fractions import Fraction as F
import json, time
start=time.perf_counter()
class K:
    def __init__(self,a=0,b=0):
        if isinstance(a,K): self.a,self.b=a.a,a.b
        else: self.a,self.b=F(a),F(b)
    def __add__(self,v):
        v=K(v);return K(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,v):return self+-K(v)
    def __rsub__(self,v):return K(v)+-self
    def __mul__(self,v):
        v=K(v);return K(self.a*v.a-self.b*v.b,self.a*v.b+self.b*v.a-self.b*v.b)
    __rmul__=__mul__
    def inv(self):
        norm=self.a*self.a-self.a*self.b+self.b*self.b
        if not norm:raise ZeroDivisionError
        return K((self.a-self.b)/norm,-self.b/norm)
    def __truediv__(self,v):return self*K(v).inv()
    def __pow__(self,n):
        if n<0:return self.inv()**(-n)
        r=K(1);a=self
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r
    def __eq__(self,v):
        v=K(v);return self.a==v.a and self.b==v.b
    def __hash__(self):return hash((self.a,self.b))
    def __repr__(self):return f'({self.a})+({self.b})*zeta'
O=None
z=K(0,1)
assert z*z+z+1==0 and z**3==1 and z!=1

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u and y+v+1==0:return O
    slope=(v-y)/(u-x) if x!=u else (3*x*x)/(2*y+1)
    intercept=y-slope*x
    w=slope*slope-x-u
    return w,-slope*w-intercept-1

def mul(n,P):
    R=O
    while n:
        if n&1:R=add(R,P)
        P=add(P,P);n//=2
    return R
points=[O,(K(0),K(0)),(K(0),K(-1))]
for x in [-K(1),-z,-z*z]:
    for y in [z,z*z]:points.append((x,y))
assert len(set(points))==9
for P in points:
    if P is not O:
        x,y=P
        assert y*y+y==x**3
        assert 3*x*(x**3+1)==0
    assert mul(3,P)==O
assert all(add(P,Q) in points for P in points for Q in points)
P=(K(0),K(0));Q=(-K(1),z)
assert len({add(mul(a,P),mul(b,Q)) for a in range(3) for b in range(3)})==9
# General Weierstrass invariants for [a1,a2,a3,a4,a6]=[0,0,1,0,0].
b2,b4,b6,b8=0,0,1,0
c4=b2*b2-24*b4
Delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert (c4,Delta)==(0,-27)
out={
 'input':{'p':3,'field':'Q_3(zeta), zeta^2+zeta+1=0','absolute_ramification_index':2,'residue_field':'F_3','curve':'y^2+y=x^3'},
 'division_polynomial':'psi_3=3*x*(x^3+1)',
 'points':[str(P) for P in points],
 'all_points_on_curve':True,'all_points_killed_by_3':True,'closed_under_addition':True,
 'basis':[str(P),str(Q)],'basis_generates':9,
 'c4':c4,'discriminant':Delta,'v_K_discriminant':6,'v_K_discriminant_mod_12':6,
 'j':0,'finite_certificate':'E[3] has degree 9 in characteristic zero; nine distinct rational points exhaust it.',
 'reduction_certificate':'v_K(Delta)=6 mod 12 excludes any good integral Weierstrass equation. j=0 is integral; a displayed degree-6 ramified extension in B_reduction.tex gives good reduction, so the reduction is additive potentially good.',
 'elapsed_seconds':time.perf_counter()-start
}
print(json.dumps(out,indent=2))
