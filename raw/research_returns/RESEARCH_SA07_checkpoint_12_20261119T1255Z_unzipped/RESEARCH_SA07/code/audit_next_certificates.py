"""Exact certificates for F.3.10 and F.3.12.

The infinite/profinite and descent conclusions are proved in F_audit.tex;
these computations certify the specified universal polynomial identities.
"""
from itertools import product

DEGREE = 5

def clean(a):
    return {w: c for w, c in a.items() if c}

def add(a, b):
    r = dict(a)
    for w, c in b.items():
        r[w] = r.get(w, 0) + c
    return clean(r)

def neg(a):
    return {w: -c for w, c in a.items()}

def mul(a, b):
    r = {}
    for w, c in a.items():
        for z, d in b.items():
            if len(w + z) <= DEGREE:
                r[w + z] = r.get(w + z, 0) + c*d
    return clean(r)

ONE = {'': 1}

def inverse(a):
    assert a.get('', 0) == 1
    n = add(a, neg(ONE))
    total = dict(ONE)
    power = dict(ONE)
    for _ in range(DEGREE):
        power = mul(power, neg(n))
        total = add(total, power)
    assert mul(a, total) == ONE == mul(total, a)
    return total

def comm(a, b):
    return mul(mul(mul(a, b), inverse(a)), inverse(b))

a = {'': 1, 'X': 1}
b = {'': 1, 'Y': 1}
c = comm(a, b)
certificate = add(comm(c, comm(c, a)), neg(ONE))
assert certificate
assert all(len(w) == 5 for w in certificate)
assert certificate['XYYXX'] == -1
print('F.3.10 exact integral degree-five commutator coefficients:')
for w in sorted(certificate):
    print(f'  {w}: {certificate[w]}')
print('Coefficient at XYYXX is -1, hence nonzero modulo every prime.')
for ell in [2, 3, 5, 7, 11, 13]:
    reduced = {w: v % ell for w, v in certificate.items() if v % ell}
    assert reduced.get('XYYXX') == ell - 1
    print(f'  Reduction modulo {ell}: nonidentity double commutator.')

# The one-coordinate carry identity proves the arbitrary finite-support
# identity by adding coordinates. Check the complete one-coordinate domain.
for x, y, z in product([0, 1], repeat=3):
    assert x*y + (x ^ y)*z == y*z + x*(y ^ z)
print('F.3.12 carry identity: all eight one-coordinate cases passed.')

# Complete finite tensor-constraint test with three coordinates and every
# sign sequence, including its trivialization over Z[i]. Exponents modulo 4
# encode exact powers of i, avoiding numerical complex approximations.
degrees = list(product([0, 1], repeat=3))
def xor(x, y):
    return tuple(a ^ b for a, b in zip(x, y))

def constraint(epsilon, x, y):
    return sum(2*e*a*b for e, a, b in zip(epsilon, x, y)) % 4

def trivialization(epsilon, x):
    return sum(e*a for e, a in zip(epsilon, x)) % 4

checked = 0
for eps in degrees:
    for x, y in product(degrees, repeat=2):
        assert constraint(eps, x, y) == constraint(eps, y, x)
        assert (trivialization(eps, xor(x, y)) + constraint(eps, x, y)) % 4 == (trivialization(eps, x) + trivialization(eps, y)) % 4
        for z in degrees:
            assert (constraint(eps, x, y) + constraint(eps, xor(x, y), z)) % 4 == (constraint(eps, y, z) + constraint(eps, x, xor(y, z))) % 4
            checked += 1
print(f'F.3.12 all {checked} three-coordinate associativity cases passed; symmetry and Z[i] trivializations passed.')
print('All exact certificates passed; no infinite theorem is inferred from a finite sample.')
