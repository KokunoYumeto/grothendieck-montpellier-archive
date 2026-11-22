# Checks for CONSULT_a157422a_FABLE_SHAPE.md (Claude Fable 5.2 at effort max, 21 Nov 2026).
# Run: python -I -B consult_a157422a_checks.py
import itertools
import numpy as np
from mpmath import mp, mpf, zeta, gamma, pi, taylor, log, matrix, eigsy, det, zetazero

mp.dps = 70

def xi(s):
    if s == 1 or s == 0:
        return mpf(1) / 2
    return s * (s - 1) / 2 * pi ** (-s / 2) * gamma(s / 2) * zeta(s)

# ---- 1. Li-Toeplitz kernel K(m,n) = l_m + l_n - l_|m-n| : positive definite sections
N = 10
c = taylor(lambda z: log(xi(1 / (1 - z))), 0, N)
lam = [mpf(0)] + [n * c[n] for n in range(1, N + 1)]
print("lambda_1, lambda_2 =", mp.nstr(lam[1], 12), mp.nstr(lam[2], 12))
for size in (2, 4, 6, 8, 10):
    K = matrix(size, size)
    for m in range(1, size + 1):
        for n in range(1, size + 1):
            K[m - 1, n - 1] = lam[m] + lam[n] - lam[abs(m - n)]
    ev = eigsy(K, eigvals_only=True)
    print("K_%d: min eigenvalue %s, det %s" % (size, mp.nstr(min(ev), 6), mp.nstr(det(K), 6)))

# ---- 2. Polya-frequency / Thoma form: e_n = a_{2n}/a_0, Jacobi-Trudi minors s_lambda > 0
M = 9
a = taylor(xi, mpf(1) / 2, 2 * M)
print("odd Taylor coefficients at 1/2 vanish:", all(abs(a[2 * k + 1]) < mpf(10) ** (-40) for k in range(M)))
e = [a[2 * k] / a[0] for k in range(M + 1)]
print("all a_{2n} > 0:", all(x > 0 for x in e))
def E(k):
    return e[k] if 0 <= k <= M else mpf(0)
def partitions(n, maxpart=None):
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, maxpart), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest
worst = None
count = 0
for size in range(1, M + 1):
    for la in partitions(size):
        # dual Jacobi-Trudi: s_{la'} = det(e_{la_i - i + j})
        r = len(la)
        J = matrix(r, r)
        for i in range(r):
            for j in range(r):
                J[i, j] = E(la[i] - i + j)
        d = det(J)
        count += 1
        if worst is None or d < worst[0]:
            worst = (d, la)
print("Jacobi-Trudi minors checked:", count, "; smallest:", mp.nstr(worst[0], 6), "at", worst[1])
# power sums by Newton's identities versus the zeros
p = [mpf(0)] * (M + 1)
for k in range(1, M + 1):
    # Newton: p_k = sum_{i=1}^{k-1} (-1)^{i-1} e_i p_{k-i} + (-1)^{k-1} k e_k
    s = (-1) ** (k - 1) * k * e[k] + sum((-1) ** (i - 1) * e[i] * p[k - i] for i in range(1, k))
    p[k] = s
mp.dps = 20
gam = [zetazero(k).imag for k in range(1, 61)]
print("Z(2) from Taylor coefficients:", mp.nstr(p[1], 10), "; partial sum over 60 zeros:", mp.nstr(sum(g ** -2 for g in gam), 10))
print("Z(4) from Taylor coefficients:", mp.nstr(p[2], 10), "; partial sum over 60 zeros:", mp.nstr(sum(g ** -4 for g in gam), 10))
print("Z(6) from Taylor coefficients:", mp.nstr(p[3], 10), "; partial sum over 60 zeros:", mp.nstr(sum(g ** -6 for g in gam), 10))
print("Thoma parameters alpha_1..alpha_3:", [mp.nstr(g ** -2 / p[1], 6) for g in gam[:3]])

# ---- 3. Sedenions: dimension of the annihilator of e_i + e_j
def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def cd(x, y):
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a_, b_, c_, d_ = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([cd(a_, c_) - cd(conj(d_), b_), cd(d_, a_) + cd(b_, conj(c_))])
def Lmat(x):
    n = len(x)
    return np.array([cd(x, np.eye(n)[k]) for k in range(n)]).T
dims = {}
for i, j in itertools.combinations(range(1, 16), 2):
    for sgn in (1.0, -1.0):
        x = np.zeros(16); x[i] = 1.0; x[j] = sgn
        nul = 16 - np.linalg.matrix_rank(Lmat(x), tol=1e-9)
        dims[nul] = dims.get(nul, 0) + 1
print("sedenions: nullity of L_x over x = e_i +- e_j (1<=i<j<=15):", dims)
x = np.zeros(16); x[3] = 1; x[10] = 1
Lx = Lmat(x)
u, s, vt = np.linalg.svd(Lx)
ker = vt[np.abs(s) < 1e-9]
z = ker[0]
assoc = cd(cd(x, x), z) - cd(x, cd(x, z))
print("x = e3+e10: x*x =", cd(x, x)[0], "; [x,x,z] = -lambda^{-1}-normalized equals z:", np.allclose(-assoc / 2.0, z))
