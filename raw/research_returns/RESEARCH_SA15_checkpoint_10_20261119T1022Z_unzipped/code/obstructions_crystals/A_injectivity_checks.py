"""Exact integer certificate for the two normalized Tango covers.

The program checks arithmetic identities and finite bounds used in the proof;
smoothness, descent, cohomological identifications, and generic existence are
proved in A_injectivity_counterexample.tex, not inferred from computation.
"""
from fractions import Fraction
from pathlib import Path
import json
import time

started = time.perf_counter()

def ceil_div(a, b):
    return -((-a) // b)

g = 421
assert 2 * g - 2 == 840
assert 843 == 2 * 422 - 1
assert 420 == 21 * 20
assert 210 == 21 * 10
assert 20 == 2 * 10
assert 10 == 5 * 2
assert 4 == 2 * 2

floor_checks = 0
for k in (21, 5):
    for a in range(-1000, 1001):
        for i in range(k):
            assert -i + ((a + (k - 2) * i) // k) == (a - 2 * i) // k
            floor_checks += 1

assert [i for i in range(21) if (2 - 2 * i) // 21 >= 0] == [0, 1]
assert [i for i in range(5) if (2 - 2 * i) // 5 >= 0] == [0, 1]
first_relative_degrees = [42 - ceil_div(2*i, 21) for i in range(21)]
first_base_exponents = [441 + 20*i for i in range(21)]
second_relative_degrees = [178 - ceil_div(2*j, 5) for j in range(5)]
second_base_exponents = [445 + 4*j for j in range(5)]
assert min(first_relative_degrees) == 40
assert min(first_base_exponents) == 441
assert 2 * 441 > 2 * g + 1
assert min(second_relative_degrees) == 176
assert min(second_base_exponents) == 445
assert 441 % 21 == 0 and 445 % 5 == 0

def h0_l2(t):
    assert t >= 441
    result = 0
    for i in range(21):
        a = 2 * (t-i) // 21
        assert a >= 40
        assert 2 * (t+20*i) > 2*g-2
        result += (a+1)*(2*t+40*i+1-g) + 210*a*(a+1)
    return result

second_counts = []
for j in range(5):
    a = 2*(445-j)//5
    b = 445+4*j
    second_counts.append(sum(h0_l2(b+10*h) for h in range(a+1)))
assert h0_l2(441) == 8189386
assert sum(second_counts) == 79232578014
assert second_counts == [15939762050, 15806658456, 15889770216,
                         15756777770, 15839609522]

betti = 2*g
root_count = betti+1
assert (betti, root_count) == (842, 843)
assert root_count > 2*3+1
assert root_count > betti

result = {
    "status": "PASS",
    "arithmetic": "exact integers only",
    "normalization_floor_identities_checked": floor_checks,
    "curve": {"characteristic": 2, "exponent": 843,
              "genus": g, "differential_divisor_degree": 840},
    "first_step": {"cyclic_degree": 21, "very_ample_power": 441,
                   "minimum_relative_degree": min(first_relative_degrees),
                   "minimum_base_degree": 2*min(first_base_exponents),
                   "h0_L2_441": h0_l2(441)},
    "second_step": {"cyclic_degree": 5, "very_ample_power": 445,
                    "minimum_relative_degree": min(second_relative_degrees),
                    "minimum_base_exponent": min(second_base_exponents),
                    "eigensummand_h0_L_445": second_counts,
                    "h0_L_445": sum(second_counts)},
    "amplification": {"root_exponent": 445, "number_of_roots": root_count,
                      "cover_degree": "445^843", "first_betti_number": betti,
                      "coherent_kernel_dimension_lower_bound": root_count,
                      "strict_dimension_margin": root_count-betti},
    "elapsed_seconds": time.perf_counter()-started,
}
output = Path(__file__).with_name("A_injectivity_checks_output.json")
output.write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))
