"""Exact projected-primary root-lifting certificates, without coefficient tables.

This implements the new root-lifting step for r=3, d=2 in Fp[s]/(s^2+3).
It is a finite test of the arithmetic algorithm, not a proof of its uniform bound.
"""
from pathlib import Path
import json
from math import isqrt


def certificate(p, remove_two=False):
    assert p % 3 == 2 and p > 3
    assert all(p % divisor for divisor in range(2, isqrt(p) + 1))
    a, cofactor = 0, p + 1
    while cofactor % 3 == 0:
        cofactor //= 3
        a += 1
    if remove_two:
        while cofactor % 2 == 0:
            cofactor //= 2
    assert p >= 6 * cofactor
    zero, one = (0, 0), (1, 0)

    def add(u, v):
        return ((u[0] + v[0]) % p, (u[1] + v[1]) % p)

    def neg(u):
        return ((-u[0]) % p, (-u[1]) % p)

    def sub(u, v):
        return add(u, neg(v))

    def mul(u, v):
        return ((u[0] * v[0] - 3 * u[1] * v[1]) % p,
                (u[0] * v[1] + u[1] * v[0]) % p)

    def inv(u):
        norm = (u[0] ** 2 + 3 * u[1] ** 2) % p
        assert norm
        t = pow(norm, -1, p)
        return (u[0] * t % p, -u[1] * t % p)

    def power(u, n):
        if n < 0:
            return power(inv(u), -n)
        v = one
        while n:
            if n & 1:
                v = mul(v, u)
            u = mul(u, u)
            n >>= 1
        return v

    def trim(f):
        f = list(f)
        while f and f[-1] == zero:
            f.pop()
        return f

    def remainder(f, g):
        f, g = trim(f), trim(g)
        assert g
        while len(f) >= len(g):
            coefficient = mul(f[-1], inv(g[-1]))
            offset = len(f) - len(g)
            for i, v in enumerate(g):
                f[i + offset] = sub(f[i + offset], mul(coefficient, v))
            f = trim(f)
        return f

    def gcd(f, g):
        f, g = trim(f), trim(g)
        while g:
            f, g = g, remainder(f, g)
        scalar = inv(f[-1])
        return [mul(v, scalar) for v in f]

    half = pow(2, -1, p)
    eta = (-half % p, half)
    assert power(eta, 3) == one and eta != one
    logs = []

    def root(c):
        # Elements of R are three coefficients in K, modulo X^3-c.
        Rone = [one, zero, zero]
        alpha = [zero, one, zero]
        modulus = [neg(c), zero, zero, one]

        def rsub(v, w):
            return [sub(v[i], w[i]) for i in range(3)]

        def rmul(v, w):
            output = [zero] * 5
            for i in range(3):
                for j in range(3):
                    output[i + j] = add(output[i + j], mul(v[i], w[j]))
            for i in (4, 3):
                output[i - 3] = add(output[i - 3], mul(c, output[i]))
            return output[:3]

        def rpower(v, n):
            output = Rone
            while n:
                if n & 1:
                    output = rmul(output, v)
                v = rmul(v, v)
                n >>= 1
            return output

        def rinv(v):
            columns = [rmul(v, [one if i == j else zero for i in range(3)])
                       for j in range(3)]
            matrix = [[columns[j][i] for j in range(3)] + [Rone[i]]
                      for i in range(3)]
            for j in range(3):
                pivot = next(i for i in range(j, 3) if matrix[i][j] != zero)
                matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
                scalar = inv(matrix[j][j])
                matrix[j] = [mul(x, scalar) for x in matrix[j]]
                for i in range(3):
                    if i != j:
                        scalar = matrix[i][j]
                        matrix[i] = [sub(matrix[i][k], mul(scalar, matrix[j][k]))
                                     for k in range(4)]
            return [matrix[i][3] for i in range(3)]

        def tau(v):
            return [mul(v[i], power(eta, i)) for i in range(3)]

        def scalar(v):
            return v[1] == zero and v[2] == zero

        def split(v, prime=3):
            assert rpower(v, prime) == Rone and not scalar(v)
            primitive = eta if prime == 3 else neg(one)
            for j in range(prime):
                h = gcd(rsub(v, [power(primitive, j), zero, zero]), modulus)
                if 1 < len(h) < 4:
                    return h
            raise AssertionError("No proper factor in torsion comparison")

        for i in range(1, 6 * cofactor):
            minus_i = (-i % p, 0)
            if power(minus_i, 3) == c:
                logs.append({"shift": i, "branch": "scalar root"})
                return minus_i
            v = [(i % p, 0), one, zero]
            beta = rmul(v, rinv(rpower(v, p)))
            gamma = rpower(beta, cofactor)
            delta = rmul(tau(gamma), rinv(gamma))
            if scalar(delta):
                continue
            order = (p + 1) // cofactor
            for prime in (2, 3):
                while order % prime == 0 and rpower(delta, order // prime) == Rone:
                    order //= prime
            assert order > 1 and rpower(delta, order) == Rone
            order_exponent, odd_part = 0, order
            while odd_part % 3 == 0:
                odd_part //= 3
                order_exponent += 1
            if order % 2 == 0:
                h, branch = split(rpower(delta, order // 2), 2), "order-two comparison"
            elif order_exponent == 1:
                h, branch = split(delta), "order-three comparison"
            else:
                assert odd_part == 1 and 2 <= order_exponent <= a
                xi = rpower(delta, 3 ** (order_exponent - 2))
                xi3 = rpower(xi, 3)
                if not scalar(xi3):
                    h, branch = split(xi3), "nonscalar cube of order-nine element"
                else:
                    epsilon = rmul(tau(xi), rinv(xi))
                    assert not scalar(epsilon), "Forbidden odd-prime commutator case"
                    h, branch = split(epsilon), "commutator comparison"
            degree = len(h) - 1
            w = h[0] if degree % 2 == 0 else neg(h[0])
            u = pow(degree, -1, 3)
            v_exponent = (1 - u * degree) // 3
            result = mul(power(w, u), power(c, v_exponent))
            assert power(result, 3) == c
            logs.append({"shift": i, "delta_order": order,
                         "branch": branch, "factor_degree": degree,
                         "factor_coefficients": h, "root": result})
            return result
        raise AssertionError("Projected search exhausted")

    z = eta
    for j in range(1, a):
        z = root(z)
        assert power(z, 3 ** (j + 1)) == one
        assert power(z, 3 ** j) != one
    assert power(z, p + 1) == one
    trace = add(z, inv(z))
    assert trace[1] == 0
    constant = -trace[0] % p
    roots_of_cubic = [x for x in range(p) if (x ** 3 - 3 * x + constant) % p == 0]
    assert not roots_of_cubic
    return {"p": p, "a": a, "removed_two_primary_part": remove_two,
            "cofactor_M": cofactor,
            "initial_primitive_cube_root": eta, "lifting_steps": logs,
            "maximal_three_primary_unit": z,
            "cubic_coefficients_ascending": [constant, -3 % p, 0, 1],
            "cubic_roots_in_prime_field": roots_of_cubic,
            "all_assertions_passed": True}


if __name__ == "__main__":
    data = {"scope": "Exact arithmetic tests of r=3,d=2 projected-primary lifting",
            "certificates": [certificate(p) for p in (17, 53, 4373)],
            "two_primary_refinement_certificates":
                [certificate(p, remove_two=True) for p in (17, 53, 4373)]}
    print(json.dumps(data, indent=2))
