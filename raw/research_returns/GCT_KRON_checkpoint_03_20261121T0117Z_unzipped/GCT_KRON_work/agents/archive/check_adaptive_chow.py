#!/usr/bin/env python3
"""Exact arithmetic checks for A-021 and A-022; standard library only."""
from math import isqrt
import csv
from pathlib import Path


def b_bound(degree, second_row):
    return second_row + sum(min(j, second_row) for j in range(2, degree))


def n_bound(degree, second_row):
    assert degree >= 2 and second_row >= 1
    value = 1
    for r in range(2, degree):
        shift = min(r, second_row)
        value = shift + max(value, min(r * shift - 1, second_row))
    return value


def maximum_bound(degree, second_row):
    assert second_row >= degree >= 2
    return degree * (degree - 1) // 2 + max(
        [0] + [min(j * j - 1, second_row) - j * (j - 1) // 2
               for j in range(2, degree)]
    )


def p_bound(degree, second_row):
    assert degree >= 2 and second_row >= 1
    value = 1
    for r in range(2, degree):
        shift = min(r, second_row)
        value = shift + max(value, min((r - 1) * shift, second_row))
    return value


def grouped_maximum_bound(degree, second_row):
    assert second_row >= degree >= 2
    triangular = lambda j: j * (j - 1) // 2
    return triangular(degree) + max(
        [0] + [min(triangular(j), second_row - triangular(j))
               for j in range(2, degree)]
    )


def grouped_two_candidate_bound(degree, second_row):
    assert second_row >= degree >= 2
    if degree == 2:
        return 1
    root = (1 + isqrt(1 + 4 * second_row)) // 2
    candidates = {min(degree - 1, root), min(degree - 1, root + 1)}
    triangular = lambda j: j * (j - 1) // 2
    return triangular(degree) + max(
        [0] + [min(triangular(j), second_row - triangular(j))
               for j in candidates]
    )


def two_candidate_bound(degree, second_row):
    assert second_row >= degree >= 2
    if degree == 2:
        return 1
    root = isqrt(second_row + 1)
    candidates = {min(degree - 1, root), min(degree - 1, root + 1)}
    return degree * (degree - 1) // 2 + max(
        [0] + [min(j * j - 1, second_row) - j * (j - 1) // 2
               for j in candidates]
    )


def verify():
    checks = []
    b_cases = 0
    for degree in range(2, 80):
        for second_row in range(80):
            value = b_bound(degree, second_row)
            if second_row == 0:
                closed = 0
            elif second_row < degree:
                closed = degree * second_row - second_row * (second_row - 1) // 2 - 1
            else:
                closed = second_row + degree * (degree - 1) // 2 - 1
            assert value == closed
            assert value <= (degree - 1) * second_row
            if degree >= 3:
                assert value == b_bound(degree - 1, second_row) + min(degree - 1, second_row)
            if second_row:
                assert value >= second_row
            b_cases += 1
    checks.append(("A-021", "sum_closed_form_recurrence", b_cases, "PASS"))

    n_cases = 0
    for degree in range(2, 100):
        previous = 0
        for second_row in range(1, 300):
            value = n_bound(degree, second_row)
            assert previous <= value <= b_bound(degree, second_row)
            assert value <= degree * (degree - 1) - 1
            previous = value
            if second_row >= degree:
                assert value == maximum_bound(degree, second_row)
                assert value == two_candidate_bound(degree, second_row)
                upper = degree * (degree - 1) // 2 + (second_row - 1 + isqrt(second_row + 1)) // 2
                assert value <= upper
            n_cases += 1
    checks.append(("A-022", "monotonicity_maximum_two_candidates_upper_bound", n_cases, "PASS"))

    p_cases = 0
    for degree in range(2, 100):
        previous = 0
        for second_row in range(1, 300):
            value = p_bound(degree, second_row)
            assert previous <= value <= n_bound(degree, second_row)
            assert value <= (degree - 1) ** 2
            previous = value
            if second_row >= degree:
                assert value == grouped_maximum_bound(degree, second_row)
                assert value == grouped_two_candidate_bound(degree, second_row)
                assert value <= degree * (degree - 1) // 2 + second_row // 2
            p_cases += 1
    checks.append(("A-023", "grouped_recurrence_maximum_two_candidates_upper_bound", p_cases, "PASS"))

    # Exact examples quantify the refinement; they are not proof of the theorem.
    for degree, second_row in [(10, 10), (100, 100), (100, 3000), (100, 5000), (1000, 26)]:
        checks.append(("A-022", f"example_d{degree}_L{second_row}",
                       f"B={b_bound(degree, second_row)};N={n_bound(degree, second_row)};P={p_bound(degree, second_row)}", "PASS"))
    return checks


if __name__ == "__main__":
    output = Path(__file__).with_name("CHOW_BOUND_CHECKS.tsv")
    rows = verify()
    with output.open("w", newline="") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(["finding", "check", "cases_or_values", "result"])
        writer.writerows(rows)
    print(f"All exact checks passed; wrote {output}")
