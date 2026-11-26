"""Independent computations for the last read of paper 5 (P5_paper.tex of 25 Nov 2026).

Conference convener ae84c4aa (Claude Fable 5.2 at effort max), 25 Nov 2026. Written from the statements of the
paper, without looking at the writer's scripts. Each block prints what it tested and the result.

usage: python -I -B last_read_checks.py
"""
import cmath
import itertools
import math
import sys
from fractions import Fraction

sys.stdout.reconfigure(encoding="utf-8")
OK = True


def report(name, cond, detail=""):
    global OK
    OK = OK and bool(cond)
    print("[%s] %s%s" % ("ok" if cond else "FAIL", name, (": " + detail) if detail else ""))


# ---------------------------------------------------------------- weights of Section 7
def weights(n):
    return [(-2) ** i for i in range(n - 1)] + [0]


def S(n):
    w = weights(n)
    E = {frozenset((0, 1, k)) for k in range(2, n)} | {frozenset((0, 2, 3))}
    out = [w[i] for i in range(n - 1)]
    out += [w[i] + w[j] + w[k] for i, j, k in itertools.combinations(range(n), 3) if frozenset((i, j, k)) not in E]
    return out


def T(n):
    w = weights(n)
    out = [1]
    out += [1 + w[j] + w[k] for j, k in itertools.combinations(range(2, n), 2) if (j, k) != (2, 3)]
    out += [2 + w[k] for k in range(3, n)]
    out += [6]
    return out


def log2prod(ws, a, M):
    """log2 of prod |1 - exp(2 pi i a b / M)|^(-1)"""
    s = 0.0
    for b in ws:
        r = (a * b) % M
        assert r != 0
        s -= math.log2(2 * abs(math.sin(math.pi * r / M)))
    return s


print("== Section 7: the multiset S_n, the product formula and the dominant pair")
for n in range(4, 14):
    assert len(S(n)) == math.comb(n, 3) and all(b % 2 ** (n - 1) for b in S(n))
report("|S_n| = binom(n,3) and no element divisible by M, n = 4..13", True)

# the character identity behind Prop 7.2: Sym^3 V - V (x) V^* = sum over S_n, as characters of Z/M
for n in range(4, 11):
    M = 2 ** (n - 1)
    w = weights(n)
    sym3 = {}
    for i, j, k in itertools.combinations_with_replacement(range(n), 3):
        r = (w[i] + w[j] + w[k]) % M
        sym3[r] = sym3.get(r, 0) + 1
    for i in range(n):
        for j in range(n):
            r = (w[i] - w[j]) % M
            sym3[r] = sym3.get(r, 0) - 1
    target = {}
    for b in S(n):
        target[b % M] = target.get(b % M, 0) + 1
    sym3 = {k: v for k, v in sym3.items() if v}
    if sym3 != target:
        report("character identity N^* = sum over S_n, n = %d" % n, False)
        break
else:
    report("character of Sym^3 V - V(x)V^* on <D> equals the multiset S_n mod M, n = 4..10", True)

# n = 4: Salmon's invariants of cubic surfaces, degrees 8,16,24,32,40,100; in the grading s = D/4
z8 = cmath.exp(2j * cmath.pi / 8)
salmon = (1 + z8 ** 25) / ((1 - z8 ** 2) * (1 - z8 ** 4) * (1 - z8 ** 6) * (1 - z8 ** 10))
prod4 = 1 / math.prod((1 - z8 ** b) for b in S(4))
report("C_4(zeta): product formula against the residue of (1+t^25)/((1-t^2)(1-t^4)(1-t^6)(1-t^8)(1-t^10))",
       abs(salmon - prod4) < 1e-12, "%.5f%+.5fi" % (prod4.real, prod4.imag))

print("   n  log2|Z_n|   first line of (24)   n^4/24-2n^3    Q_n = E_n/|Z_n|   log2 delta_n   bound on log2 delta_n")
for n in range(4, 15):
    M = 2 ** (n - 1)
    bn = pow(3, -1, M)
    Sn = S(n)
    logs = {a: log2prod(Sn, a, M) for a in range(1, M, 2)}
    top = max(logs.values())
    argtop = sorted(a for a in logs if abs(logs[a] - top) < 1e-9)
    logZ = logs[bn] - (n - 1)
    first = math.comb(n, 4) - 3 * math.comb(n - 1, 3) - (n - 1) * (n - 2) - math.comb(n, 3) - (n - 1)
    second = n ** 4 / 24 - 2 * n ** 3
    Q = sum(2.0 ** (logs[a] - logs[bn]) for a in logs if a not in (bn, M - bn))
    ld = logs[(bn + M // 2) % M] - logs[bn]
    lb = -n ** 3 / 6 + 4 * n ** 2 - 107 * n / 6 + 19
    print("  %2d  %9.2f  %12d  %16.1f  %14.3e  %12.2f  %12.2f   max at a = %s (b_n = %d)"
          % (n, logZ, first, second, Q, ld, lb, argtop, bn))
    report("  (24) at n = %d" % n, logZ >= first >= second)
    if n >= 5:
        report("  delta_n <= 2^(bound) at n = %d" % n, ld <= lb + 1e-9)

for n in range(5, 12):
    M = 2 ** (n - 1)
    Tn = T(n)
    assert len(Tn) == math.comb(n - 1, 2)
    good = True
    for a in range(1, M, 2):
        lhs = log2prod(S(n), a, M)
        rhs = log2prod(Tn, a, M) + log2prod(S(n - 1), (-a) % (M // 2), M // 2)
        good = good and abs(lhs - rhs) < 1e-6
    if not good:
        report("recursion P_n(a) = J_n(a) P_(n-1)(-a) at n = %d" % n, False)
        break
else:
    report("recursion P_n(a) = J_n(a) P_(n-1)(-a mod M_(n-1)) for every odd a, n = 5..11", True)

for n in range(4, 200):
    first = math.comb(n, 4) - 3 * math.comb(n - 1, 3) - (n - 1) * (n - 2) - math.comb(n, 3) - (n - 1)
    assert first >= Fraction(n ** 4, 24) - 2 * n ** 3
    if n >= 48:
        assert Fraction(-n ** 3, 6) + 4 * n ** 2 - Fraction(107 * n, 6) + 19 <= Fraction(-n ** 3, 12)
report("first line of (24) >= n^4/24 - 2n^3 (4 <= n < 200); delta exponent <= -n^3/12 (48 <= n < 200)", True)

# constants of Theorem 7.9
dl = Fraction(1, 10 ** 5)
N = 10 ** 20
report("thresholds of Thm 7.9: 48/delta^3, 16/delta, 2688/delta^3 <= N = 10^20",
       48 / dl ** 3 <= N and 16 / dl <= N and 2688 / dl ** 3 <= N,
       "48/d^3 = %.2e, 2688/d^3 = %.2e" % (48 / dl ** 3, 2688 / dl ** 3))
report("log2(3)/12 > 1/8 and 2502/10^5 < 1/12", math.log2(3) / 12 > 1 / 8 and Fraction(2502, 10 ** 5) < Fraction(1, 12))
for n in (1024, 2000, 10 ** 4, 10 ** 6):
    assert Fraction(3 * n ** 4, 80) + Fraction(2 * n ** 3, 5) < Fraction(n ** 4, 24) - 2 * n ** 3 - 1
    assert math.comb(n + 2, 3) <= n ** 3 / 5
report("3n^4/80 + 2n^3/5 < n^4/24 - 2n^3 - 1 and m <= n^3/5 at n = 1024, 2000, 10^4, 10^6", True)
for n in range(3, 400):
    assert n - 1 + (n - 3) * math.comb(n, 3) + 2 * n ** 3 <= n ** 4
report("n - 1 + (n-3) binom(n,3) + 2n^3 <= n^4 for 3 <= n < 400", True)

print("== Section 7.1 and Prop 7.1 at n = 4: Fourier normalization and the wave identity, exactly")
# f_4(s) from the Salmon series; constituents for the period L = 120 by exact interpolation
LEN = 120 * 8
den = [1]
for a in (2, 4, 6, 8, 10):
    new = [0] * (len(den) + a)
    for i, c in enumerate(den):
        new[i] += c
        new[i + a] -= c
    den = new
num = [0] * 26
num[0] = num[25] = 1
f4 = [0] * LEN
for s in range(LEN):
    v = num[s] if s < len(num) else 0
    for i in range(1, min(s, len(den) - 1) + 1):
        v -= den[i] * f4[s - i]
    f4[s] = v
L = 120


def constituent(r):
    xs = [r + L * k for k in range(5)]
    ys = [Fraction(f4[x]) for x in xs]

    def q(X):
        tot = Fraction(0)
        for i in range(5):
            t = ys[i]
            for j in range(5):
                if j != i:
                    t *= Fraction(X - xs[j], xs[i] - xs[j])
            tot += t
        return tot
    return q


assert all(constituent(r)(r + L * 6) == f4[r + L * 6] for r in range(L))
z8 = cmath.exp(2j * cmath.pi / 8)
A = {a: (1 / math.prod((1 - z8 ** (a * b)) for b in S(4))) / 8 for a in (1, 3, 5, 7)}
bad = 0
for r in range(L):
    W = sum(A[a] * z8 ** (-a * r) for a in A)
    for X in (r, r + 7, 1000 + r):
        d = constituent(r)(X) - constituent((r + L // 2) % L)(X)
        if abs(complex(d) - 2 * W) > 1e-9:
            bad += 1
report("q_r(X) - q_(r+60)(X) = 2 W_4(r) for all 120 residues, with A = C/M from the product formula", bad == 0)

print("== Fixed weights (Thm 5.3 and Prop 6.1(4)) and the grading stabilizer (Prop 6.1(3))")
for n in range(2, 16):
    M = 2 ** (n - 1)
    w = [((-2) ** i) % M for i in range(n)]            # w_1..w_n of Thm 5.3 are (-2)^(i-1)
    lin = sum(1 for i in range(n) if w[i] % M == 0)
    hook = sum(1 for i in range(n) for j in range(n) if i != j and (2 * w[i] + w[j]) % M == 0)
    hook += 2 * sum(1 for c in itertools.combinations(range(n), 3) if sum(w[i] for i in c) % M == 0)
    cub = sum(1 for c in itertools.combinations_with_replacement(range(n), 3) if sum(w[i] for i in c) % M == 0)
    assert lin + hook == n and (n < 2 or cub == n) and len(set(w)) == n, (n, lin, hook, cub)
report("dim of the g-fixed part of W + S_(2,1)W is n; fixed cubic monomials are n; simple spectrum; n = 2..15", True)
for n in range(2, 60):
    M = 2 ** (n - 1)
    nu = math.gcd(n, 3)
    gamma = 3 // nu
    Ssum = sum((-2) ** i for i in range(n))
    assert Ssum == (1 - (-2) ** n) // 3 and Ssum % 2 == 1 and (Ssum - n) % 3 == 0
    assert math.gcd(Ssum, 3 * M) == nu
    assert 3 * M // math.gcd(3 * M, gamma * Ssum) == M
report("S odd, S = n mod 3, |ker det| = nu, grading stabilizer of order M; n = 2..59", True)

print("== Kempf-Ness data (Thm 5.3 and Prop 6.1(1))")
for n in range(2, 40):
    for last in (1, 3):                                  # a_n = e_n (Kronecker) or 3 e_n (cubic)
        r = [Fraction(1) / 3 * (1 - Fraction(-1, 2) ** i) for i in range(1, n)]
        r.append((1 - r[-1]) / last)
        a = [[0] * n for _ in range(n)]
        for i in range(n - 1):
            a[i][i], a[i][i + 1] = 2, 1
        a[n - 1][n - 1] = last
        tot = [sum(r[i] * a[i][c] for i in range(n)) for c in range(n)]
        assert all(x > 0 for x in r) and all(t == 1 for t in tot)
        rows = a if last == 3 else a[:n - 1]              # in the Kronecker case e_n lies in the other summand
        for i, j in itertools.permutations(range(len(rows)), 2):
            d = [rows[i][c] - rows[j][c] for c in range(n)]
            assert not (sorted(d) == [-1] + [0] * (n - 2) + [1])
report("positive coefficients, sum r_i a_i = (1,...,1), no two support weights differ by a root; n = 2..39", True)

print("== Torus examples (Props 8.1 and 8.2), from the definitions")


def indices(vals, period, deg):
    """positivity and saturation index of a quasi-polynomial given by its values, by the definitions of Section 2"""
    def coeffs(r):                                       # exact interpolation of the constituent of residue r
        xs = [r + period * k for k in range(deg + 1)]
        ys = [Fraction(vals[x]) for x in xs]
        # degree <= 1 is all we need here
        assert deg == 1
        slope = (ys[1] - ys[0]) / (xs[1] - xs[0])
        return ys[0] - slope * xs[0], slope
    cs = [coeffs(r) for r in range(period)]
    p = 0
    while True:                                          # constituents of n -> f(n+p): X -> q_r(X+p)
        if all(c0 + c1 * p >= 0 and c1 >= 0 for c0, c1 in cs):
            break
        p += 1
    s = 0
    while True:
        okk = True
        for c0, c1 in cs:
            if (c0, c1) == (0, 0):
                continue
            # positive at every integer X >= 1 (the function X -> c0 + c1 (X+s) is monotone)
            if c1 < 0 or c0 + c1 * (1 + s) <= 0:
                okk = False
        if okk:
            break
        s += 1
    return p, s


good = True
for N in range(2, 13):
    for n in range(0, 150):
        cnt = sum(1 for a in range(n + 1) if (N + 1) * a + (n - a) == 2 * n)
        good = good and cnt == (1 if n % N == 0 else 0)
report("f_N(n) = 1 if N | n, else 0; N = 2..12, n < 150", good)
good = True
for N in range(3, 20, 2):
    vals = []
    for n in range(0, 2 * N * 4):
        vals.append(sum(1 for b in range(n + 1) for c in range(n + 1 - b) if (n - b - c) + 3 * b + (N + 1) * c == 2 * n))
    ser = [0] * len(vals)                                 # 1/((1-T^2)(1-T^N))
    for i in range(0, len(vals), 2):
        for j in range(0, len(vals) - i, N):
            ser[i + j] += 1
    good = good and ser == vals and indices(vals, 2 * N, 1) == (N - 2, N - 2)
report("g_N: series 1/((1-T^2)(1-T^N)) and p = s = N - 2; odd N = 3..19", good)

print("ALL AS CLAIMED" if OK else "SOME CHECK FAILED")
