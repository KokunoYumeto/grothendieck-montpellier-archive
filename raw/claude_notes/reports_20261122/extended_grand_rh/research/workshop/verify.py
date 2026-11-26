"""Direct divisor enumerations for the four occupied/unoccupied ES shell examples."""
from math import gcd, isqrt


def shell_pairs(prime, denominator):
    modulus = 4 * denominator - prime
    norm = prime * denominator
    assert modulus > 0 and gcd(modulus, norm) == 1
    divisors = set()
    for divisor in range(1, isqrt(norm) + 1):
        if norm % divisor == 0:
            divisors.update([divisor, norm // divisor])
    return sum((left + right) % modulus == 0 for left in divisors for right in divisors)


for p, a, expected in [(5, 2, 8), (5, 3, 0), (1009, 253, 32), (1009, 400, 0)]:
    observed = shell_pairs(p, a)
    assert observed == expected
    print(f"p={p} a={a} R={4*a-p} S={p*a} opposing_pairs={observed}")
