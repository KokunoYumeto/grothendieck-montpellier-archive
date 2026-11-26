"""Rank of Ihara brackets W_a x W_b -> W_12 (a+b=12) inside W^lac_12 (LM2 B.g2/B.g3 space), mod a prime.
Bears on LM8_PUSH C.33 notes ("Weight12 rank7 versus bracket rank6"). Claude Opus 5.5 (effort high), 24 Nov 2026."""
import numpy as np
src = "#" + open('check_lm2_graded.py').read().split("# ---------- method 2")[1].split("for P in (1000003")[0]
ns = {}
exec('import numpy as np\n' + src, ns)
P = 1000003
ns['P'] = P
memo = {}
bv = lambda w: ns['bracket_vec'](w, memo)
subst = ns['subst']; lyn = ns['lyndon_words']
xv = np.array([1, 0], dtype=np.int64); yv = np.array([0, 1], dtype=np.int64)

def nullspace_mod(A):
    """rows of A are constraints applied to coefficient vectors? Here: A has shape (m, k); return basis of {c: c A = 0}."""
    A = A.copy() % P
    m, k = A.shape
    # solve c A = 0  <=> A^T c^T = 0
    M = A.T.copy() % P  # shape (k, m)
    rows, cols = M.shape
    piv_cols = []
    r = 0
    for c in range(cols):
        piv = None
        for i in range(r, rows):
            if M[i, c]:
                piv = i; break
        if piv is None:
            continue
        M[[r, piv]] = M[[piv, r]]
        inv = pow(int(M[r, c]), P - 2, P)
        M[r] = (M[r] * inv) % P
        for i in np.nonzero(M[:, c])[0]:
            if i != r:
                M[i] = (M[i] - M[i, c] * M[r]) % P
        piv_cols.append(c); r += 1
        if r == rows: break
    free = [c for c in range(cols) if c not in piv_cols]
    basis = []
    for f in free:
        v = np.zeros(cols, dtype=np.int64); v[f] = 1
        for i, pc in enumerate(piv_cols):
            v[pc] = (-M[i, f]) % P
        basis.append(v)
    return basis

def W_basis(n):
    L = [bv(w) for w in lyn(n)]
    cons = []
    for v in L:
        e1 = (v + subst(v, n, ns['S_'])) % P
        w2 = subst(v, n, ns['JM']); xy = xv + yv
        J = (np.kron(xv, v) - np.kron(v, xv) - (np.kron(xy, w2) - np.kron(w2, xy))) % P
        cons.append(np.concatenate([e1, J]))
    coeffs = nullspace_mod(np.array(cons))
    B = np.array(L)
    return [(c @ B) % P for c in coeffs]

def D_apply(psi, a, phi, b):
    """Derivation D_psi(x)=0, D_psi(y)=[y,psi] applied to degree-b tensor phi; result degree a+b."""
    ypsi = (np.kron(yv, psi) - np.kron(psi, yv)) % P   # degree a+1
    T = phi.reshape((2,) * b)
    out = np.zeros((2,) * (a + b), dtype=np.int64)
    Y = ypsi.reshape((2,) * (a + 1))
    for k in range(b):
        sl = np.take(T, 1, axis=k)          # positions where letter k is y; shape (2,)*(b-1)
        # build tensor: left indices (0..k-1), then Y block, then right indices
        left = sl.reshape((2,) * k + (2 ** (b - 1 - k),)) if k > 0 else sl.reshape((1, 2 ** (b - 1 - k)))
        if k > 0:
            left2 = sl.reshape(2 ** k, 2 ** (b - 1 - k))
        else:
            left2 = sl.reshape(1, 2 ** (b - 1 - k))
        res = np.einsum('ij,k->ikj', left2, ypsi) % P   # (2^k, 2^(a+1), 2^(b-1-k))
        out = (out + res.reshape((2,) * (a + b))) % P
    return out.reshape(-1)

def ihara(psi, a, phi, b):
    br = (np.kron(psi, phi) - np.kron(phi, psi)) % P
    return (D_apply(psi, a, phi, b) - D_apply(phi, b, psi, a) + br) % P

W = {n: W_basis(n) for n in range(3, 13)}
print({n: len(W[n]) for n in W})
def rank_vecs(vs):
    if not vs: return 0
    return ns['rank_mod'](np.array(vs) % P) if True else 0
ns['P'] = P
# sanity: brackets of W elements land in W (check closure) for one pair
def in_span(v, basis):
    return rank_vecs(basis + [v]) == rank_vecs(basis)
for target in (8, 10, 12):
    brs = []
    for a in range(3, target - 2):
        b = target - a
        if a > b: continue
        for i, p_ in enumerate(W.get(a, [])):
            for j, q_ in enumerate(W.get(b, [])):
                if a == b and j <= i: continue
                brs.append(ihara(p_, a, q_, b))
    closed = all(in_span(v, W[target]) for v in brs)
    print(f'weight {target}: dim W = {len(W[target])}, #brackets = {len(brs)}, bracket rank = {rank_vecs(brs)}, brackets inside W: {closed}')
