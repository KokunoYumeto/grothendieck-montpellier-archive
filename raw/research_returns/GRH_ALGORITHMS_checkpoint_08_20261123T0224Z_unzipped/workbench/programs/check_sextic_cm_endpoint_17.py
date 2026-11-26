#!/usr/bin/env python3
"""Check the exact p=17 endpoint; this does not implement the CM/Pila algorithm.

Run: python3 check_sextic_cm_endpoint_17.py
Expected JSON: ../checks/sextic_cm_endpoint_17.json
Only Python's standard library is used. All arithmetic is exact.
"""
import json

p = 17


def multiply(a, b):
    return ((a[0]*b[0] - 3*a[1]*b[1]) % p,
            (a[0]*b[1] + a[1]*b[0]) % p)


def power(a, exponent):
    result = (1, 0)
    while exponent:
        if exponent & 1:
            result = multiply(result, a)
        a = multiply(a, a)
        exponent //= 2
    return result


u = 7
z = (12, 3)
roots = [x for x in range(p) if (x**3 - 3*x + 1) % p == 0]
values = [(x**3 - 3*x - u) % p for x in range(p)]
assert roots == [7, 13, 14]
assert pow(p - 3, (p - 1)//2, p) == p - 1
assert (multiply(z, z)[0] - u*z[0] + 1) % p == 0
assert (multiply(z, z)[1] - u*z[1]) % p == 0
assert power(z, 9) == (1, 0) and power(z, 3) != (1, 0)
assert 0 not in values  # a cubic over a field is irreducible iff it has no root
print(json.dumps({
    "p": p,
    "quadratic_presentation": "s^2+3=0",
    "real_cubic": "X^3-3X+1",
    "real_cubic_roots": roots,
    "chosen_root": u,
    "z": z,
    "z3": power(z, 3),
    "z6": power(z, 6),
    "z9": power(z, 9),
    "irreducible_cubic": "Y^3-3Y-7",
    "cubic_values_at_0_through_16": values,
    "scope": "Exact endpoint example; not an execution of theta recognition or Pila point counting.",
}, indent=2))
