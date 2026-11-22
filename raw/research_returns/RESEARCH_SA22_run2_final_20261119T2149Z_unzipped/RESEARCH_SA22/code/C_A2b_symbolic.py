#!/usr/bin/env python3
"""Exact rational certificates for the explicit Strebel and covering formulas.
No numerical evidence is used to establish the general energy/image theorems.
"""
import json,time
import sympy as s
start=time.monotonic()
u,z,w=s.symbols('u z w')
f=4*u/(1+u)**2
one=s.factor(s.diff(f,u)**2/(f**2*(f-1)))
g=u/(1+u)
two=s.factor(-s.diff(g,u)**2/(g**2*(g-1)**2))
a0,a1,ai=s.symbols('a0 a1 ai')
y0,y1,yi=s.symbols('y0 y1 yi')
upstairs=4*a0*y0/2+a1*(y1-s.log(2))+a1*(y1-s.log(2))+4*ai*yi/2
wanted=2*(a0*y0+a1*y1+ai*yi-a1*s.log(2))
assert one==-1/u**2
assert two==-1/u**2
assert s.diff(f,u).subs(u,0)==4
assert s.diff(g,u).subs(u,0)==1
assert s.simplify(upstairs-wanted)==0
print(json.dumps({'coefficient_domain':'Q(a0,a1,ai,y0,y1,yi,log2,u)',
 'one_weight_pullback':str(one),'one_weight_radius':4,
 'two_equal_weight_pullback':str(two),'two_equal_weight_radius':1,
 'cover_weighted_sum_difference':str(s.simplify(upstairs-wanted)),
 'checks':5,'runtime_seconds':time.monotonic()-start},indent=2))
