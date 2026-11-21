#!/usr/bin/env python3
"""Exact integer Jacobians for permanent binary-prefix/suffix-order-two jets."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import random
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import sympy as sp


def multiply_linear(poly, coefficients):
    """A homogeneous monomial key is (x_1 exponent, sorted suffix indices)."""
    out = {}
    for (a, suffix), value in poly.items():
        if coefficients[0]:
            key = (a + 1, suffix)
            out[key] = out.get(key, 0) + value * coefficients[0]
        if coefficients[1]:
            key = (a, suffix)
            out[key] = out.get(key, 0) + value * coefficients[1]
        if len(suffix) < 2:
            for k in range(2, len(coefficients)):
                if coefficients[k]:
                    key = (a, tuple(sorted(suffix + (k,))))
                    out[key] = out.get(key, 0) + value * coefficients[k]
    return {key: value for key, value in out.items() if value}


def cofactor_by_subset_dp(pencil, deleted_row, deleted_column):
    m = len(pencil)
    rows = [i for i in range(m) if i != deleted_row]
    cols = [j for j in range(m) if j != deleted_column]
    dp = {0: {(0, ()): 1}}
    for row in rows:
        following = {}
        for mask, poly in dp.items():
            for bit, col in enumerate(cols):
                if mask & (1 << bit):
                    continue
                newmask = mask | (1 << bit)
                product = multiply_linear(poly, pencil[row][col])
                target = following.setdefault(newmask, {})
                for key, value in product.items():
                    target[key] = target.get(key, 0) + value
        dp = following
    return dp[(1 << (m - 1)) - 1]


def monomial_list(m, r):
    targets = []
    for suffix_degree in range(3):
        for suffix in itertools.combinations_with_replacement(range(2, r), suffix_degree):
            for a in range(m - suffix_degree + 1):
                exponent = [a, m - suffix_degree - a] + [0] * (r - 2)
                for j in suffix:
                    exponent[j] += 1
                targets.append((tuple(exponent), (a, suffix)))
    targets.sort()
    return targets


def jacobian(pencil):
    m = len(pencil)
    r = len(pencil[0][0])
    targets = monomial_list(m, r)
    position = {key: j for j, (_, key) in enumerate(targets)}
    matrix = [[0] * (m * m * r) for _ in targets]
    for i in range(m):
        for j in range(m):
            cofactor = cofactor_by_subset_dp(pencil, i, j)
            for (a, suffix), coefficient in cofactor.items():
                for k in range(r):
                    if k == 0:
                        key = (a + 1, suffix)
                    elif k == 1:
                        key = (a, suffix)
                    elif len(suffix) < 2:
                        key = (a, tuple(sorted(suffix + (k,))))
                    else:
                        continue
                    matrix[position[key]][(m * i + j) * r + k] += coefficient
    return [list(exponent) for exponent, _ in targets], matrix


def echelon_mod_prime(matrix, prime):
    # prime^2 < 2^63, so these int64 products are exact before reduction.
    assert prime * prime < 2**63
    work = np.array(matrix, dtype=np.int64) % prime
    rank = 0
    pivots = []
    determinant = 1
    for col in range(work.shape[1]):
        possibilities = np.flatnonzero(work[rank:, col])
        if not len(possibilities):
            continue
        pivotrow = rank + int(possibilities[0])
        if pivotrow != rank:
            work[[rank, pivotrow]] = work[[pivotrow, rank]]
            determinant = -determinant
        pivot = int(work[rank, col])
        determinant = determinant * pivot % prime
        inverse = pow(pivot, -1, prime)
        work[rank, col:] = work[rank, col:] * inverse % prime
        if rank + 1 < work.shape[0]:
            factors = work[rank + 1:, col].copy()
            work[rank + 1:, col:] = (
                work[rank + 1:, col:] - factors[:, None] * work[rank, col:][None, :]
            ) % prime
        pivots.append(col)
        rank += 1
        if rank == work.shape[0]:
            break
    return rank, pivots, int(determinant % prime)


def run(m, r, seed, max_trials):
    rng = random.Random(seed)
    prime = 1000003
    assert sp.isprime(prime)
    trials = []
    best = None
    for trial in range(max_trials):
        pencil = [[[rng.randint(-3, 3) for _ in range(r)] for _ in range(m)] for _ in range(m)]
        target, matrix = jacobian(pencil)
        rank, pivots, residue = echelon_mod_prime(matrix, prime)
        print(json.dumps({"m": m, "r": r, "trial": trial, "rank": rank,
                          "target": len(target), "source": m * m * r}), flush=True)
        trials.append({"trial": trial, "rank": rank})
        if best is None or rank > best["rank"]:
            best = {"trial": trial, "rank": rank, "pencil_coefficients": pencil,
                    "target_monomials": target, "pivot_columns": pivots,
                    "selected_minor_mod_prime": residue, "Jacobian": matrix}
        if rank == len(target):
            break
    path = Path(__file__).with_name(f"per{m}_{r}vars_binary_jets_certificate.json")
    result = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "model": "GPT-6 Astra Pro", "effort": "not exposed",
        "run": "GCT_KRON_20261120", "author": "/root/archive_finish",
        "m": m, "r": r, "seed": seed, "prime": prime,
        "method": "Integer cofactor polynomials by subset dynamic programming, truncated at suffix degree two; source derivative x_k times each permanent cofactor. Exact modular elimination.",
        "monomial_order": "Increasing lexicographic order of all r exponents.",
        "source_order": "Zero-based column ((m*i+j)*r+k), with i,j,k zero-based.",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "trials": trials, "best": best,
        "status": "FULL RANK" if best["rank"] == len(best["target_monomials"]) else "RANK DEFICIENT",
    }
    path.write_text(json.dumps(result, indent=2) + "\n")
    print(path, flush=True)
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=int)
    parser.add_argument("--r", type=int)
    parser.add_argument("--seed", type=int, default=20261121)
    parser.add_argument("--trials", type=int, default=3)
    args = parser.parse_args()
    run(args.m, args.r or (2 * args.m + 1), args.seed, args.trials)
