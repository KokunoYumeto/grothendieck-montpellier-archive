"""Integral three-multidegree certificate for C25 bar indecomposables."""
from pathlib import Path
from itertools import permutations, combinations
from collections import Counter
from functools import reduce
from math import gcd
import json
import time
import sympy as sp

started = time.perf_counter()
root = Path(__file__).resolve().parents[1]


def as_lists(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.cols)]
            for i in range(matrix.rows)]


checks = []
for pattern in ("aaa", "aab", "abc"):
    words = sorted(set(permutations(pattern)))
    index = {word: i for i, word in enumerate(words)}
    # Every signed (1,2)-shuffle relation is a*(b|c)=abc-bac+bca.
    split_words = []
    relation_columns = []
    for a in sorted(set(pattern)):
        remaining = list(pattern)
        remaining.remove(a)
        for b, c in sorted(set(permutations(remaining))):
            relation = [0] * len(words)
            for word, sign in (((a, b, c), 1), ((b, a, c), -1), ((b, c, a), 1)):
                relation[index[word]] += sign
            split_words.append([a, b, c])
            relation_columns.append(relation)
    relations = sp.Matrix.hstack(*(sp.Matrix(v) for v in relation_columns))
    if pattern == "aaa":
        projection = sp.zeros(0, 1)
        section = sp.zeros(1, 0)
    elif pattern == "aab":
        projection = sp.Matrix([[1, 0, -1]])
        section = sp.Matrix([[1], [0], [0]])
    else:
        projection = sp.Matrix([[1, 0, 1, 0, -1, -1],
                                [0, 1, -1, -1, 1, 0]])
        section = sp.Matrix([[1, 0], [0, 1], [0, 0],
                             [0, 0], [0, 0], [0, 0]])
    assert projection * relations == sp.zeros(projection.rows, relations.cols)
    assert projection * section == sp.eye(projection.rows)
    relation_rank = len(words) - projection.rows
    unimodular_columns = None
    for chosen in combinations(range(relations.cols), relation_rank):
        basis = sp.Matrix.hstack(relations[:, list(chosen)], section)
        determinant = int(basis.det())
        if abs(determinant) == 1:
            unimodular_columns = chosen
            break
    assert unimodular_columns is not None

    # In form4 use a tensor the divided monomial on the remaining pair.
    singles = sorted(set(pattern))
    row_index = {a: i for i, a in enumerate(singles)}
    raw_differential = sp.zeros(len(singles), len(words))
    for column, (a, b, c) in enumerate(words):
        raw_differential[row_index[a], column] += 2 if b == c else 1
        raw_differential[row_index[c], column] -= 2 if a == b else 1
    differential = raw_differential * section
    assert raw_differential == differential * projection
    counts = Counter(pattern)
    multiplication = sp.Matrix([[counts[a] for a in singles]])
    assert multiplication * differential == sp.zeros(1, differential.cols)
    assert differential.rank() == differential.cols
    assert differential.cols == len(singles) - 1
    if differential.cols:
        maximal_minors = [
            abs(int(differential[list(rows), :].det()))
            for rows in combinations(range(differential.rows), differential.cols)
        ]
        primitive_gcd = reduce(gcd, maximal_minors, 0)
    else:
        maximal_minors = [1]
        primitive_gcd = 1
    assert primitive_gcd == 1
    cokernel_order = reduce(gcd, [int(v) for v in multiplication], 0)
    assert cokernel_order == (3 if pattern == "aaa" else 1)
    checks.append({
        "pattern": pattern,
        "word_basis": ["".join(word) for word in words],
        "shuffle_splits": split_words,
        "shuffle_relation_matrix": as_lists(relations),
        "quotient_projection": as_lists(projection),
        "quotient_section": as_lists(section),
        "relation_columns_in_unimodular_basis": list(unimodular_columns),
        "unimodular_basis": as_lists(basis),
        "unimodular_determinant": determinant,
        "form4_single_letter_basis": singles,
        "raw_bar_differential": as_lists(raw_differential),
        "quotient_differential": as_lists(differential),
        "multiplication": as_lists(multiplication),
        "maximal_minors_of_quotient_differential": maximal_minors,
        "primitive_image_gcd": primitive_gcd,
        "only_nonzero_vertical_homology": (
            {"form_degree": 5, "group": "Z/3"} if cokernel_order == 3 else None
        ),
    })

result = {
    "statement": "C25: Q3 of the positive bar closure has sole vertical H5=M/3",
    "arithmetic": "exact integers; all finite-rank free-module patterns exhausted by aaa,aab,abc",
    "checks": checks,
    "runtime_seconds": time.perf_counter() - started,
    "scope": "Basis pattern certificate; the natural simplicial identification and extension argument are proved in the accompanying text.",
}
path = root / "logs/B_bar_arity3_checks.json"
path.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"path": str(path), "patterns": ["aaa", "aab", "abc"],
                  "all_checks_passed": True, "runtime_seconds": result["runtime_seconds"]}))
