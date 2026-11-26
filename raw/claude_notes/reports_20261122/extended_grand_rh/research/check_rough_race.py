"""Check the rational squarefree sieve for the cubic Frobenius character."""
from itertools import product
from math import isqrt, log


def smallest_factors(limit):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


def trace(p):
    if p in (3, 269):
        raise ValueError("the interval calculation omits ramified primes")
    if p % 3 == 2:
        return 0
    return 2 if pow(269, (p - 1) // 3, p) == 1 else -1


def polynomial_product(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, j in product(range(len(left)), range(len(right))):
        result[i + j] += left[i] * right[j]
    return result


def main():
    for t, eta in [(2, 1), (-1, 1), (0, -1)]:
        correction = polynomial_product([1, t], [1, -t, eta])
        assert correction == [1, 0, eta - t * t, t * eta]
        coefficients = [1, t]
        for k in range(2, 20):
            coefficients.append(t * coefficients[-1] - eta * coefficients[-2])
        restored = polynomial_product(coefficients, correction)[:20]
        assert restored == [1, t] + [0] * 18

    limit = 300_000
    spf = smallest_factors(limit)
    print("y       z      split primes     composite products    signed log sums (prime, composite, total)")
    for y in [12_000, 30_000, 75_000, 150_000]:
        z = log(y) ** 2
        direct = [0.0, 0.0]
        counts = [0, 0]
        for n in range(y + 1, 2 * y + 1):
            if n % 3 != 1:
                continue
            left, weight = n, 1
            while left > 1 and weight:
                p = spf[left]
                left //= p
                if p in (3, 269) or p <= z or left % p == 0:
                    weight = 0
                else:
                    weight *= trace(p)
            if weight:
                i = int(spf[n] != n)
                counts[i] += 1
                direct[i] += weight * log(n)

        # Here (log y)^6 > 2y, so every contributing composite is a semiprime.
        assert z ** 3 > 2 * y
        independent = 0.0
        for p in range(int(z) + 1, isqrt(2 * y) + 1):
            if spf[p] != p or p == 269 or p % 3 != 1:
                continue
            for q in range(max(p + 1, y // p + 1), 2 * y // p + 1):
                if spf[q] == q and q != 269 and q % 3 == 1:
                    independent += trace(p) * trace(q) * log(p * q)
        assert abs(direct[1] - independent) < 1e-7
        print(f"{y:6d}  {z:6.1f}   {counts[0]:7d}            {counts[1]:7d}           "
              f"{direct[0]:9.2f} {direct[1]:9.2f} {sum(direct):9.2f}")


if __name__ == "__main__":
    main()
