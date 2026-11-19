#!/usr/bin/env python3
"""Finite certificate for the nontrivial Mazur boundary group in Rolfsen 11E.3.

Presentation (printed p.356, opened scan):
  <x,y | y^5=x^7, y^4=x^2 y x^2>.
This is an auxiliary check; the geometric counterexample has a separate proof.
"""
from itertools import combinations, permutations
from time import perf_counter
from datetime import datetime, timezone

start = perf_counter()
n = 7
identity = tuple(range(n))
x = tuple((i + 1) % n for i in range(n))

def compose(a, b):
    return tuple(a[b[i]] for i in range(n))

def power(a, k):
    result = identity
    for _ in range(k):
        result = compose(result, a)
    return result

checked = 0
solutions = []
for support in combinations(range(n), 5):
    for tail in permutations(support[1:]):
        cycle = (support[0],) + tail
        y = list(identity)
        for i in range(5):
            y[cycle[i]] = cycle[(i + 1) % 5]
        y = tuple(y)
        checked += 1
        if power(y, 4) == compose(compose(power(x, 2), y), power(x, 2)):
            assert power(y, 5) == power(x, 7)
            solutions.append(y)
assert checked == 504
assert len(solutions) == 14

y = solutions[0]
group = {identity}
queue = [identity]
while queue:
    a = queue.pop()
    for generator in (x, y):
        b = compose(generator, a)
        if b not in group:
            group.add(b)
            queue.append(b)
assert len(group) == 2520
assert x != identity
print('UTC:', datetime.now(timezone.utc).isoformat())
print('Presentation: <x,y | y^5=x^7, y^4=x^2*y*x^2>')
print('Permutations use zero-based image tuples; products act right-to-left.')
print('x =', x, '= (0 1 2 3 4 5 6)')
print('y =', y, '= (0 3 1 4 2)')
print('x^7 = y^5 =', power(x, 7))
print('y^4 = x^2*y*x^2 =', power(y, 4))
print('Five-cycles checked for fixed x:', checked)
print('Solutions:', len(solutions))
print('Generated permutation group order:', len(group), '(A7)')
print('Both defining relations hold; the group has a nontrivial finite quotient.')
print('Elapsed seconds:', format(perf_counter() - start, '.9f'))
