# Checks for CONSULT_a157422a_IMPLICATIONS.md (Claude Fable 5.2 at effort max, 21 Nov 2026).
# Run: python -I -B consult_a157422a_implications_checks.py
import itertools, math, os
import numpy as np
from mpmath import (mp, mpf, mpc, zeta, gamma, pi, taylor, log, matrix, eigsy, findroot, primezeta,
                    exp, sqrt, siegeltheta, polyroots)

HERE = os.path.dirname(os.path.abspath(__file__))
mp.dps = 60

def xi(s):
    if s == 1 or s == 0:
        return mpf(1) / 2
    return s * (s - 1) / 2 * pi ** (-s / 2) * gamma(s / 2) * zeta(s)

print("== item 3: the Li Toeplitz matrix (lambda_|j-k|) is Lorentzian")
N = 10
c = taylor(lambda z: log(xi(1 / (1 - z))), 0, N)
lam = [mpf(0)] + [n * c[n] for n in range(1, N + 1)]
for size in (3, 6, 11):
    L = matrix(size, size)
    for j in range(size):
        for k in range(size):
            L[j, k] = lam[abs(j - k)]
    ev = sorted(eigsy(L, eigvals_only=True))
    print(" size %d: positive eigenvalues %d, negative %d; largest %s, largest negative %s" % (
        size, sum(1 for e in ev if e > 0), sum(1 for e in ev if e < 0), mp.nstr(ev[-1], 6),
        mp.nstr(max(e for e in ev if e < 0), 6)))
print(" sum 1/(rho(1-rho))^2 via 2(4 lam1 - lam2) =", mp.nstr(2 * (4 * lam[1] - lam[2]), 10),
      "; sum over k=3: 2(15 lam1 - 6 lam2 + lam3) =", mp.nstr(2 * (15 * lam[1] - 6 * lam[2] + lam[3]), 10))
print(" Castelnuovo-Severi sample: sqrt(lam3) <= sqrt(lam1)+sqrt(lam2):", sqrt(lam[3]) <= sqrt(lam[1]) + sqrt(lam[2]),
      "; lam2 < 4 lam1:", lam[2] < 4 * lam[1], "; lam4 < 4 lam2:", lam[4] < 4 * lam[2])

print("== item 2: thresholds in the half-plane of absolute convergence")
mp.dps = 25
s_half = findroot(lambda s: zeta(2 * s) / zeta(s) - mpf(1) / 2, 1.6)
s_hur = findroot(lambda s: zeta(s) - 2, 1.7)
s_one = findroot(lambda s: primezeta(s) - 2 ** (1 - s), 1.8)
print(" zeta(2s)/zeta(s) = 1/2 at s =", mp.nstr(s_half, 8), "(zeros of 2 zeta - 1 reach this abscissa)")
print(" zeta(s) = 2 at s =", mp.nstr(s_hur, 8), "(limit of the zero abscissa of zeta(s,1+t), t -> 0 transcendental)")
print(" primezeta(s) = 2^(1-s) at s =", mp.nstr(s_one, 8), "(circle-approximation threshold for the 1-points)")

print("== item 8: cusp values")
def wp_over(u, q, terms=40):
    # wp(z,tau)/(2 pi i)^2 with u = e^{2 pi i z}, q = e^{2 pi i tau}
    s = mpf(1) / 12 + u / (1 - u) ** 2
    for n in range(1, terms):
        qn = q ** n
        s += qn * u / (1 - qn * u) ** 2 + qn / u / (1 - qn / u) ** 2 - 2 * qn / (1 - qn) ** 2
    return s
for T in (1.5, 2.0, 3.0):
    q = exp(-2 * pi * T)
    u0 = findroot(lambda u: wp_over(u, q), -(5 - 2 * sqrt(6)))
    z0 = log(u0) / (2j * pi)
    print(" tau = %.1fi: zero of wp at u = %s, z = %s ; cusp value -(5-2 sqrt6) = %s" % (
        T, mp.nstr(u0, 12), mp.nstr(z0, 10), mp.nstr(-(5 - 2 * sqrt(6)), 12)))
def eulerian(m):
    # coefficients A(m,k), k = 0..m-1
    A = [1]
    for n in range(2, m + 1):
        A = [(k + 1) * (A[k] if k < len(A) else 0) + (n - k) * (A[k - 1] if k >= 1 else 0) for k in range(n)]
    return A
for m in (3, 4, 5, 8, 12):
    A = eulerian(m)
    r = polyroots(A[::-1], maxsteps=200, extraprec=200)
    print(" Eulerian A_%d: coefficients %s; all roots real negative: %s; roots %s" % (
        m, A if m <= 5 else "...", all(abs(x.imag) < mpf(10) ** -15 and x.real < 0 for x in r),
        [mp.nstr(x.real, 8) for x in r] if m <= 5 else "..."))
print(" 5+2 sqrt6 =", mp.nstr(5 + 2 * sqrt(6), 10), "; 2+sqrt3 =", mp.nstr(2 + sqrt(3), 10))

print("== item 7: label statistics from the label consult's run (zeros 1..5000)")
rows = [l.split("\t") for l in open(os.path.join(HERE, "ad855737_scripts", "run_1_5000.tsv"))]
g = np.array([float(r[1]) for r in rows]); lab = np.array([int(r[2]) for r in rows]); W = np.array([float(r[4]) for r in rows])
def model(v, r, K=41):
    tot = 0.5
    for j in range(1, K, 2):
        for k in range(1, K, 2):
            a = math.exp(-math.pi ** 2 * v * (j * j + k * k - 2 * j * k * r) / 2)
            b = math.exp(-math.pi ** 2 * v * (j * j + k * k + 2 * j * k * r) / 2)
            tot += 4 / math.pi ** 2 * (a - b) / (j * k)
    return tot
for lo, hi in ((0, 1000), (1000, 3000), (3000, 5000), (0, 5000)):
    w = W[lo:hi]; l = lab[lo:hi]; d = np.diff(w)
    v = w.var(); r = np.corrcoef(w[:-1], w[1:])[0, 1]
    theta = np.array([float(siegeltheta(x)) for x in g[lo:hi]])
    delta = np.diff(theta) / math.pi
    print(" zeros %d..%d: mean W %.4f, var W %.4f, var(W_{n+1}-W_n) %.4f, var(gap) %.4f, max|dW-(1-gap)| %.3f, corr %.3f; "
          "same label observed %.4f, Gaussian model %.4f" % (lo + 1, hi, w.mean(), v, d.var(), delta.var(),
          np.abs(d - (1 - delta)).max(), r, (l[1:] == l[:-1]).mean(), model(v, r)))
print(" asymptotic value 1/2 + (4/pi^2) sum_{k odd} exp(-pi^2 k^2 s2/2)/k^2 with s2 = 0.180 (GUE gap variance):",
      round(0.5 + 4 / math.pi ** 2 * sum(math.exp(-math.pi ** 2 * k * k * 0.180 / 2) / k ** 2 for k in (1, 3, 5)), 4))
for t in (1e-8, 1e-11, 1e-14):
    target = 144 * math.pi ** 2 / (2 * t) ** 1.5
    T = 1e3
    for _ in range(200):
        T = target / math.log(T / (2 * math.pi)) ** 4
    print(" collisions: at time -%.0e the expected number of collided pairs reaches 1 near height %.2e; all pairs collide above %.2e"
          % (t, T, 2 * math.pi * math.exp(2 * math.pi / math.sqrt(2 * t)) if t > 1e-3 else float("inf")))

print("== item 5: dimensions of the nonstandard Hecke algebra (cyclic module on 1 x 1)")
def hecke_left(r, v):
    perms = list(itertools.permutations(range(r)))
    idx = {p: i for i, p in enumerate(perms)}
    def length(p):
        return sum(1 for i in range(r) for j in range(i + 1, r) if p[i] > p[j])
    mats = []
    for s in range(r - 1):
        M = np.zeros((len(perms), len(perms)))
        for p in perms:
            sp = list(p); 
            # left multiplication by s: swap the values s and s+1
            sp = tuple(s + 1 if x == s else s if x == s + 1 else x for x in p)
            if length(sp) > length(p):
                M[idx[sp], idx[p]] += 1.0
            else:
                M[idx[sp], idx[p]] += 1.0
                M[idx[p], idx[p]] += v - 1.0 / v
        mats.append(M)
    return mats
def nonstandard_dim(r, v):
    T = hecke_left(r, v); n = T[0].shape[0]; I = np.eye(n)
    P = [np.kron(t + I / v, t + I / v) + np.kron(t - v * I, t - v * I) for t in T]
    x0 = np.zeros(n * n); x0[0] = 1.0
    basis = [x0 / np.linalg.norm(x0)]; frontier = [x0]
    while frontier:
        new = []
        for x in frontier:
            for p in P:
                y = p @ x
                yn = np.linalg.norm(y)
                if yn < 1e-12:
                    continue
                y = y / yn
                for _ in range(2):
                    for b in basis:
                        y = y - (b @ y) * b
                res = np.linalg.norm(y)
                if res > 1e-7:
                    basis.append(y / res); new.append(y / res)
        frontier = new
    return len(basis)
for r in (2, 3, 4):
    print(" r = %d: dimension at v = 1.37: %d; at v = 1: %d; r! = %d" % (
        r, nonstandard_dim(r, 1.37), nonstandard_dim(r, 1.0), math.factorial(r)))
