"""Exact finite checks for the singular-base genus-one construction.

These verify the displayed elliptic plane cubic and fibre-product algebra.
The infinite-order cohomology class and torsor argument are proved in TeX.
"""
from itertools import product
from time import perf_counter
import sympy as sp

start = perf_counter()
x, y, z = sp.symbols('x y z')
F = y*y*z + y*z*z + x*x*x + x*x*z
partials = [sp.Poly(sp.diff(F, a), x, y, z, modulus=2).as_expr()
            for a in (x, y, z)]
G = sp.groebner(partials, x, y, z, modulus=2)
print('Field: F_2')
print('Cubic:', F)
print('Partial derivatives modulo 2:', partials)
print('Gradient ideal Groebner basis:', [g.as_expr() for g in G.polys])
assert set(g.as_expr() for g in G.polys) == {x*x, y*y, z*z}
print('Smoothness certificate: gradient radical is (x,y,z), so no projective singular point.')
points = [p for p in product(range(2), repeat=3)
          if p != (0, 0, 0) and int(F.subs(dict(zip((x, y, z), p)))) % 2 == 0]
print('All projective F_2 points:', points)
print('Point count:', len(points))
assert len(points) == 5
assert (0, 1, 0) in points

a, b, c, d, f, t = sp.symbols('a b c d f t')
reduced = sp.rem((a+b*t)*(c+d*t), t*t-f*t, t)
pair_product = (a*c, (a+f*b)*(c+f*d))
pair_of_reduced = (reduced.subs(t, 0), reduced.subs(t, f))
differences = tuple(sp.expand(u-v) for u, v in zip(pair_product, pair_of_reduced))
print('Product reduced modulo t(t-f):', reduced)
print('Difference from componentwise product under t -> (0,f):', differences)
assert differences == (0, 0)
print('Injectivity over a domain with f nonzero: (a,a+fb)=(0,0) forces a=b=0.')
print('Image is precisely pairs congruent modulo f; coefficient b is their divided difference.')
print('No numerical claim about Brauer infinitude is made by this example.')
print('Wall time seconds:', f'{perf_counter()-start:.6f}')
