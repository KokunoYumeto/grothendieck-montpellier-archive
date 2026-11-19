#!/usr/bin/env python3
"""Exact degree-six tangent derivation in the genus-two free Lie algebra.

Integer associative-word expansions certify the formulas.  Membership in the
universal arithmetic monodromy algebra is not asserted by this calculation.
"""
from time import perf_counter

started = perf_counter()


def add(a, b):
    out = dict(a)
    for word, coefficient in b.items():
        out[word] = out.get(word, 0) + coefficient
        if not out[word]:
            del out[word]
    return out


def scale(a, coefficient):
    return {word: coefficient * value for word, value in a.items()
            if coefficient * value}


def multiply(a, b):
    out = {}
    for first, left in a.items():
        for second, right in b.items():
            word = first + second
            out[word] = out.get(word, 0) + left * right
    return {word: coefficient for word, coefficient in out.items() if coefficient}


def bracket(a, b):
    return add(multiply(a, b), scale(multiply(b, a), -1))


def derivation(poly, images):
    out = {}
    for word, coefficient in poly.items():
        for index, letter in enumerate(word):
            terms = {word[:index] + replacement + word[index + 1:]:
                     coefficient * value
                     for replacement, value in images[letter].items()}
            out = add(out, terms)
    return out


def rename(poly, permutation):
    out = {}
    for word, coefficient in poly.items():
        image = ''.join(permutation[letter] for letter in word)
        out[image] = out.get(image, 0) + coefficient
    return {word: coefficient for word, coefficient in out.items() if coefficient}


generators = {letter: {letter: 1} for letter in 'abcd'}
z1 = bracket(generators['a'], generators['b'])
z2 = bracket(generators['c'], generators['d'])
c = bracket(z1, z2)
a1 = bracket(z2, c)
a2 = scale(bracket(z1, c), -1)
assert a1 and a2 and a1 != a2
assert {tuple(word.count(letter) for letter in 'abcd') for word in a1} == {(1, 1, 2, 2)}
assert {tuple(word.count(letter) for letter in 'abcd') for word in a2} == {(2, 2, 1, 1)}
images = {letter: bracket(a1 if letter in 'ab' else a2, generators[letter])
          for letter in 'abcd'}
assert all(images.values())
assert not derivation(add(z1, z2), images)
assert c == bracket(z1, add(z1, z2))
print('PASS: all four degree-seven images are nonzero and D([a,b]+[c,d])=0 exactly.')
print('PASS: c=[z1,omega]; hence every D(v) lies in the ideal (omega) and induces zero on the closed-surface Lie quotient.')
print('PASS: a1 and a2 are nonzero, with distinct multidegrees (1,1,2,2) and (2,2,1,1).')
for letter in 'abcd':
    word = min(images[letter])
    print('LEADING_WORD:', letter, word, images[letter][word],
          'SUPPORT_SIZE:', len(images[letter]))

# Torus coordinates (alpha1, alpha2, t), with beta_i=t/alpha_i.
weights = {'a': (1, 0, 0), 'b': (-1, 0, 1),
           'c': (0, 1, 0), 'd': (0, -1, 1)}
for letter, poly in images.items():
    for word in poly:
        actual = tuple(sum(weights[ch][index] for ch in word) - weights[letter][index]
                       for index in range(3))
        assert actual == (0, 0, 3)
print('PASS: every derivation coefficient has the exact similitude character t^3.')

order_five = {'a': 1, 'b': -1, 'c': 2, 'd': -2}
assert all((sum(order_five[ch] for ch in word) - order_five[letter]) % 5 == 0
           for letter, poly in images.items() for word in poly)
swap = {'a': 'c', 'b': 'd', 'c': 'a', 'd': 'b'}
assert rename(a1, swap) == a2 and rename(a2, swap) == a1
assert all(rename(images[letter], swap) == images[swap[letter]] for letter in 'abcd')
print('PASS: D commutes with the displayed order-five action and exchange of the two pairs.')
print('PROOF DEPENDENCY: the free-Lie centralizer of a generator proves D is not inner;')
print('the four displayed equations D(v)=[a_i,v] prove tangency to all generator conjugacy classes.')
print('LIMIT: this computation does not place D in gr_6(Gamma_univ) or construct an arithmetic normalizer.')
print('The written forgetful diagram, using Takao Theorem3.5, proves q_6(Q_l[D] intersect gr_6(Gamma_univ))=0.')
print('ACTUAL_WALL_SECONDS:', format(perf_counter() - started, '.9f'))
