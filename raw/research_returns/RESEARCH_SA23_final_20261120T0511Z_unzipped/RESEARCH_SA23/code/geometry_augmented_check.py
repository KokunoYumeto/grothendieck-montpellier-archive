"""Finite certificate for the augmented/unaugmented jet-group distinction.

A=F_2[e]/(e^2) has four elements, represented by bits 1,e.
R=A[t]/(t^2) has sixteen elements, represented by pairs (constant,linear).
All unital A-algebra automorphisms t -> a*t+b are enumerated.
"""
from itertools import product, permutations
from time import perf_counter

start = perf_counter()
A = tuple(range(4))
def add(x, y): return x ^ y
def mul(x, y):
    return ((x & 1) * (y & 1)) | (((((x >> 1) & 1) * (y & 1)) ^ ((x & 1) * ((y >> 1) & 1))) << 1)
def radd(x, y): return (add(x[0], y[0]), add(x[1], y[1]))
def rmul(x, y):
    return (mul(x[0], y[0]), add(mul(x[0], y[1]), mul(x[1], y[0])))
R = tuple(product(A, repeat=2))
units = tuple(a for a in A if any(mul(a, c) == 1 for c in A))
square_zero = tuple(b for b in A if mul(b, b) == 0)
H = tuple(product(units, square_zero))
def subst(h, x):
    a, b = h
    return (add(x[0], mul(x[1], b)), mul(x[1], a))
def comp(h, k):
    # Affine actions h(k(v)); opposite substitution convention has same group.
    a, b = h; c, d = k
    return (mul(a, c), add(mul(a, d), b))
for h in H:
    assert len({subst(h, x) for x in R}) == 16
    for x, y in product(R, repeat=2):
        assert subst(h, radd(x, y)) == radd(subst(h, x), subst(h, y))
        assert subst(h, rmul(x, y)) == rmul(subst(h, x), subst(h, y))
for h, k in product(H, repeat=2): assert comp(h, k) in H
def affine(h, v): return add(mul(h[0], v), h[1])
def linear(h, v): return mul(h[0], v)
for action in (affine, linear):
    for h, k, v in product(H, H, A):
        assert action(comp(h, k), v) == action(h, action(k, v))
for h in H:
    if h[1] == 0:
        assert all(affine(h, v) == linear(h, v) for v in A)
translation = (1, 2)
assert subst(translation, (0, 1))[0] == 2  # augmentation changes from0 toe
assert affine(translation, 0) == 2 and linear(translation, 0) == 0
equivariant_bijections = [p for p in permutations(A)
    if all(p[affine(h, v)] == linear(h, p[v]) for h, v in product(H, A))]
assert not equivariant_bijections
print('A_elements', len(A), 'R_elements', len(R), 'H_automorphisms', len(H))
print('addition_checks', len(H)*len(R)**2, 'multiplication_checks', len(H)*len(R)**2)
print('composition_checks', len(H)**2, 'action_law_checks', 2*len(H)**2*len(A))
print('bijections_checked', 24, 'equivariant_bijections', len(equivariant_bijections))
print('nonaugmented_translation_t_to_t_plus_e', 'verified')
print('elapsed_seconds', round(perf_counter()-start, 6))
