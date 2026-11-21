"""Exact four-parameter trace and positivity test in the c<k upper chamber.

Coordinates C,X,B,K>=0: c=C,k=C+K+4,b=C+3K+10+B,x=X.
The actual full triple term is zero and every first-gap is nonnegative.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product,permutations
from fractions import Fraction
from math import comb,factorial,lcm
import json
import sympy as sp
from sympy.functions.combinatorial.numbers import stirling
from chamber_polynomials import (
    a,b,k,h,triangle,pair_data,binary_h,binary_truncated,square_cycles,
    binomial_polynomial,CLASSES,SIZES,
)

HERE=Path(__file__).resolve().parent
c=sp.Symbol('c');q=sp.Symbol('q')
X,B,K,C=sp.symbols('X B K C')
COORDS=(X,B,K,C)
P3=tuple(permutations(range(3)))
SIGN={p:(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3)) for p in P3}


def sum_polynomial(expr,bound):
    """Exact sum over 0<=q<=bound, also zero at bound=-1."""
    answer=0
    for (d,),coefficient in sp.Poly(sp.expand(expr),q).terms():
        for j in range(d+1):
            factor=int(stirling(d,j,kind=2))*factorial(j)
            if factor:answer+=coefficient*factor*binomial_polynomial(bound+1,j+1)
    return sp.expand(answer)


@lru_cache(None)
def singleton(rest,ar,br,kr,cr):
    L=lcm(*rest);det=(-1)**(4-len(rest));answer=0
    for s in range(L):
        expr=triangle(rest,(ar+s)%L,(br+s)%L,(kr-s)%L)
        expr=expr.subs({a:a+s+L*q,b:b+s+L*q,k:k-s-L*q},simultaneous=True)
        bound=(c-s-(cr-s)%L)/L
        sign=-1 if det==-1 and (cr-s)%2 else 1
        answer+=sign*sum_polynomial(expr,bound)
    return sp.expand(answer)


@lru_cache(None)
def fixed_pair(rest,kr,cr):
    L=lcm(*rest);answer=0
    for s in range(L):
        ell=s+L*q
        expr=binary_truncated(rest,k-ell,kr-s)*binary_truncated(rest,k-c+ell,kr-cr+s)
        bound=(c-s-(cr-s)%L)/L
        answer+=sum_polynomial(expr,bound)
    return sp.expand(answer)


@lru_cache(None)
def class_polynomial(cycles,ar,br,kr,cr):
    alpha=(a+c,b+c,c);res=(ar+cr,br+cr,cr)
    matrix=[[h(cycles,res[i]-i+j,alpha[i]-i+j) for j in range(3)] for i in range(3)]
    answer=sum(SIGN[p]*sp.prod(matrix[i][p[i]] for i in range(3)) for p in P3)
    fixed=cycles.count(1)
    if fixed:
        rest=list(cycles);rest.remove(1);rest=tuple(rest);L=lcm(*rest)
        answer-=fixed*singleton(rest,ar%L,br%L,kr%L,cr%L)
    for swapped,rest in pair_data(cycles):
        determinant=(-1)**((3-len(rest))*(br+cr))
        exterior=determinant*binary_h(rest,a-b,ar-br)
        if swapped:
            if cr%2:continue
            normal=binary_truncated(square_cycles(rest),k-c/2,kr-cr//2)
            answer-=exterior*normal
        else:
            L=lcm(*rest)
            answer+=exterior*fixed_pair(rest,kr%L,cr%L)
    return sp.expand(answer)


def dictionary(expr):
    return {power:Fraction(int(v.p),int(v.q)) for power,v in sp.Poly(expr,*COORDS).terms() if v}


def serialized(poly):
    return {','.join(map(str,p)):[v.numerator,v.denominator] for p,v in sorted(poly.items())}


@lru_cache(None)
def axis_difference(p,d):
    if d==0:return ((p,1),)
    if p<d:return ()
    return tuple((j,comb(p,j)*60**(p-j)*factorial(d)*int(stirling(p-j,d,kind=2)))
                 for j in range(p-d+1))


@lru_cache(None)
def difference_tuple(poly,order):
    answer={}
    for power,value in poly:
        for selected in product(*(axis_difference(p,d) for p,d in zip(power,order))):
            target=tuple(j for j,v in selected)
            coefficient=value
            for j,v in selected:coefficient*=v
            if coefficient:answer[target]=answer.get(target,0)+coefficient
    return tuple(sorted((p,v) for p,v in answer.items() if v))


def main():
    data=[];degrees=[];separate=[]
    for cycles in CLASSES:
        L=lcm(*cycles);row={}
        for ar,br,kr,cr in product(range(L),repeat=4):
            expr=class_polynomial(cycles,ar,br,kr,cr)
            expr=expr.subs({a:C+3*K+10+B+X,b:C+3*K+10+B,k:C+K+4,c:C},simultaneous=True)
            row[(ar,br,kr,cr)]=dictionary(sp.expand(expr))
        degree=max((sum(p) for poly in row.values() for p in poly),default=0)
        sep=tuple(max((p[i] for poly in row.values() for p in poly),default=0) for i in range(4))
        data.append(row);degrees.append(degree);separate.append(sep)
        print('class',cycles,'phases',len(row),'degree',degree,'separate',sep,flush=True)
    identity=data[0][(0,0,0,0)]
    unique=[set(tuple(sorted(poly.items())) for poly in row.values()) for row in data]
    print('unique phases',list(map(len,unique)),flush=True)
    support=set(p for row in data for poly in row.values() for p in poly)
    orders=set(order for p in support for order in product(*(range(v+1) for v in p)))
    orders.discard((0,0,0,0))
    active=[];margins=[];failed=[]
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
    result={'parameters':'x=X,c=C,k=C+K+4,b=C+3K+10+B; X,B,K,C>=0',
            'degrees':degrees,'separate_degrees':separate,
            'negative_identity':serialized({p:v for p,v in identity.items() if v<0}),
            'active_orders':active,'margins':margins,'failed':failed,
            'phase_polynomials':[{','.join(map(str,key)):serialized(poly) for key,poly in row.items()}
                                for row in data]}
    (HERE/'GENERIC_TWIST_UPPER_POLYNOMIALS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'degrees':degrees,'active':len(active),
                      'negative_identity':result['negative_identity'],
                      'failed':failed,'minimum_constant':str(min(Fraction(v['constant']) for v in margins))},indent=2),flush=True)


if __name__=='__main__':main()
