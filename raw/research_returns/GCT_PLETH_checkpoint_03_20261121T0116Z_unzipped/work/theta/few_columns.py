"""Exact finite exterior-character certificates in ranks five and six.

For U=Lambda^3 C^rank, the character of Lambda(U) is the finite product
  product_{|I|=3}(1 + t product_{i in I} x_i).
The program expands that product by integer arithmetic. Multiplication by
the Weyl denominator extracts irreducible GL-rank multiplicities.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb
from pathlib import Path
import sys


def permutation_sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p))
                      for j in range(i + 1, len(p)))


def dimension(lam):
    value = Fraction(1)
    rank = len(lam)
    for i in range(rank):
        for j in range(i+1, rank):
            value *= Fraction(lam[i]-lam[j]+j-i, j-i)
    assert value.denominator == 1
    return value.numerator


def exterior_character(rank):
    zero = (0,) * rank
    weights = [tuple(int(i in triple) for i in range(rank))
               for triple in combinations(range(rank), 3)]
    by_degree = [Counter({zero: 1})]
    for weight in weights:
        by_degree.append(Counter())
        for degree in range(len(by_degree)-1, 0, -1):
            for old, value in by_degree[degree-1].items():
                new = tuple(x+y for x, y in zip(old, weight))
                by_degree[degree][new] += value
    return by_degree


def schur_coefficients(rank):
    characters = exterior_character(rank)
    rho = tuple(range(rank-1, -1, -1))
    shifts = [(permutation_sign(p), tuple(rho[i]-rho[p[i]]
                                        for i in range(rank)))
              for p in permutations(range(rank))]
    rows = []
    for degree, character in enumerate(characters):
        candidates = sorted({tuple(sorted(weight, reverse=True))
                             for weight in character}, reverse=True)
        degree_rows = []
        for lam in candidates:
            coefficient = sum(sign * character.get(tuple(lam[i]+shift[i]
                                         for i in range(rank)), 0)
                              for sign, shift in shifts)
            assert coefficient >= 0, (rank, degree, lam, coefficient)
            if coefficient:
                degree_rows.append((degree, lam, coefficient))
        expected = comb(comb(rank, 3), degree)
        obtained = sum(coefficient * dimension(lam)
                       for _, lam, coefficient in degree_rows)
        assert obtained == expected, (rank, degree, obtained, expected)
        assert sum(character.values()) == expected
        rows.extend(degree_rows)
    return rows


@lru_cache(maxsize=None)
def schur_character_by_interlacing(lam):
    """Independent character construction by the GL-rank branching rule."""
    if len(lam) == 1:
        return Counter({lam: 1})
    result = Counter()
    for lower in product(*(range(lam[i+1], lam[i]+1)
                           for i in range(len(lam)-1))):
        last_weight = sum(lam) - sum(lower)
        for weight, coefficient in schur_character_by_interlacing(lower).items():
            result[weight + (last_weight,)] += coefficient
    return result


def verify_entire_characters(rank, rows):
    """Reconstruct every monomial coefficient, not only dimensions."""
    expected = exterior_character(rank)
    reconstructed = [Counter() for _ in expected]
    for degree, lam, multiplicity in rows:
        for weight, coefficient in schur_character_by_interlacing(lam).items():
            reconstructed[degree][weight] += multiplicity * coefficient
    assert reconstructed == expected
    print(f"rank={rank}: independent interlacing reconstruction equals "
          "the complete exterior product character in every monomial; PASS")


def write_table(rank):
    rows = schur_coefficients(rank)
    path = Path(__file__).with_name(f"EXTERIOR_CUBE_RANK_{rank}.tsv")
    content = ["exterior_degree\tpartition\tmultiplicity\tdimension"]
    for degree, lam, coefficient in rows:
        content.append(f"{degree}\t{','.join(map(str,lam))}\t{coefficient}\t{dimension(lam)}")
    path.write_text("\n".join(content) + "\n")
    print(f"rank={rank}: {len(rows)} irreducible summands by degree; "
          f"max multiplicity={max(row[2] for row in rows)}; "
          f"dimension sum={sum(c*dimension(l) for _,l,c in rows)}; PASS")
    verify_entire_characters(rank, rows)
    return rows


if __name__ == '__main__':
    for rank in [int(a) for a in sys.argv[1:]] or [5, 6]:
        write_table(rank)
