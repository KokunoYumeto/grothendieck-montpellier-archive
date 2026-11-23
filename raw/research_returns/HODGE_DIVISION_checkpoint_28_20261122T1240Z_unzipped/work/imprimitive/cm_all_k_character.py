#!/usr/bin/env python3
"""Exact symbolic-d certificate for HD-N07, over Q(d,s), s^2=-d."""
from cm_complex_character import S, I, add, scale, mul, power, exp, e, wedge, integrate_cd

d=S.Symbol('d',positive=True,integer=True)
s=I*S.sqrt(d)

def clean(poly):
 return {m:S.simplify(c) for m,c in poly.items() if S.simplify(c)!=0}

def same(a,b):
 assert clean(add(a,scale(b,-1)))=={}

Pout=add(wedge(0,3),scale(wedge(1,2),-1))
theta_out=add(scale(wedge(0,1),4*d),wedge(2,3))
for a,b in ((s,s),(-s,-s),(s,-s),(-s,s)):
 hxy=mul(add(e(0),e(2)),add(e(1),e(3)))
 pin=add(wedge(2,5),scale(wedge(3,4),-1))
 exponent=add(scale(hxy,2*a),scale(wedge(2,3),2*b),scale(pin,-1))
 out=mul(exp(scale(Pout,S.Rational(-1,2)),4),integrate_cd(exp(exponent,6)))
 expected=scale(exp(scale(theta_out,a/(4*d)),4),4*a) if a==b else add(scale(wedge(0,1),4*d),scale(Pout,2*a),scale(wedge(2,3),-1))
 same(out,expected)
print('all four symbolic-d one-pair Fourier identities PASS')

theta={}; wp={0:S.Integer(1)};wm={0:S.Integer(1)}
for j in range(3):
 a,b,u,v=[4*j+k for k in range(4)]
 ab=wedge(a,b);uv=wedge(u,v);p=add(wedge(a,v),scale(wedge(b,u),-1))
 theta=add(theta,scale(ab,4*d),uv)
 wp=mul(wp,add(scale(ab,4*d),scale(p,2*s),scale(uv,-1)))
 wm=mul(wm,add(scale(ab,4*d),scale(p,-2*s),scale(uv,-1)))
t=clean(scale(add(wp,wm),S.Rational(-1,2)))
alpha=(1+1/s)/2;beta=(1-1/s)/2
raw=add(scale(exp(scale(theta,s/(4*d)),12),-alpha**2*(4*s)**3),scale(exp(scale(theta,-s/(4*d)),12),-beta**2*(-4*s)**3),scale(add(wp,wm),-alpha*beta))
poly=add({0:64*d},scale(theta,-8*(d-1)),scale(power(theta,2),-2),scale(power(theta,3),(d-1)/(12*d)),scale(power(theta,4),1/(96*d)),scale(power(theta,5),-(d-1)/(3840*d**2)),scale(power(theta,6),-1/(46080*d**2)))
same(raw,add(scale(t,(d+1)/(2*d)),poly))
same(mul(theta,t),{})
same(power(t,2),{(1<<12)-1:-2048*d**3})
same(power(theta,6),{(1<<12)-1:64*d**3*S.factorial(6)})
uvmask=sum((1<<(4*j+2))+(1<<(4*j+3)) for j in range(3))
assert t[uvmask]==1
assert all(S.Poly(c,d).domain.is_ZZ for c in t.values())
print('whole symbolic-d character, integral primitive t, norm and volume PASS')
J=S.Matrix([[0,S.Rational(1,2)],[-2*d,0]])
H=S.diag(4*d,1)
assert J*J==-d*S.eye(2)
assert J.T*H+H*J==S.zeros(2)
group_map=S.Matrix([[1,-1],[2,2],[-2,0],[0,1]])
left_inverse=S.Matrix([[1,0,0,1],[0,0,0,1]])
assert left_inverse*group_map==S.eye(2)
print('J_d^2=-d, Rosati skew-adjointness, actual group-map left inverse PASS')
