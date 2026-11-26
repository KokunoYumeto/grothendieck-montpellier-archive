# Independent check (Claude Opus 5.5 at effort high, intake pile 24 Nov 2026) of S2COUNT A.M1 / Prop. Mr-homology:
# integral homology of the normalized bar complex of M_r = {1, x00,x01,x10,x11, y_1..y_r}, vw = x_{row v, col w}.
# Ranks over Q (float SVD), F_2 and F_3 (own elimination) of the boundary maps; H_n = Z^{r^(n-2)} expected, no torsion.
import itertools, numpy as np, sys
def monoid(r):
    els = ['x00','x01','x10','x11'] + ['y%d'%s for s in range(1,r+1)]
    row = {'x00':0,'x01':0,'x10':1,'x11':1}; col = {'x00':0,'x01':1,'x10':0,'x11':1}
    for s in range(1,r+1): row['y%d'%s]=0; col['y%d'%s]=0
    mul = lambda v,w: 'x%d%d'%(row[v],col[w])
    return els, mul
def boundary(els, mul, n):
    idx_n = {c:i for i,c in enumerate(itertools.product(els, repeat=n))}
    idx_m = {c:i for i,c in enumerate(itertools.product(els, repeat=n-1))} if n>1 else {():0}
    D = np.zeros((len(idx_m), len(idx_n)), dtype=np.int64)
    for c,j in idx_n.items():
        if n==1: continue  # d1 = 0 (both faces are the empty bar)
        D[idx_m[c[1:]],j] += 1
        for i in range(n-1):
            p = mul(c[i],c[i+1])  # never the identity here
            D[idx_m[c[:i]+(p,)+c[i+2:]],j] += (-1)**(i+1)
        D[idx_m[c[:-1]],j] += (-1)**n
    return D
def rank_mod(A, p):
    A = (A % p).astype(np.int64); r = 0; rows, cols = A.shape
    for c in range(cols):
        piv = np.nonzero(A[r:,c])[0]
        if len(piv)==0: continue
        k = r+piv[0]; A[[r,k]] = A[[k,r]]
        inv = pow(int(A[r,c]), p-2, p); A[r] = (A[r]*inv) % p
        nz = np.nonzero(A[:,c])[0]; nz = nz[nz!=r]
        A[nz] = (A[nz] - np.outer(A[nz,c], A[r])) % p
        r += 1
        if r==rows: break
    return r
for r_, N in ((0,5),(1,5),(2,4)):
    els, mul = monoid(r_)
    # associativity of the multiplication on non-identity elements
    assert all(mul(mul(a,b),c)==mul(a,mul(b,c)) for a in els for b in els for c in els)
    ranks = {}
    for n in range(1, N+2):
        D = boundary(els, mul, n)
        ranks[n] = {'Q': np.linalg.matrix_rank(D.astype(float)) if D.size else 0,
                    2: rank_mod(D,2) if D.size else 0, 3: rank_mod(D,3) if D.size else 0}
    for n in range(1, N+1):
        dim = len(els)**n
        out = {k: dim - ranks[n][k] - ranks[n+1][k] for k in ('Q',2,3)}
        print('r=%d H_%d: betti_Q=%s dim_F2=%s dim_F3=%s expected %s' % (r_, n, out['Q'], out[2], out[3], (r_**(n-2) if n>=2 else 0)))
    sys.stdout.flush()
