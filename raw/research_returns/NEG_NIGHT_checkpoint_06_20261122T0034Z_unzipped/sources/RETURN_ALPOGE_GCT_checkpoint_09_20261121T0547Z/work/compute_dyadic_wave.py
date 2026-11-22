"""Exact exploratory primitive-dyadic wave, not an asymptotic certificate.

Uses actual residue C(zeta)=prod_w(1-zeta^(g*w))^(-normal_mult(w)),
with normal character Sym^3(chain weights)-End(chain weights).
All arithmetic for the inverse is integral with a power-of-two denominator.
"""
from collections import Counter
from itertools import combinations_with_replacement
from math import gcd, log2
from pathlib import Path
import json
import sys


def multiply_shift(v, w):
    d = len(v)
    out = [0] * d
    for i, x in enumerate(v):
        j, r = divmod(i + w, d)
        out[r] += (-x if j % 2 else x)
    return out


def twice_inverse_factor(v, w):
    """Return 2*(1-X^w)^(-1)*v modulo X^d+1, 0<w<2d."""
    d = len(v)
    g = gcd(d, w)
    length = d // g
    out = [0] * d
    for start in range(g):
        indices = [start]
        signs = []
        previous = start
        accum = 0
        for _ in range(1, length):
            quotient, nxt = divmod(previous + w, d)
            sign = -1 if quotient % 2 else 1
            signs.append(sign)
            indices.append(nxt)
            accum = sign * accum + v[nxt]
            previous = nxt
        quotient, nxt = divmod(previous + w, d)
        assert nxt == start
        closing_sign = -1 if quotient % 2 else 1
        out[start] = v[start] + closing_sign * accum
        for j in range(1, length):
            out[indices[j]] = signs[j-1] * out[indices[j-1]] + 2*v[indices[j]]
    return out


def compute(n):
    M = 2**(n-1)
    d = M//2
    g = gcd(n, 3)
    weights = [pow(-2, i, M) for i in range(n)]
    normal = Counter(sum(weights[i] for i in triple) % M
                     for triple in combinations_with_replacement(range(n), 3))
    normal.subtract((weights[i]-weights[j]) % M
                    for i in range(n) for j in range(n))
    assert all(v >= 0 for v in normal.values()) and normal[0] == 0
    assert sum(normal.values()) == n*(n-1)*(n-2)//6
    v = [1]+[0]*(d-1)
    power = 0
    for w, count in sorted(normal.items()):
        exponent = (g*w) % M
        for _ in range(count):
            out = twice_inverse_factor(v, exponent)
            if n <= 12:
                shifted = multiply_shift(out, exponent)
                assert all(a-b == 2*c for a,b,c in zip(out, shifted, v))
            v = out
            power += 1
            while all(x % 2 == 0 for x in v):
                v = [x//2 for x in v]
                power -= 1
    if n == 4:
        assert v == [1,1,1,1] and power == 3
    # 2*wave(s) = coefficient of X^s in this negacyclic inverse.
    def value(s):
        quotient, r = divmod(s, d)
        a = (-1 if quotient % 2 else 1)*v[r]
        return {'s':s,'sign':(a>0)-(a<0),
                'numerator':str(a),'denominator_power_of_two':power+1,
                'log2_abs':None if not a else log2(abs(a))-power-1}
    samples=sorted(set(list(range(min(33,M)))+[n,n*n,n**3,n**4]))
    result={'n':n,'M':M,'D':sum(normal.values()),'normal_weights':dict(sorted(normal.items())),
            'inverse_denominator_power_of_two':power,
            'positive_coefficients':sum(x>0 for x in v),
            'negative_coefficients':sum(x<0 for x in v),
            'zero_coefficients':sum(x==0 for x in v),
            'samples':[value(s) for s in samples]}
    if n <= 12:
        result['full_inverse_numerators']=[str(x) for x in v]
    return result


if __name__ == '__main__':
    upper=int(sys.argv[1]) if len(sys.argv)>1 else 14
    path=Path('work/dyadic_wave_experiments.json')
    rows=[]
    for n in range(4,upper+1):
        r=compute(n);rows.append(r)
        path.write_text(json.dumps(rows,indent=2)+'\n')
        print(json.dumps({k:r[k] for k in ['n','M','D','positive_coefficients','negative_coefficients','zero_coefficients']}),flush=True)
        print(json.dumps([{k:v for k,v in s.items() if k!='numerator'} for s in r['samples'][:8]]),flush=True)
