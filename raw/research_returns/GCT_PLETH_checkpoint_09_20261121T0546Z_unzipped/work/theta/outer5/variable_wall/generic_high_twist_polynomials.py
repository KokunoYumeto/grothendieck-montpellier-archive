"""Exact normalized k<=c<2k chamber and coefficientwise positivity test.

X,B,K,C>=0: x=X,b=K+B+1,k=K+C+1,c=K+2C+1.
Here K=2k-c-1 and C=c-k. The full three-row simplex is retained.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product,permutations
from fractions import Fraction
from math import factorial,lcm
import json
import sympy as sp
from sympy.functions.combinatorial.numbers import stirling
from chamber_polynomials import (
    a,b,k,h,pair_data,binary_h,binary_truncated,square_cycles,
    binomial_polynomial,CLASSES,SIZES,
)
from generic_twist_upper_polynomials import (
    c,X,B,K,C,COORDS,dictionary,serialized,difference_tuple,fixed_pair,
)

HERE=Path(__file__).resolve().parent
VARIABLES=sp.symbols('u0 u1 u2')
P3=tuple(permutations(range(3)))
SIGN={p:(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in P3}


@lru_cache(None)
def moment(powers,L,offset,kr):
    remainder=(kr-1-offset)%L
    bound=(k-1-offset-remainder)/L
    answer=0
    for reduced in product(*(range(d+1) for d in powers)):
        factor=1
        for d,j in zip(powers,reduced):factor*=factorial(j)*int(stirling(d,j,kind=2))
        if factor:answer+=factor*binomial_polynomial(bound+3,sum(reduced)+3)
    return sp.expand(answer)


@lru_cache(None)
def full_singleton(rest,ar,br,kr,cr):
    L=lcm(*rest);alpha=(a+c,b+c,c);res=(ar+cr,br+cr,cr)
    rows={}
    for i,j,s in product(range(3),range(3),range(L)):
        expr=h(rest,res[i]-i+j-s,alpha[i]-i+j-s-L*VARIABLES[i])
        rows[i,j,s]=tuple((power[0],coef) for power,coef in sp.Poly(sp.expand(expr),VARIABLES[i]).terms() if coef)
    answer=0
    for offsets in product(range(L),repeat=3):
        total=sum(offsets)
        for sigma in P3:
            options=[rows[i,sigma[i],offsets[i]] for i in range(3)]
            for choices in product(*options):
                powers=tuple(d for d,v in choices)
                coefficient=SIGN[sigma]*sp.prod(v for d,v in choices)
                answer+=coefficient*moment(powers,L,total,kr)
    return sp.expand(answer)


@lru_cache(None)
def class_polynomial(cycles,ar,br,kr,cr):
    alpha=(a+c,b+c,c);res=(ar+cr,br+cr,cr)
    matrix=[[h(cycles,res[i]-i+j,alpha[i]-i+j) for j in range(3)] for i in range(3)]
    answer=sum(SIGN[p]*sp.prod(matrix[i][p[i]] for i in range(3)) for p in P3)
    fixed=cycles.count(1)
    if fixed:
        rest=list(cycles);rest.remove(1);rest=tuple(rest);L=lcm(*rest)
        answer-=fixed*full_singleton(rest,ar%L,br%L,kr%L,cr%L)
    for swapped,rest in pair_data(cycles):
        determinant=(-1)**((3-len(rest))*(br+cr))
        exterior=determinant*binary_h(rest,a-b,ar-br)
        if swapped:
            if cr%2:continue
            normal=binary_truncated(square_cycles(rest),k-c/2,kr-cr//2)
            answer-=exterior*normal
        else:
            L=lcm(*rest);rp=(2*kr-cr)%L;r=2*k-c
            normal=fixed_pair(rest,(rp-1)%L,(rp-2)%L).subs(
                {k:r-1,c:r-2},simultaneous=True)
            answer+=exterior*normal
    return sp.expand(answer)


def main():
    data=[];degrees=[];separate=[]
    for cycles in CLASSES:
        L=lcm(*cycles);row={}
        for ar,br,kr,cr in product(range(L),repeat=4):
            expr=class_polynomial(cycles,ar,br,kr,cr)
            expr=expr.subs({a:K+B+1+X,b:K+B+1,k:K+C+1,c:K+2*C+1},simultaneous=True)
            row[(ar,br,kr,cr)]=dictionary(sp.expand(expr))
        degree=max((sum(p) for poly in row.values() for p in poly),default=0)
        sep=tuple(max((p[i] for poly in row.values() for p in poly),default=0) for i in range(4))
        data.append(row);degrees.append(degree);separate.append(sep)
        print('class',cycles,'phases',len(row),'degree',degree,'separate',sep,flush=True)
    identity=data[0][(0,0,0,0)]
    unique=[set(tuple(sorted(poly.items())) for poly in row.values()) for row in data]
    print('unique phases',list(map(len,unique)),flush=True)
    support=set(p for row in data for poly in row.values() for p in poly)
    orders=set(o for p in support for o in product(*(range(v+1) for v in p)))
    orders.discard((0,0,0,0));active=[];margins=[];failed=[]
    for order in sorted(orders):
        first=dict(difference_tuple(tuple(sorted(identity.items())),order));worst={}
        for size,polys in zip(SIZES[1:],unique[1:]):
            bound={}
            for poly in polys:
                for p,v in difference_tuple(poly,order):bound[p]=max(bound.get(p,0),abs(v))
            for p,v in bound.items():worst[p]=worst.get(p,0)+size*v
        if not first and not worst:continue
        active.append(order)
        margin={p:first.get(p,0)-worst.get(p,0) for p in first.keys()|worst.keys()}
        bad={p:v for p,v in margin.items() if v<0}
        if bad:failed.append({'order':order,'negative':serialized(bad)})
        margins.append({'order':order,'constant':str(margin.get((0,0,0,0),0)),
                        'minimum':str(min(margin.values())),
                        'margin':serialized(margin)})
    result={'parameters':'x=X,b=K+B+1,k=K+C+1,c=K+2C+1; X,B,K,C>=0',
            'degrees':degrees,'separate_degrees':separate,
            'negative_identity':serialized({p:v for p,v in identity.items() if v<0}),
            'active_orders':active,'margins':margins,'failed':failed,
            'phase_polynomials':[{','.join(map(str,key)):serialized(poly) for key,poly in row.items()}
                                for row in data]}
    (HERE/'GENERIC_HIGH_TWIST_POLYNOMIALS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'degrees':degrees,'active':len(active),
                      'negative_identity':result['negative_identity'],
                      'failed':failed,'minimum_constant':str(min(Fraction(v['constant']) for v in margins))},indent=2),flush=True)


if __name__=='__main__':main()
