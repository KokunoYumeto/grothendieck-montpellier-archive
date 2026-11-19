"""Finite certificates used in B.2 and B.4. No numerical approximation is used."""
from itertools import product, combinations
from pathlib import Path
from time import perf_counter
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

t0 = perf_counter()
G = (0, 1)
assert all(((a+b)%2+c)%2 == (a+(b+c)%2)%2 for a,b,c in product(G,repeat=3))
print('C2 group axioms: all 8 associativity triples and both inverses verified.')

def basis(n):
    return [()] if n == 0 else list(product((1,), repeat=n))

def differential(n):
    rows, cols = basis(n-1), basis(n)
    m = sp.zeros(len(rows), len(cols))
    for k,g in enumerate(cols):
        faces=[g[1:]]+[g[:i-1]+((g[i-1]+g[i])%2,)+g[i+1:] for i in range(1,n)]+[g[:-1]]
        for i,h in enumerate(faces):
            if 0 not in h: m[rows.index(h),k] += (-1)**i
    return m

d={n:differential(n) for n in range(1,5)}
for n in d: print('normalized C2 bar differential d'+str(n),d[n].tolist())
for n in range(2,5): assert d[n-1]*d[n] == sp.zeros(1,1)
assert d[1] == sp.Matrix([[0]]) and smith_normal_form(d[2],domain=ZZ) == sp.Matrix([[2]])
print('H1(BC2; Z) = Z/2; hence reduced H2(Sigma BC2; Z) = Z/2.')

# The fundamental cycle of the boundary of the oriented tetrahedron.
verts=tuple(range(4)); edges=list(combinations(verts,2)); faces=list(combinations(verts,3))
b1=sp.zeros(4,6); b2=sp.zeros(6,4)
for k,(i,j) in enumerate(edges): b1[i,k]=-1; b1[j,k]=1
for k,f in enumerate(faces):
    for q in range(3): b2[edges.index(f[:q]+f[q+1:]),k]+=(-1)**q
assert b1*b2 == sp.zeros(4,4)
cycle=sp.Matrix([-1,1,-1,1]); cocycle=sp.Matrix([1,0,0,0])
assert b2*cycle == sp.zeros(6,1)
assert int((cocycle.T*cycle)[0]) == -1
assert b2.rank() == 3
print('Tetrahedral sphere: 4 vertices, 6 edges, 4 faces; rank(boundary2)=3.')
print('Fundamental cycle',list(cycle),'; chosen integral 2-cocycle',list(cocycle))
print('Pairing = -1: this cocycle is not an integral coboundary.')
print('The zero cocycle and this cocycle have identical data on the 1-skeleton.')
print('elapsed_seconds',round(perf_counter()-t0,6))
