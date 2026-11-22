#!/usr/bin/env python3
"""Exact finite certificates for the proper-K2 curve and C.3ad form formulas.

The general statements and all K-theory inputs are proved in the written
arguments. This program checks the stated polynomial identities and a finite
collection of exterior-form coordinate calculations only.
"""
from pathlib import Path
from time import perf_counter
from itertools import combinations
import json
import sympy as s

start = perf_counter()
a, b, c, f, g = s.symbols('a b c f g')
f0, f1, g0, g1 = s.symbols('f0 f1 g0 g1')
F = (f-1)**2*(g-1)**2-c*f*g
H = (f1-f0)**2*(g1-g0)**2-c*f1*f0*g1*g0
curve = {
    'specified_point': s.cancel(F.subs({f:a,g:b,c:(a-1)**2*(b-1)**2/(a*b)})) == 0,
    'f_zero_boundary': s.expand(H.subs(f1,0)-f0**2*(g1-g0)**2) == 0,
    'f_infinity_boundary': s.expand(H.subs(f0,0)-f1**2*(g1-g0)**2) == 0,
    'g_zero_boundary': s.expand(H.subs(g1,0)-g0**2*(f1-f0)**2) == 0,
    'g_infinity_boundary': s.expand(H.subs(g0,0)-g1**2*(f1-f0)**2) == 0,
    'smooth_Q_partial_f': s.diff(F,f).subs({f:0,g:1}) == -c,
    'smooth_Q_partial_g': s.diff(F,g).subs({f:0,g:1}) == 0,
    'local_unit_identity': s.cancel(f-(f-1)**2*(g-1)**2/(c*g)+F/(c*g)) == 0,
}
assert all(curve.values())

x = s.symbols('x0:4')
def clean(v):
    return {I:s.cancel(q) for I,q in v.items() if s.cancel(q) != 0}
def add(v,w):
    z=dict(v)
    for I,q in w.items(): z[I]=z.get(I,0)+q
    return clean(z)
def scale(v,q): return clean({I:q*r for I,r in v.items()})
def wedge(v,w):
    z={}
    for I,q in v.items():
        for J,r in w.items():
            if set(I)&set(J): continue
            sign=(-1)**sum(i>j for i in I for j in J)
            K=tuple(sorted(I+J))
            z[K]=z.get(K,0)+sign*q*r
    return clean(z)
def diff(v):
    z={}
    for I,q in v.items():
        for i,xi in enumerate(x):
            z=add(z,wedge({(i,):s.diff(q,xi)},{I:1}))
    return clean(z)

u=1+x[0]+x[1]*x[2]
du=diff({():u})
checks=[]
for degree in range(1,5):
    eta={I:(n+1)*(x[0]*x[1]+x[2]**2+x[3])
         for n,I in enumerate(combinations(range(4),degree-1))}
    omega={I:(n+2)*(x[1]+x[0]*x[3]**2)
           for n,I in enumerate(combinations(range(4),degree))}
    assert not diff(diff(eta))
    for j in range(1,8):
        transformed_h=add(scale(omega,u**j),scale(wedge(du,eta),u**(j-1)))
        transformed_v=scale(eta,u**j)
        projected=add(transformed_h,scale(diff(transformed_v),-s.Rational(1,j)))
        expected=scale(add(omega,scale(diff(eta),-s.Rational(1,j))),u**j)
        assert not add(projected,scale(expected,-1))
        exact_h=diff(eta)
        exact_v=scale(eta,j)
        assert not add(exact_h,scale(diff(exact_v),-s.Rational(1,j)))
        checks.append({'form_degree':degree,'internal_weight':j,'gluing':True,'exact_relation':True})

out={
    'curve_equation':'(f-1)^2(g-1)^2 = c*f*g',
    'curve_checks':curve,
    'form_checks':checks,
    'form_general_proof':'Projection omega-(1/j)d eta; coordinate cancellation follows from d(u^j eta)=j*u^(j-1)du wedge eta+u^j*d eta; remaining exact terms vanish by d^2=0.',
    'scope':'Finite symbolic checks only. Does not prove localization, Gersten, Goodwillie, Adams compatibility, KAN, algebraization or any unrestricted top Chow assertion.',
    'all_passed':True,
    'runtime_seconds':round(perf_counter()-start,6),
}
p=Path(__file__).with_name('top_quotient_aux_output.json')
p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
