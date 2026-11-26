"""Finite exact checks for AM-K023; not a proof of higher 11-adic content."""

from functools import lru_cache
from itertools import product
from math import comb, prod
from pathlib import Path
import hashlib
import json

P = 11


def make_nf(kappa):
    @lru_cache(None)
    def nf(beta):
        # order: (1+,1-,2+,2-,3+,3-); all operations in F_11.
        b = list(beta)
        for j in range(6):
            if b[j] < P:
                continue
            b[j] -= P
            if j < 2:
                target = j + 4
                factor = 2 * kappa * b[target]
                if factor % P == 0:
                    return 0, (0,) * 6
                b[target] -= 1
            elif j < 4:
                target = 3 - j
                factor = -1
                b[target] += 1
            else:
                target = j - 2
                factor = -kappa * pow(2, -1, P) * b[target]
                if factor % P == 0:
                    return 0, (0,) * 6
                b[target] -= 1
            c, tail = nf(tuple(b))
            return factor * c % P, tail
        return 1, tuple(b)
    return nf


def cayley(a, n):
    return prod(range(n, n + a))


def rectangle_target(a, q, r, kappa):
    scalar = pow(kappa, 4 * a * q, P)
    scalar *= pow(prod(cayley(a, r - ell) for ell in range(q)), 4, P)
    exponents = (r + q, r + q, r - q, r - q, r - q, r - q)
    return scalar % P, exponents


def det2_product(exponents, scalar=1):
    # Key records the six diagonal and six off-diagonal exponents.
    out = {}
    options = [
        [(j, (-1) ** j * comb(n, j) % P)
         for j in range(n + 1) if comb(n, j) % P]
        for n in exponents
    ]
    for choices in product(*options):
        off = tuple(c[0] for c in choices)
        diagonal = tuple(n - j for n, j in zip(exponents, off))
        coefficient = scalar * prod(c[1] for c in choices) % P
        out[(diagonal, off)] = coefficient
    return {key: value for key, value in out.items() if value}


def reduce_det2_product(n, kappa):
    # Sparse full expansion and entrywise normal form, independent of Cayley.
    nf = make_nf(kappa)
    original = det2_product((n,) * 6)
    out = {}
    for (diagonal, off), coefficient in original.items():
        cd, bd = nf(diagonal)
        if not cd:
            continue
        co, bo = nf(off)
        if not co:
            continue
        coefficient = coefficient * cd * cd * co * co % P
        key = bd, bo
        out[key] = (out.get(key, 0) + coefficient) % P
    return {key: value for key, value in out.items() if value}, len(original)


def check_det2_cayley(n):
    # Integer polynomial check: (d_a d_d - d_b d_c)(ad-bc)^n.
    out = {}
    for j in range(n + 1):
        c = (-1) ** j * comb(n, j)
        if n - j:
            key = (n - j - 1, j)
            out[key] = out.get(key, 0) + c * (n - j) ** 2
        if j:
            key = (n - j, j - 1)
            out[key] = out.get(key, 0) - c * j * j
    expected = {
        (n - 1 - j, j): n * (n + 1) * (-1) ** j * comb(n - 1, j)
        for j in range(n)
    }
    return {key: value for key, value in out.items() if value} == expected


def main():
    checks = []
    assert all(check_det2_cayley(n) for n in range(1, 41))
    checks.append({"check": "integer Cayley determinant2", "n_range": [1, 40], "pass": True})

    count = 0
    for kappa in range(1, P):
        nf = make_nf(kappa)
        for q in range(1, 6):
            for r in range(q, 11 - q):
                n = 11 * q + r
                actual = nf((n,) * 6)
                expected = rectangle_target(1, q, r, kappa)
                assert actual == expected, (kappa, q, r, actual, expected)
                count += 1
    checks.append({"check": "one-entry full normal form vs closed rectangle formula",
                   "cases": count, "pass": True})

    for n, q, r in [(12, 1, 1), (24, 2, 2)]:
        actual, source_terms = reduce_det2_product(n, 5)
        scalar, exponents = rectangle_target(2, q, r, 5)
        expected = det2_product(exponents, scalar)
        assert actual == expected, (n, len(actual), len(expected))
        checks.append({"check": "full six-matrix determinant2 expansion",
                       "n": n, "kappa": 5, "source_terms_mod11": source_terms,
                       "output_terms": len(actual), "pass": True})

    actual, source_terms = reduce_det2_product(23, 5)
    assert not actual
    checks.append({"check": "outside-unit-range rectangle vanishes mod11",
                   "a": 2, "n": 23, "source_terms_mod11": source_terms, "pass": True})

    scalar, exponents = rectangle_target(6, 5, 5, 5)
    assert scalar and exponents == (10, 10, 0, 0, 0, 0)
    assert 6 * 6 * 60 == 2160
    assert 3 * 2160 + 2 == 6482
    assert 29 ** 2 < 6482 <= 29 ** 3
    checks.append({"check": "literal rank6 n60 example arithmetic",
                   "normal_form_scalar_mod11_at_kappa5": scalar,
                   "remaining_powers": exponents, "degree": 2160,
                   "level_threshold": 6482, "least_power29": 24389, "pass": True})

    payload = {
        "claim": "Finite exact checks supporting AM-K023; no higher-content or infinite claim is inferred from finite enumeration.",
        "prime": P, "checks": checks, "pass": True,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
