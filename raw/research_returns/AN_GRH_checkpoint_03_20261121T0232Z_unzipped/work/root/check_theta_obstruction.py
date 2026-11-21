"""Exact small certificate for AN_GRH A06; Python standard library only."""
from math import gcd, isqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n)+1))


def order(a, n):
    x = 1
    for j in range(1, n):
        x = x*a % n
        if x == 1:
            return j
    raise AssertionError("unit order not found")


candidates = [19*m+1 for m in range(2, 38, 2) if prime(19*m+1)]
assert candidates == [191, 229, 419, 457, 571, 647]
orders = [order(2, p) for p in candidates]
assert orders == [95, 76, 418, 76, 114, 323]
assert [p for p, o in zip(candidates, orders) if o == p-1] == [419]
g = pow(2, 19, 419)
assert g == 119 and order(g, 419) == 22
exponents = [(0, 11), (19, 20), (9, 8)]
pairs = [(pow(g, a, 419), pow(g, b, 419)) for a, b in exponents]
assert pairs == [(1, 418), (71, 69), (350, 348)]
assert len(set(pairs)) == 3
assert all((a-b) % 419 == 2 for a, b in pairs)
print("Prime candidates:", candidates)
print("Exact orders of 2:", orders)
print("Only primitive-root candidate: 419")
print("g=2^19 modulo 419:", g)
print("Three distinct ordered pairs in <g>, all with difference 2:", pairs)
print("A06 small arithmetic certificate: PASS")
