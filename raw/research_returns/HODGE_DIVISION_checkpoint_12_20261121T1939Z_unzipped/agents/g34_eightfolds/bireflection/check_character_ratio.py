#!/usr/bin/env python3
"""Exact arithmetic for D-BI18/18a; no finite-group classification is computed."""
from fractions import Fraction
from math import ceil
from pathlib import Path
import json


def possible_degrees(c, upper, factor=4, esd=False):
    result = []
    for e in range(3, upper + 1):
        minimum = ceil(Fraction(e, factor) * (1 - c))
        moving = 2 * ceil(Fraction(e, 2)) + 10 * minimum if esd else 12 * minimum
        if moving <= 2 * e + 6:
            result.append(e)
    return result


small_fields = []
for q, expected in zip([29, 31, 32, 37, 41, 43], [87, 45, 33, 21, 15, 15]):
    # 9/q >= 1/(sqrt(q)-1) is exactly this positive squared comparison.
    assert (q + 9) ** 2 <= 81 * q
    c = Fraction(9, q)
    upper = int(Fraction(6, 1) / (1 - 3 * c))
    degrees = possible_degrees(c, upper)
    assert max(degrees) == expected
    small_fields.append(dict(q=q, c=str(c), continuous_max=upper,
                             integer_max=max(degrees), possible_degrees=degrees))

# For q>=47 both decreasing terms of c(q) are strictly below 1/5.
assert 47 > 45 and 47 > 36
# The strict inequality c<1/5 means the integer minimum is floor(e/5)+1.
large_field_degrees = [e for e in range(3, 15) if 12 * (e // 5 + 1) <= 2 * e + 6]
assert large_field_degrees == [3, 4, 9]

# Extraspecial characters vanish away from scalars; the continuous bound is e<=6.
extraspecial_degrees = possible_degrees(Fraction(0), 6)
assert extraspecial_degrees == [3, 4]

# q>=16: c(q)<=9/16; e<=48/5 under the scalar-only estimate.
assert Fraction(1, 3) <= Fraction(9, 16)
scalar_upper = Fraction(6, 1) / (4 - 6 * Fraction(9, 16))
assert scalar_upper == Fraction(48, 5)
scalar_degrees = possible_degrees(Fraction(9, 16), int(scalar_upper), factor=2)
assert scalar_degrees == [3, 4, 9]
# q>=29: both terms are <1/3, so e<3, contradicting e>=3.
assert 29 > 27 and 29 > 16

# q>=19: both terms are <1/2; the ESD continuous bound is e<24.
assert 19 > 18 and 19 > 9
# At the weakest exact bound c(19)=9/19, the integer candidates below 24
# are a proper subset; D-BI09 removes every primitive nonsplit degree >=9.
assert (19 + 9) ** 2 <= 81 * 19
esd_upper = int(Fraction(12, 1) / (3 - 5 * Fraction(9, 19)))
esd_degrees = possible_degrees(Fraction(9, 19), esd_upper, esd=True)
assert esd_upper < 24

output = dict(status="PASS", small_fields=small_fields,
              q_at_least_47_necessary_degrees=large_field_degrees,
              extraspecial_necessary_degrees=extraspecial_degrees,
              scalar_q_at_least_16_degrees=scalar_degrees,
              scalar_q_at_least_29="no degree e>=3",
              esd_q19_continuous_max=esd_upper,
              esd_q19_integer_degrees=esd_degrees,
              scope="Exact ceiling arithmetic only. Group-character bounds are published inputs; geometry and support estimates are proved in the section.")
path = Path(__file__).with_suffix('.json')
path.write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps(output, indent=2))
