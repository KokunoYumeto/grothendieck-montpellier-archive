#!/usr/bin/env python3
"""Exploratory exact A27 rational character test over F256 at conductor13.

Uses a separately written characteristic-two Mumford divisor arithmetic
implementation and the finite field/polynomial utilities of the theta probe.
Every composition/reduction checks the Mumford divisibility identity. This
producer is not an independent verification certificate or formal proof.
"""
from pathlib import Path
import hashlib
import json
import probe_A27_theta13 as F

add, mul, pmul, peval, trim = F.add, F.mul, F.pmul, F.peval, F.trim
inv = lambda a: F.INVERSES[a]
U = min(a for a in range(256) if mul(a, a) ^ a ^ 1 == 0)
H = [0, 0, 1]
f = [0, U, 0, 1, 0, U]
ZERO = ((1,), ())


def scale(a, c):
    return trim([mul(x, c) for x in a])


def divmodp(a, b):
    a, b = trim(a), trim(b)
    assert b
    out = [0] * max(0, len(a) - len(b) + 1)
    bi = inv(b[-1])
    while a and len(a) >= len(b):
        i = len(a) - len(b)
        c = mul(a[-1], bi)
        out[i] = c
        a = add(a, [0]*i + scale(b, c))
    return trim(out), a


def rem(a, b):
    return divmodp(a, b)[1]


def quotient(a, b):
    q, r = divmodp(a, b)
    assert not r
    return q


def xgcd(a, b):
    a, b = trim(a), trim(b)
    s0, s1, t0, t1 = [1], [], [], [1]
    while b:
        q, r = divmodp(a, b)
        a, b = b, r
        s0, s1 = s1, add(s0, pmul(q, s1))
        t0, t1 = t1, add(t0, pmul(q, t1))
    c = inv(a[-1])
    return scale(a, c), scale(s0, c), scale(t0, c)


def check(u, v):
    assert u and u[-1] == 1 and len(v) < len(u)
    assert not rem(add(add(pmul(v, v), pmul(H, v)), f), u)


def compose(d1, d2):
    u1, v1 = map(list, d1)
    u2, v2 = map(list, d2)
    check(u1, v1)
    check(u2, v2)
    d0, e1, e2 = xgcd(u1, u2)
    d, c1, c2 = xgcd(d0, add(add(v1, v2), H))
    s1, s2, s3 = pmul(c1, e1), pmul(c1, e2), c2
    u = quotient(pmul(u1, u2), pmul(d, d))
    numerator = add(add(pmul(pmul(s1, u1), v2),
                        pmul(pmul(s2, u2), v1)),
                    pmul(s3, add(pmul(v1, v2), f)))
    v = rem(quotient(numerator, d), u)
    check(u, v)
    while len(u) > 3:
        u = quotient(add(add(pmul(v, v), pmul(H, v)), f), u)
        u = scale(u, inv(u[-1]))
        v = rem(add(H, v), u)
        check(u, v)
    return tuple(u), tuple(v)


def multiple(d, n):
    out = ZERO
    while n:
        if n & 1:
            out = compose(out, d)
        n >>= 1
        if n:
            d = compose(d, d)
    return out


def negate(d):
    return d[0], tuple(rem(add(d[1], H), d[0]))


def main():
    points = [(x, y) for x in range(256) for y in range(256)
              if mul(y, y) ^ mul(mul(x, x), y) ^ peval(f, x) == 0]
    divisors = [ZERO] + [((x, 1), (y,) if y else ()) for x, y in points]
    assert len(divisors) == 256
    for d in divisors:
        assert compose(d, ZERO) == d
        assert compose(d, negate(d)) == ZERO
        assert multiple(d, 65520) == ZERO
    projected = [multiple(d, 5040) for d in divisors]
    generator = next(d for d in projected if d != ZERO)
    assert multiple(generator, 13) == ZERO
    table = {multiple(generator, i): i for i in range(13)}
    assert len(table) == 13 and all(d in table for d in projected)
    counts = [0] * 13
    for d in projected:
        counts[table[d]] += 1
    coeff = [c & 1 for c in counts]
    coeff[0] ^= 1
    # Phi13 is irreducible in F2[X], so a degree<=12 polynomial vanishes
    # at a primitive13 root iff it is zero or Phi13. Augmentation is one,
    # excluding zero. This checks the exact B.2 character test at W.
    is_unit = len(set(coeff)) != 1
    assert sum(coeff) % 2 == 1
    # Deterministic associativity controls involving generic/divisible cases.
    for i in range(0, len(divisors), 7):
        a, b, c = divisors[i], divisors[(i+31) % 256], divisors[(i+79) % 256]
        assert compose(compose(a, b), c) == compose(a, compose(b, c))
    result = {
        'curve': 'Y^2+X^2Y=uX^5+X^3+uX, u^2+u+1=0',
        'field': {'size': 256, 'modulus': F.MOD, 'u': U},
        'base_point': 'W=infinity', 'conductor': 13,
        'Jacobian_order': 65520, 'projection_multiplier': 5040,
        'cyclic_generator_Mumford': generator,
        'point_image_counts': counts,
        'B2_F2_group_ring_coefficients': coeff,
        'B2_all_primitive_characters_nonzero': is_unit,
        'all_point_differences_killed_by_claimed_J_order': True,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Exact exploratory producer; positive cover inference needs whole-check of divisor arithmetic or an independent certificate before promotion.',
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
