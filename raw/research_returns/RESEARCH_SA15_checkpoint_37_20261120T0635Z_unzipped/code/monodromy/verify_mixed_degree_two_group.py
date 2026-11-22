#!/usr/bin/env python3
"""Independent exact reconstruction of two mixed degree-two Frobenius points.

No discovery program or stored Cartier matrix is imported.  The one-factor
Cartier maps are reconstructed by squaring in the two coordinate rings:
 C_o(f dx/x)^2=(1+e)f and C_s(f dx)^2=n f.
The mathematical generic-family conclusion is separately proved in the TeX.
"""
import itertools
import json
import time
from pathlib import Path
import sympy as sp

started = time.perf_counter()
basis = [(0,0),(1,0),(2,0),(3,0),(0,1),(1,1)]
indices = {v:i for i,v in enumerate(basis)}

def add(*polys):
    out = set()
    for poly in polys:
        out.symmetric_difference_update(poly)
    return out

def reduce_monomial(u,v,ordinary):
    if v < 2:
        return {(u,v)}
    # y^2=xy+x^3+1 in the ordinary ring; y^2=y+x^3 in the ss ring.
    if ordinary:
        return add(reduce_monomial(u+1,v-1,True),
                   reduce_monomial(u+3,v-2,True),
                   reduce_monomial(u,v-2,True))
    return add(reduce_monomial(u,v-1,False),
               reduce_monomial(u+3,v-2,False))

def multiply(p,q,ordinary):
    return add(*(reduce_monomial(a+c,b+d,ordinary)
                 for a,b in p for c,d in q))

def derive(poly,ordinary):
    out = set()
    for u,v in poly:
        if ordinary:
            if (u+v) % 2:
                out.symmetric_difference_update({(u,v)})
            if v:
                out.symmetric_difference_update({(u+2,0)})
        else:
            if u % 2:
                out.symmetric_difference_update({(u-1,v)})
            if v:
                out.symmetric_difference_update({(u+2,0)})
    return out

def one_factor(ordinary):
    squares = [multiply({v},{v},ordinary) for v in basis]
    # Exhaustive 64-entry inverse of the square map on this six-dimensional
    # F2-space; equality is in its reduced coordinate ring.
    square_inverse = {}
    for bits in range(64):
        poly = add(*(squares[i] for i in range(6) if bits >> i & 1))
        key = frozenset(poly)
        assert key not in square_inverse
        square_inverse[key] = bits
    table = []
    for a in basis:
        row = []
        for b in basis:
            product = multiply({a},{b},ordinary)
            target = derive(product,ordinary)
            if ordinary:
                target = add(target,product)
            row.append(square_inverse[frozenset(target)])
        table.append(row)
    derivation = []
    for a in basis:
        poly = derive({a},ordinary)
        assert poly.issubset(indices)
        derivation.append(sum(1 << indices[v] for v in poly))
    return table,derivation

ordinary,eo = one_factor(True)
supersingular,ns = one_factor(False)

def tensor_bits(a,b):
    return sum(1 << (6*i+j) for i in range(6) for j in range(6)
               if a >> i & 1 and b >> j & 1)

def matrix_for(section):
    rows = [0]*36
    for j in range(36):
        u,v = divmod(j,6)
        col = 0
        for h in range(36):
            if section >> h & 1:
                a,b = divmod(h,6)
                col ^= tensor_bits(ordinary[a][u],supersingular[b][v])
        for i in range(36):
            rows[i] |= ((col >> i) & 1) << j
    return rows

def apply(rows,v):
    return sum(((row & v).bit_count() & 1) << i
               for i,row in enumerate(rows))

def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            lead = row.bit_length()-1
            if lead not in pivots:
                pivots[lead] = row
                break
            row ^= pivots[lead]
    return len(pivots)

def compose(rows):
    return [sum((apply(rows,1 << j) >> i & 1) << j for j in range(36))
            for i in range(36)]

def matrix_square(rows):
    columns = [apply(rows,1 << j) for j in range(36)]
    columns2 = [apply(rows,v) for v in columns]
    return [sum((columns2[j] >> i & 1) << j for j in range(36))
            for i in range(36)]

def derivative_vector(s,first):
    out = 0
    for j in range(36):
        if s >> j & 1:
            a,b = divmod(j,6)
            out ^= tensor_bits(eo[a],1 << b) if first else tensor_bits(1 << a,ns[b])
    return out

def pmod(a,b):
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a

def pgcd(a,b):
    while b:
        a,b = b,pmod(a,b)
    return a

def psquare(a):
    return sum((a >> i & 1) << (2*i) for i in range(a.bit_length()))

T = sp.Symbol('T')
witnesses = [
    (34346068584,[1494603548,420583168],None),
    (68001692233,[26911823620,74729216],[8601123076,41642123014]),
]
records = []
for number,(s,lambdas,mus) in enumerate(witnesses,1):
    C = matrix_for(s)
    assert compose(C) == C
    assert rank(C) == rank(matrix_square(C)) == 34
    l0 = derivative_vector(s,False)
    l1 = derivative_vector(l0,True)
    assert [l0,l1] == lambdas and l0 and l1 and l0 != l1
    assert all(apply(C,x) == x for x in lambdas)
    integer_matrix = sp.Matrix(36,36,lambda i,j:(C[i] >> j) & 1)
    cp = sp.Poly(integer_matrix.charpoly(T).as_expr(),T,modulus=2)
    f,rem = sp.div(cp,sp.Poly(T**2*(T+1)**2,T,modulus=2))
    assert rem.is_zero and f.degree() == 32
    record = dict(section_bits=s,lambda_bits=lambdas,rank_C=34,rank_C2=34,
                  full_charpoly=str(cp.as_expr()),kernel_charpoly=str(f.as_expr()))
    if number == 1:
        fb = sum((int(v)%2) << mon[0] for mon,v in f.terms())
        assert fb == 6372510499
        x = 2
        for power in range(1,33):
            x = pmod(psquare(x),fb)
            if power == 16:
                assert pgcd(x ^ 2,fb) == 1
        assert x == 2
        reciprocal = sum((fb >> i & 1) << (32-i) for i in range(33))
        assert reciprocal != fb
        assert all(65537 % q for q in range(2,257))
        assert pow(2,16,65537) == 65536 and pow(2,32,65537) == 1
        assert all(pow(2,j,65537) != 1 for j in (1,2,4,8,16))
        record.update(kernel_polynomial_bits=fb,irreducible=True,
                      nonreciprocal=True,primitive_prime=65537,order_of_2=32)
    else:
        assert all(apply(C,mu) ^ mu == lam for mu,lam in zip(mus,lambdas))
        assert rank([row ^ (1 << i) for i,row in enumerate(C)]) == 34
        record.update(mu_bits=mus,rank_C_minus_I=34,explicit_coboundaries=True)
    records.append(record)

out = dict(status='PASS',scope='Exact two-point coefficient calculation only; generic-family normality and group arguments are separate.',
           reconstruction='Coordinate-ring multiplication, invariant derivations and exhaustive inversion of the square map; no imported Cartier matrices.',
           curves=['y^2+xy=x^3+1','y^2+y=x^3'],basis=basis,records=records,
           runtime_seconds=time.perf_counter()-started)
destination = Path(__file__).resolve().parents[1]/'outputs/verify_mixed_degree_two_group.json'
destination.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
