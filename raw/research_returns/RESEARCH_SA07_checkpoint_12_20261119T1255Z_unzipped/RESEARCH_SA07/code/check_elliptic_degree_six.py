#!/usr/bin/env python3
"""Exact middle-degree-six free-Lie certificate for all elliptic normalizers.
This script constructs all words independently; source arithmetic is not a computation.
"""
from time import perf_counter
started=perf_counter()
from itertools import product
from functools import lru_cache
import sympy as s
def add(a,b):
    c=dict(a)
    for w,k in b.items():
        c[w]=c.get(w,0)+k
        if not c[w]:del c[w]
    return c
def scale(a,k):return {w:k*c for w,c in a.items() if k*c}
def mul(a,b):
    c={}
    for u,j in a.items():
        for v,k in b.items():c[u+v]=c.get(u+v,0)+j*k
    return {w:k for w,k in c.items() if k}
def bracket(a,b):return add(mul(a,b),scale(mul(b,a),-1))
def derive(a,dx,dy):
    c={}
    for w,k in a.items():
        for i,ch in enumerate(w):
            c=add(c,{w[:i]+v+w[i+1:]:k*j for v,j in (dx if ch=='x' else dy).items()})
    return c
def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
@lru_cache(None)
def standard(w):
    if len(w)==1:return {w:1}
    i=next(i for i in range(1,len(w)) if lyndon(w[i:]))
    return bracket(standard(w[:i]),standard(w[i:]))
def words(n):return [''.join(w) for w in product('xy',repeat=n)]
def lb(n,nx):return [w for w in words(n) if w.count('x')==nx and lyndon(w)]
def col(a,rows):return s.Matrix([a.get(w,0) for w in rows])
def lin(v,L):
    a={}
    for c,z in zip(v,L):a=add(a,scale(z,c))
    return a
x={'x':1};y={'y':1};omega=bracket(x,y)
wx=lb(7,4);wy=lb(7,3);w6=lb(6,3);w8=lb(8,4)
assert (len(wx),len(wy),len(w6),len(w8))==(5,5,3,8)
Lx=[standard(w) for w in wx];Ly=[standard(w) for w in wy]
coefx=[[1,-5,-6,1,-2],[-3,-9,-6,-3,-2]]
coefy=[[-1,4,6,8,0],[3,12,6,0,8]]
Ds=[(lin(a,Lx),lin(b,Ly)) for a,b in zip(coefx,coefy)]
assert all(not derive(omega,*D) for D in Ds)
print('PASS: both displayed degree6 derivations preserve [x,y] exactly')
r8=[w for w in words(8) if w.count('x')==4]
M=s.Matrix.hstack(*[col(bracket(a,y),r8) for a in Lx],*[col(bracket(x,a),r8) for a in Ly])
assert M.rank()==8 and len(M.nullspace())==2
print('PASS: full middle special-derivation space has dimension2 (10 columns, rank8)')
pair=s.Matrix.hstack(*[col(D[0],words(7)).col_join(col(D[1],words(7))) for D in Ds])
assert pair.rank()==2
print('PASS: displayed special derivations form a basis')
expected={
 'x':s.Matrix([[1,-3,1,0,0],[-5,-9,0,1,0],[-6,-6,0,0,1],[1,-3,0,0,0],[-2,-2,0,0,0]]),
 'y':s.Matrix([[-1,3,-1,0,0],[4,12,-1,-1,0],[6,6,0,0,-1],[8,0,1,0,-1],[0,8,0,-1,1]])
}
for ch,W,L in [('x',wx,Lx),('y',wy,Ly)]:
    rows=[w for w in words(7) if w.count('x')==W[0].count('x')]
    basis=s.Matrix.hstack(*[col(a,rows) for a in L]);columns=[]
    for D in Ds:columns.append(basis.gauss_jordan_solve(col(D[0 if ch=='x' else 1],rows))[0])
    for w in w6:columns.append(basis.gauss_jordan_solve(col(bracket({ch:1},standard(w)),rows))[0])
    C=s.Matrix.hstack(*columns)
    assert C==expected[ch] and C.det()==-8
    print('PASS:',ch,'obstruction matrix exactly matches manuscript and has determinant -8')
    print('MATRIX_'+ch+':',C.tolist())
print('LIMIT: Nakamura1996 supplies the nonzero arithmetic quotient; compact closed image and denominator clearing are the written actual-element proof.')
print('LIMIT: no integral inversion of8 is used, and no arbitrary higher-genus or full profinite A22 conclusion is asserted.')
print('ACTUAL_WALL_SECONDS:',format(perf_counter()-started,'.9f'))
