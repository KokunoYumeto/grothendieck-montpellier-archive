"""Finite exact-arithmetic check of NG05; not a substitute for its proof."""
from math import comb


def c(m: int, k: int) -> int:
    return comb(m, k) if 0 <= k <= m else 0


def multiplicity(m: int, a: int, b: int) -> int:
    return c(m, a) * c(m, b) - c(m, a + 1) * c(m, b - 1)


checked = 0
for m in range(1, 21):
    for j in range(2 * m + 1):
        terms = [(a, b, multiplicity(m, a, b))
                 for a in range(m + 1)
                 for b in range(a + 1) if a + b == j]
        assert all(d >= 0 for _, _, d in terms)
        assert sum((a - b + 1) * d for a, b, d in terms) == comb(2*m, j)
        # Compare every torus-weight coefficient of the asserted decomposition.
        for x_degree in range(j + 1):
            predicted = sum(d for a, b, d in terms if b <= x_degree <= a)
            actual = c(m, x_degree) * c(m, j-x_degree)
            assert predicted == actual
        checked += 1

print(f"PASS: {checked} exterior degrees for 1 <= m <= 20.")
print("Checked nonnegative multiplicities, total dimensions, every torus-weight coefficient.")
print("E^2 terms (a,b,multiplicity,rank):")
for a in range(3):
    for b in range(a + 1):
        d = multiplicity(2, a, b)
        print(a, b, d, a-b+1)
