#!/usr/bin/env python3
"""Exact census of the 72 indicated rank-one Artin-Schreier models over F4.

This enumerates models, not geometric or arithmetic isomorphism classes.
It counts F4/F16 points to recover their F4 Weil polynomials and checks
possible factorizations into elliptic Weil quadratics by integer arithmetic.
"""
import json
from pathlib import Path

def mul(a,b,n,mod):
    c=0
    while b:
        if b&1:c^=a
        b>>=1
        a<<=1
        if a&(1<<n):a^=mod
    return c

def power(a,k,n,mod):
    z=1
    while k:
        if k&1:z=mul(z,a,n,mod)
        a=mul(a,a,n,mod)
        k>>=1
    return z

def trace(a,n,mod):
    ans=0
    for _ in range(n):
        ans^=a
        a=mul(a,a,n,mod)
    assert ans in (0,1)
    return ans

def count(a,b,c,d,n,mod):
    total=2 # The unique points over the order-one and order-three poles.
    for x in range(1,1<<n):
        f=mul(a,power(x,3,n,mod),n,mod)^mul(b,x,n,mod)^mul(c,power(x,(1<<n)-2,n,mod),n,mod)^d
        total+=2*(trace(f,n,mod)==0)
    return total

def main():
    # u in F4 has u^2+u+1=0; F16 uses z^4+z+1=0 and u=z^2+z.
    embedding=[0,1,6,7]
    for x in range(4):
        for y in range(4):
            assert embedding[mul(x,y,2,0b111)]==mul(embedding[x],embedding[y],4,0b10011)
    rows=[]
    for a in (1,2,3):
        for b in range(4):
            for c in (1,2,3):
                for d in (0,2): # Absolute trace zero / one representatives.
                    N4=count(a,b,c,d,2,0b111)
                    N16=count(*(embedding[v] for v in (a,b,c,d)),4,0b10011)
                    a1=N4-5
                    a2=(a1*a1-(17-N16))//2
                    assert 2*a2==a1*a1-(17-N16)
                    factors=[]
                    for to in (-3,-1,1,3):
                        for ts in (-4,-2,0,2,4):
                            if -(to+ts)==a1 and to*ts+8==a2:
                                factors.append(dict(ordinary_trace=to,supersingular_trace=ts,
                                                    quadratic_factors=[[1,-to,4],[1,-ts,4]]))
                    rows.append(dict(a=a,b=b,c=c,d=d,N4=N4,N16=N16,
                                     weil_polynomial=[1,a1,a2,4*a1,16],elliptic_factors=factors))
    assert len(rows)==72
    split=[r for r in rows if r['elliptic_factors']]
    result={'scope':'72 displayed models, not an isomorphism classification; exact two-field counts and algebraic polynomial factorization.',
            'F4_modulus_bits':0b111,'F16_modulus_bits':0b10011,'embedding_F4_into_F16':embedding,
            'models':len(rows),'distinct_weil_polynomials':len({tuple(r['weil_polynomial']) for r in rows}),
            'split_models':len(split),'split_rows':split,'all_rows':rows}
    path=Path(__file__).with_name('RANK_ONE_F4_SPLIT_SEARCH.json')
    path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('all_rows',)},indent=2))

if __name__=='__main__':main()
