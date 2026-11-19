#!/usr/bin/env python3
"""Exact six-generator reconstruction of the R-vanishing calculation."""
from itertools import combinations
from functools import lru_cache
from time import perf_counter

G=5;letters=tuple(range(2*G));prime=1009;started=perf_counter()

def pair(x,y):
    return (1 if x%2==0 else -1) if x//2==y//2 and x!=y else 0

def addterm(out,w,c):
    if c:
        out[w]=out.get(w,0)+c
        if not out[w]:del out[w]

def johnson(t):
    D=[{} for _ in letters]
    for i,x in enumerate(t):
        y,z=t[(i+1)%3],t[(i+2)%3]
        c=pair(x^1,x)
        addterm(D[x^1],(y,z),c);addterm(D[x^1],(z,y),-c)
    return D

def act(D,P,out,sign):
    for word,c in P.items():
        for i,x in enumerate(word):
            for tail,d in D[x].items():
                addterm(out,word[:i]+tail+word[i+1:],sign*c*d)

def bracket(D,E):
    out=[]
    for x in letters:
        Q={};act(D,E[x],Q,1);act(E,D[x],Q,-1);out.append(Q)
    return out

def matchings(items):
    if not items:yield ();return
    a=items[0]
    for j in range(1,len(items)):
        for rest in matchings(items[1:j]+items[j+1:]):yield ((a,items[j]),)+rest

chords=list(matchings(tuple(range(8))));index={m:i for i,m in enumerate(chords)}

@lru_cache(maxsize=300000)
def contractions(word):
    def visit(items,pairs,sgn):
        if not items:
            yield index[tuple(pairs)],sgn;return
        i=items[0]
        for k in range(1,len(items)):
            j=items[k];c=pair(word[i],word[j])
            if c:yield from visit(items[1:k]+items[k+1:],pairs+[(i,j)],sgn*c)
    return tuple(visit(tuple(range(8)),[],1))

def detector(D):
    out=[0]*105
    for x in letters:
        first=x^1;sign=-1 if x%2==0 else 1
        for tail,c in D[x].items():
            if tail[-1]!=0:continue
            word=(first,)+tail[:-1]
            for i,v in contractions(word):out[i]+=sign*c*v
    return out

rterms=[(-2,((0,1),(2,4),(3,6),(5,7))),
 (2,((0,1),(2,5),(3,6),(4,7))),
 (2,((0,1),(2,5),(3,7),(4,6))),
 (2,((0,1),(2,6),(3,5),(4,7))),
 (1,((0,2),(1,5),(3,6),(4,7)))]


import sympy as sp
WITNESSES=[[[3, 7, 5], [1, 2, 0], [9, 8, 6], [6, 8, 5], [2, 4, 7], [9, 0, 3], [4, 6, 7]], [[9, 5, 0], [6, 4, 7], [6, 2, 0], [6, 5, 8], [7, 3, 8], [1, 4, 3], [9, 2, 7]], [[1, 3, 4], [4, 2, 0], [5, 7, 0], [9, 2, 7], [5, 6, 8], [5, 3, 0], [1, 4, 6]], [[0, 1, 4], [3, 5, 0], [9, 0, 5], [2, 3, 9], [4, 6, 8], [8, 1, 0], [2, 7, 1]], [[3, 7, 0], [4, 9, 6], [3, 5, 2], [7, 3, 8], [6, 7, 2], [0, 8, 9], [1, 2, 6]], [[5, 4, 0], [0, 8, 1], [5, 2, 3], [7, 4, 3], [0, 4, 1], [6, 5, 2], [6, 7, 9]]]

rows=[]
for number,triples in enumerate(WITNESSES,1):
    assert len(triples)==7 and all(len(set(t))==3 for t in triples)
    D=johnson(triples[0])
    for t in triples[1:]:D=bracket(D,johnson(t))
    assert any(D)
    # Degree seven and exact torus weight x1 of the derivation tensor.
    for x in letters:
        for tail,c in D[x].items():
            assert len(tail)==8 and isinstance(c,int)
            tensor=(x^1,)+tail
            weight=[sum(1 if y==2*h else -1 if y==2*h+1 else 0 for y in tensor) for h in range(G)]
            assert weight==[1,0,0,0,0]
    # Literal specialness: D(sum[x_i,y_i])=0.
    omega={}
    for h in range(G):omega[(2*h,2*h+1)]=1;omega[(2*h+1,2*h)]=-1
    special={};act(D,omega,special,1);assert not special
    K=detector(D);rv=sum(c*K[index[m]] for c,m in rterms)
    assert rv==0
    rows.append(K)
    print('WITNESS',number,'TRIPLES',triples,'TERMS',sum(map(len,D)),'R',rv,flush=True)
    print('DETECTOR',K,flush=True)
A=sp.Matrix(rows)
_,columns=A.rref();columns=list(columns)
assert len(columns)==6
minor=A[:,columns];det=minor.det();assert det!=0
print('PIVOT_CONTRACTIONS_ZERO_BASED',columns,flush=True)
print('EXACT_SIX_BY_SIX_MINOR',minor.tolist(),flush=True)
print('EXACT_NONZERO_DETERMINANT',det,flush=True)
print('R_VALUES',[sum(c*row[index[m]] for c,m in rterms) for row in rows],flush=True)
print('PASSED: six actual degree-seven Johnson brackets have independent H-valued detector vectors and zero R; all are supported on five handles.',flush=True)
print('SCOPE: the complete R-vanishing proof additionally uses the opened primary stable multiplicity bound J7[1]<=6 and the proved actual stabilization map.',flush=True)
print('ACTUAL_WALL_SECONDS',format(perf_counter()-started,'.9f'),flush=True)
