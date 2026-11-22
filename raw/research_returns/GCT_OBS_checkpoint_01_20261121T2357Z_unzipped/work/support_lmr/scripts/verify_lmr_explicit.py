#!/usr/bin/env python3
"""Explicit degree-12 HW functions at lambda=(19,7,2,2,2,2,2).
Python standard library only; no input files. Run with --output result.json.

For a symmetric trilinear cubic T on C^7 let f_i=T(0^(3-i),1^i),
S_b=(T(b,i,j)), A=(T(0,0,i)). Define h_k=[t^k]det(S_0+tS_1)/binom(7,k),
b_k=[t^k]det([[S_0+tS_1,A],[A^t,0]])/binom(6,k).
Each term below is (coefficient, exponents of f_0,...,f_3, kind, k),
where kind=0 means h_k and kind=1 means b_k. The six polynomials are
P0,...,P4,R. Formal raising identities and the Hessian-divisibility
identity are verified exactly over Q, followed by modular evaluation
certificates proving det multiplicity>=5 and per multiplicity>=6.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement, permutations
from math import comb
from pathlib import Path
import argparse, json, time

POLYS = [
    [(2, (0, 5, 0, 0), 0, 0), (-5, (1, 3, 1, 0), 0, 0), (3, (2, 1, 2, 0), 0, 0), (1, (2, 2, 0, 1), 0, 0), (-1, (3, 0, 1, 1), 0, 0)],
    [(1, (0, 5, 0, 0), 0, 0), (-2, (1, 3, 1, 0), 0, 0), (-1, (1, 4, 0, 0), 0, 1), (1, (2, 1, 2, 0), 0, 0), (2, (2, 2, 1, 0), 0, 1), (-1, (3, 0, 2, 0), 0, 1)],
    [(2, (0, 5, 0, 0), 0, 0), (-3, (1, 3, 1, 0), 0, 0), (-4, (1, 4, 0, 0), 0, 1), (1, (2, 2, 0, 1), 0, 0), (6, (2, 2, 1, 0), 0, 1), (2, (2, 3, 0, 0), 0, 2), (-2, (3, 1, 0, 1), 0, 1), (-3, (3, 1, 1, 0), 0, 2), (1, (4, 0, 0, 1), 0, 2)],
    [(1, (0, 5, 0, 0), 0, 0), (-1, (1, 3, 1, 0), 0, 0), (-3, (1, 4, 0, 0), 0, 1), (3, (2, 2, 1, 0), 0, 1), (3, (2, 3, 0, 0), 0, 2), (-3, (3, 1, 1, 0), 0, 2), (-1, (3, 2, 0, 0), 0, 3), (1, (4, 0, 1, 0), 0, 3)],
    [(1, (0, 5, 0, 0), 0, 0), (-5, (1, 4, 0, 0), 0, 1), (10, (2, 3, 0, 0), 0, 2), (-10, (3, 2, 0, 0), 0, 3), (5, (4, 1, 0, 0), 0, 4), (-1, (5, 0, 0, 0), 0, 5)],
    [(5, (0, 3, 1, 0), 1, 0), (-10, (0, 4, 0, 0), 1, 1), (-3, (1, 1, 2, 0), 1, 0), (-1, (1, 2, 0, 1), 1, 0), (20, (1, 3, 0, 0), 1, 2), (1, (2, 0, 1, 1), 1, 0), (-20, (2, 2, 0, 0), 1, 3), (10, (3, 1, 0, 0), 1, 4), (-2, (4, 0, 0, 0), 1, 5)],
]
RELATION = (2,21,7,35,7,0)


def formal_checks():
    for poly in POLYS:
        derivative=defaultdict(int)
        for c,a,kind,k in poly:
            assert sum(a)==5-kind and sum(i*a[i] for i in range(4))+k==5
            for i in range(1,4):
                if a[i]:
                    b=list(a);b[i]-=1;b[i-1]+=1
                    derivative[tuple(b),kind,k]+=c*i*a[i]
            if k:derivative[a,kind,k-1]+=c*k
        assert all(v==0 for v in derivative.values())
    # If H(X,Y)=F(X,Y)*Q(X,Y), normalized coefficients obey the following.
    remainder=defaultdict(Fraction)
    for scalar,poly in zip(RELATION,POLYS):
        for c,a,kind,k in poly:
            if not scalar:continue
            assert kind==0
            for i in range(4):
                j=k-i
                if 0<=j<=4:
                    b=list(a);b[i]+=1
                    remainder[tuple(b),j]+=Fraction(scalar*c*comb(3,i)*comb(4,j),comb(7,k))
    assert all(v==0 for v in remainder.values())
    return dict(raising_identities=6,divisibility_identity=True)


def det(a,p):
    a=[list(row) for row in a];value=1;n=len(a)
    for j in range(n):
        k=next((k for k in range(j,n) if a[k][j]%p),None)
        if k is None:return 0
        if k!=j:a[j],a[k]=a[k],a[j];value=-value
        pivot=a[j][j]%p;value=value*pivot%p;inv=pow(pivot,-1,p)
        for k in range(j+1,n):
            c=a[k][j]*inv%p
            for h in range(j+1,n):a[k][h]=(a[k][h]-c*a[j][h])%p
    return value%p


@lru_cache(None)
def interpolation_inverse(degree,p):
    n=degree+1
    a=[[pow(i,j,p) for j in range(n)]+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j]);a[j],a[k]=a[k],a[j]
        inv=pow(a[j][j],-1,p);a[j]=[x*inv%p for x in a[j]]
        for k in range(n):
            if k!=j:
                c=a[k][j];a[k]=[(x-c*y)%p for x,y in zip(a[k],a[j])]
    return [row[n:] for row in a]


def evaluate(T,p):
    def entry(*indices):return T[tuple(sorted(indices))]
    f=[entry(*([0]*(3-i)+[1]*i)) for i in range(4)]
    S=[[[entry(b,i,j) for j in range(7)] for i in range(7)] for b in range(2)]
    A=[entry(0,0,i) for i in range(7)];covariants=[]
    for kind in (0,1):
        degree=7-kind;values=[]
        for t in range(degree+1):
            matrix=[[(S[0][i][j]+t*S[1][i][j])%p for j in range(7)] for i in range(7)]
            if kind:
                matrix=[row+[A[i]] for i,row in enumerate(matrix)]+[A+[0]]
            values.append(det(matrix,p))
        covariants.append([sum(x*y for x,y in zip(row,values))*pow(comb(degree,k),-1,p)%p
            for k,row in enumerate(interpolation_inverse(degree,p))])
    out=[]
    for poly in POLYS:
        v=0
        for c,a,kind,k in poly:
            term=c*covariants[kind][k]
            for i,power in enumerate(a):term=term*pow(f[i],power,p)%p
            v+=term
        out.append(v%p)
    return out


def lcg(seed):
    state=seed
    while True:
        state=(1664525*state+1013904223)%2**32
        yield (state>>16)%101


def sample(kind,seed,p):
    g=lcg(seed)
    triples=list(combinations_with_replacement(range(7),3))
    if kind=='generic':return {abc:next(g) for abc in triples}
    matrices=[[next(g) for _ in range(9)] for _ in range(7)]
    def cubic(M):
        total=0
        for s in permutations(range(3)):
            inv=sum(a>b for i,a in enumerate(s) for b in s[i+1:])
            sign=1 if kind=='per' else (-1)**inv
            total+=sign*M[0][s[0]]*M[1][s[1]]*M[2][s[2]]
        return total%p
    T={}
    for abc in triples:
        total=0
        for xyz in permutations(abc):
            M=[[matrices[xyz[j]][3*i+j] for j in range(3)] for i in range(3)]
            total+=cubic(M)
        T[abc]=total*pow(6,-1,p)%p
    return T


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output')
    args=ap.parse_args();start=time.monotonic();p=1000003
    exact=formal_checks();seeds=list(range(20261122,20261128));out={}
    for kind in ('generic','det','per'):
        values=[evaluate(sample(kind,s,p),p) for s in seeds]
        columns=[0,1,2,3,5] if kind=='det' else list(range(6))
        rows=list(range(len(columns)))
        minor=det([[values[i][j] for j in columns] for i in rows],p)
        psi=[sum(c*v for c,v in zip(RELATION,row))%p for row in values]
        assert minor
        if kind=='det':assert not any(psi)
        else:assert psi[0]
        out[kind]=dict(values=values,minor_rows=rows,minor_columns=columns,minor_determinant=minor,psi_values=psi)
    assert out['det']['minor_determinant']==170120
    assert out['per']['minor_determinant']==851602
    result=dict(status='PASS',prime=p,seeds=seeds,exact_checks=exact,evaluations=out,
                relation=RELATION,elapsed_seconds=time.monotonic()-start)
    if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
