#!/usr/bin/env python3
"""Exact exterior-algebra certificates for the CM sixfold perfect complex.
No numerical complex arithmetic is used. Standard integral generators on E_i^6.
"""
from fractions import Fraction
import sympy as S
I=S.I

def add(*xs):
 out={}
 for x in xs:
  for m,c in x.items():out[m]=S.expand(out.get(m,0)+c)
 return {m:c for m,c in out.items() if c!=0}

def scale(x,c):return {m:S.expand(v*c) for m,v in x.items() if S.expand(v*c)!=0}

def sign(a,b):
 return -1 if sum((b&((1<<j)-1)).bit_count() for j in range(a.bit_length()) if a>>j&1)%2 else 1

def mul(x,y):
 out={}
 for a,c in x.items():
  for b,d in y.items():
   if a&b:continue
   m=a|b;out[m]=S.expand(out.get(m,0)+sign(a,b)*c*d)
 return {m:c for m,c in out.items() if c!=0}

def power(x,n):
 out={0:S.Integer(1)}
 for _ in range(n):out=mul(out,x)
 return out

def exp(x,dim):
 out={0:S.Integer(1)};term={0:S.Integer(1)}
 for k in range(1,dim//2+1):
  term=mul(term,x);out=add(out,scale(term,S.Rational(1,S.factorial(k))))
 return out

def e(j):return {1<<j:S.Integer(1)}

def wedge(i,j):return mul(e(i),e(j))

def integrate_cd(poly):
 # Variables a,b,c,d,u,v in positions0,...,5. Integration over c,d.
 out={}
 for mask,c in poly.items():
  if mask&12!=12:continue
  old=[j for j in range(6) if mask>>j&1 and j not in (2,3)]
  mapping={0:0,1:1,4:2,5:3}
  new=sum(1<<mapping[j] for j in old)
  # c,d are an adjacent even block: moving it last introduces no sign.
  out[new]=c
 return out

# Check one elliptic-coordinate Fourier integral for all four sign choices.
Pxy=add(wedge(0,5),scale(wedge(1,4),-1))
Pout=add(wedge(0,3),scale(wedge(1,2),-1))
Thetaout=add(scale(wedge(0,1),2),scale(wedge(2,3),S.Rational(1,2)))
for s,t in ((I,I),(-I,-I),(I,-I),(-I,I)):
 theta_xy=mul(add(e(0),e(2)),add(e(1),e(3)))
 Pin=add(wedge(2,5),scale(wedge(3,4),-1))
 z=add(scale(theta_xy,2*s),scale(wedge(2,3),2*t),scale(Pin,-1))
 transformed=integrate_cd(exp(z,6))
 normalized=mul(exp(scale(Pout,S.Rational(-1,2)),4),transformed)
 if s==t:
  expected=scale(exp(scale(Thetaout,s/2),4),4*s)
 else:
  expected=add(scale(wedge(0,1),4),scale(Pout,2*s),scale(wedge(2,3),-1))
 assert add(normalized,scale(expected,-1))=={}
 print('one-pair normalized Fourier identity',s,t,'PASS')

# On E_i^6 order coordinates (a_j,b_j,u_j,v_j) forj0,1,2.
Hx={};Hhat={};P={};Wplus={0:S.Integer(1)};Wminus={0:S.Integer(1)}
for j in range(3):
 a,b,u,v=[4*j+k for k in range(4)]
 ab=wedge(a,b);uv=wedge(u,v);pj=add(wedge(a,v),scale(wedge(b,u),-1))
 Hx=add(Hx,ab);Hhat=add(Hhat,uv);P=add(P,pj)
 Wplus=mul(Wplus,add(scale(ab,4),scale(pj,2*I),scale(uv,-1)))
 Wminus=mul(Wminus,add(scale(ab,4),scale(pj,-2*I),scale(uv,-1)))
t=scale(add(Wplus,Wminus),S.Rational(-1,2))
theta=add(scale(Hx,4),Hhat)
assert all(c.is_Integer for c in t.values())
assert mul(theta,t)=={}
assert power(t,2)=={(1<<12)-1:S.Integer(-2048)}
assert power(theta,6)=={(1<<12)-1:S.Integer(64*S.factorial(6))}
poly=add({0:S.Integer(64)},scale(power(theta,2),-2),scale(power(theta,4),S.Rational(1,96)),scale(power(theta,6),S.Rational(-1,46080)))
# Sum the four normalized transform terms from the two exponential decomposition.
a=(1-I)/2;b=(1+I)/2
Thetahalf=scale(theta,S.Rational(1,4))
raw=add(scale(exp(scale(Thetahalf,I),12),-a*a*(4*I)**3),scale(exp(scale(Thetahalf,-I),12),-b*b*(-4*I)**3),scale(Wplus,-a*b),scale(Wminus,-a*b))
assert add(raw,scale(add(t,poly),-1))=={}
print('full B-twisted Chern character identity PASS')
print('t integral coefficients:',len(t),'nonzero terms')
print('t^2 integral = -2048; theta*t = 0; volume(theta)=64')
# Point-morphism matrices for diagonal balanced CM action.
J=S.Matrix([[0,S.Rational(1,2)],[-2,0]])
D=S.diag(I,-I);U=S.Matrix([[1,1],[2*I,-2*I]])
assert U*D==J*U
H=S.diag(2,S.Rational(1,2))
assert S.conjugate(U).T*H*U==4*S.eye(2)
print('balanced-action isogeny identity J*S=S*diag(i,-i) PASS')
print('per-pair degree =',S.expand(S.det(U)*S.conjugate(S.det(U))))

# Standard diagonal embedding: exact integral pullback and character-summand scale.
# New ordered generators are (A_j,B_j,C_j,D_j), with i^*A=-B,i^*B=A.
pullbacks=[];theta0={};Bd={};Dc=[];Qd=[]
for j in range(3):
 A,B,C,Dg=[e(4*j+k) for k in range(4)]
 pullbacks.extend([add(A,C),add(B,Dg),add(scale(B,-2),scale(Dg,2)),add(scale(A,2),scale(C,-2))])
 theta0=add(theta0,mul(A,B),mul(C,Dg))
 Dc.append(add(mul(A,Dg),scale(mul(B,C),-1)))
 Qd.append(add(mul(A,C),mul(B,Dg)))
 Bd=add(Bd,scale(Qd[-1],2))

def pull(poly):
 out={}
 for mask,c in poly.items():
  term={0:c}
  for j in range(12):
   if mask>>j&1:term=mul(term,pullbacks[j])
  out=add(out,term)
 return out

t_diag=scale(add(mul(mul(Dc[0],Dc[1]),Dc[2]),
 scale(mul(mul(Dc[0],Qd[1]),Qd[2]),-1),
 scale(mul(mul(Qd[0],Dc[1]),Qd[2]),-1),
 scale(mul(mul(Qd[0],Qd[1]),Dc[2]),-1)),-1)
assert len(t_diag)==32 and all(c in (S.Integer(1),S.Integer(-1)) for c in t_diag.values())
assert pull(t)==scale(t_diag,512)
assert pull(theta)==scale(theta0,8)
assert pull(scale(P,S.Rational(-1,2)))==Bd
assert mul(theta0,t_diag)=={}
assert power(t_diag,2)=={(1<<12)-1:S.Integer(-32)}
assert power(theta0,6)=={(1<<12)-1:S.factorial(6)}
diag_poly=add({0:S.Integer(4)},scale(power(theta0,2),-8),scale(power(theta0,4),S.Rational(8,3)),scale(power(theta0,6),S.Rational(-16,45)))
assert scale(pull(add(t,poly)),S.Rational(1,16))==add(scale(t_diag,32),diag_poly)
print('standard diagonal pullback and 1/16 character-summand identity PASS')
print('principal theta0 volume1; primitive t_diag has32 coefficients +/-1; T=32; Weil coefficient32')
