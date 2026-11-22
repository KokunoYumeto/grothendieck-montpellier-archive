"""Exact point certificate for the printed Boyle--Chen A.6 generator.

The printed map rotates each disk slice by pi*y.  At y=1 its action
is exactly (x1,x2)->(-x1,-x2).  In the disk quotient model of RP^2,
only opposite points ON the disk boundary are identified.
"""

from fractions import Fraction as F
from time import perf_counter


def squared_norm(point):
    return sum(x * x for x in point)


def same_projective_disk_class(p, q):
    assert squared_norm(p) <= 1 and squared_norm(q) <= 1
    return p == q or (squared_norm(p) == 1 and p == tuple(-x for x in q))


def main():
    started = perf_counter()
    p = (F(1, 2), F(0))
    image = tuple(-x for x in p)
    assert squared_norm(p) == F(1, 4)
    assert squared_norm(image) == F(1, 4)
    assert not same_projective_disk_class(p, image)
    print("SOURCE: Boyle--Chen2024 AppendixA TheoremA.6 p614")
    print("TOP INPUT: (1/2,0,1)")
    print("TOP IMAGE: (-1/2,0,1)")
    print("SQUARED DISK NORMS: 1/4, 1/4")
    print("PASS: distinct interior-disk classes; printed T1 is not top-boundary-fixed")
    print(f"RUNTIME_SECONDS: {perf_counter() - started:.9f}")


if __name__ == "__main__":
    main()
