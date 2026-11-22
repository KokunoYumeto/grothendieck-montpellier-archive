"""Exact symmetric-group characters using beta-set Murnaghan--Nakayama.

No external algebra system. The tuple of cycle lengths is decreasing.
"""
from functools import lru_cache
from collections import Counter
from math import factorial

def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    if largest is None or largest > n:
        largest = n
    for k in range(largest, 0, -1):
        for tail in partitions(n-k, k):
            yield (k,) + tail

def centralizer_size(cycles):
    z = 1
    for k, m in Counter(cycles).items():
        z *= k**m * factorial(m)
    return z

@lru_cache(maxsize=None)
def _beta_character(beta, cycles):
    if not cycles:
        return int(beta == tuple(range(len(beta)-1, -1, -1)))
    k, rest = cycles[0], cycles[1:]
    answer = 0
    occupied = set(beta)
    for i, b in enumerate(beta):
        target = b-k
        if target < 0 or target in occupied:
            continue
        height = sum(target < c < b for c in beta)
        reduced = tuple(sorted(beta[:i] + beta[i+1:] + (target,), reverse=True))
        answer += (-1)**height * _beta_character(reduced, rest)
    return answer

def character(shape, cycles):
    shape = tuple(a for a in shape if a)
    cycles = tuple(sorted(cycles, reverse=True))
    assert sum(shape) == sum(cycles)
    rank = len(shape)
    beta = tuple(a+rank-1-i for i, a in enumerate(shape))
    return _beta_character(beta, cycles)

def clear_cache():
    _beta_character.cache_clear()

def rectangular_triple(n, s):
    degree = n*s
    fact = factorial(degree)
    value = 0
    for cycles in partitions(degree):
        chi = character((s,)*n, cycles)
        if chi:
            value += fact // centralizer_size(cycles) * chi**3
    assert value % fact == 0
    return value // fact
