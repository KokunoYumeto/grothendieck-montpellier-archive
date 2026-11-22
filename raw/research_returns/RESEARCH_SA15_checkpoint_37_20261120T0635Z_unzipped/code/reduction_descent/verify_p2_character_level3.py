"""Exact certificate for the p=2,e=1 level-eight character counterexample."""
from pathlib import Path
from time import perf_counter
import json
from fractions import Fraction as Q
started=perf_counter()
import sympy as s
class K:
 def __init__(self,a=0,b=0):
  if isinstance(a,K):self.a,self.b=a.a,a.b
  else:self.a,self.b=Q(a),Q(b)
 def __add__(self,o):
  o=K(o);return K(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return K(-self.a,-self.b)
 def __sub__(self,o):return self+-K(o)
 def __rsub__(self,o):return K(o)+-self
 def __mul__(self,o):
  o=K(o);return K(self.a*o.a-3*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def inv(self):
  n=self.a*self.a+3*self.b*self.b
  return K(self.a/n,-self.b/n)
 def __truediv__(self,o):return self*K(o).inv()
 def __rtruediv__(self,o):return K(o)*self.inv()
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  r=K(1);a=self
  while n:
   if n&1:r=r*a
   a=a*a;n//=2
  return r
 def __eq__(self,o):
  o=K(o);return self.a==o.a and self.b==o.b
 def __hash__(self):return hash((self.a,self.b))
 def __repr__(self):return f'({self.a})+({self.b})*lam'
lam=K(0,1);a1=5-lam;a2=-2*lam;a3=-4*lam;a4=a6=K(0)
def add(P,R):
 if P is None:return R
 if R is None:return P
 x,y=P;u,v=R
 if x==u and y+v+a1*x+a3==0:return None
 if x==u:
  m=(3*x*x+2*a2*x+a4-a1*y)/(2*y+a1*x+a3)
 else:m=(v-y)/(u-x)
 k=y-m*x
 X=m*m+a1*m-a2-x-u
 Y=-(m+a1)*X-k-a3
 return X,Y
points=[None];P=(K(0),K(0));R=None
for n in range(1,9):R=add(R,P);points.append(R)
assert len(set(points[:-1]))==8
assert points[-1] is None and points[4] is not None
for j in range(8):
 for k in range(8):assert add(points[j],points[k])==points[(j+k)%8]
b2=a1*a1+4*a2;b4=a1*a3;b6=a3*a3;b8=a2*a3*a3
c4=b2*b2-24*b4;c6=-b2**3+36*b2*b4-216*b6
D=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert c4==K(-200,-312) and c6==K(15488,576) and D==K(-41472,20736)
# Exact affine Miller function.
z,x,y=s.symbols('lam x y')
def ex(v):return s.Rational(v.a.numerator,v.a.denominator)+s.Rational(v.b.numerator,v.b.denominator)*z
def red(v):
 v=s.cancel(v);num,den=s.fraction(v)
 num=s.rem(num,z*z+3,z);den=s.rem(den,z*z+3,z)
 return s.rem(num*s.invert(den,z*z+3,z),z*z+3,z)
x2,y2=points[2];x4,y4=points[4]
m=(3*x2*x2+2*a2*x2-a1*y2)/(2*y2+a1*x2+a3);k=y2-m*x2
assert m==K(Q(-9,2),Q(1,2)) and k==K(-3,3)
curve=y*y+ex(a1)*x*y+ex(a3)*y-x**3-ex(a2)*x*x
num=s.rem(y**4*(y-ex(m)*x-ex(k))**2,curve,y)
num=s.Poly(num,x,y).as_dict();num=sum(red(c)*x**ij[0]*y**ij[1] for ij,c in num.items())
den=(x-ex(x2))**4*(x-ex(x4))
quot,rem=s.div(num,den,x)
rem=s.Poly(rem,x,y).as_dict();assert all(red(c)==0 for c in rem.values())
quot=s.Poly(quot,x,y).as_dict();ff=sum(red(c)*x**ij[0]*y**ij[1] for ij,c in quot.items())
expected=x**4-4*z*x**3-8*x*x+(2*z-6)*x*x*y+(12*z+4)*x*y+16*y
assert s.expand(ff-expected)==0
def ev(F,P):return red(F.subs({x:ex(P[0]),y:ex(P[1])}))
ratio=red(ev(ff,points[3])/ev(ff,points[2]))
assert ratio==-s.Rational(4,3)*z
q=lam**7*(lam-1)**6*(lam+1)**4
assert red(ex(q)/ratio-ex((-3-lam)**8))==0

def v2rat(t):
 t=Q(t)
 if not t:return None
 n=abs(t.numerator);d=t.denominator;r=0
 while n%2==0:n//=2;r+=1
 while d%2==0:d//=2;r-=1
 return r
def v2K(t):return Q(v2rat(t.a*t.a+3*t.b*t.b),2)
assert v2K(c4)==4 and v2K(D)==8 and v2K(c4**3/D)==4
q0=-4*lam/3
assert v2K(q0)==2
out={
 'status':'PASS','field':'Q_2(omega), omega^2+omega+1=0, lambda=1+2omega',
 'integral_curve':'y^2+(5-lambda)*x*y-4*lambda*y=x^3-2*lambda*x^2',
 'point':'P=(0,0), order8',
 'multiples':[None if P is None else [repr(a) for a in P] for P in points[:-1]],
 'all_64_additions':True,
 'invariants':{'c4':repr(c4),'c6':repr(c6),'Delta':repr(D),'v2c4':4,'v2Delta':8,'v2j':4},
 'tangent_at_2P':{'slope':repr(m),'intercept':repr(k)},
 'miller_function':str(expected),
 'miller_identity':True,'f_2P':str(ev(ff,points[2])),'f_3P':str(ev(ff,points[3])),
 'Kummer_ratio':str(ratio),'Tate_parameter':'-4*lambda/3','Tate_parameter_valuation':2,
 'Figure8_parameter_comparison_eighth_root':'-3-lambda',
 'elapsed_seconds':perf_counter()-started,
 'scope':'Exact characteristic-zero group/invariant/function identities; quotient-Tate and inertia character arguments are separately proved in B_p2_character_level3.tex.'}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
