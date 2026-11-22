#!/usr/bin/env python3
"""Small explicit highest-weight evaluation certificates for LMR's (19,7,2^5).
Only Python stdlib and SymPy (for rational nullspaces) are used.

For a symmetric cubic tensor T on C^7, S_b=(T[b,i,j]), b=0,1,
and A=(T[0,0,i],T[0,1,i],T[1,1,i]).  For r=0,1,2, p=7-r,
I,J r-subsets of {0,1,2}, define
 J_(I,J,k) = [t^k] det([[S_0+t S_1,A_I],[A_J^t,0]]) / binom(p,k).
Multiply this by monomials of degree 5-r in f_i=T[0^(3-i),1^i].
The exact rational kernel of the binary raising derivation at y-weight 5
consists of highest-weight polynomials of GL_7-weight (19,7,2,2,2,2,2).
This script evaluates that explicitly specified kernel on deterministic
integer pencils of determinant/permanent cubics and on general tensors.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, permutations
from math import comb, gcd, lcm
from pathlib import Path
import argparse, json, time
import sympy as sp


def exponents(total, length):
    if length == 1:
        yield (total,)
    else:
        for k in range(total+1):
            for rest in exponents(total-k, length-1):
                yield (k,)+rest


def monomials(r, weight):
    p=7-r
    subsets=list(combinations(range(3),r))
    out=[]
    for a in exponents(5-r,4):
        af=sum(i*x for i,x in enumerate(a))
        for I,J in combinations_with_replacement(subsets,2):
            k=weight-af-sum(I)-sum(J)
            if 0<=k<=p:
                out.append((a,I,J,k))
    return out


def raise_set(I):
    for at,v in enumerate(I):
        if not v or v-1 in I: continue
        new=list(I); new[at]-=1
        # Lowering by one cannot cross another distinct integer label.
        yield tuple(new),v


def raise_term(term):
    a,I,J,k=term
    for i in range(1,4):
        if a[i]:
            b=list(a); b[i]-=1; b[i-1]+=1
            yield (tuple(b),I,J,k),i*a[i]
    if k: yield (a,I,J,k-1),k
    for B,c in raise_set(I):
        C,D=sorted((B,J)); yield (a,C,D,k),c
    for B,c in raise_set(J):
        C,D=sorted((I,B)); yield (a,C,D,k),c


def highest_weight_basis():
    terms=[]; polys=[]; details=[]
    for r in range(3):
        source=monomials(r,5); target=monomials(r,4)
        target_index={t:i for i,t in enumerate(target)}
        matrix=sp.zeros(len(target),len(source))
        for j,t in enumerate(source):
            for u,c in raise_term(t): matrix[target_index[u],j]+=c
        null=matrix.nullspace()
        offset=len(terms); terms += [(r,)+t for t in source]
        for v in null:
            multiple=lcm(*(int(q.q) for q in v))
            values=[int(multiple*q) for q in v]
            common=gcd(*values)
            values=[x//common for x in values]
            if next(x for x in values if x)<0: values=[-x for x in values]
            polys.append({offset+i:c for i,c in enumerate(values) if c})
        details.append(dict(r=r,source=len(source),target=len(target),kernel=len(null)))
    return terms,polys,details


def determinant(a,prime):
    a=[list(row) for row in a]; value=1; n=len(a)
    for j in range(n):
        k=next((k for k in range(j,n) if a[k][j]%prime),None)
        if k is None: return 0
        if k!=j: a[j],a[k]=a[k],a[j]; value=-value
        pivot=a[j][j]%prime; value=value*pivot%prime; inv=pow(pivot,-1,prime)
        for k in range(j+1,n):
            c=a[k][j]*inv%prime
            for h in range(j+1,n): a[k][h]=(a[k][h]-c*a[j][h])%prime
    return value%prime


@lru_cache(None)
def inverse_vandermonde(degree,prime):
    n=degree+1
    a=[[pow(i,j,prime) for j in range(n)]+[int(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if a[k][j]); a[j],a[k]=a[k],a[j]
        inv=pow(a[j][j],-1,prime); a[j]=[x*inv%prime for x in a[j]]
        for k in range(n):
            if k!=j:
                c=a[k][j]; a[k]=[(x-c*y)%prime for x,y in zip(a[k],a[j])]
    return [row[n:] for row in a]


def tensor_values(T,terms,polys,prime):
    def entry(*indices): return T[tuple(sorted(indices))]
    f=[entry(*([0]*(3-i)+[1]*i)) for i in range(4)]
    S=[[[entry(b,i,j) for j in range(7)] for i in range(7)] for b in range(2)]
    A=[[entry(*([0]*(2-c)+[1]*c),i) for c in range(3)] for i in range(7)]
    needed={(r,I,J) for r,a,I,J,k in terms}; J_values={}
    for r,I,J in sorted(needed):
        p=7-r; evaluations=[]
        for t in range(p+1):
            M=[[(S[0][i][j]+t*S[1][i][j])%prime for j in range(7)]+[A[i][c] for c in I] for i in range(7)]
            M += [[A[j][c] for j in range(7)]+[0]*r for c in J]
            evaluations.append(determinant(M,prime))
        coeff=[sum(x*y for x,y in zip(row,evaluations))%prime for row in inverse_vandermonde(p,prime)]
        for k,c in enumerate(coeff): J_values[r,I,J,k]=c*pow(comb(p,k),-1,prime)%prime
    values=[]
    for r,a,I,J,k in terms:
        v=J_values[r,I,J,k]
        for i,power in enumerate(a): v=v*pow(f[i],power,prime)%prime
        values.append(v)
    return [sum(c*values[i] for i,c in poly.items())%prime for poly in polys]


def generator(seed):
    state=seed
    while True:
        state=(1664525*state+1013904223)%2**32
        yield (state>>16)%101


def tensor_from_pencil(matrices,permanent,prime):
    def cubic(M):
        return sum((1 if permanent or sum(a>b for i,a in enumerate(s) for b in s[i+1:])%2==0 else -1)*M[0][s[0]]*M[1][s[1]]*M[2][s[2]] for s in permutations(range(3)))%prime
    T={}
    for abc in combinations_with_replacement(range(7),3):
        total=0
        for xyz in permutations(abc):
            M=[[matrices[xyz[j]][3*i+j] for j in range(3)] for i in range(3)]
            total+=cubic(M)
        T[abc]=total*pow(6,-1,prime)%prime
    return T


def sample_tensor(kind,seed,prime):
    g=generator(seed)
    if kind=='generic': return {abc:next(g) for abc in combinations_with_replacement(range(7),3)}
    matrices=[[next(g) for _ in range(9)] for _ in range(7)]
    return tensor_from_pencil(matrices,kind=='per',prime)


def row_reduce(a,prime):
    a=[list(row) for row in a]; order=list(range(len(a))); rank=0; pivots=[]
    for j in range(len(a[0])):
        k=next((k for k in range(rank,len(a)) if a[k][j]),None)
        if k is None: continue
        a[rank],a[k]=a[k],a[rank]; order[rank],order[k]=order[k],order[rank]
        inv=pow(a[rank][j],-1,prime); a[rank]=[x*inv%prime for x in a[rank]]
        for i in range(rank+1,len(a)):
            c=a[i][j]; a[i]=[(x-c*y)%prime for x,y in zip(a[i],a[rank])]
        pivots.append(j); rank+=1
        if rank==len(a): break
    return rank,order[:rank],pivots


def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--output'); ap.add_argument('--prime',type=int,default=1000003)
    args=ap.parse_args(); start=time.monotonic(); prime=args.prime
    terms,polys,details=highest_weight_basis()
    print(json.dumps({'formal_basis':details,'total_polynomials':len(polys)}),flush=True)
    results={}
    for kind in ('generic','det','per'):
        seeds=list(range(20261122,20261134))
        values=[tensor_values(sample_tensor(kind,s,prime),terms,polys,prime) for s in seeds]
        rank,rows,columns=row_reduce(values,prime)
        minor=[[values[i][j] for j in columns] for i in rows]
        results[kind]=dict(rank=rank,seeds=seeds,values=values,minor_rows=rows,minor_columns=columns,minor_determinant=determinant(minor,prime))
        print(json.dumps({'kind':kind,'rank':rank,'minor_rows':rows,'minor_columns':columns,'minor_determinant':results[kind]['minor_determinant']}),flush=True)
    out=dict(prime=prime,details=details,terms=terms,polynomials=polys,results=results,elapsed_seconds=time.monotonic()-start)
    if args.output: Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    assert results['generic']['rank']==6
    assert results['det']['rank']==5
    assert results['per']['rank']==6
    print(json.dumps({'status':'PASS','elapsed_seconds':out['elapsed_seconds']}),flush=True)

if __name__=='__main__': main()
