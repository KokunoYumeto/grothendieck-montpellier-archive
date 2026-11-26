# G_N = <(A_1,-1),(A_2,0)> in GL_4(Z/N) x Z/N  (S6 Paper III C.1.4), with Paper V's A_1, A_2 (S6-067)
import itertools
A1 = ((1,0,0,0),(6,0,1,0),(-6,-1,-1,0),(-2,1,0,1))
A2 = ((1,0,0,0),(0,0,-1,0),(-6,1,0,0),(3,0,1,1))
def mm(X, Y, N): return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(4)) % N for j in range(4)) for i in range(4))
def red(X, N): return tuple(tuple(x % N for x in r) for r in X)
def gen_group(N):
    g1 = (red(A1, N), (-1) % N); g2 = (red(A2, N), 0)
    I = (red(((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)), N), 0)
    seen = {I}; frontier = [I]
    while frontier:
        new = []
        for (M, k) in frontier:
            for (G, l) in (g1, g2):
                e = (mm(M, G, N), (k + l) % N)
                if e not in seen: seen.add(e); new.append(e)
        frontier = new
    return seen
for N in (2, 3, 4):
    G = gen_group(N)
    print("N =", N, " |G_N| =", len(G))
G = gen_group(3)
# B-part: middle 2x2 block rows 1-2, cols 1-2
def B(M): return (M[1][1], M[1][2], M[2][1], M[2][2])
Bs = {B(M) for M, k in G}
print("|image in GL_2(F_3) of B-part| =", len(Bs))
K = [(M, k) for M, k in G if B(M) == (1, 0, 0, 1)]
print("|kernel K| =", len(K))
def mul(e, f, N=3): return (mm(e[0], f[0], N), (e[1] + f[1]) % N)
ab = all(mul(x, y) == mul(y, x) for x in K for y in K)
orders = {}
for x in K:
    y, o = x, 1
    I = (red(((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)), 3), 0)
    while y != I: y = mul(y, x); o += 1
    orders[o] = orders.get(o, 0) + 1
print("K abelian:", ab, " element orders in K:", orders)
for x in K[:9]: print("  K elt: col0 =", (x[0][1][0], x[0][2][0], x[0][3][0]), " row3 =", x[0][3][1:3], " k =", x[1])
# does G contain a complement: a subgroup of order 24 mapping isomorphically to SL2(F3)? count elements of order 3 and 4 etc
from collections import Counter
def order(x):
    I = (red(((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)), 3), 0); y, o = x, 1
    while y != I: y = mul(y, x); o += 1
    return o
print("element orders in G_3:", sorted(Counter(order(x) for x in G).items()))
# center of G_3
Z = [x for x in G if all(mul(x, y) == mul(y, x) for y in G)]
print("|Z(G_3)| =", len(Z))
