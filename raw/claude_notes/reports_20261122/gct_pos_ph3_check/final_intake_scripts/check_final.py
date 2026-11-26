"""Own checks, written from the printed statements of GCT_POS's final.  No file of the return is imported or run."""
from fractions import Fraction as Fr
from itertools import product, combinations
from math import lcm, gcd
from collections import Counter
import cmath, math

print('== K-018/K-019/K-020/K-021: the gadget, glued from the printed data')
E = '262 540 056 336 755 517 622 420 303 114 275 472 746 524 065 033 607 121 347 663 611 770'.split()
E = [tuple(int(c) for c in e) for e in E]
p = [120, 112, 131, 126, 125, 96, 148, 12, -15, 208, 136, -12, -1, 48, -5, 130, 15, 48, 145, 141, -48, 132]
u = [72, 16, -43, -14, 43, -96, -244, 84, 87, -80, -72, 172, 57, 80, 29, 14, 169, 80, -73, -101, 176, -100]
bd = (4, 0, 1)


def glue(n, edges, sel):
    r = edges.pop(sel)
    maps = []
    for j in range(3):
        mp, t = {bd[j]: sel[j]}, n
        for c in range(8):
            if c != bd[j]:
                mp[c] = t
                t += 1
        maps.append(mp)
    for i, e in enumerate(E):
        m = (p[i] + u[i] * r) / Fr(256)
        assert m > 0
        edges[tuple(maps[j][e[j]] for j in range(3))] = m
    return n + 7, edges, tuple(maps[j][(7, 5, 5)[j]] for j in range(3))


def inverse_and_det(M):
    N = len(M)
    A = [[Fr(x) for x in r] + [Fr(int(i == j)) for j in range(N)] for i, r in enumerate(M)]
    det = Fr(1)
    for c in range(N):
        k = next(i for i in range(c, N) if A[i][c] != 0)
        if k != c:
            A[c], A[k] = A[k], A[c]
            det = -det
        pv = A[c][c]
        det *= pv
        A[c] = [x / pv if x else x for x in A[c]]
        for i in range(N):
            f = A[i][c]
            if i != c and f:
                A[i] = [a - f * b if b else a for a, b in zip(A[i], A[c])]
    return [r[N:] for r in A], abs(det)


def lie_rank(n, edges, q=1000003):
    piv = {}
    for f in range(3):
        for a in range(n):
            for b in range(n):
                v = {}
                for idx, (e, m) in enumerate(sorted(edges.items())):
                    if e[f] != b:
                        continue
                    t = list(e)
                    t[f] = a
                    k = tuple(t)
                    # generic nonzero coefficients: rank mod q with these gives a lower bound on the generic rank
                    v[k] = (v.get(k, 0) + pow(7, idx + 1, q)) % q
                v = {k: x for k, x in v.items() if x}
                while v:
                    k = min(v)
                    if k not in piv:
                        iv = pow(v[k], -1, q)
                        piv[k] = {x: y * iv % q for x, y in v.items()}
                        break
                    c = v[k]
                    for x, y in piv[k].items():
                        z = (v.get(x, 0) - c * y) % q
                        if z:
                            v[x] = z
                        else:
                            v.pop(x, None)
    return len(piv)


h = Fr(1, 2)
n, ed = 2, {(0, 0, 1): h, (0, 1, 0): h, (1, 0, 0): h, (1, 1, 1): h}
sel = (1, 1, 1)
for k in range(1, 5):
    n, ed, sel = glue(n, ed, sel)
    marg = Counter()
    pairs = Counter()
    for e, m in ed.items():
        for j in range(3):
            marg[j, e[j]] += m
        for a, b in combinations(range(3), 2):
            pairs[a, b, e[a], e[b]] += 1
    assert all(marg[j, i] == 1 for j in range(3) for i in range(n)) and max(pairs.values()) == 1 and len(ed) == 3 * n - 2
    M = [[0] * (3 * n) for _ in ed]
    for r, e in zip(M, ed):
        for j in range(3):
            r[j * n + e[j]] = 1
    for c in (0, n):
        M.append([int(i == c) for i in range(3 * n)])
    inv, det = inverse_and_det(M)
    D = 2 * 256 ** k
    cols = list(zip(*inv))
    gen = next(c for c in cols if lcm(*[x.denominator for x in c]) == D)
    w = [int(x * D) % D for x in gen]
    chi = Fr(sum(w) % D, D).denominator
    line = 'k=%d n=%d |det|=%s D=%d order(chi)=%d' % (k, n, det, D, chi)
    for l in range(0, k + 1):
        Dl = D // 256 ** l if l < k else None
        mods = [('l=%d' % l, Dl)] if Dl else []
        if l == 0:
            mods.append(('M=2^(n-1)', 2 ** (n - 1)))
        for lab, md in mods:
            W = [[x % md for x in w[j * n:(j + 1) * n]] for j in range(3)]
            C = [Counter(X) for X in W]
            VV = sum(ca * cb * C[2].get((-a - b) % md, 0) for a, ca in C[0].items() for b, cb in C[1].items())
            lie = sum(sum(c * c for c in X.values()) - 1 for X in C)
            line += ' | %s: fixed coords %d, fixed dim %d' % (lab, VV, VV - lie)
            if lab.startswith('l='):
                line += ' (K-021a %d)' % (343 * l ** 3 + 14 * l + 1)
    if k <= 3:
        line += ' | Lie rank mod q %d of %d' % (lie_rank(n, ed), 3 * n * n - 2)
    print(line, flush=True)

print('== K-025 and K-037a: criticality and the order-three element')
s = math.sqrt
def reduced(T, j):
    R = [[0.0] * 3 for _ in range(3)]
    for a, x in T.items():
        for b, y in T.items():
            if all(a[i] == b[i] for i in range(3) if i != j):
                R[a[j]][b[j]] += x * y
    return [[round(v, 10) + 0.0 for v in r] for r in R]
T25 = {(0, 0, 0): s(2 / 3), (0, 1, 2): -1 / s(6), (1, 1, 2): 1 / s(2), (0, 2, 1): -1 / s(6), (1, 2, 1): -1 / s(2),
       (2, 0, 2): 1 / s(3), (2, 1, 1): 1 / s(3), (2, 2, 0): 1 / s(3)}
for rho, T in [('K-025', T25)] + [(r, dict(T25, **{})) for r in (0.5, 0.9)]:
    T = dict(T)
    if rho != 'K-025':
        T[0, 0, 0] = s(rho - 1 / 3)
        T[0, 1, 2] = T[0, 2, 1] = 1 / s(6)
    ok = all(([0, 0, 1][a] + [0, 1, 2][b] + [0, 1, 2][c]) % 3 == 0 for a, b, c in T)
    print(rho, [reduced(T, j) for j in range(3)], 'fixed:', ok, 'det exponent mod 3:', (1 + 3 + 3) % 3)

print('== K-022: Gr(2,5) with the printed weights')
for m in (2, 4, 8, 16):
    a = (1, m, 2 * m - 1, 2 * m + 1, 4 * m - 1)
    S, MM = sum(a), 4 * m
    num = Counter({0: 1})
    for x in a:
        num[S - x] -= 1
        num[S + x] += 1
    num[2 * S] -= 1
    deg = [a[i] + a[j] for i, j in combinations(range(5), 2)]
    nd = sum(1 for d in deg if d % MM == 0)
    z = cmath.exp(2j * math.pi / MM)
    derivs = [max(abs(sum(c * math.prod(d - q for q in range(o)) * r ** d for d, c in num.items()))
                  for r in [z ** b for b in range(1, MM, 2)]) for o in range(nd + 1)]
    line = 'M=%d den factors vanishing %d; max |N|,|N\'|,|N\'\'| at the roots %s' % (MM, nd, ['%.1e' % x for x in derivs])
    if m == 2:
        N = 48
        ser = [num.get(i, 0) for i in range(N)]
        for d in deg:
            for i in range(d, N):
                ser[i] += ser[i - d]
        pl = list(combinations(range(5), 2))
        cnt = [0] * N
        def rec(start, d, last):
            cnt[d] += 1
            for i in range(start, 10):
                P = pl[i]
                if last and not (P[0] >= last[0] and P[1] >= last[1]):
                    continue
                if d + deg[i] < N:
                    rec(i, d + deg[i], P)
        rec(0, 0, None)
        line += ' | series = standard monomial count to degree 47: %s' % (ser == cnt)
    print(line)

print('== R-DIAG-001: Laurent coefficients at u=0')
def mul(A, B):
    return [sum(A[i] * B[k - i] for i in range(k + 1)) for k in range(len(A))]
def binom_series(e, N):
    o, c = [], Fr(1)
    for i in range(N):
        o.append(c)
        c = c * (e - i) * -1 / (i + 1)
    return o
N = 7
nu = [(i == 0) - c for i, c in enumerate(binom_series(Fr(9, 2), N))][1:]
de = [(i == 0) - c for i, c in enumerate(binom_series(Fr(3), N))][1:]
de3 = mul(mul(de, de), de)
q = []
for i in range(3):
    q.append((nu[i] - sum(q[j] * de3[i - j] for j in range(i))) / de3[0])
print('u^-2, u^-1:', q[:2])

print('== K-033c against K-033d')
num = [1, 91067, 429033, 416212, 78249]
ser = num + [0] * 35
for d in (1, 1, 1, 1):
    for i in range(1, 40):
        ser[i] += ser[i - 1]
for i in range(1, 40):
    ser[i] -= ser[i - 1]
f = [Fr(507281, 6) * a ** 3 + 6410 * a * a + Fr(338, 3) * a + Fr(3, 4) + Fr((-1) ** a, 4) for a in range(40)]
print('equal to a=39:', ser == f, '| density', Fr(sum(num), 2), 'mod 3', Fr(sum(num), 2) % 3)

print('== K-027/K-031 congruence against the n=4 residue: total minus chain, divided by three')
print('(14-10r)/256 - (2+2r)/256 =', (14 - 2, -10 - 2), '/256; both coefficients divisible by 3:', 12 % 3 == 0)

print('== PNEW-015c / PNEW-016 arithmetic')
print(Fr(1, 12) - Fr(1, 32) == Fr(5, 96), Fr(1, 12) - Fr(1, 16) * Fr(1, 5) == Fr(17, 240))
L2 = math.log2(79004)
print('2+log2 n <= n/96:', 2 + L2 <= 79004 / 96, '| n^4/96 > 5n^3+2:', Fr(79004 ** 4, 96) > 5 * 79004 ** 3 + 2,
      '| I7 at 2000 exactly:', Fr(7 * 2000 - 3, 12) ** 3 + 3 * 2000 ** 2 <= Fr(2000 ** 3, 5))
