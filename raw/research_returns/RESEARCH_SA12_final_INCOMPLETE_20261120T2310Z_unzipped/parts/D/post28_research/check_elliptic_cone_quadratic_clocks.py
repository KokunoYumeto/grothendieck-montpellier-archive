"""Finite arithmetic checks only; no claim to certify the geometric proof."""
import hashlib
import json
import math
from pathlib import Path
import random
import time


def run():
    started = time.perf_counter()
    assertions = 0

    def check(condition):
        nonlocal assertions
        assertions += 1
        assert condition

    moduli = [m for m in range(5, 81) if math.gcd(m, 6) == 1]
    rng = random.Random(2866)
    for m in moduli:
        identity = (0, (0,) * m)

        def mul(a, b):
            s, phi = a
            t, psi = b
            return ((s + t) % m,
                    tuple((psi[j] + phi[(j + t) % m]) % m
                          for j in range(m)))

        def inv(a):
            s, phi = a
            return ((-s) % m,
                    tuple((-phi[(j - s) % m]) % m for j in range(m)))

        def power(a, n):
            result = identity
            while n:
                if n & 1:
                    result = mul(result, a)
                a = mul(a, a)
                n //= 2
            return result

        def comm(a, b):
            return mul(mul(mul(a, b), inv(a)), inv(b))

        def projectively_equal(a, b):
            return a[0] == b[0] and len({(x-y) % m
                                         for x, y in zip(a[1], b[1])}) == 1

        X = (1, (0,) * m)
        Z = (0, tuple(range(m)))
        Y = (0, tuple((-3*j*(j-1)//2) % m for j in range(m)))
        for a in (X, Y, Z):
            check(mul(a, inv(a)) == identity)
            check(power(a, m) == identity)
        check(comm(X, Y) == (0, tuple((3*j-3) % m for j in range(m))))
        check(comm(X, Z) == (0, ((-1) % m,) * m))
        check(comm(Y, Z) == identity)
        check(sum(Z[1]) % m == 0)
        check(sum(Y[1]) % m == 0)
        for b in range(m):
            for c in range(m):
                value = mul(power(Y, b), power(Z, c))
                check(projectively_equal(value, identity) == (b == c == 0))
        for _ in range(120):
            a, b, c, d, e, f = [rng.randrange(m) for _ in range(6)]
            left = mul(mul(power(X, a), power(Y, b)), power(Z, c))
            right = mul(mul(power(X, d), power(Y, e)), power(Z, f))
            target = mul(mul(power(X, (a+d) % m), power(Y, (b+e) % m)),
                         power(Z, (c+f-3*d*b) % m))
            check(projectively_equal(mul(left, right), target))

    for p in (2, 3, 5, 7, 11, 13):
        previous = []
        for j in range(1, 7):
            q = p ** (2**j)
            m = q+1 if p == 2 else (q+1)//2
            check(m >= 5 and math.gcd(m, 6*p) == 1 and (q+1) % m == 0)
            check(all(math.gcd(m, n) == 1 for n in previous))
            previous.append(m)

    return {
        "verdict": "PASS",
        "assertions": assertions,
        "moduli": moduli,
        "scope": "Exact monomial-matrix identities, determinants, projective kernel, composite-modulus Heisenberg multiplication and fixed-p arithmetic sequences only.",
        "geometric_claims_tested": False,
        "seconds": time.perf_counter() - started,
    }


if __name__ == "__main__":
    result = run()
    result["program_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result, indent=2))
