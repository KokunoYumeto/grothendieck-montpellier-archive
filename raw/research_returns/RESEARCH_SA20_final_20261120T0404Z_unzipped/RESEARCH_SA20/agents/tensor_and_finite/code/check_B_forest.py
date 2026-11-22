"""Exact finite certificates for the infinite construction in B.067.

These checks verify the finite algebra identities and transition maps.
The infinite direct limit, colon calculations and nonflatness are proved
in part_B.tex, not inferred from these finite bounds.
"""
from itertools import product


def product_monomial(a, b):
    return None if a & b else a | b


def row_basis(rows):
    pivots = {}
    for row in rows:
        while row:
            p = row.bit_length() - 1
            if p in pivots:
                row ^= pivots[p]
            else:
                pivots[p] = row
                break
    return pivots


def reduce_vector(row, pivots):
    while row:
        p = row.bit_length() - 1
        if p not in pivots:
            return row
        row ^= pivots[p]
    return 0


transition_monomials = transition_products = 0
for old in range(4):
    for leaves in range(1, 7):
        def image(mask):
            out = mask & ((1 << old) - 1)
            for j in range(leaves):
                if mask & (1 << (old + j)):
                    out |= 7 << (old + 3 * j)
            return out
        masks = list(range(1 << (old + leaves)))
        images = [image(a) for a in masks]
        assert len(set(images)) == len(masks)
        transition_monomials += len(masks)
        for a, b in product(masks, repeat=2):
            ab = product_monomial(a, b)
            actual = product_monomial(images[a], images[b])
            assert actual == (None if ab is None else images[ab])
            transition_products += 1
print('PASS injective squarefree transitions:', transition_monomials,
      'monomials;', transition_products, 'monomial products')

# One finite branching level: S=F2[x,l,r]/(x^2,l^2,r^2),
# R is spanned by 1,x,xl,xr. This does not assert the finite map is epic.
base = [0, 1, 3, 5]
relations = []
for scalar, a, b in product(base, range(8), range(8)):
    row = 0
    left = product_monomial(scalar, a)
    right = product_monomial(scalar, b)
    if left is not None:
        row ^= 1 << (8 * left + b)
    if right is not None:
        row ^= 1 << (8 * a + right)
    relations.append(row)
pivots = row_basis(relations)
delta_root = (1 << (8 * 7)) ^ (1 << 7)
delta_leaf = (1 << (8 * 2)) ^ (1 << 2)
assert reduce_vector(delta_root, pivots) == 0
assert reduce_vector(delta_leaf, pivots) != 0
print('PASS finite branching tensor shuffle: 256 balancing relations;',
      'tensor dimension', 64 - len(pivots),
      '; root difference zero, leaf difference nonzero')

# Values at 0,1 and derivatives at 0,1, on 1,X,X^2,X^3.
hermite = [1, 15, 2, 10]
assert len(row_basis(hermite)) == 4
rows = [1]
size = 1
for n in range(1, 4):
    new = []
    for old_row in rows:
        for small_row in hermite:
            row = 0
            for i in range(size):
                if old_row & (1 << i):
                    row |= small_row << (4 * i)
            new.append(row)
    rows = new
    size *= 4
    assert len(row_basis(rows)) == size
    print('PASS Hermite interpolation:', n, 'variables; rank', size)


def add(*polys):
    ans = set()
    for poly in polys:
        ans.symmetric_difference_update(poly)
    return ans


def mul(a, b):
    ans = set()
    for x, y in product(a, b):
        exponent = (x[0] + y[0], x[1] + y[1])
        if exponent in ans:
            ans.remove(exponent)
        else:
            ans.add(exponent)
    return ans


def power(poly, n):
    ans = {(0, 0)}
    for _ in range(n):
        ans = mul(ans, poly)
    return ans


x, y = {(1, 0)}, {(0, 1)}
qx = add(power(x, 4), power(x, 2))
qy = add(power(y, 4), power(y, 2))
assert add(power(add(x, y), 4), power(add(x, y), 2)) == add(qx, qy)
assert add(power(mul(x, y), 4), power(mul(x, y), 2)) == add(
    mul(qx, qy), mul(qx, power(y, 2)), mul(power(x, 2), qy))
print('PASS exact additive and multiplicative Q=X^4+X^2 identities')
print('All finite certificates passed; infinite assertions require the written proof.')
