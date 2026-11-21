"""Finite arithmetic checks for H9-C1; not a proof of the geometric claims."""
from fractions import Fraction
from math import comb

for m in range(2, 13):
    self_intersection = sum(comb(m + 1, k) * (-2) ** (m - k) for k in range(m + 1))
    expected = Fraction(1 + (-1) ** m, 2)
    assert self_intersection == expected
    cross = 1 - self_intersection
    delta_square = 2 * (self_intersection - cross)
    base_delta_square = 2 * (-1) ** (m - 1)
    exceptional_square = -base_delta_square
    assert delta_square == exceptional_square == 2 * (-1) ** m
    u_square = delta_square + exceptional_square
    u_cross = -delta_square + exceptional_square
    local = Fraction(delta_square ** 2, u_square)
    assert u_square == 4 * (-1) ** m
    assert u_cross == 0
    assert local == (-1) ** m
    assert (-1) ** m * (delta_square - 2 * local) == 0
    print(f"m={m}: plane_self={self_intersection}, delta2={delta_square}, "
          f"exceptional2={exceptional_square}, local_signed={(-1)**m*local}, "
          "corrected_height=0")
print("All 11 finite sign checks passed. This is not a formal certificate.")
