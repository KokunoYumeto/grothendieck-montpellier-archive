"""Small integer certificates for the localized stable Hecke argument.

This uses the already reviewed exact polynomial file. It does not rederive
the automorphic factorization, any deformation comparison, or Selmer bound.
Only the six reduced evaluations and their explicit Bezout identities are
new calculations here. Coefficients are in descending degree order.
"""
from pathlib import Path
from math import gcd
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve().parent
INPUT = HERE / "symmetric_square_check.json"
MODULI = {
    26: 697446897311,
    28: 323026426255399,
    30: 236017358500033404991,
}


def evaluate_mod(coefficients, value, modulus):
    out = 0
    for coefficient in coefficients:
        out = (out * value + coefficient) % modulus
    return out


def main():
    data = json.loads(INPUT.read_text())
    lookup = {(row["e"], row["p"]): row for row in data["results"]}
    rows = []
    for e, modulus in MODULI.items():
        assert gcd(modulus, 6 * 7 * 13) == 1
        for p in (7, 13):
            row = lookup[e, p]
            target = 1 + p ** e + p ** (2 * e)
            assert row["comparison_point"] == target
            coefficients = row["remaining_stable_coefficients"]
            assert coefficients[0] == 1
            residue = evaluate_mod(coefficients, target % modulus, modulus)
            assert residue == row["remaining_stable_comparison"] % modulus
            assert evaluate_mod(row["symmetric_square_coefficients"],
                                target % modulus, modulus) == 0
            inverse = pow(residue, -1, modulus)
            multiple = (1 - inverse * residue) // modulus
            assert inverse * residue + multiple * modulus == 1
            rows.append({
                "e": e, "p": p, "modulus": modulus,
                "remaining_degree": len(coefficients) - 1,
                "remaining_value_mod_modulus": residue,
                "inverse_mod_modulus": inverse,
                "bezout_modulus_coefficient": multiple,
                "bezout_identity_verified": True,
                "symmetric_square_value_mod_modulus": 0,
            })
    result = {
        "status": "PASS all six exact unit certificates",
        "scope": "Modular polynomial evaluations and Bezout identities only; no Selmer comparison",
        "input": INPUT.name,
        "input_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
        "rows": rows,
    }
    output = HERE / "hecke_normal_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    for row in rows:
        print("e={e}, p={p}, R(t) mod M={remaining_value_mod_modulus}, "
              "inverse={inverse_mod_modulus}: PASS".format(**row))


if __name__ == "__main__":
    main()
