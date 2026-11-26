#!/usr/bin/env python3
"""Exact symbolic and cycle-index checks for primitive relative monodromy.
CC0 1.0. These finite checks corroborate the mathematical proofs.
No third-party package is required.
"""
from collections import deque, Counter
from itertools import permutations
from math import factorial, comb
from pathlib import Path
import hashlib, json

# Sparse polynomials over F2 in (t,u,x,y); a set contains nonzero monomials.
Z = frozenset()
ONE = frozenset({(0,0,0,0)})
def var(i):
    a=[0]*4; a[i]=1; return frozenset({tuple(a)})
def add(*ps):
    r=set()
    for p in ps: r.symmetric_difference_update(p)
    return frozenset(r)
def mul(a,b):
    r=set()
    for u in a:
        for v in b:
            w=tuple(x+y for x,y in zip(u,v))
            if w in r:r.remove(w)
            else:r.add(w)
    return frozenset(r)
def power(a,n):
    r=ONE
    for _ in range(n):r=mul(r,a)
    return r
def subst(p,values):
    r=Z
    for a in p:
        z=ONE
        for v,e in zip(values,a):z=mul(z,power(v,e))
        r=add(r,z)
    return r
T,U,X,Y=(var(i) for i in range(4))
a=mul(U,power(T,2)); b=add(ONE,power(U,3))
c=add(ONE,power(T,3)); d=mul(T,power(U,2))
checks={}
def check(name,left,right):
    assert left==right,name
    checks[name]=True
check('Euler_determinant',add(mul(a,d),mul(b,c)),add(ONE,power(T,3),power(U,3)))
f1=add(X,mul(a,power(X,2)),mul(b,power(Y,2)))
f2=add(Y,mul(c,power(X,2)),mul(d,power(Y,2)))
g1=subst(f1,[T,Z,X,Y]);g2=subst(f2,[T,Z,X,Y])
check('slice_u_zero_first_equation',g1,add(X,power(Y,2)))
check('slice_u_zero_eliminant',add(g2,mul(c,power(g1,2))),add(Y,mul(c,power(Y,4))))
h1=subst(f1,[T,T,X,Y]);h2=subst(f2,[T,T,X,Y])
check('diagonal_sum',add(h1,h2),add(X,Y,power(X,2),power(Y,2)))
check('diagonal_fixed_vector_first',subst(h1,[T,U,ONE,ONE]),Z)
check('diagonal_fixed_vector_second',subst(h2,[T,U,ONE,ONE]),Z)
check('diagonal_Artin_Schreier_equation',subst(h1,[T,U,X,add(X,ONE)]),add(power(X,2),X,ONE,power(T,3)))

# Cycle-index computation, not enumeration of every quotient vector.
def partitions(n,lo=1):
    if n==0:yield ()
    for j in range(lo,n+1):
        for q in partitions(n-j,j):yield (j,)+q
cycle_rows=[]
for n in (3,5,7,11,13,17):
    classes=list(partitions(n)); total=0; fixed_sum=0
    for part in classes:
        den=1
        for length,count in Counter(part).items():den*=length**count*factorial(count)
        size=factorial(n)//den
        total+=size
        # Odd n excludes a permutation exchanging every subset with its complement.
        fixed_sum+=size*2**(len(part)-1)
    assert total==factorial(n)
    assert fixed_sum%factorial(n)==0
    nonzero_orbits=fixed_sum//factorial(n)-1
    degrees=[comb(n,j) for j in range(1,(n-1)//2+1)]
    assert nonzero_orbits==(n-1)//2
    assert sum(degrees)==2**(n-1)-1
    gl=1
    for j in range(n-1):gl*=2**(n-1)-2**j
    assert (factorial(n)==gl) if n==3 else (factorial(n)<gl)
    cycle_rows.append(dict(n=n,conjugacy_classes=len(classes),nonzero_orbits=nonzero_orbits,invariant_degrees=degrees,S_n_order=factorial(n),GL_order=gl))

# Faithful S5 matrices in the even-weight model: basis e_i+e_5.
def matrix_of(p):
    n=len(p)
    return tuple(((1<<p[i])^(1<<p[-1]))&((1<<(n-1))-1) for i in range(n-1))
def apply(M,x):
    r=0
    for i,col in enumerate(M):
        if (x>>i)&1:r^=col
    return r
def compose(A,B):return tuple(apply(A,col) for col in B)
identity=(1,2,4,8)
generators=[matrix_of((1,2,3,4,0)),matrix_of((1,0,2,3,4))]
seen={identity};queue=deque([identity])
while queue:
    M=queue.popleft()
    for G in generators:
        P=compose(G,M)
        if P not in seen:seen.add(P);queue.append(P)
assert len(seen)==120
assert seen=={matrix_of(p) for p in permutations(range(5))}
remaining=set(range(1,16));orbits=[]
while remaining:
    x=min(remaining);orb={apply(M,x) for M in seen}
    remaining-=orb;orbits.append(sorted(orb))
assert sorted(map(len,orbits))==[5,10]
report={'passed':True,'symbolic_identities':checks,'cycle_index':cycle_rows,'S5_generated_matrix_count':len(seen),'S5_nonzero_orbits':orbits,'program_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'passed':True,'symbolic_identities':len(checks),'cycle_index_cases':len(cycle_rows),'S5_generated_matrix_count':len(seen),'S5_orbit_sizes':sorted(map(len,orbits))}))
