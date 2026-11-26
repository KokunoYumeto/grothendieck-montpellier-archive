#!/usr/bin/env python3
"""Exact finite calculations only; no point-section equality is inferred by code."""
from collections import Counter
from itertools import product
import json

exponents = [pow(3, j, 20) for j in range(4)]
degrees = {}
for m in range(1, 5):
    c = Counter(sum(v) % 20 for v in product(exponents, repeat=m))
    degrees[str(m)] = {"residues": sorted(c), "zero_multiplicity": c[0]}
    if m <= 3:
        assert c[0] == 0
assert degrees["4"]["zero_multiplicity"] > 0

q = 11
def mul(x, y):
    # F_121 = F_11[s]/(s^2-2); 2 is a nonsquare modulo 11.
    return ((x[0]*y[0] + 2*x[1]*y[1]) % q,
            (x[0]*y[1] + x[1]*y[0]) % q)
def power(x, n):
    z = (1, 0)
    while n:
        if n & 1:
            z = mul(z, x)
        x = mul(x, x)
        n //= 2
    return z
assert pow(2, (q-1)//2, q) == q-1
def quadratic_character(x):
    if x == (0, 0):
        return 0
    y = power(x, (q*q-1)//2)
    assert y in [(1, 0), (q-1, 0)]
    return 1 if y == (1, 0) else -1
n1 = 1 + sum(1 + (0 if (1+4*pow(u, 5, q)) % q == 0 else
                  (1 if pow((1+4*pow(u, 5, q)) % q, (q-1)//2, q) == 1 else -1))
             for u in range(q))
n2 = 1
for u in product(range(q), repeat=2):
    v = power(u, 5)
    disc = ((1+4*v[0]) % q, 4*v[1] % q)
    n2 += 1 + quadratic_character(disc)
a1 = q + 1 - n1
numerator = a1*a1 - (q*q + 1 - n2)
assert numerator % 2 == 0
a2 = numerator // 2
charpoly = [q*q, -q*a1, a2, -a1, 1]  # ascending powers
coeff = [c % 3 for c in charpoly]
companion = [[0]*4 for _ in range(4)]
for j in range(3):
    companion[j+1][j] = 1
for i in range(4):
    companion[i][3] = -coeff[i] % 3
def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(4)) % 3
             for j in range(4)] for i in range(4)]
identity = [[int(i == j) for j in range(4)] for i in range(4)]
z = identity
order = None
for i in range(1, 81):
    z = mm(z, companion)
    if z == identity:
        order = i
        break
assert order == 20
assert n1 == 13 and n2 == 103
assert charpoly == [121, 11, -9, 1, 1]

counts = {}
for a in [5, 7]:
    chars = [(i,j) for i in range(1,a) for j in range(1,a) if (i+j)%a]
    opposite = sum(1 for i,x in enumerate(chars) for y in chars[i+1:]
                   if (x[0]+y[0])%a == 0 and (x[1]+y[1])%a == 0)
    assert opposite == (a-1)*(a-2)//2
    intersections = [(r,s) for r in range(a) for s in range(a)
                     if (r+s)%a == (s-2*r)%a == (r-2*s)%a]
    assert intersections == [(0,0)]
    counts[str(a)] = {"H1_character_count":len(chars),
                       "diagonal_invariant_wedge_rank":opposite,
                       "diagonal_invariant_L2_rank":opposite-1,
                       "equal_three_quotient_weights":intersections}

out = {"status":"PASS", "method":"integer and finite-field arithmetic only",
       "Frobenius_order":20, "F81_embedding_exponents_mod20":exponents,
       "tensor_degrees":degrees,
       "prime_11":{"A_point_count":n1,"A_point_count_quadratic":n2,
                   "Weil_polynomial_ascending":charpoly,
                   "Weil_polynomial_mod3_ascending":coeff,
                   "residual_companion_order":order},
       "symmetry_checks":counts,
       "arithmetic_density":{"order20_elements":8,"total_residual_group_order":80,
                              "reduced_fraction":[1,10]},
       "scope":"No code claim of full pro-three collision; see mathematical proof."}
print(json.dumps(out, indent=2))
