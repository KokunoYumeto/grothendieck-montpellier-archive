"""Finite group checks for the cubic progressions note; Python 3, standard library."""

from collections import defaultdict
from itertools import permutations, product
from math import gcd, isqrt


def sign(s):
    inversions = sum(x > y for i, x in enumerate(s) for y in s[i + 1:])
    return (-1) ** inversions


def trace(s):
    return sum(i == v for i, v in enumerate(s)) - 1


def main():
    cubic = list(permutations(range(3)))
    moduli = 90
    for m in range(1, moduli + 1):
        units = [a for a in range(m) if gcd(a, m) == 1]
        group = [(g, a) for g, a in product(cubic, units)
                 if m % 3 or sign(g) == (1 if a % 3 == 1 else -1)]
        sums = defaultdict(int)
        for g, a in group:
            sums[a] += trace(g)
        assert all(sums[a] == 0 for a in units)
        assert sum(trace(g) ** 2 for g, a in group) == len(group)
        assert len(group) * (2 if m % 3 == 0 else 1) == 6 * len(units)
        test = lambda a: complex((a % 5) - 2, (a % 3) - 1)
        # Compute squared norms with integer arithmetic, including cross term.
        def norm2(z):
            return int(z.real) ** 2 + int(z.imag) ** 2
        lhs = sum(norm2(trace(g) - test(a)) for g, a in group)
        rhs = len(group) + sum(norm2(test(a)) for g, a in group)
        assert lhs == rhs

    trace2 = lambda i, j: 0 if j else (2 if i == 0 else -1)
    for m in range(1, moduli + 1):
        joint = defaultdict(list)
        for i, k, j, a in product(range(3), range(3), range(2), range(m)):
            if gcd(a,m) != 1 or (m % 3 == 0 and (-1) ** j != (1 if a % 3 == 1 else -1)):
                continue
            joint[i,j,a].append(trace2(k,j))
        assert all(sum(v) == 0 for v in joint.values())
        assert sum(y*y for v in joint.values() for y in v) == sum(map(len, joint.values()))

    primechecks = 0
    for p in range(2, 1000):
        if p in (2,3,269) or any(p % d == 0 for d in range(2, isqrt(p)+1)):
            continue
        for r in (2,269):
            roots = [x for x in range(p) if pow(x,3,p) == r%p]
            expected = 0 if p%3 == 2 else 3*int(pow(r,(p-1)//3,p)==1)-1
            assert len(roots)-1 == expected
            primechecks += 1
    assert [i for i in range(37) if pow(i,3,37) == 269%37] == [7,33,34]
    assert not [i for i in range(7) if pow(i,3,7) == 269%7]
    print(f"PASS: {moduli} moduli in both group models; {primechecks} prime/radicand tests.")


if __name__ == "__main__":
    main()
