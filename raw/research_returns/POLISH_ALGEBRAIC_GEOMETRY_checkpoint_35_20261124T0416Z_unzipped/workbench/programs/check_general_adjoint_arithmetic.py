#!/usr/bin/env python3
"""General adjoint differential verifier (CC0 1.0).

Independent finite-field polynomial differentiation and integral Gram matrices.
These checks do not certify the geometric argument or extrapolate finite cases.
Run with Python 3 and SymPy; JSON is printed to stdout.
"""
import json
import sympy as sp

checks=[]
def zero(label,value,prime=None):
    value=sp.Poly(sp.expand(value),x,y,modulus=prime).as_expr() if prime else sp.factor(value)
    assert value==0,(label,value)
    checks.append(label)
def true(label,value):
    assert value,label
    checks.append(label)
x,y=sp.symbols('x y')
phi=x**3+y**3+x*y
eta_x=sp.diff(phi,x);eta_y=sp.diff(phi,y)
a=1+x+x*x*y
for p in (2,3,5,7,11):
    for conductor in (1,2,3):
        m=p*conductor
        alpha_x=a*y**(m-1)*eta_x
        alpha_y=a*y**(m-1)*eta_y
        direct=sp.diff(alpha_y,x)-sp.diff(alpha_x,y)
        bracket_x=y*sp.diff(a,x)
        bracket_y=y*sp.diff(a,y)-a
        divided=y**(m-2)*(bracket_x*eta_y-bracket_y*eta_x)
        zero(f'exact canonical derivative p={p},conductor={conductor}',direct-divided,p)
# Dividing a closed form by its divisorial zero part need not preserve closedness.
u=y*y;v=2*x*y
zero('closed exact form before saturation',sp.diff(v,x)-sp.diff(u,y),3)
true('nonclosed residual form after saturation',sp.Poly(sp.diff(v/y,x)-sp.diff(u/y,y),x,y,modulus=3).as_expr()==1)
# Strict-transform exceptional bases, computed from total-transform Gram matrix.
for n in range(1,9):
    change=sp.eye(n)
    for i in range(n-1):change[i,i+1]=-1
    gram=-change*change.T
    true(f'exceptional determinant n={n}',gram.det()==(-1)**n)
    w=sp.Matrix(sp.symbols('w0:'+str(n)))
    q=(w.T*gram*w)[0]
    zero(f'exceptional negative-square expansion n={n}',q+sum(z*z for z in change.T*w))
    D=sp.symbols('D')
    expanded=sp.diag(D,*([-1]*n))
    moved=sp.Matrix([1]+list(-change.T*w))
    zero(f'pullback and moving square n={n}',(moved.T*expanded*moved)[0]-(D+q))
# Restriction and exceptional-curve numerical relations.
m,d,z,t=sp.symbols('m d z t')
canonical_intersection=(m-1)*d+z+t
zero('adjoint degree on Y',canonical_intersection-(m-2)*d-z-(d+t))
c,h,z0,Ae=sp.symbols('c h z0 Ae')
zero('exceptional component multiplicity identity',(-1-(m-2)*h-(-c+z0))-(c-1-(m-2)*h-z0))
print(json.dumps({'verdict':'PASS','assertions':len(checks),'method':'direct finite-field polynomial derivatives and integral exceptional Gram matrices','scope':'Arithmetic only; no geometric or source theorem certification','checks':checks},indent=2))
