"""Independent check of LM2_LOOP_EQUATIONS B.g3 (dims of H_n and W^lac_n through weight 12).
Two methods: (1) Witt character formula; (2) direct linear algebra in the tensor algebra modulo two primes.
Written by Claude Opus 5.5 (effort high), intake pile 24 Nov 2026. Reads no file of the return."""
import numpy as np
from fractions import Fraction
from itertools import product

N = 12
# ---------- method 1: characters ----------
def mobius(n):
    res, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res
def q(n, tr):  # trace of g on Lie_n V given tr(g^d) function
    s = sum(mobius(d) * tr(d) ** (n // d) for d in range(1, n + 1) if n % d == 0)
    return Fraction(s, n)
tr1 = lambda d: 2
trs = lambda d: 0 if d % 2 else 2       # s: trace 0, s^2 = 1 trace 2
trr = lambda d: 2 if d % 3 == 0 else -1  # r: trace -1, r^3=1
# d_n from prod (1-t^n)^{-d_n} = (1-t^2)/(1-t^2-t^3)
M = N + 2
f = [0] * (M + 1)  # series of (1-t^2)/(1-t^2-t^3)
den = [1, 0, -1, -1] + [0] * M
numr = [1, 0, -1] + [0] * M
for k in range(M + 1):
    f[k] = numr[k] - sum(den[i] * f[k - i] for i in range(1, min(k, 3) + 1))
# log f = sum_n d_n * (-log(1-t^n)) ; compute d_n by successive division
import math
d = [0] * (M + 1)
cur = f[:]
for n in range(1, M + 1):
    d[n] = cur[n]
    # divide cur by (1-t^n)^{-d_n}, i.e. multiply by (1-t^n)^{d_n}
    for _ in range(abs(d[n])):
        if d[n] > 0:
            cur = [cur[k] - (cur[k - n] if k >= n else 0) for k in range(M + 1)]
        else:
            new = cur[:]
            for k in range(M + 1):
                new[k] = cur[k] + (new[k - n] if k >= n else 0)
            cur = new
print('n dimL H_n W_n d_n  (character formula)')
char = {}
for n in range(1, N + 1):
    L = q(n, tr1)
    H = (q(n, tr1) - q(n, trr)) / 3
    W = H - (q(n + 1, tr1) + 3 * q(n + 1, trs) + 2 * q(n + 1, trr)) / 6 if n > 1 else 0
    char[n] = (int(L), H, W, d[n])
    print(n, L, H, W, d[n])

# ---------- method 2: direct linear algebra ----------
def lyndon_words(n):
    # Duval's algorithm, alphabet {0,1}
    w = [-1]
    out = []
    while w:
        w[-1] += 1
        m = len(w)
        if m == n:
            out.append(tuple(w))
        while len(w) < n:
            w.append(w[len(w) - m])
        while w and w[-1] == 1:
            w.pop()
    return out
def is_lyndon(w):
    return all(w < w[i:] + w[:i] for i in range(1, len(w))) if len(w) > 1 else True
P = None
def bracket_vec(w, memo):
    if w in memo:
        return memo[w]
    if len(w) == 1:
        v = np.zeros(2, dtype=np.int64); v[w[0]] = 1
    else:
        # standard factorization: v longest proper Lyndon suffix
        for i in range(1, len(w)):
            if is_lyndon(w[i:]):
                u_, v_ = w[:i], w[i:]
                break
        a = bracket_vec(u_, memo); b = bracket_vec(v_, memo)
        v = (np.kron(a, b) - np.kron(b, a)) % P
    memo[w] = v
    return v
def subst(vec, n, Mx):
    # Mx[old][new]: letter old -> sum_new Mx[old][new] * new
    t = vec.reshape((2,) * n)
    Mm = np.array(Mx, dtype=np.int64) % P
    for ax in range(n):
        t = np.moveaxis(np.tensordot(t, Mm, axes=([ax], [0])) % P, -1, ax)
    return t.reshape(-1)
def rank_mod(A):
    A = A.copy() % P
    r = 0; rows, cols = A.shape
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if A[i, c]:
                piv = i; break
        if piv is None:
            continue
        A[[r, piv]] = A[[piv, r]]
        inv = pow(int(A[r, c]), P - 2, P)
        A[r] = (A[r] * inv) % P
        nz = np.nonzero(A[:, c])[0]
        for i in nz:
            if i != r:
                A[i] = (A[i] - A[i, c] * A[r]) % P
        r += 1
        if r == rows:
            break
    return r
S_ = [[0, 1], [1, 0]]
R1 = [[0, 1], [-1, -1]]    # x->y, y->z
R2 = [[-1, -1], [1, 0]]    # x->z, y->x
JM = [[-1, -1], [0, 1]]    # x-> -x-y, y->y
for P in (1000003, 999983):
    print('prime', P)
    memo = {}
    for n in range(1, N + 1):
        basis = [bracket_vec(w, memo) for w in lyndon_words(n)]
        B = np.array(basis, dtype=np.int64)
        L = len(basis)
        assert rank_mod(B) == L
        rows_H = []
        rows_W = []
        xv = np.array([1, 0], dtype=np.int64); yv = np.array([0, 1], dtype=np.int64)
        for v in basis:
            e1 = (v + subst(v, n, S_)) % P
            e2 = (v + subst(v, n, R1) + subst(v, n, R2)) % P
            rows_H.append(np.concatenate([e1, e2]))
            if n > 1:
                w2 = subst(v, n, JM)
                xy = (xv + yv)
                Jv = (np.kron(xv, v) - np.kron(v, xv) - (np.kron(xy, w2) - np.kron(w2, xy))) % P
                rows_W.append(np.concatenate([e1, np.zeros(2 ** n, dtype=np.int64), Jv]))
        H = L - rank_mod(np.array(rows_H))
        W = (L - rank_mod(np.array(rows_W))) if n > 1 else 0
        c = char[n]
        print(n, L, H, W, 'agree' if (L, H, W) == (c[0], c[1], c[2]) else 'DISAGREE', flush=True)
