#!/usr/bin/env python3
"""Positive compressed GOS/KOH polytopes for outer degree six, two-row output.

The known Pak--Panova--Swanson marked-tree identity is the mathematical input.
This file compresses maximal all-ones KOH chains, exports the resulting fixed
polytope templates, evaluates small cases by positive Clebsch--Gordan paths,
and evaluates arbitrary binary parameters by exact hook-content recurrence.
It does NOT evaluate the full six-point flag-bundle problem by this formula.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
import json
from pathlib import Path


@lru_cache(None)
def partitions(n: int, largest: int | None = None) -> tuple[tuple[int, ...], ...]:
    if n == 0:
        return ((),)
    if largest is None:
        largest = n
    return tuple((a,) + tail for a in range(min(n, largest), 0, -1)
                 for tail in partitions(n-a, a))


def qj(partition: tuple[int, ...], j: int) -> int:
    return sum(min(a, j) for a in partition)


def conjugate(partition: tuple[int, ...], length: int) -> tuple[int, ...]:
    return tuple(sum(a >= j for a in partition) for j in range(1, length+1))


@lru_cache(None)
def gos_configurations(mu: tuple[int, ...]):
    n, ell = sum(mu), len(mu)
    sizes = [sum(mu[i:]) for i in range(1, ell)]
    answer = []
    for middle in product(*(partitions(s) for s in sizes)):
        nu = ((1,) * n,) + middle + ((),)
        vacancy = {}
        for i in range(1, ell):
            for j in range(1, n+1):
                vacancy[i, j] = qj(nu[i+1], j) - 2*qj(nu[i], j) + qj(nu[i-1], j)
        if any(v < 0 for v in vacancy.values()):
            continue
        factors = tuple((vacancy[i, j], count)
                        for i in range(1, ell)
                        for j, count in sorted(Counter(nu[i]).items()))
        alpha = [conjugate(p, n) for p in nu]
        tau = sum(alpha[i][j] * (alpha[i][j] - alpha[i+1][j])
                  for i in range(1, ell) for j in range(n))
        answer.append((nu, len(nu[1]), tau, factors))
    return tuple(answer)


@lru_cache(None)
def constant_koh(a: int, b: int) -> tuple[tuple[int, ...], ...]:
    """All leaf lists, retaining repeated lists from distinct literal trees."""
    if a < 0:
        return ()
    if b == 0:
        return ((),)
    if b == 1:
        return ((a,),)
    result = []
    for rho in partitions(b):
        children = [(j*(a+2)-2*qj(rho, j), count)
                    for j, count in sorted(Counter(rho).items())]
        if any(x < 0 for x, _ in children):
            continue
        assert all(y < b or x < a for x, y in children)
        for leaves in product(*(constant_koh(x, y) for x, y in children)):
            result.append(sum(leaves, ()))
    return tuple(result)


@lru_cache(None)
def skeletons(b: int):
    """A leaf is (); an internal node is (rho, ((edge, child), ...))."""
    if b == 1:
        return ((),)
    result = []
    for rho in partitions(b):
        if rho == (1,) * b:
            continue
        groups = sorted(Counter(rho).items())
        for children in product(*(skeletons(count) for _, count in groups)):
            result.append((rho, tuple((j, child) for (j, _), child in zip(groups, children))))
    return tuple(result)


def internal_count(tree) -> int:
    return 0 if not tree else 1 + sum(internal_count(child) for _, child in tree[1])


def affine_add(left, right):
    return tuple(x+y for x, y in zip(left, right))


def affine_scale(scalar, form):
    return tuple(scalar*x for x in form)


def expand_skeleton(tree, first, run_count):
    """Forms are (coefficient of n, constant, coefficients of run variables)."""
    nodes, leaves = [], []

    def visit(node, a):
        if not node:
            leaves.append(a)
            return
        rho, children = node
        b = sum(rho)
        index = len(nodes)
        nodes.append({"partition": rho, "mass": b, "input": a, "run_index": index})
        reduced = list(a)
        reduced[2+index] -= 2*(b-1)
        for j, child in children:
            child_a = list(affine_scale(j, reduced))
            child_a[1] += 2*j-2*qj(rho, j)
            visit(child, tuple(child_a))

    visit(tree, first)
    assert len(nodes) == run_count
    return nodes, leaves


def polytope_constraints(nodes, leaves):
    """Return rows lhs(x)<=alpha*n+beta*r+gamma; all variables are >=0."""
    run_count, t = len(nodes), len(leaves)
    width = run_count+t
    inequalities, equalities = [], []

    def add_leaf_nonnegative(form):
        row = [-x for x in form[2:]] + [0]*t
        inequalities.append({"lhs": row, "rhs": [form[0], 0, form[1]]})

    for node in nodes:
        a = list(node["input"])
        a[2+node["run_index"]] -= 2*(node["mass"]-1)
        add_leaf_nonnegative(a)
    for a in leaves:
        add_leaf_nonnegative(a)
    first = [0]*width
    first[run_count] = 1
    equalities.append({"lhs": first, "rhs": [0, 0, 0]})
    total = tuple(sum(a[j] for a in leaves) for j in range(run_count+2))
    last = [-x for x in total[2:]] + [0]*t
    last[-1] = 2
    equalities.append({"lhs": last, "rhs": [total[0]-6, 2, total[1]]})
    prefix = (0,)*(run_count+2)
    for i in range(t-1):
        prefix = affine_add(prefix, leaves[i])
        monotone = [0]*width
        monotone[run_count+i] = 1
        monotone[run_count+i+1] = -1
        inequalities.append({"lhs": monotone, "rhs": [0, 0, 0]})
        cap = [-x for x in leaves[i+1][2:]] + [0]*t
        cap[run_count+i] = -1
        cap[run_count+i+1] = 1
        inequalities.append({"lhs": cap, "rhs": [leaves[i+1][0], 0, leaves[i+1][1]]})
        cap = [-x for x in prefix[2:]] + [0]*t
        cap[run_count+i] = 1
        cap[run_count+i+1] = 1
        inequalities.append({"lhs": cap, "rhs": [prefix[0], 0, prefix[1]]})
    return {"variables": [f"u{i}" for i in range(run_count)] + [f"k{i+1}" for i in range(t)],
            "all_variables_nonnegative": True,
            "equalities": equalities, "inequalities": inequalities}


@lru_cache(None)
def templates(mu: tuple[int, ...]):
    assert sum(mu) == 6
    result = []
    for configuration_index, (nu, minimum, tau, factors) in enumerate(gos_configurations(mu)):
        for constant_index, factor_leaves in enumerate(product(*(constant_koh(a, b) for a, b in factors))):
            constants = sum(factor_leaves, ())
            # Center of the constant part and final Gaussian: the GOS identity.
            constant_degree = sum(a*b for a, b in factors)
            assert 2*tau + constant_degree == 6*minimum
            for skeleton_index, tree in enumerate(skeletons(6)):
                count = internal_count(tree)
                nodes, leaves = expand_skeleton(tree, (1, -minimum)+(0,)*count, count)
                leaves = [(0, a)+(0,)*count for a in constants] + leaves
                result.append({"mu": mu, "tag": [configuration_index, constant_index, skeleton_index],
                               "configuration": nu, "minimum_inner": minimum, "tau": tau,
                               "constant_factors": factors, "constant_leaves": constants,
                               "skeleton": tree, "run_nodes": nodes, "leaf_forms": leaves,
                               "polytope": polytope_constraints(nodes, leaves)})
    return tuple(result)


def evaluate_affine(form, n, runs):
    return form[0]*n+form[1]+sum(a*b for a, b in zip(form[2:], runs))


def valid_runs(template, n):
    nodes = template["run_nodes"]
    runs = [0]*len(nodes)

    def visit(index):
        if index == len(nodes):
            leaves = tuple(evaluate_affine(a, n, runs) for a in template["leaf_forms"])
            if min(leaves) >= 0:
                yield tuple(runs), leaves
            return
        node = nodes[index]
        # Input only depends on ancestors, which precede this node.
        assert all(c == 0 for c in node["input"][2+index:])
        a = evaluate_affine(node["input"], n, runs)
        for repetition in range(a//(2*(node["mass"]-1))+1):
            runs[index] = repetition
            yield from visit(index+1)
        runs[index] = 0

    yield from visit(0)


def clebsch_gordan(leaves):
    answer = {leaves[0]: 1}
    for a in leaves[1:]:
        next_answer = defaultdict(int)
        for degree, count in answer.items():
            for j in range(min(a, degree)+1):
                next_answer[degree+a-2*j] += count
        answer = dict(next_answer)
    return answer


def positive_values(mu, n):
    """Positive path enumeration for calibration, not the binary-time evaluator."""
    answer = [0]*(3*n+1)
    for template in templates(mu):
        for runs, leaves in valid_runs(template, n):
            assert sum(leaves) <= 6*n and (6*n-sum(leaves)) % 2 == 0
            for degree, count in clebsch_gordan(leaves).items():
                assert (6*n-degree) % 2 == 0
                answer[(6*n-degree)//2] += count
    return tuple(answer)


def polynomial_multiply(a, b):
    answer = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            answer[i+j] += x*y
    while len(answer) > 1 and answer[-1] == 0:
        answer.pop()
    return answer


@lru_cache(None)
def hooks(mu):
    if not mu:
        return ()
    conjugated = conjugate(mu, max(mu))
    return tuple(mu[i]-j+conjugated[j]-i-1
                 for i in range(len(mu)) for j in range(mu[i]))


@lru_cache(None)
def denominator(mu):
    q = [1]
    for h in hooks(mu):
        factor = [1]+[0]*h
        factor[-1] = -1
        q = polynomial_multiply(q, factor)
    return tuple(q)


@lru_cache(None)
def reciprocal_coefficient(mu, exponent):
    if exponent < 0:
        return 0
    p, q = [1], list(denominator(mu))
    while exponent:
        minus = [x if i % 2 == 0 else -x for i, x in enumerate(q)]
        p = polynomial_multiply(p, minus)[exponent % 2::2]
        q = polynomial_multiply(q, minus)[::2]
        exponent //= 2
    assert q[0] == 1
    return p[0]


def fast_value(mu: tuple[int, ...], n: int, r: int) -> int:
    """Exact polynomial-bit-time evaluation of the positive formula's value."""
    assert sum(mu) == 6 and n >= 0
    if r < 0 or r > 3*n or len(mu) > n+1:
        return 0
    shift = sum(i*a for i, a in enumerate(mu))
    numerator = {0: 1}
    for i, row in enumerate(mu):
        for j in range(row):
            exponent = n+1+j-i
            assert exponent > 0
            next_numerator = defaultdict(int, numerator)
            for degree, count in numerator.items():
                next_numerator[degree+exponent] -= count
            numerator = {degree: count for degree, count in next_numerator.items() if count}
    answer = sum(count*(reciprocal_coefficient(mu, r-shift-degree)
                       -reciprocal_coefficient(mu, r-1-shift-degree))
                 for degree, count in numerator.items())
    assert answer >= 0
    return answer


def scalar_fat_point(mu: tuple[int, ...], c: int, k: int) -> int:
    assert c >= 0 and k >= 0
    if c-k < 0 or 4*c-6*k < 0:
        return 0
    return fast_value(mu, c-k, c)


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2)+"\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--templates", type=Path)
    parser.add_argument("--check", type=Path)
    parser.add_argument("--max-inner", type=int, default=12)
    parser.add_argument("--mu")
    parser.add_argument("--inner", type=int)
    parser.add_argument("--second-row", type=int)
    parser.add_argument("--c", type=int)
    parser.add_argument("--k", type=int)
    args = parser.parse_args()
    if args.templates:
        data = {",".join(map(str, mu)): templates(mu) for mu in partitions(6)}
        write_json(args.templates, {"schema": "positive affine polytope templates; rhs=[n,r,1]",
                                    "valid_inputs": "mu partitions 6; n>=0; 0<=r<=3n",
                                    "templates": data})
        print(json.dumps({"skeleton_counts": {b: len(skeletons(b)) for b in range(1, 7)},
                          "template_counts": {mu: len(ts) for mu, ts in data.items()},
                          "maximum_variables": max(len(t["polytope"]["variables"])
                                                   for ts in data.values() for t in ts)}, indent=2))
    if args.check:
        rows, checked = [], 0
        for mu in partitions(6):
            for n in range(args.max_inner+1):
                positive = positive_values(mu, n)
                fast = tuple(fast_value(mu, n, r) for r in range(3*n+1))
                assert positive == fast, (mu, n, positive, fast)
                rows.append({"mu": mu, "n": n, "values": positive})
                checked += len(positive)
        write_json(args.check, {"status": "PASS", "coefficient_checks": checked,
                                "scope": "compressed positive path counts versus independent hook-content recurrence",
                                "rows": rows})
        print(json.dumps({"status": "PASS", "coefficient_checks": checked}))
    if args.mu:
        mu = tuple(map(int, args.mu.split(",")))
        if args.c is not None:
            print(scalar_fat_point(mu, args.c, args.k))
        else:
            print(fast_value(mu, args.inner, args.second_row))


if __name__ == "__main__":
    main()
