#!/usr/bin/env python3
"""Exact finite algebra checks for B.2p; the geometric proof is in the paper.

All polynomial calculations are over F_3.  The finite field is represented
as F_3[x,y]/(x^3-x+1,y^2+1), of dimension six over F_3.  The two factors
have coprime degrees and are irreducible, so their tensor product is F_729.
"""
from itertools import combinations
from pathlib import Path
import datetime
import json
import time
import sympy as sp

start = time.perf_counter()
checks = []

def check(name, value):
    assert value, name
    checks.append(dict(name=name, passed=True))

X,Y,Z,W,V,x,y,w,v,t,s,q,h = sp.symbols('X Y Z W V x y w v t s q h')
F = Y**2*Z-X**3+X*Z**2
Q = Y**2+Z**2
G = V**3-W*Q
variables = (X,Y,Z,W,V)
reduce3 = lambda f: sp.Poly(f, *variables, modulus=3).as_expr()
check('homogeneous gradient of elliptic cubic',
      tuple(reduce3(sp.diff(F,z)) for z in variables) ==
      (Z**2,-Y*Z,-X*Z+Y**2,0,0))
check('homogeneous gradient of pure-cover equation',
      tuple(reduce3(sp.diff(G,z)) for z in variables) ==
      (0,W*Y,W*Z,-Y**2-Z**2,0))
check('no singular point of E on Z=0',
      sp.expand(F.subs(Z,0)) == -X**3 and
      sp.diff(F,Z).subs({X:0,Z:0}) == Y**2)
check('Q nonzero at the point of E with Z=0', Q.subs({Y:1,Z:0}) == 1)

f = y*y-x**3+x
g = v**3-w*(y*y+1)
affine_vars = (x,y,w,v)
jac = sp.Matrix([[sp.diff(f,z) for z in affine_vars],
                 [sp.diff(g,z) for z in affine_vars]])
minors = [jac[:,list(pair)].det() for pair in combinations(range(4),2)]
gb = sp.groebner([f,g]+minors, v,w,y,x, modulus=3, order='lex')
expected = [v**3,w,y*y+1,x**3-x+1]
gb_expected = sp.groebner(expected,v,w,y,x,modulus=3,order='lex')
check('affine singular-locus ideal is exact',
      tuple(gb.polys) == tuple(gb_expected.polys))
px = sp.Poly(x**3-x+1,x,modulus=3)
py = sp.Poly(y*y+1,y,modulus=3)
check('cubic irreducible over F3', px.is_irreducible)
check('quadratic irreducible over F3', py.is_irreducible)
check('cubic separable', sp.gcd(px,px.diff()).degree() == 0)
check('quadratic separable', sp.gcd(py,py.diff()).degree() == 0)
transverse_det = sp.Poly(sp.diff(f,x)*sp.diff(y*y+1,y),x,y,modulus=3).as_expr()
check('intersection transverse',
      sp.rem(sp.Poly(y*transverse_det,y,modulus=3),py).as_expr() == 1)

# Basis x^i y^j, index i+3j, 0<=i<3 and 0<=j<2.
def digits(n):
    result = []
    for _ in range(6):
        result.append(n % 3)
        n //= 3
    return result

def encode(a):
    return sum((c % 3)*3**i for i,c in enumerate(a))

basis_product = {}
for i in range(6):
    for j in range(6):
        xi, yi = i % 3, i // 3
        xj, yj = j % 3, j // 3
        poly = sp.Poly(x**(xi+xj),x,modulus=3).rem(px)
        yc = 1 if yi+yj < 2 else 2
        yd = (yi+yj) % 2
        a = [0]*6
        for (xd,),c in poly.terms():
            a[xd+3*yd] = int(c)*yc % 3
        basis_product[i,j] = a

all_digits = [digits(n) for n in range(729)]
def add(a,b):
    return encode([u+v for u,v in zip(all_digits[a],all_digits[b])])
def neg(a):
    return encode([-u for u in all_digits[a]])
def mul(a,b):
    result = [0]*6
    for i,ai in enumerate(all_digits[a]):
        for j,bj in enumerate(all_digits[b]):
            if ai and bj:
                for k,c in enumerate(basis_product[i,j]):
                    result[k] += ai*bj*c
    return encode(result)
def power(a,n):
    r = 1
    while n:
        if n & 1:
            r = mul(r,a)
        a = mul(a,a)
        n >>= 1
    return r

check('every nonzero field element has order dividing728',
      all(power(a,728) == 1 for a in range(1,729)))
xroots = [a for a in range(729) if add(add(power(a,3),neg(a)),1) == 0]
yroots = [a for a in range(729) if add(power(a,2),1) == 0]
check('exactly three cubic roots in F729',len(xroots) == 3)
check('exactly two quadratic roots in F729',len(yroots) == 2)
points = [(a,b) for a in xroots for b in yroots]
check('six distinct geometric intersection points',len(set(points)) == 6)
check('all six satisfy E and Q',all(
    add(add(power(b,2),neg(power(a,3))),a) == 0 and
    add(power(b,2),1) == 0 for a,b in points))
check('all six have nonzero transverse derivative',all(b != 0 for a,b in points))

check('normalization substitution satisfies cusp equation',
      sp.cancel((s**3-t**2*q).subs({t:h**3/q**2,s:h**2/q})) == 0)
check('integral element cube identity',
      sp.rem(sp.Poly(s**6-t**4*q**2,s),sp.Poly(s**3-t**2*q,s)).as_expr() == 0)
semigroup = {2*i+3*j for i in range(12) for j in range(12)}
check('cusp valuation semigroup omits1',1 not in semigroup and 2 in semigroup and 3 in semigroup)

out = dict(certificate='B.2p abelian-target graph counterexample',
           utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
           sympy_version=sp.__version__, characteristic=3,
           finite_field_order=729, checks=checks,
           affine_singular_groebner_basis=[str(z.as_expr()) for z in gb.polys],
           six_points_basis_codes=points,
           elapsed_seconds=time.perf_counter()-start,
           limitation='Finite algebra certificate; geometric normality and the modification obstruction are proved separately in the paper.')
path=Path(__file__).resolve().parent/'output'/'abelian_graph_certificate_B.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
