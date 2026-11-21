"""G039: cubic transfer, curvature quotient, and independent finite numerators."""
from pathlib import Path
from fractions import Fraction
from itertools import combinations_with_replacement, product
from collections import Counter
import sys,json

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"root"))
import stable_third_row_positive as target
from check_stable_second_row_independent import (
    compositions, rank, schur_dimension, partitions, character,
    centralizer, fake
)


def cubic_dimensions(d,D):
    kernel=cokernel=blocks=0
    for beta in compositions(D,d):
        rows=[gamma for gamma in compositions(2,d) if all(v<=w for v,w in zip(gamma,beta))]
        columns=[]
        for gamma in compositions(3,d):
            if not all(v<=w for v,w in zip(gamma,beta)):continue
            col={}
            for i,v in enumerate(gamma):
                if v:
                    row=gamma[:i]+(gamma[i]-1,)+gamma[i+1:]
                    col[row]=v
            columns.append(col)
        image=rank(columns)
        kernel+=len(columns)-image;cokernel+=len(rows)-image;blocks+=1
    return kernel,cokernel,blocks


def sym_monomial(i,j,d):
    return [[Fraction(int(u==i and v==j)+int(u==j and v==i),2)
             for v in range(d)] for u in range(d)]


def kulkarni(A,B):
    d=len(A)
    return {(i,j,k,l): A[i][k]*B[j][l]+A[j][l]*B[i][k]
                           -A[i][l]*B[j][k]-A[j][k]*B[i][l]
            for i,j,k,l in product(range(d),repeat=4)}


def ricci(R,ginverse,d):
    return [[sum(ginverse[i][k]*R[i,j,k,l] for i in range(d) for k in range(d))
             for l in range(d)] for j in range(d)]


def metric_trace(B,ginverse):
    return sum(ginverse[i][j]*B[i][j] for i in range(len(B)) for j in range(len(B)))


def complete(cycle,degree):
    P=[1]+[0]*degree
    for length in cycle:
        for i in range(length,degree+1):P[i]+=P[i-length]
    return tuple(P[i]-(P[i-1] if i else 0) for i in range(degree+1))


def exact_integer(x):
    assert x.denominator==1
    return int(x)


def independent_numerator(nu,counts):
    m=sum(nu);N=m*(m-1)//2;shapes=partitions(m)
    coeff={rho:Fraction(character(nu,rho),centralizer(rho)) for rho in shapes}
    h={rho:complete(rho,3) for rho in shapes}
    c2=exact_integer(sum((coeff[rho]*h[rho][2] for rho in shapes),Fraction()))
    c21=exact_integer(sum((coeff[rho]*(h[rho][2]*h[rho][1]-h[rho][3])
                          for rho in shapes),Fraction()))
    cR=exact_integer(sum((coeff[rho]*(h[rho][2]**2-h[rho][3]*h[rho][1]-h[rho][2])
                         for rho in shapes),Fraction()))
    assert min(c2,c21,cR)>=0
    result=[0]*(N+4)
    for alpha in shapes:
        a=exact_integer(sum((coeff[rho]*character(alpha,rho)*h[rho][3]
                             for rho in shapes),Fraction()))
        b=exact_integer(sum((coeff[rho]*character(alpha,rho)*h[rho][2]
                             for rho in shapes),Fraction()))
        assert a==target.S3(nu).get(alpha,0)
        assert b==target.S2(nu).get(alpha,0)
        counts["literal_tensor_operator_entries"]+=2
        for j,v in enumerate(fake(alpha)):
            result[j+3]+=a*v;result[j+2]-=b*v
    for shift,multiplicity,weights in (
        (2,c2,(4,)+tuple(range(3,m+1))),
        (3,c21,tuple(range(2,m+1))),
        (4,cR,tuple(range(2,m+1)))):
        result[shift]+=multiplicity
        for w in weights:result[shift+w]-=multiplicity
    while len(result)>1 and not result[-1]:result.pop()
    assert all(v>=0 for v in result)
    return tuple(result),(c2,c21,cR)


def main():
    counts=Counter()
    for d in range(2,6):
        for D in range(2,9):
            kernel,cokernel,blocks=cubic_dimensions(d,D)
            assert kernel==(schur_dimension((D-3,3),d) if D>=6 else 0),(d,D,kernel)
            shape={2:(2,),3:(2,1),4:(2,2)}.get(D)
            assert cokernel==(schur_dimension(shape,d) if shape else 0),(d,D,cokernel)
            counts["actual_cubic_degree_maps"]+=1
            counts["exact_multidegree_blocks"]+=blocks
    for d in range(3,7):
        g=[[Fraction(1+int(i==j)) for j in range(d)] for i in range(d)]
        gi=[[Fraction(int(i==j))-Fraction(1,d+1) for j in range(d)] for i in range(d)]
        for u,v in combinations_with_replacement(range(d),2):
            B=sym_monomial(u,v,d);R=kulkarni(g,B);S=ricci(R,gi,d)
            traceB=metric_trace(B,gi)
            assert S==[[(d-2)*B[i][j]+traceB*g[i][j] for j in range(d)] for i in range(d)]
            traceS=metric_trace(S,gi)
            recovered=[[(S[i][j]-traceS*g[i][j]/(2*(d-1)))/(d-2)
                        for j in range(d)] for i in range(d)]
            assert recovered==B
            for i,j,k,l in product(range(d),repeat=4):
                assert R[i,j,k,l]==-R[j,i,k,l]==R[k,l,i,j]
                assert R[i,j,k,l]+R[i,k,l,j]+R[i,l,j,k]==0
            counts["ricci_inverse_basis_tensors"]+=1
    # The displayed curvature quotient kills every literal degree-four transfer column.
    for d in range(2,5):
        for first in range(d):
            for triple in combinations_with_replacement(range(d),3):
                image=Counter()
                for index in set(triple):
                    remaining=list(triple);remaining.remove(index)
                    A=sym_monomial(first,index,d)
                    B=sym_monomial(remaining[0],remaining[1],d)
                    for slot,value in kulkarni(A,B).items():
                        image[slot]+=triple.count(index)*value
                assert not any(image.values()),(d,first,triple)
                counts["quotient_kills_actual_transfer_columns"]+=1
    for m in range(4,8):
        for nu in partitions(m):
            assert independent_numerator(nu,counts)==target.free_numerator(nu)
            counts["independent_free_numerators"]+=1
    receipt={
        "statement":"G039 independent cubic-map, Ricci, and numerator audit",
        "status":"PASS",
        "methods":[
            "actual cubic monomial transfer columns and exact rational elimination",
            "nonorthonormal invariant Gram matrix; literal four-index curvature and Ricci inverse",
            "literal degree-four transfer images killed by the curvature quotient",
            "independent Young-permutation/Jacobi-Trudi character rows and direct SYT fake degrees"
        ],
        **dict(counts),
        "root_MN_or_hook_quotient_checker":"not imported",
        "prior_independent_helper":"A092 character, tableau, and exact elimination routines"
    }
    (HERE/"STABLE_THIRD_ROW_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))


if __name__=="__main__":main()
