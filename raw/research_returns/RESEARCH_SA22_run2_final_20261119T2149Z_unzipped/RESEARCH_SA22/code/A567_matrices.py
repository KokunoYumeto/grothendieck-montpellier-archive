#!/usr/bin/env python3
"""Exact finite certificates for cote 67/050 and the A.2(a) examples.

Uses only the Python standard library. The group presentations are proved
in the paper; this checks the displayed matrices and rational witnesses.
Run: python3 code/A567_matrices.py > logs/A567_matrices.json
"""
from fractions import Fraction
from itertools import product, permutations
import json
from time import perf_counter

started = perf_counter()
I = ((1, 0), (0, 1))
minus_I = ((-1, 0), (0, -1))


def mul(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def power(a, n):
    out = I
    for _ in range(n):
        out = mul(out, a)
    return out


def det(a):
    return a[0][0]*a[1][1] - a[0][1]*a[1][0]


S = ((0, -1), (1, 0))
T = ((1, 1), (0, 1))
R = mul(S, T)
r1 = ((-1, 0), (0, 1))
r2 = ((0, 1), (1, 0))
r3 = ((1, 1), (0, -1))
checks = {
    "S_squared_equals_minus_I": power(S, 2) == minus_I,
    "R_cubed_equals_minus_I": power(R, 3) == minus_I,
    "R_sixth_equals_I": power(R, 6) == I,
    "r1_r2_equals_S": mul(r1, r2) == S,
    "r2_r3_equals_R": mul(r2, r3) == R,
    "all_ri_involutions": all(power(r, 2) == I for r in (r1, r2, r3)),
    "all_ri_determinant_minus_one": all(det(r) == -1 for r in (r1, r2, r3)),
    "r2_conjugates_S_to_inverse": mul(mul(r2, S), r2) == power(S, 3),
    "r2_conjugates_R_to_inverse": mul(mul(r2, R), r2) == power(R, 5),
}
assert all(checks.values())

# All linear and affine transformations of F_2^2, with no group-theory
# library.  Permutations are stored as the images of the four points.
points = list(product(range(2), repeat=2))
linear = [((a, b), (c, d)) for a, b, c, d in product(range(2), repeat=4)
          if (a*d-b*c) % 2 == 1]


def affine_permutation(matrix, shift):
    images = [tuple((sum(matrix[i][j]*p[j] for j in range(2))
                     + shift[i]) % 2 for i in range(2)) for p in points]
    return tuple(points.index(p) for p in images)


linear_permutations = {affine_permutation(m, (0, 0)) for m in linear}
affine_permutations = {affine_permutation(m, v) for m in linear for v in points}
translations = {affine_permutation(I, v) for v in points}
all_s4 = set(permutations(range(4)))
Smod2 = tuple(tuple(x % 2 for x in row) for row in S)
Rmod2 = tuple(tuple(x % 2 for x in row) for row in R)


def compose(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def generated_permutations(generators):
    group = {tuple(range(len(generators[0])))}
    while True:
        larger = group | {compose(a, b) for a in group for b in generators}
        if larger == group:
            return group
        group = larger


finite_checks = {
    "SL2_F2_order_6": len(linear) == 6,
    "linear_action_faithful": len(linear_permutations) == 6,
    "AGL2_F2_is_all_S4": affine_permutations == all_s4,
    "translations_order_4": len(translations) == 4,
    "zero_stabilizer_is_linear_group": {
        p for p in affine_permutations if p[0] == 0} == linear_permutations,
    "S_R_mod2_generate_SL2_F2": generated_permutations([
        affine_permutation(Smod2, (0, 0)),
        affine_permutation(Rmod2, (0, 0))]) == linear_permutations,
}
assert all(finite_checks.values())


def cap_a(lambdas):
    a, b, c = lambdas
    return Fraction(1+a*a+b*b-c*c, 2*(1+a*a))


examples = [(1, 1, 1), (1, 2, 1)]
coefficients = [cap_a(x) for x in examples]
assert coefficients == [Fraction(1, 2), Fraction(5, 4)]
# Boundary components for (P1-{0,1,infinity})^2 and the blowup at (0,0).
boundary = [(axis, p) for axis in ("horizontal", "vertical")
            for p in ("0", "1", "infinity")]
blown_up_boundary = boundary + [("exceptional", "(0,0)")]
assert len(boundary) == 6 and len(blown_up_boundary) == 7
print(json.dumps({
    "certificate": "exact integer and rational arithmetic",
    "matrices": {"S": S, "T": T, "R": R, "r1": r1, "r2": r2, "r3": r3},
    "checks": checks,
    "F2_points": points,
    "SL2_F2_matrices": linear,
    "SL2_F2_order": len(linear),
    "AGL2_F2_order": len(affine_permutations),
    "finite_affine_checks": finite_checks,
    "cap_examples_lambda": examples,
    "cap_quadratic_to_linear_ratios": [str(q) for q in coefficients],
    "compactification_boundary_components": boundary,
    "blowup_boundary_components": blown_up_boundary,
    "runtime_seconds": perf_counter()-started,
}, indent=2))
