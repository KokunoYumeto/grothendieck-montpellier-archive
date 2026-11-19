#!/usr/bin/env python3
"""Complete exact rank certificate for the genus-two CM-weight tangent space.

Input: free Lie algebra on ordered a<b<c<d, degree6 conjugators, torus
characters a=alpha1,b=t/alpha1,c=alpha2,d=t/alpha2.  All arithmetic
claims are proved separately; the only finite field used here certifies
nonzero integer minors over Q, not an assertion in characteristic101.
"""
from functools import lru_cache
from itertools import product
from time import perf_counter
import json

started = perf_counter()
prime = 101


def add(a, b):
    out = dict(a)
    for word, value in b.items():
        out[word] = out.get(word, 0) + value
        if not out[word]:
            del out[word]
    return out


def scale(a, value):
    return {word: value * coefficient for word, coefficient in a.items()
            if value * coefficient}


def multiply(a, b):
    out = {}
    for first, left in a.items():
        for second, right in b.items():
            word = first + second
            out[word] = out.get(word, 0) + left * right
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def bracket(a, b):
    return add(multiply(a, b), scale(multiply(b, a), -1))


def lyndon(word):
    return all(word < word[index:] for index in range(1, len(word)))


@lru_cache(None)
def standard(word):
    if len(word) == 1:
        return {word: 1}
    split = next(index for index in range(1, len(word)) if lyndon(word[index:]))
    out = bracket(standard(word[:split]), standard(word[split:]))
    assert min(out) == word and out[word] == 1
    return out


def lyndon_words(length):
    return [word for letters in product('abcd', repeat=length)
            if lyndon(word := ''.join(letters))]


def multidegree(word):
    return tuple(word.count(letter) for letter in 'abcd')


def pivot_minor(matrix, modulus):
    work = [[entry % modulus for entry in row] for row in matrix]
    origins = list(range(len(work)))
    selected_rows, selected_columns = [], []
    rank = 0
    for column in range(len(work[0])):
        pivot = next((index for index in range(rank, len(work)) if work[index][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        origins[rank], origins[pivot] = origins[pivot], origins[rank]
        selected_rows.append(origins[rank])
        selected_columns.append(column)
        inverse = pow(work[rank][column], -1, modulus)
        work[rank] = [entry * inverse % modulus for entry in work[rank]]
        for index in range(rank + 1, len(work)):
            factor = work[index][column]
            if factor:
                work[index] = [(left - factor * right) % modulus
                               for left, right in zip(work[index], work[rank])]
        rank += 1
        if rank == len(work):
            break
    return selected_rows, selected_columns


def determinant_mod(matrix, modulus):
    work = [[entry % modulus for entry in row] for row in matrix]
    determinant = 1
    for column in range(len(work)):
        pivot = next((index for index in range(column, len(work)) if work[index][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant = -determinant
        entry = work[column][column]
        determinant = determinant * entry % modulus
        inverse = pow(entry, -1, modulus)
        for index in range(column + 1, len(work)):
            factor = work[index][column] * inverse % modulus
            for j in range(column + 1, len(work)):
                work[index][j] = (work[index][j] - factor * work[column][j]) % modulus
    return determinant % modulus


six, eight = lyndon_words(6), lyndon_words(8)
balanced = {i: [word for word in six if multidegree(word) == (i, i, 3-i, 3-i)]
            for i in range(4)}
assert [len(balanced[i]) for i in range(4)] == [3, 30, 30, 3]
letters = {letter: {letter: 1} for letter in 'abcd'}
z1 = bracket(letters['a'], letters['b'])
z2 = bracket(letters['c'], letters['d'])
c = bracket(z1, z2)
a1 = bracket(z2, c)
a2 = scale(bracket(z1, c), -1)
k1 = add(add(standard('abcdcd'), scale(standard('acdbcd'), 2)), standard('acdcdb'))
k2 = add(standard('ababcd'), standard('abacdb'))
assert a1 == scale(k1, -1) and a2 == scale(k2, -1)
kernel_coefficients = {
    ('a', 'abcdcd'): 1, ('a', 'acdbcd'): 2, ('a', 'acdcdb'): 1,
    ('b', 'abcdcd'): 1, ('b', 'acdbcd'): 2, ('b', 'acdcdb'): 1,
    ('c', 'ababcd'): 1, ('c', 'abacdb'): 1,
    ('d', 'ababcd'): 1, ('d', 'abacdb'): 1,
}
expected_shapes = [(8, 6), (140, 66), (312, 120), (140, 66), (8, 6)]
expected_ranks = [6, 66, 119, 66, 6]
print('INPUT: degree6; alphabet a<b<c<d; torus balance; minor prime101; exact integer word arithmetic.')
print('PASS: the four balanced degree6 Lyndon dimensions are 3,30,30,3.')
for n in range(5):
    rows = [word for word in eight if multidegree(word) == (n, n, 4-n, 4-n)]
    labels, columns, polynomials = [], [], []
    for letter in 'abcd':
        conjugator_degree = n-1 if letter in 'ab' else n
        for word in balanced.get(conjugator_degree, []):
            image = bracket(standard(word), letters[letter])
            if letter == 'a':
                result = bracket(image, letters['b'])
            elif letter == 'b':
                result = bracket(letters['a'], image)
            elif letter == 'c':
                result = bracket(image, letters['d'])
            else:
                result = bracket(letters['c'], image)
            labels.append((letter, word))
            columns.append([result.get(row, 0) for row in rows])
            polynomials.append(result)
    matrix = [[column[index] for column in columns] for index in range(len(rows))]
    assert (len(rows), len(labels)) == expected_shapes[n]
    pivot_rows, pivot_columns = pivot_minor(matrix, prime)
    assert len(pivot_rows) == expected_ranks[n]
    minor = [[matrix[i][j] for j in pivot_columns] for i in pivot_rows]
    determinant = determinant_mod(minor, prime)
    assert determinant != 0
    if n == 2:
        vector = [kernel_coefficients.get(label, 0) for label in labels]
        assert any(vector)
        assert all(sum(entry * coefficient for entry, coefficient in zip(row, vector)) == 0
                   for row in matrix)
        polynomial = {}
        for coefficient, result in zip(vector, polynomials):
            polynomial = add(polynomial, scale(result, coefficient))
        assert polynomial == {}
    print('BLOCK', n, 'ROWS', len(rows), 'COLUMNS', len(labels),
          'RANK_OVER_Q', len(pivot_rows), 'MINOR_DET_MOD101', determinant,
          'NULLITY', len(labels)-len(pivot_rows))
    print('MINOR_ROW_INDICES_ZERO_BASED:', json.dumps(pivot_rows))
    print('MINOR_COLUMN_INDICES_ZERO_BASED:', json.dumps(pivot_columns))
assert c == bracket(z1, add(z1, z2))
print('PASS: the complete tangent special space has dimension1 and is spanned by the displayed D.')
print('PASS: the unique spanning derivation induces zero on L/(omega), because c=[z1,omega].')
print('PROOF: nonzero minors modulo101 give rational lower ranks; the exact nonzero middle kernel gives its upper rank119.')
print('PROOF: restriction to all Lyndon-word coefficients is injective on each homogeneous free-Lie component.')
print('LIMIT: Galois conjugation, Hodge-Tate character separation, actual image projection and Takao quotient are written arithmetic proofs.')
print('ACTUAL_WALL_SECONDS:', format(perf_counter()-started, '.9f'))
