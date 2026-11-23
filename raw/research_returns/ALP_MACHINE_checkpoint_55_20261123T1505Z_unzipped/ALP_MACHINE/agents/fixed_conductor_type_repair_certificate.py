"""Exact finite arithmetic checks for ALP-LIFT-11, not a formal global proof."""
from itertools import product
import json
from pathlib import Path

p = 29
assert pow(2, 14, p) == p - 1
assert pow(2, 4, p) == 16
assert len({pow(2, a, p) for a in range(28)}) == 28
assert len({pow(16, a, p) for a in range(7)}) == 7
assert len({((-1)**a * pow(16, b, p)) % p
            for a in range(2) for b in range(7)}) == 14

checked_characters = 0
for c in product(range(14), repeat=3):
    C = sum(c)
    S = sum((i+1) * c[i] for i in range(3))
    r = (7*C + 6*S) % 14
    assert (r + S) % 7 == 0
    assert (r + C) % 2 == 0
    # Check every rational root (-1)^a zeta^b in exponents of zeta_28.
    for a in range(2):
        for b in range(7):
            infinity_exp = 14*a*C + 4*b*S
            finite_exp = r*(14*a + 4*b)
            assert (infinity_exp + finite_exp) % 28 == 0
    checked_characters += 1

nu = (0, 0, 1)
checked_weights = 0
for d in product(range(11), repeat=3):
    c = tuple(-d[i]-2-nu[i] for i in range(3))
    for i in range(3):
        first = (d[i]+nu[i]+c[i], nu[i]+c[i])
        second = (-2, -d[i]-2)
        assert first == second
    checked_weights += 1

checked_prefixes = 0
for D in range(20):
    for d in range(D+1):
        c = -D-2
        first = (d+c, c)
        lam = (D, D-d)
        assert first == (-2-lam[1], -2-lam[0])
        assert sum(lam) == 2*D-d
        checked_prefixes += 1

explicit_d = (2, 0, 2)
explicit_c = tuple(-explicit_d[i]-2-nu[i] for i in range(3))
C = sum(explicit_c)
S = sum((i+1)*explicit_c[i] for i in range(3))
r = (7*C+6*S) % 14
assert explicit_c == (-4, -2, -5)
assert (C, S, r) == (-11, -23, 9)

bilinear_c = tuple(2-nu[i] for i in range(3))
bilinear_C = sum(bilinear_c)
bilinear_S = sum((i+1)*bilinear_c[i] for i in range(3))
bilinear_r = (7*bilinear_C + 6*bilinear_S) % 14
assert (bilinear_c, bilinear_C, bilinear_S, bilinear_r) == ((2, 2, 1), 5, 9, 5)
for d in product(range(11), repeat=3):
    for i in range(3):
        first = (d[i]+nu[i]+bilinear_c[i], nu[i]+bilinear_c[i])
        contragredient = (-first[1], -first[0])
        assert contragredient == (-2, -d[i]-2)

result = {
    "status": "passed",
    "kind": "exact finite arithmetic computation, not a formal global proof",
    "residue_modulus": 29,
    "primitive_generator": 2,
    "zeta_image": 16,
    "all_character_classes_checked": checked_characters,
    "weight_triples_checked": checked_weights,
    "finite_prefix_pairs_checked": checked_prefixes,
    "explicit_degree": explicit_d,
    "explicit_twist": explicit_c,
    "explicit_finite_character_exponent_mod28": r,
    "fixed_bilinear_twist": bilinear_c,
    "fixed_bilinear_finite_character_exponent_mod28": bilinear_r,
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
