#!/usr/bin/env python3
"""Finite certificate for the perfect quotient in the residual-kernel proof.
The procyclic normalizer condition is deliberately not an output.
"""
from time import perf_counter
_started=perf_counter()
from collections import deque

one=tuple(range(5))
def mul(a,b):return tuple(a[b[i]] for i in range(5))
def inverse(a):return tuple(a.index(i) for i in range(5))
def generated(gens):
    gens=tuple(gens)
    gens=gens+tuple(inverse(g) for g in gens)
    ans={one};todo=deque([one])
    while todo:
        a=todo.popleft()
        for g in gens:
            b=mul(a,g)
            if b not in ans:ans.add(b);todo.append(b)
    return ans

a=(1,2,3,4,0) # (1 2 3 4 5)
b=(1,2,0,3,4) # (1 2 3)
G=generated([a,b])
assert len(G)==60
assert all(sum(g[i]>g[j] for i in range(5) for j in range(i+1,5))%2==0 for g in G)
print('PASS: the displayed 5-cycle and3-cycle generate all60 even permutations')
commutators={mul(mul(mul(g,h),inverse(g)),inverse(h)) for g in G for h in G}
derived=generated(commutators)
assert derived==G
print('PASS: the closed-commutator finite certificate has derived subgroup order60')
assert generated(mul(mul(mul(g,h),inverse(g)),inverse(h)) for g in G for h in derived)==G
print('PASS: the lower central series remains of order60, so this perfect quotient is nonnilpotent')
print('PROOF_USE: F -> A5 is surjective; F_prime, R, S=R_nil(F_prime), and S_prime map onto A5 by the written pronilpotent quotient argument.')
print('LIMIT: no arithmetic open-normalizer property is asserted for a lifted nontrivial element of S_prime.')
print('ACTUAL_WALL_SECONDS:',format(perf_counter()-_started,'.9f'))
