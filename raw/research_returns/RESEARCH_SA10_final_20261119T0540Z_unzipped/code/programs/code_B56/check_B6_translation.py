#!/usr/bin/env python3
"""Verify explicit Grandis-to-manuscript generator words at finite bounds.
All maps are image tuples on one-based finite sets; compose acts right-to-left.
The all-arity proof is in B56.tex, B6.2; this is an auxiliary finite certificate.
"""
from datetime import datetime, timezone
from time import perf_counter
start = perf_counter()

def identity(n): return tuple(range(1, n + 1))
def compose(a, b): return tuple(a[x - 1] for x in b)
def cycle(i, n):
    return tuple(k if k < i else k + 1 if k < n else i for k in range(1, n + 1))
def inverse(a): return tuple(a.index(k) + 1 for k in range(1, len(a) + 1))

cofaces = codegeneracies = 0
for n in range(1, 13):
    delta = identity(n)
    kappa = identity(n) + (n,)
    for i in range(1, n + 2):
        word = compose(cycle(i, n + 1), delta)
        desired = tuple(k if k < i else k + 1 for k in range(1, n + 1))
        assert word == desired
        if i == n + 1: assert word == delta
        cofaces += 1
    for i in range(1, n + 1):
        inv = inverse(cycle(i, n + 1))
        beta = compose(inv, inv)
        word = compose(cycle(i, n), compose(kappa, beta))
        desired = tuple(k if k <= i else k - 1 for k in range(1, n + 2))
        assert word == desired
        if i == n: assert word == kappa
        codegeneracies += 1
print('UTC:', datetime.now(timezone.utc).isoformat())
print('Checked all n=1,...,12, every allowed i.')
print('c_i^(m) denotes cycle (i i+1 ... m), including identity for i=m.')
print('d_i^(n) = c_i^(n+1) * delta_n:', cofaces, 'checks passed.')
print('e_i^(n) = c_i^(n) * K_n * (c_i^(n+1))^(-2):', codegeneracies, 'checks passed.')
print('Last coface and last codegeneracy recover delta_n and K_n literally.')
print('Total:', cofaces + codegeneracies, 'generator-word checks; zero failures.')
print('Elapsed seconds:', format(perf_counter() - start, '.9f'))
