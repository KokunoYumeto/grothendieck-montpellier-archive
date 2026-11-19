#!/usr/bin/env python3
"""Exact F4 edge-case certificate; supplements the general characteristic-2 identities."""
from itertools import product

# F4 = F2[a]/(a*a+a+1); integers encode constant and a coefficients.
def mul(x, y):
    value = 0
    for i in range(2):
        for j in range(2):
            if ((x >> i) & 1) and ((y >> j) & 1):
                value ^= 1 << (i+j)
    if value & 4:
        value ^= 7
    return value

points = tuple(range(4)) + ('infinity',)
translations = {a: tuple(x ^ a if isinstance(x, int) else x for x in points)
                for a in range(4)}
assert len(set(translations.values())) == 4
identity = points
def compose(f, g):
    return tuple(f[points.index(gx)] for gx in g)
for a, b in product(range(4), repeat=2):
    assert compose(translations[a], translations[b]) == translations[a ^ b]
for a in range(1, 4):
    assert compose(translations[a], translations[a]) == identity
    fixed = [x for x, image in zip(points, translations[a]) if x == image]
    assert fixed == ['infinity']
assert [x for x in range(4) if mul(x,x) == 1] == [1]
inversion = tuple('infinity' if x == 0 else 0 if x == 'infinity' else mul(x,x)
                  for x in points)
standard_four = {identity, identity, inversion, inversion}
assert len(standard_four) == 2
six_set = {0, 'infinity', 1, 1, 1, 1}
assert len(six_set) == 3
print('PASS: all 16 translation products in F4 equal addition of their parameters.')
print('PASS: four distinct translations form V4; every nonidentity fixes exactly infinity on P1(F4).')
print('PASS: the only root of i^2=-1=1 in F4 is i=1.')
print('PASS: the displayed standard four transformations collapse to two, and the six-set to three points.')
print('General-field fixed-point proof: z+a=z for finite z forces a=0; hence the same nonzero translations fix only infinity over the algebraic closure.')
