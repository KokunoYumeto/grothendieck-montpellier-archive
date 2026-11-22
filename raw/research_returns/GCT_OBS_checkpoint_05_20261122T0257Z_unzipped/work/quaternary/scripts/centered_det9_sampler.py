#!/usr/bin/env python3
"""Exact centered symmetric tensors from genuine four-variable determinants.

Only the Python standard library is used.  The dense sampler takes
F=x0^9 det(I9+(x1/x0) A1+(x2/x0) A2+(x3/x0) A3), with each Ai traceless.
Coefficients are reconstructed by exact total-degree Newton interpolation,
not by a rank test.  The block sampler uses three such 3x3 pencils.

Public API:
    sampler = CenteredDeterminantSampler(seed=20261122, prime=101)
    tensors, certificate = sampler.sample(kind='dense', sanity_points=3)
    tensors[j][(a,b,c)] = [x1^a x2^b x3^c] F(1,x1,x2,x3)
                          * (9-j)! a! b! c! / 9!,  j=a+b+c in 2,...,8.

All divisions take place modulo prime.  These are entries of the normalized
symmetric tensor associated with a nonic.  The source matrices and direct
determinant sanity values are retained in the certificate.
"""
import argparse
from functools import lru_cache
from itertools import permutations, product
from math import comb, factorial
import json
import time


def exponents(degree):
    return [(a,b,degree-a-b) for a in range(degree,-1,-1)
            for b in range(degree-a,-1,-1)]


def determinant(matrix, prime):
    """Ordinary pivoted Gaussian determinant, valid also at singular points."""
    a=[row[:] for row in matrix]
    value=1
    for k in range(len(a)):
        pivot=next((i for i in range(k,len(a)) if a[i][k] % prime),None)
        if pivot is None:return 0
        if pivot!=k:
            a[k],a[pivot]=a[pivot],a[k]
            value=-value
        d=a[k][k] % prime
        value=value*d % prime
        inverse=pow(d,prime-2,prime)
        for i in range(k+1,len(a)):
            c=a[i][k]*inverse % prime
            if c:
                for j in range(k+1,len(a)):
                    a[i][j]=(a[i][j]-c*a[k][j]) % prime
    return value % prime


def pencil_at(matrices, point, prime):
    n=len(matrices[0])
    return [[((i==j)+sum(point[k]*matrices[k][i][j] for k in range(3))) % prime
             for j in range(n)] for i in range(n)]


@lru_cache(None)
def interpolation_data(degree, prime):
    """Forward differences and the monomial expansions of binomial(x,alpha)."""
    assert prime > degree
    nodes=[alpha for j in range(degree+1) for alpha in exponents(j)]
    index={alpha:i for i,alpha in enumerate(nodes)}
    falling=[[1]]
    binomial=[[1]]
    for k in range(1,degree+1):
        previous=falling[-1]
        current=[0]*(k+1)
        for j,v in enumerate(previous):
            current[j]=(current[j]-(k-1)*v) % prime
            current[j+1]=(current[j+1]+v) % prime
        falling.append(current)
        inv=pow(factorial(k) % prime,prime-2,prime)
        binomial.append([v*inv % prime for v in current])
    differences=[]
    expansions=[]
    for alpha in nodes:
        stencil=[]
        expansion=[]
        for beta in product(*(range(a+1) for a in alpha)):
            signed=((-1)**(sum(alpha)-sum(beta)))
            for a,b in zip(alpha,beta):signed*=comb(a,b)
            stencil.append((index[beta],signed % prime))
            v=1
            for a,b in zip(alpha,beta):v=v*binomial[a][b] % prime
            if v:expansion.append((index[beta],v))
        differences.append(stencil)
        expansions.append(expansion)
    return nodes,differences,expansions


def dense_coefficients(matrices, prime):
    """All coefficients of a size-n determinant in three affine variables."""
    nodes,stencils,expansions=interpolation_data(len(matrices[0]),prime)
    values=[determinant(pencil_at(matrices,a,prime),prime) for a in nodes]
    newton=[sum(v*values[i] for i,v in row) % prime for row in stencils]
    coefficients=[0]*len(nodes)
    for c,row in zip(newton,expansions):
        if c:
            for i,v in row:coefficients[i]=(coefficients[i]+c*v) % prime
    return dict(zip(nodes,coefficients))


def polynomial_product(a,b,prime):
    out={}
    for alpha,c in a.items():
        if not c:continue
        for beta,d in b.items():
            if not d:continue
            gamma=tuple(x+y for x,y in zip(alpha,beta))
            out[gamma]=(out.get(gamma,0)+c*d) % prime
    return {a:c for a,c in out.items() if c}


def cubic_coefficients(matrices, prime):
    """Independent six-term Leibniz expansion for a 3x3 linear pencil."""
    units=[(1,0,0),(0,1,0),(0,0,1)]
    out={}
    for pi in permutations(range(3)):
        sign=(-1)**sum(pi[i]>pi[j] for i in range(3) for j in range(i+1,3))
        term={(0,0,0):sign}
        for i,j in enumerate(pi):
            entry={units[k]:matrices[k][i][j] for k in range(3)}
            if i==j:entry[(0,0,0)]=1
            term=polynomial_product(term,entry,prime)
        for a,c in term.items():out[a]=(out.get(a,0)+c) % prime
    return {a:c for a,c in out.items() if c}


def polynomial_at(coefficients, point, prime):
    powers=[[pow(x,j,prime) for j in range(10)] for x in point]
    return sum(c*powers[0][a]*powers[1][b]*powers[2][d]
               for (a,b,d),c in coefficients.items()) % prime


def tensor_normalization(coefficients, prime, max_jet=8):
    assert 2<=max_jet<=9
    inverse=pow(factorial(9) % prime,prime-2,prime)
    return {j:{a:coefficients.get(a,0)*factorial(9-j)*
                  factorial(a[0])*factorial(a[1])*factorial(a[2])*inverse % prime
               for a in exponents(j)} for j in range(2,max_jet+1)}


class Generator:
    """Explicit 32-bit LCG; reproducible independently of random-library versions."""
    def __init__(self,seed,prime):self.state=seed & 0xffffffff;self.prime=prime
    def next(self):
        self.state=(1664525*self.state+1013904223) & 0xffffffff
        return (self.state >> 16) % self.prime
    def traceless(self,n):
        a=[[self.next() for j in range(n)] for i in range(n)]
        # Keep this entry as a negative integer: the displayed source pencil
        # then has trace exactly zero over Z, not only modulo prime.
        a[-1][-1]=-sum(a[i][i] for i in range(n-1))
        return a


class CenteredDeterminantSampler:
    def __init__(self,seed=20261122,prime=101):
        assert prime>9 and all(prime%d for d in range(2,int(prime**0.5)+1))
        self.prime=prime;self.seed=seed;self.generator=Generator(seed,prime)
        self.index=0

    def sample(self,kind='dense',sanity_points=3,max_jet=8):
        prime=self.prime
        state_before=self.generator.state
        if kind=='dense':
            matrices=[self.generator.traceless(9) for _ in range(3)]
            coefficients=dense_coefficients(matrices,prime)
        elif kind=='block':
            blocks=[[self.generator.traceless(3) for _ in range(3)] for _ in range(3)]
            matrices=[[[0]*9 for _ in range(9)] for _ in range(3)]
            coefficients={(0,0,0):1}
            for block_index,block in enumerate(blocks):
                for k in range(3):
                    for i in range(3):
                        for j in range(3):
                            matrices[k][3*block_index+i][3*block_index+j]=block[k][i][j]
                coefficients=polynomial_product(coefficients,cubic_coefficients(block,prime),prime)
        else:raise ValueError('kind must be dense or block')
        assert coefficients[(0,0,0)]==1
        assert all(coefficients.get(a,0)==0 for a in exponents(1))
        assert all(sum(m[i][i] for i in range(9))==0 for m in matrices)
        tensors=tensor_normalization(coefficients,prime,max_jet)
        # Sanity probes use a separate generator, so enabling them never changes
        # the sequence of sample pencils.
        probes=Generator(state_before ^ 0x9e3779b9,prime)
        sanity=[]
        for _ in range(sanity_points):
            point=tuple(probes.next() for _ in range(3))
            direct=determinant(pencil_at(matrices,point,prime),prime)
            reconstructed=polynomial_at(coefficients,point,prime)
            assert direct==reconstructed
            sanity.append(dict(point=point,determinant=direct,reconstructed=reconstructed))
        certificate=dict(prime=prime,kind=kind,seed=self.seed,index=self.index,
                         generator_state_before=state_before,
                         generator_state_after=self.generator.state,
                         matrices=matrices,sanity=sanity,
                         coefficients=[[list(a),coefficients.get(a,0)]
                                       for j in range(10) for a in exponents(j)],
                         normalized_tensors={str(j):[[list(a),c] for a,c in values.items()]
                                             for j,values in tensors.items()})
        self.index+=1
        return tensors,certificate


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed',type=int,default=20261122)
    parser.add_argument('--prime',type=int,default=101)
    parser.add_argument('--kind',choices=('dense','block'),default='dense')
    parser.add_argument('--samples',type=int,default=4)
    parser.add_argument('--sanity-points',type=int,default=3)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    started=time.monotonic()
    sampler=CenteredDeterminantSampler(args.seed,args.prime)
    records=[]
    for _ in range(args.samples):
        tensors,certificate=sampler.sample(args.kind,args.sanity_points)
        records.append(certificate)
    result=dict(prime=args.prime,seed=args.seed,kind=args.kind,samples=records,
                seconds=round(time.monotonic()-started,3))
    with open(args.output,'w') as f:json.dump(result,f,indent=2);f.write('\n')
    summary={k:v for k,v in result.items() if k!='samples'}
    summary.update(samples=len(records),tensor_coordinates=sum(map(len,tensors.values())))
    print(json.dumps(summary))


if __name__=='__main__':main()
