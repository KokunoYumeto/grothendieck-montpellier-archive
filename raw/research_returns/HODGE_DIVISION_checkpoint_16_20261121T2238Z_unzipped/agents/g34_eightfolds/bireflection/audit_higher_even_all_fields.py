#!/usr/bin/env python3
"""Independent finite-field and exact-constant checks for D-HES04--06.

The universal proof is checked separately. A small complete descent model
and complete rank-three dual weights are arithmetic witnesses only.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time

B=Path(__file__).resolve().parent

def mul(x,y):
    a=(x&1)*(y&1);b=(x>>1)*(y&1)+(x&1)*(y>>1);c=(x>>1)*(y>>1)
    return ((a+c)&1)|(((b+c)&1)<<1)
def sq(x):return mul(x,x)
def tr(x):return x^sq(x)
def dot(x,y):
    s=0
    for a,b in zip(x,y):s^=mul(a,b)
    return s
def mv(A,x):return tuple(dot(r,x) for r in A)
def mm(A,C):return tuple(tuple(dot(r,c) for c in zip(*C)) for r in A)
def det(A):return mul(A[0][0],A[1][1])^mul(A[0][1],A[1][0])
def sigma(A):return tuple(tuple(sq(x) for x in r) for r in A)
def add(x,y):return tuple(a^b for a,b in zip(x,y))
def scal(c,v):return tuple(mul(c,x) for x in v)
def pair(x,y):return mul(x[0],y[1])^mul(x[1],y[0])

def main():
    start=time.perf_counter();I=((1,0),(0,1));omega=2
    assert sq(omega)^omega==1
    matrices=[(a[:2],a[2:]) for a in product(range(4),repeat=4)]
    group=[A for A in matrices if det(A)==1];assert len(group)==60
    cocycles=[A for A in group if mm(A,sigma(A))==I];assert len(cocycles)==10
    vectors=list(product(range(4),repeat=2));decompositions=0
    for A in cocycles:
        S=lambda v:mv(A,tuple(sq(x) for x in v))
        fixed=[v for v in vectors if S(v)==v];assert len(fixed)==4
        bases=[(u,v) for u in fixed for v in fixed if pair(u,v)==1]
        assert len(bases)==6
        for u,v in bases:
            P=tuple(zip(u,v));assert det(P)==1 and mm(A,sigma(P))==P
        for v in vectors:
            a=add(v,S(v));b=add(scal(sq(omega),v),scal(omega,S(v)))
            assert S(a)==a and S(b)==b and add(b,scal(omega,a))==v
            decompositions+=1
    weights=list(product(range(4),repeat=3));fixed=sum(tuple(sq(x) for x in v)==v for v in weights)
    assert (len(weights),fixed)==(64,8)
    for a in weights:
        for v in weights:
            assert tr(dot(a,tuple(sq(x) for x in v)))==tr(dot(tuple(sq(x) for x in a),v))
    assert 625<648
    assert F(2,3)*F(3,4)*(1-F(9,16))==F(7,32)
    assert F(7,32)/2==F(7,64)
    assert F(100,63*4)==F(25,63)<F(1,2)
    assert (1-F(1,8))/8==F(7,64)
    assert F(6)/(1+10*F(7,64)-2)==64
    assert 35**2>64 and 378>64 and 8**3-1==511>64
    out={'status':'PASS independent exact arithmetic','scope':'Universal proof separately read; finite fields here do not assert all-rank sufficiency.',
         'Sp2_F4_matrices':60,'semilinear_involution_cocycles':10,'fixed_basis_count_each':6,
         'descent_vector_identities':decompositions,'dual_weight_pairs':64*64,
         'rank3_weights':64,'fixed_weights':8,'normalizer_support':'7/64','degree_ceiling':64,
         'seconds':round(time.perf_counter()-start,6)}
    B.joinpath('audit_higher_even_all_fields.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
