"""Independent exact arithmetic check of the proposed A06 prime-orbit cutoff.

This checks the finite arithmetic after the proved geometric inequality;
it does not stand in for the geometry. Python standard library only.
"""

from math import gcd, isqrt
import json


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def order_by_successive_powers(a, n):
    x = a % n
    e = 1
    while x != 1:
        x = x * a % n
        e += 1
        assert e < n
    return e


primes = [n for n in range(3, 705, 2) if prime(n) and (n - 1) % 19 == 0]
assert primes == [191, 229, 419, 457, 571, 647]
orders = {n: order_by_successive_powers(2, n) for n in primes}
assert list(orders.values()) == [95, 76, 418, 76, 114, 323]
primitive = [n for n in primes if orders[n] == n - 1]
assert primitive == [419]

# Independently test the geometric inequality for every prime <= 704.
inequality_survivors = []
for n in range(3, 705, 2):
    if not prime(n):
        continue
    e = gcd(n - 1, 19)
    h = (n - 1) // e
    if h * (h + 1) <= 2 * (n - 1):
        inequality_survivors.append(n)
assert inequality_survivors == primes

n = 419
generator = pow(2, 19, n)
assert generator == 119
orbit = []
x = 1
while x not in orbit:
    orbit.append(x)
    x = x * generator % n
assert x == 1 and len(orbit) == 22
assert set(orbit) == {pow(2, 19 * j, n) for j in range(22)}
pairs = [(1, 418), (71, 69), (350, 348)]
assert len(set(pairs)) == 3
assert all(a in orbit and b in orbit and a != b and (a - b) % n == 2
           for a, b in pairs)
all_pairs = [(a, b) for a in sorted(orbit) for b in sorted(orbit)
             if (a - b) % n == 2]
assert len(all_pairs) >= 3

print(json.dumps({
    "maximum_prime_from_inequality": 704,
    "prime_candidates": primes,
    "orders_of_two": orders,
    "primitive_root_survivors": primitive,
    "generator_mod_419": generator,
    "orbit_size": len(orbit),
    "orbit": sorted(orbit),
    "difference_two_pairs": all_pairs,
    "result": "PASS: the required prime theta condition is impossible",
}, indent=2))
