#!/usr/bin/env python3
"""Exact constant certificate for D-UNW-01--03; no numerical character scan.

All calculations use integers/Fraction. Universal inequalities are reduced
to their written monotonic endpoint or to the displayed polynomial identity.
This is not a substitute for the published character inputs or proof review.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
sigma0 = F(1, 10**29)
J = 10**30
N = 10**61
C = 2**14 * 10**12
gamma = F(1, 2**13 * 10**12)
sigma = F(1, 6507 * 2**21 * 10**18)
assert 9*C == (3 * 2**7 * 10**6)**2
assert sigma == F(1, 241 * (3 * 2**7 * 10**6)**3)
assert sigma < gamma/82
assert sigma > 7*sigma0 > sigma0
assert N >= J*J + J + 8 and N > 2*J
assert sigma0*J/4 == F(5, 2)
# 2^(-5/2)<1/4 follows after positive squaring from 32>16.
assert 2**5 > 4**2

# q^3-2(q+1)=(q-2)(q^2+2q+2)+2, q>=2.
# q^2-(q+1)=(q-2)(q+1)+1, q>=2.
def mul(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for k,y in enumerate(b):
            out[i+k] += x*y
    return out
p = mul([-2,1],[2,2,1]); p[0] += 2
assert p == [-2,-2,0,1]
p = mul([-2,1],[1,1]); p[0] += 1
assert p == [-1,-1,1]

# Exponents in the two regimes: nj/2-3 >= nj/4 for nj>=12;
# n^2/4-4 >= n^2/8 for n>=8.
assert F(12,2)-3 == F(12,4)
assert F(8**2,4)-4 >= F(8**2,8)
# For 2<=j<=n/2, j(n-j)-2(n-2)=(j-2)(n-j-2)>=0.
for n in range(8, 40):
    for j in range(2, n//2+1):
        assert j*(n-j)-2*(n-2) == (j-2)*(n-j-2) >= 0
assert 2*8-7 > 8
assert F(8**2,4)-4 > 8
# The relevant polynomial n^2/4-n-4 increases for n>=8.
assert F(2*8+1,4)-1 > 0

# R_j<=5q^(j^2): 16.52=413/25<25 and j^2-j+1>0.
assert F(413,25) < 25
assert 2**2-2+1 > 0
# j^2-j+1 = (j-1)^2+j, positive at every integer j>=2.
for j in range(2, 16):
    assert j*j-j+1 == (j-1)**2+j
    assert (j-1)**2+j > 0

u = F(1,256)
d = 2*u+10*u*u
assert d == F(261,32768) < F(1,100)
ratio = (F(1,4)+F(1,100))/(1-F(1,100))
assert ratio == F(26,99) < F(4,15)
support = (1-F(4,15))/4
assert support == F(11,60) < F(1,4)
assert 12*support - 2 == F(1,5)
assert F(6,1)/(12*support-2) == 30
assert 2**8 > 30

result = {
    "status": "PASS",
    "scope": "exact numerical and polynomial reductions; no character-table or generic-model enumeration",
    "sigma_source": str(sigma), "sigma0": str(sigma0),
    "J": str(J), "natural_dimension_cutoff": str(N),
    "low_level_error": str(d), "low_level_ratio": str(ratio),
    "uniform_ratio": "4/15", "normalizer_support": str(support),
    "total_degree_upper_bound": 30,
    "published_inputs": {
        "LT2024_author_sha256": "70d2546d2a0f01f8e701aa718201216f2b334b6cd074c12b41c2c59e0b7cdd4f",
        "GLT2020_published_sha256": "0726271e666bd5eb736ff91ea031ef83bb072f2e10f27b664c217d7702926c32"
    }
}
(HERE/"constants_checked.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
