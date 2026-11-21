#!/usr/bin/env python3
"""Exact modular Hilbert-function obstructions for an AB extension space.

For E subset A tensor B, annihilate E in bidegree(1,1), multiply in the
ordinary symmetric algebra, and bound the quotient in bidegree(p,q).
Coordinate monomial relations are eliminated before matrix construction.
"""
from itertools import combinations_with_replacement,product
from collections import defaultdict
import math
import numpy as np
from sympy import Matrix
from det7_prolongation import rank

def primitive(v):
    den=math.lcm(*(int(x.q) for x in v));out=[int(x*den) for x in v]
    g=math.gcd(*out)
    if not g:return []
    out=[x//abs(g) for x in out]
    if next(x for x in out if x)<0:out=[-x for x in out]
    return out

def hilbert(E,p=2,q=2):
    a,b=E[0].shape
    flat=np.stack([M.reshape(-1) for M in E],axis=1)
    null=Matrix(flat.T.tolist()).nullspace()
    assert len(null)==a*b-len(E)
    relations=[];forbidden=set()
    for v in null:
        cs=primitive(v);nz=[(h//b,h%b,c) for h,c in enumerate(cs) if c]
        if len(nz)==1:forbidden.add(nz[0][:2])
        else:relations.append(nz)
    AM=list(combinations_with_replacement(range(a),p));BM=list(combinations_with_replacement(range(b),q))
    monomials=[(I,J) for I in AM for J in BM if not any((i,j) in forbidden for i in I for j in J)]
    index={M:i for i,M in enumerate(monomials)}
    am=list(combinations_with_replacement(range(a),p-1));bm=list(combinations_with_replacement(range(b),q-1))
    rows=set()
    for rel in relations:
        for I,J in product(am,bm):
            row=defaultdict(int)
            for h,v,c in rel:
                mon=(tuple(sorted(I+(h,))),tuple(sorted(J+(v,))))
                if mon in index:row[index[mon]]+=c
            r=tuple(sorted((k,v) for k,v in row.items() if v))
            if r:rows.add(r)
    rows=sorted(rows);mat=np.zeros((len(rows),len(monomials)),dtype=np.int64)
    for i,row in enumerate(rows):
        for j,c in row:mat[i,j]=c
    r,rs,cs=rank(mat)
    return {'bidegree':[p,q],'remaining_monomials':len(monomials),'relation_rows':len(rows),
            'rank_mod_p':r,'hilbert_upper_bound':len(monomials)-r,
            'matrix':mat,'rows':rs,'cols':cs,'monomials':monomials}
