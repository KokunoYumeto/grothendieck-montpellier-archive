#!/usr/bin/env python3
"""Exact certificate for B-RD42; geometric descent is proved in the text."""
from pathlib import Path
from time import perf_counter
from fractions import Fraction
import json
import sympy as s
started=perf_counter()
x,y,X,Y,b,r,p,i,v,z,T,a,d,eps=s.symbols('x y X Y b r p i v z T a d eps')

def reduce_p(expr):
    return s.rem(s.expand(expr),p*p-3,p)

def invariants(A,B):
    return -48*A, -864*B, -16*(4*A**3+27*B**2)
c4,c6,Delta=invariants(-3,3*b)
assert c4==144 and s.expand(c6+2592*b)==0
assert s.expand(Delta+432*(3*b-2)*(3*b+2))==0
assert s.factor(c4**3/Delta-6912/(4-9*b*b))==0
c4p,c6p,Dp=invariants(-9,p**5*b)
assert reduce_p(Dp-p**6*Delta)==0
# The exact translated and scaled good equation.
source=(p**3*Y)**2-((p**2*X+p*r)**3-9*(p**2*X+p*r)+p**5*b)
target=p**6*(Y**2-X**3-p*r*X**2-(r*r-1)*X)
rem=reduce_p(source-target)
assert s.rem(rem,r**3-3*r+3*b,r)==0
assert s.discriminant(r**3-3*r+3*b,r)==27*(4-9*b*b)
# Cardano U=iD: U+U^{-1}=-3b.
D=v+s.Rational(3,2)*i*b
U=i*D
gb=s.groebner([i*i+1,v*v-1+s.Rational(9,4)*b*b],i,v,b)
assert gb.reduce(s.expand(U*U+3*b*U+1))[1]==0
# Universal Hesse invariant after eliminating z^2-Tz+3.
hesse_num=27*(1+z)**3*((1+z)**3+8)**3
hesse_den=((1+z)**3-1)**3
trace_j_num=27*T**3*(T+4)**3
trace_j_den=(T+3)**3
assert s.rem(hesse_num*trace_j_den-hesse_den*trace_j_num,z*z-T*z+3,z)==0
assert s.factor(T*(T+4)-4*(T+3)-(T*T-12))==0
# Trace expansion, with epsilon^2=1 and 3=pi^2.
t0=2*eps*p+p*p*a
numer=s.expand(t0*t0-4*p*p-2*p*p*a*(t0+p*p)+p**4*(a*a+2*a))
assert s.rem(numer,eps*eps-1,eps)==0
# Cubic comparison after replacing every explicit factor 3 by pi^2.
H_cube=64+16*p**4*d+p**6*(4*d*d+d**3)
assert reduce_p((4+p*p*d)**3-H_cube)==0
comparison=s.expand(H_cube*(1-p**4*b*b/4)-64)
assert s.expand(comparison/p**4-16*(d-b*b)).subs(p,0)==0
assert s.Poly(s.expand(comparison/p**4-16*(d-b*b)),p).coeff_monomial(p)==0
up,uu=s.symbols('up uu')
assert s.factor(up+1/up-uu-1/uu-(up-1/uu)*(1-uu/up))==0
# Opposite marked lifts, including determinants and actual central sign.
S=s.Matrix([[0,-1],[1,0]])
R=s.diag(1,-1)
assert R*S*R.inv()==S.inv()==-S
assert R.det()==-1 and S.det()==1 and S*S==-s.eye(2)
# All discriminant candidates and short-model scaling valuations.
delta_cases=[]
for delta in (0,6,12,18):
    vc4=Fraction(delta+6,3)
    vc6_lower=Fraction(min(3*vc4,6+delta),2)
    delta_cases.append({'delta':delta,'vA':str(vc4-2),'vB_lower':str(vc6_lower-6)})
assert delta_cases[1]['vA']=='2' and delta_cases[1]['vB_lower']=='0'
assert delta_cases[2]['vA']=='4' and delta_cases[2]['vB_lower']=='3'
assert delta_cases[3]['vA']=='6' and delta_cases[3]['vB_lower']=='6'
# Exact Newton polygons; points with infinite coefficients are omitted.
def lower_hull(points):
    hull=[]
    for point in sorted(points):
        while len(hull)>=2:
            x0,y0=hull[-2];x1,y1=hull[-1];x2,y2=point
            if (y1-y0)*(x2-x1)>=(y2-y1)*(x1-x0):hull.pop()
            else:break
        hull.append(point)
    return hull
newton=[]
for valB in (0,1,2,3):
    hull=lower_hull([(0,2),(1,valB),(2,2),(4,0)])
    slopes=[(str(-Fraction(y1-y0,x1-x0)),x1-x0) for (x0,y0),(x1,y1) in zip(hull,hull[1:])]
    newton.append({'vB':valB,'root_valuations_and_multiplicities':slopes})
assert newton[0]['root_valuations_and_multiplicities']==[('2',1),('0',3)]
assert newton[1]['root_valuations_and_multiplicities']==[('1',1),('1/3',3)]
assert newton[2]['root_valuations_and_multiplicities']==[('1/2',4)]
assert lower_hull([(0,2),(1,2),(3,0)])==[(0,2),(3,0)]
assert Fraction(1)+Fraction(2,3)-1==Fraction(2,3)
# Cube bounds used over K (e=2) and F (e=4).
cube_cases=0
for e in (2,4):
    for w in range(1,1001):
        bound=min(e+w,e+2*w,3*w)
        assert bound>=3
        cube_cases+=1
assert 2+3+1==6 and Fraction(6,2)==3
# Explicit GF(9) check of the exact square/line equivalence, including
# residues outside F3. This checks an identity whose general proof is algebraic.
def add(A,B):return ((A[0]+B[0])%3,(A[1]+B[1])%3)
def neg(A):return ((-A[0])%3,(-A[1])%3)
def mul(A,B):return ((A[0]*B[0]-A[1]*B[1])%3,(A[0]*B[1]+A[1]*B[0])%3)
units=[(a,b) for a in range(3) for b in range(3) if (a,b)!=(0,0)]
residue_cases=0
for B in units:
    for C in units:
        assert (mul(B,B)==mul(C,C))==(C in (B,neg(B)))
        residue_cases+=1
out={'status':'PASS','normal_form_invariants':{'c4':str(c4),'c6':str(c6),'delta_polynomial':str(s.factor(Delta))},'universal_good_model':'Y^2=X^3+pi*r*X^2+(r^2-1)*X','cubic_discriminant':'27*(4-9*b^2)','cardano_identity':True,'trace_j_elimination':True,'trace_congruence':'T=2*epsilon*pi+(pi^2/2)*b^2 mod pi^3','reverse_marked_matrix_identity':True,'discriminant_cases':delta_cases,'newton_polygons':newton,'cube_cases':cube_cases,'GF9_residue_cases':residue_cases,'elapsed_seconds':perf_counter()-started,'scope':'Universal exact identities and finite valuation arithmetic; full descent, inertia and Kummer-field arguments are in B_height_two_c4_final_exclusion.tex.'}
dest=Path(__file__).with_suffix('.output.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
