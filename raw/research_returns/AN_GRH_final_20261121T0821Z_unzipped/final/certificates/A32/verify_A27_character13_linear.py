#!/usr/bin/env python3
"""Second exact implementation of the A27 conductor13 character calculation.

No imports from the producer or its field/polynomial library. Addition is
computed by cancelling opposite support and solving the remaining root
interpolation as an F2-linear system, rather than the producer's extended-
GCD Cantor composition formula. Norm reduction then supplies the reduced
Mumford representative. This is an exact computation, not formal verification.
"""
from pathlib import Path
import hashlib
import json


def field_product(a, b):
    p = 0
    for i in range(8):
        if (b >> i) & 1:
            p ^= a << i
    for j in range(14, 7, -1):
        if (p >> j) & 1:
            p ^= 0x11b << (j-8)
    return p


M = [[field_product(a, b) for b in range(256)] for a in range(256)]
I = [0] + [next(b for b in range(1, 256) if M[a][b] == 1) for a in range(1, 256)]
assert all(M[a][I[a]] == 1 for a in range(1, 256))


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def plus(a, b):
    out = list(a) + [0]*max(0, len(b)-len(a))
    for i, c in enumerate(b):
        out[i] ^= c
    return trim(out)


def times(a, b):
    out = [0]*max(0, len(a)+len(b)-1)
    for i, c in enumerate(a):
        for j, d in enumerate(b):
            out[i+j] ^= M[c][d]
    return trim(out)


def squared(a):
    out = [0]*max(0, 2*len(a)-1)
    for i, c in enumerate(a):
        out[2*i] = M[c][c]
    return trim(out)


def division(a, b):
    a, b = trim(a), trim(b)
    assert b
    out = [0]*max(0, len(a)-len(b)+1)
    while a and len(a) >= len(b):
        k = len(a)-len(b)
        c = M[a[-1]][I[b[-1]]]
        out[k] = c
        for j, d in enumerate(b):
            a[k+j] ^= M[c][d]
        a = trim(a)
    return trim(out), a


def exact(a, b):
    q, r = division(a, b)
    assert not r
    return q


def mod(a, b):
    return division(a, b)[1]


def monic(a):
    assert a
    return [M[c][I[a[-1]]] for c in a]


def gcd(a, b):
    while b:
        a, b = b, mod(a, b)
    return monic(a)


def evalp(a, x):
    z = 0
    for c in reversed(a):
        z = M[z][x] ^ c
    return z


u = next(a for a in range(2, 256) if M[a][a] ^ a ^ 1 == 0)
h = [0, 0, 1]
f = [0, u, 0, 1, 0, u]
IDENTITY = ((1,), ())


def verify(D):
    a, b = D
    assert a[-1] == 1 and len(b) < len(a)
    assert not mod(plus(plus(squared(b), times(h, b)), f), a)


def encode(a):
    return sum(c << (8*i) for i, c in enumerate(a))


def decode(a, degree):
    return trim([(a >> (8*i)) & 255 for i in range(degree)])


def solve_columns(columns, rhs):
    basis = {}
    for j, column in enumerate(columns):
        combination = 1 << j
        while column:
            k = column.bit_length()-1
            if k not in basis:
                basis[k] = (column, combination)
                break
            old, mask = basis[k]
            column ^= old
            combination ^= mask
        assert column, 'the constrained interpolation should be unique'
    answer = 0
    while rhs:
        k = rhs.bit_length()-1
        assert k in basis, 'the interpolation should have a solution'
        column, mask = basis[k]
        rhs ^= column
        answer ^= mask
    return answer


def interpolate(a1, b1, a2, b2):
    a = times(a1, a2)
    degree, d1, d2 = len(a)-1, len(a1)-1, len(a2)-1
    if degree == 0:
        return a, []
    # Solve v^2+h*v=f modulo a, v=b1 modulo a1, v=b2 modulo a2.
    # Squaring is F2-linear, so the whole system is a binary linear system.
    def image(v):
        return (encode(mod(plus(squared(v), times(h, v)), a)) |
                (encode(mod(v, a1)) << (8*degree)) |
                (encode(mod(v, a2)) << (8*(degree+d1))))
    rhs = (encode(mod(f, a)) |
           (encode(b1) << (8*degree)) |
           (encode(b2) << (8*(degree+d1))))
    columns = [image(decode(1 << j, degree)) for j in range(8*degree)]
    answer = solve_columns(columns, rhs)
    v = decode(answer, degree)
    assert image(v) == rhs
    return a, v


def add_divisors(D1, D2):
    verify(D1)
    verify(D2)
    a1, b1 = map(list, D1)
    a2, b2 = map(list, D2)
    # Common opposite points cancel by the principal x-polynomial divisor.
    cancel = gcd(gcd(a1, a2), plus(plus(b1, b2), h))
    a1, a2 = exact(a1, cancel), exact(a2, cancel)
    b1, b2 = mod(b1, a1), mod(b2, a2)
    a, b = interpolate(a1, b1, a2, b2)
    verify((a, b))
    while len(a) > 3:
        # div(Y+b) gives the complementary support; conjugation changes its sign.
        a = monic(exact(plus(plus(squared(b), times(h, b)), f), a))
        b = mod(plus(b, h), a)
        verify((a, b))
    return tuple(a), tuple(b)


def scalar(D, n):
    # Left-to-right multiplication differs from the producer's right-to-left chain.
    out = IDENTITY
    for bit in bin(n)[2:]:
        out = add_divisors(out, out)
        if bit == '1':
            out = add_divisors(out, D)
    return out


def f2degree(a):
    return a.bit_length()-1


def f2div(a, b):
    q = 0
    while a and f2degree(a) >= f2degree(b):
        j = f2degree(a)-f2degree(b)
        q ^= 1 << j
        a ^= b << j
    return q, a


def f2product(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out


def f2bezout(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b:
        q, r = f2div(a, b)
        a, b = b, r
        s0, s1 = s1, s0 ^ f2product(q, s1)
        t0, t1 = t1, t0 ^ f2product(q, t1)
    return a, s0, t0


def residue_product(a, b, modulus):
    return f2div(f2product(a, b), modulus)[1]


def residue_power(a, n, modulus):
    out = 1
    while n:
        if n & 1:
            out = residue_product(out, a, modulus)
        a = residue_product(a, a, modulus)
        n >>= 1
    return out


def main():
    points = []
    for x in range(256):
        for y in range(256):
            if M[y][y] ^ M[M[x][x]][y] == evalp(f, x):
                points.append((x, y))
    assert len(points)+1 == 256
    divisors = [IDENTITY] + [((x, 1), (y,) if y else ()) for x, y in points]
    projected = [scalar(D, 5040) for D in divisors]
    generator = next(D for D in projected if D != IDENTITY)
    cycle = [IDENTITY]
    for _ in range(12):
        cycle.append(add_divisors(cycle[-1], generator))
    assert len(set(cycle)) == 13 and add_divisors(cycle[-1], generator) == IDENTITY
    lookup = {D: i for i, D in enumerate(cycle)}
    assert all(D in lookup for D in projected)
    counts = [0]*13
    for D in projected:
        counts[lookup[D]] += 1
    coeff = [c & 1 for c in counts]
    coeff[0] ^= 1
    assert [pow(2, i, 13) for i in range(12)] == [1, 2, 4, 8, 3, 6, 12, 11, 9, 5, 10, 7]
    polynomial = sum(c << i for i, c in enumerate(coeff))
    cyclotomic = (1 << 13)-1
    gcd_value, bezout_a, bezout_b = f2bezout(polynomial, cyclotomic)
    assert gcd_value == 1
    assert f2product(polynomial, bezout_a) ^ f2product(cyclotomic, bezout_b) == 1
    beta = f2div(polynomial ^ 1, cyclotomic)[1]
    assert beta not in (0, 1)
    assert residue_power(beta, 8, cyclotomic) == beta
    beta_powers = [residue_power(beta, i, cyclotomic) for i in range(1, 8)]
    assert beta_powers[-1] == 1 and all(x != 1 for x in beta_powers[:-1])
    faithful_values = []
    norm_coefficients = [1]
    for i in range(1, 13):
        s = 0
        for j in (1, 5, 8, 12):
            s ^= 1 << ((i*j) % 13)
        s = f2div(s, cyclotomic)[1]
        faithful_values.append(s)
        assert s not in (0, 1) and residue_power(s, 7, cyclotomic) == 1
        out = norm_coefficients + [0]
        for j, c in enumerate(norm_coefficients):
            out[j+1] ^= residue_product(c, s, cyclotomic)
        norm_coefficients = out
    assert all(c in (0, 1) for c in norm_coefficients)
    assert len(set(faithful_values)) == 3
    records = [{'point': None, 'image_in_Z13': lookup[projected[0]],
                'projected_Mumford': projected[0]}]
    records += [{'point': list(point), 'image_in_Z13': lookup[D],
                 'projected_Mumford': D} for point, D in zip(points, projected[1:])]
    point_output = Path(__file__).with_name('A32_ALL_POINT_IMAGES.json')
    point_output.write_text(json.dumps(records, indent=2)+'\n')
    result = {
        'field_modulus': 0x11b, 'u': u,
        'method': 'independent binary-linear root interpolation; opposite-support cancellation; norm reduction; left-to-right scalar chain',
        'rational_points': 256,
        'Jacobian_order_input_from_A27': 65520,
        'projection_multiplier': 5040,
        'cyclic_generator_Mumford': generator,
        'point_image_counts': counts,
        'B2_F2_group_ring_coefficients': coeff,
        'B2_polynomial_binary': polynomial,
        'Phi13_binary': cyclotomic,
        'F2_Bezout_coefficients_binary': [bezout_a, bezout_b],
        'B2_all_primitive_characters_nonzero': True,
        'beta_residue_binary': beta,
        'beta_powers_1_through_7_binary': beta_powers,
        'faithful_S_values_binary': faithful_values,
        'reduced_Prym_L_polynomial_coefficients_ascending': norm_coefficients,
        'beta_exact_order': 7,
        'constant_extension_relative_class_number_odd_iff': 'extension degree is not divisible by7',
        'all_point_images_file': point_output.name,
        'all_point_images_sha256': hashlib.sha256(point_output.read_bytes()).hexdigest(),
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Exact second-implementation check; written mathematical interpretation and whole proof reading are still required before theorem promotion.',
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
