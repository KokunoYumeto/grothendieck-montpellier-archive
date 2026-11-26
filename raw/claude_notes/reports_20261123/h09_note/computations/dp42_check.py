"""Exact check of DP42's coefficient congruence (eq:pathcoefficient) along mixed lines, written independently of the
DP_MULT run's code (Claude Opus 5.5 at effort max, 23 Nov 2026). Univariate truncated series in t with exact rationals.
b(S, Y) is DP41's formula (eq:fullprimitive); L_H = sum_n M^n(Y)/p^n with M_1 = Y_d^(p^2), M_i = Y_(i-1)^p (DP32);
L_0 = sum_u S^(q^u)/p^u. Along the line, S = E_0(u t) and Y = E_H(v t)."""
from fractions import Fraction as Fr
import sys

def mul(a, b, D):
    c = [Fr(0)] * (D + 1)
    for i, x in enumerate(a):
        if x:
            for j in range(0, D + 1 - i):
                if b[j]: c[i + j] += x * b[j]
    return c

def pw(a, e, D):
    r = [Fr(0)] * (D + 1); r[0] = Fr(1)
    b = a[:]
    while e:
        if e & 1: r = mul(r, b, D)
        e >>= 1
        if e: b = mul(b, b, D)
    return r

def vp(x, p):
    if x == 0: return None
    n, d, v = x.numerator, x.denominator, 0
    while n % p == 0: n //= p; v += 1
    while d % p == 0: d //= p; v -= 1
    return v

def run(p, h, u, v, D):
    d, q = h - 1, p ** h
    def M(Y):
        return [pw(Y[d - 1], p * p, D)] + [pw(Y[i - 1], p, D) for i in range(1, d)]
    def LH(Y):
        out = [y[:] for y in Y]; cur = [y[:] for y in Y]; n = 0
        while True:
            cur = M(cur); n += 1
            if all(all(c == 0 for c in comp) for comp in cur): break
            for i in range(d):
                for k in range(D + 1): out[i][k] += cur[i][k] / Fr(p ** n)
        return out
    vt = [[Fr(0)] * (D + 1) for _ in range(d)]
    for i in range(d): vt[i][1] = Fr(v[i])
    E = [x[:] for x in vt]
    for _ in range(D + 2):  # E = v t - (L_H(E) - E)
        L = LH(E)
        E = [[vt[i][k] - (L[i][k] - E[i][k]) for k in range(D + 1)] for i in range(d)]
    assert all(LH(E)[i][k] == vt[i][k] for i in range(d) for k in range(D + 1))
    S = [Fr(0)] * (D + 1); S[1] = Fr(u)
    L0S = S[:]  # S^(q^u) has degree >= q > D for the D used here
    assert q > D
    b = [Fr(0)] * (D + 1)
    for j in range(1, d + 1):          # first family: - S^(p^(n+lh+j)) Y_j^(p^n) / p^(n+l+1)
        for n in range(0, 6):
            for l in range(0, 3):
                e1 = p ** (n + l * h + j); e2 = p ** n
                if e1 + e2 > D: continue
                t = mul(pw(S, e1, D), pw(E[j - 1], e2, D), D)
                for k in range(D + 1): b[k] -= t[k] / Fr(p ** (n + l + 1))
    C = [Fr(0)] * (D + 1)              # C(Y) = sum_j sum_l Y_j^(p^(lh+h-j)) / p^(dl+h-j)
    for j in range(1, d + 1):
        for l in range(0, 3):
            e = p ** (l * h + h - j)
            if e > D: continue
            t = pw(E[j - 1], e, D)
            for k in range(D + 1): C[k] += t[k] / Fr(p ** (d * l + h - j))
    t2 = mul(L0S, C, D)
    for k in range(D + 1): b[k] += t2[k]
    jj = min(i for i in range(d) if v[i] % p) + 1
    kk = h - jj; N = p ** kk + 1; Sk = (p ** kk - 1) // (p - 1)
    coef = b[N]
    lhs = coef * p ** Sk
    rhs = (-1) ** (kk - 1) * u * v[jj - 1] ** (p ** kk)
    ok = vp(lhs - rhs, p) is None or vp(lhs - rhs, p) >= 1
    print(f"p={p} h={h} u={u} v={v}: j={jj} k={kk} N_k={N} S_k={Sk}; [t^N]beta = {coef} (v_p = {vp(coef, p)}); "
          f"p^S_k*coef - (-1)^(k-1) u v_j^(p^k) has v_p {vp(lhs - rhs, p)}; congruence {'HOLDS' if ok else 'FAILS'}")
    w = Fr(p ** kk, (p - 1) * (p ** kk + 1))
    vals = [(n, vp(b[n], p)) for n in range(1, D + 1) if b[n]]
    print("   weighted values v_p(a_n) + w_k n at w_k =", w, ":", [(n, float(val + w * n)) for n, val in vals])
    return ok

allok = True
for (p, h, u, v, D) in [(3, 3, 1, (1, 0), 12), (3, 3, 1, (0, 1), 12), (3, 3, 2, (1, 1), 12), (3, 3, 1, (3, 1), 12),
                        (5, 3, 1, (0, 1), 12), (3, 4, 1, (0, 0, 1), 12)]:
    allok &= run(p, h, u, v, D)
print("ALL HOLD" if allok else "SOME FAIL")
