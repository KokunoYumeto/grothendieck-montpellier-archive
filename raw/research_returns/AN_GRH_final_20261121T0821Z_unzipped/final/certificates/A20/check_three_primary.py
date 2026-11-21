"""Exact arithmetic for A20; standard library only."""
from pathlib import Path
import itertools
import json

def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

def matrix_power(a, n):
    out = [[int(i == j) for j in range(4)] for i in range(4)]
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n //= 2
    return out

def determinant(a):
    out = 0
    for p in itertools.permutations(range(4)):
        sign = (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))
        term = sign
        for i in range(4):
            term *= a[i][p[i]]
        out += term
    return out

def main():
    cp = [[0,0,0,-4],[1,0,0,-2],[0,1,0,0],[0,0,1,-1]]
    a = matrix_power(cp, 20)
    identity_mod3 = all((a[i][j] - int(i == j)) % 3 == 0 for i in range(4) for j in range(4))
    assert identity_mod3
    n = determinant([[int(i == j)-a[i][j] for j in range(4)] for i in range(4)])
    assert n == 1099812538656
    v = 0
    cofactor = n
    while cofactor % 3 == 0:
        cofactor //= 3
        v += 1
    assert v == 4 and cofactor == 13577932576 and cofactor % 3 == 1
    p = [4,2,0,1,1]
    q = [-1,-1,-1,0,-1,1,-1,0,0,0,1,1,1,0,1,-1,1]
    product = [0]*21
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            product[i+j] = (product[i+j]+x*y) % 3
    target = [2]+[0]*19+[1]
    assert product == target
    result = dict(status='PASS', scope='Finite arithmetic only; geometric conclusion uses A19 and A10',
                  frobenius_polynomial_ascending=p, exponent=20, frobenius_power_mod3_is_identity=True,
                  jacobian_order=n, valuation_at_3=v, cofactor=cofactor,
                  quotient_polynomial_ascending_mod3=[x % 3 for x in q],
                  companion_power=a)
    Path(__file__).with_name('three_primary_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    main()
