"""Exact finite checks for the higher-three-power research note.

Run from the version root: python3 programs/verify_higher_three_power.py
This checks algebraic formulas; it does not implement CM recognition.
"""

import json
from math import gcd


def subtract(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] -= x
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c


def chebyshev(n):
    a, b = [2], [0, 1]
    if n == 0:
        return a
    for _ in range(1, n):
        a, b = b, subtract([0] + b, a)
    return b


def determinant(matrix):
    a = [row[:] for row in matrix]
    previous, sign, n = 1, 1, len(a)
    for k in range(n - 1):
        if a[k][k] == 0:
            j = next((j for j in range(k + 1, n) if a[j][k]), None)
            if j is None:
                return 0
            a[k], a[j] = a[j], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = a[i][j] * pivot - a[i][k] * a[k][j]
                assert value % previous == 0
                a[i][j] = value // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = pivot
    return sign * a[-1][-1]


def resultant(f, h):
    fd, hd = list(reversed(f)), list(reversed(h))
    m, n = len(f) - 1, len(h) - 1
    matrix = [[0] * i + fd + [0] * (n - 1 - i) for i in range(n)]
    matrix += [[0] * i + hd + [0] * (m - 1 - i) for i in range(m)]
    return determinant(matrix)


def evaluate_modulo(f, x, p):
    value = 0
    for c in reversed(f):
        value = (x * value + c) % p
    return value


def run():
    fields = []
    for b in (2, 3, 4):
        n, g = 3**b, 3 ** (b - 1)
        f = chebyshev(g)
        f[0] += 1
        derivative = [i * f[i] for i in range(1, len(f))]
        discriminant = (-1) ** (g * (g - 1) // 2) * resultant(f, derivative)
        exponent = ((2 * b - 1) * g - 1) // 2
        assert discriminant == 3**exponent
        units = [u for u in range(1, n) if gcd(u, n) == 1]
        support = {u for u in units if 2 * u < n}
        stabilizer = [v for v in units if {u * v % n for u in support} == support]
        assert stabilizer == [1]
        fields.append({
            "b": b, "g": g, "polynomial_low_to_high": f,
            "discriminant_power_of_3": exponent,
            "CM_support_stabilizer": stabilizer,
            "product_order_index_power_of_3": (g - 1) // 2,
        })
    traces = []
    for p in (17, 53, 107, 809):
        a, m = 0, p + 1
        while m % 3 == 0:
            a += 1
            m //= 3
        for b in range(2, a + 1):
            f = chebyshev(3 ** (b - 1))
            f[0] += 1
            roots = [u for u in range(p) if evaluate_modulo(f, u, p) == 0]
            assert len(roots) == 3 ** (b - 1)
            u = min(roots)
            next_roots = [x for x in range(p) if (x**3 - 3*x - u) % p == 0]
            assert len(next_roots) == (3 if b < a else 0)
            traces.append({
                "p": p, "a": a, "b": b, "least_trace_root": u,
                "next_trace_cubic_roots": next_roots,
            })
    return {"field_formula_checks": fields, "trace_lift_checks": traces}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
