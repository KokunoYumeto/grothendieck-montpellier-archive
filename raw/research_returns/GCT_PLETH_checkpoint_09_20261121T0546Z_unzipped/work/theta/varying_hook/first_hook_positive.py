#!/usr/bin/env python3
"""T060: first-hook stable plethysm, with explicit positive polytopes.

The formula generator is polynomial in m plus the binary parameter lengths.
The exact coefficient evaluator uses integer parity reduction of a rational
generating function. No character-table or plethysm oracle is used.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import json


def partition(value):
    answer = tuple(value)
    if not answer or any(type(x) is not int or x <= 0 for x in answer):
        raise ValueError("outer label must be a nonempty positive partition")
    if any(answer[i] < answer[i+1] for i in range(len(answer)-1)):
        raise ValueError("outer label must be nonincreasing")
    return answer


def transpose(mu):
    return tuple(sum(x >= j for x in mu) for j in range(1, mu[0]+1))


def cells(mu):
    return tuple((i, j) for i, length in enumerate(mu, 1)
                 for j in range(1, length+1))


def _trim(a):
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y:
                    out[i+j] += x*y
    return _trim(out)


def rational_coefficient(n, numerator, denominator):
    """Exact coefficient by even/odd multiplication, Q(0)=1."""
    if n < 0:
        return 0
    p, q = list(numerator), list(denominator)
    if q[0] != 1:
        raise ValueError("denominator must have constant coefficient one")
    while n:
        qminus = [x if i % 2 == 0 else -x for i, x in enumerate(q)]
        pq = multiply(p, qminus)
        qq = multiply(q, qminus)
        if any(qq[1::2]):
            raise ArithmeticError("even-denominator identity failed")
        p = _trim(pq[n % 2::2] or [0])
        q = _trim(qq[::2])
        n //= 2
    return p[0]


@lru_cache(None)
def denominator(first, m):
    out = [1]
    for degree in range(first, m+1):
        factor = [1]+[0]*degree
        factor[-1] = -1
        out = multiply(out, factor)
    return tuple(out)


@lru_cache(None)
def fake_degree(mu):
    """The q-hook product, computed in degree at most binom(m,2)."""
    mu = partition(mu)
    m = sum(mu)
    bound = m*(m-1)//2
    shift = sum(i*length for i, length in enumerate(mu))
    cap = bound-shift
    f = [1]+[0]*cap
    tr = transpose(mu)
    for i, j in cells(mu):
        hook = mu[i-1]-j+tr[j-1]-i+1
        for d in range(hook, cap+1):
            f[d] += f[d-hook]
    for degree in range(1, m+1):
        for d in range(cap, degree-1, -1):
            f[d] -= f[d-degree]
    if any(x < 0 for x in f):
        raise ArithmeticError("q-hook positivity failed")
    return tuple([0]*shift+f)


@lru_cache(None)
def nontrivial_numerator(nu):
    nu = partition(nu)
    if len(nu) == 1:
        raise ValueError("the trivial label uses the Koszul cells")
    m = sum(nu)
    f = fake_degree(nu)
    out = [0]*(m*(m-1)//2+2)
    for i, j in cells(nu):
        if (i, j) in ((1, 1), (2, 1)):
            continue
        shift = j-i+1
        for degree, value in enumerate(f):
            if value:
                if not 0 <= degree+shift < len(out):
                    raise ArithmeticError("numerator degree escaped its proved bound")
                out[degree+shift] += value
    return tuple(_trim(out))


def parameters(m, a, t, n, mu):
    if any(type(x) is not int for x in (m, a, t, n)):
        raise ValueError("parameters must be integers")
    if m < 4 or a < 1 or t < 0 or n < a+t:
        raise ValueError("require m>=4, a>=1, t>=0, n>=a+t")
    mu = partition(mu)
    if sum(mu) != m:
        raise ValueError("outer label must partition m")
    nu = transpose(mu) if t % 2 else mu
    lam = (m*n-a-(m-1)*t-1, a+t, t+1)+(t,)*(m-3)
    if any(lam[i] < lam[i+1] for i in range(m-1)) or sum(lam) != m*n:
        raise ArithmeticError("shape identity failed")
    return mu, nu, lam


def coefficient(m, a, t=0, n=None, mu=None):
    if n is None:
        n = a+t
    if mu is None:
        mu = (m,)
    _, nu, _ = parameters(m, a, t, n, mu)
    degree = a+1
    if len(nu) != 1:
        return rational_coefficient(degree, nontrivial_numerator(nu),
                                    denominator(2, m))
    return sum(rational_coefficient(degree-i-j, (1,), denominator(i, m))
               for i in range(2, m) for j in range(i+1, m+1))


def support(m, a, t=0, n=None, mu=None):
    if n is None:
        n = a+t
    if mu is None:
        mu = (m,)
    _, nu, _ = parameters(m, a, t, n, mu)
    if len(nu) == 1:
        threshold = 5
    else:
        base = sum(i*length for i, length in enumerate(nu))
        weight = min(j-i+1 for i, j in cells(nu)
                     if (i, j) not in ((1, 1), (2, 1)))
        threshold = base+weight
    return {"positive": a+1 >= threshold, "minimum_total_degree": threshold,
            "effective_label": nu}


def _polytope(weights, rhs, multiplicity, tag):
    if rhs < 0 or multiplicity <= 0:
        return None
    names = [f"u{w}" for w in weights]
    selector = multiplicity != 1
    if selector:
        names.append("y")
    dim = len(names)
    inequalities = []
    bounds = []
    for j in range(dim):
        row = [0]*dim
        row[j] = -1
        inequalities.append(row)
        bounds.append(0)
    if selector:
        row = [0]*dim
        row[-1] = 1
        inequalities.append(row)
        bounds.append(multiplicity-1)
    return {"tag": tag, "variables": names,
            "equalities": [list(weights)+([0] if selector else [])],
            "equality_bounds": [rhs], "inequalities": inequalities,
            "inequality_bounds": bounds, "convention": "A z <= b; E z = f"}


def polytopes(m, a, t=0, n=None, mu=None):
    if n is None:
        n = a+t
    if mu is None:
        mu = (m,)
    outer, nu, lam = parameters(m, a, t, n, mu)
    degree = a+1
    pieces = []
    if len(nu) != 1:
        for shift, value in enumerate(nontrivial_numerator(nu)):
            piece = _polytope(tuple(range(2, m+1)), degree-shift, value,
                              {"numerator_degree": shift})
            if piece is not None:
                pieces.append(piece)
    else:
        for i in range(2, m):
            for j in range(i+1, m+1):
                piece = _polytope(tuple(range(i, m+1)), degree-i-j, 1,
                                  {"least_support": i, "other_basis_index": j})
                if piece is not None:
                    pieces.append(piece)
    return {"statement": "T-060", "outer": outer, "effective_label": nu,
            "inner": n, "partition": lam, "support": support(m,a,t,n,mu),
            "polytopes": pieces}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--m', type=int, required=True)
    p.add_argument('--a', type=int, required=True)
    p.add_argument('--t', type=int, default=0)
    p.add_argument('--n', type=int)
    p.add_argument('--outer')
    p.add_argument('--polytopes', action='store_true')
    args = p.parse_args()
    mu = tuple(map(int,args.outer.split(','))) if args.outer else (args.m,)
    result = {"coefficient": coefficient(args.m,args.a,args.t,args.n,mu),
              "support": support(args.m,args.a,args.t,args.n,mu)}
    if args.polytopes:
        result['formula'] = polytopes(args.m,args.a,args.t,args.n,mu)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
