#!/usr/bin/env python3
"""Independent outer-six character certificate and scalar-polytope replay.

Method A: power-sum plethysm, then beta-set Murnaghan--Nakayama.
Method B: literal monomial characters of Sym^n(Q^6), cycle traces,
          and the 720-term GL6 Weyl alternant.
The positive scalar templates are counted directly from their exported
integer matrix inequalities, independently of their Clebsch--Gordan evaluator.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
import json
from math import comb, factorial, prod
from pathlib import Path

from outer_six_scalar import (fast_value, hooks, partitions, positive_values,
                              templates, write_json)


def z_value(cycle_type):
    return prod(length**count * factorial(count)
                for length, count in Counter(cycle_type).items())


@lru_cache(None)
def symmetric_character(shape, cycle_type):
    if not cycle_type:
        return int(not shape)
    if sum(shape) != sum(cycle_type):
        return 0
    length = len(shape)
    beta = tuple(shape[i]+length-1-i for i in range(length))
    occupied = set(beta)
    k = cycle_type[0]
    answer = 0
    for x in beta:
        if x < k or x-k in occupied:
            continue
        replacement = sorted((occupied-{x}) | {x-k}, reverse=True)
        smaller = tuple(a-length+1+i for i, a in enumerate(replacement)
                        if a-length+1+i > 0)
        height = sum(x-k < y < x for y in occupied)
        answer += (-1)**height*symmetric_character(smaller, cycle_type[1:])
    return answer


def multiply_power_sums(left, right):
    answer = defaultdict(Fraction)
    for a, x in left.items():
        for b, y in right.items():
            answer[tuple(sorted(a+b, reverse=True))] += x*y
    return dict(answer)


@lru_cache(None)
def power_cycle_trace(n, cycle_type):
    answer = {(): Fraction(1)}
    for length in cycle_type:
        factor = {tuple(length*x for x in sigma): Fraction(1, z_value(sigma))
                  for sigma in partitions(n)}
        answer = multiply_power_sums(answer, factor)
    return answer


@lru_cache(None)
def power_plethysm(mu, n):
    answer = defaultdict(Fraction)
    for rho in partitions(6):
        character = symmetric_character(mu, rho)
        if character:
            scalar = Fraction(character, z_value(rho))
            for sigma, coefficient in power_cycle_trace(n, rho).items():
                answer[sigma] += scalar*coefficient
    return {sigma: coefficient for sigma, coefficient in answer.items() if coefficient}


def power_value(mu, n, lam):
    value = sum(coefficient*symmetric_character(lam, rho)
                for rho, coefficient in power_plethysm(mu, n).items())
    assert value.denominator == 1 and value >= 0
    return value.numerator


@lru_cache(None)
def compositions(total, length):
    if length == 1:
        return ((total,),)
    return tuple((first,)+tail for first in range(total+1)
                 for tail in compositions(total-first, length-1))


@lru_cache(None)
def monomial_cycle_trace(n, cycle_type):
    if not cycle_type:
        return {(0,)*6: 1}
    previous = monomial_cycle_trace(n, cycle_type[:-1])
    length = cycle_type[-1]
    factor = tuple(tuple(length*x for x in weight) for weight in compositions(n, 6))
    answer = defaultdict(int)
    for weight, count in previous.items():
        for other in factor:
            answer[tuple(a+b for a, b in zip(weight, other))] += count
    return dict(answer)


def permutation_sign(permutation):
    return (-1)**sum(permutation[i] > permutation[j]
                     for i in range(len(permutation))
                     for j in range(i+1, len(permutation)))


WEYL_SHIFTS = tuple((tuple(i-permutation[i] for i in range(6)), permutation_sign(permutation))
                    for permutation in permutations(range(6)))


def monomial_schur_traces(n, lam):
    lam = lam+(0,)*(6-len(lam))
    result = []
    for rho in partitions(6):
        weights = monomial_cycle_trace(n, rho)
        total = 0
        for shift, sign in WEYL_SHIFTS:
            # delta_i-delta_sigma(i)=sigma(i)-i.
            target = tuple(a-b for a, b in zip(lam, shift))
            if min(target) >= 0:
                total += sign*weights.get(target, 0)
        result.append(total)
    return tuple(result)


def schur_dimension(shape, rank):
    if len(shape) > rank:
        return 0
    numerator = prod(rank+j-i for i, row in enumerate(shape) for j in range(row))
    denominator = prod(hooks(shape))
    assert numerator % denominator == 0
    return numerator//denominator


def rhs_value(row, n, r):
    a, b, c = row["rhs"]
    return a*n+b*r+c


def matrix_polytope_count(template, n, r):
    poly = template["polytope"]
    width = len(poly["variables"])
    run_count = sum(name.startswith("u") for name in poly["variables"])
    leaf_count = width-run_count
    run_rows = poly["inequalities"][:run_count]
    runs = [0]*run_count
    answer = 0

    def recurse(index):
        nonlocal answer
        if index < run_count:
            row = run_rows[index]
            assert row["lhs"][index] > 0
            assert all(x == 0 for x in row["lhs"][index+1:])
            residual = rhs_value(row, n, r)-sum(a*b for a, b in zip(row["lhs"], runs))
            upper = residual//row["lhs"][index]
            for value in range(upper+1):
                runs[index] = value
                recurse(index+1)
            runs[index] = 0
            return
        # The second equality fixes the last mark.  All run variables are known.
        last = poly["equalities"][1]
        residual = rhs_value(last, n, r)-sum(a*b for a, b in zip(last["lhs"], runs))
        if residual < 0 or residual % 2:
            return
        target = residual//2
        candidates = [(0,)] if leaf_count == 1 and target == 0 else []
        if leaf_count >= 2:
            candidates = ((0,)+middle+(target,)
                          for middle in combinations_with_replacement(range(target+1), leaf_count-2))
        for marks in candidates:
            point = tuple(runs)+marks
            if any(sum(a*b for a, b in zip(row["lhs"], point)) != rhs_value(row, n, r)
                   for row in poly["equalities"]):
                continue
            if any(sum(a*b for a, b in zip(row["lhs"], point)) > rhs_value(row, n, r)
                   for row in poly["inequalities"]):
                continue
            answer += 1

    recurse(0)
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-inner", type=int, default=3)
    args = parser.parse_args()
    labels, classes = partitions(6), partitions(6)
    character_rows = {mu: tuple(symmetric_character(mu, rho) for rho in classes) for mu in labels}
    for mu in labels:
        assert character_rows[mu][-1] == factorial(6)//prod(hooks(mu))
        for nu in labels:
            assert sum(Fraction(a*b, z_value(rho))
                       for a, b, rho in zip(character_rows[mu], character_rows[nu], classes)) == int(mu == nu)
    rows, coefficient_checks, scalar_checks, dimension_checks = [], 0, 0, 0
    counts_by_inner = {}
    for n in range(args.max_inner+1):
        shapes = partitions(6*n)
        counts_by_inner[n] = len(shapes)
        dimension_sums = {mu: 0 for mu in labels}
        for lam in shapes:
            traces = monomial_schur_traces(n, lam) if len(lam) <= 6 else None
            for mu in labels:
                value = power_value(mu, n, lam)
                if traces is None:
                    assert value == 0
                    alternate = None
                else:
                    alternate = sum(Fraction(character*trace, z_value(rho))
                                    for character, trace, rho in zip(character_rows[mu], traces, classes))
                    assert alternate.denominator == 1
                    alternate = alternate.numerator
                    assert value == alternate, (mu, n, lam, value, alternate)
                    dimension_sums[mu] += value*schur_dimension(lam, 6)
                rows.append({"mu": mu, "n": n, "lambda": lam,
                             "power_sum_MN": value, "monomial_Weyl": alternate})
                coefficient_checks += 1
        for mu in labels:
            expected_dimension = schur_dimension(mu, comb(n+5, 5))
            assert dimension_sums[mu] == expected_dimension
            dimension_checks += 1
            positive = positive_values(mu, n)
            for r in range(3*n+1):
                lam = tuple(x for x in (6*n-r, r) if x)
                matrix_count = sum(matrix_polytope_count(template, n, r) for template in templates(mu))
                assert matrix_count == positive[r] == fast_value(mu, n, r) == power_value(mu, n, lam), (mu, n, r)
                scalar_checks += 1
    output = {"status": "PASS", "max_inner": args.max_inner,
              "outer_size": 6, "partitions_by_inner": counts_by_inner,
              "full_coefficient_checks": coefficient_checks,
              "scalar_polytope_matrix_checks": scalar_checks,
              "GL6_dimension_checks": dimension_checks,
              "S6_character_table": {",".join(map(str, mu)): row for mu, row in character_rows.items()},
              "cycle_types": classes,
              "scope": "All output partitions, all mu partitions 6, 0<=n<=max_inner; length>6 vanish by MN and the row-Pieri bound. Positive scalar templates cover only outputs of length<=2.",
              "rows": rows}
    write_json(args.output, output)
    print(json.dumps({key: value for key, value in output.items()
                      if key not in ("rows", "S6_character_table", "cycle_types")}, indent=2))


if __name__ == "__main__":
    main()
