"""RESEARCH_SA20 D.025: brute-force check of the type-A outer stabilizer count in the cyclic model.
Pairs (p,q) of orderings of Z/n; inner action (p,q) -> (a p + x, a^-1 q + y); outer tau(p,q) = (rev p, -rev q).
Counts classes C_n and outer-fixed classes F_n by orbit enumeration for n = 3..6, and S_n^aff by brute force for n <= 60,
against the run's closed forms (D25.1), (D25.5). Claude Opus 5.5 at effort max, acf08879a01b97ed4, 22 Nov 2026."""
import itertools, math
def phi(n): return sum(1 for a in range(1, n + 1) if math.gcd(a, n) == 1)
def omega(m):
    s, p = set(), 2
    while m > 1:
        while m % p == 0: s.add(p); m //= p
        p += 1
    return len(s)
def closedF(n):
    if n % 2: return 0
    k = n // 2; m = n
    while m % 2 == 0: m //= 2
    F = Fraction((2**k * math.factorial(k))**2 * 2**omega(m), n * phi(n))
    return F if n % 4 == 0 else F / 2
from fractions import Fraction
def brute(n):
    units = [a for a in range(1, n) if math.gcd(a, n) == 1]
    inv = {a: pow(a, -1, n) for a in units}
    G = [(a, x, y) for a in units for x in range(n) for y in range(n)]
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    N = len(perms); seen = bytearray(N * N); classes = 0; fixed = 0; free = True
    for i, p in enumerate(perms):
        for j, q in enumerate(perms):
            if seen[i * N + j]: continue
            classes += 1; orb = set()
            for (a, x, y) in G:
                pp = tuple((a * t + x) % n for t in p); qq = tuple((inv[a] * t + y) % n for t in q)
                orb.add((idx[pp], idx[qq]))
            if len(orb) != len(G): free = False
            for (u, v) in orb: seen[u * N + v] = 1
            tp = tuple(reversed(p)); tq = tuple((-t) % n for t in reversed(q))
            if (idx[tp], idx[tq]) in orb: fixed += 1
    return classes, fixed, free
for n in range(3, 7):
    c, f, free = brute(n)
    print("n=%d: classes %d (formula (n!)^2/(n^2 phi(n)) = %s), free %s, outer-fixed %d (closed form %s)"
          % (n, c, Fraction(math.factorial(n)**2, n * n * phi(n)), free, f, closedF(n)))
def is_fpf_inv(a, x, n):
    return all(((a * ((a * t + x) % n) + x) % n) == t for t in range(n)) and all(((a * t + x) % n) != t for t in range(n))
bad = []
for n in range(4, 61, 2):
    units = [a for a in range(1, n) if math.gcd(a, n) == 1]
    S = sum(1 for a in units for x in range(n) for y in range(n)
            if is_fpf_inv(a, x, n) and is_fpf_inv((-a) % n, (-y) % n, n))
    m = n
    while m % 2 == 0: m //= 2
    closedS = n * 2**omega(m) if n % 4 == 0 else (n // 2) * 2**omega(m)
    F = Fraction(S * (2**(n // 2) * math.factorial(n // 2))**2, n * n * phi(n))
    if S != closedS or F != closedF(n): bad.append((n, S, closedS, F, closedF(n)))
print("S_n^aff closed form and (D25.5) = (D25.1) for even n = 4..60:", "all agree" if not bad else bad)
