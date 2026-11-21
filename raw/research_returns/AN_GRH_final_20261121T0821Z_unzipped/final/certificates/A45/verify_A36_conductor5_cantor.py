#!/usr/bin/env python3
"""Independent exact conductor-5 check using extended-GCD Cantor arithmetic.

Adapted from the separate A32 Cantor producer, rather than the root probe's
F2-linear interpolation arithmetic. This calculation projects all256 point classes onto the actual cyclic5 subgroup
and retains every image; it does not import the root linear-interpolation probe.
This is exact finite computation, not formal verification.
"""
from pathlib import Path
import hashlib
import json

MOD = 0x11B
Q = 256


def slow_mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & Q:
            a ^= MOD
    return out


TABLE = [[slow_mul(a, b) for b in range(Q)] for a in range(Q)]


def mul(a, b):
    return TABLE[a][b]


def power(a, n):
    out = 1
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


INVERSES = [0] + [power(a, Q - 2) for a in range(1, Q)]
assert all(mul(a, INVERSES[a]) == 1 for a in range(1, Q))


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) ^
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def pmul(a, b):
    out = [0] * max(0, len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i+j] ^= mul(ai, bj)
    return trim(out)


def ppow(a, n):
    out = [1]
    for _ in range(n):
        out = pmul(out, a)
    return out


def peval(a, x):
    out = 0
    for ai in reversed(a):
        out = mul(out, x) ^ ai
    return out



inv = lambda a: INVERSES[a]
U=min(a for a in range(Q) if mul(a,a)^a^1==0)
H=[0,0,1]
f=[0,U,0,1,0,U]
ZERO=((1,),())

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
    points=[(x,y) for x in range(Q) for y in range(Q)
            if mul(y,y)^mul(mul(x,x),y)^peval(f,x)==0]
    divisors=[ZERO]+[((x,1),(y,) if y else ()) for x,y in points]
    assert len(divisors)==256
    sums=[]
    orders=[]
    for trace in (1,-2):
        prev,now=2,trace
        for m in range(2,5):
            prev,now=now,trace*now-4*prev
        sums.append(now);orders.append(4**4+1-now)
    assert sums==[17,-16] and orders==[240,273]
    jac=orders[0]*orders[1]
    assert 4**4+1-sum(sums)==256 and jac==65520
    assert jac%5==0 and jac%25!=0
    for d in divisors:
        assert compose(d,ZERO)==d and compose(d,negate(d))==ZERO
        assert multiple(d,jac)==ZERO
    projected=[multiple(d,13104) for d in divisors]
    gen=next(d for d in projected if d!=ZERO)
    cycle=[multiple(gen,j) for j in range(5)]
    assert len(set(cycle))==5 and multiple(gen,5)==ZERO
    lookup={d:i for i,d in enumerate(cycle)}
    counts=[0]*5;images=[]
    for i,d in enumerate(projected):
        residue=lookup[d];counts[residue]+=1
        images.append({'point':'infinity' if i==0 else list(points[i-1]),
                       'projected_Mumford':d,'residue':residue})
    assert gen==((224,80,1),(180,59))
    assert counts==[76,45,45,45,45]
    normalized=[counts[i]-counts[4] for i in range(4)]
    assert normalized==[31,0,0,0]
    L=[1,31,256]
    H_E=pmul_integer(L,L)
    assert H_E==[1,62,1473,15872,65536]
    jac_E=sum(H_E)
    assert jac_E==288**2==2**10*3**4 and jac_E%5!=0
    for i in range(0,len(divisors),7):
        a,b,c=divisors[i],divisors[(i+31)%256],divisors[(i+79)%256]
        assert compose(compose(a,b),c)==compose(a,compose(b,c))
    result={'curve':'Y^2+X^2Y=uX^5+X^3+uX over F256',
            'field':{'size':Q,'modulus':MOD,'u':U,'encoding':'binary polynomial coefficients, low degrees first'},
            'point_count':len(divisors),'Jacobian_order':jac,
            'elliptic_factor_power_sums':sums,'factor_orders':orders,
            'conductor':5,'projection_multiplier':13104,
            'cyclic_generator_Mumford':gen,'generator_cycle':cycle,
            'point_image_counts':counts,'all_point_images':images,
            'faithful_character_c1_Phi5_basis':normalized,
            'faithful_L_polynomial_low_to_high':L,
            'reflection_Jacobian_H_polynomial_low_to_high':H_E,
            'reflection_Jacobian_order':jac_E,
            'reflection_Jacobian_order_factorization':{'2':10,'3':4},
            'scope':'Independent Cantor arithmetic certificate for the root linear-interpolation calculation. Reflection deductions use A33 and the character-factor proof; this is not formal verification.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({k:result[k] for k in ('field','point_count','Jacobian_order','cyclic_generator_Mumford','point_image_counts','faithful_L_polynomial_low_to_high','reflection_Jacobian_order','source_sha256')},indent=2))

def pmul_integer(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

if __name__=='__main__':
    main()
