#!/usr/bin/env python3
"""Independent exact conductor-19 check using extended-GCD Cantor arithmetic.

Adapted from the separate A32 Cantor producer, rather than the root probe's
F2-linear interpolation arithmetic. Cyclotomic products use cyclic length-19
convolution then normalization modulo Phi19, rather than polynomial reduction.
This is exact finite computation, not formal verification.
"""
from pathlib import Path
import hashlib
import json

MOD = 0x43
Q = 64


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


def cyclic_product(a,b,modulus):
    c=[0]*19
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            c[(i+j)%19]=(c[(i+j)%19]+ai*bj)%modulus
    return c

def cyc_power(a,n,modulus):
    out=[1]+[0]*18
    for unused in range(n):
        out=cyclic_product(out,a,modulus)
    return out

def normalize(a,modulus):
    return [(a[i]-a[18])%modulus for i in range(18)]

def main():
    points=[(x,y) for x in range(Q) for y in range(Q)
            if mul(y,y)^mul(mul(x,x),y)^peval(f,x)==0]
    divisors=[ZERO]+[((x,1),(y,) if y else ()) for x,y in points]
    assert len(divisors)==60
    # A27's two Frobenius factors over F4 have traces 1 and -2.
    sums=[]
    orders=[]
    for trace in (1,-2):
        prev,now=2,trace
        for m in range(2,4):
            prev,now=now,trace*now-4*prev
        sums.append(now)
        orders.append(4**3+1-now)
    assert 4**3+1-sum(sums)==60
    jac=orders[0]*orders[1]
    assert jac==3724 and jac%19==0 and jac%(19*19)!=0
    for d in divisors:
        assert compose(d,ZERO)==d
        assert compose(d,negate(d))==ZERO
        assert multiple(d,jac)==ZERO
    projected=[multiple(d,196) for d in divisors]
    gen=next(d for d in projected if d!=ZERO)
    cycle=[multiple(gen,j) for j in range(19)]
    assert len(set(cycle))==19 and multiple(gen,19)==ZERO
    lookup={d:i for i,d in enumerate(cycle)}
    counts=[0]*19
    images=[]
    for i,d in enumerate(projected):
        residue=lookup[d]
        counts[residue]+=1
        images.append({'point':'infinity' if i==0 else list(points[i-1]),
                       'projected_Mumford':d,'residue':residue})
    expected=[6,2,2,2,5,2,5,2,2,5,5,2,2,5,2,5,2,2,2]
    assert counts==expected
    assert U==58 and gen==((8,54,1),(50,49))
    # Phi19 irreducibility: 2 has exact multiplicative order18 modulo19.
    assert pow(2,18,19)==1 and all(pow(2,d,19)!=1 for d in (1,2,3,6,9))
    powers_mod2=[normalize(cyc_power(counts,j,2),2) for j in range(1,8)]
    one=[1]+[0]*17
    assert powers_mod2[-1]==one and all(v!=one for v in powers_mod2[:-1])
    one_plus={}
    for modulus in (4,8):
        v=cyc_power(counts,7,modulus)
        v[0]=(v[0]+1)%modulus
        v=normalize(v,modulus)
        one_plus[str(modulus)]=v
    assert one_plus['4']==[2]+[0]*17
    assert one_plus['8']==[6]+[0]*17
    # Associativity samples include coincident, opposite and generic supports.
    for i in range(0,len(divisors),3):
        a,b,c=divisors[i],divisors[(i+17)%60],divisors[(i+29)%60]
        assert compose(compose(a,b),c)==compose(a,compose(b,c))
    result={'field':{'size':Q,'modulus':MOD,'u':U,
                     'encoding':'binary polynomial basis, low-degree bits first'},
            'curve':'Y^2+X^2Y=uX^5+X^3+uX',
            'point_count':len(divisors),'Jacobian_order':jac,
            'elliptic_factor_power_sums':sums,'factor_orders':orders,
            'quotient_degree':19,'projection_multiplier':196,
            'cyclic_generator_Mumford':gen,'point_image_counts':counts,
            'generator_cycle':cycle,'all_point_images':images,
            'Phi19_irreducible_over_F2':True,'order_c1_mod2':7,
            'one_plus_c1_power7':one_plus,
            'claimed_Prym_exponent_after_degree7':2,
            'scope':'Independent Cantor divisor arithmetic and cyclic-convolution check of the root F2-linear probe. Exponent inference additionally uses A34 exact module proof; no formal verification claim.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    target=Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps({key:result[key] for key in ('point_count','Jacobian_order','cyclic_generator_Mumford','point_image_counts','order_c1_mod2','one_plus_c1_power7','source_sha256')},indent=2))

if __name__=='__main__':
    main()
