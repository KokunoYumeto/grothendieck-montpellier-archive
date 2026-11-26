#!/usr/bin/env python3
"""Exact modular certificate for a specified rank-four Hecke word minor.

This program is independent of the attached arithmetic programs.  It constructs
the type-A Hecke tensor action from permutations, chooses words and coordinate
rows by exact finite-field elimination, and evaluates the selected determinant
at all four conjugate parameters.  A nonzero determinant proves generic linear
independence only.  The assertion that these 114 words span generically uses the
published dimension in Blasiak--Mulmuley--Sohoni, arXiv:cs/0703110v4, Section11.8,
pp67--68; this program does not independently certify that upper bound.

The polynomial is specified exactly, without expanding its coefficients:
g(v) is the determinant of the selected standard-basis word-coordinate matrix;
f(D)=g(v)g(-v)g(v^-1)g(-v^-1), D=v²+2+v^-2.
The certificate gives all words and rows needed to reconstruct this expression.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path
from time import perf_counter


def prime_check(n: int) -> bool:
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


PERMS = tuple(itertools.permutations(range(1, 5)))
PINDEX = {w: i for i, w in enumerate(PERMS)}
N = len(PERMS) ** 2


def inversion_count(w):
    return sum(w[i] > w[j] for i in range(4) for j in range(i + 1, 4))


def transitions():
    data = []
    for s in range(3):
        col = []
        for w in PERMS:
            ws = list(w)
            ws[s], ws[s + 1] = ws[s + 1], ws[s]
            col.append((PINDEX[tuple(ws)], int(w[s] > w[s + 1])))
        data.append(col)
    return data


TRANS = transitions()


def apply_p(vec, s, v, prime):
    """Right multiplication by P_(s+1) in the standard tensor basis.

    If delta_i records a right descent of w_i, the four coefficients are
    2, (2 delta_j-1)h, (2 delta_i-1)h, and c or2 according as the
    two descents agree or differ, where h=v-v^-1, c=v²+v^-2.
    This follows by expanding 2(T tensor T)-h(T tensor1+1 tensor T)+c.
    """
    vinv = pow(v, -1, prime)
    h = (v - vinv) % prime
    c = (v * v + vinv * vinv) % prime
    out = [0] * N
    trans = TRANS[s]
    for row, a in enumerate(vec):
        if not a:
            continue
        i, j = divmod(row, 24)
        ip, di = trans[i]
        jp, dj = trans[j]
        out[ip * 24 + jp] += 2 * a
        out[ip * 24 + j] += (2 * dj - 1) * h * a
        out[i * 24 + jp] += (2 * di - 1) * h * a
        out[row] += (c if di == dj else 2) * a
    return [x % prime for x in out]


def apply_t(vec, s, side, v, prime):
    """Separate implementation of ordinary Hecke multiplication."""
    h = (v - pow(v, -1, prime)) % prime
    out = [0] * N
    for row, a in enumerate(vec):
        if not a:
            continue
        i, j = divmod(row, 24)
        k, descent = TRANS[s][i if side == 0 else j]
        target = k * 24 + j if side == 0 else i * 24 + k
        out[target] += a
        if descent:
            out[row] += h * a
    return [x % prime for x in out]


def check_generator_formula(prime, v):
    """Check all columns using the two separately expanded tensor summands."""
    vi = pow(v, -1, prime)
    for s in range(3):
        for row in range(N):
            e = [0] * N
            e[row] = 1
            left = apply_t(e, s, 0, v, prime)
            right = apply_t(e, s, 1, v, prime)
            both = apply_t(left, s, 1, v, prime)
            expanded = [
                (2 * both[k] + (vi - v) * (left[k] + right[k])
                 + (vi * vi + v * v) * e[k]) % prime
                for k in range(N)
            ]
            if expanded != apply_p(e, s, v, prime):
                raise AssertionError(("generator formula", s, row))
    return 3 * N


def echelon_insert(vector, echelon, prime):
    work = vector[:]
    for pivot in sorted(echelon):
        coeff = work[pivot]
        if coeff:
            r = echelon[pivot]
            work = [(x - coeff * y) % prime for x, y in zip(work, r)]
    pivot = next((i for i, a in enumerate(work) if a), None)
    if pivot is None:
        return None
    inv = pow(work[pivot], -1, prime)
    echelon[pivot] = [(a * inv) % prime for a in work]
    return pivot


def select_words(prime, v):
    one = [0] * N
    one[0] = 1
    words = [()]
    vectors = [one]
    echelon = {}
    rows = [echelon_insert(one, echelon, prime)]
    cursor = 0
    candidates = 0
    while cursor < len(words):
        parent_word, parent_vector = words[cursor], vectors[cursor]
        for s in range(3):
            candidates += 1
            vector = apply_p(parent_vector, s, v, prime)
            pivot = echelon_insert(vector, echelon, prime)
            if pivot is not None:
                words.append(parent_word + (s + 1,))
                vectors.append(vector)
                rows.append(pivot)
        cursor += 1
    return words, rows, vectors, candidates


def word_vectors(words, prime, v):
    one = [0] * N
    one[0] = 1
    cache = {(): one}
    for word in words:
        if word not in cache:
            for length in range(1, len(word) + 1):
                prefix = word[:length]
                if prefix not in cache:
                    cache[prefix] = apply_p(cache[prefix[:-1]], prefix[-1] - 1, v, prime)
    return [cache[w] for w in words]


def determinant(matrix, prime):
    a = [r[:] for r in matrix]
    det = 1
    size = len(a)
    for k in range(size):
        pivot = next((i for i in range(k, size) if a[i][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            det = -det
        value = a[k][k]
        det = det * value % prime
        inv = pow(value, -1, prime)
        pivot_tail = a[k][k + 1:]
        for i in range(k + 1, size):
            if a[i][k]:
                factor = a[i][k] * inv % prime
                a[i][k + 1:] = [
                    (x - factor * y) % prime
                    for x, y in zip(a[i][k + 1:], pivot_tail)
                ]
                a[i][k] = 0
    return det % prime


def evaluate_minor(words, rows, prime, v):
    vectors = word_vectors(words, prime, v)
    matrix = [[column[row] for column in vectors] for row in rows]
    return determinant(matrix, prime)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=1000003)
    parser.add_argument("--v", type=int, default=2)
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "checks/paper3_rank4_word_minor.json")
    args = parser.parse_args()
    prime, v = args.prime, args.v % args.prime
    if not prime_check(prime) or not v:
        raise ValueError("The modulus must be prime and the parameter nonzero")
    started = perf_counter()
    checked_columns = check_generator_formula(prime, v)
    words, rows, vectors, candidates = select_words(prime, v)
    vi = pow(v, -1, prime)
    conjugates = [v, (-v) % prime, vi, (-vi) % prime]
    determinants = [evaluate_minor(words, rows, prime, value) for value in conjugates]
    norm = math.prod(determinants) % prime
    Dvalue = (v * v + 2 + vi * vi) % prime
    data = {
        "status": "exact modular nonvanishing certificate; generic upper bound supplied by cited primary source",
        "rank_parameter": 4,
        "prime": prime,
        "prime_verified_by_trial_division": True,
        "parameter_v": v,
        "parameter_D": Dvalue,
        "specialized_word_algebra_dimension": len(words),
        "selected_word_count": len(words),
        "largest_word_length": max(map(len, words)),
        "candidate_right_products_reduced": candidates,
        "generator_columns_checked_against_tensor_expansion": checked_columns,
        "word_order": "breadth first; simple generators1,2,3 in this order; append only independent columns",
        "tensor_coordinate_order": "lexicographic permutations of1,2,3,4; row24*i+j for T_perm_i tensor T_perm_j",
        "words": [list(w) for w in words],
        "selected_rows_zero_based": rows,
        "selected_rows_as_permutations": [[list(PERMS[i // 24]), list(PERMS[i % 24])] for i in rows],
        "minor_definition": "g(v)=det of these ordered rows and word columns in the standard Hecke tensor basis",
        "norm_definition": "f(D)=g(v)g(-v)g(v^-1)g(-v^-1), D=v²+2+v^-2",
        "conjugate_v_values": conjugates,
        "minor_determinants_mod_prime": determinants,
        "norm_determinant_mod_prime": norm,
        "nonvanishing": all(determinants) and bool(norm),
        "generic_dimension_background": {
            "authors": ["Jonah Blasiak", "Ketan D. Mulmuley", "Milind Sohoni"],
            "year": 2013,
            "source": "arXiv:cs/0703110v4",
            "locator": "Section11.8, pp67–68; complete irreducible dimension list and dimension114",
            "dimensions": [1, 2, 3, 6, 5, 5, 2, 3, 1],
            "dimension": 114,
            "verification_scope": "Primary paragraph opened; generic upper bound not independently recomputed here"
        },
        "limitations": [
            "No least localization is asserted",
            "The norm polynomial is defined by a finite determinant expression, not expanded",
            "No global integral freeness or positive distinguished basis is asserted",
            "A modular rank alone proves only a generic lower bound; published dimension114 supplies the upper bound"
        ],
        "program_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": round(perf_counter() - started, 3)
    }
    if len(words) != 114 or not data["nonvanishing"]:
        raise AssertionError({k: data[k] for k in ["selected_word_count", "minor_determinants_mod_prime", "nonvanishing"]})
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2) + "\n")
    print(json.dumps({k: data[k] for k in ["selected_word_count", "largest_word_length", "minor_determinants_mod_prime", "norm_determinant_mod_prime", "nonvanishing", "elapsed_seconds"]}))


if __name__ == "__main__":
    main()
