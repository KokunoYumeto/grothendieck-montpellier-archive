#!/usr/bin/env python3
"""G-021: positive five-parameter coefficients and explicit bounded polytopes.

This standalone Python-standard-library evaluator computes 122 fixed
Newton constants from seven elementary trace functions. It needs no
table file. Trace indices in its fixed calculation never exceed 539.

Example:
  python five_point_two_row_positive.py --x 1 --b 2 --k 1 --t 0 --d 0
  python five_point_two_row_positive.py --x 61 --b 2 --k 1 --t 0 --d 0 --polytopes --witnesses 10
"""
from __future__ import annotations

import argparse
from functools import lru_cache
import json
from math import comb
import sys
from typing import Iterator

PERIOD = 60
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
# TR.10, identical to the 122-element downset in the exact certificate.
_SHAPE_BOUNDS = (
    ((0, 0), 3), ((1, 0), 3), ((0, 1), 3), ((2, 0), 3),
    ((0, 2), 3), ((1, 1), 3), ((2, 1), 3), ((1, 2), 3),
    ((3, 0), 2), ((0, 3), 2), ((3, 1), 2), ((2, 2), 2), ((1, 3), 2),
    ((0, 4), 1), ((1, 4), 1), ((2, 3), 1), ((3, 2), 1),
)
ACTIVE_ORDERS = tuple(sorted(
    (ix, ib, jk, jt)
    for (ix, ib), bound in _SHAPE_BOUNDS
    for jk in range(bound + 1) for jt in range(bound + 1 - jk)
))
SHAPE_ORDERS = tuple(sorted(pair for pair, _ in _SHAPE_BOUNDS))
SCALAR_ORDERS = tuple((j, ell) for j in range(4) for ell in range(4-j))
assert len(ACTIVE_ORDERS) == 122 and max(map(sum, ACTIVE_ORDERS)) == 6


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


def parameters(x: int, b: int, k: int, t: int, d: int, outer=(5,)):
    """Return (outer, effective_label, inner_degree, output_partition)."""
    if any(type(value) is not int or value < 0 for value in (x, b, k, t, d)):
        raise ValueError("x, b, k, t, and d must be nonnegative integers")
    outer = _label(outer)
    effective = transpose(outer) if (d+b+x) % 2 else outer
    n = d+b+x+k+t
    lam = (d+3*b+2*x+3*k+4*t, d+b+x+2*k+t, d+b+x, d+x, d)
    return outer, effective, n, tuple(part for part in lam if part)


def trace(class_index: int, n: int) -> int:
    """TP.8, including the zero negative-index convention."""
    if type(class_index) is not int or not 0 <= class_index < 7:
        raise ValueError("class_index must be an integer from zero through six")
    if type(n) is not int:
        raise ValueError("trace degree must be an integer")
    if n < 0:
        return 0
    if class_index == 0:
        return (n+1)*(n+2)*(n+3)//6
    if class_index == 1:
        return (n//2+1)*((n+1)//2+1)
    if class_index == 2:
        return n//2+1 if n % 2 == 0 else 0
    if class_index == 3:
        return n//3+1
    if class_index == 4:
        return (1, -1, 1, 0, 0, 0)[n % 6]
    if class_index == 5:
        return int(n % 4 == 0)
    return (1, -1, 0, 0, 0)[n % 5]


@lru_cache(maxsize=7 * 542)
def _h(g: int, n: int) -> int:
    if not -2 <= n <= 539:
        raise ArithmeticError("a fixed trace index escaped its proved range")
    return trace(g, n)


def _schur(g: int, aa: int, bb: int) -> int:
    # This determinant also gives zero for every omitted boundary term.
    return _h(g, aa)*_h(g, bb)-_h(g, aa+1)*_h(g, bb-1)


def _shape(g: int, x: int, b: int) -> tuple[int, int, int]:
    a = b+x
    s0 = _schur(g, a, b)
    s1 = _schur(g, a-1, b)+_schur(g, a, b-1)
    zz = _schur(g, a-1, b-1)
    return s0-s1+zz, s1-2*zz, zz


def _scalar_difference(g: int, base: int, jk: int, jt: int) -> int:
    return sum(
        (-1)**(jk+jt-u-v)*comb(jk, u)*comb(jt, v)*
        _h(g, base+120*u+60*v)
        for u in range(jk+1) for v in range(jt+1)
    )


@lru_cache(maxsize=256)
def _constants(effective: tuple[int, ...], rx: int, rb: int,
               rk: int, rt: int) -> tuple[int, ...]:
    class_data = []
    for g in range(7):
        shape_grid = [[_shape(g, rx+60*u, rb+60*v)
                       for v in range(5)] for u in range(4)]
        shape_diff = {}
        for ix, ib in SHAPE_ORDERS:
            values = [0, 0, 0]
            for u in range(ix+1):
                for v in range(ib+1):
                    weight = (-1)**(ix+ib-u-v)*comb(ix, u)*comb(ib, v)
                    for component in range(3):
                        values[component] += weight*shape_grid[u][v][component]
            shape_diff[ix, ib] = tuple(values)
        jets = tuple(sum((-1)**(j-u)*comb(j, u)*_h(g, rk+60*u-1)
                         for u in range(j+1)) for j in range(4))
        scalar_diff = {}
        for j, ell in SCALAR_ORDERS:
            h0 = _scalar_difference(g, 2*rk+rt, j, ell)
            h1 = _scalar_difference(g, 2*rk+rt-1, j, ell)
            h2 = _scalar_difference(g, 2*rk+rt-2, j, ell)
            scalar_diff[j, ell] = (
                h0-(FIXED_LETTERS[g]*jets[j] if ell == 0 else 0),
                h0-h1,
                h0-2*h1+h2,
            )
        class_data.append((shape_diff, scalar_diff))
    weights = tuple(size*ch for size, ch in
                    zip(CLASS_SIZES, CHARACTERS[effective]))
    result = []
    for ix, ib, jk, jt in ACTIVE_ORDERS:
        numerator = 0
        for weight, (shape_diff, scalar_diff) in zip(weights, class_data):
            rr, tt, zz = shape_diff[ix, ib]
            cc, dc, ddc = scalar_diff[jk, jt]
            numerator += weight*(rr*cc+tt*dc+zz*ddc)
        value, remainder = divmod(numerator, 120)
        if remainder or value < 0:
            raise ArithmeticError("a fixed Newton constant failed integrality or positivity")
        if (ix, ib, jk, jt) != (0, 0, 0, 0) and value == 0:
            raise ArithmeticError("a positive-order Newton constant unexpectedly vanished")
        result.append(value)
    return tuple(result)


def newton_constants(effective, rx: int, rb: int, rk: int, rt: int):
    """The 122 constants at one fixed effective label and residue."""
    effective = _label(effective)
    if any(type(r) is not int or not 0 <= r < PERIOD for r in (rx, rb, rk, rt)):
        raise ValueError("residues must be integers from zero through 59")
    return dict(zip(ACTIVE_ORDERS, _constants(effective, rx, rb, rk, rt)))


def _terms(x: int, b: int, k: int, t: int, effective: tuple[int, ...]):
    values = (x, b, k, t)
    quotients = tuple(value//PERIOD for value in values)
    residues = tuple(value % PERIOD for value in values)
    constants = _constants(effective, *residues)
    binomials = tuple(tuple(comb(q, order) for order in range(bound+1))
                      for q, bound in zip(quotients, (3, 4, 3, 3)))
    terms = []
    for orders, constant in zip(ACTIVE_ORDERS, constants):
        value = constant
        for axis, order in enumerate(orders):
            value *= binomials[axis][order]
        terms.append((orders, constant, value))
    return quotients, residues, tuple(terms)


def coefficient(x: int, b: int, k: int, t: int, d: int, outer=(5,)) -> int:
    _, effective, _, _ = parameters(x, b, k, t, d, outer)
    return sum(value for _, _, value in _terms(x, b, k, t, effective)[2])


def polytopes(x: int, b: int, k: int, t: int, d: int, outer=(5,)):
    """TR.16 matrices for the active residue, with zero constants omitted.

    All equalities are [row,rhs]. Every inequality means row.dot(point)<=rhs.
    Chains are zero based: 0 <= z1 < ... < z_order < quotient.
    """
    _, effective, _, _ = parameters(x, b, k, t, d, outer)
    _, residues, terms = _terms(x, b, k, t, effective)
    output = []
    for orders, constant, count in terms:
        if constant == 0:
            continue
        variables = ["qx", "qb", "qk", "qt", "y"]
        variables += [f"z{axis+1}_{j}" for axis, length in enumerate(orders)
                      for j in range(1, length+1)]
        size = len(variables)
        equalities = []
        for axis, (value, residue) in enumerate(zip((x, b, k, t), residues)):
            row = [0]*size
            row[axis] = PERIOD
            equalities.append([row, value-residue])
        inequalities = []
        for axis in range(5):
            row = [0]*size
            row[axis] = -1
            inequalities.append([row, 0])
        row = [0]*size
        row[4] = 1
        inequalities.append([row, constant-1])
        start = 5
        for axis, length in enumerate(orders):
            if length:
                row = [0]*size
                row[start] = -1
                inequalities.append([row, 0])
                for j in range(length-1):
                    row = [0]*size
                    row[start+j] = 1
                    row[start+j+1] = -1
                    inequalities.append([row, -1])
                row = [0]*size
                row[start+length-1] = 1
                row[axis] = -1
                inequalities.append([row, -1])
            start += length
        assert size <= 11
        output.append({
            "residues": list(residues), "orders": list(orders),
            "constant": constant, "variables": variables,
            "equalities": equalities, "inequalities": inequalities,
            "inequality_convention": "row dot point <= rhs",
            "lattice_count": count,
        })
    assert len(output) <= 122
    return output


def _subsets(upper: int, length: int, start: int = 0,
             prefix: tuple[int, ...] = ()) -> Iterator[tuple[int, ...]]:
    """Lazy zero-based subsets, without allocating a pool of size upper."""
    if length == 0:
        yield prefix
        return
    for value in range(start, upper-length+1):
        yield from _subsets(upper, length-1, value+1, prefix+(value,))


def _chain_products(quotients: tuple[int, ...], orders: tuple[int, ...],
                    axis: int = 0, prefix: tuple[int, ...] = ()):
    if axis == 4:
        yield prefix
        return
    for chain in _subsets(quotients[axis], orders[axis]):
        yield from _chain_products(quotients, orders, axis+1, prefix+chain)


def witnesses(x: int, b: int, k: int, t: int, d: int,
              outer=(5,), limit: int | None = None):
    """Yield distinct tagged integer points, optionally bounded by limit."""
    parameters(x, b, k, t, d, outer)
    if limit is not None and (type(limit) is not int or limit < 0):
        raise ValueError("witness limit must be a nonnegative integer")
    if limit == 0:
        return
    quotients = tuple(v//PERIOD for v in (x, b, k, t))
    emitted = 0
    for poly in polytopes(x, b, k, t, d, outer):
        if poly["lattice_count"] == 0:
            continue
        orders = tuple(poly["orders"])
        for chain in _chain_products(quotients, orders):
            for y in range(poly["constant"]):
                yield {
                    "residues": poly["residues"], "orders": poly["orders"],
                    "variables": poly["variables"],
                    "point": [*quotients, y, *chain],
                }
                emitted += 1
                if limit is not None and emitted >= limit:
                    return


def evaluate(x: int, b: int, k: int, t: int, d: int, outer=(5,),
             include_polytopes: bool = False, include_terms: bool = False,
             witness_limit: int | None = None):
    outer, effective, n, lam = parameters(x, b, k, t, d, outer)
    quotients, residues, terms = _terms(x, b, k, t, effective)
    value = sum(term[2] for term in terms)
    result = {
        "statement": "G-021",
        "parameters": {"x": x, "b": b, "k": k, "t": t, "d": d},
        "quotient_shape": [b+x, b],
        "outer": list(outer), "effective_label": list(effective),
        "inner": n, "lambda": list(lam), "coefficient": value,
        "positive": value > 0,
        "residues": list(residues), "quotients": list(quotients),
        "fixed_tag_bound": 122,
        "nonempty_tag_count": sum(count > 0 for _, _, count in terms),
    }
    if include_terms:
        result["newton_terms"] = [
            {"orders": list(order), "constant": constant, "contribution": count}
            for order, constant, count in terms]
    if include_polytopes:
        result["polytopes"] = polytopes(x, b, k, t, d, outer)
    if witness_limit is not None:
        points = list(witnesses(x, b, k, t, d, outer, witness_limit))
        result["witnesses"] = points
        result["witness_count"] = len(points)
        result["witnesses_truncated"] = len(points) < value
    return result


def main(argv=None):
    if hasattr(sys, "set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("x", "b", "k", "t", "d"):
        parser.add_argument("--"+name, required=True, type=int)
    parser.add_argument("--outer", default="5", help="partition of five, e.g. 5 or 3,2")
    parser.add_argument("--terms", action="store_true")
    parser.add_argument("--polytopes", action="store_true")
    parser.add_argument("--witnesses", nargs="?", const=20, type=int, metavar="LIMIT",
                        help="include at most LIMIT points (default 20)")
    args = parser.parse_args(argv)
    try:
        outer = tuple(int(part) for part in args.outer.replace(",", " ").split())
        result = evaluate(args.x, args.b, args.k, args.t, args.d, outer,
                          args.polytopes, args.terms, args.witnesses)
    except (ValueError, TypeError) as exc:
        parser.error(str(exc))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
