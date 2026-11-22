#!/usr/bin/env python3
"""Exact algebra certificate for B-RD35, not a finite-group classification proof."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import time


def eadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def eneg(x):
    return (-x[0], -x[1])


def emul(x, y):
    # zeta^2+zeta+1=0.
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c - b * d)


def ebar(x):
    return (x[0] - x[1], -x[1])


ZERO = ((F(0), F(0)), (F(0), F(0)))
ONE = ((F(1), F(0)), (F(0), F(0)))
ZETA = ((F(0), F(1)), (F(0), F(0)))
J = ((F(0), F(0)), (F(1), F(0)))


def add(x, y):
    return (eadd(x[0], y[0]), eadd(x[1], y[1]))


def neg(x):
    return (eneg(x[0]), eneg(x[1]))


def mul(x, y):
    a, b = x
    c, d = y
    return (eadd(emul(a, c), eneg(emul(b, ebar(d)))),
            eadd(emul(a, d), emul(b, ebar(c))))


def norm(x):
    a, b = x
    result = eadd(emul(a, ebar(a)), emul(b, ebar(b)))
    assert result[1] == 0
    return result[0]


def scale(x, c):
    return tuple(tuple(t * c for t in part) for part in x)


def inv(x):
    a, b = x
    return scale((ebar(a), eneg(b)), 1 / norm(x))


def power(x, n):
    if n < 0:
        return power(inv(x), -n)
    ans = ONE
    while n:
        if n & 1:
            ans = mul(ans, x)
        x = mul(x, x)
        n //= 2
    return ans


def conjugate(g, x):
    return mul(mul(g, x), inv(g))


def vp3(q):
    assert q != 0
    n, d = abs(q.numerator), q.denominator
    value = 0
    while n % 3 == 0:
        n //= 3
        value += 1
    while d % 3 == 0:
        d //= 3
        value -= 1
    return value


PI = add(ZETA, neg(ONE))
IMAGINARY = add(ZETA, neg(inv(ZETA)))
H0 = {mul(power(ZETA, a), power(J, b)) for a in range(3) for b in range(4)}


def order(x):
    for n in range(1, 13):
        if power(x, n) == ONE:
            return n
    raise AssertionError("Element outside finite test group")


def normalize_zeta(z):
    d = add(add(z, ZETA), ONE)
    if d == ZERO:
        d = J
    assert mul(d, z) == mul(ZETA, d)
    d = mul(power(PI, -vp3(norm(d))), d)
    assert vp3(norm(d)) == 0
    assert conjugate(d, z) == ZETA
    return d


def normalize_dic12(z, t):
    first = normalize_zeta(z)
    t1 = conjugate(first, t)
    b = mul(t1, inv(J))
    assert b[1] == (0, 0)
    assert norm(b) == 1
    c = add(ONE, b) if b != neg(ONE) else IMAGINARY
    assert conjugate(inv(c), t1) == J
    second = inv(c)
    second = mul(power(PI, -vp3(norm(second))), second)
    answer = mul(second, first)
    assert vp3(norm(answer)) == 0
    assert conjugate(answer, z) in H0
    assert conjugate(answer, t) in H0
    return answer


def main():
    start = time.perf_counter()
    assert len(H0) == 12
    assert all(mul(x, y) in H0 for x in H0 for y in H0)
    assert norm(PI) == 3
    assert norm(IMAGINARY) == 3
    assert power(ZETA, 3) == ONE
    assert power(J, 2) == neg(ONE)
    assert conjugate(J, ZETA) == inv(ZETA)
    assert conjugate(PI, J) == neg(mul(ZETA, J))
    assert conjugate(IMAGINARY, J) == neg(J)
    assert {conjugate(PI, h) for h in H0} == H0
    distribution = {}
    for h in H0:
        distribution[order(h)] = distribution.get(order(h), 0) + 1
    assert distribution == {1: 1, 2: 1, 3: 2, 4: 6, 6: 2}

    conjugator_cases = 0
    for coefficients in product((-1, 0, 1), repeat=4):
        if not any(coefficients):
            continue
        g = (tuple(map(F, coefficients[:2])), tuple(map(F, coefficients[2:])))
        z, t = conjugate(g, ZETA), conjugate(g, J)
        unit = normalize_dic12(z, t)
        image = {conjugate(unit, conjugate(g, h)) for h in H0}
        assert image == H0
        conjugator_cases += 1

    result = {
        "status": "PASS",
        "quaternion_relation": "Q(zeta3)+Q(zeta3)j, j^2=-1, j*zeta=zeta^-1*j",
        "automorphism_group_order": len(H0),
        "automorphism_element_orders": distribution,
        "group_products_checked": 144,
        "exact_rational_conjugator_examples": conjugator_cases,
        "normalizer_valuation": 1,
        "scope": "Finite algebra checks of displayed identities; the proof establishes all conjugacy cases",
        "elapsed_seconds": time.perf_counter() - start,
    }
    Path(__file__).with_suffix(".output.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
