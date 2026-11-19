"""Exact rational certificates for the estimates in the E2* zero proof.

The classical rational inequalities pi > 157/50 and pi < 22/7 are
used explicitly.  No floating-point output is used by these checks.
"""
from fractions import Fraction as Q
from math import factorial
import time

start = time.perf_counter()
r = Q(1, 200)
s3 = r * (1 + 4*r + r*r) / (1-r)**4
exp_lower = sum(Q(27, 5)**k / factorial(k) for k in range(14))
assert Q(173, 100)**2 < 3
assert Q(157, 50) * Q(173, 100) > Q(27, 5)
assert exp_lower > 200
assert s3 / r < 2
assert s3 < Q(1, 180)
assert Q(22, 7)**2 < 15
print('S3(1/200) =', s3)
print('S3(1/200)/(1/200) =', s3/r, '< 2')
print('S3(1/200) < 1/180:', s3 < Q(1, 180))
print('exp(27/5) > Taylor polynomial of degree 13 =', exp_lower, '> 200')
print('pi * sqrt(3) > (157/50)*(173/100) > 27/5')
print('pi^2 < (22/7)^2 < 15')
print('All six rational checks passed.')
print('Runtime seconds:', round(time.perf_counter()-start, 6))
