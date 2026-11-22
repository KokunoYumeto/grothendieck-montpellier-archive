"""Finite arithmetic certificate for B-RD25.

The extension, formal-group, and ramification assertions are proved in the
accompanying TeX.  This checks their exact integer and rational computations.
It does not test the existence of a new full-27 curve at absolute index 216.
"""
from fractions import Fraction
from pathlib import Path
import json
import time

started = time.perf_counter()
p, n, e, defect = 3, 2, 24, 12
good_e = e * defect
feasible = []
for region in range(n):
    coefficient = (p-1) * p**(2*n-region-2)
    for b in range(1, good_e+1):
        for a in range(3, good_e+1, 3):
            if a < p**(2*region)*b:
                continue
            if region < n-1 and a > p**(2*region+2)*b:
                continue
            if good_e == coefficient * (a+p**(2*region+1)*b):
                feasible.append({"region": region, "A": a, "B": b})
assert feasible == [{"region": 1, "A": 21, "B": 1}]

a, b = 21, 1
low_three = p*p*b
high_three = Fraction(good_e-(p*p-p)*low_three, p-1)
assert (low_three, high_three) == (9, 117)
divide_min = Fraction(b, p*p)
divide_max = Fraction(a, p*p)
assert (divide_min, divide_max) == (Fraction(1, 9), Fraction(7, 3))
assert divide_min < low_three and divide_max < low_three
assert p*p*low_three == 81

first_degree = 9
z_value = first_degree*divide_min
s_value = first_degree*divide_max
assert (z_value, s_value) == (1, 21)
translation_values = [first_degree*low_three, first_degree*high_three]
assert translation_values == [81, 1053]
high_break = translation_values[1]-1
forced_lower_bound = s_value+high_break
assert high_break == 1052 and forced_lower_bound == 1073
assert forced_lower_bound > max(translation_values)

epsilon_bound = 1053+2
v_three = good_e*first_degree
delta_value = translation_values[0]
norm_difference_terms = [v_three+2+delta_value,
                         v_three+1+2*delta_value, 3*delta_value]
assert norm_difference_terms == [2675, 2755, 243]
assert min(norm_difference_terms) < epsilon_bound
quotient_difference_value = Fraction(min(norm_difference_terms), 3)
quotient_break = quotient_difference_value-1
assert quotient_break == 80
quotient_s_value = Fraction(s_value, 3)
assert quotient_s_value == 7 and quotient_s_value.numerator % 3 != 0
forced_difference = quotient_s_value+quotient_break
available_translation_values = [3*low_three, 3*high_three]
assert forced_difference == 87
assert available_translation_values == [27, 351]
assert forced_difference not in available_translation_values

result = {
    "status": "PASS",
    "arithmetic": "exact integer and Fraction arithmetic",
    "scope": "base change of e24 full9 curves; direct e216 full27 remains open",
    "good_absolute_index": good_e,
    "feasible_primitive9_extrema": feasible,
    "three_torsion_slopes": [str(low_three), str(high_three)],
    "next_division_slopes": [str(divide_min), str(divide_max)],
    "first_division_degree": first_degree,
    "translation_values": [str(x) for x in translation_values],
    "high_subgroup_break": str(high_break),
    "high_subgroup_difference_lower_bound": str(forced_lower_bound),
    "norm_correction_lower_bound": epsilon_bound,
    "norm_difference_term_valuations": norm_difference_terms,
    "quotient_break": str(quotient_break),
    "quotient_maximum_division_slope": str(quotient_s_value),
    "forced_difference": str(forced_difference),
    "available_translation_values": [str(x) for x in available_translation_values],
    "minimum_full_next_division_degree": 27,
    "elapsed_seconds": time.perf_counter()-started,
}
output = Path(__file__).with_name("verify_level27_basechange_obstruction.output.json")
output.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
