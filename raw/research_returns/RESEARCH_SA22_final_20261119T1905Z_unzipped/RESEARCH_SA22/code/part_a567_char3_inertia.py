#!/usr/bin/env python3
"""Exact certificate for the merged exceptional four-point orbit in char3."""
from itertools import product

p=3
points=((1,0),(0,1),(1,1),(2,1))
def norm(v):
    for c in v:
        if c%p:
            a=pow(c,-1,p)
            return tuple(a*x%p for x in v)
    raise ValueError('zero projective vector')

matrices=set()
permutations=set()
for a,b,c,d in product(range(p),repeat=4):
    if (a*d-b*c)%p==0:
        continue
    m=norm((a,b,c,d))
    matrices.add(m)
    images=tuple(norm((a*x+b*y,c*x+d*y)) for x,y in points)
    assert set(images)==set(map(norm,points))
    permutations.add(images)
assert len(matrices)==len(permutations)==24
lam=2
inv=lambda x:pow(x%p,-1,p)
values=(lam,(1-lam)%p,inv(lam),inv(1-lam),lam*inv(lam-1)%p,(lam-1)*inv(lam)%p)
assert values==(2,)*6
print('PGL2(F3): 24 distinct projective matrices and 24 permutations of P1(F3).')
print('All six anharmonic transformations fix lambda=-1=2:',values)
print('Exceptional inertia in characteristic3 is S4, order24. PASS')
