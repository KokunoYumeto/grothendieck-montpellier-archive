"""Exact test of the one new identity in the independent check (Claude Opus 5.5 at effort high, a8d75352, 22 Nov 2026).

On A x A, P = m*theta - theta1 - theta2. For a real class t in H^{2p}(A) and m = 2(g-p):
    eps(g,p) * integral (t x C t) P^m = m! * |t|^2,
C being the action of the complex structure on H^{2p}, eps a sign depending on (g,p) only. For t of type (p,p), Ct = t.
Also: |integral (Z x Z') P^m| <= binom(m, m/2) deg Z deg Z' on graphs in E x E.
"""
import random
from itertools import combinations
from math import comb, factorial

random.seed(20261122)


def wedge(a, b):
    o = {}
    for s, x in a.items():
        for t, y in b.items():
            if s & t:
                continue
            n, u = 0, t
            while u:
                low = u & -u
                n += bin(s & ~(low | (low - 1))).count("1")
                u ^= low
            o[s | t] = o.get(s | t, 0) + (-x * y if n & 1 else x * y)
    return {s: x for s, x in o.items() if x}


def setup(g):
    """theta on A = sum e_i f_i, e_i = bit 2i, f_i = bit 2i+1; second factor shifted by 2g."""
    P = {}
    for i in range(g):
        for first, second in ((2 * i, 2 * i + 1 + 2 * g), (2 * i + 2 * g, 2 * i + 1)):
            w = wedge({1 << first: 1}, {1 << second: 1})
            for s, x in w.items():
                P[s] = P.get(s, 0) + x
    return P


def rotate(t, g):
    """J e_i = f_i, J f_i = -e_i, extended multiplicatively."""
    o = {}
    for s, x in t.items():
        v = {0: x}
        for i in range(2 * g):
            if s >> i & 1:
                v = wedge(v, {1 << (i + 1): 1} if i % 2 == 0 else {1 << (i - 1): -1})
        for r, y in v.items():
            o[r] = o.get(r, 0) + y
    return o


def form(a, b, g, Pm):
    b2 = {s << (2 * g): x for s, x in b.items()}
    return wedge(wedge(a, b2), Pm).get((1 << (4 * g)) - 1, 0)


n = 0
for g in range(1, 5):
    P, powers = setup(g), [{0: 1}]
    for _ in range(2 * g):
        powers.append(wedge(powers[-1], P))
    for p in range(g + 1):
        m = 2 * (g - p)
        signs = set()
        for _ in range(4):
            t = {sum(1 << i for i in c): random.randint(-5, 5) or 1 for c in combinations(range(2 * g), 2 * p)}
            val = form(t, rotate(t, g), g, powers[m])
            norm = factorial(m) * sum(x * x for x in t.values())
            assert abs(val) == norm, (g, p, val, norm)
            signs.add(val > 0)
            n += 1
        assert len(signs) == 1
        print(f"g={g} p={p}: |Q(t,Ct)| = {m}! |t|^2, sign {'+' if signs.pop() else '-'}")

# graphs of [k] in E x E, with fundamental class (f2 - k f1)(...) = class of the kernel of y - k x
g = 2
P = setup(g)
P2 = wedge(P, P)


def graph(k):
    return wedge({1 << 2: 1, 1 << 0: -k}, {1 << 3: 1, 1 << 1: -k})


for k in range(-12, 13):
    for l in range(-12, 13):
        q = abs(form(graph(k), graph(l), g, P2))
        assert q <= comb(2, 1) * (1 + k * k) * (1 + l * l)
print(f"identity: {n} random classes PASS; intersection bound: 625 pairs of curves PASS")
