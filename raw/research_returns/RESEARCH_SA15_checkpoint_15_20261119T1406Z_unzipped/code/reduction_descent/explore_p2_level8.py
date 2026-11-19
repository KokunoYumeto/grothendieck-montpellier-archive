from fractions import Fraction as Q
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
print('points',points)
assert points[-1] is None and points[4] is not None
for j in range(8):
 for k in range(8):assert add(points[j],points[k])==points[(j+k)%8]
b2=a1*a1+4*a2;b4=a1*a3;b6=a3*a3;b8=a2*a3*a3
c4=b2*b2-24*b4;c6=-b2**3+36*b2*b4-216*b6
D=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
print('inv',c4,c6,D,'j',c4**3/D)
# Exact affine Miller function.
z,x,y=s.symbols('lam x y')
def ex(v):return s.Rational(v.a.numerator,v.a.denominator)+s.Rational(v.b.numerator,v.b.denominator)*z
def red(v):
 v=s.cancel(v);num,den=s.fraction(v)
 num=s.rem(num,z*z+3,z);den=s.rem(den,z*z+3,z)
 return s.rem(num*s.invert(den,z*z+3,z),z*z+3,z)
x2,y2=points[2];x4,y4=points[4]
m=(3*x2*x2+2*a2*x2-a1*y2)/(2*y2+a1*x2+a3);k=y2-m*x2
print('tangent2',m,k)
curve=y*y+ex(a1)*x*y+ex(a3)*y-x**3-ex(a2)*x*x
num=s.rem(y**4*(y-ex(m)*x-ex(k))**2,curve,y)
num=s.Poly(num,x,y).as_dict();num=sum(red(c)*x**ij[0]*y**ij[1] for ij,c in num.items())
den=(x-ex(x2))**4*(x-ex(x4))
quot,rem=s.div(num,den,x)
rem=s.Poly(rem,x,y).as_dict();assert all(red(c)==0 for c in rem.values())
quot=s.Poly(quot,x,y).as_dict();ff=sum(red(c)*x**ij[0]*y**ij[1] for ij,c in quot.items())
print('f8',s.factor(ff))
def ev(F,P):return red(F.subs({x:ex(P[0]),y:ex(P[1])}))
ratio=red(ev(ff,points[3])/ev(ff,points[2]))
print('ratio',ratio)
q=lam**7*(lam-1)**6*(lam+1)**4
print('q',q,'q/ratio',red(ex(q)/ratio))
