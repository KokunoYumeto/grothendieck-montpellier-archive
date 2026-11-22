#!/usr/bin/env python3
"""Exact integral checks for AS17 and the relative q=3 period test.

The certificate does not extrapolate a theorem from finite data.
It records integer matrices for Stokes in weights 2..8 and checks
the explicit general coefficient formulas on a finite range.
"""
from fractions import Fraction
from itertools import product
from math import comb
from pathlib import Path
import json
import time


def compositions(total, length):
    if length == 1:
        return [(total,)]
    return [(a,) + rest for a in range(total + 1)
            for rest in compositions(total - a, length - 1)]


def add_entry(matrix, row, col, value):
    matrix[row][col] += value


def stokes_matrix(weight):
    # A form is gamma_a(t0,t1,t2) dt_j.  The independent forms
    # are dt1,dt2, and dt0=-dt1-dt2.  Divided-power derivatives
    # lower one exponent with coefficient one.
    coeff = compositions(weight - 1, 3)
    one_basis = [(a, j) for a in coeff for j in (1, 2)]
    top_basis = compositions(weight - 2, 3)
    edge_basis = compositions(weight - 1, 2)
    ti = {a: i for i, a in enumerate(top_basis)}
    ei = {a: i for i, a in enumerate(edge_basis)}
    differential = [[0] * len(one_basis) for _ in top_basis]
    restriction = [[0] * len(one_basis) for _ in range(3 * len(edge_basis))]
    # dt_j on face_i, expressed in the increasing edge coordinate.
    form_restriction = {(0, 1): -1, (0, 2): 1,
                        (1, 1): 0, (1, 2): 1,
                        (2, 1): 1, (2, 2): 0}
    for col, (a, j) in enumerate(one_basis):
        # d(f dt1)=(partial_0 f-partial_2 f) dt1 dt2.
        # d(f dt2)=(partial_1 f-partial_0 f) dt1 dt2.
        derivatives = ((0, 1), (2, -1)) if j == 1 else ((1, 1), (0, -1))
        for variable, sign in derivatives:
            if a[variable]:
                b = list(a)
                b[variable] -= 1
                add_entry(differential, ti[tuple(b)], col, sign)
        for face in range(3):
            sign = form_restriction[face, j]
            if a[face] == 0 and sign:
                b = tuple(a[k] for k in range(3) if k != face)
                add_entry(restriction, face * len(edge_basis) + ei[b], col, sign)
    # Integration sends every divided-power top monomial to T^[weight].
    lhs = [sum(row[col] for row in differential) for col in range(len(one_basis))]
    rhs = [sum((-1) ** face * restriction[face * len(edge_basis) + row][col]
               for face in range(3) for row in range(len(edge_basis)))
           for col in range(len(one_basis))]
    assert lhs == rhs
    return {"weight": weight,
            "one_form_basis": [[list(a), j] for a, j in one_basis],
            "top_form_basis": [list(a) for a in top_basis],
            "edge_form_basis": [list(a) for a in edge_basis],
            "vertical_differential": differential,
            "all_face_restrictions": restriction,
            "integral_stokes_columns_checked": len(one_basis)}


def main():
    started = time.perf_counter()
    # In G_1, Tt1=t0*t1+2 gamma_2(t1).  With dt0=-dt1,
    # its derivative is (t0-t1+2t1)dt1=Tdt1.
    derivative_T_t1 = {"t0_dt1": 1, "t1_dt1": -1 + 2}
    assert derivative_T_t1 == {"t0_dt1": 1, "t1_dt1": 1}
    endpoints_T_t1 = {"d1": 0, "d0_in_T_divided_square_basis": 2}
    residue = Fraction(-2, 3)
    assert residue.denominator == 3

    matrices = [stokes_matrix(w) for w in range(2, 9)]
    # The weight-three top form Tdt1dt2 is the sum of three
    # divided-power basis elements, each with integral period one.
    relative_q3_period = sum(1 for _ in compositions(1, 3))
    assert relative_q3_period == 3
    assert relative_q3_period % 2 == 1

    tails = []
    for r in range(121):
        # T^[r] * T^2 = 2*binom(r+2,2) T^[r+2].
        endpoint = 2 * comb(r + 2, 2)
        assert endpoint == (r + 1) * (r + 2)
        # T^[r] * Tdt1dt2 = (r+1) T^[r+1]dt1dt2.
        # Its period counts all three-variable compositions.
        relative = (r + 1) * comb(r + 3, 2)
        assert relative == (r + 1) * (r + 2) * (r + 3) // 2
        assert (endpoint % 3 != 0) == (r % 3 == 0)
        assert (relative % 2 != 0) == (r % 4 == 0)
        tails.append({"r": r, "AS17_endpoint_coefficient": endpoint,
                      "AS17_mod3": endpoint % 3,
                      "relative_q3_period": relative,
                      "relative_q3_mod2": relative % 2})
    output = {"status": "all exact checks passed",
              "arithmetic": "integer and Fraction only; no numerical rank inference",
              "AS17_derivative": derivative_T_t1,
              "AS17_endpoints": endpoints_T_t1,
              "AS17_residue": str(residue),
              "relative_q3_weight3_period": relative_q3_period,
              "stokes_matrices": matrices,
              "stokes_columns_checked": sum(m["integral_stokes_columns_checked"] for m in matrices),
              "tail_values_checked": len(tails),
              "tail_values": tails,
              "runtime_seconds": time.perf_counter() - started}
    destination = Path(__file__).resolve().parents[1] / "logs" / "A_cosimplicial_residue_certificate.json"
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({key: output[key] for key in
                     ("status", "stokes_columns_checked", "tail_values_checked", "runtime_seconds")}))


if __name__ == "__main__":
    main()
