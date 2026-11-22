"""Small exact controls for QE.1--QE.6, not a uniform field search."""
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb, gcd, isqrt
from pathlib import Path
import json


def bernoulli(n):
    values = [Fraction(1)]
    for r in range(1, n + 1):
        values.append(-sum(Fraction(comb(r + 1, j)) * values[j]
                           for j in range(r)) / (r + 1))
    return values


def legendre(a, ell):
    if a % ell == 0:
        return 0
    return 1 if pow(a, (ell - 1) // 2, ell) == 1 else -1


def squarefree_factors(d):
    factors = []
    r = 2
    while r * r <= d:
        if d % r == 0:
            d //= r
            assert d % r != 0
            factors.append(r)
        r += 1
    if d > 1:
        factors.append(d)
    return factors


def character(a, factors):
    value = 1
    for ell in factors:
        value *= legendre(a, ell)
    return value


def beta_direct(r, d, factors, numbers):
    return sum(Fraction(comb(r, j)) * numbers[j] *
               Fraction(d ** j, d) *
               sum(character(a, factors) * a ** (r - j)
                   for a in range(1, d + 1))
               for j in range(r + 1)) / r


def main():
    p, q, m, b = 31, 311, 105, 17
    for ell in (p, q):
        assert all(ell % r for r in range(2, isqrt(ell) + 1))
    assert q % p == 1 and gcd(m, p * q) == 1
    numbers = bernoulli(b)
    residue = lambda z: z.numerator * pow(z.denominator, -1, p) % p
    units = [a for a in range(1, m + 1) if gcd(a, m) == 1]
    squares = {a * a % m for a in units}
    prime_factors = [3, 5, 7]
    characters = [
        [ell for ell, bit in zip(prime_factors, bits) if bit]
        for bits in product((0, 1), repeat=3)
    ]
    selected = [s for s in characters
                if character(-1, s) == character(q, s) == -1]

    def f(r, a):
        x = Fraction(a, m)
        br = sum(Fraction(comb(r, j)) * numbers[j] * x ** (r - j)
                 for j in range(r + 1))
        return residue(Fraction(m ** (r - 1), r) * br)

    fs = {r: {a: f(r, a) for a in units} for r in (3, b)}
    kernel = {}
    for g in units:
        lhs = sum(character(g, s) for s in selected) % p
        indicators = (int(g in squares) - int((-g) % m in squares)
                      - int(q * g % m in squares)
                      + int(-q * g % m in squares))
        rhs = len(characters) * pow(4, -1, p) * indicators % p
        assert lhs == rhs
        kernel[g] = lhs
    rows = []
    diagonal = 0
    for s in selected:
        conductor = 1
        for ell in s:
            conductor *= ell
        row = {"D": -conductor}
        values = {}
        for r in (3, b):
            imprimitive = sum(character(a, s) * fs[r][a]
                              for a in units) % p
            primitive_exact = beta_direct(r, conductor, s, numbers)
            primitive = residue(primitive_exact)
            euler = 1
            for ell in prime_factors:
                if ell not in s:
                    euler = euler * (1 - character(ell, s) *
                                     pow(ell, r - 1, p)) % p
            assert imprimitive == primitive * euler % p
            row[str(r)] = {
                "primitive_exact": str(primitive_exact),
                "primitive_mod_p": primitive,
                "euler_mod_p": euler,
                "imprimitive_mod_p": imprimitive,
            }
            values[r] = imprimitive
        diagonal = (diagonal + values[3] * values[b]) % p
        rows.append(row)
    convolution = sum(fs[3][a] * fs[b][c] * kernel[a * c % m]
                      for a in units for c in units) % p
    assert diagonal == convolution

    beta3_controls = []
    for d in (3, 7, 11, 15, 19, 23, 35, 39, 51, 79, 87, 91):
        factors = squarefree_factors(d)
        assert d % 4 == 3 and character(-1, factors) == -1
        s1 = sum(character(a, factors) * a for a in range(1, d + 1))
        s2 = sum(character(a, factors) * a ** 2
                 for a in range(1, d + 1))
        s3 = sum(character(a, factors) * a ** 3
                 for a in range(1, d + 1))
        value = Fraction(s3 - d * d * s1, 3 * d)
        assert s2 == d * s1
        assert value == beta_direct(3, d, factors, numbers) and value > 0
        if d not in (3, 7):
            assert value.denominator == 1
        if d ** 5 <= 1600 * p * p:
            assert residue(value) != 0
        beta3_controls.append({"D": -d, "beta3": str(value)})
    assert beta3_controls[0]["beta3"] == "2/9"
    assert beta3_controls[1]["beta3"] == "16/7"
    report = {
        "status": "PASS", "p": p, "q": q, "m": m, "b": b,
        "quadratic_character_count": len(characters),
        "selected_character_count": len(selected),
        "orthogonality_checks": len(units),
        "same_character_product_sum": diagonal,
        "convolution_sum": convolution,
        "rows": rows,
        "beta3_controls": beta3_controls,
        "scope": "One conductor and twelve small discriminants only; controls "
                 "for the explicit formulas, not a uniform existence theorem.",
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    output = Path(__file__).with_suffix(".json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"status": report["status"], "sum": diagonal,
                      "selected": len(selected), "output": str(output)}))


if __name__ == "__main__":
    main()
