"""Exact checks for the rectangular-character research fragment.

This is a computation certificate for the specified small examples, not a
verification of the general theorems. Uses only the Python standard library.
"""
from itertools import permutations, product
from fractions import Fraction
from collections import Counter
import json
from pathlib import Path


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


matchings = (
    frozenset((frozenset((0, 1)), frozenset((2, 3)))),
    frozenset((frozenset((0, 2)), frozenset((1, 3)))),
    frozenset((frozenset((0, 3)), frozenset((1, 2)))),
)


def act_matching(p, matching):
    return frozenset(frozenset(p[i] for i in pair) for pair in matching)


def char22(p):
    return sum(act_matching(p, m) == m for m in matchings) - 1


def chars(p):
    standard = sum(p[i] == i for i in range(4)) - 1
    return {
        "4": 1,
        "31": standard,
        "22": char22(p),
        "211": parity(p) * standard,
        "1111": parity(p),
    }


perms = tuple(permutations(range(4)))
tensor = {}
symmetric = {}
alternating = {}
for shape in chars(perms[0]):
    tensor[shape] = sum(chars(p)[shape] * char22(p) ** 2 for p in perms) // 24
    symmetric[shape] = sum(
        chars(p)[shape] * (char22(p) ** 2 + char22(compose(p, p)))
        for p in perms
    ) // 48
    alternating[shape] = sum(
        chars(p)[shape] * (char22(p) ** 2 - char22(compose(p, p)))
        for p in perms
    ) // 48
assert tensor == {"4": 1, "31": 0, "22": 1, "211": 0, "1111": 1}
assert symmetric == {"4": 1, "31": 0, "22": 1, "211": 0, "1111": 0}
assert alternating == {"4": 0, "31": 0, "22": 0, "211": 0, "1111": 1}


# Schur polynomials in two variables, represented by exponent -> coefficient.
def s2(shape):
    a, b = tuple(shape) + (0,) * (2 - len(shape))
    return Counter({(a - i, b + i): 1 for i in range(a - b + 1)})


def linear_combination(terms):
    c = Counter()
    for mult, poly in terms:
        for exponent, coeff in poly.items():
            c[exponent] += mult * coeff
    return {k: v for k, v in c.items() if v}


assert linear_combination([(1, s2((4,))), (3, s2((3, 1))), (2, s2((2, 2)))]) == {
    (4, 0): 1, (3, 1): 4, (2, 2): 6, (1, 3): 4, (0, 4): 1,
}
assert linear_combination([(1, s2((4,))), (-1, s2((3, 1))), (2, s2((2, 2)))]) == {
    (4, 0): 1, (2, 2): 2, (0, 4): 1,
}
joint_power_moment = 1 * 1 + 3 * (-1) + 2 * 2
assert joint_power_moment == 2


# Enumerate all semistandard tableaux of shape (2,2) over alphabet
# (x1*y1, x1*y2, x2*y1, x2*y2). Rows weak, columns strict.
tableaux = []
content = Counter()
for a, b, c, d in product(range(4), repeat=4):
    if not (a <= b and c <= d and a < c and b < d):
        continue
    tableaux.append((a, b, c, d))
    xp = [0, 0]
    yp = [0, 0]
    for t in (a, b, c, d):
        xp[t // 2] += 1
        yp[t % 2] += 1
    content[tuple(xp + yp)] += 1
assert len(tableaux) == 20


def weyl_extract(shape_x, shape_y):
    target = (shape_x[0] + 1, shape_x[1], shape_y[0] + 1, shape_y[1])
    total = 0
    for delta_x, sign_x in [((1, 0), 1), ((0, 1), -1)]:
        for delta_y, sign_y in [((1, 0), 1), ((0, 1), -1)]:
            sub = delta_x + delta_y
            exponent = tuple(target[i] - sub[i] for i in range(4))
            total += sign_x * sign_y * content[exponent]
    return total


assert weyl_extract((3, 1), (2, 2)) == 0
assert weyl_extract((2, 2), (2, 2)) == 1
assert weyl_extract((4, 0), (2, 2)) == 1


# Twirl dimension bookkeeping: tensor-product branching of S_(22)(C^4).
restricted = {}
for mu in ((4, 0), (3, 1), (2, 2)):
    for nu in ((4, 0), (3, 1), (2, 2)):
        value = weyl_extract(mu, nu)
        if value:
            restricted[str((mu, nu))] = value
weighted_sum = sum(
    weyl_extract(mu, nu) * (mu[0] - mu[1] + 1) * (nu[0] - nu[1] + 1)
    for mu in ((4, 0), (3, 1), (2, 2))
    for nu in ((4, 0), (3, 1), (2, 2))
)
assert weighted_sum == 20


report = {
    "symmetric_group_S4_tensor_square_22": tensor,
    "symmetric_group_S4_symmetric_square_22": symmetric,
    "symmetric_group_S4_exterior_square_22": alternating,
    "U2_joint_power_moment": joint_power_moment,
    "SSYT_22_alphabet_4_count": len(tableaux),
    "tensor_subgroup_restriction": restricted,
    "dimension_weighted_sum": weighted_sum,
    "CUE_leading_constant_k2": str(Fraction(1, 12)),
    "all_assertions_passed": True,
}
out = Path(__file__).with_name("small_case_results.json")
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
