"""Original exact checks of finite-slice colon recovery and regular combinations.

No random probability estimate is inferred from these finite checks. They exercise
nilpotents, binary-degree evaluation, insufficient single slices, exact kernel
certificates, and the need to use combinations rather than a regular row sublist.
"""
from itertools import product, combinations, combinations_with_replacement
from pathlib import Path
import json


def rank(rows, p, ncols=None):
    if not rows:
        return 0
    a = [[x % p for x in row] for row in rows]
    n = ncols or len(a[0])
    r = 0
    for j in range(n):
        k = next((k for k in range(r, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        u = pow(a[r][j], -1, p)
        a[r] = [(x * u) % p for x in a[r]]
        for k in range(len(a)):
            if k != r and a[k][j]:
                u = a[k][j]
                a[k] = [(x - u * y) % p for x, y in zip(a[k], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def pmul(f, g, p):
    h = {}
    for a, u in f.items():
        for b, v in g.items():
            e = tuple(x + y for x, y in zip(a, b))
            h[e] = (h.get(e, 0) + u * v) % p
    return {e: v for e, v in h.items() if v}


def padd(f, g, p):
    h = dict(f)
    for e, v in g.items():
        h[e] = (h.get(e, 0) + v) % p
    return {e: v for e, v in h.items() if v}


def ppow(f, k, p):
    h = {(0,) * len(next(iter(f))): 1}
    while k:
        if k & 1:
            h = pmul(h, f, p)
        f = pmul(f, f, p)
        k //= 2
    return h


def value(f, x, p):
    return sum(v * prod(pow(t, a, p) for t, a in zip(x, e))
               for e, v in f.items()) % p


def prod(items):
    z = 1
    for x in items:
        z *= x
    return z


def curve_count(f, p):
    points = [(1, a, b) for a, b in product(range(p), repeat=2)]
    points += [(0, 1, a) for a in range(p)] + [(0, 0, 1)]
    return sum(value(f, x, p) == 0 for x in points)


def finite_ring(f, a, p):
    # x is the first curve variable, y=a, z=1; w^2=0.
    co = [0] * 4
    for (i, j, k), v in f.items():
        co[i] = (co[i] + v * pow(a, j, p)) % p
    inv = pow(co[3], -1, p)
    co = [(v * inv) % p for v in co]
    basis = [(w, x) for w in range(2) for x in range(3)]
    index = {e: i for i, e in enumerate(basis)}

    def mul(u, v):
        acc = {}
        for i, x in enumerate(u):
            if not x:
                continue
            for j, y in enumerate(v):
                if not y:
                    continue
                w = basis[i][0] + basis[j][0]
                if w >= 2:
                    continue
                z = basis[i][1] + basis[j][1]
                acc[w, z] = (acc.get((w, z), 0) + x * y) % p
        for z in range(4, 2, -1):
            for w in range(2):
                v = acc.pop((w, z), 0)
                for j in range(3):
                    e = w, z - 3 + j
                    acc[e] = (acc.get(e, 0) - v * co[j]) % p
        out = [0] * 6
        for e, v in acc.items():
            out[index[e]] = v % p
        return out

    one = [1, 0, 0, 0, 0, 0]
    x = [0, 1, 0, 0, 0, 0]
    w = [0, 0, 0, 1, 0, 0]
    y = [a, 0, 0, 0, 0, 0]

    def power(v, k):
        r = one
        while k:
            if k & 1:
                r = mul(r, v)
            v = mul(v, v)
            k //= 2
        return r

    return mul, power, [x, y, one, w]


def check_curve(name, p, f):
    exponent = p ** 30 + 17
    rows = []
    dimensions = []
    for a in (0, 1):
        mul, power, coordinates = finite_ring(f, a, p)
        w = coordinates[3]
        assert mul(w, w) == [0] * 6 and any(w)
        # The high-degree rows are w*x^M, w*y^M and w*z^M.
        # The two designated rows w^2 and E vanish in the quotient.
        for coordinate in coordinates[:3]:
            u = mul(w, power(coordinate, exponent))
            columns = [mul(q, u) for q in coordinates]
            rows.extend([[columns[j][i] for j in range(4)] for i in range(6)])
        dimensions.append(4 - rank(rows, p))
    assert dimensions == [2, 1]
    assert all(row[3] == 0 for row in rows)
    # Thus the final kernel is exactly span(w), not just a probabilistic guess.
    alpha = ppow(f, p - 1, p).get((p - 1,) * 3, 0)
    count = curve_count(f, p)
    assert alpha == (1 - count) % p
    # Radical point evaluation on w^2=E=0 sees w=0 and imposes no condition.
    radical_point_kernel_dimension = 4
    assert radical_point_kernel_dimension > dimensions[-1]
    return dict(name=name, prime=p, exponent_bits=exponent.bit_length(),
                fibre_algebra_dimension=6, kernel_dimensions=dimensions,
                radical_point_kernel_dimension=radical_point_kernel_dimension,
                recovered_generator="w", alpha=alpha, projective_curve_points=count)


def macaulay_rank(forms, degree, p):
    columns = []
    for f in forms:
        d = sum(next(iter(f)))
        for k in range(degree - d + 1):
            column = [0] * (degree + 1)
            for (a, b), v in f.items():
                column[a + k] = v % p
            columns.append(column)
    rows = [[column[i] for column in columns] for i in range(degree + 1)]
    return rank(rows, p)


def profile_check(p):
    g = {(2, 0): 1, (0, 2): 1}
    h = {(2, 0): 1, (0, 2): 2}
    gh = padd(g, h, p)
    rows = [pmul(g, h, p), pmul(g, gh, p), pmul(h, gh, p)]
    pair_ranks = [macaulay_rank(pair, 7, p) for pair in combinations(rows, 2)]
    chosen = [padd(rows[0], rows[1], p), padd(rows[1], rows[2], p)]
    chosen_rank = macaulay_rank(chosen, 7, p)
    assert all(r < 8 for r in pair_ranks)
    assert chosen_rank == 8
    return dict(prime=p, row_pair_ranks=pair_ranks,
                combination_rank=chosen_rank, target_rank=8,
                conclusion="No regular row pair; the two displayed combinations are regular")


def degree_two_grid_check(p):
    """A two-parameter Newton grid, with e=2 and nonreduced fibres.

    X=(w, E) in P^4, E=x^4+y^4+z^4+t^4, J=(w^3,E).
    K adds w times a huge power of every other coordinate.
    On t=1 the fibre algebra is k[w,x]/(w^3,x^4+a^4+b^4+1).
    """
    exponent = p ** 40 + 23
    basis = [(w, x) for w in range(3) for x in range(4)]
    index = {v: i for i, v in enumerate(basis)}
    monomials = list(combinations_with_replacement(range(5), 2))
    grid = [(a, b) for a in range(3) for b in range(3) if a + b <= 2]
    rows, dimensions = [], []
    for a, b in grid:
        constant = (pow(a, 4, p) + pow(b, 4, p) + 1) % p

        def mul(u, v):
            out = [0] * 12
            for i, ui in enumerate(u):
                if not ui:
                    continue
                for j, vj in enumerate(v):
                    if not vj:
                        continue
                    w = basis[i][0] + basis[j][0]
                    if w >= 3:
                        continue
                    x = basis[i][1] + basis[j][1]
                    coefficient = ui * vj
                    if x >= 4:
                        x -= 4
                        coefficient *= -constant
                    k = index[w, x]
                    out[k] = (out[k] + coefficient) % p
            return out

        one = [1] + [0] * 11

        def power(v, k):
            result = one
            while k:
                if k & 1:
                    result = mul(result, v)
                v = mul(v, v)
                k //= 2
            return result

        w = [0] * 12
        w[index[1, 0]] = 1
        x = [0] * 12
        x[index[0, 1]] = 1
        coordinates = [w, x, [a] + [0] * 11, [b] + [0] * 11, one]
        assert any(power(w, 2)) and not any(power(w, 3))
        q_columns = [mul(coordinates[i], coordinates[j]) for i, j in monomials]
        for coordinate in coordinates[1:]:
            row_value = mul(w, power(coordinate, exponent))
            columns = [mul(q, row_value) for q in q_columns]
            rows.extend([col[k] for col in columns] for k in range(12))
        dimensions.append(len(monomials) - rank(rows, p))
    w_squared = monomials.index((0, 0))
    assert all(row[w_squared] == 0 for row in rows)
    assert dimensions[-1] == 1
    points = []
    for first in range(4):
        points.extend((0,) * first + (1,) + tail
                      for tail in product(range(p), repeat=3-first))
    count = sum(sum(pow(v, 4, p) for v in point) % p == 0 for point in points)
    # In E^(p-1), all four target exponents p-1 must be multiples of 4.
    scalar = 0
    if (p-1) % 4 == 0:
        from math import factorial
        scalar = factorial(p-1) // factorial((p-1)//4)**4 % p
    assert count % p == (1 + scalar) % p
    return {"prime": p, "excess": 2, "fibre_dimension": 12,
            "grid": grid, "successive_kernel_dimensions": dimensions,
            "kernel_generator": "w^2", "input_exponent_bits": exponent.bit_length(),
            "quartic_surface_points": count, "coherent_scalar": scalar}


def main():
    cases = [
        ("ordinary", 2, {(0, 2, 1): 1, (1, 1, 1): 1, (3, 0, 0): 1, (0, 0, 3): 1}),
        ("supersingular", 2, {(0, 2, 1): 1, (0, 1, 2): 1, (3, 0, 0): 1}),
        ("ordinary", 3, {(0, 2, 1): 1, (3, 0, 0): -1, (2, 0, 1): -1, (0, 0, 3): -1}),
        ("supersingular", 3, {(0, 2, 1): 1, (3, 0, 0): -1, (1, 0, 2): -1}),
        ("ordinary", 5, {(0, 2, 1): 1, (3, 0, 0): -1, (1, 0, 2): -1, (0, 0, 3): -1}),
        ("supersingular", 5, {(0, 2, 1): 1, (3, 0, 0): -1, (0, 0, 3): -1}),
    ]
    result = {"finite_slices": [check_curve(*c) for c in cases],
              "degree_profiles": [profile_check(p) for p in (5, 7, 11)],
              "deterministic_degree_two_grid": [degree_two_grid_check(p) for p in (3, 5, 7)],
              "scope": "Exact finite examples; no empirical certification of asymptotic probability bounds"}
    out = Path(__file__).resolve().parents[1] / "certificates/sliced_colon_results.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
