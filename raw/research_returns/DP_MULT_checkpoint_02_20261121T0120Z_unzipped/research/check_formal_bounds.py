#!/usr/bin/env python3
"""Finite exact-arithmetic checks, not a formal proof.

Use the Lubin--Tate p-series p*T+T**q and compute the logarithm from
L([p](T))=p*L(T), then the invariant vector field 1/L'(T).
All arithmetic is rational and all valuations are exact.
"""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import csv

OUT = Path(__file__).resolve().parent

def vp(x, p):
    if not x:
        return 10**9
    x = Fraction(x)
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % p == 0:
        a //= p
        v += 1
    while b % p == 0:
        b //= p
        v -= 1
    return v

def floor_bound(n, p, h):
    ans, j, power = 0, 1, p
    while power <= n:
        if j % h:
            ans += n // power
        j += 1
        power *= p
    return ans

def ceiling(x):
    return -((-x.numerator) // x.denominator)

def case(p, h, N):
    q = p**h
    log = [Fraction(0)] * (N+1)
    log[1] = Fraction(1)
    for n in range(2, N+1):
        rhs = Fraction(int(n == q))
        for j in range(2, n):
            gap = n-j
            if gap % (q-1):
                continue
            k = gap // (q-1)
            if k <= j:
                rhs += log[j] * comb(j, k) * p**(j-k)
        log[n] = rhs / (p-p**n)
    deriv = [(j+1)*log[j+1] for j in range(N)]
    vec = [Fraction(0)] * N
    vec[0] = Fraction(1)
    for n in range(1, N):
        vec[n] = -sum(deriv[j]*vec[n-j] for j in range(1,n+1))
    assert all(vp(x,p) >= 0 for x in vec)
    c = Fraction(1,p-1)-Fraction(1,q-1)
    prev = [Fraction(0)]*(N+1)
    prev[0] = Fraction(1)
    rows = []
    for n in range(1, N+1):
        row = [Fraction(0)]*(N+1)
        for m in range(1,n+1):
            row[m] = m*sum(vec[j]*prev[m-1+j] for j in range(n-m+1))
        actual = min(vp(x,p) for x in row if x)
        E = floor_bound(n,p,h)
        C = max(0,ceiling(c*n-(h-1)))
        assert actual >= max(E,C), (p,h,n,actual,E,C)
        power, j = 1, 0
        while power < n:
            power *= p
            j += 1
        witness = ""
        if power == n:
            m = p**(j % h)
            assert vp(row[m],p) == E, (p,h,n,m,vp(row[m],p),E)
            witness = f"t^{m} attains E_h(n)"
        if n == q-1:
            assert vp(row[n],p) == c*n-(h-1)
            witness += "; t^n attains affine bound"
        rows.append([p,h,n,E,C,actual,witness])
        prev = row
    return rows

def main():
    cases = [(2,1,32),(2,2,64),(2,3,32),(3,2,32),(3,3,32),(5,2,32)]
    rows = []
    for p,h,N in cases:
        rows.extend(case(p,h,N))
    with (OUT/'formal_bound_computation.tsv').open('w',newline='') as f:
        writer=csv.writer(f,delimiter='\t')
        writer.writerow(['p','h','derivative_order','floor_sum_bound','affine_bound_rounded','minimum_on_monomials','sharpness_witness'])
        writer.writerows(rows)
    print(f'PASS: {len(rows)} derivative orders in {len(cases)} finite Lubin--Tate examples; exact Fraction arithmetic.')
    print('All available p-power witnesses and q-1 affine-intercept witnesses passed. This is not a formal certificate.')

if __name__ == '__main__':
    main()
