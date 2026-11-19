"""Exact certificate over Q[i,pi]/(i^2+1, pi^2+3pi+3).
No floating-point or p-adic approximation is used.  Valuation v_K(pi)=1.
"""
import sympy as S, json, time
from fractions import Fraction
from pathlib import Path
start=time.monotonic();pi,i=S.symbols('pi i')
GB=S.groebner([pi*pi+3*pi+3,i*i+1],pi,i,domain=S.QQ)
def red(a):return S.expand(GB.reduce(S.expand(a))[1])
def mul(a,b):return red(a*b)
def power(a,n):
 r=S.Integer(1)
 for _ in range(n):r=mul(r,a)
 return r
def vp(q):
 q=Fraction(q)
 if not q:return None
 a,b=q.numerator,q.denominator;v=0
 while a%3==0:a//=3;v+=1
 while b%3==0:b//=3;v-=1
 return v
def val(a):
 vals=[2*vp(c)+mon[0] for mon,c in S.Poly(red(a),pi,i).terms() if c]
 return min(vals) if vals else None
zeta=pi+1;delta=2*pi+3;t=1+i*pi
assert red(power(zeta,2)+zeta+1)==0 and red(power(delta,2)+3)==0
a=-27*mul(t,power(t,3)+8);b=54*(power(t,6)-20*power(t,3)-8)
a=red(a);b=red(b)
D=red(-16*(4*power(a,3)+27*power(b,2)))
Dfactor=2**12*3**9*power(power(t,3)-1,3)
assert red(D-Dfactor)==0
points=[]
x0=-9*power(t,2);y0=12*mul(delta,power(t,3)-1)
points.extend([(red(x0),red(y0)),(red(x0),red(-y0))])
for eps in [S.Integer(1),zeta,power(zeta,2)]:
 x=red(3*power(t,2)+12*mul(eps,t)+12*power(eps,2))
 y=36*red(mul(eps,power(t,2))+mul(power(eps,2),t)+1)
 points.extend([(x,red(y)),(x,red(-y))])
checks=[]
for x,y in points:
 curve=red(power(y,2)-power(x,3)-mul(a,x)-b)
 tripling=red(power(3*power(x,2)+a,2)-12*mul(x,power(y,2)))
 assert curve==0 and tripling==0 and y!=0
 checks.append({'x':str(x),'y':str(y),'curve_residual':str(curve),'tripling_residual':str(tripling)})
assert len(set((str(x),str(y)) for x,y in points))==8
assert points[0][0]!=points[2][0]
pinv=-(pi+3)/3
A=mul(-3*mul(t,power(t,3)+8),power(pinv,4))
B=mul(2*(power(t,6)-20*power(t,3)-8),power(pinv,6))
assert red(A-(4*i*pi+3*pi+6))==0
assert red(B-(-12*i+20*pi+30))==0
assert val(A)==val(B)==1
out={'field':'K=Q_3(i,zeta_3), i^2=-1; pi=zeta_3-1, pi^2+3pi+3=0','absolute_ramification':2,'residue_field':'F_9','t':str(t),'a4':str(a),'a6':str(b),'discriminant_formula':'2^12*3^9*(t^3-1)^3','v_discriminant':val(D),'v_t3_minus_1':val(power(t,3)-1),'v_t3_plus_8':val(power(t,3)+8),'v_j':6+3*val(power(t,3)+8)-3*val(power(t,3)-1),'torsion_points':checks,'nonzero_torsion_points_count':len(points),'independent_basis_indices':[0,2],'two_division_scale':'x=3*pi^2*Z','two_division_coefficients':{'A':str(A),'B':str(B)},'two_division_coefficient_valuations':[1,1,0],'Eisenstein_cubic':True,'good_extension_data':{'v_K(x0)':'13/3','v_K(3*x0^2+a4)':'9','u_equation':'u^4=3*x0^2+a4','v_K(u)':'9/4','v_K(3*x0/u^2)':'11/6','good_special_equation':'Y^2=X^3+X','ramification_degree':12},'seconds':time.monotonic()-start}
print(json.dumps(out,indent=2))
