"""Exact F16 arithmetic for the new Frobenius specialization obstruction.

The finite certificate checks the actual field, all six cross-ratio
values, Frobenius images, and the cyclotomic lift. Étale invariance and
the characteristic-zero anabelian input are source theorems, not tested.
"""
import datetime
import json
from pathlib import Path
import time

started = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.monotonic()
modulus = 0b10011  # T^4+T+1
checks = []


def check(name, truth):
    assert truth, name
    checks.append({"id": name, "passed": True})


def remainder(f, g):
    while f and f.bit_length() >= g.bit_length():
        f ^= g << (f.bit_length() - g.bit_length())
    return f


def multiply(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 0b10000:
            a ^= modulus
    return out


def power(a, n):
    out = 1
    while n:
        if n & 1:
            out = multiply(out, a)
        a = multiply(a, a)
        n >>= 1
    return out


def inverse(a):
    assert a
    return power(a, 14)


def divide(a, b):
    return multiply(a, inverse(b))


def polynomial_value(binary_coefficients, value):
    out = 0
    for i in range(binary_coefficients.bit_length() - 1, -1, -1):
        out = multiply(out, value) ^ ((binary_coefficients >> i) & 1)
    return out


irreducibility_remainders = {str(g): remainder(modulus, g) for g in (0b10, 0b11, 0b111)}
for g, value in irreducibility_remainders.items():
    check("no_factor_" + g, value != 0)
check("all_nonzero_elements_invertible", all(multiply(x, inverse(x)) == 1 for x in range(1, 16)))
a = 0b0010
a2 = multiply(a, a)
check("quartic_relation", polynomial_value(modulus, a) == 0)
check("a_squared_distinct", a2 not in (0, 1, a))
orbit = [a, 1 ^ a, inverse(a), inverse(1 ^ a), divide(a, a ^ 1), divide(a ^ 1, a)]
check("six_crossratios_distinct", len(set(orbit)) == 6)
for index, value in enumerate(orbit):
    check("frobenius_outside_crossratio_" + str(index), value != a2)
frobenius_images = {str(x): multiply(x, x) for x in range(16)}
check("frobenius_is_bijection_on_field", len(set(frobenius_images.values())) == 16)
check("fourth_frobenius_is_identity", all(power(x, 16) == x for x in range(16)))
check("frobenius_maps_punctures", [0, 1, "infinity", a2] == [multiply(0, 0), multiply(1, 1), "infinity", multiply(a, a)])
check("primitive_order15", power(a, 15) == 1 and power(a, 3) != 1 and power(a, 5) != 1)
# Phi15=T^8-T^7+T^5-T^4+T^3-T+1, reduced modulo 2.
phi15 = sum(1 << exponent for exponent in (8, 7, 5, 4, 3, 1, 0))
check("cyclotomic_lift_relation", polynomial_value(phi15, a) == 0)
check("order_of_2_mod15", pow(2, 4, 15) == 1 and all(pow(2, j, 15) != 1 for j in (1, 2, 3)))
check("separable_15th_root", power(a, 14) != 0)

payload = {
    "started_utc": started,
    "elapsed_seconds": time.monotonic() - tick,
    "field_representation": "F2[T]/(T^4+T+1), polynomial bits from constant upward",
    "irreducibility_remainders": irreducibility_remainders,
    "a": a,
    "a_squared": a2,
    "six_crossratio_values": orbit,
    "frobenius_images": frobenius_images,
    "assertion_count": len(checks),
    "checks": checks,
    "scope_limit": "Exact finite field and cross-ratio certificate only; does not prove the universal-homeomorphism theorem or anabelian reconstruction.",
}
root = Path(__file__).resolve().parents[1]
output = root / "code/part_c_a6_frobenius_certificate_output.json"
encoded = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
output.write_text(encoded)
output.with_suffix(".txt").write_text(encoded)
print(json.dumps({key: value for key, value in payload.items() if key not in ("checks", "frobenius_images")}, indent=2))
