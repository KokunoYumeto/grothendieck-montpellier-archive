#!/usr/bin/env python3
"""Finite checks of the actual chain matrices in E.4e--f, including m=1.

The integral projective model of the standard complex is
  C0=Z --(2,0,...)--> C1=Z^(1+s) --0--> C2=Z^s --sum--> C3=Z.
For the sign-deleted version remove the first Z in C0 and C1.
We enumerate kernels/images of the nonzero matrices modulo m.
"""
from itertools import product
from math import gcd
from time import perf_counter

started = perf_counter()
print("s\tm\tstandard H0,H1,H2,H3 orders\tpositive H0,H1,H2,H3 orders")
for s in range(4):
    for m in range(1, 9):
        kernel_two = [x for x in range(m) if 2*x % m == 0]
        image_two = {2*x % m for x in range(m)}
        residues = list(product(range(m), repeat=s))
        kernel_sum = [v for v in residues if sum(v) % m == 0]
        image_sum = {sum(v) % m for v in residues}
        standard = (len(kernel_two), m**(s+1)//len(image_two),
                    len(kernel_sum), m//len(image_sum))
        positive = (1, m**s, len(kernel_sum), m//len(image_sum))
        d = gcd(m, 2)
        expected = (d, d*m**s, m**max(s-1, 0), m if s == 0 else 1)
        assert standard == expected
        assert positive == (1, m**s, m**max(s-1, 0), m if s == 0 else 1)
        print(f"{s}\t{m}\t{standard}\t{positive}")

print("\nCoordinate-inclusion chain-map check:")
for s in range(4):
    for t in range(s, 4):
        for m in (2, 3, 4, 5):
            for v in product(range(m), repeat=s):
                included = v + (0,)*(t-s)
                assert sum(included) % m == sum(v) % m
        print(f"s={s} -> t={t}: d^2 inclusions commute, checked mod 2,3,4,5")
print(f"Elapsed seconds: {perf_counter()-started:.6f}")
