#!/usr/bin/env python3
"""Standalone exact check of P-11's minors and explicit upper expressions."""
from itertools import combinations, permutations, product
from pathlib import Path
from collections import defaultdict
import json

HERE=Path(__file__).resolve().parent
PAIRS=list(combinations(range(4),2))

def tensor(sign):
    values={}
    for a,last in enumerate((2,3)):
        labels=(0,1,last)
        for order in permutations(range(3)):
            inversions=sum(order[i]>order[j] for i in range(3) for j in range(i+1,3))
            values[(a,)+tuple(labels[i] for i in order)]=sign**inversions
    return values

def entry(T,row,col):
    pair_index,l=divmod(row,4)
    alpha,rest=divmod(col,16)
    u,k=divmod(rest,4)
    i,j=PAIRS[pair_index]
    a=1-alpha
    return (-1)**a*((u==j)*T.get((a,i,k,l),0)-(u==i)*T.get((a,j,k,l),0))

def det(M):
    a=[row[:] for row in M]
    previous=1;sign=1
    for k in range(len(a)-1):
        if not a[k][k]:
            p=next((p for p in range(k+1,len(a)) if a[p][k]),None)
            if p is None:return 0
            a[k],a[p]=a[p],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,len(a)):
            for j in range(k+1,len(a)):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value%previous==0
                a[i][j]=value//previous
        for i in range(k+1,len(a)):a[i][k]=0
        previous=pivot
    return sign*a[-1][-1]

def main():
    certs=json.loads((HERE/'adjacent_cubic_certificates.json').read_text())
    for cert in certs:
        T=tensor(1 if cert['family']=='per' else -1)
        rows,cols=cert['rows'],cert['cols']
        assert len(rows)==len(cols)==cert['threshold_order']
        assert len(set(rows))==len(set(cols))==len(rows)
        assert cert['pure_cost']==3
        value=det([[entry(T,r,c) for c in cols] for r in rows])
        assert value==cert['determinant_Z']
        assert (cert['family'],len(rows),value) in [('per',16,1),('det',19,4)]
        print(cert['family'],len(rows),'minor determinant',value)

    # Two mixed finite differences; retain each tensor word and t degree.
    curve=defaultdict(int);evaluation_sets=set()
    for a,last in enumerate((2,3)):
        for R,c in [((),1),((1,),-1),((last,),-1),((1,last),1)]:
            evaluation_sets.add(R)
            for word in product((0,)+R,repeat=3):
                degree=sum(v!=0 for v in word)-2
                curve[(a,word,degree)]+=c
    assert len(evaluation_sets)==6
    assert all(not v for (a,w,d),v in curve.items() if d<0)
    T=tensor(1)
    for a,*w in product(range(2),range(4),range(4),range(4)):
        assert curve[(a,tuple(w),0)]==T.get((a,)+tuple(w),0)
    print('permanent six-term curve: all128 constant coefficients and negative-power cancellations PASS')

    # Eight-term determinant curve. A vector is a list of (basis, t-degree,
    # integer coefficient) triples. Every atom has one scalar t exponent.
    e=lambda v:[(v,0,1)]
    affine=lambda v,z,sgn:[(v,0,1),(z,1,sgn)]
    atoms=[]
    for a,z in enumerate((2,3)):
        atoms.append((-1,1,[e(a),affine(0,z,1),affine(0,z,-1),affine(1,z,1)]))
    atoms.append((-1,-1,[[(0,0,1),(1,0,1)],e(0),e(0),e(1)]))
    for a,z in enumerate((2,3)):
        atoms.append((-1,1,[e(a),affine(1,z,-1),affine(1,z,1),affine(0,z,-1)]))
    atoms.append((-1,-1,[[(0,0,1),(1,0,1)],e(1),e(1),e(0)]))
    for a,z in enumerate((2,3)):
        atoms.append((0,-1,[e(a),[(0,0,1),(1,0,1)],[(0,0,1),(1,0,-1)],e(z)]))
    assert len(atoms)==8
    curve=defaultdict(int)
    for scalar_degree,scalar_coeff,factors in atoms:
        for choices in product(*factors):
            word=tuple(q[0] for q in choices)
            degree=scalar_degree+sum(q[1] for q in choices)
            coeff=scalar_coeff
            for q in choices:coeff*=q[2]
            curve[word,degree]+=coeff
    assert all(not v for (w,d),v in curve.items() if d<0)
    T=tensor(-1)
    for w in product(range(2),range(4),range(4),range(4)):
        assert curve[w,0]==T.get(w,0)
    print('determinant eight-term curve: all128 constant coefficients and negative-power cancellations PASS overZ')

    # Independent reconstruction of the Borel multiplication certificates.
    # Columns: BC, BD, CD; the indicated 9-plane basis; free index 0..3.
    # No generator, array package, or rank/nullspace oracle is used here.
    borel=json.loads((HERE/'adjacent_cubic_borel_certificate.json').read_text())
    expected_types=list(product((0,1),repeat=3))
    assert [tuple(c['types_BC_BD_CD']) for c in borel['cases']]==expected_types
    expected_dets=(-4,4,-4,8,16,32,-64,-64)
    for case,expected_det in zip(borel['cases'],expected_dets):
        kinds=case['types_BC_BD_CD'];bases=[]
        for kind in kinds:
            basis=[]
            for i in range(4):
                for j in range(i,4):
                    if (i,j)==(0,0) or (kind==1 and (i,j)==(0,1)):continue
                    basis.append({(i,j):1,(j,i):1})
            if kind==1:basis.append({(2,3):1,(3,2):-1})
            assert len(basis)==9
            bases.append(basis)
        def multiplication_entry(row,col):
            b,rest=divmod(row,16);c,d=divmod(rest,4)
            block,rest=divmod(col,36);pair_index,free=divmod(rest,4)
            pair,other=(((b,c),d),((b,d),c),((c,d),b))[block]
            return bases[block][pair_index].get(pair,0) if other==free else 0
        rows,cols=case['rows'],case['cols']
        assert case['matrix_shape']==[64,108] and case['minor_order']==58
        assert len(rows)==len(cols)==len(set(rows))==len(set(cols))==58
        assert all(0<=r<64 for r in rows) and all(0<=c<108 for c in cols)
        value=det([[multiplication_entry(r,c) for c in cols] for r in rows])
        assert value==case['determinant_Z']==expected_det
        assert abs(value)&(abs(value)-1)==0
        print('Borel types',tuple(kinds),'58-minor determinant',value)

    # The earlier nine-term rank formula is retained as an independently
    # checked source specialization, although it is no longer the best bound.
    data=json.loads((HERE/'adjacent_det9_upper.json').read_text())
    assert data['denominator']==2 and len(data['atoms'])==9
    T=tensor(-1)
    for ix in product(range(2),range(4),range(4),range(4)):
        total=0
        for atom in data['atoms']:
            term=atom['numerator']
            for factor,index in zip(atom['factors'],ix):term*=factor[index]
            total+=term
        assert total==2*T.get(ix,0)
    print('determinant nine-term expression: all128 coefficients overZ PASS')
    print('PASS P-11: permanent6allfields; determinant8awaychar2; determinant6inchar2')

if __name__=='__main__':main()
