"""Exact independent character checks; no external algebra package.

Characters are computed by Murnaghan--Nakayama, enumerating skew border
strips directly.  The family formulas are evaluated separately.
Run: python computations/independent_characters.py
"""
from functools import lru_cache
from collections import Counter
from fractions import Fraction
from itertools import product, combinations_with_replacement
from math import factorial
from pathlib import Path
import json


@lru_cache(None)
def partitions(n, bound=None):
    if n == 0:
        return ((),)
    if n < 0:
        return ()
    if bound is None:
        bound = n
    return tuple((a,) + p for a in range(min(n, bound), 0, -1)
                 for p in partitions(n-a, a))


@lru_cache(None)
def removals(lam, r):
    n = sum(lam)
    ans = []
    for nu in partitions(n-r):
        if len(nu) > len(lam) or any(a > b for a,b in zip(nu, lam)):
            continue
        cells = {(i,j) for i,a in enumerate(lam)
                 for j in range(nu[i] if i < len(nu) else 0, a)}
        if not cells or len(cells) != r:
            continue
        if any((i+1,j) in cells and (i,j+1) in cells and (i+1,j+1) in cells
               for i,j in cells):
            continue
        seen = {next(iter(cells))}
        stack = list(seen)
        while stack:
            i,j = stack.pop()
            for c in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if c in cells and c not in seen:
                    seen.add(c)
                    stack.append(c)
        if len(seen) == r:
            height = len({i for i,j in cells})-1
            ans.append((nu, (-1)**height))
    return tuple(ans)


@lru_cache(None)
def character(lam, cyc):
    if not cyc:
        return int(not lam)
    if sum(lam) != sum(cyc):
        return 0
    return sum(sign * character(nu, cyc[1:])
               for nu, sign in removals(lam, cyc[0]))


@lru_cache(None)
def z_type(cyc):
    z = 1
    for r,m in Counter(cyc).items():
        z *= r**m * factorial(m)
    return z


def kronecker(lam, mu, nu):
    n = sum(lam)
    assert sum(mu) == sum(nu) == n
    v = sum((Fraction(character(lam,c)*character(mu,c)*character(nu,c),
                      z_type(c)) for c in partitions(n)), Fraction(0))
    assert v.denominator == 1 and v >= 0, (lam,mu,nu,v)
    return v.numerator


def two_row(n,a):
    return tuple(x for x in (n-a,a) if x)


def hook(n,a):
    return (n-a,) + (1,)*a


def interval_formula(n,a,b,c):
    a,b,c = sorted((a,b,c), reverse=True)
    lower = max(0, (a+b+c-n+1)//2)
    upper = (b+c-a)//2
    return max(0,upper-lower+1)


def hook_formula(n,a,b,c):
    return int(max(a,b,c)*2 <= a+b+c <= 2*n-2)


def rectangle_partitions(a,b):
    counts = [0]*(a*b+1)
    for n in range(a*b+1):
        counts[n] = sum(1 for p in partitions(n,b) if len(p) <= a)
    return counts


def subset_sum_counts(parts):
    out = Counter({0:1})
    for a in parts:
        for k,v in list(out.items()):
            out[k+a] += v
    return out


def run():
    results = {'engine':'Murnaghan--Nakayama by connected skew border strips',
               'arithmetic':'exact fractions and integers', 'checks':{}}
    orth = 0
    for n in range(0,9):
        ps = partitions(n)
        for i,lam in enumerate(ps):
            for j,mu in enumerate(ps[:i+1]):
                ip = sum((Fraction(character(lam,c)*character(mu,c),z_type(c))
                          for c in ps), Fraction(0))
                assert ip == int(i==j), (n,lam,mu,ip)
                orth += 1
    results['checks']['character_orthogonality_N_0_to_8'] = orth
    rows = 0
    for n in range(1,13):
        for a,b,c in combinations_with_replacement(range(n//2+1),3):
            got = kronecker(two_row(n,a),two_row(n,b),two_row(n,c))
            exp = interval_formula(n,a,b,c)
            assert got == exp, (n,a,b,c,got,exp)
            rows += 1
    results['checks']['two_row_sorted_triples_N_1_to_12'] = rows
    hooks = 0
    for n in range(1,11):
        for a,b,c in combinations_with_replacement(range(n),3):
            got = kronecker(hook(n,a),hook(n,b),hook(n,c))
            exp = hook_formula(n,a,b,c)
            assert got == exp, (n,a,b,c,got,exp)
            hooks += 1
    results['checks']['hook_sorted_triples_N_1_to_10'] = hooks
    rect_two = rect_hooks = 0
    for a in range(1,5):
        for b in range(1,6):
            n = a*b
            if n > 16:
                continue
            rect = (b,)*a
            p = rectangle_partitions(a,b)
            for r in range(n//2+1):
                got = kronecker(rect,rect,two_row(n,r))
                exp = p[r]-(p[r-1] if r else 0)
                assert got == exp, (a,b,r,got,exp)
                rect_two += 1
            hs = subset_sum_counts(range(3,2*min(a,b),2))
            for r in range(n):
                got = kronecker(rect,rect,hook(n,r))
                exp = hs[r]
                assert got == exp, (a,b,r,got,exp)
                rect_hooks += 1
    results['checks']['rectangle_two_row_a_le4_b_le5_N_le16'] = rect_two
    results['checks']['rectangle_hooks_a_le4_b_le5_N_le16'] = rect_hooks
    results['sample_rectangular_ray'] = [kronecker((k,k),(k,k),(k,k))
                                          for k in range(1,9)]
    results['status'] = 'all assertions passed'
    path = Path(__file__).with_name('independent_character_results.json')
    path.write_text(json.dumps(results,indent=2)+'\n')
    print(json.dumps(results,indent=2))


if __name__ == '__main__':
    run()
