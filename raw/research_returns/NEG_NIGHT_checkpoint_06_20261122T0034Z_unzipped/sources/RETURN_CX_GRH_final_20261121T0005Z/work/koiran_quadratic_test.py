"""Finite diagnostic for the CX-N13 trace construction, not a proof.

Only the small test models use trial search for D. The general algorithm
obtains D from a trace-zero element of its supplied extension model.
"""
import json
from pathlib import Path


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for r in range(2, int(n**0.5) + 1):
        if sieve[r]:
            sieve[r * r : n + 1 : r] = b"\x00" * (((n - r * r) // r) + 1)
    return [r for r in range(2, n + 1) if sieve[r]]


def mul(x, y, p, D):
    return (
        (x[0] * y[0] + D * x[1] * y[1]) % p,
        (x[0] * y[1] + x[1] * y[0]) % p,
    )


def fp2pow(x, n, p, D):
    result = (1, 0)
    while n:
        if n & 1:
            result = mul(result, x, p, D)
        x = mul(x, x, p, D)
        n >>= 1
    return result


checked_primes = checked_branches = 0
examples = []
for p in primes_upto(10000):
    if p % 4 != 3:
        continue
    checked_primes += 1
    D = next(z for z in range(2, p) if pow(z, (p - 1) // 2, p) == p - 1)
    v = 0
    n = p + 1
    while n % 2 == 0:
        v += 1
        n //= 2
    states = {0}
    for j in range(v - 2):
        following = set()
        for a in states:
            rad = (2 + a) % p
            assert rad and pow(rad, (p - 1) // 2, p) == 1, (p, j, a, "intermediate")
            z = pow(rad, (p + 1) // 4, p)
            assert z * z % p == rad
            following |= {z, (-z) % p}
        states = following
    for a in states:
        checked_branches += 1
        d, e = (a + 2) % p, (a - 2) % p
        assert (
            d and e
            and pow(d, (p - 1) // 2, p) == p - 1
            and pow(e, (p - 1) // 2, p) == 1
        ), (p, a, "terminal")
        ratio = d * pow(D, -1, p) % p
        s, w = pow(ratio, (p + 1) // 4, p), pow(e, (p + 1) // 4, p)
        assert s * s % p == ratio and w * w % p == e
        inv2 = pow(2, -1, p)
        b = (w * inv2 % p, s * inv2 % p)
        conjugate = fp2pow(b, p, p, D)
        assert mul(b, conjugate, p, D) == (p - 1, 0), (p, a, "norm")
        assert fp2pow(b, (p * p - 1) // 2, p, D) == (p - 1, 0), (p, a, "nonsquare")
        if p in {3, 7, 31, 127, 8191} and not any(row["p"] == p for row in examples):
            examples.append({
                "p": p,
                "v2_p_plus_1": v,
                "D": D,
                "a": a,
                "b_basis_1_u": b,
                "norm": p - 1,
            })

result = {
    "range": "all primes p <= 10000 with p == 3 mod 4",
    "checked_primes": checked_primes,
    "all_terminal_sign_branches_checked": checked_branches,
    "examples": examples,
    "result": "all assertions passed",
    "scope": (
        "Finite diagnostic only; proof is independent. Least D enumeration "
        "is only for constructing these test models, not part of proposed general algorithm."
    ),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
