# Independent check (Claude Opus 5.5 at effort high, intake pile 24 Nov 2026) of RESIDUE A.5 / S2COUNT B3a:
# number of monoids of order n <= 5 up to isomorphism (RESIDUE: 1, 2, 7, 35, 228), and among order 5 the ones whose
# minimal ideal has |I|,|J| >= 2 (the rectangular-band monoid 1 + 2x2), plus H_2, H_3 of BM for every order-5 monoid
# over Q and F_2 (bar complex), compared with the claim "BM is BH for a finite group H, or S^2".
import itertools, sys, numpy as np
def monoids(n):
    E = list(range(1, n))          # 0 is the identity
    cells = [(a, b) for a in E for b in E]
    T = {}
    def prod(a, b):
        if a == 0: return b
        if b == 0: return a
        return T.get((a, b))
    def ok():
        for a in E:
            for b in E:
                ab = prod(a, b)
                if ab is None: continue
                for c in E:
                    bc = prod(b, c)
                    if bc is None: continue
                    l = prod(ab, c); r = prod(a, bc)
                    if l is not None and r is not None and l != r: return False
        return True
    out = []
    def rec(i):
        if i == len(cells):
            out.append(dict(T)); return
        for v in range(n):
            T[cells[i]] = v
            if ok(): rec(i + 1)
            del T[cells[i]]
    rec(0)
    return out
def canon(T, n):
    E = list(range(1, n)); best = None
    for p in itertools.permutations(E):
        m = {0: 0}; m.update(dict(zip(E, p)))
        key = tuple(m[T[(a, b)]] if True else 0 for a, b in sorted(((m_inv, None) for m_inv in []), key=lambda x: x)) if False else None
        inv = {v: k for k, v in m.items()}
        key = tuple(m[T[(inv[a], inv[b])]] for a in E for b in E)
        if best is None or key < best: best = key
    return best
def rank_mod(A, p):
    A = (A % p).astype(np.int64); r = 0; rows, cols = A.shape
    for c in range(cols):
        piv = np.nonzero(A[r:, c])[0]
        if len(piv) == 0: continue
        k = r + piv[0]; A[[r, k]] = A[[k, r]]
        A[r] = (A[r] * pow(int(A[r, c]), p - 2, p)) % p
        nz = np.nonzero(A[:, c])[0]; nz = nz[nz != r]
        A[nz] = (A[nz] - np.outer(A[nz, c], A[r])) % p
        r += 1
        if r == rows: break
    return r
def homology(T, n, top, primes=(2,)):
    # normalized bar complex: cells = tuples of non-identity elements; a face producing the identity is degenerate (0)
    E = list(range(1, n))
    mul = lambda a, b: T[(a, b)]
    idx = {k: {c: i for i, c in enumerate(itertools.product(E, repeat=k))} for k in range(0, top + 2)}
    def D(k):
        M = np.zeros((len(idx[k - 1]), len(idx[k])), dtype=np.int64)
        if k == 1: return M
        for c, j in idx[k].items():
            M[idx[k - 1][c[1:]], j] += 1
            for i in range(k - 1):
                p = mul(c[i], c[i + 1])
                if p != 0: M[idx[k - 1][c[:i] + (p,) + c[i + 2:]], j] += (-1) ** (i + 1)
            M[idx[k - 1][c[:-1]], j] += (-1) ** k
        return M
    Ds = {k: D(k) for k in range(1, top + 2)}
    res = {}
    for F in ('Q',) + tuple(primes):
        rk = {k: (np.linalg.matrix_rank(Ds[k].astype(float)) if F == 'Q' else rank_mod(Ds[k], F)) for k in Ds}
        res[F] = [len(idx[k]) - rk[k] - rk[k + 1] for k in range(1, top + 1)]
    return res
counts = {}
for n in range(1, 6):
    ms = monoids(n)
    classes = {}
    for T in ms: classes.setdefault(canon(T, n), T)
    counts[n] = len(classes)
    print('order', n, 'labelled (identity fixed at 0):', len(ms), 'iso classes:', len(classes)); sys.stdout.flush()
    if n == 5:
        reps = list(classes.values())
        nontrivial = []
        for T in reps:
            h = homology(T, n, 3)
            units = [a for a in range(1, n) if any(T[(a, b)] == 0 and T[(b, a)] == 0 for b in range(1, n))]
            # rational homology of BH for finite H is that of a point; flag any monoid with rational H_1..H_3 != 0
            if any(h['Q']): nontrivial.append((T, h))
        print('order-5 monoids with nonzero rational H_1..H_3:', len(nontrivial))
        for T, h in nontrivial: print('  table', [[T[(a, b)] for b in range(1, n)] for a in range(1, n)], h)
print('counts', counts, 'expected {1: 1, 2: 2, 3: 7, 4: 35, 5: 228}')
