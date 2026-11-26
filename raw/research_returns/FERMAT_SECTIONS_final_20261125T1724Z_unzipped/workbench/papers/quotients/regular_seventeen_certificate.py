#!/usr/bin/env python3
"""Exact standard-library replay of the finite p=17 checks only."""
from fractions import Fraction
from math import comb
import json

p = 17
bernoulli = [Fraction(1)]
for m in range(1, p - 2):
    bernoulli.append(-sum(Fraction(comb(m + 1, k)) * bernoulli[k]
                         for k in range(m)) / (m + 1))
even = {m: bernoulli[m] for m in range(2, p - 1, 2)}
expected = [Fraction(1, 6), Fraction(-1, 30), Fraction(1, 42),
            Fraction(-1, 30), Fraction(5, 66), Fraction(-691, 2730),
            Fraction(7, 6)]
assert list(even.values()) == expected
assert all(b.numerator % p for b in even.values())
errors = [(pow(a, p, p*p) + pow((1-a) % p, p, p*p) - 1) % (p*p)
          for a in range(p)]
expected_errors = [0, 0, 153, 68, 102, 119, 170, 34, 34, 68, 34, 34,
                   170, 119, 102, 68, 153]
assert errors == expected_errors
roots = [a for a, e in enumerate(errors) if e == 0]
assert roots == [0, 1]
wild_check = pow(4, p-1, p*p)
assert wild_check == 154 and wild_check != 1
print(json.dumps({"prime": p,
                  "even_Bernoulli": {str(m): str(b) for m, b in even.items()},
                  "regular_by_full_class_number_Kummer_criterion": True,
                  "residue_errors_mod_289": errors,
                  "residue_roots": roots,
                  "4_power_16_mod_289": wild_check,
                  "all_assertions": "PASS"}, indent=2))
