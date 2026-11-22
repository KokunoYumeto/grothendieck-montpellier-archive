"""Independent exact finite check of K-023 and K-024 support conventions.

The symmetric-group side uses Murnaghan--Nakayama.  The auxiliary side
uses integer weight dynamic programming and the Weyl denominator.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial, gcd
from pathlib import Path
import json

root = Path(__file__).resolve().parent

@lru_cache(None)
def partitions(total, maximum=None):
    if maximum is None:
        maximum = total
    if total == 0:
        return ((),)
    result = []
    for first in range(min(total, maximum), 0, -1):
        result.extend((first,) + tail for tail in partitions(total - first, first))
    return tuple(result)

@lru_cache(None)
def character(shape, cycle_type):
    if not cycle_type:
        return int(not shape)
    length = cycle_type[0]
    old = {(i, j) for i, width in enumerate(shape) for j in range(width)}
    result = 0
    for smaller in partitions(sum(shape) - length):
        if len(smaller) > len(shape) or any(width > shape[i] for i, width in enumerate(smaller)):
            continue
        cells = old - {(i, j) for i, width in enumerate(smaller) for j in range(width)}
        if any({(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)} <= cells for i, j in cells):
            continue
        reached = {next(iter(cells))}
        todo = list(reached)
        while todo:
            i, j = todo.pop()
            for neighbor in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if neighbor in cells and neighbor not in reached:
                    reached.add(neighbor)
                    todo.append(neighbor)
        if reached != cells:
            continue
        sign = (-1) ** (len({i for i, j in cells}) - 1)
        result += sign * character(smaller, cycle_type[1:])
    return result


def class_denominator(cycle_type):
    answer = 1
    for length, count in Counter(cycle_type).items():
        answer *= length ** count * factorial(count)
    return answer


def cube_type(cycle_type):
    result = []
    for length in cycle_type:
        count = gcd(length, 3)
        result.extend([length // count] * count)
    return tuple(sorted(result, reverse=True))


def auxiliary_generators(n):
    generators = []
    for i in range(n):
        weight = [0] * n
        weight[i] = 1
        generators.append(tuple(weight))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            weight = [0] * n
            weight[i] = 2
            weight[j] = 1
            generators.append(tuple(weight))
    for triple in combinations(range(n), 3):
        weight = tuple(int(i in triple) for i in range(n))
        generators.extend([weight, weight])
    return generators


def auxiliary_dimension(n, stretch):
    total = n * stretch
    bound = stretch + n - 1
    dp = {(0,) * n: 1}
    for weight in auxiliary_generators(n):
        updated = Counter()
        for current, multiplicity in dp.items():
            max_copies = min((bound - current[i]) // weight[i] for i in range(n) if weight[i])
            max_copies = min(max_copies, (total - sum(current)) // sum(weight))
            for copies in range(max_copies + 1):
                target = tuple(current[i] + copies * weight[i] for i in range(n))
                updated[target] += multiplicity
        dp = updated
    delta = tuple(range(n - 1, -1, -1))
    answer = 0
    for permutation in permutations(range(n)):
        inversions = sum(permutation[i] > permutation[j] for i in range(n) for j in range(i + 1, n))
        target = tuple(stretch + delta[i] - delta[permutation[i]] for i in range(n))
        answer += (-1) ** inversions * dp.get(target, 0)
    return answer


rows = []
for n, largest_stretch in ((2, 6), (3, 4), (4, 3), (5, 2)):
    for stretch in range(largest_stretch + 1):
        total = n * stretch
        shape = (stretch,) * n if stretch else ()
        kronecker = sum((F(character(shape, cycle) ** 3, class_denominator(cycle))
                        for cycle in partitions(total)), F(0))
        trace = sum((F(character(shape, cube_type(cycle)), class_denominator(cycle))
                     for cycle in partitions(total)), F(0))
        auxiliary = auxiliary_dimension(n, stretch)
        assert kronecker.denominator == trace.denominator == 1
        assert trace == auxiliary
        assert kronecker >= trace and (kronecker - trace).numerator % 3 == 0
        rows.append({'n': n, 's': stretch, 'kronecker': int(kronecker),
                     'cyclic_trace': int(trace), 'auxiliary_dimension': auxiliary})

support_receipts = []
for n in range(2, 15):
    M = 2 ** (n - 1)
    weights = [pow(-2, i, M) for i in range(n)]
    q = [(1 - F(-1, 2) ** i) / 3 for i in range(1, n)]
    q.append(1 - q[-1])
    assert all(value > 0 for value in q)
    assert 2 * q[0] == 1
    assert all(q[i - 1] + 2 * q[i] == 1 for i in range(1, n - 1))
    assert q[-2] + q[-1] == 1
    assert len(set(weights)) == n and sum(weights) % 2 == 1
    fixed = [weight for weight in auxiliary_generators(n)
             if sum(x * y for x, y in zip(weight, weights)) % M == 0]
    expected = []
    for i in range(n - 1):
        weight = [0] * n
        weight[i] = 2
        weight[i + 1] = 1
        expected.append(tuple(weight))
    expected.append((0,) * (n - 1) + (1,))
    assert Counter(fixed) == Counter(expected)
    paired = [(i, j) for i in range(n) for j in range(i + 1, n)
              if (weights[i] - weights[j]) % M == M // 2]
    assert paired == [(n - 2, n - 1)]
    support_receipts.append({'n': n, 'period': M, 'fixed_weight_dimension': len(fixed),
                            'antipodal_pair_zero_based': paired[0],
                            'positive_masses': [str(value) for value in q]})

(root / 'cyclic_trace_hook_checks.json').write_text(json.dumps({
    'status': 'PASS', 'independent_finite_character_checks': rows,
    'hook_support_convention_checks': support_receipts}, indent=2))
print('PASS K-023/K-024: 19 exact symmetric-group versus auxiliary-weight counts; n2..14 masses, complete fixed weights and unique antipodal pair.')
