#!/usr/bin/env python3
"""The 17 ordinary-character cores used by CUE_GCT R-26/R-27; stdlib only.

Reconstruct every eight-column matrix from path matchings, check the
explicit 8x8 minors, and check both insertion operations on applicable cores.
"""
import argparse
import json
from functools import lru_cache

P = 101
CORES = [
    (10,6,14,[0,1,4,2,3,5,6,7],73),
    (9,6,14,[0,1,4,2,3,5,6,7],58),
    (8,6,14,[0,1,4,2,3,5,6,7],16),
    (7,6,14,[0,1,4,2,3,5,6,7],8),
    (6,6,14,[0,1,4,2,3,5,6,7],53),
    (6,7,14,[0,1,5,3,2,6,7,8],51),
    (6,8,14,[0,1,5,3,4,6,2,7],72),
    (6,9,14,[0,1,6,3,4,7,2,8],20),
    (6,10,14,[0,1,6,3,4,7,2,8],90),
    (2,15,34,[0,1,9,3,4,10,6,7],51),
    (15,2,34,[0,1,2,3,4,5,6,7],16),
    (3,14,61,[0,1,8,3,4,9,6,7],88),
    (14,3,61,[0,1,3,4,2,5,6,7],93),
    (4,13,88,[0,1,8,3,4,9,6,7],23),
    (13,4,88,[0,1,3,2,4,5,6,7],24),
    (5,12,82,[0,1,7,3,4,8,6,2],83),
    (12,5,82,[0,1,4,2,3,5,6,7],40)]


def determinant(matrix):
    a = [row[:] for row in matrix]
    out = 1
    for j in range(len(a)):
        i = next((i for i in range(j,len(a)) if a[i][j]),None)
        if i is None:
            return 0
        if i!=j:
            a[i],a[j] = a[j],a[i]
            out = -out % P
        out = out*a[j][j] % P
        inverse = pow(a[j][j],-1,P)
        for i in range(j+1,len(a)):
            factor = a[i][j]*inverse % P
            a[i] = [(x-factor*y) % P for x,y in zip(a[i],a[j])]
    return out


def pair_matrix(r,j,delta,K):
    L = r+j-1

    @lru_cache(None)
    def interval(a,b):
        # Explicit matching enumeration: choose nonadjacent path edges.
        out = [0]*((b-a+1)//2+1)
        def walk(v,k,weight):
            if v>b:
                out[k] = (out[k]+weight) % P
                return
            walk(v+1,k,weight)
            if v<b:
                walk(v+2,k+1,weight*delta[v] % P)
        walk(a,0,1)
        return out

    def poly(a,b,h=0,scale=1):
        return [0]*h+[scale*x % P for x in interval(a,b)]

    positive = [poly(r+1,L),poly(r,L),poly(r+2,L,1),poly(0,j-1),
                poly(0,j),poly(0,j-2,1),poly(r+1,L-1,1,2),poly(1,j-1,0,2)]
    negative = [poly(0,r-1),poly(0,r-2,1,delta[r-1]),
                poly(0,r,0,pow(delta[r],-1,P)),poly(j+1,L,0,K),
                poly(j+2,L,1,K*delta[j]),poly(j,L,0,K*pow(delta[j-1],-1,P)),
                poly(1,r-1,0,2),poly(j+1,L-1,1,2*K)]
    sizes = [(j+1)//2+1,(r+1)//2+1]
    return ([[column[k] if k<len(column) else 0 for column in positive] for k in range(sizes[0])]
            + [[column[k] if k<len(column) else 0 for column in negative] for k in range(sizes[1])])


def product(values):
    out = 1
    for value in values:
        out = out*value % P
    return out


def insert(delta,edge):
    assert delta[edge]==0
    return delta[:edge]+[0,0]+delta[edge+1:]


def same_coefficients(old,new,r,j,rnew,jnew):
    oldsplit,newsplit = (j+1)//2+1,(jnew+1)//2+1
    expected = (old[:oldsplit]+[[0]*8]*(newsplit-oldsplit)
                +old[oldsplit:]+[[0]*8]*(((rnew+1)//2)-((r+1)//2)))
    assert expected==new


def check():
    results = []
    for r,j,K,rows,expected in CORES:
        m = r+j
        delta = [(7*i*i+13*i+36) % P or 1 for i in range(m-1)]
        if min(r,j)>=6:
            delta[2]=delta[m-4]=0
            if abs(r-j)==4:
                delta[min(r,j)+1]=0
        else:
            delta[min(r,j)+1]=0
            ratio = product(delta[:min(r,j)])*pow(product(delta[max(r,j):]),-1,P) % P
            assert ratio==K
        matrix = pair_matrix(r,j,delta,K)
        det = determinant([matrix[i] for i in rows])
        assert det==expected,(r,j,det)
        tests = []
        if min(r,j)>=6:
            changed = insert(insert(delta,m-4),2)
            new = pair_matrix(r+1,j+1,changed,K)
            same_coefficients(matrix,new,r,j,r+1,j+1)
            tests.append('paired')
        if abs(r-j)>=4:
            changed = insert(delta,min(r,j)+1)
            rn,jn = (r+1,j) if r>j else (r,j+1)
            new = pair_matrix(rn,jn,changed,K)
            same_coefficients(matrix,new,r,j,rn,jn)
            tests.append('central')
        results.append(dict(r=r,j=j,K=K,determinant=det,insertions_checked=tests))
    return dict(prime=P,cores=results,all_passed=True,
                scope='finite cores and one step of each applicable insertion; full coverage follows from the proved insertion rules')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output')
    args = parser.parse_args()
    result = check()
    print(json.dumps(result,indent=2))
    if args.output:
        with open(args.output,'w') as stream:
            json.dump(result,stream,indent=2)
            stream.write('\n')


if __name__=='__main__':
    main()
