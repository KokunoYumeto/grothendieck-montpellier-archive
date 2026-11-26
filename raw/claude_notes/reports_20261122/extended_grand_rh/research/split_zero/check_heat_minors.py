"""Exact polynomial examples for fixed-contour subdiscriminants under heat flow."""
from fractions import Fraction
from math import comb, factorial, prod


def partitions(total, least=1):
    if total == 0:
        yield ()
    for part in range(least, total + 1):
        for rest in partitions(total - part, part):
            yield (part,) + rest


def endpoint(orders):
    coefficients = [1]
    for center, multiplicity in enumerate(orders):
        for _ in range(multiplicity):
            coefficients = [a - center * b for a, b in
                            zip([0] + coefficients, coefficients + [0])]
    return coefficients


def evolve(coefficients, time):
    n = len(coefficients) - 1
    # z^i evolves to sum_j (-t)^j i! z^(i-2j)/(j! (i-2j)!).
    return [sum(coefficients[i] * (-time) ** ((i - h) // 2) * factorial(i)
                // (factorial((i - h) // 2) * factorial(h))
                for i in range(h, n + 1, 2)) for h in range(n + 1)]


def newton_sums(polynomial, top):
    n = len(polynomial) - 1
    sums = [n]
    for j in range(1, top + 1):
        initial = j * polynomial[n-j] if j <= n else 0
        sums.append(-initial - sum(polynomial[n-i] * sums[j-i]
                                   for i in range(1, min(n, j-1)+1)))
    return sums


def determinant(entries):
    a = [row.copy() for row in entries]
    sign, previous = 1, 1
    for j in range(len(a) - 1):
        pivot = next((i for i in range(j, len(a)) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            sign = -sign
        for i in range(j+1, len(a)):
            for h in range(j+1, len(a)):
                numerator = a[j][j] * a[i][h] - a[i][j] * a[j][h]
                val, remainder = divmod(numerator, previous)
                assert remainder == 0
                a[i][h] = val
        previous = a[j][j]
    return sign * a[-1][-1]


def coefficients_from_values(values):
    # Newton's forward formula at 0 applied in the ordinary monomial basis.
    result = [Fraction(0)] * len(values)
    basis = [Fraction(1)]
    for j in range(len(result)):
        for i, coefficient in enumerate(basis):
            result[i] += values[0] * coefficient
        values = [b-a for a, b in zip(values, values[1:])]
        basis = [(a-j*b)/(j+1)
                 for a, b in zip([Fraction(0)]+basis, basis+[Fraction(0)])]
    return result


def occupancy(orders, total):
    if not orders:
        if total == 0:
            yield ()
        return
    for k in range(min(orders[0],total)+1):
        for rest in occupancy(orders[1:],total-k):
            yield (k,)+rest


def hermite_constant(m, a):
    return m**a * prod((m-j)**(a-j) for j in range(1,a))


def leading_term(orders, k):
    costs = sorted(j for m in orders for j in range(m))
    valuation = sum(costs[:k])
    total = 0
    for counts in occupancy(orders, k):
        if sum(comb(a, 2) for a in counts) != valuation:
            continue
        internal = prod(hermite_constant(m,a) for m,a in zip(orders,counts))
        external = prod((j-i)**(2*counts[i]*counts[j])
                        for j in range(len(counts)) for i in range(j))
        total += internal * external
    return valuation, 2**valuation * total


def check(orders):
    polynomial = endpoint(orders)
    n = sum(orders)
    # Each Newton sum S_j has degree at most floor(j/2) in t.
    degree_bound = comb(n,2)
    sample = [newton_sums(evolve(polynomial,t),2*n-2)
              for t in range(degree_bound+2)]
    for k in range(1,n+1):
        d = comb(k,2)
        values = [determinant([[s[i+j] for j in range(k)] for i in range(k)])
                  for s in sample[:d+2]]
        coefficients = coefficients_from_values(values[:d+1])
        assert sum(a*(d+1)**h for h,a in enumerate(coefficients)) == values[-1]
        v = next(i for i, a in enumerate(coefficients) if a)
        assert (v, coefficients[v]) == leading_term(orders,k), (orders,k)
    return n


if __name__ == "__main__":
    totals = [check(orders) for n in range(1,9) for orders in partitions(n)]
    print(f"Passed {len(totals)} multiplicity partitions and {sum(totals)} principal minors through total degree 8.")

