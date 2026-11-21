#!/usr/bin/env python3
"""Exploratory conductor-19 quotient on the A27 curve over F64.

Adapted from row_audit/verify_A27_character13_linear.py; this is the
same binary-interpolation arithmetic implementation at a different field
and conductor, not an independently written second implementation.
The follow-up arithmetic in Z/4[Z]/Phi19 computes the first rational
2-primary exponent after a degree-seven constant extension.
"""
from pathlib import Path
import hashlib
import json


def field_product(a, b):
    p = 0
    for i in range(6):
        if (b >> i) & 1:
            p ^= a << i
    for j in range(10, 5, -1):
        if (p >> j) & 1:
            p ^= 0x43 << (j-6)
    return p


M = [[field_product(a, b) for b in range(64)] for a in range(64)]
I = [0] + [next(b for b in range(1, 64) if M[a][b] == 1) for a in range(1, 64)]
assert all(M[a][I[a]] == 1 for a in range(1, 64))


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


u = next(a for a in range(2, 64) if M[a][a] ^ a ^ 1 == 0)
h = [0, 0, 1]
f = [0, u, 0, 1, 0, u]
IDENTITY = ((1,), ())


def verify(D):
    a, b = D
    assert a[-1] == 1 and len(b) < len(a)
    assert not mod(plus(plus(squared(b), times(h, b)), f), a)


def encode(a):
    return sum(c << (6*i) for i, c in enumerate(a))


def decode(a, degree):
    return trim([(a >> (6*i)) & 63 for i in range(degree)])


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
                (encode(mod(v, a1)) << (6*degree)) |
                (encode(mod(v, a2)) << (6*(degree+d1))))
    rhs = (encode(mod(f, a)) |
           (encode(b1) << (6*degree)) |
           (encode(b2) << (6*(degree+d1))))
    columns = [image(decode(1 << j, degree)) for j in range(6*degree)]
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



points=[]
for x in range(64):
 for y in range(64):
  if M[y][y]^M[M[x][x]][y]==evalp(f,x):points.append((x,y))
assert len(points)+1==60
Ds=[IDENTITY]+[((x,1),(y,) if y else ()) for x,y in points]
projected=[scalar(D,196) for D in Ds]
gen=next(D for D in projected if D!=IDENTITY)
cycle=[IDENTITY]
for j in range(18):cycle.append(add_divisors(cycle[-1],gen))
assert len(set(cycle))==19 and add_divisors(cycle[-1],gen)==IDENTITY
lookup={D:i for i,D in enumerate(cycle)}
counts=[0]*19
for D in projected:counts[lookup[D]]+=1
phi=(1<<19)-1
S=sum((v%2)<<i for i,v in enumerate(counts))
S=f2div(S,phi)[1]
order=1
if S:
 while residue_power(S,order,phi)!=1:order+=1

def cmul(a,b,mod):
 c=[0]*35
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%mod
 for i in range(34,17,-1):
  for j in range(18):c[i-18+j]=(c[i-18+j]-c[i])%mod
 return c[:18]
def cpow(a,n,mod):
 r=[1]+[0]*17
 while n:
  if n&1:r=cmul(r,a,mod)
  a=cmul(a,a,mod);n//=2
 return r
out=dict(field_modulus=67,u=u,gen=gen,counts=counts,S=S,order_mod2=order,scope='Exploratory adaptation of the existing A32 independent checker, not a separate independent implementation.')
for mod in [4,8]:
 c=[(counts[i]-counts[18])%mod for i in range(18)]
 v=cpow(c,order,mod);v[0]=(v[0]+1)%mod
 out['one_plus_c1_power_mod'+str(mod)]=v
print(json.dumps(out,indent=2))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
