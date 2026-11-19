"""Finite certificates used in the odd-plane and alpha_4 Picard arguments.

Python standard library only.  These checks verify the stated algebraic
identities and finite linear systems; they do not replace the geometric
monodromy proof or the cited transvection classification.
"""
from itertools import combinations, permutations
from math import comb
import json
import time
from pathlib import Path


def rank(rows, p):
    if not rows:
        return 0
    a = [[x % p for x in row] for row in rows]
    r = 0
    for j in range(len(a[0])):
        z = next((i for i in range(r, len(a)) if a[i][j]), None)
        if z is None:
            continue
        a[r], a[z] = a[z], a[r]
        q = pow(a[r][j], -1, p)
        a[r] = [q*x % p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][j]:
                q = a[i][j]
                a[i] = [(x-q*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def wedge(v, w):
    return [v[i]*w[j]-v[j]*w[i]
            for i, j in combinations(range(len(v)), 2)]


def add(a, b, scale=1):
    return [[x+scale*y for x, y in zip(r, s)] for r, s in zip(a, b)]


def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col))
             for col in zip(*b)] for row in a]


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def trans(i, j, a=1):
    t = eye(3)
    t[i][j] = a
    return t


def cocycle_certificate(p):
    roots = list(permutations(range(3), 2))
    blocks = {}
    for t, ij in enumerate(roots):
        a = [[0]*18 for _ in range(3)]
        for j in range(3):
            a[j][3*t+j] = 1
        blocks[ij] = a
    equations = []
    for i, j in roots:
        diag = eye(3)
        diag[i][i] = diag[j][j] = -1
        equations.extend(mm(add(diag, eye(3), -1), blocks[i, j]))
    for i, j, k in permutations(range(3)):
        x, y = trans(i, j), trans(j, k)
        xi, yi = trans(i, j, -1), trans(j, k, -1)
        # c(x y x^-1 y^-1) with c(x^-1)=-x^-1 c(x).
        c = blocks[i, j]
        c = add(c, mm(x, blocks[j, k]))
        c = add(c, mm(mm(mm(x, y), xi), blocks[i, j]), -1)
        c = add(c, mm(mm(mm(mm(x, y), xi), yi), blocks[j, k]), -1)
        c = add(c, blocks[i, k], -1)
        equations.extend(c)
    r = rank(equations, p)
    assert r == 18
    return {"p": p, "variables": 18, "equations": len(equations),
            "rank": r, "normalized_cocycle_nullity": 18-r}


# Polynomial algebra F2[a,b,c,d,...]/(a^2,b^2,c^2,d^2,...).
# A polynomial is a bitset of squarefree monomial masks.
def poly(*monomials):
    z = 0
    for m in monomials:
        z ^= 1 << m
    return z


def pmul(a, b):
    out = 0
    while a:
        bit = a & -a
        i = bit.bit_length()-1
        a ^= bit
        bb = b
        while bb:
            bit = bb & -bb
            j = bit.bit_length()-1
            bb ^= bit
            if not i & j:
                out ^= 1 << (i | j)
    return out


def pmm(a, b):
    def entry(row, col):
        z = 0
        for x, y in zip(row, col):
            z ^= pmul(x, y)
        return z
    return [[entry(row, col) for col in zip(*b)] for row in a]


def group_matrix(a, b):
    # Jordan block J has J e_i=e_(i+1), J^4=0.
    coeff = [poly(0), a, b, pmul(a, b)]
    return [[coeff[i-j] if 0 <= i-j < 4 else 0
             for j in range(4)] for i in range(4)]


def alpha4_certificate():
    a, b, c, d, e, f = [poly(1 << i) for i in range(6)]
    # (a,b)*(c,d)=(a+c,b+d+ac).
    assert pmm(group_matrix(a, b), group_matrix(c, d)) == group_matrix(
        a ^ c, b ^ d ^ pmul(a, c))
    left = (a ^ c ^ e, b ^ d ^ pmul(a, c) ^ f ^ pmul(a ^ c, e))
    right = (a ^ c ^ e, b ^ d ^ f ^ pmul(c, e) ^ pmul(a, c ^ e))
    assert left == right
    assert pmul(a ^ c, a ^ c) == 0
    assert pmul(b ^ d ^ pmul(a, c), b ^ d ^ pmul(a, c)) == 0
    # Primitive elements of O(G), in basis 1,a,b,ab.
    delta = [poly(0), a ^ c, b ^ d ^ pmul(a, c),
             pmul(a ^ c, b ^ d ^ pmul(a, c))]
    first = [poly(0), a, b, pmul(a, b)]
    second = [poly(0), c, d, pmul(c, d)]
    matrix = [[((delta[j] ^ first[j] ^ second[j]) >> i) & 1
               for j in range(4)] for i in range(16)]
    assert rank(matrix, 2) == 3
    assert all(row[1] == 0 for row in matrix)
    # Multiplication on dual coalgebra is truncated polynomial multiplication.
    # Multiplication of G's dual-basis coordinates is divided-power multiplication.
    g_basis = [poly(0), a, b, pmul(a, b)]
    for i in range(4):
        for j in range(4):
            expected = (g_basis[i+j] if i+j < 4 and comb(i+j, i) % 2 else 0)
            assert pmul(g_basis[i], g_basis[j]) == expected
    j8 = [[0]*8 for _ in range(8)]
    for start in (0, 4):
        for i in range(3):
            j8[start+i+1][start+i] = 1
    assert rank(j8, 2) == 6
    assert rank(mm(j8, j8), 2) == 4
    return {"group": "Cartier dual of alpha_4 over F2",
            "hopf_algebra": "F2[a,b]/(a^2,b^2)",
            "group_law": "(a,b)*(c,d)=(a+c,b+d+ac)",
            "matrix_representation": "I+aJ+bJ^2+abJ^3, two 4x4 Jordan blocks",
            "associativity": True, "representation_identity": True,
            "primitive_dimension": 1, "primitive_basis": ["a"],
            "frobenius_on_primitives": 0,
            "dimension_V": 8, "rank_J_squared": 4,
            "nonfree_projective_locus": "P(ker J^2)=P^3 in P^7",
            "nonfree_codimension": 4}


def main():
    t0 = time.perf_counter()
    out = {"matching_matrix": [[0, 1, 1], [1, 0, -1], [-1, 1, 0]],
           "matching_determinant": 2, "wedge_span_checks": []}
    for p in (3, 5, 7, 11):
        for d in range(4, 11):
            w_basis = eye(d-1) + [[-1]*(d-1)]
            primal, dual = [], []
            for i, j, k, l in permutations(range(d), 4):
                if i > j or k > l or (i, j) > (k, l):
                    continue
                r = [x-y for x, y in zip(w_basis[i], w_basis[j])]
                s = [x-y for x, y in zip(w_basis[k], w_basis[l])]
                primal.append(wedge(r, s))
                rr = [int(x == i)-int(x == j) for x in range(d-1)]
                ss = [int(x == k)-int(x == l) for x in range(d-1)]
                dual.append(wedge(rr, ss))
            rp, rd = rank(primal, p), rank(dual, p)
            expected = comb(d-2 if d % p == 0 else d-1, 2)
            assert rp == expected and rd == comb(d-1, 2)
            out["wedge_span_checks"].append({"p": p, "d": d,
                "primal_rank": rp, "dual_rank": rd, "expected_A_rank": expected})
    out["sl3_cocycle_checks"] = [cocycle_certificate(p) for p in (3, 5, 7, 11)]
    out["alpha4"] = alpha4_certificate()
    out["runtime_seconds"] = time.perf_counter()-t0
    path = Path(__file__).resolve().parent.parent / "outputs/odd_plane_and_alpha4_checks.json"
    path.write_text(json.dumps(out, indent=2)+"\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
