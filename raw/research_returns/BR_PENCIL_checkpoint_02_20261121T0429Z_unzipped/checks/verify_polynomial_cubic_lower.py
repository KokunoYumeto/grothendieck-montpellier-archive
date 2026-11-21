#!/usr/bin/env python3
"""Independent stdlib verification of the polynomial cubic Koszul minors."""
from itertools import combinations,product
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent
SOURCE=list(combinations(range(12),4))
TARGET=list(combinations(range(12),5))
EW=[tuple(int(h==i//4) for h in range(3))+tuple(int(h==i%4) for h in range(4)) for i in range(12)]
AW=[(-1,-1,-1,-1,-1,-1,0),(-1,-1,-1,-1,-1,0,-1)]

def add(*ws):return tuple(sum(x) for x in zip(*ws))
def parity(p):return (-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))

def coefficient(a,b,c,d,sign):
    rows=(b//4,c//4,d//4);cols=(b%4,c%4,d%4)
    if set(rows)!={0,1,2} or set(cols)!={0,1,2+a}:return 0
    return parity(rows)*parity(cols) if sign==-1 else 1

def source(col):
    alpha,rest=divmod(col,len(SOURCE)*12);i,k=divmod(rest,12)
    return alpha,SOURCE[i],k

def target(row):
    j,l=divmod(row,12)
    return TARGET[j],l

def entry(row,col,sign):
    J,l=target(row);alpha,I,k=source(col)
    missing=[j for j in J if j not in I]
    if len(missing)!=1:return 0
    j=missing[0]
    return (-1)**(1-alpha+sum(i<j for i in I))*coefficient(1-alpha,j,k,l,sign)

def determinant(M):
    n=len(M)
    if n==0:return 1
    M=[row[:] for row in M];previous=1;sgn=1
    for k in range(n-1):
        if M[k][k]==0:
            p=next((p for p in range(k+1,n) if M[p][k]),None)
            if p is None:return 0
            M[k],M[p]=M[p],M[k];sgn=-sgn
        pivot=M[k][k]
        for i in range(k+1,n):
            left=M[i][k]
            for j in range(k+1,n):
                value=M[i][j]*pivot-left*M[k][j]
                assert value%previous==0
                M[i][j]=value//previous
            M[i][k]=0
        previous=pivot
    return sgn*M[-1][-1]

def main():
    cases=json.loads((HERE/'polynomial_cubic_lower_certificate.json').read_text())
    start=time.time();summary=[]
    for case in cases:
        sign=-1 if case['family']=='det' else 1
        assert case['p']==4 and case['pure_cost']==330
        assert case['matrix_shape']==[9504,11880]
        # Verify the tensor and every nonzero coefficient is homogeneous.
        terms=0
        for a,b,c,d in product(range(2),range(12),range(12),range(12)):
            if coefficient(a,b,c,d,sign):
                terms+=1
                assert add(AW[a],EW[b],EW[c],EW[d])==(0,)*7
        assert terms==72
        weights=set();rank=0;allrows=set();allcols=set()
        field=case['field_condition']
        assert (case['family'],field) in [('det','characteristic_not2or3'),('per','all_characteristics')]
        for block in case['blocks']:
            w=tuple(block['weight']);assert w not in weights;weights.add(w)
            rows,cols=block['rows'],block['cols']
            assert len(rows)==len(cols)==len(set(rows))==len(set(cols))
            assert not allrows.intersection(rows) and not allcols.intersection(cols)
            allrows.update(rows);allcols.update(cols)
            for row in rows:
                assert 0<=row<9504
                J,l=target(row)
                assert add(AW[0],AW[1],*(EW[j] for j in J),EW[l])==w
            for col in cols:
                assert 0<=col<11880
                alpha,I,k=source(col)
                assert add(AW[alpha],*(EW[i] for i in I),tuple(-x for x in EW[k]))==w
            value=determinant([[entry(r,c,sign) for c in cols] for r in rows])
            assert value==block['determinant_Z']!=0
            if field=='all_characteristics':assert abs(value)==1
            else:
                unit=abs(value)
                for p in [2,3]:
                    while unit%p==0:unit//=p
                assert unit==1
            rank+=len(rows)
        assert rank==case['certified_rank'] and rank>20*330
        rec={'family':case['family'],'blocks_verified':len(weights),'rank_lower_bound':rank,
             'pure_cost':330,'border_rank_lower_bound':21,'field_scope':field,'status':'PASS'}
        summary.append(rec);print(json.dumps(rec),flush=True)
    output={'results':summary,'seconds':time.time()-start,'method':'exact integer block minors, independently reconstructed entries and weights'}
    (HERE/'polynomial_cubic_lower_verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print('PASS seconds',time.time()-start)

if __name__=='__main__':main()
