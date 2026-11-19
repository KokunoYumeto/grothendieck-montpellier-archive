#!/usr/bin/env python3
"""Exact certificate for B-RD29; rational arithmetic and polynomial identities."""
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter
import json
import sympy as s
started=perf_counter()
a1,a2,a3,a4,a6=map(F,[-3,-12,-12,0,0])
P=(F(0),F(0))
def neg(P):
    if P is None:return None
    x,y=P;return x,-y-a1*x-a3
def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;X,Y=Q
    if x==X and Q==neg(P):return None
    if P==Q:
        den=2*y+a1*x+a3
        lam=(3*x*x+2*a2*x+a4-a1*y)/den
        nu=(-x**3+a4*x+2*a6-a3*y)/den
    else:
        lam=(Y-y)/(X-x);nu=(y*X-Y*x)/(X-x)
    z=lam*lam+a1*lam-a2-x-X
    return z,-(lam+a1)*z-nu-a3
pts=[None]
for i in range(1,10):pts.append(add(pts[-1],P))
assert pts[9] is None and len(set(pts[:9]))==9
for Q in pts[1:9]:
    x,y=Q;assert y*y+a1*x*y+a3*y==x**3+a2*x*x
for i in range(9):
    for j in range(9):assert add(pts[i],pts[j])==pts[(i+j)%9]
x,y,X,Y=s.symbols('x y X Y')
weier=y*y-3*x*y-12*y-x**3+12*x*x
# Miller factors: g3 has divisor 3(P)-(3P)-2(O), and ell has divisor3(3P)-3(O).
assert s.rem(y*(y-4*x)-(x-12)*(x*x-y),weier,y)==0
ell=y-3*x+4
assert s.factor(weier.subs(y,3*x-4))==-(x-4)**3
f9=(x*x-y)**3*ell/(x-4)**3
f4=s.cancel(f9.subs({x:pts[4][0],y:pts[4][1]}));f5=s.cancel(f9.subs({x:pts[5][0],y:pts[5][1]}))
assert f4==2916 and f5==-3456
q0=s.cancel(f5/f4);q=s.Integer(2)**5*3**6
assert q0==s.Rational(-32,27) and q/q0==(-3)**9
# Degree-nine isogeny from exact short-coordinate rational functions.
A=s.Rational(-219,16);B=s.Rational(827,32)
qs=[s.Rational(v)-s.Rational(13,4) for v in [0,12,4,6]]
Fcurve=lambda z:z**3+A*z+B
R=s.cancel(X+sum(2*(3*r*r+A)/(X-r)+4*Fcurve(r)/(X-r)**2 for r in qs))
Aprime=A-5*sum(2*(3*r*r+A) for r in qs)
Bprime=B-7*sum(2*(5*r**3+3*A*r+2*B) for r in qs)
assert Aprime==s.Rational(-37179,16) and Bprime==s.Rational(-1397493,32)
assert s.cancel(Fcurve(X)*s.diff(R,X)**2-R**3-Aprime*R-Bprime)==0
num,den=s.fraction(R)
assert s.degree(num,X)==9 and s.degree(den,X)==8 and s.gcd(num,den)==1
assert s.degree(den,X)==8
for r in qs:assert den.subs(X,r)==0 and s.diff(den,X).subs(X,r)==0
# The quotient in the original long coordinates, then an explicit Q-isomorphism.
quot=y*y-3*x*y-12*y-x**3+12*x*x+2310*x+36190
shortquot=Y*Y-X**3-Aprime*X-Bprime
assert s.expand(quot.subs({x:X+s.Rational(13,4),y:Y+s.Rational(3,2)*(X+s.Rational(13,4))+6})-shortquot)==0
minimal=Y*Y-X*Y+Y-X**3+X*X+28*X+53
assert s.expand(quot.subs({x:9*X+1,y:27*Y+21})-3**6*minimal)==0
def invariants(ai):
    a1,a2,a3,a4,a6=map(s.Integer,ai)
    b2=a1*a1+4*a2;b4=a1*a3+2*a4;b6=a3*a3+4*a6
    b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    c4=b2*b2-24*b4
    D=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    return int(c4),int(D),str(s.Rational(c4**3,D))
invE=invariants([-3,-12,-12,0,0]);invB=invariants([-1,-1,1,-28,-53])
assert invE==(3**2*73,-2**9*3**5,str(s.Rational(-3*73**3,2**9)))
assert invB==(3**4*17,-2*3**9,str(s.Rational(-3**3*17**3,2)))
# Raw discriminant valuation is9e; for every e==2 mod4 the good inertia degree is even.
for e in range(2,2002,4):
    for m in range(1,25):
        if 9*e*m%12==0:assert m%2==0
out={'status':'PASS','scope':'Explicit elliptic 9-isogeny, rational 9-point subgroup, descent function, Kummer parameter and inertia parity; Tate uniformization is proved separately',
     'E_coefficients':[-3,-12,-12,0,0],'M_curve_coefficients':[-1,-1,1,-28,-53],
     'points':[None if Q is None else [str(z) for z in Q] for Q in pts[:9]],
     'all_81_subgroup_additions':True,'invariants_E':invE,'invariants_M_curve':invB,
     'descent_function':'(x^2-y)^3*(y-3*x+4)/(x-4)^3','f_4P':str(f4),'f_5P':str(f5),
     'Kummer_ratio':str(q0),'Tate_parameter':str(q),'Kummer_adjustment':'(-3)^9',
     'short_isogeny_x':str(R),'isogeny_degree':9,'isogeny_target_identity':True,
     'odd_part_base_change_indices_checked':500,'elapsed_seconds':perf_counter()-started}
p=Path(__file__).with_suffix('.output.json');p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
