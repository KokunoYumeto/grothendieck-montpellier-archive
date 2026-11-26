"""Finite marks, blind proper restrictions and a trace form in a mixed basis."""
from collections import Counter
from itertools import product
from functools import lru_cache
from check_covers import transports


def vector_lattice(p, r):
    vectors = list(product(range(p), repeat=r))
    @lru_cache(None)
    def add(x, y):
        return tuple((a + b) % p for a, b in zip(x, y))
    zero = frozenset([vectors[0]])
    spaces = {zero}
    queue = [zero]
    for h in queue:
        for v in vectors:
            if v in h:
                continue
            scalars = [tuple(k*a % p for a in v) for k in range(p)]
            k = frozenset(add(x, a) for x in h for a in scalars)
            if k not in spaces:
                queue.append(k)
                spaces.add(k)
    return spaces, add


def marks(p, r):
    spaces, add = vector_lattice(p, r)
    G = max(spaces, key=len)
    orbits = []
    for H in spaces:
        d = next(i for i in range(r+1) if p**i * len(H) == len(G))
        m = (-1)**d * p**((d-1)*(d-2)//2)
        for _ in range(abs(m)):
            orbits.append((H, m > 0))
    checks = 0
    for K in spaces:
        restrictions = [Counter(), Counter()]
        for H, positive in orbits:
            # Every K-orbit within G/H has stabilizer H intersect K.
            J = H & K
            count = (len(G)*len(J)) // (len(H)*len(K))
            restrictions[positive][J] += count
        if K == G:
            assert restrictions[1][G] - restrictions[0][G] == p
        else:
            assert restrictions[0] == restrictions[1]
            checks += 1
    n = sum(len(G)//len(H) for H, positive in orbits if positive)
    print("p/r/sheets/proper restrictions", p, r, n, checks)


def null_basis(rows, p, columns):
    a = [[t % p for t in row] for row in rows]
    k = 0
    pivots = []
    for j in range(columns):
        try:
            ii = next(i for i in range(k, len(a)) if a[i][j])
        except StopIteration:
            continue
        a[k], a[ii] = a[ii], a[k]
        scale = pow(a[k][j], -1, p)
        a[k] = [t*scale % p for t in a[k]]
        for i, row in enumerate(a):
            if i != k and row[j]:
                a[i] = [(t-row[j]*u) % p for t, u in zip(row, a[k])]
        k += 1
        pivots.append(j)
    basis = []
    for f in (i for i in range(columns) if i not in pivots):
        v = [int(j == f) for j in range(columns)]
        for i, j in enumerate(pivots):
            v[j] = -a[i][f] % p
        basis.append(v)
    return basis


def gram_repair(regular, p):
    from sympy import Matrix, eye
    n = 6
    S = eye(n)
    for j in range(2*n+1):
        i, h = j % n, (j+1) % n
        S[i, :] += (j+1)*S[h, :]
    S_inv = S.inv()
    equations = []
    for perm in transports(regular):
        A = Matrix(n, n, lambda i, j: int(i == perm[j]))
        equations.extend((S_inv*A*S-eye(n)).tolist())
    W = Matrix(null_basis(equations, p, n)).T
    gram = W.T*S.T*S*W
    return gram.cols - len(null_basis(gram.tolist(), p, gram.cols))


if __name__ == "__main__":
    for p, r in ((2, 2), (2, 3), (2, 4), (3, 2), (3, 3)):
        marks(p, r)
    for p, expected in ((2, [2, 0]), (3, [3, 3])):
        ranks = [gram_repair(regular, p) for regular in (True, False)]
        assert ranks == expected
        print("ground characteristic/Gram ranks", p, ranks)
