"""Exact finite-field certificate for the quintic residual group.

Uses only finite arithmetic over F_81. The separate CM reciprocity
argument identifies this group with the arithmetic residual image.
"""

from collections import Counter
import hashlib
import json
from pathlib import Path


def digits(a):
    r = []
    for _ in range(4):
        r.append(a % 3)
        a //= 3
    return r


def encode(v):
    return sum((x % 3) * 3**i for i, x in enumerate(v))


def add(a, b):
    return encode([x + y for x, y in zip(digits(a), digits(b))])


def neg(a):
    return encode([-x for x in digits(a)])


def mul(a, b):
    x, y = digits(a), digits(b)
    v = [0] * 7
    for i in range(4):
        for j in range(4):
            v[i + j] += x[i] * y[j]
    # z^4 + z^3 + z^2 + z + 1 = 0.
    for k in range(6, 3, -1):
        t = v[k]
        for j in range(4):
            v[k - 4 + j] -= t
    return encode(v[:4])


def power(a, n):
    r = 1
    while n:
        if n & 1:
            r = mul(r, a)
        a = mul(a, a)
        n //= 2
    return r


def trace(a):
    r = 0
    for i in range(4):
        r = add(r, power(a, 3**i))
    assert r in (0, 1, 2)
    return r


def compose(g, h):
    a, i = g
    b, j = h
    return mul(a, power(b, 3**i)), (i + j) % 4


def gpower(g, n):
    r = (1, 0)
    while n:
        if n & 1:
            r = compose(r, g)
        g = compose(g, g)
        n //= 2
    return r


def order(g):
    r = (1, 0)
    for k in range(1, 321):
        r = compose(r, g)
        if r == (1, 0):
            return k
    raise AssertionError("order bound exceeded")


z = 3
assert power(z, 5) == 1 and z != 1
assert all(power(a, 80) == 1 for a in range(1, 81))
c = add(z, neg(power(z, 4)))
assert power(c, 9) == neg(c)
assert power(c, 8) == 2
basis = [1, 3, 9, 27]


def pairing(x, y):
    return trace(mul(c, mul(x, power(y, 9))))


J = [[pairing(x, y) for y in basis] for x in basis]
assert all(J[i][i] == 0 for i in range(4))
assert all((J[i][j] + J[j][i]) % 3 == 0
           for i in range(4) for j in range(4))
assert all(any(pairing(x, y) for y in basis) for x in range(1, 81))


def action(g, x):
    return mul(g[0], power(x, 3**g[1]))


def multiplier(g):
    for m in (1, 2):
        if all(pairing(action(g, x), action(g, y)) == m * pairing(x, y) % 3
               for x in basis for y in basis):
            return m
    return None


normalizer = {(a, i) for a in range(1, 81) for i in range(4)
              if multiplier((a, i)) is not None}
assert len(normalizer) == 80
tau = (mul(power(c, 4), z), 0)
F = (power(c, 5), 1)
assert order(tau) == 20 and order(F) == 8
assert multiplier(tau) == 2 and multiplier(F) == 1
assert gpower(F, 4) == (2, 0) == gpower(tau, 10)
assert compose(F, tau) == compose(gpower(tau, 3), F)
generated = {compose(gpower(tau, a), gpower(F, i))
             for a in range(20) for i in range(4)}
assert generated == normalizer
assert all(gpower(g, 4) == (2, 0) for g in normalizer if g[1] == 1)
I3 = {g for g in normalizer if g[1] == 0}
assert len(I3) == 20
assert {power(a, 4) for a in range(1, 81)} == {g[0] for g in I3}
assert {power(a, 28) for a in range(1, 81)} == {g[0] for g in I3}
wild5 = {(power(z, a), 0) for a in range(5)}
I5 = {g for g in normalizer if multiplier(g) == 1}
assert len(I5) == 40
assert {compose((power(z, a), 0), gpower(F, i))
        for a in range(5) for i in range(8)} == I5
assert compose(F, (z, 0)) == compose((power(z, 3), 0), F)

result = {
    "field": "F3[z]/(z^4+z^3+z^2+z+1)",
    "encoding": "sum_i coefficient_i*3^i",
    "z": z,
    "c": c,
    "pairing_matrix": J,
    "tau": tau,
    "F": F,
    "group_order": len(normalizer),
    "element_order_counts": dict(sorted(Counter(map(order, normalizer)).items())),
    "I3_order": len(I3),
    "I5_order": len(I5),
    "wild5_order": len(wild5),
    "all_assertions_passed": True,
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
print("result_sha256", hashlib.sha256(out.read_bytes()).hexdigest())
