#!/usr/bin/env python3
"""G-020: exact positive coefficients, active polytopes, and bounded witnesses.

Only the Python standard library is required.  The 36 Newton constants
are calculated from fixed formulas with trace indices at most 717;
there is no lookup-table file and no loop whose length depends on a,k,t,d.

Example:
  python five_point_three_parameter_positive.py --a 2 --k 3 --t 1 --d 0
  python five_point_three_parameter_positive.py --a 61 --k 0 --t 0 --d 0 --polytopes
  python five_point_three_parameter_positive.py --a 2 --k 3 --t 1 --d 0 --witnesses 10

Witness enumeration is optional and is bounded by the requested limit.
The Python witnesses() generator can also be used without a limit.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import json
from math import comb
import sys
from typing import Iterator

PERIOD = 60
MAX_CONSTANT = 1_021_264_200
LABELS = ((5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1),
          (2, 1, 1, 1), (1, 1, 1, 1, 1))
CLASS_SIZES = (1, 10, 15, 20, 20, 30, 24)
FIXED_LETTERS = (5, 3, 1, 2, 0, 1, 0)
CHARACTERS = {
    (5,): (1, 1, 1, 1, 1, 1, 1),
    (4, 1): (4, 2, 0, 1, -1, 0, -1),
    (3, 2): (5, 1, 1, -1, 1, -1, 0),
    (3, 1, 1): (6, 0, -2, 0, 0, 0, 1),
    (2, 2, 1): (5, -1, 1, -1, -1, 1, 0),
    (2, 1, 1, 1): (4, -2, 0, 1, 1, 0, -1),
    (1, 1, 1, 1, 1): (1, -1, 1, 1, -1, -1, 1),
}
ACTIVE_ORDERS = tuple(
    (i, j, ell)
    for i in range(4)
    for j in range(4)
    for ell in range(4)
    if j + ell <= 3 and i + j + ell <= 5
)
assert len(ACTIVE_ORDERS) == 36


def transpose(partition: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(part >= j for part in partition)
                 for j in range(1, max(partition, default=0) + 1))


def _label(outer) -> tuple[int, ...]:
    try:
        label = tuple(outer)
    except TypeError as exc:
        raise ValueError("outer must be a partition of five") from exc
    if any(type(part) is not int for part in label) or label not in CHARACTERS:
        raise ValueError("outer must be a partition of five, such as (5,) or (3,2)")
    return label


def parameters(a: int, k: int, t: int, d: int, outer=(5,)):
    """Return (outer, effective_label, inner_degree, output_partition)."""
    if any(type(value) is not int or value < 0 for value in (a, k, t, d)):
        raise ValueError("a, k, t, and d must be nonnegative integers")
    outer = _label(outer)
    effective = transpose(outer) if (d + a) % 2 else outer
    n = d + a + k + t
    lam = (d + 2*a + 3*k + 4*t, d + a + 2*k + t,
           d + a, d + a, d)
    return outer, effective, n, tuple(part for part in lam if part)


def trace(class_index: int, n: int) -> int:
    """The seven elementary h_n functions in TP.8; negative indices are zero."""
    if type(class_index) is not int or not 0 <= class_index < 7:
        raise ValueError("class_index must be an integer from zero through six")
    if type(n) is not int:
        raise ValueError("trace degree must be an integer")
    if n < 0:
        return 0
    if class_index == 0:
        return (n + 1) * (n + 2) * (n + 3) // 6
    if class_index == 1:
        return (n // 2 + 1) * ((n + 1) // 2 + 1)
    if class_index == 2:
        return n // 2 + 1 if n % 2 == 0 else 0
    if class_index == 3:
        return n // 3 + 1
    if class_index == 4:
        return (1, -1, 1, 0, 0, 0)[n % 6]
    if class_index == 5:
        return int(n % 4 == 0)
    return (1, -1, 0, 0, 0)[n % 5]


@lru_cache(maxsize=7 * 719)
def _fixed_trace(class_index: int, n: int) -> int:
    if not -1 <= n <= 717:
        raise ArithmeticError("fixed-constant trace index escaped its proved range")
    return trace(class_index, n)


def _difference(g: int, base: int, step: int, order: int) -> int:
    return sum((-1)**(order-u) * comb(order, u) *
               _fixed_trace(g, base + step*u)
               for u in range(order + 1))


def _mixed_difference(g: int, base: int, j: int, ell: int) -> int:
    return sum(
        (-1)**(j+ell-u-v) * comb(j, u) * comb(ell, v) *
        _fixed_trace(g, base + 120*u + 60*v)
        for u in range(j + 1) for v in range(ell + 1)
    )


@lru_cache(maxsize=512)
def _constants(effective: tuple[int, ...], ra: int, rk: int, rt: int) -> tuple[int, ...]:
    """TP.9--TP.11, in the fixed ACTIVE_ORDERS order."""
    class_data = []
    pair_orders = tuple((j, ell) for j in range(4) for ell in range(4)
                        if j + ell <= 3)
    for g in range(7):
        a0 = tuple(_difference(g, ra, 60, i) for i in range(4))
        a1 = tuple(_difference(g, ra-1, 60, i) for i in range(4))
        jets = tuple(_difference(g, rk-1, 60, j) for j in range(4))
        b0 = {(j, ell): _mixed_difference(g, 2*rk+rt, j, ell)
              for j, ell in pair_orders}
        b1 = {(j, ell): _mixed_difference(g, 2*rk+rt-1, j, ell)
              for j, ell in pair_orders}
        class_data.append((a0, a1, jets, b0, b1))
    result = []
    weights = tuple(size * char for size, char in
                    zip(CLASS_SIZES, CHARACTERS[effective]))
    for i, j, ell in ACTIVE_ORDERS:
        numerator = 0
        for g, (a0, a1, jets, b0, b1) in enumerate(class_data):
            value = a0[i] * b0[j, ell] - a1[i] * b1[j, ell]
            if ell == 0:
                value -= FIXED_LETTERS[g] * (a0[i] - a1[i]) * jets[j]
            numerator += weights[g] * value
        value, remainder = divmod(numerator, 120)
        if remainder or not 0 <= value <= MAX_CONSTANT:
            raise ArithmeticError("a fixed Newton constant failed its proved integral bounds")
        result.append(value)
    return tuple(result)


def newton_constants(effective, ra: int, rk: int, rt: int):
    """Return the 36 fixed constants for a valid effective label and residues."""
    effective = _label(effective)
    if any(type(r) is not int or not 0 <= r < PERIOD for r in (ra, rk, rt)):
        raise ValueError("residues must be integers from zero through 59")
    return dict(zip(ACTIVE_ORDERS, _constants(effective, ra, rk, rt)))


def _terms(a: int, k: int, t: int, effective: tuple[int, ...]):
    quotients = (a // PERIOD, k // PERIOD, t // PERIOD)
    residues = (a % PERIOD, k % PERIOD, t % PERIOD)
    constants = _constants(effective, *residues)
    binomials = tuple(tuple(comb(q, degree) for degree in range(4))
                      for q in quotients)
    terms = tuple(
        (orders, constant,
         constant * binomials[0][orders[0]] *
         binomials[1][orders[1]] * binomials[2][orders[2]])
        for orders, constant in zip(ACTIVE_ORDERS, constants)
    )
    return quotients, residues, terms


def coefficient(a: int, k: int, t: int, d: int, outer=(5,)) -> int:
    """Exact coefficient from 36 positive Newton terms."""
    _, effective, _, _ = parameters(a, k, t, d, outer)
    return sum(value for _, _, value in _terms(a, k, t, effective)[2])


def polytopes(a: int, k: int, t: int, d: int, outer=(5,)):
    """Export TP.14 for the selected residues.

    Zero constants are omitted. Other empty subset-chain tags are retained.
    Every equality is [row, rhs]; every inequality means row.dot(point)<=rhs.
    """
    _, effective, _, _ = parameters(a, k, t, d, outer)
    _, residues, terms = _terms(a, k, t, effective)
    result = []
    for (i, j, ell), constant, count in terms:
        if constant == 0:
            continue
        variables = (["qa", "qk", "qt", "y"] +
                     [f"x{h}" for h in range(1, i+1)] +
                     [f"z{h}" for h in range(1, j+1)] +
                     [f"w{h}" for h in range(1, ell+1)])
        size = len(variables)
        equalities = []
        for axis, (value, residue) in enumerate(zip((a, k, t), residues)):
            row = [0] * size
            row[axis] = PERIOD
            equalities.append([row, value-residue])
        inequalities = []
        for axis in range(4):
            row = [0] * size
            row[axis] = -1
            inequalities.append([row, 0])
        row = [0] * size
        row[3] = 1
        inequalities.append([row, constant-1])
        start = 4
        for length, upper_axis in ((i, 0), (j, 1), (ell, 2)):
            if length:
                row = [0] * size
                row[start] = -1
                inequalities.append([row, -1])
                for h in range(length-1):
                    row = [0] * size
                    row[start+h] = 1
                    row[start+h+1] = -1
                    inequalities.append([row, -1])
                row = [0] * size
                row[start+length-1] = 1
                row[upper_axis] = -1
                inequalities.append([row, 0])
            start += length
        assert size <= 9
        result.append({
            "residues": list(residues), "orders": [i, j, ell],
            "constant": constant, "variables": variables,
            "equalities": equalities, "inequalities": inequalities,
            "inequality_convention": "row dot point <= rhs",
            "lattice_count": count,
        })
    assert len(result) <= 36
    return result


def _increasing_tuples(upper: int, length: int, start: int = 1,
                       prefix: tuple[int, ...] = ()) -> Iterator[tuple[int, ...]]:
    """Lazy subsets without materializing range(upper), including huge upper."""
    if length == 0:
        yield prefix
        return
    for value in range(start, upper-length+2):
        yield from _increasing_tuples(upper, length-1, value+1, prefix+(value,))


def witnesses(a: int, k: int, t: int, d: int, outer=(5,), limit: int | None = None):
    """Yield distinct tagged TP.14 integer points; a limit bounds output."""
    parameters(a, k, t, d, outer)
    if limit is not None and (type(limit) is not int or limit < 0):
        raise ValueError("witness limit must be a nonnegative integer")
    if limit == 0:
        return
    qa, qk, qt = a // PERIOD, k // PERIOD, t // PERIOD
    emitted = 0
    for poly in polytopes(a, k, t, d, outer):
        if poly["lattice_count"] == 0:
            continue
        i, j, ell = poly["orders"]
        for xs in _increasing_tuples(qa, i):
            for zs in _increasing_tuples(qk, j):
                for ws in _increasing_tuples(qt, ell):
                    for y in range(poly["constant"]):
                        yield {
                            "residues": poly["residues"], "orders": poly["orders"],
                            "variables": poly["variables"],
                            "point": [qa, qk, qt, y, *xs, *zs, *ws],
                        }
                        emitted += 1
                        if limit is not None and emitted >= limit:
                            return


def evaluate(a: int, k: int, t: int, d: int, outer=(5,),
             include_polytopes: bool = False, include_terms: bool = False,
             witness_limit: int | None = None):
    outer, effective, n, lam = parameters(a, k, t, d, outer)
    quotients, residues, terms = _terms(a, k, t, effective)
    value = sum(term[2] for term in terms)
    result = {
        "statement": "G-020",
        "parameters": {"a": a, "k": k, "t": t, "d": d},
        "outer": list(outer), "effective_label": list(effective),
        "inner": n, "lambda": list(lam), "coefficient": value,
        "positive": value > 0,
        "residues": list(residues), "quotients": list(quotients),
        "fixed_tag_bound": 36,
        "nonempty_tag_count": sum(count > 0 for _, _, count in terms),
    }
    if include_terms:
        result["newton_terms"] = [
            {"orders": list(order), "constant": c, "contribution": count}
            for order, c, count in terms
        ]
    if include_polytopes:
        result["polytopes"] = polytopes(a, k, t, d, outer)
    if witness_limit is not None:
        points = list(witnesses(a, k, t, d, outer, witness_limit))
        result["witnesses"] = points
        result["witness_count"] = len(points)
        result["witnesses_truncated"] = len(points) < value
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("a", "k", "t", "d"):
        parser.add_argument("--"+name, required=True, type=int)
    parser.add_argument("--outer", default="5",
                        help="partition of five, for example 5 or 3,2")
    parser.add_argument("--terms", action="store_true",
                        help="include all 36 fixed constants and contributions")
    parser.add_argument("--polytopes", action="store_true",
                        help="export the active-residue bounded matrix descriptions")
    parser.add_argument("--witnesses", nargs="?", const=20, type=int, metavar="LIMIT",
                        help="include at most LIMIT literal points (default 20)")
    args = parser.parse_args(argv)
    try:
        outer = tuple(int(part) for part in args.outer.replace(",", " ").split())
        result = evaluate(args.a, args.k, args.t, args.d, outer,
                          args.polytopes, args.terms, args.witnesses)
    except (TypeError, ValueError) as exc:
        parser.error(str(exc))
    # Exact integer outputs can legitimately exceed Python's decimal-print cap.
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
