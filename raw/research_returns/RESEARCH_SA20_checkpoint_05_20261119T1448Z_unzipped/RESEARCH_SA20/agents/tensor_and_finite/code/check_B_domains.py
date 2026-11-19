#!/usr/bin/env python3
"""Exact polynomial checks for B.016; no floating point or symbolic dependencies."""
from itertools import product


def trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p, sign=1):
    return trim([(a[i] if i < len(a) else 0) + sign * (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))], p)


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                c[i+j] += ai * bj
    return trim(c, p)


def power(a, n, p):
    r = [1]
    while n:
        if n & 1:
            r = mul(r, a, p)
        a = mul(a, a, p)
        n >>= 1
    return r


def frobenius(a, q, p):
    # q is a power of p, so coefficients in the prime field are fixed.
    c = [0] * ((len(a)-1)*q + 1)
    for i, ai in enumerate(a):
        c[i*q] = ai
    return trim(c, p)


def valuation(a, root, p):
    a = trim(a, p)
    assert a != [0], "valuation of zero was not requested"
    if root == 0:
        return next(i for i, c in enumerate(a) if c)
    v = 0
    while len(a) > 1:
        quotient = [0] * (len(a)-1)
        quotient[-1] = a[-1]
        for i in range(len(a)-2, 0, -1):
            quotient[i-1] = (a[i] + root*quotient[i]) % p
        remainder = (a[0] + root*quotient[0]) % p
        if remainder:
            return v
        a = trim(quotient, p)
        v += 1
    return v


def g_numerator(x, q, p):
    m = [0, -1, 1]
    n = add(frobenius(x, q, p), x, p, -1)
    return add(frobenius(n, q, p), mul(n, power(m, q-1, p), p), p, -1)


count = 0
for p, q in [(2,2), (3,3), (2,4), (5,5), (7,7), (2,8), (3,9)]:
    for n in range(1,13):
        u = mul([0,1], power([-1,1], n+1, p), p)
        x = mul(u,u,p)
        a_num = add(frobenius(x,q,p), x, p, -1)
        gn = g_numerator(x,q,p)
        assert valuation(u,0,p) == 1
        assert valuation(u,1,p) == n+1
        assert valuation(a_num,0,p)-1 == 1
        assert valuation(a_num,1,p)-1 == 2*n+1
        assert valuation(gn,0,p)-q == 1
        assert valuation(gn,1,p)-q == 2*n+1
        count += 1
    print(f'q={q}: n=1..12, v0(a(u_n^2))=v0(g(u_n^2))=1; '
          'v1(a(u_n^2))=v1(g(u_n^2))=2n+1: PASS')

# Independent exhaustive checks on polynomial elements of R for prime fields.
elements = 0
for p in [2,3,5]:
    found = 0
    for coeffs in product(range(p), repeat=5):
        if sum(coeffs[1:]) % p:
            continue  # x(0) != x(1), so x is not in R.
        x = trim(list(coeffs),p)
        gn = g_numerator(x,p,p)
        if gn != [0]:
            assert valuation(gn,0,p)-p >= 1
            assert valuation(gn,1,p)-p >= 1
        found += 1
    elements += found
    print(f'q={p}: all {found} polynomial elements of R of degree <=4: '
          'g(x) has both valuations >=1 or is zero: PASS')
print(f'TOTAL: {count} exact rational-valuation cases; '
      f'{elements} exhaustive polynomial evaluations; all assertions passed.')

# B.017, R=F2, S=F2[epsilon]/epsilon^2. Represent s=a+bepsilon by a+2b.
def sq_add(x,y):
    return x ^ y

def sq_mul(x,y):
    a,b,c,d=x&1,x>>1,y&1,y>>1
    return (a*c) + 2*((a*d+b*c)&1)

for x,y,z in product(range(4),repeat=3):
    assert sq_mul(sq_mul(x,y),z)==sq_mul(x,sq_mul(y,z))
    assert sq_mul(x,sq_add(y,z))==sq_add(sq_mul(x,y),sq_mul(x,z))
assert sq_mul(2,2)==0
# e=epsilon(T^2-T) is nonzero, vanishes on both embedded base elements.
e=(0,2,2)
for r in [0,1]:
    value=0
    for c in reversed(e):
        value=sq_add(sq_mul(value,r),c)
    assert value==0
assert any(e)
# The split summand F2 e has tensor square F2; its nonzero basis tensor maps to zero.
assert all(sq_mul(a,b)==0 for a in e for b in e)
print('B.017 square-zero extension: all64 ring triples, both base evaluations, '
      'and the nonzero split tensor kernel witness: PASS')
