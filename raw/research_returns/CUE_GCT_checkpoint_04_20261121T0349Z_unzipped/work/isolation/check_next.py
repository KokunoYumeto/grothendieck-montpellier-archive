"""Focused exact finite checks of I-14--I-18, not general proof certificates."""
from itertools import product, combinations
from math import comb
from pathlib import Path
from random import Random
import sympy as sp


def rank_mod(rows, p):
    if not rows:
        return 0
    a = [[int(x) % p for x in row] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][col]:
                scale = a[i][col]
                a[i] = [(x - scale * y) % p for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def rowmul(row, matrix, p):
    return [sum(row[k] * matrix[k][j] for k in range(len(row))) % p
            for j in range(len(row))]


rng = Random(141718)
lines = []
support = list(product(range(2), repeat=3))
weights = [(0, 1, 2), (2, 1, 0), (1, 0, 1)]
groups = []
for weight in weights:
    values = sorted(set(sum(x * y for x, y in zip(alpha, weight)) for alpha in support))
    groups.extend([[index for index, alpha in enumerate(support)
                    if sum(x * y for x, y in zip(alpha, weight)) == value]
                   for value in values])
for trial in range(40):
    p, r = 5, trial % 3 + 1
    while True:
        C = [[rng.randrange(p) for _ in support] for _ in range(r)]
        if rank_mod(C, p) == r:
            break
    compressed = [[sum(row[index] for index in group) % p for group in groups]
                  for row in C]
    full_rank = rank_mod(compressed, p) == r
    every_projection_survives = True
    for lam in product(range(p), repeat=r):
        if not any(lam):
            continue
        if not any(sum(lam[i] * compressed[i][j] for i in range(r)) % p
                   for j in range(len(groups))):
            every_projection_survives = False
            break
    assert full_rank == every_projection_survives
lines.append('PASS I-14: 40 exact F_5 joint-rank / all-functional equivalence checks')

C = sp.Matrix([[1, -1, 0], [0, 1, -1]])
P1 = sp.Matrix([[1, 0], [1, 0], [0, 1]])
P2 = sp.Matrix([[0, 1], [1, 0], [1, 0]])
assert (C * P1).rank() == (C * P2).rank() == 1
assert (C * P1).row_join(C * P2).rank() == 2
lines.append('PASS I-14: two rank-one compressions jointly preserve rank two')

# The actual same-alphabet Hoza decoder has the common scalar K times 6^nu_2(i).
def nu2(i):
    ans = 0
    while i % 2 == 0:
        i //= 2
        ans += 1
    return ans
for h0, h1 in product(range(20), repeat=2):
    w1 = 6 ** nu2(1) * (h1 - h0)
    w3 = 6 ** nu2(3) * (h1 - h0)
    assert w1 == w3
lines.append('PASS I-15: 400 decoder coefficient checks for x_1-x_3')

# A bounded affine decoder with 16 distinct directions in {-1,0,1}^3.
directions = list(product([-1, 0, 1], repeat=3))[:16]
assert 2 ** 16 > (2 * 16 + 1) ** 3
seen = {}
collision = None
for alpha in product(range(2), repeat=16):
    key = tuple(sum(alpha[i] * directions[i][j] for i in range(16)) for j in range(3))
    if key in seen:
        collision = seen[key], alpha
        break
    seen[key] = alpha
assert collision and collision[0] != collision[1]
for seed in product(range(2), repeat=2):
    weights = [row[0] + row[1] * seed[0] + row[2] * seed[1] for row in directions]
    assert sum(a * w for a, w in zip(collision[0], weights)) == sum(a * w for a, w in zip(collision[1], weights))
lines.append('PASS I-15: explicit affine-decoder Boolean-exponent collision verified on every binary seed')

for q, delta, n in [(2, 1, 3), (3, 1, 3), (3, 2, 3), (5, 2, 2), (5, 4, 2)]:
    roots = list(combinations(range(q), delta))
    models = list(product(roots, repeat=n))
    for point in product(range(q), repeat=n):
        hit_count = sum(all(point[i] not in rs[i] for i in range(n)) for rs in models)
        assert hit_count == comb(q - 1, delta) ** n
    assert len(models) == comb(q, delta) ** n
lines.append('PASS I-16: five exact finite root-set covering counts')

for trial in range(36):
    p = 101
    n, w, delta = 2 + trial % 5, 1 + trial % 4, 1 + trial % 2
    factors = []
    for _ in range(n):
        while True:
            constant = [[rng.randrange(p) for _ in range(w)] for _ in range(w)]
            if rank_mod(constant, p) == w:
                break
        factors.append([constant] + [[[rng.randrange(p) for _ in range(w)] for _ in range(w)]
                                      for _ in range(delta)])
    u = [1] + [0] * (w - 1)
    rows, low = [], []
    for alpha in product(range(delta + 1), repeat=n):
        row = u
        for i, exponent in enumerate(alpha):
            row = rowmul(row, factors[i][exponent], p)
        rows.append(row)
        if sum(exponent != 0 for exponent in alpha) <= w - 1:
            low.append(row)
    assert rank_mod(rows, p) == rank_mod(low, p)
lines.append('PASS I-17: 36 exact F_101 coefficient-span checks with arbitrary invertible constant matrices')

for w in range(2, 6):
    factors = []
    for i in range(w - 1):
        coeff = sp.zeros(w)
        coeff[i, i + 1] = 1
        factors.append((sp.eye(w), coeff))
    coefficients = []
    for alpha in product(range(2), repeat=w - 1):
        row = sp.eye(w)[0, :]
        for i, exponent in enumerate(alpha):
            row *= factors[i][exponent]
        value = row[0, w - 1]
        assert value == (1 if all(alpha) else 0)
        coefficients.append(value)
lines.append('PASS I-17: nilpotent-chain examples attain support w-1 for w=2..5')

eps = sp.Symbol('eps')
L0 = sp.Matrix([[0, 1], [0, 0]])
R0 = sp.Matrix([[1, 0], [0, 0]])
pair = (L0 + eps * sp.eye(2)) * (R0 + eps * sp.eye(2))
for m in range(1, 6):
    assert sp.expand((pair ** m)[0, 0] - eps ** m * (1 + eps) ** m) == 0
for m in [2, 3]:
    n = 2 * m
    for b in product(range(3), repeat=n):
        if sum(x != 0 for x in b) >= m:
            continue
        for a in range(3):
            x = [(a + value) % 3 for value in b]
            assert sp.prod((x[2*j + 1] - x[2*j]) % 3 for j in range(m)) % 3 == 0
lines.append('PASS I-18: regularized zero-value identity m=1..5 and complete small F_3 sparse perturbations')

Ceps = sp.Matrix([[1, 0, eps], [0, 1, 0]])
Peps = sp.Matrix([[0, 0], [0, 1], [1, 0]])
assert Ceps.subs(eps, 0).rank() == 2
assert (Ceps * Peps).det() == eps
assert (Ceps * Peps).subs(eps, 0).rank() == 1
lines.append('PASS I-18: generic full-rank compression with positive determinant valuation loses special-fiber rank')

result = '\n'.join(lines) + '\n'
Path(__file__).with_name('next_computation_checks.txt').write_text(result)
print(result, end='')
