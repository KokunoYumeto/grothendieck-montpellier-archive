#!/usr/bin/env python3
"""Compact exact certificate for the root-discovered A31 norm7 witness.

All arithmetic is in F4 = F2[u]/(u^2+u+1), encoded 0,1,u,u+1 as
0,1,2,3. Polynomial and Laurent identities are checked without a
Jacobian package, external algebra system, or the exploratory Cantor code.
The geometric divisor/theta consequences are proved in the companion TeX.
"""
from pathlib import Path
import hashlib
import json


def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return out


def power(a, n):
    out = 1
    for _ in range(n):
        out = mul(out, a)
    return out


def trim(p):
    p = list(p)
    while p and not p[-1]:
        p.pop()
    return p


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) ^
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def product(a, b):
    out = [0]*max(0, len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] ^= mul(x, y)
    return trim(out)


def ppow(a, n):
    out = [1]
    for _ in range(n):
        out = product(out, a)
    return out


def value(a, x):
    out = 0
    for c in reversed(a):
        out = mul(out, x) ^ c
    return out


def ladd(a, b):
    out = dict(a)
    for e, c in b.items():
        out[e] = out.get(e, 0) ^ c
    return {e: c for e, c in out.items() if c}


def lmul(a, b):
    out = {}
    for e, c in a.items():
        for f, d in b.items():
            out[e+f] = out.get(e+f, 0) ^ mul(c, d)
    return {e: c for e, c in out.items() if c}


def main():
    u, u2 = 2, 3
    assert mul(u, u) == u2 and u2 ^ u ^ 1 == 0
    assert all(power(a, 3) == 1 for a in (1, u, u2))
    h = [0, 0, 1]
    f = [u, u, u2, u, 1, 1]
    a, b = [0, 1], [u, 1]
    norm = add(add(product(a, a), product(product(a, b), h)),
               product(product(b, b), f))
    target = ppow([1, 1], 7)
    assert norm == target == [1]*8
    r = (1, u)
    rbar = (1, u2)
    assert mul(r[1], r[1]) ^ mul(value(h, r[0]), r[1]) ^ value(f, r[0]) == 0
    assert value(a, r[0]) ^ mul(value(b, r[0]), r[1]) == 0
    assert value(a, rbar[0]) ^ mul(value(b, rbar[0]), rbar[1]) == u2
    # The only possible affine singular X-coordinate is0; f'(0)=u.
    derivative = trim([f[i+1] if (i+1) % 2 else 0 for i in range(len(f)-1)])
    assert value(derivative, 0) == u
    # X=u/t and Y=alpha*y+beta, alpha=u^2/t^2, beta=1/t^2+u^2.
    x = {-1: u}
    alpha, beta = {-2: u2}, {-2: 1, 0: u2}
    x2, alpha2 = lmul(x, x), lmul(alpha, alpha)
    assert lmul(x2, alpha) == alpha2
    g = {3: u, 1: 1, -1: u}
    lhs = ladd(ladd(lmul(alpha2, g), lmul(beta, beta)), lmul(x2, beta))
    rhs = {}
    xp = {0: 1}
    for c in f:
        rhs = ladd(rhs, {e: mul(c, d) for e, d in xp.items() if mul(c, d)})
        xp = lmul(xp, x)
    assert lhs == rhs
    # At (t,y)=(u,u^2), the displayed map gives R=(1,u).
    tinv = u2
    xr = mul(u, tinv)
    yr = mul(mul(u2, mul(tinv, tinv)), u2 ^ u) ^ u2
    assert (xr, yr) == r
    # Two substitutions check the rational inverse y=u+(Y+u^2)/X^2.
    # y recovered = u + (alpha*y+beta+u^2)/X^2.
    assert alpha == x2
    assert ladd(beta, {0: u2}) == lmul(x2, {0: u})
    signed = sorted({pow(2, j, 7) for j in range(3)} |
                    {(-pow(2, j, 7)) % 7 for j in range(3)})
    assert signed == list(range(1, 7))
    result = {
        'field': 'F2[u]/(u^2+u+1); 0,1,u,u+1 encoded0,1,2,3',
        'curve': 'Y^2+X^2Y=X^5+X^4+uX^3+u^2X^2+uX+u',
        'f_coefficients_ascending': f,
        'function': '(X+u)Y+X',
        'norm_coefficients_ascending': norm,
        'norm_target': '(X+1)^7',
        'R': list(r), 'conjugate_R': list(rbar),
        'F_at_R': 0, 'F_at_conjugate_R': u2,
        'f_prime_at_zero': u,
        'isomorphism_source': 'y^2+y=u*t^3+t+u/t',
        'isomorphism': ['X=u/t', 'Y=u^2*t^(-2)*(y+u)+u^2'],
        'inverse': ['t=u/X', 'y=u+(Y+u^2)/X^2'],
        'verified_Laurent_identity': {str(e): lhs[e] for e in sorted(lhs)},
        'point_on_source': [u, u2],
        'source_point_mapped_to_R': [xr, yr],
        'powers_of_two_mod7': [1, 2, 4],
        'signed_generated_units_mod7': signed,
        'pole_orders_at_infinity': {'X': 2, 'Y': 5, '(X+u)Y+X': 7},
        'geometric_conclusion_requires_written_proof': 'div(F)=7(R-W); exact7 theta point after Frobenius twist; A11 yields the geometric primitive-rank-zero witness',
        'credit': 'Explicit norm7 model and isomorphism discovered by /root; this verifier and companion proof checked independently by /root/row_audit.',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
