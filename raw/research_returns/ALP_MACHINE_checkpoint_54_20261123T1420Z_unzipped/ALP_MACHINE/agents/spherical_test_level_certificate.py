"""Exact finite certificates for ALP-LIFT-16 S24-S25 and split S5 constants.

This checks finite integer arithmetic and low-rank transform coefficients.
It is not a formal verification of the analytic or global theorem.
"""
from fractions import Fraction
from math import factorial
import json

def vp(x, p):
    out = 0
    while x and x % p == 0:
        out += 1
        x //= p
    return out

assert pow(29, 10, 121) == 89
assert next(n for n in range(1, 11) if pow(29, n, 11) == 1) == 10

for n in range(1, 301):
    direct = 6 * sum(vp(pow(29, i) - 1, 11) for i in range(1, n + 1))
    r = n // 10
    expected = 6 * (r + vp(factorial(r), 11))
    assert direct == expected, (n, direct, expected)

# The integral GL_n(O/p^l) count and rational-product form coincide.
for n in range(1, 9):
    gln = 1
    for i in range(n):
        gln *= pow(29, n) - pow(29, i)
    for e in range(1, 5):
        direct = pow(29, 6*n*n*(2*e-1)) * gln**6
        product = Fraction(pow(29, 12*e*n*n))
        for i in range(1, n+1):
            product *= Fraction(pow(29, i)-1, pow(29, i))**6
        assert product.denominator == 1
        assert direct == product.numerator
        assert vp(direct, 11) == 6*((n//10)+vp(factorial(n//10),11))

# Independent rank-two, trivial-representation Cartan check of S11.
# vol(K diag(pi^l1,pi^l2) K) is 1 if l1=l2,
# and q^(l1-l2)*(1+q^-1) otherwise.
# R(T)=(1-T^2)(1-q*T^2)/((1-q*T)^2(1-T)^2).
for q in (2, 3, 7, 29):
    cutoff = 16
    cartan = [Fraction(0) for _ in range(cutoff+1)]
    for l1 in range(-cutoff, cutoff+1):
        for l2 in range(-cutoff, l1+1):
            r = abs(l1)+abs(l2)
            if r <= cutoff:
                cartan[r] += 1 if l1 == l2 else Fraction(pow(q,l1-l2)*(q+1),q)
    denominator_inverse = []
    for n in range(cutoff+1):
        denominator_inverse.append(sum((i+1)*pow(q,i)*(n-i+1) for i in range(n+1)))
    rhs = []
    for n in range(cutoff+1):
        value = denominator_inverse[n]
        if n >= 2:
            value -= (q+1)*denominator_inverse[n-2]
        if n >= 4:
            value += q*denominator_inverse[n-4]
        rhs.append(Fraction(value))
    assert cartan == rhs, q

print(json.dumps({
    "status": "PASS",
    "valuation_ranks_checked": [1,300],
    "index_ranks_checked": [1,8],
    "index_depths_checked": [1,4],
    "rank_two_cartan_q": [2,3,7,29],
    "rank_two_series_degree": 16,
    "v11_examples": {str(n): 6*((n//10)+vp(factorial(n//10),11))
                     for n in (6,20,34,48,62,100,120)}
}, indent=2))

