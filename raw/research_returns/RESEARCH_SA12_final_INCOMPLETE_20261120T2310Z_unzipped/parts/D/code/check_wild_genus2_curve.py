#!/usr/bin/env python3
"""Exact F_2 certificates for the wild genus-two exceptional-curve example."""
import json
import time
from pathlib import Path
import sympy as sp

started = time.perf_counter()
a,b,t,c,d,x,y,z,u,v,r,s,q = sp.symbols('a b t c d x y z u v r s q')
checks = []

def zero(label, expr, variables):
    numerator = sp.cancel(expr).as_numer_denom()[0]
    remainder = sp.Poly(numerator, *variables, modulus=2)
    assert remainder.is_zero, (label, remainder.as_expr())
    checks.append(label)

F = b**2 + (t**5+t**2*a**2)*b + a**5
H = d**2 + (c**4+t**3+t**4*c**2)*d + t*c**5+t**2*c**7+t**4*c**6+t**6*c**5
A = c**2+t**2*c
B = t**2*d+c**5
zero('finite-map identity F(A,B,t)=t^4 H', F.subs({a:A,b:B})-t**4*H, (c,d,t))
zero('target derivative a', sp.diff(F,a)-a**4, (a,b,t))
zero('target derivative b', sp.diff(F,b)-t**2*(a**2+t**3), (a,b,t))
zero('target derivative t', sp.diff(F,t)-b*t**4, (a,b,t))
zero('source derivative c', sp.diff(H,c)-c**4*t*(c**2*t+t**5+1), (c,d,t))
zero('source derivative d', sp.diff(H,d)-(c**4+c**2*t**4+t**3), (c,d,t))
zero('source derivative t', sp.diff(H,t)-(c**5+d*t**2), (c,d,t))
zero('source Jacobian excludes c,t nonzero',
     t**2*((t**4+t**-1)**2+t**4*(t**4+t**-1)+t**3)-1, (t,))
zero('special source equation', H.subs(t,0)-d*(d+c**4), (c,d))
zero('special target equation', F.subs(t,0)-(b**2+a**5), (a,b))
zero('special differential db/dc', sp.diff(B,c).subs(t,0)-c**4, (c,))

cp = c+t**2
dp = d+c**4+t**6*c+t**8
zero('deck action preserves a', A.subs(c,cp)-A, (c,t))
zero('deck action preserves b', t**2*dp+cp**5-B, (c,d,t))
zero('deck action preserves source equation', H.subs({c:cp,d:dp}, simultaneous=True)-H, (c,d,t))
zero('deck involution c', cp.subs(c,cp)-c, (c,t))
zero('deck involution d', dp.subs({c:cp,d:dp}, simultaneous=True)-d, (c,d,t))

G = y**2+(1+t*x**2)*y+x**5
Ginf = v**2+(u**3+t*u)*v+u
zero('weighted t chart', F.subs({a:t**2*x,b:t**5*y})-t**10*G, (t,x,y))
zero('proper curve chart gluing', x**6*Ginf.subs({u:1/x,v:y/x**3})-G, (t,x,y))
zero('Cech torsor gluing', x**4*((y/x**2)**2+t*y/x**2+x+y/x**4)-G, (t,x,y))
zero('Frobenius first basis relation', x**2*((y/x)**2+y/x**2+t*y+x**3)-G, (t,x,y))
zero('formal infinity divisibility', Ginf-(u*(1+t*v+u**2*v)+v**2), (t,u,v))

J = q**2*(1+q+r*s**2)+s**5
zero('weighted infinity chart', F.subs({a:r**2*q,b:r**5*q**2,t:r*s})-r**10*q**2*J, (r,s,q))
zero('infinity chart derivative q is a unit', sp.diff(J,q)-q**2, (r,s,q))
zero('infinity exceptional point', J.subs({r:0,s:0,q:1}), (q,))
zero('different of fierce extension', sp.diff(z**2+t*z+x,z)-t, (x,t,z))

weights = {a:2,b:5,t:1}
monomial_weights = []
for monomial, coefficient in sp.Poly(F,a,b,t,modulus=2).terms():
    monomial_weights.append(sum(e*weights[w] for e,w in zip(monomial,(a,b,t))))
assert sorted(monomial_weights)==[10,10,10,11]
checks.append('target has three weight10 terms and one weight11 term')

output = {
  'characteristic': 2,
  'assertions_passed': len(checks),
  'elapsed_seconds': time.perf_counter()-started,
  'checks': checks,
  'scope': 'Exact finite polynomial and chart certificates only; the paper supplies integrality, properness, genus, and ramification proofs.'
}
out = Path(__file__).resolve().parents[1]/'output'/'wild_genus2_curve.json'
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
