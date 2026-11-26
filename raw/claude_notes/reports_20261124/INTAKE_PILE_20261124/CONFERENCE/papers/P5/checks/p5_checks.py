"""Checks of the steps that paper P5 adds to the run's proofs.

Written by a0805369bae2ebddc (Claude Opus 5.5 at effort high), 25 Nov 2026.
Each check is labelled with the place in P5_paper.tex that it tests.
Run: python -I -B p5_checks.py
"""
from fractions import Fraction as Fr
from math import comb, gcd, log2
import itertools
import mpmath as mp

mp.mp.dps = 60
out = []


def say(s):
    print(s)
    out.append(s)


# (a) Prop. torus-modular (P-F14): weights of Sym^n(C^2) under diag(t^{N+1}, t)
ok = True
for N in range(2, 13):
    for n in range(0, 200):
        mult = sum(1 for a in range(n + 1) if (N + 1) * a + (n - a) == 2 * n)
        ok &= mult == (1 if n % N == 0 else 0)
say(f"(a) torus modular index: f_N(n) = 1_[N|n] for N<=12, n<200: {ok}")


# (b) Prop. torus-indices (P-F15): g_N, its constituents, p(g_N), s(g_N)
def g_count(N, n):
    # weights a + 3b + (N+1)c with a+b+c = n, equal to 2n
    return sum(1 for b in range(n + 1) for c in range(n + 1 - b) if (n - b - c) + 3 * b + (N + 1) * c == 2 * n)


def constituents(f, period, deg, start):
    """Fit, for each residue r mod period, the polynomial of degree <= deg through
    the values f(n), n = r mod period, n >= start; return exact coefficients."""
    cons = {}
    for r in range(period):
        ns = [n for n in range(start, start + period * (deg + 4)) if n % period == r][: deg + 3]
        # Lagrange through first deg+1 points, check on the rest
        pts = ns[: deg + 1]
        import sympy as sp
        x = sp.symbols('x')
        poly = sp.expand(sp.interpolate([(n, f(n)) for n in pts], x)) if len(pts) > 1 else sp.Integer(f(pts[0]))
        for n in ns:
            assert poly.subs(x, n) == f(n), (r, n)
        cons[r] = sp.Poly(poly, x)
    return cons


import sympy as sp
x = sp.symbols('x')
ok_b = True
for N in range(3, 16, 2):
    L = 2 * N
    # generating function check
    ser = sp.series(1 / ((1 - x**2) * (1 - x**N)), x, 0, 6 * N).removeO()
    for n in range(6 * N):
        ok_b &= ser.coeff(x, n) == g_count(N, n)
    cons = constituents(lambda n: g_count(N, n), L, 1, 0)

    def shifted_constituent(r, p):
        # constituent of n -> f(n+p) on class n = i mod L with i+p = r mod L
        return sp.Poly(cons[r].as_expr().subs(x, x + p), x)

    def positive_after(p):
        return all(all(c >= 0 for c in shifted_constituent(r, p).all_coeffs()) for r in range(L))

    def saturated_after(s):
        for r in range(L):
            q = shifted_constituent(r, s)
            if q.is_zero:
                continue
            # linear polynomial: positive for all integers n >= 1 iff value at 1 > 0 and slope >= 0
            if not (q.eval(1) > 0 and q.all_coeffs()[0] >= 0):
                return False
        return True

    p = next(p for p in range(0, 10 * N) if positive_after(p))
    s = next(s for s in range(0, 10 * N) if saturated_after(s))
    ok_b &= (p == N - 2 and s == N - 2)
say(f"(b) torus indices: GF 1/((1-T^2)(1-T^N)) and p = s = N-2 for odd N in 3..15: {ok_b}")

# (c) plethysm: grading stabilizer of the chain point is exactly mu_M.
# Exact stabilizer of F_n: diag(a^{(-2)^{i-1}}), a^{3M} = 1; det = a^S;
# grading character det^{3/g}; its image has order M.
ok_c = True
for n in range(4, 41):
    M = 2 ** (n - 1)
    g = gcd(n, 3)
    S = sum((-2) ** i for i in range(n))
    assert S == (1 - (-2) ** n) // 3 and S % 2 == 1 and (S - n) % 3 == 0
    expo = (S * (3 // g)) % (3 * M)
    order = (3 * M) // gcd(3 * M, expo)
    ok_c &= order == M
    # chain monomials fixed by the generator: weights w_i = (-2)^{i-1} mod 3M
    w = [pow(-2, i, 3 * M) for i in range(n)]
    for i in range(n - 1):
        ok_c &= (2 * w[i] + w[i + 1]) % (3 * M) == 0
    ok_c &= (3 * w[n - 1]) % (3 * M) == 0
say(f"(c) plethysm grading stabilizer = mu_M for 4<=n<=40: {ok_c}")

# (d) Kempf-Ness for the chain cubic: positive r_i with sum r_i a_i = 1,
# and no two supported weights differ by a root e_a - e_b.
ok_d = True
for n in range(2, 31):
    cols = []
    for i in range(n - 1):
        v = [0] * n; v[i] = 2; v[i + 1] = 1; cols.append(tuple(v))
    v = [0] * n; v[n - 1] = 3; cols.append(tuple(v))
    r = [Fr(1 - Fr(-1, 2) ** (i + 1), 3) for i in range(n - 1)]
    r.append((1 - r[n - 2]) / 3)
    ok_d &= all(ri > 0 for ri in r)
    tot = [sum(r[k] * cols[k][j] for k in range(n)) for j in range(n)]
    ok_d &= all(t == 1 for t in tot)
    for A, B in itertools.permutations(cols, 2):
        d = [a - b for a, b in zip(A, B)]
        if sorted(d) == [-1] + [0] * (n - 2) + [1]:
            ok_d = False
say(f"(d) Kempf-Ness data for the chain cubic, 2<=n<=30: {ok_d}")


# (e) amplitude bound via the positive multiset S_n (my route to (P-F56m)).
def S_multiset(n):
    M = 2 ** (n - 1)
    w = [(-2) ** i for i in range(n - 1)] + [0]
    E = {frozenset({0, 1, k}) for k in range(2, n)} | {frozenset({0, 2, 3})}
    S = [w[i] for i in range(n - 1)]
    for i, j, k in itertools.combinations(range(n), 3):
        if frozenset({i, j, k}) not in E:
            S.append(w[i] + w[j] + w[k])
    return S, M


ok_e = True
rows = []
for n in range(4, 15):
    S, M = S_multiset(n)
    assert len(S) == comb(n, 3)
    assert all(b % M != 0 for b in S)
    g = gcd(n, 3)
    rr = 3 * g
    a_star = pow(rr, -1, M)
    zeta = mp.exp(2j * mp.pi / M)
    # Z_n = C_n(zeta^{a*}) / M with C_n(zeta) = prod (1 - zeta^{g b})^{-1}
    C = mp.mpf(1)
    for b in S:
        C /= (1 - zeta ** (a_star * g * b))
    lZ = float(mp.log(abs(C) / M, 2))
    bound = comb(n, 4) - 3 * comb(n - 1, 3) - (n - 1) * (n - 2) - comb(n, 3) - (n - 1)
    runs = comb(n, 4) - 2 * comb(n - 1, 3) - comb(n + 2, 3) + 1 - (n - 3) * n * (n - 1)
    ok_e &= lZ >= bound and bound >= n ** 4 / 24 - 2 * n ** 3
    rows.append((n, round(lZ, 2), bound, runs, round(n ** 4 / 24 - 2 * n ** 3, 1)))
say(f"(e) log2|Z_n| >= my bound >= n^4/24 - 2n^3 for 4<=n<=14: {ok_e}")
for r in rows:
    say(f"    n={r[0]}: log2|Z_n|={r[1]}, my bound={r[2]}, run's (P-F56m) first line={r[3]}, n^4/24-2n^3={r[4]}")

# check the bound inequality for larger n symbolically/numerically
ok_e2 = all(comb(n, 4) - 3 * comb(n - 1, 3) - (n - 1) * (n - 2) - comb(n, 3) - (n - 1) >= n ** 4 / 24 - 2 * n ** 3
            for n in range(4, 5000))
say(f"(e2) my amplitude bound >= n^4/24 - 2n^3 for 4<=n<5000: {ok_e2}")

# (f) Fourier normalization: a simple pole C/(1-t^M) at zeta contributes (C/M) zeta^{-s}.
M = 8; zeta = mp.exp(2j * mp.pi / M)
ser = [sum(zeta ** (-a * s) for a in range(M)) / M for s in range(20)]
ok_f = all(abs(ser[s] - (1 if s % M == 0 else 0)) < 1e-40 for s in range(20))
say(f"(f) partial fractions 1/(1-t^M) = (1/M) sum_rho 1/(1-t/rho): {ok_f}")

with open('p5_checks_output.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out) + '\n')
