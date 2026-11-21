"""One exact control for the ramification caveat; no existence inference."""
from fractions import Fraction
from hashlib import sha256
from math import comb, isqrt
from pathlib import Path
import json

p, b = 31, 21
assert all(p % d for d in range(2, isqrt(p) + 1))
bernoulli = [Fraction(1)]
for n in range(1, 2 * b + 1):
    bernoulli.append(-sum(Fraction(comb(n + 1, j)) * bernoulli[j]
                          for j in range(n)) / (n + 1))

def chi(a):
    if a % p == 0:
        return 0
    return 1 if pow(a % p, (p - 1) // 2, p) == 1 else -1

beta = sum(Fraction(chi(a)) * sum(
    Fraction(comb(b, j)) * bernoulli[j] * Fraction(a, p) ** (b - j)
    for j in range(b + 1)) for a in range(1, p + 1)) * Fraction(p ** (b - 1), b)
constant = -bernoulli[2 * b] / (2 * b)

def residue(value):
    assert value.denominator % p
    return value.numerator * pow(value.denominator, -1, p) % p

assert residue(constant) == 12
assert residue(beta) == 8
report = {
    "status": "PASS",
    "p": p,
    "b": b,
    "general_discriminant_bound": 2 * b - 7,
    "constant": [constant.numerator, constant.denominator],
    "constant_mod_p": residue(constant),
    "beta_b_chi_minus_p": [beta.numerator, beta.denominator],
    "beta_b_chi_minus_p_mod_p": residue(beta),
    "scope": "A ramified p-index coefficient can be a unit under the general hypotheses; no claim it is the only unit seed.",
    "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
