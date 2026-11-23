#!/usr/bin/env python3
"""Exact finite normalization checks for AM-R-011; not a proof checker."""
from pathlib import Path
from math import factorial, prod
from fractions import Fraction
import json
import sympy as sp


def partitions(n, max_part=None, max_len=3):
    if n == 0:
        yield ()
        return
    if max_len == 0:
        return
    for a in range(min(n, max_part or n), 0, -1):
        for rest in partitions(n-a, a, max_len-1):
            yield (a,) + rest


def hook(lam):
    return prod(lam[i]-j + sum(row > j for row in lam)-i-1
                for i in range(len(lam)) for j in range(lam[i]))


def hook_factorial(lam):
    a = len(lam)
    return Fraction(prod(factorial(lam[i]+a-i-1) for i in range(a)),
                    prod(lam[i]-lam[j]+j-i
                         for i in range(a) for j in range(i+1, a)))


def valuation(n, p):
    out = 0
    while n and n % p == 0:
        n //= p
        out += 1
    return out


def polynomial_norm(lam):
    a = len(lam)
    if not a:
        return 1, 1
    variables = sp.symbols('z0:'+str(a*a))
    matrix = sp.Matrix(a, a, variables)
    p = sp.Integer(1)
    for i in range(a):
        exponent = lam[i] - (lam[i+1] if i+1 < a else 0)
        if exponent:
            p *= matrix[:i+1, :i+1].det() ** exponent
    poly = sp.Poly(sp.expand(p), *variables)
    norm = sum(int(c)**2 * prod(factorial(a) for a in exps)
               for exps, c in poly.terms())
    return norm, len(poly.terms())


def main():
    cases = []
    for degree in range(10):
        for lam in partitions(degree):
            norm, terms = polynomial_norm(lam)
            expected = hook(lam)
            assert norm == expected == hook_factorial(lam)
            cases.append({'partition':lam,'degree':degree,
                          'terms':terms,'fischer_norm_squared':norm,
                          'hook_product':expected})
    eta0 = (0,)*6
    nu0 = (1,)*6
    eta1 = nu0 + (0,)*14
    nu1 = (3,)*6 + (2,)*14
    eta2 = nu1 + (0,)*14
    assert sum(nu0) == 6 and sum(nu1) == 46
    assert tuple(x+2 for x in eta1) == nu1
    h0, h1 = hook(nu0), hook(nu1)
    ratio = prod(eta1[i]+20-i-1+r for i in range(20) for r in (1,2))
    assert h0 == factorial(6)
    assert h1 == ratio*h0
    assert hook(eta0) == 1
    assert hook(eta1) == h0 and hook(eta2) == h1
    assert hook_factorial(nu1) == h1
    record = {
        'status':'PASS',
        'scope':'Finite exact polynomial norm and selected hook-ratio checks only.',
        'small_polynomial_cases':cases,
        'number_of_small_cases':len(cases),
        'rank_example':{
            'ranks':[6,20,34], 'kernel_degrees':[6,46],
            'hook_nu0':h0, 'hook_nu1':h1, 'second_ratio':ratio,
            'valuations':{str(p):[valuation(h0,p),valuation(h1,p),valuation(ratio,p)]
                          for p in (2,3,5,7,11,13,17,19,23,29)}
        }
    }
    dest = Path(__file__).resolve().parents[1]/'checks/selected_schur_metric_certificate.json'
    dest.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k!='small_polynomial_cases'}))


if __name__ == '__main__':
    main()
