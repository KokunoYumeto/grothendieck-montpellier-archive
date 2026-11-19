#!/usr/bin/env python3
"""Exact four-handle balanced tangent block and permutation-average certificate.

All Lie operations have integer coefficients in associative words.  The only
large operation is exact elimination modulo 101 using NumPy signed integers;
every intermediate product has absolute value at most 10000.  The witness
records an ordered nonzero minor and its pivot-product determinant.
"""
from functools import lru_cache
from itertools import permutations
from fractions import Fraction
from math import gcd, lcm
from hashlib import sha256
from pathlib import Path
from time import perf_counter
import json
import numpy as np

started = perf_counter()

def add(a, b):
    out = dict(a)
    for w, c in b.items():
        out[w] = out.get(w, 0) + c
        if not out[w]:
            del out[w]
    return out

def scale(a, c):
    return {w: c * v for w, v in a.items() if c * v}

def multiply(a, b):
    out = {}
    for x, c in a.items():
        for y, d in b.items():
            out[x + y] = out.get(x + y, 0) + c * d
    return {w: c for w, c in out.items() if c}

def bracket(a, b):
    return add(multiply(a, b), scale(multiply(b, a), -1))

def lyndon(w):
    return all(w < w[i:] for i in range(1, len(w)))

@lru_cache(None)
def standard(w):
    if len(w) == 1:
        return {w: 1}
    split = next(i for i in range(1, len(w)) if lyndon(w[i:]))
    out = bracket(standard(w[:split]), standard(w[split:]))
    assert min(out) == w and out[w] == 1
    return out

def multilinear_basis(letters):
    return [''.join(p) for p in permutations(letters) if lyndon(''.join(p))]

def nullspace_integer(matrix):
    a = [[Fraction(c) for c in row] for row in matrix]
    pivots = []
    r = 0
    for j in range(len(a[0])):
        k = next((k for k in range(r, len(a)) if a[k][j]), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        value = a[r][j]
        a[r] = [c / value for c in a[r]]
        for k in range(len(a)):
            if k != r and a[k][j]:
                value = a[k][j]
                a[k] = [x - value * y for x, y in zip(a[k], a[r])]
        pivots.append(j)
        r += 1
        if r == len(a):
            break
    result = []
    for j in range(len(a[0])):
        if j in pivots:
            continue
        v = [Fraction(0)] * len(a[0]); v[j] = 1
        for k, pivot in enumerate(pivots):
            v[pivot] = -a[k][j]
        denominator = lcm(*(x.denominator for x in v))
        v = [int(x * denominator) for x in v]
        divisor = gcd(*v)
        result.append([x // divisor for x in v])
    return result

def substitute(poly, images):
    out = {}
    for word, c in poly.items():
        value = {'': c}
        for letter in word:
            value = multiply(value, images[letter])
        out = add(out, value)
    return out

# First construct the exact two-dimensional kernel using four formal z_i.
zletters = 'wxyz'
zvars = {x: {x: 1} for x in zletters}
zlabels = [(x, w) for x in zletters
           for w in multilinear_basis(zletters.replace(x, ''))]
zpolys = [bracket(standard(w), zvars[x]) for x, w in zlabels]
zrows = multilinear_basis(zletters)
zmat = [[p.get(w, 0) for p in zpolys] for w in zrows]
zbasis = nullspace_integer(zmat)
assert len(zbasis) == 2
conjugators = []
for coefficients in zbasis:
    aa = {x: {} for x in zletters}
    for coefficient, (x, w) in zip(coefficients, zlabels):
        aa[x] = add(aa[x], scale(standard(w), coefficient))
    special = {}
    for x in zletters:
        special = add(special, bracket(aa[x], zvars[x]))
    assert not special
    conjugators.append(aa)
print('FORMAL_Z_LABELS', zlabels)
print('FORMAL_Z_KERNEL_VECTORS', zbasis)

# An exact S4 orbit sum proves every invariant functional vanishes here.
for aa in conjugators:
    total = {x: {} for x in zletters}
    for perm in permutations(zletters):
        mapping = dict(zip(zletters, perm))
        for x in zletters:
            translated = {''.join(mapping[c] for c in word): value
                          for word, value in aa[x].items()}
            total[mapping[x]] = add(total[mapping[x]], translated)
    assert all(not p for p in total.values())
print('PASS: both formal kernel generators have zero exact S4 orbit sum.')

# Full eight-generator specialness block: n=(1,1,1,1).
letters = 'abcdefgh'
v = {x: {x: 1} for x in letters}
rows = multilinear_basis(letters)
labels, polynomials = [], []
for i, x in enumerate(letters):
    y = letters[i ^ 1]
    remainder = ''.join(c for c in letters if c not in (x, y))
    for word in multilinear_basis(remainder):
        image = bracket(standard(word), v[x])
        poly = bracket(image, v[y]) if i % 2 == 0 else bracket(v[y], image)
        labels.append((x, word)); polynomials.append(poly)
matrix = np.array([[p.get(w, 0) for p in polynomials] for w in rows], dtype=np.int16)
assert matrix.shape == (5040, 960)
print('BLOCK (1,1,1,1) SHAPE', *matrix.shape)
print('INPUT_MATRIX_SHA256', sha256(matrix.tobytes()).hexdigest())

zimages = {zletters[i]: bracket(v[letters[2*i]], v[letters[2*i+1]])
           for i in range(4)}
label_index = {label: i for i, label in enumerate(labels)}
vectors = []
for aa in conjugators:
    vector = [0] * len(labels)
    special = {}
    for i, zletter in enumerate(zletters):
        ai = substitute(aa[zletter], zimages)
        special = add(special, bracket(ai, zimages[zletter]))
        remainder = dict(ai)
        while remainder:
            word = min(remainder)
            assert lyndon(word)
            coefficient = remainder[word]
            for letter in letters[2*i:2*i+2]:
                vector[label_index[(letter, word)]] = coefficient
            remainder = add(remainder, scale(standard(word), -coefficient))
    assert not special
    assert np.all(matrix.astype(np.int64) @ np.array(vector, dtype=np.int64) == 0)
    vectors.append(vector)
independence = next((i, j, vectors[0][i]*vectors[1][j]-vectors[0][j]*vectors[1][i])
                    for i in range(len(labels)) for j in range(i+1, len(labels))
                    if vectors[0][i]*vectors[1][j]-vectors[0][j]*vectors[1][i])
print('EXACT_KERNEL_INDEPENDENCE_MINOR', independence)

# Rectangular exact elimination. The selected original rows are ordered in
# pivot order, so their selected-column minor has this pivot-product determinant.
p = 101
work = matrix % p
origins = np.arange(len(rows))
selected_rows, selected_columns = [], []
rank, determinant = 0, 1
for column in range(work.shape[1]):
    nonzero = np.flatnonzero(work[rank:, column])
    if not len(nonzero):
        continue
    pivot = rank + int(nonzero[0])
    if pivot != rank:
        work[[rank, pivot]] = work[[pivot, rank]]
        origins[[rank, pivot]] = origins[[pivot, rank]]
    entry = int(work[rank, column])
    determinant = determinant * entry % p
    selected_rows.append(int(origins[rank])); selected_columns.append(column)
    work[rank, column:] = work[rank, column:] * pow(entry, -1, p) % p
    targets = np.flatnonzero(work[rank+1:, column]) + rank + 1
    if len(targets):
        coefficients = work[targets, column].copy()
        block = work[targets, column:]
        block -= coefficients[:, None] * work[rank, column:]
        block %= p
        work[targets, column:] = block
    rank += 1
    if rank % 240 == 0:
        print('EXACT_MODULAR_PIVOTS', rank, flush=True)
assert rank == 958 and determinant != 0
print('RANK_MOD101', rank, 'ORDERED_MINOR_DETERMINANT', determinant)
print('PASS: rational nullity exactly2; all balanced degree6 blocks are now certified.')
witness = {'modulus':p, 'shape':list(matrix.shape), 'rank':rank,
           'ordered_original_rows':selected_rows, 'columns':selected_columns,
           'ordered_minor_determinant_mod101':determinant,
           'formal_z_labels':zlabels, 'formal_z_kernel_vectors':zbasis,
           'independence_minor':independence,
           'input_matrix_sha256':sha256(matrix.tobytes()).hexdigest(),
           'numpy_version':np.__version__}
path = Path(__file__).with_suffix('.witness.json')
path.write_text(json.dumps(witness, indent=2)+'\n')
print('WITNESS', path.name, 'SHA256', sha256(path.read_bytes()).hexdigest())
print('SCOPE: finite Lie algebra calculation only; actual arithmetic and geometric maps are proved in the accompanying manuscript.')
print('ACTUAL_WALL_SECONDS', format(perf_counter()-started, '.9f'))
