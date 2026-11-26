import sys; sys.path.insert(0, '.')
from collections import Counter
exec(open('gN.py').read().split("for N in (2, 3, 4):")[0])
def mul(e, f, N): return (mm(e[0], f[0], N), (e[1] + f[1]) % N)
def ident(N): return (red(((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)), N), 0)
def order(x, N):
    y, o = x, 1
    while y != ident(N): y = mul(y, x, N); o += 1
    return o
for N in (2, 4):
    G = gen_group(N)
    Bs = {(M[1][1], M[1][2], M[2][1], M[2][2]) for M, k in G}
    K = [(M, k) for M, k in G if (M[1][1], M[1][2], M[2][1], M[2][2]) == (1, 0, 0, 1)]
    Z = [x for x in G if all(mul(x, y, N) == mul(y, x, N) for y in G)]
    print("N =", N, "|G| =", len(G), " |B-image| =", len(Bs), " |K| =", len(K), " K abelian:", all(mul(x, y, N) == mul(y, x, N) for x in K for y in K),
          " |Z| =", len(Z), " orders:", sorted(Counter(order(x, N) for x in G).items()), " k-values on K:", sorted(Counter(k for M, k in K).items()))
