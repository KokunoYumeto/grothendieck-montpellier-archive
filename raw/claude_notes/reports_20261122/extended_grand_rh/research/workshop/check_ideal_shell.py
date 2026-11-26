"""Exact finite coefficient check for the marked Eisenstein ideal-divisor sums."""
from itertools import product
from math import comb, isqrt, prod


def good_prime_ideals(limit):
    # Each entry describes one prime ideal by its norm, norm sign, and the
    # exponent of omega in the cubic residue symbol of 269 at that ideal.
    prime = bytearray([1]) * (limit + 1)
    prime[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if prime[p]:
            for n in range(p*p, limit + 1, p):
                prime[n] = 0
    ideals = []
    for p in range(2, limit + 1):
        if not prime[p] or p in (2, 3, 7, 269):
            continue
        if p % 3 == 2:
            if p*p <= limit:
                ideals.append((p*p, 1, 0))
            continue
        order = (p - 1) // 3
        root = next(value for g in range(2, p) if (value := pow(g, order, p)) != 1)
        exponent = [1, root, root*root % p].index(pow(269, order, p))
        sign = 1 if p % 4 == 1 else -1
        ideals.extend([(p, sign, exponent), (p, sign, -exponent % 3)])
    return sorted(ideals)


def visit_ideals(prime_ideals, limit, start=0, norm=1, factors=()):
    yield factors
    for i in range(start, len(prime_ideals)):
        q, sign, phase = prime_ideals[i]
        if norm*q > limit:
            break
        power_norm, power = norm*q, 1
        while power_norm <= limit:
            yield from visit_ideals(prime_ideals, limit, i+1, power_norm,
                                    factors + ((sign, phase, power),))
            power_norm *= q
            power += 1


def ordered_opposites(signs, norm_sign):
    tags = signs + [norm_sign*sign for sign in signs]
    return sum(left != right for left in tags for right in tags)


def mixed_coefficient(k, sign):
    # Coefficient of (1-x²)/((1-x)²(1-sign*x)²).
    def denominator(j):
        return sum((t+1)*(j-t+1)*sign**t for t in range(j+1))
    return denominator(k) - denominator(k-2)


def main():
    limit = 30000
    primes = good_prime_ideals(limit)
    counts = {(sign, phase): 0 for sign in (1, -1) for phase in range(3)}
    for factors in visit_ideals(primes, limit):
        divisor_signs = [prod(values) for values in product(
            *[[sign**j for j in range(k+1)] for sign, _, k in factors])]
        norm_sign = prod(sign**k for sign, _, k in factors)
        phase = sum(phase*k for _, phase, k in factors) % 3
        counts[norm_sign, phase] += 1
        tau = len(divisor_signs)
        # Coefficients of P^4/Z, Q^4/Z and P^2Q^2/Z after division by psi(a).
        pure = prod(comb(k+3, 3)-comb(k+1, 3) for _, _, k in factors)
        twisted = pure*norm_sign
        mixed = prod(mixed_coefficient(k, sign) for sign, _, k in factors)
        assert pure == tau*tau
        assert mixed == sum(divisor_signs)**2
        marked_once = divisor_signs + [-v for v in divisor_signs]
        marked_twice = marked_once + divisor_signs
        weight0 = ordered_opposites(divisor_signs, norm_sign)
        weight2 = ordered_opposites(marked_twice, norm_sign)
        assert weight0*(norm_sign == 1) == pure + twisted - 2*mixed
        assert weight2*(norm_sign == 1) == 9*(pure + twisted) - 2*mixed
        assert ordered_opposites(marked_once, -norm_sign) == 8*tau*tau
        if norm_sign == 1:
            two_distinct_marks = marked_once + [-v for v in marked_once]
            assert ordered_opposites(two_distinct_marks, 1) == 32*tau*tau
    assert min(counts.values()) > 0
    print("Good integral ideals of norm at most", limit, ":", sum(counts.values()))
    print("Counts by (norm sign, cubic exponent):", counts)


if __name__ == "__main__":
    main()
