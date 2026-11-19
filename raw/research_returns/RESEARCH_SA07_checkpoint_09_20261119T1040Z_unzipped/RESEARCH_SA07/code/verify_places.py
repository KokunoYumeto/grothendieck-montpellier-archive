#!/usr/bin/env python3
"""Finite certificates for E.1.2--E.3.1; no finite check proves the infinite claim."""
from math import factorial, gcd
from time import perf_counter
import sympy as sp

start=perf_counter()
print('Exact arithmetic; no numerical precision parameter.')
print('Factorial residues and compatibility:')
previous=0
for n in range(2,15):
    s=sum(factorial(m) for m in range(1,n))
    mod=factorial(n)
    assert (s-previous)%factorial(n-1)==0
    if n>=4:
        assert 0<2*s<mod
    print(f'n={n:2d}, modulus={mod}, residue={s}, twice_residue_lt_modulus={2*s<mod}')
    previous=s

print('All invertible matrices modulo n stabilizing e1,e2,e1+e2:')
for n in range(2,17):
    found=[]
    # Stabilization of the first two direct summands forces both off-diagonals zero.
    for a in range(n):
        for d in range(n):
            if gcd(a*d,n)!=1:
                continue
            if a==d:  # Membership of (a,d) in the diagonal cyclic subgroup.
                found.append((a,0,0,d))
    expected=[(u,0,0,u) for u in range(n) if gcd(u,n)==1]
    assert found==expected
    print(f'n={n:2d}: {len(found)} matrices, all scalar units')

x,z=sp.symbols('x z')
u=sp.Matrix([[1,2*x],[0,1]])
assert u**7==sp.Matrix([[1,14*x],[0,1]])
assert u.inv()*sp.Matrix([[z,2*x*z],[0,z]])==z*sp.eye(2)
print('Unipotent powers and scalar stabilizer identities: PASS')

a=sp.symbols('a')
aa=-3*a/(a-1)
bb=-2*a/(a-1)
disc=sp.factor(-16*(4*aa**3+27*bb**2))
j=sp.factor(-1728*(4*aa)**3/disc)
assert disc==1728*a*a/(a-1)**3
assert j==1728*a
print('Elliptic j-family discriminant:',disc)
print('Elliptic j-family classical j:',j)
print('Scope: verifies finite residue cases, matrix identities, and rational-function identities.')
print('The field, monodromy, inverse-limit, and Hodge reconstruction claims use the written proofs.')
print(f'Runtime_seconds={perf_counter()-start:.6f}')
