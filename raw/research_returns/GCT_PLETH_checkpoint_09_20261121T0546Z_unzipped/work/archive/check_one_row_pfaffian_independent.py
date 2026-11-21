"""R048: exact Pfaffian congruences and paired Schur characters."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from math import prod
import json

HERE=Path(__file__).resolve().parent


def multiply(A,B):
    return [[sum(A[i][h]*B[h][j] for h in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def identity(n):
    return [[Fraction(i==j) for j in range(n)] for i in range(n)]


def pfaffian(A):
    n=len(A)
    if n==0:return Fraction(1)
    if n%2:return Fraction()
    return sum(((-1)**(j+1)*A[0][j]*
                pfaffian([[A[u][v] for v in range(1,n) if v!=j]
                          for u in range(1,n) if u!=j])
                for j in range(1,n)),Fraction())


def determinant(A):
    A=[list(map(Fraction,row)) for row in A];n=len(A);answer=Fraction(1)
    for i in range(n):
        p=next((j for j in range(i,n) if A[j][i]),None)
        if p is None:return Fraction()
        if p!=i:A[p],A[i]=A[i],A[p];answer=-answer
        pivot=A[i][i];answer*=pivot
        for j in range(i+1,n):
            c=A[j][i]/pivot
            for h in range(i+1,n):A[j][h]-=c*A[i][h]
    return answer


def partitions(n,length,maximum=None):
    if length==0:
        if n==0:yield ()
        return
    for first in range(min(n,maximum if maximum is not None else n),-1,-1):
        for tail in partitions(n-first,length-1,first):
            yield (first,)+tail


def schur(shape,x):
    n=len(x);shape=shape+(0,)*(n-len(shape))
    numerator=determinant([[v**(shape[j]+n-1-j) for j in range(n)] for v in x])
    denominator=determinant([[v**(n-1-j) for j in range(n)] for v in x])
    result=numerator/denominator
    assert result.denominator==1
    return int(result)


def complete(weights,D):
    out=[1]+[0]*D
    for value in weights:
        for d in range(1,D+1):out[d]+=value*out[d-1]
    return out[D]


def main():
    congruences=characters=leading=0
    for t in range(2,11):
        for sample in range(3):
            r=t//2;z=[Fraction(2+i+sample) for i in range(r)]
            block=[[Fraction() for _ in range(t)] for _ in range(t)]
            for i,v in enumerate(z):
                block[2*i][2*i+1]=v;block[2*i+1][2*i]=-v
            u=identity(t)
            for i in range(t):
                for j in range(i+1,t):u[i][j]=Fraction(((i+2)*(j+3)+sample)%7-3)
            A=multiply(multiply(transpose(u),block),u)
            for i in range(1,r+1):
                assert pfaffian([row[:2*i] for row in A[:2*i]])==prod(z[:i])
                leading+=1
            current=A
            accumulated=identity(t)
            for start in range(0,2*r,2):
                pivot=current[start][start+1]
                v=identity(t)
                # -J^{-1}B for J=[[0,pivot],[-pivot,0]].
                for j in range(start+2,t):
                    v[start][j]=current[start+1][j]/pivot
                    v[start+1][j]=-current[start][j]/pivot
                current=multiply(multiply(transpose(v),current),v)
                accumulated=multiply(accumulated,v)
                assert all(not current[i][j] for i in (start,start+1)
                           for j in range(start+2,t))
            assert current==block
            assert multiply(multiply(transpose(accumulated),A),accumulated)==block
            congruences+=1
    for t in range(2,9):
        x=tuple(range(1,t+1))
        pair_weights=tuple(x[i]*x[j] for i in range(t) for j in range(i+1,t))
        for d in range(7):
            value=sum(schur(tuple(v for c in paired for v in (c,c)),x)
                      for paired in partitions(d,t//2))
            assert value==complete(pair_weights,d),(t,d,value)
            characters+=1
    receipt={
        "statement":"R048 independent Pfaffian map and paired-character audit",
        "status":"PASS",
        "methods":[
            "literal rational upper-unipotent congruence on generic-chart samples",
            "recursive Pfaffians versus exact leading block products",
            "Weyl alternants versus symmetric powers of literal exterior-pair weights"
        ],
        "complete_congruences":congruences,
        "leading_pfaffian_checks":leading,
        "paired_character_checks":characters,
        "source_imports":[],
        "finite_standard_module_sweep":"not repeated"
    }
    (HERE/"ONE_ROW_PFAFFIAN_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps(receipt,indent=2))


if __name__=="__main__":main()
