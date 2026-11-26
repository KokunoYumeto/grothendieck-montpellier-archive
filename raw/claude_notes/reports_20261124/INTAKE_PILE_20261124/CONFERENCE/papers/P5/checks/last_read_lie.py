"""Lemma 5.2 and Theorem 5.3(1) in small rank: the stabilizer of z_n = (e_n, F_n) in gl_n and in the diagonal torus.

Conference convener ae84c4aa (Claude Fable 5.2 at effort max), 25 Nov 2026. Exact arithmetic; written from the
statement, F_n = sum_{i<n} [e_i,[e_i,e_{i+1}]] inside W^(x3), with [a,b] = ab - ba.
"""
import itertools
import sys

import sympy as sp

sys.stdout.reconfigure(encoding="utf-8")


def word(i, j, k):
    """[e_i,[e_j,e_k]] as a dict on index triples"""
    out = {}
    for t, c in (((i, j, k), 1), ((i, k, j), -1), ((j, k, i), -1), ((k, j, i), 1)):
        out[t] = out.get(t, 0) + c
    return {t: c for t, c in out.items() if c}


def act(a, b, tensor, n):
    """E_ab (e_b -> e_a) as a derivation on a tensor of W^(x3)"""
    out = {}
    for t, c in tensor.items():
        for pos in range(3):
            if t[pos] == b:
                u = list(t)
                u[pos] = a
                u = tuple(u)
                out[u] = out.get(u, 0) + c
    return {t: c for t, c in out.items() if c}


ALL = True
for n in range(2, 8):
    F = {}
    for i in range(n - 1):
        for t, c in word(i, i, i + 1).items():
            F[t] = F.get(t, 0) + c
    norm6 = all(sum(c * c for c in word(i, i, i + 1).values()) == 6 for i in range(n - 1))
    triples = list(itertools.product(range(n), repeat=3))
    rows = []
    for a in range(n):
        for b in range(n):
            col = [0] * (n + len(triples))
            if b == n - 1:                       # E_ab e_n = e_a
                col[a] = 1
            img = act(a, b, F, n)
            for t, c in img.items():
                col[n + triples.index(t)] = c
            rows.append(col)
    rank = sp.Matrix(rows).rank()
    M = 2 ** (n - 1)
    w = [((-2) ** i) % M for i in range(n)]
    g_fixes = w[n - 1] == 0 and all((sum(w[i] for i in t)) % M == 0 for t in F)
    # diagonal elements fixing z_n: d_n = 1, d_i^2 d_(i+1) = 1  => the cyclic group of order M
    count = sum(1 for k in range(M)
                if all((2 * ((-2) ** i * k) + ((-2) ** (i + 1) * k)) % M == 0 for i in range(n - 1)))
    ok = rank == n * n and g_fixes and norm6 and count == M
    ALL = ALL and ok
    print("n = %d: rank of X -> X.z_n is %d of %d; g fixes z_n: %s; Lie words of squared norm 6: %s; %s"
          % (n, rank, n * n, g_fixes, norm6, "as claimed" if ok else "DIFFERENT"))
print("ALL AS CLAIMED" if ALL else "SOME CHECK FAILED")
