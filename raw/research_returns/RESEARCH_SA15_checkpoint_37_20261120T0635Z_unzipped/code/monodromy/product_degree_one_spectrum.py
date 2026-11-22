#!/usr/bin/env python3
"""Explore all F2 sections of O(3O) box O(3O) on the fixed E x E.

This is a finite search certificate, not a proof of generic monodromy.
The three one-factor Cartier multiplication matrices follow directly
from T(1)=1,T(x)=0,T(y)=x,T(x^2)=x,T(xy)=y+1,T(y^2)=y.
"""
import itertools,json,time
from pathlib import Path
import sympy as sp

start=time.perf_counter()
M=[[[1,0,0],[0,0,1],[0,0,0]],
   [[0,0,1],[0,1,0],[0,0,1]],
   [[0,1,0],[1,0,0],[0,1,1]]]
tensor=list(itertools.product(range(3),repeat=2))
matrices=[]
for a,b in tensor:
    matrices.append([[M[a][i][j]*M[b][k][l] for j,l in tensor]
                     for i,k in tensor])

def rank(cols):
    piv={}
    for v in cols:
        while v:
            i=v.bit_length()-1
            if i in piv:v^=piv[i]
            else:piv[i]=v;break
    return len(piv)

def apply(cols,v):
    z=0
    while v:
        i=(v&-v).bit_length()-1;z^=cols[i];v&=v-1
    return z

cols_matrices=[[sum(m[i][j]<<i for i in range(9)) for j in range(9)]
               for m in matrices]

def matrix(s):
    out=[0]*9
    for a,C in enumerate(cols_matrices):
        if s>>a&1:out=[x^y for x,y in zip(out,C)]
    return out

hist={};examples={};regular=[];irreducible_ordinary=[]
Z=sp.Symbol('Z')
for s in range(1,512):
    C=matrix(s)
    power=[1<<i for i in range(9)]
    ranks=[9]
    for j in range(1,10):
        power=[apply(C,v) for v in power];ranks.append(rank(power))
        if ranks[-1]==ranks[-2]:break
    key=','.join(map(str,ranks))
    hist[key]=hist.get(key,0)+1;examples.setdefault(key,s)
    assert apply(C,s)==s
    if ranks[:9]==list(range(9,0,-1)):
        regular.append({'section_bits':s,'columns':C,'ranks':ranks})
    if ranks[1]==9:
        S=sp.Matrix(9,9,lambda i,j:(C[j]>>i)&1)
        cp=sp.Poly(S.charpoly(Z).as_expr(),Z,modulus=2)
        relative=sp.div(cp,sp.Poly(Z+1,Z,modulus=2))[0]
        if relative.is_irreducible:
            irreducible_ordinary.append({'section_bits':s,
                'relative_characteristic_polynomial':str(relative.as_expr()),
                'columns':C})

result={'field':'F2','basis':['Z','X','Y'],
        'ambient':'E x E; E:Y^2Z+XYZ+X^3+Z^3=0',
        'one_factor_Cartier_matrices':M,
        'all_nonzero_sections_tested':511,
        'rank_sequence_histogram':hist,'first_section_for_sequence':examples,
        'regular_nilpotent_relative_examples':regular,
        'ordinary_irreducible_relative_examples':irreducible_ordinary,
        'scope':'Search certificate only; no generic group conclusion',
        'runtime_seconds':time.perf_counter()-start}
dest=Path(__file__).resolve().parents[1]/'outputs'/'product_degree_one_spectrum.json'
dest.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
