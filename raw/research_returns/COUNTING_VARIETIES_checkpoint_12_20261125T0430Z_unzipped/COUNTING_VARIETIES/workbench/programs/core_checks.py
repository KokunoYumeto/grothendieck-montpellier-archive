#!/usr/bin/env python3
"""Finite checks for the coherent-line construction; standard Python only.

Run from any directory: python3 core_checks.py --output core_results.json
These computations check examples and finite identities, not geometric smoothness.
"""
import argparse
import itertools
import json
import math
import random
from pathlib import Path


def add(a, b, p):
    c = a.copy()
    for e, v in b.items():
        c[e] = (c.get(e, 0) + v) % p
        if not c[e]:
            del c[e]
    return c


def mul(a, b, p, cap=None):
    c = {}
    for e, u in a.items():
        for f, v in b.items():
            g = tuple(x + y for x, y in zip(e, f))
            if cap is not None and any(x > cap for x in g):
                continue
            c[g] = (c.get(g, 0) + u * v) % p
    return {e: v for e, v in c.items() if v}


def power(a, n, p, r, cap=None):
    b = {(0,) * r: 1}
    for _ in range(n):
        b = mul(b, a, p, cap)
    return b


def hasse(a, p, r):
    return power(a, p - 1, p, r, p - 1).get((p - 1,) * r, 0)


def stabilize(g, p, u, q):
    m, d = q - 1, q + 1
    f = {}
    for ex, c in g.items():
        f[ex + (1,) * (m - u) + (1, 1)] = c % p
    ex = [0] * d
    ex[0], ex[-2], ex[-1] = m, 1, 1
    f = add(f, {tuple(ex): 1}, p)
    for j in list(range(m)) + [m]:
        ex = [0] * d
        ex[j] = d
        f = add(f, {tuple(ex): 1}, p)
    ex = [0] * d
    ex[0], ex[-1] = 1, q
    return add(f, {tuple(ex): p - 1}, p)


def compositions(n, r):
    if r == 1:
        yield (n,)
    else:
        for i in range(n + 1):
            for rest in compositions(n - i, r - 1):
                yield (i,) + rest


def projective_points(p, r):
    for first in range(r):
        for tail in itertools.product(range(p), repeat=r - first - 1):
            yield (0,) * first + (1,) + tail


def rank(a, p):
    a = [list(row) for row in a]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        j = next((j for j in range(r, len(a)) if a[j][c] % p), None)
        if j is None:
            continue
        a[r], a[j] = a[j], a[r]
        z = pow(a[r][c] % p, -1, p)
        a[r] = [(x * z) % p for x in a[r]]
        for j in range(len(a)):
            if j != r:
                z = a[j][c] % p
                a[j] = [(x - z * y) % p for x, y in zip(a[j], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def inverse(a, p):
    n = len(a)
    b = [list(row) + [int(i == j) for j in range(n)] for i, row in enumerate(a)]
    for c in range(n):
        j = next(j for j in range(c, n) if b[j][c] % p)
        b[c], b[j] = b[j], b[c]
        z = pow(b[c][c] % p, -1, p)
        b[c] = [(x * z) % p for x in b[c]]
        for j in range(n):
            if j != c:
                z = b[j][c]
                b[j] = [(x - z * y) % p for x, y in zip(b[j], b[c])]
    return [row[n:] for row in b]


def linear_poly(row, p):
    r = len(row)
    out = {}
    for j, c in enumerate(row):
        if c % p:
            e = [0] * r
            e[j] = 1
            out[tuple(e)] = c % p
    return out


def linear_product_coefficient(rows, exponents, p, m):
    a = {(0,) * m: 1}
    for row, e in zip(rows, exponents):
        for _ in range(e):
            a = mul(a, linear_poly(row, p), p, p - 1)
    return a.get((p - 1,) * m, 0)


def small_surplus_coefficient(rows, exponents, p, m):
    """Independent implementation of the saturated-factor elimination."""
    full = [r for r, e in zip(rows, exponents) if e == p - 1]
    other = [(r, e) for r, e in zip(rows, exponents) if e != p - 1]
    k = len(full)
    if k > m or rank(full, p) < k:
        return 0, 0
    basis = [r[:] for r in full]
    for j in range(m):
        row = [int(i == j) for i in range(m)]
        if rank(basis + [row], p) > len(basis):
            basis.append(row)
    inv = inverse(basis, p)
    rsmall = m - k
    reduced = []
    for row, e in other:
        new = [sum(row[j] * inv[j][i] for j in range(m)) % p
               for i in range(k, m)]
        reduced.append((new, e))
    if not rsmall:
        return int(not other), 0
    return linear_product_coefficient([r for r, e in reduced],
                                      [e for r, e in reduced], p, rsmall), rsmall


def syndrome_coefficient(rows, exponents, p, m):
    chosen=[]
    extras=[]
    for row,e in zip(rows,exponents):
        if rank([r for r,d in chosen]+[row],p)>len(chosen):
            chosen.append((row,e))
        else:
            extras.append((row,e))
    if len(chosen)<m:
        return 0
    inv=inverse([r for r,e in chosen],p)
    coeff=[[sum(row[j]*inv[j][i] for j in range(m))%p for i in range(m)]
           for row,e in extras]
    k=len(extras)
    states={(0,)*k:1}
    for i,(row,e) in enumerate(chosen):
        nxt={}
        for state,value in states.items():
            for a in range(p):
                dest=tuple((state[j]+a*coeff[j][i])%p for j in range(k))
                nxt[dest]=(nxt.get(dest,0)+value*pow(a,e,p))%p
        states={s:v for s,v in nxt.items() if v}
    out=sum(v*math.prod(pow(s[j],extras[j][1],p) for j in range(k))
            for s,v in states.items())
    return ((-1)**m*out)%p


def main():
    rng = random.Random(20261124)
    result = {}
    checks = 0
    for p in (2, 3, 5):
        for u in (1, 2, 3):
            q0 = p * ((u + 1) // p + 1)
            for q in (q0, q0 + p):
                for _ in range(5):
                    g = {e: rng.randrange(p) for e in compositions(u, u)}
                    g = {e: c for e, c in g.items() if c}
                    assert hasse(g, p, u) == hasse(stabilize(g, p, u, q), p, q + 1)
                    checks += 1
    result['stabilization_cases_including_Q_equals_p'] = checks
    counts = []
    for a in range(3):
        n = 0
        for r, s, y, z in projective_points(3, 4):
            n += (y*z*(r*r-a*s*s)+y**4+r**4+s**4-r*z**3) % 3 == 0
        counts.append(n)
    assert counts == [13, 11, 15]
    result['quartic_K3_counts_F3'] = counts
    quintics = []
    for a in range(2):
        quintics.append(sum((y*z*(a*r*s*t+r**3)+y**5+r**5+s**5+t**5-r*z**4)%2 == 0
                            for r,s,t,y,z in projective_points(2,5)))
    assert quintics == [15, 14]
    result['quintic_counts_F2'] = quintics
    orcounts = {}
    for p, q, m in ((2, 8, 7), (3, 9, 8)):
        cone = 0
        for xy in itertools.product(range(p), repeat=m+1):
            x, y = xy[:-1], xy[-1]
            a,b,c,e = x[:4]
            P = ((a*e+b*c+b*e)*(a+b)*(c+e)) % p
            Z = (a*b*c*e) % p
            if p == 2:
                G = x[4]*P
                u = 5
            else:
                G = -x[4]**2*P+x[5]**2*Z
                u = 6
            A = (G*math.prod(x[u:])+x[0]**(q-1)) % p
            coeff = (y*A-x[0]) % p
            const = (y**(q+1)+sum(v**(q+1) for v in x)) % p
            cone += 1 if coeff else (p if not const else 0)
        pointcount = (cone-1)//(p-1)
        assert pointcount % p == (1+3) % p
        orcounts[str(p)] = {'degree':q+1, 'cone':cone, 'projective':pointcount, 'scalar':3%p}
    result['two_variable_OR_rank_one'] = orcounts
    product_checks = 0
    maxsmall = 0
    for p in (2,3,5):
        for m in range(2,6):
            for _ in range(25):
                total = m*(p-1)
                exps = []
                while total:
                    e = rng.randint(1,min(p-1,total))
                    exps.append(e)
                    total -= e
                rows = [[rng.randrange(p) for _ in range(m)] for e in exps]
                truth = linear_product_coefficient(rows,exps,p,m)
                got,rsmall = small_surplus_coefficient(rows,exps,p,m)
                assert got == truth, (p,m,rows,exps,got,truth)
                assert syndrome_coefficient(rows,exps,p,m)==truth
                surplus = len(rows)-m
                assert rsmall <= max(0,(p-2)*surplus)
                maxsmall = max(maxsmall,rsmall)
                product_checks += 1
    result['near_minimal_support_product_cases'] = product_checks
    result['syndrome_dynamic_program_cases'] = product_checks
    result['largest_residual_dimension_checked'] = maxsmall
    shifts = 0
    for p in (2,3,5,7,11):
        k = (p-1).bit_length()
        for a in range(p):
            count = 0
            for x1,x2,b in itertools.product((0,1), repeat=3):
                for z in range(1<<k):
                    count += (not b and (x1 or x2) and z == 0) or (b and not x1 and not x2 and z<a)
            assert count == 3+a
            shifts += 1
    result['additive_shift_counts'] = shifts
    result['status'] = 'all assertions passed'
    parser=argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args=parser.parse_args()
    text=json.dumps(result,indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    print(text,end='')


if __name__ == '__main__':
    main()
