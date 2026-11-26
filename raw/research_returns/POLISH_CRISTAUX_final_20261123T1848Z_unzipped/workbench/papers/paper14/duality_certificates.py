#!/usr/bin/env python3
"""Hasse and determinant duality certificates (Python 3, standard library).

Finite corroboration of the paper's symbolic identities, not general proofs.
The exterior calculation multiplies in the full integer polynomial exterior
algebra; the ring calculation uses Leibniz determinants and cofactor inverses
in dual-number rings, including nonzero nilpotent coefficients.

Public domain under CC0 1.0.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations
from math import factorial
from pathlib import Path
import hashlib
import json
import random


def permutation_sign(sequence):
    inversions = sum(sequence[i] > sequence[j]
                     for i in range(len(sequence))
                     for j in range(i + 1, len(sequence)))
    return -1 if inversions % 2 else 1


def epsilon(dimension):
    return (-1) ** (dimension * (dimension + 1) // 2)


def exterior_top_polynomial(dimension):
    """Expand (-sum B_ij w_i wedge q_j)^g/g!, keeping every monomial."""
    terms = {(0, ()): 1}
    for _ in range(dimension):
        product = defaultdict(int)
        for (mask, monomial), coefficient in terms.items():
            for i in range(dimension):
                for j in range(dimension):
                    a, b = i, dimension + j
                    new_bits = (1 << a) | (1 << b)
                    if mask & new_bits:
                        continue
                    inversions = ((mask >> (a + 1)).bit_count()
                                  + (mask >> (b + 1)).bit_count())
                    key = (mask | new_bits,
                           tuple(sorted(monomial + (i * dimension + j,))))
                    product[key] -= coefficient * (-1) ** inversions
        terms = {key: value for key, value in product.items() if value}
    full_mask = (1 << (2 * dimension)) - 1
    result = {}
    for (mask, monomial), coefficient in terms.items():
        assert mask == full_mask
        assert coefficient % factorial(dimension) == 0
        result[monomial] = coefficient // factorial(dimension)
    return result


def check_exterior_identities():
    records = []
    for g in range(1, 7):
        expansion = exterior_top_polynomial(g)
        determinant = {tuple(i * g + perm[i] for i in range(g)):
                       permutation_sign(perm)
                       for perm in permutations(range(g))}
        assert expansion == {key: epsilon(g) * value
                             for key, value in determinant.items()}
        records.append({"dimension": g, "monomials": len(expansion),
                        "epsilon": epsilon(g), "passed": True})
    shuffles = []
    for g in range(1, 9):
        for h in range(1, 9):
            order = (list(range(g)) + list(range(g + h, 2 * g + h))
                     + list(range(g, g + h))
                     + list(range(2 * g + h, 2 * (g + h))))
            sign = permutation_sign(order)
            assert sign == (-1) ** (g * h)
            assert epsilon(g + h) == sign * epsilon(g) * epsilon(h)
            shuffles.append({"g": g, "h": h, "sign": sign})
    cancellations = []
    for p in (2, 3, 5):
        # Dimension two, B=pI and a principal product polarization scaled by p.
        det_b = p * p
        delta = p * p
        beta = epsilon(2) * Fraction(delta, det_b)
        assert beta.denominator == 1 and beta.numerator == -1
        cancellations.append({"p": p, "det_B": det_b, "delta": delta,
                              "integral_beta": int(beta), "mod_p": int(beta) % p})
    return {"method": "Full exterior multiplication over the integer polynomial ring",
            "dimensions": records, "product_shuffles": shuffles,
            "divisible_degree_cancellations": cancellations}


def dual_add(x, y, prime):
    return ((x[0] + y[0]) % prime, (x[1] + y[1]) % prime)


def dual_neg(x, prime):
    return (-x[0] % prime, -x[1] % prime)


def dual_mul(x, y, prime):
    return (x[0] * y[0] % prime,
            (x[0] * y[1] + x[1] * y[0]) % prime)


def dual_determinant(matrix, prime):
    result = (0, 0)
    for perm in permutations(range(len(matrix))):
        term = (1, 0)
        for i, j in enumerate(perm):
            term = dual_mul(term, matrix[i][j], prime)
        if permutation_sign(perm) < 0:
            term = dual_neg(term, prime)
        result = dual_add(result, term, prime)
    return result


def check_dual_number_minors():
    rng = random.Random(202611230651)
    records = []
    for prime in (2, 3, 5, 7):
        for g in (1, 2, 3):
            nilpotent_count = 0
            for case in range(12):
                n = 2 * g
                matrix = [[(int(i == j), 0) for j in range(n)]
                          for i in range(n)]
                for _ in range(8 * n):
                    i, j = rng.sample(range(n), 2)
                    coefficient = (rng.randrange(prime), rng.randrange(prime))
                    matrix[i] = [dual_add(matrix[i][k],
                                          dual_mul(coefficient, matrix[j][k], prime),
                                          prime) for k in range(n)]
                assert dual_determinant(matrix, prime) == (1, 0)
                inverse_block = []
                for i in range(g):
                    row = []
                    for j in range(g):
                        # The inverse entry (i,j) is cofactor (j,i), since det=1.
                        minor = [[matrix[r][c] for c in range(n) if c != i]
                                 for r in range(n) if r != j]
                        value = dual_determinant(minor, prime)
                        row.append(value if (i + j) % 2 == 0
                                   else dual_neg(value, prime))
                    inverse_block.append(row)
                lhs = dual_determinant(inverse_block, prime)
                rhs = dual_determinant([row[g:] for row in matrix[g:]], prime)
                assert lhs == rhs, (prime, g, case, lhs, rhs)
                nilpotent_count += int(rhs[1] != 0)
            records.append({"p": prime, "g": g, "cases": 12,
                            "nonzero_nilpotent_determinants": nilpotent_count,
                            "passed": True})
    return {"method": "Leibniz determinants and adjugate inverse over F_p[epsilon]/epsilon^2",
            "cases": records,
            "total_cases": sum(item["cases"] for item in records),
            "nonzero_nilpotent_determinants":
                sum(item["nonzero_nilpotent_determinants"] for item in records)}


def main():
    result = {"name": "Hasse and determinant duality certificates",
              "exterior": check_exterior_identities(),
              "minors": check_dual_number_minors(),
              "passed": True, "finite_corroboration_only": True,
              "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"passed": True, "symbolic_dimensions": 6,
                      "product_shuffles": 64, "dual_number_cases": 144,
                      "nonzero_nilpotent_determinants":
                          result["minors"]["nonzero_nilpotent_determinants"]}))


if __name__ == "__main__":
    main()
