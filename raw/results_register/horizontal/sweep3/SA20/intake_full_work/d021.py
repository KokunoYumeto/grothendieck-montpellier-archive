"""RESEARCH_SA20 D.021: independent recomputation of the norms of the root values of a primitive Coxeter eigenvector
v = sum_j zeta^-j C^j e_1 on the coweight lattice (adjoint group), C the contragredient Coxeter matrix.
Claude Opus 5.5 at effort max, acf08879a01b97ed4, full intake round 3, 22 Nov 2026."""
import cmath, math
from fractions import Fraction
def cartan(t):
    if t == "G2": return [[2,-1],[-3,2]]
    if t == "F4": return [[2,-1,0,0],[-1,2,-2,0],[0,-1,2,-1],[0,0,-1,2]]
    n = int(t[1]); A = [[0]*n for _ in range(n)]
    for i in range(n): A[i][i] = 2
    # Bourbaki E_n: 1-3-4-5-..., 2 attached to 4
    edges = [(1,3),(3,4),(4,2)] + [(k,k+1) for k in range(4,n)]
    for a,b in edges: A[a-1][b-1] = A[b-1][a-1] = -1
    return A
def run(t):
    A = cartan(t); r = len(A)   # A[i][j] = <alpha_i^vee, alpha_j>
    def refl(i, v):  # v in simple-root coordinates
        w = list(v); w[i] -= sum(A[i][j]*v[j] for j in range(r)); return tuple(w)
    simple = [tuple(1 if k == i else 0 for k in range(r)) for i in range(r)]
    roots = set(simple); frontier = list(simple)
    while frontier:
        new = []
        for v in frontier:
            for i in range(r):
                w = refl(i, v)
                if w not in roots: roots.add(w); new.append(w)
        frontier = new
    pos = [v for v in roots if all(x >= 0 for x in v)]
    h = len(roots) // r
    # Coxeter c = s_1 ... s_r on root coordinates (columns = images of simple roots)
    def cox(v):
        for i in reversed(range(r)): v = refl(i, v)
        return v
    cm = [list(col) for col in zip(*[cox(s) for s in simple])]  # matrix c (rows x cols)
    # contragredient on coweights: C = (c^-1)^T ; compute c^-1 via c^(h-1)
    def matmul(X, Y): return [[sum(X[i][k]*Y[k][j] for k in range(r)) for j in range(r)] for i in range(r)]
    I = [[int(i == j) for j in range(r)] for i in range(r)]
    P = I
    for _ in range(h - 1): P = matmul(P, cm)
    C = [list(row) for row in zip(*P)]
    assert matmul(matmul(P, cm), I) == I
    norms = set(); bad = []
    units = [k for k in range(1, h) if math.gcd(k, h) == 1]
    vecs = {}
    for k in units:
        z = cmath.exp(2j * math.pi * k / h)
        v = [0j]*r; Cj = I
        for j in range(h):
            col = [Cj[i][0] for i in range(r)]
            v = [v[i] + z**(-j) * col[i] for i in range(r)]
            Cj = matmul(C, Cj)
        vecs[k] = v
    for a in pos:
        N = 1
        for k in units: N *= sum(a[i] * vecs[k][i] for i in range(r))
        n = round(N.real); assert abs(N - n) < 1e-6 * max(1, abs(n)), (t, a, N)
        norms.add(abs(n))
    primes = set()
    for n in norms:
        m = n; p = 2
        while m > 1:
            while m % p == 0: primes.add(p); m //= p
            p += 1
    print(t, "h =", h, "positive roots", len(pos), "norm set", sorted(norms), "primes", sorted(primes),
          "all divide h:", all(h % p == 0 for p in primes))
for t in ["G2", "F4", "E6", "E7", "E8"]: run(t)
