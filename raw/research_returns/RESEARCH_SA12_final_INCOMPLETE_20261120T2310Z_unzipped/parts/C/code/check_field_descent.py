#!/usr/bin/env python3
"""Exact finite-group and field-algebra checks for C:field-descent.

These certificates check all nine vectors, all four lines, the cyclic
quartic defining algebra, the displayed 3-isogeny identity and GF(25).
Geometric connectedness and the induced-torsor argument are proved in TeX.
"""
import json
import time
import itertools
import sympy as sp

started=time.perf_counter()
V=list(itertools.product(range(3),repeat=2))
def T(v): return ((-v[1])%3,v[0])
def neg(v): return ((-v[0])%3,(-v[1])%3)
assert all(T(T(v))==neg(v) for v in V)
lines={tuple(sorted({(0,0),v,neg(v)})) for v in V if v!=(0,0)}
assert len(lines)==4
assert all({T(v) for v in line}!=set(line) for line in lines)
assert all({T(T(v)) for v in line}==set(line) for line in lines)
assert all(a*a%3==1 for a in (1,2))

r=sp.symbols('r')
f=sp.Poly(r**4-4*r*r+2,r,domain=sp.QQ)
assert f.is_irreducible
def red(g): return sp.rem(sp.Poly(g,r,domain=sp.QQ),f).as_expr()
s=r**3-3*r
assert red(f.as_expr().subs(r,s))==0
assert red(s.subs(r,s))==-r
assert red((r*r-2)**2)==2
assert red((r*r-2).subs(r,s))==-(r*r-2)
assert red((2+(r*r-2)))==r*r

x,y,b=sp.symbols('x y b')
identity=y*y*(x**3-8*b)**2-(x**3+4*b)**3+27*b*x**6
assert sp.Poly(sp.expand(identity.subs(y*y,x**3+b)),x,b).is_zero

# GF(25)=GF(5)[u]/(u^2-2).
def mul(a,b): return ((a[0]*b[0]+2*a[1]*b[1])%5,
                     (a[0]*b[1]+a[1]*b[0])%5)
def power(a,n):
    z=(1,0)
    while n:
        if n&1: z=mul(z,a)
        a=mul(a,a); n//=2
    return z
F25=list(itertools.product(range(5),repeat=2))
u=(0,1)
assert not any(a*a%5==2 for a in range(5))
assert all(power(a,25)==a for a in F25)
assert power(u,12)==(4,0)
assert u not in {mul(a,a) for a in F25}
assert len({mul(a,a) for a in F25 if a!=(0,0)})==12

output={
  'finite_group': {'vectors_checked':len(V),'lines_checked':len(lines),
      'matrix_T':[[0,2],[1,0]],'T_squared':'-identity',
      'T_stable_order_3_subgroups':0,'T_squared_stable_order_3_subgroups':4,
      'order_3_descent_obstruction':'Every scalar automorphism in F3* squares to +1, whereas restriction requires -1.'},
  'cyclic_quartic': {'polynomial':str(f.as_expr()),'irreducible_over_Q':True,
      'sigma_r':str(s),'sigma_squared_r':'-r',
      'quadratic_subfield_generator':'r^2-2','generator_square':2,
      'sigma_on_quadratic_subfield':'negation'},
  'isogeny': {'source':'y^2=x^3+b','target':'Y^2=X^3-27b',
      'X':'(x^3+4b)/x^2','Y':'y*(x^3-8b)/x^3',
      'cleared_equation_residue':'0'},
  'finite_field': {'field':'GF(5)[u]/(u^2-2)','elements_checked':len(F25),
      'u_power_12':list(power(u,12)),'u_is_nonsquare':True},
  'elapsed_seconds':time.perf_counter()-started,
  'scope':'Exact finite algebra and all subgroup lines; global geometry and torsor minimality are proved in paper_C.tex.'}
print(json.dumps(output,indent=2))
