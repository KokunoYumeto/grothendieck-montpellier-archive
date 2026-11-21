#!/usr/bin/env python3
"""Exact first-order local algebra for F plus free summands.
No global semiregularity or existence assertion is supplied by this script.
"""
from pathlib import Path
import json, time
import sympy as s
start=time.perf_counter()
x,y,t=s.symbols('x y t')
P,alpha,beta=s.symbols('P alpha beta')
b1,b2=s.symbols('b1 b2')
v=s.Matrix([-y,x]); w=s.Matrix([[x,y]])
u=s.Matrix([x,y]); d=v*w
zero=s.zeros(2,1)
# All first jets of a bivector on the three relevant functions.
def bracket(a,b):
    return s.expand(P*(s.diff(a,x)*s.diff(b,y)-s.diff(a,y)*s.diff(b,x))
                    +alpha*(s.diff(a,t)*s.diff(b,x)-s.diff(a,x)*s.diff(b,t))
                    +beta*(s.diff(a,t)*s.diff(b,y)-s.diff(a,y)*s.diff(b,t)))
def pb(A,B):
    assert A.cols==B.rows
    return s.Matrix(A.rows,B.cols,lambda i,j:sum(bracket(A[i,k],B[k,j])/2 for k in range(A.cols)))
def eq(A,B):
    return all(s.expand(a-b)==0 for a,b in zip(A,B))
h=s.Rational(3,2)*P*s.eye(2)
assert eq(d*v,zero)
assert eq(pb(d,v)+h*v,zero)
# Scalar line-frame transition, f_j=t*f_i and g_j=t*g_i.
vj=t*v; dj=t*t*d
Pj=bracket(t*x,t*y)
hj=s.Rational(3,2)*Pj*s.eye(2)
G0=t*s.eye(2); G1=t**3*s.eye(2); G2=s.Matrix([[t**4]])
O0=G0*hj-h*G1+pb(G0,dj)-pb(d,G1)
O1=pb(G1,vj)-pb(v,G2)
C=x*beta-y*alpha
z=s.Matrix([-beta,alpha]); row=s.Matrix([[alpha,beta]])
assert s.expand(Pj-(t*t*P+t*C))==0
assert eq(O0,t*t*(s.Rational(3,2)*C*s.eye(2)+2*s.Matrix(2,2,lambda i,j:bracket(t,d[i,j]))))
assert eq(O0*vj+d*O1,zero)
# Column pairs representing u*z plus v*row in Hom(P^-1,F).
Uz=z*w  # columns x*z,y*z
assert eq(O0/t**3, (s.Rational(1,2)*Uz+s.Rational(7,2)*v*row)/t)
# Nilpotent endomorphism and its first-order lifting obstruction.
b=s.Matrix([[b1,b2]]); tb=(b*v)[0]
delta=v*b
Od=delta*h-h*(tb*s.eye(2))+pb(delta,d)-pb(d,tb*s.eye(2))
j=s.Matrix([b2,-b1])
assert eq(Od,P*(v*b-j*w))
assert eq(Od*v+d*s.Matrix([bracket(tb,-y),bracket(tb,x)]),zero)
# A general scalar a has independent Hamiltonian derivatives ax,ay.
ax,ay=s.symbols('ax ay')
Da=s.Matrix([[-ax*y-ay*x,-2*ay*y],[2*ax*x,ax*y+ay*x]])
assert eq(Da,s.Matrix([-ay,ax])*w+v*s.Matrix([[ax,ay]]))
# Highest-syzygy ring character, including factorization through a free term.
m1,m2=s.symbols('m1 m2'); m=s.Matrix([m1,m2]); pm=(w*m)[0]
bm=s.Matrix([[m2,-m1]])
assert eq(m*w-pm*s.eye(2),v*bm)
assert s.expand(pm+(bm*v)[0])==0
# Pure FF composition: a''+b''v = (a+bv)(a'+b'v), modulo I^2.
a,ap,c1,c2=s.symbols('a ap c1 c2'); c=s.Matrix([[c1,c2]])
tc=(c*v)[0]
newb=a*c+ap*b+tb*c
assert s.expand(a*ap+(newb*v)[0]-(a+tb)*(ap+tc))==0
# A representative-lift change b -> b + I*row alters ell only modulo I^2.
r1,r2,r3,r4=s.symbols('r1 r2 r3 r4')
change=(s.Matrix([[x*r1+y*r2,x*r3+y*r4]])*v)[0]
assert all(sum(mon)>=2 for mon,coef in s.Poly(change,x,y).terms())
# Determinant identity for a generic rank-two normal derivative.
a11,a12,a21,a22=s.symbols('a11 a12 a21 a22')
e11,e12,e21,e22=s.symbols('e11 e12 e21 e22')
A=s.Matrix([[a11,a12],[a21,a22]]); E=s.Matrix([[e11,e12],[e21,e22]])
jet=s.symbols('jet')
assert s.cancel(s.trace(A.inv()*E)-s.diff((A+jet*E).det(),jet).subs(jet,0)/A.det())==0
out={'result':'PASS','runtime_seconds':time.perf_counter()-start,
     'minimal_first_order_correction':'(3/2)*{f,g}*I2; syzygy v unchanged',
     'unit_frame_overlap_U_coefficient':'1/2',
     'unit_frame_overlap_T_coefficient':'7/2',
     'nilpotent_T_projection':'{f,g}*(b1,b2)',
     'highest_syzygy_character':'ell=a+bv modulo I^2; kills all maps factoring through a free module',
     'checks':['exact corrected complex square','generic line-frame first overlap and chain identity','both exact Ext1 components','nilpotent lifting obstruction','scalar lifting obstruction','free-factorization cancellation','multiplicativity modulo I^2','representative independence modulo I^2','generic2x2 logarithmic determinant identity'],
     'limits':'Does not compute global Cech cohomology, certify independent theorem review, construct a finite action, or assert any semiregular seed.'}
Path(__file__).with_name('rm_free_summand_overlap_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
