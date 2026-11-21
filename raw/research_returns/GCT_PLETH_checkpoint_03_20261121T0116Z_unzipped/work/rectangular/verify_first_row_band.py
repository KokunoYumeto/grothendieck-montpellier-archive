"""Independent exact matrix/coefficient checks for R019.

The coefficient side computes actual determinants and bounded polynomial
multiplication, without replacing any minor by a group-sum formula.
"""
from pathlib import Path
from functools import lru_cache
from collections import defaultdict
from math import factorial, comb
import csv

HERE=Path(__file__).resolve().parent


@lru_cache(None)
def det(matrix):
    n=len(matrix)
    if n==0:return 1
    return sum((-1)**j*entry*det(tuple(tuple(row[k] for k in range(n) if k!=j)
                for row in matrix[1:])) for j,entry in enumerate(matrix[0]) if entry)


def row(r,i,j):
    values=[0]*r;values[i]=1;values[j]-=1
    return tuple(values)


def coefficient(r,L):
    s=r//2;t=r-s;C=r*(L-1)
    A=tuple(row(r,i,s-1) for i in range(s-1))+tuple(row(r,s+j,r-1) for j in range(t-1))
    last=row(r,r-1,s-1)
    units=tuple(tuple(int(i==j) for j in range(r)) for i in range(r))
    determinant=tuple(det((e,)+A+(last,)) for e in units)
    cofactors=[]
    for i in range(r):
        values=[]
        for e in units:
            B=(e,)+A
            minor=tuple(tuple(rr[j] for j in range(r) if j!=i) for rr in B)
            values.append((-1)**(r+i+1)*det(minor))
        cofactors.append(tuple(values))
    factors=[determinant]*C+cofactors
    poly={(0,)*r:1}
    for linear in factors:
        out=defaultdict(int)
        for alpha,c in poly.items():
            for j,value in enumerate(linear):
                if value and alpha[j]<L:
                    beta=list(alpha);beta[j]+=1
                    out[tuple(beta)]+=value*c
        poly={alpha:c for alpha,c in out.items() if c}
    return poly.get((L,)*r,0)


def main():
    rows=[]
    cases=[(r,L) for r in range(2,7) for L in range(1,5) if (r*L)%2==0]
    cases += [(7,2),(8,1),(8,2)]
    for r,L in cases:
        s=r//2;t=r-s;C=r*(L-1)
        actual=coefficient(r,L)
        numerator=(-1)**s*comb(C,s*L-t)*factorial(s*L)*factorial(t*L)
        denominator=factorial(L)**r
        assert numerator%denominator==0
        expected=numerator//denominator
        assert actual==expected and actual,(r,L,actual,expected)
        rows.append(dict(r=r,L=L,b=r*L-1,
            highest_weight=','.join(map(str,(r*L,)*(r-1)+(C,))),
            determinant_DP=actual,closed_coefficient=expected,status='PASS'))
    with (HERE/'FIRST_ROW_BAND_COEFFICIENT_CHECK.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t')
        writer.writeheader();writer.writerows(rows)
    print('PASS',len(rows),'exact actual-matrix coefficient checks')


if __name__=='__main__':main()
