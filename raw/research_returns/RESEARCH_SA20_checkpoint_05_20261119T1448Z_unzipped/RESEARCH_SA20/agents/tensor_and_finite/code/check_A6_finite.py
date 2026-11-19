#!/usr/bin/env python3
"""Exact finite checks for the two polygonal gluings in A6.008.

An oriented edge has a positive and a negative half-edge at the
single vertex of a rose.  A corner after x and before y joins -x to y.
Every polygon side maps once, linearly, to the named rose edge.
No randomized steps or external libraries are used.
"""
from collections import Counter, defaultdict
from itertools import permutations, product


def reduce_word(word):
    reduced = []
    for letter in word:
        if reduced and reduced[-1] == -letter:
            reduced.pop()
        else:
            reduced.append(letter)
    return tuple(reduced)


def link(word):
    vertices = set(word) | {-x for x in word}
    edges = [(-word[i], word[(i + 1) % len(word)])
             for i in range(len(word))]
    adjacency = defaultdict(set)
    degree = Counter()
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
        degree[a] += 1
        degree[b] += 1
    unseen = set(vertices)
    components = []
    while unseen:
        root = min(unseen)
        seen = {root}
        todo = [root]
        while todo:
            for neighbor in adjacency[todo.pop()]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    todo.append(neighbor)
        unseen -= seen
        components.append(tuple(sorted(seen)))
    assert all(degree[x] == 2 for x in vertices)
    return edges, sorted(components, key=lambda c: (len(c), c))


words = ((1, -1, 2, -2, 3, -3), (1, 2, -2, -1, 3, -3))
results = []
for word in words:
    assert reduce_word(word) == ()
    assert Counter(abs(x) for x in word) == {1: 2, 2: 2, 3: 2}
    edges, components = link(word)
    sizes = sorted(map(len, components))
    results.append(sizes)
    print('word:', word)
    print('reduced boundary word:', reduce_word(word))
    print('vertex-link edges:', edges)
    print('marked points per vertex-link component:', sizes)
assert results == [[1, 1, 1, 3], [1, 1, 2, 2]]

# Independently check all graph automorphisms (signed permutations),
# and all rotations and reversals of a polygon boundary.
orbit = set()
for perm in permutations((1, 2, 3)):
    for signs in product((-1, 1), repeat=3):
        image = {i + 1: signs[i] * perm[i] for i in range(3)}
        transformed = tuple((1 if x > 0 else -1) * image[abs(x)]
                            for x in words[0])
        for direction in (transformed, tuple(-x for x in transformed[::-1])):
            for offset in range(6):
                orbit.add(direction[offset:] + direction[:offset])
assert words[1] not in orbit
print('signed edge permutations:', 48)
print('dihedral polygon actions per permutation:', 12)
print('second gluing absent from complete first-word orbit:', True)
print('PASS: identical aggregate fundamental-groupoid diagrams; distinct stratified links.')
