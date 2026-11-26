# Sanity checks for Section 10 of the note (version 2), standard library only.
# (1) In B_4 (unreduced Burau representation at t = 3, exact rationals): Delta s_i Delta^-1 = s_{4-i},
#     (s1 s2)^3 and (s2 s3)^3 are exchanged by Ad(Delta), (s1 s3 s2)^2 = Delta, Delta^2 is central.
# (2) In B_3: (u v^2)^2 = (u v)^3 and it is central.
# (3) In PSL_2(Z) with u -> U, v -> L: (uv)^3 = 1, (u^2 v)^2 = 1, s = uvu has order 2.
# The Burau representation is not known to be faithful for n = 4; identities that hold in it are necessary
# consequences of the braid identities, and the braid identities themselves are standard. This is a sanity
# check of the conventions, not a proof.
from fractions import Fraction as Fr

def matmul(A, B):
    n = len(A); return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
def ident(n): return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
def inv(A):
    n = len(A); M = [row[:] + ident(n)[i] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0); M[c], M[p] = M[p], M[c]
        d = M[c][c]; M[c] = [x/d for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [x - f*y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]
def burau(i, n, t):
    M = ident(n); M[i-1][i-1] = 1 - t; M[i-1][i] = t; M[i][i-1] = Fr(1); M[i][i] = Fr(0); return M
def word(w, gens):
    n = len(next(iter(gens.values()))); M = ident(n)
    for g in w:
        M = matmul(M, gens[g] if g > 0 else inv(gens[-g]))
    return M

t = Fr(3)
g4 = {i: burau(i, 4, t) for i in (1, 2, 3)}
D = word([1, 2, 3, 1, 2, 1], g4); Di = inv(D)
ok1 = all(matmul(matmul(D, g4[i]), Di) == g4[4 - i] for i in (1, 2, 3))
x45 = word([1, 2]*3, g4); x51 = word([2, 3]*3, g4)
ok2 = matmul(matmul(D, x45), Di) == x51 and matmul(matmul(D, x51), Di) == x45
ok3 = word([1, 3, 2]*2, g4) == D
D2 = matmul(D, D); ok4 = all(matmul(D2, g4[i]) == matmul(g4[i], D2) for i in (1, 2, 3))
print("B4: Delta s_i Delta^-1 = s_{4-i}:", ok1, "| x45 <-> x51:", ok2, "| (s1 s3 s2)^2 = Delta:", ok3, "| Delta^2 central:", ok4)

g3 = {i: burau(i, 3, t) for i in (1, 2)}
lhs = word([1, 2, 2, 1, 2, 2], g3); rhs = word([1, 2]*3, g3)
ok5 = lhs == rhs and all(matmul(rhs, g3[i]) == matmul(g3[i], rhs) for i in (1, 2))
print("B3: (u v^2)^2 = (u v)^3 and central:", ok5)

U = [[Fr(1), Fr(1)], [Fr(0), Fr(1)]]; L = [[Fr(1), Fr(0)], [Fr(-1), Fr(1)]]
gp = {1: U, 2: L}
def pm(M): return M == ident(2) or M == [[-x for x in r] for r in ident(2)]
print("PSL2(Z): (uv)^3 = 1:", pm(word([1, 2]*3, gp)), "| (u^2 v)^2 = 1:", pm(word([1, 1, 2]*2, gp)),
      "| (uvu)^2 = 1:", pm(word([1, 2, 1]*2, gp)), "| (vu)^3 = 1:", pm(word([2, 1]*3, gp)))
