#!/usr/bin/env python3
"""Exact finite checks of E.5f, supplementing its infinite-limit proof.

The infinite contradiction is proved in the text, not established by
these checks. All modular arithmetic uses integers or exact fractions.
"""
from fractions import Fraction
from time import perf_counter

started = perf_counter()
print("N\tpartial sum mod 2^N\t(-1/7) mod 2^N\tmatch")
for n in range(1, 61):
    modulus = 2**n
    partial = sum(2**j for j in range(n) if j % 3 == 0)
    target = (-pow(7, -1, modulus)) % modulus
    assert partial % modulus == target
    if n <= 12 or n % 6 == 0:
        print(f"{n}\t{partial % modulus}\t{target}\tTrue")

print("\nFinite truncations have compatible valuations in Z:")
for n in (1, 3, 6, 12, 24, 60):
    # Starting from the terminal point x_N=1 gives x_j=t^r_j.
    values = [0] * (n+1)
    for j in range(n-1, -1, -1):
        values[j] = (1 if j % 3 == 0 else 0) + 2*values[j+1]
    assert all(values[j] == (1 if j % 3 == 0 else 0) + 2*values[j+1]
               for j in range(n))
    assert values[0] == sum(2**j for j in range(n) if j % 3 == 0)
    print(f"N={n}: r_N=0, r_0={values[0]}, all recurrences hold")

print("\nPeriod-three geometric-sum identity:")
for blocks in range(1, 21):
    n = 3*blocks
    partial = sum(2**j for j in range(n) if j % 3 == 0)
    assert 7*partial == 8**blocks - 1
print("7 * sum_{j=0}^{m-1} 8^j = 8^m - 1, checked for m=1,...,20.")

target = Fraction(-1, 7)
print(f"\nForced limit has reduced denominator {target.denominator}.")
assert target.denominator == 7
assert all(3**m % 7 != 0 for m in range(120))
print("A denominator 7 cannot divide a power of 3; "
      "the proof uses unique prime factorization, not this finite check.")
print(f"Elapsed seconds: {perf_counter()-started:.6f}")
