#!/usr/bin/env python3
"""Universal linear algebra for the normalized-row tangent-triple construction."""
from pathlib import Path
from time import perf_counter
import json
import sympy as sp
started=perf_counter()
a01,a02,a10,a12=sp.symbols('a01 a02 a10 a12')
b00,b01,b02,b10,b11,b12,b20,b21,b22=sp.symbols('b00 b01 b02 b10 b11 b12 b20 b21 b22')
alpha,beta,r,s,k0,k1=sp.symbols('alpha beta r s k0 k1')
variables=(a01,a02,a10,a12,b00,b01,b02,b10,b11,b12,b20,b21,b22,alpha,beta,r,s,k0,k1)
def red(expr):return sp.Poly(sp.expand(expr),*variables,modulus=2).as_expr()
S=sp.Matrix([[0,alpha*b02,alpha*b01],[beta*b12,0,beta*b10],[r,s,0]])
assert all(S[i,i]==0 for i in range(3))
assert red((S*sp.Matrix([b00,b01,b02]))[0])==0
assert red((S*sp.Matrix([b10,b11,b12]))[1])==0
l0=(sp.Matrix([[0,a01,a02]])*S)[0]
l1=(sp.Matrix([[a10,0,a12]])*S)[1]
third=(S*sp.Matrix([b20,b21,b22]))[2]
assert red(l0-(a01*beta*b12+a02*r))==0
assert red(l1-(a10*alpha*b02+a12*s))==0
assert red(third-(r*b20+s*b21))==0
assert sp.Matrix([l0,l1]).jacobian([r,s]).det()==a02*a12
contact=red(alpha*k0*l1+beta*k1*l0)
assert red(sp.diff(contact,r)-beta*k1*a02)==0
assert red(sp.diff(contact,s)-alpha*k0*a12)==0
# The five actual linear constraints have a nonzero universal minor.
rows=[]
for col in [0,4,8]:rows.append([int(j==col) for j in range(9)])
rows.append([b00,b01,b02,0,0,0,0,0,0])
rows.append([0,0,0,b10,b11,b12,0,0,0])
constraints=sp.Matrix(rows)
minor=constraints[:,[0,4,8,2,5]]
assert red(minor.det()-b02*b12)==0
# In the original cubic coordinates the tangent-line quadratic coefficient
# at (x,y) is x^4+x.  The translated series is the previously proved
# universal invariant-parameter expansion.
x,y,t=sp.symbols('x y t')
xt=x+t+x*x*t*t
yt=y+x*x*t+x*t*t
line=(yt-y)+x*x*(xt-x)
assert sp.Poly(sp.expand(line-(x**4+x)*t*t),x,y,t,modulus=2).as_expr()==0
out={
    'status':'PASS',
    'scope':'Universal matrix and quadratic-coefficient identities; finite-exception and global-incidence arguments are separate proofs',
    'rank_five_minor_columns':[0,4,8,2,5],
    'rank_five_minor_determinant':'b02*b12',
    'first_gradients':[str(l0),str(l1)],
    'gradient_parameter_jacobian':'a02*a12',
    'contact_numerator':str(contact),
    'contact_r_coefficient':'beta*k1*a02',
    'contact_s_coefficient':'alpha*k0*a12',
    'third_vertical_derivative':str(third),
    'standard_tangent_quadratic':'x^4+x',
    'elapsed_seconds':perf_counter()-started,
}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
