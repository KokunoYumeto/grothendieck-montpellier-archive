#!/usr/bin/env python3
"""Exhaustive check of the strict quadratic-form boundary in characteristic2."""
from itertools import product, combinations
import json

vectors=list(product(range(2),repeat=4))
pairs=list(combinations(range(4),2))
def q(coeff,x):
    return (sum(coeff[i]*x[i] for i in range(4))+
            sum(coeff[4+j]*x[a]*x[b] for j,(a,b) in enumerate(pairs)))%2
def h(x):return x[0]*x[1]%2
def tensor(v,w):return (v[0]*w[0],v[0]*w[1],v[1]*w[0],v[1]*w[1])
pure=[(tensor(v,w),h(v)*h(w)%2) for v,w in product(product(range(2),repeat=2),repeat=2)]
compatible=[]; natural=[]
for coeff in product(range(2),repeat=10):
    if all(q(coeff,x)==value for x,value in pure):
        compatible.append(coeff)
        row=lambda x:(x[2],x[3],x[0],x[1])
        col=lambda x:(x[1],x[0],x[3],x[2])
        if all(q(coeff,x)==q(coeff,row(x))==q(coeff,col(x)) for x in vectors):
            natural.append(coeff)
assert len(compatible)==2 and not natural
# The polar form of every one-dimensional quadratic form over F2 is zero.
for coeff in range(2):
    assert all((coeff*((x+y)%2)**2-coeff*x*x-coeff*y*y)%2==0
               for x,y in product(range(2),repeat=2))
print(json.dumps(dict(field=2,quadratic_forms_on_tensor_square=1024,
    pure_tensor_product_compatible_forms=len(compatible),
    row_and_column_swap_invariant_compatible_forms=len(natural),
    compatible_coefficient_vectors=compatible,
    coefficient_order=['x0^2','x1^2','x2^2','x3^2']+[f'x{a}x{b}' for a,b in pairs],
    nonsingular_one_dimensional_quadratic_forms=0,
    hyperbolic_plane_polar_matrix=[[0,1],[1,0]]),indent=2))
