#!/usr/bin/env python3
"""Separate extended-GCD Cantor certificate for the twisted A27 degree39 cover.

Uses the retained Cantor implementation, not the effective agent's linear
interpolation arithmetic. Enumerates every point and derives every quotient
label afresh. Expected constants are assertions, not imported point data.
This is exact finite computation, not a formal proof assistant certificate.
"""
from pathlib import Path
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent
ARITHMETIC = HERE / 'verify_A36_conductor5_cantor.py'
spec = importlib.util.spec_from_file_location('separate_cantor', ARITHMETIC)
ar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ar)


def imul(a, b):
    c = [0] * max(0, len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    while c and c[-1] == 0:
        c.pop()
    return c


def idiv(a, b):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    q = [0] * max(0, len(a) - len(b) + 1)
    assert b[-1] == 1
    while len(a) >= len(b):
        k = len(a) - len(b)
        c = a[-1]
        q[k] = c
        for j, bj in enumerate(b):
            a[k + j] -= c * bj
        while a and a[-1] == 0:
            a.pop()
    while q and not q[-1]:
        q.pop()
    return q, a


def cyclotomic(n):
    product = [1]
    for d in range(1, n):
        if n % d == 0:
            product = imul(product, cyclotomic(d))
    polynomial = [-1] + [0] * (n - 1) + [1]
    quotient, remainder = idiv(polynomial, product)
    assert remainder == []
    return quotient


def bmul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
    return out


def bdiv(a, b):
    assert b
    quotient = 0
    while a and a.bit_length() >= b.bit_length():
        j = a.bit_length() - b.bit_length()
        quotient ^= 1 << j
        a ^= b << j
    return quotient, a


def bxgcd(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b:
        q, r = bdiv(a, b)
        a, b = b, r
        s0, s1 = s1, s0 ^ bmul(q, s1)
        t0, t1 = t1, t0 ^ bmul(q, t1)
    return a, s0, t0


def binary(poly):
    return sum((a % 2) << i for i, a in enumerate(poly))


def l_value(counts, n, q):
    a = list(counts)
    a[0] += 1 + q
    phi = cyclotomic(n)
    _, remainder = idiv(a, phi)
    return remainder + [0] * (len(phi) - 1 - len(remainder))


def frob4_divisor(d):
    return tuple(tuple(ar.power(a, 4) for a in poly) for poly in d)


def main():
    assert ar.Q == 256 and ar.MOD == 0x11B and ar.U == 188
    points = [(x, y) for x in range(256) for y in range(256)
              if ar.mul(y, y) ^ ar.mul(ar.mul(x, x), y) ^ ar.peval(ar.f, x) == 0]
    point_list = [None] + [list(p) for p in points]
    divisors = [ar.ZERO] + [((x, 1), (y,) if y else ()) for x, y in points]
    assert len(divisors) == 256

    sums = []
    for trace in (1, -2):
        previous, current = 2, trace
        for _ in range(2, 5):
            previous, current = current, trace * current - 4 * previous
        sums.append(current)
    jacobian_order = (257 - sums[0]) * (257 - sums[1])
    assert sums == [17, -16] and jacobian_order == 65520
    assert 257 - sum(sums) == len(divisors)
    assert jacobian_order // 9 == 7280 and jacobian_order % 27
    assert jacobian_order // 13 == 5040 and jacobian_order % 169

    projected9 = []
    projected13 = []
    for index, d in enumerate(divisors):
        ar.check(*d)
        assert ar.compose(d, ar.negate(d)) == ar.ZERO
        assert ar.multiple(d, jacobian_order) == ar.ZERO
        projected9.append(ar.multiple(d, 7280))
        projected13.append(ar.multiple(d, 5040))
        if index % 64 == 0:
            print('completed Cantor projections', index, flush=True)

    generator9 = next(d for d in projected9 if ar.multiple(d, 3) != ar.ZERO)
    generator13 = next(d for d in projected13 if d != ar.ZERO)
    cycle9 = [ar.multiple(generator9, j) for j in range(9)]
    cycle13 = [ar.multiple(generator13, j) for j in range(13)]
    assert len(set(cycle9)) == 9 and ar.multiple(generator9, 9) == ar.ZERO
    assert len(set(cycle13)) == 13 and ar.multiple(generator13, 13) == ar.ZERO
    labels9 = {d: j for j, d in enumerate(cycle9)}
    labels13 = {d: j for j, d in enumerate(cycle13)}
    assert generator9 == ((189, 0, 1), (80, 189))
    assert generator13 == ((237, 80, 1), (207, 106))
    assert frob4_divisor(generator9) == cycle9[8]
    assert frob4_divisor(generator13) == cycle13[5]
    assert ar.negate(frob4_divisor(generator9)) == cycle9[1]
    assert ar.negate(frob4_divisor(generator13)) == cycle13[8]

    twist_root = next(a for a in range(256) if ar.mul(a, a) ^ a == ar.U)
    assert twist_root == 92 and ar.power(twist_root, 4) ^ twist_root == 1
    twist_f = [0, ar.U, 0, 1, ar.U, ar.U]
    counts39 = [0] * 39
    counts13 = [0] * 13
    counts3 = [0] * 3
    counts3_F4 = [0] * 3
    images = []
    points_F4 = []
    for point, d9, d13 in zip(point_list, projected9, projected13):
        a9, a13 = labels9[d9], labels13[d13]
        a3 = a9 % 3
        a39 = next(j for j in range(39) if j % 3 == a3 and j % 13 == a13)
        counts39[a39] += 1
        counts13[a13] += 1
        counts3[a3] += 1
        if point is None:
            twist_point = None
            rational_F4 = True
        else:
            x, y = point
            yt = y ^ ar.mul(twist_root, ar.mul(x, x))
            assert ar.mul(yt, yt) ^ ar.mul(ar.mul(x, x), yt) ^ ar.peval(twist_f, x) == 0
            twist_point = [x, yt]
            rational_F4 = ar.power(x, 4) == x and ar.power(yt, 4) == yt
        if rational_F4:
            counts3_F4[a3] += 1
            points_F4.append({'point': twist_point, 'original_point': point,
                              'a3': a3})
        images.append({'original_point': point, 'twist_point': twist_point,
                       'projected9_Mumford': d9, 'a9': a9,
                       'projected13_Mumford': d13, 'a13': a13,
                       'a3': a3, 'a39': a39})

    # Check the actual Frobenius permutation of every twisted rational point.
    lookup = {None if row['twist_point'] is None else tuple(row['twist_point']): row
              for row in images}
    for row in images:
        point = row['twist_point']
        next_point = None if point is None else tuple(ar.power(c, 4) for c in point)
        image = lookup[next_point]
        assert image['a39'] == 34 * row['a39'] % 39
        assert image['a3'] == row['a3']
        assert image['a13'] == 8 * row['a13'] % 13
    assert pow(34, 4, 39) == 1 and all(pow(34, j, 39) != 1 for j in (1, 2))
    assert len(points_F4) == 4 and counts3_F4 == [2, 1, 1]
    assert counts3 == [74, 91, 91]
    expected39 = [14, 7, 6, 6, 6, 7, 4, 6, 7, 4, 6, 6, 5, 15, 7, 6, 6, 6, 5,
                  6, 6, 5, 6, 6, 6, 7, 15, 5, 6, 6, 4, 7, 6, 4, 7, 6, 6, 6, 7]
    assert counts39 == expected39

    L3_F4, L3_F256 = l_value(counts3_F4, 3, 4), l_value(counts3, 3, 256)
    L13, L39 = l_value(counts13, 13, 256), l_value(counts39, 39, 256)
    assert L3_F4 == [6, 0] and L3_F256 == [240, 0]
    assert all(c % 2 == 0 for c in L39)
    phi13, phi39 = cyclotomic(13), cyclotomic(39)
    phi13b, phi39b = binary(phi13), binary(phi39)
    gcd13, left13, right13 = bxgcd(binary(L13), phi13b)
    half39 = [c // 2 for c in L39]
    gcd39, left39, right39 = bxgcd(binary(half39), phi39b)
    assert gcd13 == gcd39 == 1
    assert bmul(binary(L13), left13) ^ bmul(phi13b, right13) == 1
    assert bmul(binary(half39), left39) ^ bmul(phi39b, right39) == 1
    c39 = list(counts39)
    _, c39_reduced = idiv(c39, phi39)
    assert binary(c39_reduced) == 1
    assert L39 == [256, 2, 0, 0, 2, 0, -2, 2, 0, -2, 0, 0,
                   -2, 0, 2, 0, 0, 2, -2, 0, 2, -2, 0, 0]
    assert 39 > (2 * 2 - 1) ** 2 and not 39 > (2 * 16 - 1) ** 2

    result = {'status': 'PASS',
              'scope': 'Independent Cantor computation of all point images and exact cyclotomic identities; group-exponent interpretation is proved in A45_STRICT_39.tex, not formal verification.',
              'field': {'size': 256, 'modulus': ar.MOD, 'u': ar.U,
                        'encoding': 'binary polynomial coefficients, low degrees first'},
              'twist_curve': 'Y^2+X^2Y=uX^5+uX^4+X^3+uX',
              'twist_root': twist_root, 'point_count_F256': len(divisors),
              'Jacobian_order_F256': jacobian_order,
              'generator9': generator9, 'generator9_cycle': cycle9,
              'generator13': generator13, 'generator13_cycle': cycle13,
              'original_Frobenius4_on_generators': [8, 5],
              'twist_Frobenius4_on_generators': [1, 8],
              'twist_deck_exponent_mod39': 34, 'deck_constant_degree': 4,
              'twist_F4_points': points_F4, 'all_point_images': images,
              'counts39': counts39, 'counts13': counts13, 'counts3_F256': counts3,
              'counts3_F4': counts3_F4, 'L3_F4': L3_F4, 'L3_F256': L3_F256,
              'L13': L13, 'L39': L39, 'Phi13': phi13, 'Phi39': phi39,
              'L13_mod2_Bezout': [left13, right13],
              'L39_half_mod2_Bezout': [left39, right39],
              'L39_half_mod2_binary': binary(half39), 'Phi39_binary': phi39b,
              'faithful39_c1_mod2': 1,
              'Cantor_source_sha256': hashlib.sha256(ARITHMETIC.read_bytes()).hexdigest(),
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: result[k] for k in ('status', 'field', 'point_count_F256',
                      'Jacobian_order_F256', 'generator9', 'generator13', 'counts39',
                      'counts3_F4', 'L3_F4', 'L3_F256', 'L39', 'L39_half_mod2_Bezout',
                      'source_sha256')}, indent=2))


if __name__ == '__main__':
    main()
