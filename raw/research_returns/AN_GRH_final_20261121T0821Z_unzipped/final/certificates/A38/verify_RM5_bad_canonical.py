#!/usr/bin/env python3
"""Exact arithmetic for the A13 ordinary-RM5 canonical-detector obstruction.

The canonical orders follow from the accompanying divisor argument;
this script does not pretend to compute Jacobian divisors directly.
"""
from pathlib import Path
from math import isqrt
import hashlib
import json

MODULUS = 0x83  # a^7+a+1


def mul(x, y):
    out = 0
    while y:
        if y & 1:
            out ^= x
        y >>= 1
        x <<= 1
        if x & 128:
            x ^= MODULUS
    return out


def power(x, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, x)
        x = mul(x, x)
        n >>= 1
    return out


inverses = {x: power(x, 126) for x in range(1, 128)}
assert all(mul(x, inverses[x]) == 1 for x in range(1, 128))
points = []
for x in range(2, 128):
    rhs = x ^ inverses[x] ^ inverses[x ^ 1]
    for y in range(128):
        if mul(y, y) ^ y == rhs:
            points.append([x, y])
assert len(points) == 126
assert points[0][0] not in (0, 1)

# Frobenius P2=X^4-X^2+4, whose squared roots satisfy t^2-t+4.
trace = [2, 1]
for j in range(2, 8):
    trace.append(trace[-1] - 4*trace[-2])
jacobian_order = 4**7 + 1 - trace[7]
assert jacobian_order == 16636 == 4*4159
assert all(4159 % d for d in range(2, isqrt(4159)+1))
order = 2079
assert order == 3**3 * 7 * 11
assert pow(2, order, 4159) == 1
residues = {d: pow(2, d, 4159) for d in [2079, 693, 297, 189]}
assert all(residues[d] != 1 for d in [693, 297, 189])
output = {
    'curve': 'y^2+y=x+1/x+1/(x+1) over F2',
    'F128_modulus': MODULUS,
    'encoding': 'binary coefficients in increasing powers of a',
    'all_127_nonzero_inverses_checked': True,
    'branch_points': ['0', '1', 'infinity'],
    'all_non_Weierstrass_F128_points': points,
    'non_Weierstrass_count': len(points),
    'total_point_count': len(points)+3,
    'first_explicit_point': points[0],
    'squared_Frobenius_trace_sequence': trace,
    'Jacobian_order': jacobian_order,
    'prime_4159_trial_divisors_through': isqrt(4159),
    'order_two_mod_4159': order,
    'order_certificate_residues': residues,
    'scope': 'Exact point and finite arithmetic check. Canonical exact-order and integral RM5 conclusions require the written proof and prior checked A13 inputs. No formal verification claim.',
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix('.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps({key:output[key] for key in ['total_point_count',
    'non_Weierstrass_count', 'first_explicit_point', 'Jacobian_order',
    'order_two_mod_4159', 'order_certificate_residues']}))
