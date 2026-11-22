"""Independent recomputation for RESEARCH_SA20 D.002: does 1 -> <c> -> N_W(<c>) -> (Z/h)^x -> 1 split?
Own code (Claude Opus 5.5 at effort max, acf08879a01b97ed4, 22 Nov 2026): root systems from Cartan matrices,
Coxeter element c = s1...sr, all intertwiners w with w c = c^a w preserving the root set, membership in W by
chamber reduction of w(rho), then the orders of lifts. Exact rational arithmetic."""
from fractions import Fraction as Fr
import itertools, sys

def cartan(t):
    if t == "G2": return [[2, -1], [-3, 2]]
    if t == "F4": return [[2, -1, 0, 0], [-1, 2, -2, 0], [0, -1, 2, -1], [0, 0, -1, 2]]
    n = int(t[1:])
    A = [[2 if i == j else 0 for j in range(n)] for i in range(n)]
    # E_n Bourbaki: 1-3-4-5-..., 2 attached to 4
    edges = [(0, 2), (2, 3), (1, 3)] + [(k, k + 1) for k in range(3, n - 1)]
    for i, j in edges: A[i][j] = A[j][i] = -1
    return A

def mat_mul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mat_vec(A, v): return tuple(sum(A[i][k] * v[k] for k in range(len(v))) for i in range(len(A)))
def ident(n): return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
def inv(M):
    n = len(M); A = [list(map(Fr, r)) + [Fr(int(i == j)) for j in range(n)] for i, r in enumerate(M)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0); A[c], A[p] = A[p], A[c]
        pv = A[c][c]; A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]; A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [r[n:] for r in A]

def run(t):
    A = cartan(t); r = len(A)
    # coordinates: simple-root basis; s_i(v) = v - <v, alpha_i^vee> alpha_i, with <alpha_j, alpha_i^vee> = A[i][j]
    S = []
    for i in range(r):
        M = ident(r)
        for j in range(r): M[i][j] -= A[i][j]  # column j = s_i(alpha_j) = alpha_j - A[i][j] alpha_i
        S.append(M)
    simple = [tuple(Fr(int(i == j)) for j in range(r)) for i in range(r)]
    R = set(simple); fr = list(simple)
    while fr:
        nf = []
        for v in fr:
            for M in S:
                u = mat_vec(M, v)
                if u not in R: R.add(u); nf.append(u)
        fr = nf
    R = sorted(R)
    c = ident(r)
    for M in S: c = mat_mul(c, M)
    h = len(R) // r
    cp = [ident(r)]
    for k in range(1, 2 * h + 1): cp.append(mat_mul(cp[-1], c))
    assert cp[h] == ident(r)
    # vector v whose c-orbit spans
    for v in R:
        orb = [mat_vec(cp[k], v) for k in range(h)]
        for js in itertools.combinations(range(h), r):
            B = [[orb[j][i] for j in js] for i in range(r)]
            try: Bi = inv(B)
            except StopIteration: continue
            break
        else: continue
        break
    Rs = set(R)
    # chamber membership: w in W iff reducing w(rho') by simple reflections returns w to identity; use a regular
    # vector in the coroot-dual sense: test via action on roots: w in W iff w permutes R and, after reducing, is id.
    # Positive roots: nonnegative coordinates.
    def is_pos(v): return all(x >= 0 for x in v)
    def in_W(w):
        w = [row[:] for row in w]
        while True:
            # find simple root alpha_i with w^{-1}(alpha_i) < 0, i.e. w maps some positive root... use: left descent
            done = True
            winv = inv(w)
            for i in range(r):
                if not is_pos(mat_vec(winv, simple[i])):
                    w = mat_mul(S[i], w); done = False; break
            if done: return w == ident(r)
    units = [a for a in range(1, h) if __import__("math").gcd(a, h) == 1]
    lifts = {}
    for a in units:
        L = []
        for u in R:
            cols = [mat_vec(cp[(a * j) % h], u) for j in js]
            Bu = [[cols[k][i] for k in range(r)] for i in range(r)]
            w = mat_mul(Bu, Bi)
            if any(x.denominator != 1 for row in w for x in row): continue
            if mat_mul(w, c) != mat_mul(cp[a % h], w): continue
            if any(mat_vec(w, x) not in Rs for x in R): continue
            if not in_W(w): continue
            L.append(w)
        lifts[a] = L
    Nsize = sum(len(L) for L in lifts.values())
    # splitting test: does there exist a homomorphic section? check each unit's lifts orders vs unit order
    def order_mod(a):
        k, x = 1, a % h
        while x != 1: x = x * a % h; k += 1
        return k
    def mpow(w, k):
        P = ident(r)
        for _ in range(k): P = mat_mul(P, w)
        return P
    bad = []
    for a in units:
        o = order_mod(a)
        ok = any(mpow(w, o) == ident(r) for w in lifts[a])
        if not ok: bad.append((a, o))
    print(t, "|R| =", len(R), "h =", h, "|N_W(<c>)| =", Nsize, "lifts per unit:", sorted(set(len(L) for L in lifts.values())),
          "units with no lift of the same order:", bad)
    sys.stdout.flush()

for t in sys.argv[1:] or ["G2", "F4", "E6", "E7", "E8"]:
    run(t)
