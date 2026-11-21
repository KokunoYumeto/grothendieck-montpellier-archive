"""Independent standard-library check of A20 by Frobenius power sums.

No imports from either A20 producer or resultant verifier. The Jacobian
order is obtained from Newton recurrence, not a companion determinant
or a polynomial resultant.
"""
from pathlib import Path
import json


P = [4, 2, 0, 1, 1]  # ascending coefficients of T^4+T^3+2T+4
Q = [0] * 17
for degree in (16, 14, 12, 11, 10, 5):
    Q[degree] = 1
for degree in (15, 6, 4, 2, 1, 0):
    Q[degree] = -1
product = [0] * 21
for i, a in enumerate(P):
    for j, b in enumerate(Q):
        product[i + j] = (product[i + j] + a * b) % 3
target = [2] + [0] * 19 + [1]
assert product == target

# Newton identities: initial sums s0=4, s1=-1, s2=1, s3=-7.
# For m>=4, the characteristic equation gives
# s_m=-s_(m-1)-2*s_(m-3)-4*s_(m-4).
traces = [4, -1, 1, -7]
for m in range(4, 41):
    traces.append(-traces[m - 1] - 2 * traces[m - 3] - 4 * traces[m - 4])
assert traces[4] == -7

m = 20
Qm = 2**m
s_m, s_2m = traces[m], traces[2 * m]
assert (s_m * s_m - s_2m) % 2 == 0
second_coefficient = (s_m * s_m - s_2m) // 2
order = 1 - (1 + Qm) * s_m + second_coefficient + Qm * Qm
assert order == 1099812538656
cofactor, valuation = order, 0
while cofactor % 3 == 0:
    cofactor //= 3
    valuation += 1
assert (valuation, cofactor) == (4, 13577932576)
assert cofactor % 3 == 1

result = {
    "status": "PASS",
    "method": "Newton power-sum recurrence and Weil functional equation",
    "imports_producer_or_other_verifier": False,
    "frobenius_polynomial_ascending": P,
    "exponent": m,
    "power_sum_20": s_m,
    "power_sum_40": s_2m,
    "second_weil_coefficient_over_F2_20": second_coefficient,
    "jacobian_order_F2_20": order,
    "valuation_at_3": valuation,
    "prime_to_3_cofactor": cofactor,
    "modular_quotient_ascending": [a % 3 for a in Q],
    "P_times_Q_equals_T20_minus_one_mod3": True,
    "formal_proof_assistant_verification": False,
}
Path(__file__).with_name("A20_recurrence_check.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print(json.dumps(result, indent=2))
