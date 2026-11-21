"""Exact K=Q(omega) cohomology test, characteristic-three quaternion action."""
from fractions import Fraction as F
class K:
 def __init__(self,a=0,b=0):self.a,self.b=F(a),F(b)
 def __add__(self,y):
  if not isinstance(y,K):y=K(y)
  return K(self.a+y.a,self.b+y.b)
 __radd__=__add__
 def __neg__(self):return K(-self.a,-self.b)
 def __sub__(self,y):return self+-y
 def __mul__(self,y):
  if not isinstance(y,K):y=K(y)
  return K(self.a*y.a-self.b*y.b,self.a*y.b+self.b*y.a-self.b*y.b)
 __rmul__=__mul__
 def bar(self):return K(self.a-self.b,-self.b)
 def __bool__(self):return bool(self.a or self.b)
 def __eq__(self,y):
  if not isinstance(y,K):y=K(y)
  return self.a==y.a and self.b==y.b
 def __repr__(self):return f'({self.a},{self.b})'
def add(*xs):
 out={}
 for x in xs:
  for k,v in x.items():out[k]=out.get(k,K())+v
 return {k:v for k,v in out.items() if v}
def scale(c,x):return {k:c*v for k,v in x.items() if c*v}
def wedge(x,y):
 out={}
 for a,c in x.items():
  for b,d in y.items():
   if set(a)&set(b):continue
   key=tuple(sorted(a+b));sign=(-1)**sum(i>j for i in a for j in b)
   out[key]=out.get(key,K())+sign*c*d
 return {k:v for k,v in out.items() if v}
def form(i):return {(i,):K(1)}
def qforms(q,i):
 a,b=q;e,f=form(2*i),form(2*i+1)
 return add(scale(a,e),scale(b,f)),add(scale(-b.bar(),e),scale(a.bar(),f))
def graph(h):
 out={():K(1)}
 for row in range(2):
  pu,pv={},{}
  for col in range(2):
   u,v=qforms(h[2*row+col],col);pu=add(pu,u);pv=add(pv,v)
  out=wedge(out,add(form(4+2*row),scale(-1,pu)))
  out=wedge(out,add(form(5+2*row),scale(-1,pv)))
 return out
zero=(K(),K());one=(K(1),K());wi=(K(0,1),K());ii=(K(),K(1))
def scalar(a):return ((a,K()),zero,zero,(a,K()))
def hh(a):return ((a,K()),ii,ii,(-a,K()))
omega=K(0,1);zeta=K(1,1);r=zeta-K(1)
t0=scale(F(1,2),add(graph(scalar(K(1))),graph(scalar(K(-1))),scale(-1,graph(scalar(omega))),scale(-1,graph(scalar(-omega)))))
q1=((r,K()),zero,zero,zero);q2=(zero,zero,zero,(r,K()))
candidate=add(graph(hh(zeta)),graph(q2),scale(-1,graph(hh(K(1)))),scale(-1,graph(q1)))
diff=add(candidate,scale(-1,t0))
print('zeta=',zeta,'r=',r)
print('Candidate equals t0:',not diff)
print('Difference coordinates:',diff)
print('t0 coordinates:',t0)
