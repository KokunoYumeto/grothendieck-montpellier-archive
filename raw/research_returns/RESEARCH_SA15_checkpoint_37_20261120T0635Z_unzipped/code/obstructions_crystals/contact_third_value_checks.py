#!/usr/bin/env python3
"""Exact contact-slice identities; geometry and pole-order arguments are separate."""
from pathlib import Path
from time import perf_counter
import json
import sympy as s
started=perf_counter()
x,y,z,w,a,b,c,d,T,h,F,U,v=s.symbols('x y z w a b c d T h F U v')
variables=(x,y,z,w,a,b,c,d,T,h,F,U,v)
relations=[y*y+y+x**3,w*w+w+z**3,b*b+b+a**3,d*d+d+c**3]
gb=s.groebner(relations,*variables,modulus=2)
def red(poly): return gb.reduce(s.expand(poly))[1]
X=x+a;Y=y+b;Z=z+c;ell=w+c*c*z+d*d;A1=Y+X*x*x
f=T*ell/A1
u=Z*Z*(T/X+h)
vv=T*Z**3/X+h*(z*z*Z+w+d)+f*X*X
section=(T+h*X)*ell+F*(Y+a*a*X)+v*X+U*X*Z
dx=s.diff(section,x)+x*x*s.diff(section,y)
dz=s.diff(section,z)+z*z*s.diff(section,w)
mixed=s.diff(dz,x)+x*x*s.diff(dz,y)
sub={F:f,U:u,v:vv}
checks={}
for name,expr in [
    ('section',section),('first_derivative',dx),('second_derivative',dz),
    ('mixed_hessian',mixed-T*Z*Z/X)]:
    numerator=s.fraction(s.together(expr.subs(sub,simultaneous=True)))[0]
    assert red(numerator)==0
    checks[name]=True
alpha,beta,gamma,delta,epsilon=s.symbols('alpha beta gamma delta epsilon')
linear=alpha*f+beta*T+gamma*u+delta*vv+epsilon*h
assert s.simplify(s.diff(linear,h)-(gamma*Z*Z+delta*(z*z*Z+w+d)+epsilon))==0
assert red(A1-(y*y+b+a*x*x))==0
C=T+h*a;EE=U+h*c*c;DD=v+U*c+h*d*d+F*a*a
BB=T*c*c+EE*a;AA=T*d*d+DD*a+F*b
S=s.Matrix([[AA,BB,C],[DD,EE,h],[F,0,0]])
assert red(S.det()-F*T*U)==0
opposite=section.subs({x:a,y:b+1,z:c,w:d+1},simultaneous=True)
assert red(opposite-F-T)==0
out={
    'status':'PASS',
    'scope':'Universal polynomial identities only; no geometric existence inferred from a finite computation',
    'moving_node_equations':checks,
    'linear_relation_h_coefficient':'gamma*(z+c)^2+delta*(z^2*(z+c)+w+d)+epsilon',
    'pole_orders_used_in_proof':[6,4,0],
    'first_factor_A1':'y^2+b+a*x^2',
    'contact_determinant':'F*T*U',
    'opposite_third_value':'F+T',
    'elapsed_seconds':perf_counter()-started,
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
