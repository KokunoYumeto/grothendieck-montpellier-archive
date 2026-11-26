#!/usr/bin/env python3
"""Exact small-instance certificate for the elliptic p=17, r=3 route.

Run from the workbench root: python3 programs/check_elliptic_17_3.py
Writes elliptic_17_3_certificate.json beside this program.
Only Python's standard library is used. This is an exhaustive check of
one finite example, not a uniform curve-construction algorithm.
"""

import json
from pathlib import Path

P = 17
Q = P * P
NON_SQUARE = 3


def pair(x):
    return [x % P, x // P]


def add(x, y):
    a, b = pair(x)
    c, d = pair(y)
    return (a + c) % P + P * ((b + d) % P)


def neg(x):
    a, b = pair(x)
    return (-a) % P + P * ((-b) % P)


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    a, b = pair(x)
    c, d = pair(y)
    return (a * c + NON_SQUARE * b * d) % P + P * ((a * d + b * c) % P)


def power(x, n):
    y = 1
    while n:
        if n & 1:
            y = mul(y, x)
        x = mul(x, x)
        n >>= 1
    return y


def inv(x):
    assert x
    y = power(x, Q - 2)
    assert mul(x, y) == 1
    return y


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def padd(a, b):
    return trim([add(a[i] if i < len(a) else 0,
                     b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def pmul(a, b):
    c = [0] * max(0, len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = add(c[i + j], mul(x, y))
    return trim(c)


def pdivmod(a, b):
    a, b = trim(a), trim(b)
    assert b
    c = [0] * max(0, len(a) - len(b) + 1)
    b_inv = inv(b[-1])
    while len(a) >= len(b):
        d = len(a) - len(b)
        v = mul(a[-1], b_inv)
        c[d] = v
        for j, x in enumerate(b):
            a[d + j] = sub(a[d + j], mul(v, x))
        a = trim(a)
    return trim(c), a


def peval(a, x):
    y = 0
    for v in reversed(a):
        y = add(mul(y, x), v)
    return y


def main():
    assert pow(NON_SQUARE, (P - 1) // 2, P) == P - 1
    a = 1
    b = 1 + 6 * P
    discriminant_factor = add(mul(4, mul(mul(a, a), a)), mul(27 % P, mul(b, b)))
    assert discriminant_factor
    squares = {mul(x, x) for x in range(1, Q)}
    histogram = {"zero": 0, "nonzero_square": 0, "nonsquare": 0}
    row_histograms = [{"u_coefficient": j, "zero": 0, "nonzero_square": 0, "nonsquare": 0}
                      for j in range(P)]
    for x in range(Q):
        rhs = add(add(mul(mul(x, x), x), mul(a, x)), b)
        key = "zero" if rhs == 0 else "nonzero_square" if rhs in squares else "nonsquare"
        histogram[key] += 1
        row_histograms[x // P][key] += 1
    points = 1 + histogram["zero"] + 2 * histogram["nonzero_square"]
    trace = Q + 1 - points
    assert points == 259 and trace == 31
    assert trace * trace - 4 * Q == -195

    # psi_3 = 3 X^4 + 6 a X^2 + 12 b X - a^2, made monic.
    psi = [neg(mul(a, a)), mul(12, b), mul(6, a), 0, 3]
    psi = [mul(x, inv(3)) for x in psi]
    roots = [x for x in range(Q) if peval(psi, x) == 0]
    assert len(roots) == 1
    linear = [neg(roots[0]), 1]
    cubic, remainder = pdivmod(psi, linear)
    assert not remainder and len(cubic) == 4 and cubic[-1] == 1
    assert pmul(linear, cubic) == psi
    assert all(peval(cubic, x) != 0 for x in range(Q))
    # The cubic is irreducible because a reducible cubic has a root.

    # F_(17^6) = F_(17^2)[alpha]/cubic(alpha).
    zero, one = (0, 0, 0), (1, 0, 0)

    def eadd(x, y):
        return tuple(add(u, v) for u, v in zip(x, y))

    def eneg(x):
        return tuple(neg(u) for u in x)

    def emul(x, y):
        _, z = pdivmod(pmul(x, y), cubic)
        return tuple(z + [0] * (3 - len(z)))

    def epow(x, n):
        y = one
        while n:
            if n & 1:
                y = emul(y, x)
            x = emul(x, x)
            n >>= 1
        return y

    alpha = (0, 1, 0)
    candidates = [alpha, (0, P, 0), (0, 0, 1), (0, 0, P)]
    beta = None
    for z in candidates:
        v = eadd(z, epow(z, P**3))
        if epow(v, P) != v:
            beta = v
            break
    assert beta is not None
    assert epow(beta, P**3) == beta
    orbit = [beta, epow(beta, P), epow(beta, P**2)]
    assert len(set(orbit)) == 3
    # Product of the three linear Frobenius conjugate factors.
    minimal = [one]
    for v in orbit:
        new = [zero] * (len(minimal) + 1)
        for i, c in enumerate(minimal):
            new[i] = eadd(new[i], emul(c, eneg(v)))
            new[i + 1] = eadd(new[i + 1], c)
        minimal = new
    assert all(c[1:] == (0, 0) and c[0] < P for c in minimal)
    fp_minimal = [c[0] for c in minimal]
    fp_values = [sum(c * pow(x, i, P) for i, c in enumerate(fp_minimal)) % P
                 for x in range(P)]
    assert all(fp_values)
    assert fp_minimal[-1] == 1

    result = {
        "p": P,
        "r": 3,
        "field": {"order": Q, "basis": ["1", "u"], "relation": "u^2=3"},
        "curve": {"equation": "y^2=x^3+A*x+B", "A": pair(a), "B": pair(b),
                  "4A^3+27B^2": pair(discriminant_factor)},
        "point_count_histogram": histogram,
        "point_count_rows_for_x_equals_a_plus_bu": row_histograms,
        "point_count": points,
        "frobenius_trace": trace,
        "frobenius_discriminant": trace * trace - 4 * Q,
        "normalized_division_polynomial_coefficients_ascending": [pair(x) for x in psi],
        "unique_division_polynomial_root_in_base_field": pair(roots[0]),
        "linear_factor_coefficients_ascending": [pair(x) for x in linear],
        "irreducible_cubic_coefficients_ascending": [pair(x) for x in cubic],
        "cubic_has_no_base_field_roots": True,
        "degree_three_subfield_element_coefficients_in_1_alpha_alpha2": [pair(x) for x in beta],
        "degree_three_subfield_frobenius_orbit": [[pair(x) for x in v] for v in orbit],
        "irreducible_polynomial_over_F17_coefficients_ascending": fp_minimal,
        "values_at_0_through_16": fp_values,
        "scope": "Exact exhaustive certificate for one small case; no uniform search bound."
    }
    target = Path(__file__).with_name("elliptic_17_3_certificate.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"points": points, "trace": trace, "A": pair(a), "B": pair(b),
                      "division_factor_degrees": [1, 3], "F17_minimal_polynomial_ascending": fp_minimal,
                      "certificate": target.name}))


if __name__ == "__main__":
    main()
