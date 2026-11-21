"""Independent standard-library verification of C25's torsion branch data."""
from pathlib import Path
import json

p=109
def add(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
def neg(a):return ((-a[0])%p,(-a[1])%p)
def sub(a,b):return add(a,neg(b))
def mul(a,b):return ((a[0]*b[0]+2*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
def inv(a):
 n=(a[0]*a[0]-2*a[1]*a[1])%p
 assert n
 z=pow(n,-1,p)
 return (a[0]*z%p,-a[1]*z%p)
def scalar(n,a):return (n*a[0]%p,n*a[1]%p)
zero=(0,0)
one=(1,0)
def on(P):
 if P is None:return True
 x,y=P
 return mul(y,y)==sub(sub(mul(mul(x,x),x),scalar(30,x)),(25,0))
def eadd(P,Q):
 if P is None:return Q
 if Q is None:return P
 x,y=P;u,v=Q
 if x==u and add(y,v)==zero:return None
 slope=mul(sub(v,y),inv(sub(u,x))) if x!=u else mul(sub(scalar(3,mul(x,x)),(30,0)),inv(scalar(2,y)))
 w=sub(sub(mul(slope,slope),x),u)
 z=sub(mul(slope,sub(x,w)),y)
 A=(w,z);assert on(A)
 return A
def eneg(P):return None if P is None else (P[0],neg(P[1]))
def emul(n,P):
 Q=None
 while n:
  if n&1:Q=eadd(Q,P)
  P=eadd(P,P);n//=2
 return Q
def frob(P):return None if P is None else ((P[0][0],-P[0][1]%p),(P[1][0],-P[1][1]%p))
T=((104,0),(0,0))
U=((34,53),(11,96))
V=((2,18),(8,82))
W=((2,91),(8,27))
R=((47,0),(0,20))
assert all(on(P) for P in [T,U,V,W,R])
assert emul(2,U)==((34,0),(0,0)) and emul(4,U) is None
assert emul(4,V)==T and emul(4,W)==T
assert frob(U)==eadd(eneg(U),T)
assert frob(V)==W and frob(W)==V
assert frob(R)==eneg(R)
assert emul(13,R) is None

# Multiply the branch factors in F_109[s]/(s^2-2), without Sympy.
def polymul(a,b):
 c=[zero]*(len(a)+len(b)-1)
 for j,x in enumerate(a):
  for k,y in enumerate(b):c[j+k]=add(c[j+k],mul(x,y))
 return c
f=[(-20%p,0),(10,0),one] # (x+5)^2-45
branch=[]
for P in [U,eadd(U,R),V,W]:
 for Q in [P,eadd(P,T)]:
  branch.append(Q[0]);f=polymul(f,[neg(Q[0]),one])
assert len(set(branch))==8
assert all(b==0 for a,b in f)
coeff=[a for a,b in f]
assert coeff==[63,1,65,35,40,3,45,30,27,62,1]

# Elementary good-prime count at 7 giving a_7=2.
points7=1+sum(1 if (v:=(x*x*x-30*x-25)%7)==0 else 2 if pow(v,3,7)==1 else 0 for x in range(7))
assert points7==6
assert pow(2,6,13)==12 # irreducibility of X^2-2X+7 modulo13
data={"points_on_E":True,"orders":{"U":4,"V":8,"W":8,"R":13},
      "frobenius_relations":True,"branch_x":[list(x) for x in branch],
      "polynomial_ascending":coeff,"E_F7_count":points7,"a7":2,
      "all_checks":"PASS"}
Path('work/check_C25_torsion_independent_output.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
