"""Exact local checks for A2-collar-shape; the global sign proof is analytic.

Checks the Fermi-graph curvature derivative, the boundary-layer PDE residual,
and the exact residual-integral constant. These identities are not a numerical
solution of the global Neumann problem and are not advertised as one.
"""
import json,time
import sympy as S
start=time.perf_counter()
e,a,ap,app,r,n,s=S.symbols('epsilon a ap app r n s',real=True)
f=S.cosh(e*a)
fp=S.sinh(e*a)
k=(fp*(f*f+2*(e*ap)**2)-f*e*app)/(f*f+(e*ap)**2)**S.Rational(3,2)
variation=S.simplify(S.diff(k,e).subs(e,0))
assert variation==a-app
w=(n+1/n)*S.exp(-n*r)*S.cos(n*s)
residual=S.diff(w,r,2)+S.tanh(r)*S.diff(w,r)+S.sech(r)**2*S.diff(w,s,2)-2*w
expected=w*(n*n*S.tanh(r)**2-n*S.tanh(r)-2)
assert S.simplify(S.expand_trig(residual-expected))==0
assert S.simplify((-S.diff(w,r)).subs(r,0)-(1+n*n)*S.cos(n*s))==0
t=S.symbols('t',nonnegative=True)
constant=S.integrate((t*t+t+2)**2*S.exp(-2*t),(t,0,S.oo))
assert constant==S.Rational(23,4)
print(json.dumps(dict(status='PASS',exact_identities=4,
 curvature_variation=str(variation),residual_integral=str(constant),
 scope='local symbolic identities only; no finite or numerical claim about the global metric',
 seconds=round(time.perf_counter()-start,6)),indent=2))
