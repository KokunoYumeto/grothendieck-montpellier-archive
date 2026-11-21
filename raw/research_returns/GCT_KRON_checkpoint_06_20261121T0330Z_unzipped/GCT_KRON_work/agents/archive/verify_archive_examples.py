"""Exact finite checks for archive findings A-001, A-002, A-005, A-008.

This is a reproducible computation, not a formal proof of the general statements.
Python standard library only. All matrix operations use exact arithmetic modulo p.
"""
from itertools import combinations
from pathlib import Path
import csv
from datetime import datetime, timezone


def rank(a, p):
    a = [[x % p for x in row] for row in a]
    n, m = len(a), len(a[0]) if a else 0
    r = 0
    for j in range(m):
        pivot = next((i for i in range(r, n) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(n):
            if i != r:
                c = a[i][j]
                a[i] = [(x - c * y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == n:
            break
    return r


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def jordan(n):
    return [[int(i == j) + int(j == i + 1) for j in range(n)] for i in range(n)]


def product(a, b, p):
    return [[sum(x * y for x, y in zip(row, col)) % p
             for col in zip(*b)] for row in a]


def kron(a, b):
    return [[x * y for x in row_a for y in row_b]
            for row_a in a for row_b in b]


def exterior2(a, p):
    ij = list(combinations(range(len(a)), 2))
    return [[(a[i][k] * a[j][l] - a[i][l] * a[j][k]) % p
             for k, l in ij] for i, j in ij]


def jordan_type(a, p):
    n = len(a)
    t = [[(a[i][j] - int(i == j)) % p for j in range(n)] for i in range(n)]
    powers = identity(n)
    ranks = [n]
    for _ in range(n + 1):
        powers = product(powers, t, p)
        ranks.append(rank(powers, p))
        if ranks[-1] == 0:
            break
    ranks.append(0)
    blocks = []
    for k in range(1, len(ranks) - 1):
        blocks.extend([k] * (ranks[k-1] - 2*ranks[k] + ranks[k+1]))
    assert sum(blocks) == n
    return tuple(sorted(blocks, reverse=True))


def main():
    events = []
    def check(statement, name, actual, expected):
        assert actual == expected, (statement, name, actual, expected)
        events.append((statement, name, repr(actual), "PASS"))

    # A-001: C2 acts on a free two-set. Fixed-point marks are indexed by 1,C2.
    e = (2, 0)
    p2 = (1, 1)
    square = (4, 0)
    claimed_rhs = tuple(2*x+y for x,y in zip(p2,e))
    check("A-001", "C2: marks of E^2", square, (4,0))
    check("A-001", "C2: marks of 2*P2(E)+E", claimed_rhs, (4,2))
    assert claimed_rhs != square

    # A-002: V4 marks are indexed by G,H1,H2,H3,1.
    one = (1,1,1,1,1)
    xs = [(0,2,0,0,2),(0,0,2,0,2),(0,0,0,2,2)]
    free = (0,0,0,0,4)
    lam2_free = tuple(3*free[i] - sum(x[i] for x in xs) for i in range(5))
    p2_universal = tuple(2*free[i]-2*one[i] for i in range(5))
    check("A-002", "V4: canonical lambda2(E) marks", lam2_free, (0,-2,-2,-2,6))
    check("A-002", "V4: universal product RHS marks", p2_universal, (-2,-2,-2,-2,6))
    assert lam2_free != p2_universal

    # A-005: Jordan tensor and exterior computations in characteristic three.
    check("A-005", "J2 tensor J2", jordan_type(kron(jordan(2),jordan(2)),3), (3,1))
    check("A-005", "J2 tensor J3", jordan_type(kron(jordan(2),jordan(3)),3), (3,3))
    check("A-005", "J3 tensor J3", jordan_type(kron(jordan(3),jordan(3)),3), (3,3,3))
    check("A-005", "exterior2 J2", jordan_type(exterior2(jordan(2),3),3), (1,))
    check("A-005", "exterior2 J3", jordan_type(exterior2(jordan(3),3),3), (3,))
    def add(u,v):
        return tuple(x+y for x,y in zip(u,v))
    def scale(c,u):
        return tuple(c*x for x in u)
    def green_mul(u,v):
        table = [[(1,0,0),(0,1,0),(0,0,1)],
                 [(0,1,0),(1,0,1),(0,0,2)],
                 [(0,0,1),(0,0,2),(0,0,3)]]
        out=(0,0,0)
        for i in range(3):
            for j in range(3):
                out=add(out,scale(u[i]*v[j],table[i][j]))
        return out
    unit,a,b=(1,0,0),(0,1,0),(0,0,1)
    psi_a=add(green_mul(green_mul(a,a),a),scale(-3,a))
    psi_b=add(add(green_mul(green_mul(b,b),b),scale(-3,green_mul(b,b))),scale(3,unit))
    check("A-005", "psi3(HJ2*HJ3) in basis 1,J2,J3", scale(8,psi_b), (24,0,0))
    check("A-005", "psi3(HJ2)*psi3(HJ3) in basis 1,J2,J3", green_mul(scale(2,psi_a),scale(2,psi_b)), (0,-24,24))

    # A-008: over F2, I3 is isometric to [1] plus a hyperbolic plane.
    p = [[1,1,0],[1,1,1],[1,0,1]]
    pt = list(map(list,zip(*p)))
    check("A-008", "change-of-basis rank", rank(p,2), 3)
    check("A-008", "P^T I3 P", product(pt,p,2), [[1,0,0],[0,0,1],[0,1,0]])
    out = Path(__file__).with_name("ARCHIVE_COMPUTATIONS.tsv")
    with out.open("w",newline="") as f:
        w=csv.writer(f,delimiter="\t")
        w.writerow(["statement_id","check","exact_result","outcome"])
        w.writerows(events)
    print(f"{len(events)} exact checks passed; {out}")
    print("UTC:",datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
