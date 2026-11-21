#!/usr/bin/env python3
"""Exact obstruction to border rank 10 for the exceptional five-permanent tensor.

The proof and all 26 possible quotient weights are in PENCIL_PROOFS.md.
This script constructs every matrix from scratch and evaluates the required
minor over Z, not merely with floating point or sampled parameters.
"""
from collections import defaultdict
from itertools import combinations
from pathlib import Path
import json
import math
import numpy as np
from sympy import Matrix
from sympy.polys.matrices import DomainMatrix

PRIME=1000003
A_DIM=5
B_DIM=9
# q1=ae+bd, q2=af+cd, q3=bf+ce, q4=ah+bg, q5=ai+cg.
RECTANGLES=[((0,1),(0,1)),((0,1),(0,2)),((0,1),(1,2)),
            ((0,2),(0,1)),((0,2),(0,2))]
VARIABLES=[(i,j) for i in range(3) for j in range(3)]


def weight_var(i,j):
    return tuple(int(k==i) for k in range(3))+tuple(int(k==j) for k in range(3))


def weight_quad(I,J):
    return tuple(int(k in I) for k in range(3))+tuple(int(k in J) for k in range(3))


def tensor():
    result=np.zeros((A_DIM,B_DIM,B_DIM),dtype=np.int64)
    for q,((r,s),(c,d)) in enumerate(RECTANGLES):
        a,b,x,y=3*r+c,3*r+d,3*s+c,3*s+d
        for i,j in [(a,y),(y,a),(b,x),(x,b)]:
            result[q,i,j]=1
    return result


def weights():
    classes=defaultdict(list)
    for q,(I,J) in enumerate(RECTANGLES):
        for v,(i,j) in enumerate(VARIABLES):
            w=tuple(x-y for x,y in zip(weight_var(i,j),weight_quad(I,J)))
            classes[w].append((q,v))
    image={tuple(-x for x in weight_var(*v)):c for c,v in enumerate(VARIABLES)}
    return classes,image


def maximal_extension(T,weight,block,image):
    basis=[T[:,:,c].copy() for c in range(B_DIM) if image.get(weight)!=c]
    for q,v in block:
        mat=np.zeros((A_DIM,B_DIM),dtype=np.int64)
        mat[q,v]=1
        basis.append(mat)
    return basis


def prolongation_matrix(basis,orientation):
    # orientation B: L tensor B -> A tensor Lambda^2 B.
    # orientation A: A tensor L -> Lambda^2 A tensor B.
    matrices=basis if orientation=='B' else [M.T for M in basis]
    n1,n2=matrices[0].shape
    pairs=list(combinations(range(n2),2))
    out=np.zeros((n1*len(pairs),len(basis)*n2),dtype=np.int64)
    for p,(i,j) in enumerate(pairs):
        for q in range(n1):
            for s,L in enumerate(matrices):
                out[q*len(pairs)+p,s*n2+j]=L[q,i]
                out[q*len(pairs)+p,s*n2+i]=-L[q,j]
    return out


def pivots(matrix):
    a=matrix.copy()%PRIME
    ids=list(range(a.shape[0]))
    rows=[];cols=[]
    r=0
    for c in range(a.shape[1]):
        nz=np.flatnonzero(a[r:,c])
        if not len(nz):continue
        rr=r+int(nz[0])
        if rr!=r:
            a[[r,rr]]=a[[rr,r]]
            ids[r],ids[rr]=ids[rr],ids[r]
        rows.append(ids[r]);cols.append(c)
        a[r,c:]=(a[r,c:]*pow(int(a[r,c]),-1,PRIME))%PRIME
        for rr in range(r+1,a.shape[0]):
            if a[rr,c]:a[rr,c:]=(a[rr,c:]-a[rr,c]*a[r,c:])%PRIME
        r+=1
        if r==a.shape[0]:break
    return rows,cols


def main():
    # A deterministic elementary primality check makes the exploratory pivot
    # computation self-contained. The final minors are integer determinants.
    assert all(PRIME%d for d in range(2,math.isqrt(PRIME)+1))
    T=tensor();classes,image=weights()
    result=[]
    assert len(classes)==28
    assert sum(len(block)-(w in image) for w,block in classes.items())==36
    for number,(w,block) in enumerate(classes.items()):
        quotient_dim=len(block)-(w in image)
        if quotient_dim==0:continue
        basis=maximal_extension(T,w,block,image)
        assert len(basis)==9+quotient_dim
        options=[]
        for orientation in ['A','B']:
            M=prolongation_matrix(basis,orientation)
            rows,cols=pivots(M)
            nullity_upper=M.shape[1]-len(rows)
            if nullity_upper<10:
                # A minor of this order alone proves nullity at most nine.
                order=M.shape[1]-9
                rows,cols=rows[:order],cols[:order]
                minor=M[np.ix_(rows,cols)].tolist()
                det=int(DomainMatrix.from_Matrix(Matrix(minor)).det())
                assert det!=0 and det%PRIME!=0
                options.append({'orientation':orientation,'matrix_shape':list(M.shape),
                                'nullity_upper_from_mod_p':nullity_upper,'minor_order':order,
                                'minor_rows':rows,'minor_cols':cols,'determinant_Z':det,
                                'certified_nullity_upper':9})
        assert options, ('Unexcluded weight',number,w)
        # Prefer a unit determinant, then the smaller matrix/minor.
        chosen=min(options,key=lambda x:(abs(x['determinant_Z'])!=1,x['minor_order']))
        result.append({'weight_number':number,'weight':w,'block':block,
                       'quotient_weight_dimension':quotient_dim,'maximal_extension_dimension':len(basis),
                       'chosen_certificate':chosen,
                       'other_certificates': [x for x in options if x is not chosen]})
    assert len(result)==26
    output={'statement':'BR of the exceptional five-permanent tensor is at least 11',
            'proof':'Every possible torus weight extension violates a necessary prolongation dimension >=10.',
            'weight_classes_total':len(classes),'quotient_weights_checked':len(result),
            'records':result}
    path=Path(__file__).with_name('per5_prolongation_certificate.json')
    path.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':'PASS','weights_checked':26,
                      'chosen_integer_determinants':[r['chosen_certificate']['determinant_Z'] for r in result],
                      'certificate':str(path)},indent=2))


if __name__=='__main__':main()
