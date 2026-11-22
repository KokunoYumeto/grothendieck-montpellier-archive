"""Independent integer-arithmetic verifier for the finite P-F44 certificate.

Uses no symbolic algebra package and no inverse computation.  The displayed
candidate numerator is checked by polynomial multiplication and monic division.
"""

from itertools import combinations


def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def divide_monic(poly, modulus):
    remainder = list(poly)
    quotient = [0] * max(1, len(poly) - len(modulus) + 1)
    assert modulus[-1] == 1
    while len(remainder) >= len(modulus):
        offset = len(remainder) - len(modulus)
        coefficient = remainder[-1]
        quotient[offset] = coefficient
        for j, entry in enumerate(modulus):
            remainder[offset + j] -= coefficient * entry
        trim(remainder)
    return trim(quotient), trim(remainder)


def multiply(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


N = [
    -1167, 0, 1048, -808, 0, 708, 0, 454,
    0, -708, 254, 0, 0, -708, 100, -340,
    0, 708, -708, 340, -100, 0, 708, 100,
    -354, -340, -708, 708, 100, 100, -694, 100,
    708, -708, 354, -694, 340, -100, -708, 808,
    354, -354, 708, -708, -100, 354, 100, 0,
    -708, 0, -694, 354, 0, 340, 0, -694,
    808, 808, -254, 0, -1048, -100, 808, -708,
]

# Phi_85 = (1+x^5+...+x^80)/(1+x+...+x^16).
numerator = [int(i % 5 == 0) for i in range(81)]
phi, remainder = divide_monic(numerator, [1] * 17)
assert remainder == [0] and len(phi) == 65
weights = [pow(-2, i, 85) for i in range(8)]
residues = [(-sum(weights[i] for i in triple)) % 85
            for triple in combinations(range(8), 3)]
assert len(residues) == 56 and 0 not in residues
denominator = [1]
for exponent in residues:
    factor = [0] * (exponent + 1)
    factor[0], factor[-1] = 1, -1
    _, denominator = divide_monic(multiply(denominator, factor), phi)
_, remainder = divide_monic(multiply(denominator, N), phi)
assert remainder == [17]

sum5 = sum(N[j] for j in range(1, 64) if j % 5 == 0)
sum17 = sum(N[j] for j in range(1, 64) if j % 17 == 0)
sum_other = sum(N[j] for j in range(1, 64) if j % 5 and j % 17)
trace_numerator = 64 * N[0] - 4 * sum5 - 16 * sum17 + sum_other
assert (sum5, sum17, sum_other) == (-2934, 1416, 744)
assert trace_numerator == -84864
assert trace_numerator // 17 == -4992
print({
    "integer_modular_identity": "D*N == 17 mod Phi_85",
    "trace_C1": -4992,
    "K8": "-624/85",
    "scope": "specified primitive Klein contribution, not full B8 or U8",
})
