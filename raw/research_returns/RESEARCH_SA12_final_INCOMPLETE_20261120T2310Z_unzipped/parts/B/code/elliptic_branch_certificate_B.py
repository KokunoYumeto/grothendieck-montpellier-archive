#!/usr/bin/env python3
"""Exact characteristic-three tangent/flex checks for the B.2q candidate.

The geometric proof uses the chord-and-tangent law.  These checks establish
the displayed equations for all geometric points, not only F3-rational ones.
"""
from pathlib import Path
import datetime
import json
import time
import sympy as sp

started=time.perf_counter()
x,y,u,m,a2,a4,a6=sp.symbols('x y u m a2 a4 a6')
checks=[]
def check(name,test):
    assert test,name
    checks.append(dict(name=name,passed=True))

# Substitute the line y+m(u-x) through (x,y) in the Weierstrass equation.
intersection=sp.Poly(u**3+a2*u**2+a4*u+a6-(y+m*(u-x))**2,
                     u,domain=sp.GF(3).poly_ring(x,y,m,a2,a4,a6))
check('quadratic coefficient is a2-m^2',sp.expand(intersection.nth(2))==a2-m*m)

f1=y*y-x**3+x
f2=y*y-x**3-x*x-1
# Slopes: E1 has m=-1/(2y), E2 has m=x/y.
g1=sp.groebner([f1,2*y*m+1,m*m],m,y,x,modulus=3)
check('E1 has no finite flex with nonzero y',list(g1)==[1])
g2=sp.groebner([f2,y*m-x,m*m-1],m,y,x,modulus=3,order='lex')
expected_full=sp.groebner([m+x*x*y,y*y-x*x,x**3+1],m,y,x,modulus=3,order='lex')
check('E2 full flex ideal retains cube thickening',tuple(g2.polys)==tuple(expected_full.polys))
g2_reduced=sp.groebner(list(g2)+[x+1],m,y,x,modulus=3,order='lex')
expected=sp.groebner([m+y,y*y-1,x+1],m,y,x,modulus=3,order='lex')
check('E2 reduced flex ideal is x=-1,y=+-1,m=-y',tuple(g2_reduced.polys)==tuple(expected.polys))

flex_points=[(2,1,2),(2,2,1)]
for i,(xp,yp,mp) in enumerate(flex_points):
    value=sp.Poly((u**3+u*u+1-(yp+mp*(u-xp))**2)-(u-xp)**3,u,modulus=3)
    check('E2 tangent triple-intersection point'+str(i),value.is_zero)

# Smoothness in affine charts; the point at infinity is common and smooth.
check('E1 affine singular ideal is unit',list(sp.groebner(
    [f1,sp.diff(f1,x),sp.diff(f1,y)],x,y,modulus=3))==[1])
check('E2 affine singular ideal is unit',list(sp.groebner(
    [f2,sp.diff(f2,x),sp.diff(f2,y)],x,y,modulus=3))==[1])
X,Y,Z=sp.symbols('X Y Z')
for i,F in enumerate([Y*Y*Z-X**3+X*Z**2,
                      Y*Y*Z-X**3-X*X*Z-Z**3],1):
    check('E'+str(i)+' point at infinity is smooth',
          sp.diff(F,Z).subs({X:0,Y:1,Z:0})==1)

counts=[]
for rhs in [x**3-x,x**3+x*x+1]:
    affine=[(a,b) for a in range(3) for b in range(3)
            if (b*b-int(rhs.subs(x,a)))%3==0]
    counts.append(len(affine)+1)
check('F3 point counts are4 and6',counts==[4,6])

out=dict(certificate='ordinary and supersingular elliptic branches in characteristic3',
         utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
         sympy_version=sp.__version__,checks=checks,
         E1_finite_geometric_3torsion=[],E2_finite_geometric_3torsion=[[2,1],[2,2]],
         E2_full_flex_groebner_basis=[str(z.as_expr()) for z in g2.polys],
         F3_point_counts=counts,elapsed_seconds=time.perf_counter()-started,
         limitation='This certificate verifies elliptic factors; the threefold geometry and cofinal-diagram conclusion are separate proofs.')
path=Path(__file__).resolve().parent/'output'/'elliptic_branch_certificate_B.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
