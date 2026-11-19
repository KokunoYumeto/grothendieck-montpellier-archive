#!/usr/bin/env python3
"""Exact PD-indecomposable differential of the signed bar closure.

The integral signed-Lyndon basis of C24 gives a unitriangular change of
basis.  Reducing a bar differential in this basis and discarding every
PD monomial with more than one generator factor computes the intrinsic
quotient by lower-arity PD decomposables, without rational saturation.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial, gcd
from pathlib import Path
import argparse
import json
import time
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def clean(a):
    return {x: c for x, c in a.items() if c}


@lru_cache(None)
def lyndon_factors(word):
    result = []
    i = 0
    while i < len(word):
        j, k = i + 1, i
        while j < len(word) and word[k] <= word[j]:
            k = i if word[k] < word[j] else k + 1
            j += 1
        size = j - k
        while i <= k:
            result.append(word[i:i + size])
            i += size
    return tuple(result)


def is_generator(word):
    f = lyndon_factors(word)
    return len(f) == 1 or (len(f) == 2 and f[0] == f[1]
                          and len(f[0]) % 2 == 1)


@lru_cache(None)
def shuffle(a, b):
    if not a:
        return ((b, 1),)
    if not b:
        return ((a, 1),)
    out = defaultdict(int)
    for w, c in shuffle(a[1:], b):
        out[(a[0],) + w] += c
    sign = (-1) ** len(a)
    for w, c in shuffle(a, b[1:]):
        out[(b[0],) + w] += sign * c
    return tuple(clean(out).items())


def multiply(a, b):
    out = defaultdict(int)
    for x, cx in a.items():
        for y, cy in b.items():
            for z, c in shuffle(x, y):
                out[z] += cx * cy * c
    return clean(out)


@lru_cache(None)
def gamma(word, n):
    assert len(word) % 2 == 0
    out = {(): 1}
    for _ in range(n):
        out = multiply(out, {word: 1})
    div = factorial(n)
    assert all(c % div == 0 for c in out.values())
    return tuple((w, c // div) for w, c in out.items())


@lru_cache(None)
def expansion(word):
    out = {(): 1}
    for f, n in Counter(lyndon_factors(word)).items():
        if len(f) % 2 == 0:
            part = dict(gamma(f, n))
        else:
            q, r = divmod(n, 2)
            part = dict(gamma(f + f, q))
            if r:
                part = multiply(part, {f: 1})
        out = multiply(out, part)
    assert out.get(word) == 1
    assert all(w <= word for w in out)
    return tuple(out.items())


def primitive_projection(vector):
    vector = dict(vector)
    out = {}
    while vector:
        word = max(vector)
        coefficient = vector[word]
        if is_generator(word):
            out[word] = coefficient
        for w, c in expansion(word):
            vector[w] = vector.get(w, 0) - coefficient * c
            if not vector[w]:
                del vector[w]
    return out


@lru_cache(None)
def words(alpha, length):
    if length == 0:
        return ((),) if not any(alpha) else ()
    if sum(alpha) < length:
        return ()
    out = []
    for a in product(*(range(x + 1) for x in alpha)):
        if not any(a):
            continue
        residual = tuple(x - y for x, y in zip(alpha, a))
        for rest in words(residual, length - 1):
            out.append((a,) + rest)
    return tuple(out)


def bar_differential(word):
    out = defaultdict(int)
    for i in range(len(word) - 1):
        a, b = word[i:i + 2]
        c = (-1) ** (i + 1)
        for x, y in zip(a, b):
            c *= comb(x + y, x)
        merged = tuple(x + y for x, y in zip(a, b))
        out[word[:i] + (merged,) + word[i + 2:]] += c
    return clean(out)


def serialize_matrix(matrix):
    return [[int(c) for c in row] for row in matrix.tolist()]


def analyze(alpha, save_full=True):
    arity = sum(alpha)
    bases = {n: tuple(w for w in words(alpha, n) if is_generator(w))
             for n in range(1, arity + 1)}
    matrices = {}
    details = {}
    for n in range(2, arity + 1):
        src, dst = bases[n], bases[n - 1]
        columns = [primitive_projection(bar_differential(w)) for w in src]
        matrix = sp.Matrix(len(dst), len(src),
                           lambda i, j: columns[j].get(dst[i], 0))
        matrices[n] = matrix
        smith = smith_normal_form(matrix, domain=sp.ZZ)
        invariant = [abs(int(smith[i, i]))
                     for i in range(min(smith.shape)) if smith[i, i]]
        details[n] = {"source_form_degree": 2 * arity - n,
                      "source_rank": len(src), "target_rank": len(dst),
                      "rank": len(invariant), "smith_nonzero": invariant}
        if save_full:
            details[n].update(source_basis=src, target_basis=dst,
                              matrix=serialize_matrix(matrix))
    for n in range(3, arity + 1):
        assert matrices[n - 1] * matrices[n] == sp.zeros(
            matrices[n - 1].rows, matrices[n].cols)
    homology = {}
    for n in range(1, arity + 1):
        outgoing = details[n]["rank"] if n >= 2 else 0
        incoming = details[n + 1]["rank"] if n < arity else 0
        free_rank = len(bases[n]) - outgoing - incoming
        # For a complex of free Z-modules, torsion of H at this term is
        # torsion of coker(incoming): the outgoing image is free.
        torsion = ([x for x in details[n + 1]["smith_nonzero"] if x > 1]
                   if n < arity else [])
        homology[2 * arity - n] = {"free_rank": free_rank,
                                  "torsion": torsion}
    return {"multidegree": alpha, "arity": arity,
            "ranks_by_bar_length": {n: len(v) for n, v in bases.items()},
            "differentials": details, "homology_by_form_degree": homology}


def partitions(n, upper=None):
    if n == 0:
        yield ()
        return
    for a in range(min(n, upper or n), 0, -1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-arity", type=int, default=4)
    parser.add_argument("--min-arity", type=int, default=4)
    parser.add_argument("--rank-one", action="store_true")
    parser.add_argument("--output", default="D_bar_indecomposables.json")
    args = parser.parse_args()
    started = time.perf_counter()
    cases = []
    for m in range(args.min_arity, args.max_arity + 1):
        parts = [(m,)] if args.rank_one else list(partitions(m))
        for alpha in parts:
            case = analyze(alpha)
            cases.append(case)
            print(json.dumps({"multidegree": alpha,
                  "ranks": case["ranks_by_bar_length"],
                  "nonzero_homology": {q: h for q, h in
                      case["homology_by_form_degree"].items()
                      if h["free_rank"] or h["torsion"]}}), flush=True)
    receipt = {"statement": "PD-indecomposables of the signed bar closure",
               "method": "Integral unitriangular signed-Lyndon basis; exact Smith forms",
               "cases": cases, "case_count": len(cases),
               "runtime_seconds": time.perf_counter() - started}
    output = Path(__file__).resolve().parents[1] / "logs" / args.output
    output.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"output": str(output), "case_count": len(cases),
                      "runtime_seconds": receipt["runtime_seconds"]}))


if __name__ == "__main__":
    main()
