"""Exact small-integer certificate for the GD condition in three progressions."""
from math import factorial, gcd
from pathlib import Path
import json

SEEDS = (
    (26, 697446897311),
    (28, 323026426255399),
    (30, 236017358500033404991),
)


def certificate():
    rows = []
    for e0, modulus in SEEDS:
        bound = 2 * e0 + 1
        value = gcd(modulus, factorial(bound))
        assert value == 1
        rows.append({
            "e0": e0,
            "modulus": modulus,
            "bound": bound,
            "gcd_with_factorial": value,
            "conclusion": (
                "Every prime divisor ell satisfies ell-1>2e0; the same "
                "nondivisibility holds for e=e0+(ell-1)t."
            ),
        })
    return rows


if __name__ == "__main__":
    result = certificate()
    path = Path(__file__).with_suffix(".json")
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
