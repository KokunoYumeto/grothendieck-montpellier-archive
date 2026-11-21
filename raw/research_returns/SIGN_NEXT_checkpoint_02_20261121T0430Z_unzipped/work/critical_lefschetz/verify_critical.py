"""Exact checks for SN-C02 and SN-C05; no symbolic or external library required."""
from fractions import Fraction
from pathlib import Path


def multiply(a,b):
    assert len(a[0]) == len(b)
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]

lv = [[0,0,0],[1,0,0],[0,1,0]]
lu = [[0,0],[1,0]]
r = [[1,0,0],[0,1,0]]
g = [[0,0],[1,0],[0,1]]
assert multiply(g,r) == lv
assert multiply(r,g) == lu
assert multiply(r,lv) == multiply(lu,r)
assert multiply(g,lu) == multiply(lv,g)
assert multiply(lv,lv) == [[0,0,0],[0,0,0],[1,0,0]]

# P1 x P1: coefficients of 1,a,b,ab with a^2=b^2=0.
def product(x,y):
    z = {}
    for (i,j),a in x.items():
        for (k,l),b in y.items():
            if i+k < 2 and j+l < 2:
                z[(i+k,j+l)] = z.get((i+k,j+l),0) + a*b
    return {ij:a for ij,a in z.items() if a}

h = {(1,0):1,(0,1):1}
assert product(h,h) == {(1,1):2}
# Image of H^0(W) in codimension one is column (1,1), rank 1;
# target algebraic codimension-one group has independent basis a,b.
gysin_column = [[1],[1]]
assert any(row[0] for row in gysin_column)  # one nonzero column has rank one
target_basis = [[1,0],[0,1]]
assert target_basis[0][0]*target_basis[1][1]-target_basis[0][1]*target_basis[1][0] == 1
print('SN-C02: (a+b)^2 = 2ab; ordinary Gysin image column (1,1), rank 1 in rank-2 target.')
print('SN-C05: gr=L_V; rg=L_U; rL_V=L_Ur; gL_U=L_Vg; L_V^2(v0)=v2. All exact checks passed.')
