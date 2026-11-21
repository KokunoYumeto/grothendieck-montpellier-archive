#!/usr/bin/env python3
"""Generate exact 58-minor certificates for the cubic determinant seed.

The independent checker rebuilds every map without importing this file.
"""
from itertools import combinations_with_replacement, product
from pathlib import Path
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
P=1000003

def pair_basis(kind):
    result=[]
    for i,j in combinations_with_replacement(range(4),2):
        if (i,j)==(0,0) or (kind==1 and (i,j)==(0,1)):
            continue
        v=np.zeros((4,4),dtype=np.int64)
        v[i,j]=1;v[j,i]=1
        result.append(v)
    if kind==1:
        v=np.zeros((4,4),dtype=np.int64)
        v[2,3]=1;v[3,2]=-1;result.append(v)
    assert len(result)==9
    return result

def multiplication(kinds):
    cols=[]
    for (i,j),kind in zip(((0,1),(0,2),(1,2)),kinds):
        k=3-i-j
        for v in pair_basis(kind):
            for q in range(4):
                t=np.zeros((4,4,4),dtype=np.int64)
                for a,b in product(range(4),repeat=2):
                    ix=[0,0,0];ix[i]=a;ix[j]=b;ix[k]=q
                    t[tuple(ix)]=v[a,b]
                cols.append(t.ravel())
    return np.array(cols,dtype=np.int64).T

def pivots(matrix):
    a=matrix.copy()%P
    labels=list(range(a.shape[0]));rows=[];cols=[];r=0
    for c in range(a.shape[1]):
        possible=np.flatnonzero(a[r:,c])
        if not len(possible):continue
        h=r+int(possible[0])
        a[[r,h]]=a[[h,r]];labels[r],labels[h]=labels[h],labels[r]
        rows.append(labels[r]);cols.append(c)
        a[r,c:]=a[r,c:]*pow(int(a[r,c]),-1,P)%P
        inds=np.flatnonzero(a[r+1:,c])+r+1
        if len(inds):a[inds,c:]=(a[inds,c:]-a[inds,c,None]*a[r,c:])%P
        r+=1
        if r==len(a):break
    return rows,cols

def main():
    cases=[]
    for kinds in product((0,1),repeat=3):
        M=multiplication(kinds)
        rows,cols=pivots(M)
        assert len(rows)>=58
        rows=rows[:58];cols=cols[:58]
        value=int(sp.Matrix(M[np.ix_(rows,cols)].tolist()).det(method='domain-ge'))
        assert value and abs(value)&(abs(value)-1)==0
        case={'types_BC_BD_CD':list(kinds),'matrix_shape':list(M.shape),
              'minor_order':58,'rows':rows,'cols':cols,'determinant_Z':value}
        cases.append(case)
        print(kinds,value,flush=True)
    output={'basis_order':'pair lexicographic i<=j; omit00 always, omit01 for type1; append23-32 for type1; blocks BC,BD,CD; then pair basis then free index0..3; rows lexicographic B,C,D',
            'types':{'0':'symmetric tensors except00','1':'symmetric tensors except00,01 plus23-32'},
            'cases':cases}
    (HERE/'adjacent_cubic_borel_certificate.json').write_text(json.dumps(output,indent=2)+'\n')

if __name__=='__main__':main()
