"""Exploratory GF(2) finite-module divided-power disk calculations.

Coefficient ring: F2[X,Y]/(X^2,Y^2). A coefficient is a bitset on
1,X,Y,XY. Results are finite calculations, not a proof of an infinite
statement. PD and exterior relation generators are imposed explicitly.
"""
from itertools import combinations, product
from math import comb


def mulc(a,b):
    out=0
    for i in range(4):
        if (a>>i)&1:
            for j in range(4):
                if (b>>j)&1 and not (i&j):
                    out ^= 1<<(i|j)
    return out


def powc(a,n):
    out=1
    for _ in range(n): out=mulc(out,a)
    return out


def compositions(n,r):
    if r==1:
        yield (n,)
    else:
        for j in range(n+1):
            for tail in compositions(n-j,r-1): yield (j,)+tail


def basis(r,n,q):
    if q<0 or q>r or q>n: return []
    return [(a,sum(1<<j for j in js))
            for a in compositions(n-q,r)
            for js in combinations(range(r),q)]


def multiply(a,j,b,k):
    if j&k or any(x&y for x,y in zip(a,b)): return None
    return (tuple(x+y for x,y in zip(a,b)),j|k)


def rank(vectors):
    piv={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in piv: v ^= piv[p]
            else:
                piv[p]=v
                break
    return len(piv)


def run(relations,n):
    r=len(relations[0])
    bs={q:basis(r,n,q) for q in range(r+2)}
    ix={q:{v:i for i,v in enumerate(bs[q])} for q in bs}
    ideals={q:[] for q in bs}
    zero=(0,)*r
    # Each ideal generator is a list of coefficient/exponent/exterior terms.
    gens=[]
    for rel in relations:
        for k in range(1,n+1):
            terms=[]
            for a in compositions(k,r):
                c=1
                for co,pow_ in zip(rel,a): c=mulc(c,powc(co,pow_))
                if c: terms.append((c,a,0))
            if terms: gens.append((k,0,terms))
        gens.append((1,1,[(c,zero,1<<i) for i,c in enumerate(rel) if c]))
    for ar,form,terms in gens:
        for q in range(form,r+1):
            for b,k in basis(r,n-ar,q-form):
                for cm in range(4):
                    v=0
                    for c,a,j in terms:
                        prod=multiply(a,j,b,k)
                        if prod is None: continue
                        co=mulc(c,1<<cm)
                        bi=ix[q][prod]
                        v ^= co<<(4*bi)
                    if v: ideals[q].append(v)
    ds={q:[] for q in bs}
    for q in range(r+1):
        for a,j in bs[q]:
            for cm in range(4):
                out=0
                for z,ex in enumerate(a):
                    if ex and not ((j>>z)&1):
                        b=list(a); b[z]-=1
                        bi=ix[q+1][(tuple(b),j|(1<<z))]
                        out ^= 1<<(4*bi+cm)
                ds[q].append(out)
    ir={q:rank(ideals[q]) for q in bs}
    dr={q:rank(ideals[q+1]+ds[q])-ir[q+1] for q in range(r+1)}
    hs=[]
    for q in range(r+1):
        hs.append(4*len(bs[q])-ir[q]-dr[q]-(dr[q-1] if q else 0))
    assert min(hs)>=0
    return hs


if __name__=='__main__':
    examples={
        'ideal(X,Y)':[(2,0),(0,4),(4,2)],
        'kernel-like':[(2,0),(4,2)],
        'cyclic(X)':[(2,)],
    }
    for name,rels in examples.items():
        print(name)
        for n in range(1,11): print(n,run(rels,n))
