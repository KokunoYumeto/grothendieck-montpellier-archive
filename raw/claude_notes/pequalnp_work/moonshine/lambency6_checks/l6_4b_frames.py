"""Follow-up to l6_4: Frame shapes of automorphisms of N(A5^4 D4) that fix every component and preserve the glue
(then the A5 parts all carry the same diagram sign eps and the D4 part lies in W(D4), by l6_1: only +-I in GL2(F3)
fix all four lines, and they act trivially on the D4 triality). Which of 2^3 6^3, 6^4, 3^8, 2^12, 1^2 2^2 3^2 6^2 occur?
Run: python -I -B l6_4b_frames.py"""
import itertools
from collections import Counter
from sympy import symbols, Poly, prod, cyclotomic_poly, div, cancel, expand
x = symbols("x")
out = []
def say(*a):
    s = " ".join(str(v) for v in a); print(s); out.append(s)
def frame(cp):
    rem = Poly(cp, x); mult = {}
    for n in range(1, 61):
        c = Poly(cyclotomic_poly(n, x), x); k = 0
        while True:
            q, r = div(rem, c)
            if r.is_zero: rem = q; k += 1
            else: break
        if k: mult[n] = k
    res = {}
    for n in range(60, 0, -1):
        m = mult.get(n, 0) - sum(v for d, v in res.items() if d % n == 0)
        if m: res[n] = m
    return tuple(sorted(res.items()))
parts6 = [(6,), (5, 1), (4, 2), (4, 1, 1), (3, 3), (3, 2, 1), (3, 1, 1, 1), (2, 2, 2), (2, 2, 1, 1), (2, 1, 1, 1, 1), (1,) * 6]
def a5(ct, eps):
    cp = cancel(prod([(x ** c - 1) for c in ct]) / (x - 1))
    if eps == -1: cp = expand(cp.subs(x, -x) * (-1) ** 5)
    return frame(cp)
A5 = {eps: sorted({a5(ct, eps) for ct in parts6}) for eps in (1, -1)}
# W(D4): signed permutations of 4 coordinates with an even number of sign changes
D4 = set()
for perm in itertools.permutations(range(4)):
    for signs in itertools.product((1, -1), repeat=4):
        if signs.count(-1) % 2: continue
        M = [[0] * 4 for _ in range(4)]
        for i in range(4): M[perm[i]][i] = signs[i]
        import sympy as sp
        cp = sp.Matrix(M).charpoly(x).as_expr()
        D4.add(frame(cp))
D4 = sorted(D4)
say("A5 frames with eps=+1:", A5[1]); say("A5 frames with eps=-1:", A5[-1]); say("W(D4) frames:", D4)
def addf(*fs):
    t = Counter()
    for f in fs:
        for d, v in f: t[d] += v
    return tuple(sorted((d, v) for d, v in t.items() if v))
targets = {"2^3 6^3": ((2, 3), (6, 3)), "6^4": ((6, 4),), "3^8": ((3, 8),), "2^12": ((2, 12),), "1^2 2^2 3^2 6^2": ((1, 2), (2, 2), (3, 2), (6, 2)), "4^6": ((4, 6),)}
for name, tg in targets.items():
    hits = []
    for eps in (1, -1):
        for combo in itertools.combinations_with_replacement(A5[eps], 4):
            for d in D4:
                if addf(*combo, d) == tg: hits.append((eps, combo, d))
    say(f"{name}: realized by glue-preserving component-fixing automorphisms:", len(hits) > 0, hits[:2])
with open(__file__.replace(".py", "_output.txt"), "w", encoding="utf-8") as fh: fh.write("\n".join(out) + "\n")
