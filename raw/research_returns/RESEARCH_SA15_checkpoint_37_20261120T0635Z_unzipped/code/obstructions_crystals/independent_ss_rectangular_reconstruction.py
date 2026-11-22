#!/usr/bin/env python3
"""Independent Cartier reconstruction from the p-basis decomposition f=a²+x b².

No monomial Cartier formula or source matrix-builder is imported.  Sparse
polynomial arithmetic uses y²=y+x³, and exact binary linear algebra solves
for the two Frobenius coefficients before taking b.
"""
from pathlib import Path
from time import perf_counter
import json
start = perf_counter()

def basis(n):
    return [(i,0) for i in range(n//2+1)] + [(i,1) for i in range((n-3)//2+1)]

def add(P,Q):
    return P ^ Q

def reduce_monomial(i,j):
    if j < 2:return {(i,j)}
    return reduce_monomial(i,j-1) ^ reduce_monomial(i+3,j-2)

def mul(P,Q):
    out=set()
    for i,j in P:
        for k,l in Q:out ^= reduce_monomial(i+k,j+l)
    return out

def bits(P,B):
    ix={b:i for i,b in enumerate(B)}
    assert P <= set(B)
    return sum(1<<ix[b] for b in P)

def pivots(cols):
    tab={}
    for i,col in enumerate(cols):
        relation=1<<i
        while col:
            p=col.bit_length()-1
            if p in tab:
                col ^= tab[p][0]; relation ^= tab[p][1]
            else:
                tab[p]=(col,relation);break
        else:raise AssertionError('p-basis columns must be independent')
    return tab

def solve(tab,v):
    relation=0
    while v:
        p=v.bit_length()-1
        assert p in tab
        v ^= tab[p][0]; relation ^= tab[p][1]
    return relation

def one(n):
    B=basis(n); A=basis(n+1); T=basis(2*n+2)
    squared=[mul({u},{u}) for u in A]
    xsquared=[mul({(1,0)},mul({u},{u})) for u in B]
    tab=pivots([bits(v,T) for v in squared+xsquared])
    result=[]
    for u in B:
        row=[]
        for v in B:
            coeff=solve(tab,bits(mul({u},{v}),T))
            # Cartier(f dx) = b dx when f=a²+x b².
            row.append(coeff >> len(A))
        result.append(row)
    return B,result

def rank(cols):
    rows=list(cols);r=0
    for bit in range(17,-1,-1):
        pivot=next((i for i in range(r,len(rows)) if (rows[i]>>bit)&1),None)
        if pivot is None:continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i]>>bit)&1):rows[i]^=rows[r]
        r+=1
    return r

def linear(cols,v):
    return_value=0
    for i,c in enumerate(cols):
        if (v>>i)&1:return_value ^= c
    return return_value

B,P=one(6);D,Q=one(3)
section=74594
columns=[]
for u in range(6):
    for v in range(3):
        col=0
        for a in range(6):
            for b in range(3):
                if not ((section>>(3*a+b))&1):continue
                for i in range(6):
                    for j in range(3):
                        if ((P[a][u]>>i)&1) and ((Q[b][v]>>j)&1):
                            col ^= 1<<(3*i+j)
        columns.append(col)
expected=[4106,12,16432,4177,40,16660,32848,96,131456,33416,320,133280,12424,49472,82080,65664,164608,66560]
assert columns==expected
C2=[linear(columns,c) for c in columns]
assert rank(columns)==rank(C2)==16
assert linear(columns,section)==0
out={'status':'PASS','method':'Independent p-basis solve f=a²+x b² using sparse ring arithmetic; no imported Cartier formula',
     'section_bits':section,'basis_first':B,'basis_second':D,'columns':columns,
     'rank_C':rank(columns),'rank_C2':rank(C2),'elapsed_seconds':perf_counter()-start}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
