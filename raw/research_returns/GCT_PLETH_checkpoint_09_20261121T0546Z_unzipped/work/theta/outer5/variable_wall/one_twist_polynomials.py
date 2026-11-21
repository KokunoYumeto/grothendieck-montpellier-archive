"""Exact c=1 class polynomials for k>=3,x>=0,b>=3k-3.

This script records success or failure of the stated coefficientwise
positive-difference test; the report must retain the actual outcome.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from fractions import Fraction
from math import lcm
import json
import sympy as sp
from chamber_polynomials import (
    a,b,k,X,B,K,h,triangle,pair_data,binary_h,binary_truncated,
    difference,serialized,CLASSES,SIZES,
)

HERE=Path(__file__).resolve().parent


@lru_cache(None)
def class_polynomial(cycles,ar,br,kr):
    fixed=cycles.count(1)
    out=(fixed-1)*(h(cycles,ar+1,a+1)*h(cycles,br+1,b+1)
                   -h(cycles,ar+2,a+2)*h(cycles,br,b))
    out-=h(cycles,ar+1,a+1)*h(cycles,br+2,b+2)
    out+=h(cycles,ar+3,a+3)*h(cycles,br,b)
    if fixed:
        rest=list(cycles);rest.remove(1);rest=tuple(rest)
        det=(-1)**(4-len(rest))
        first=det*triangle(rest,ar,br,kr)
        second=triangle(rest,ar+1,br+1,kr-1).subs(
            {a:a+1,b:b+1,k:k-1},simultaneous=True)
        out-=fixed*(first+second)
    for swapped,rest in pair_data(cycles):
        if swapped:
            continue
        det=(-1)**((3-len(rest))*(br+1))
        out+=2*det*binary_h(rest,a-b,ar-br)*binary_truncated(
            rest,k,kr)*binary_truncated(rest,k-1,kr-1)
    return sp.expand(out)


def dictionary(expr):
    return {powers:Fraction(int(c.p),int(c.q))
            for powers,c in sp.Poly(expr,X,B,K).terms() if c}


def main():
    data=[];degrees=[];separate=[]
    for cycles in CLASSES:
        L=lcm(*cycles);row={}
        for ar,br,kr in product(range(L),repeat=3):
            expr=class_polynomial(cycles,ar,br,kr)
            expr=expr.subs({a:3*K+6+B+X,b:3*K+6+B,k:K+3},simultaneous=True)
            row[(ar,br,kr)]=dictionary(sp.expand(expr))
        degree=max((sum(p) for poly in row.values() for p in poly),default=0)
        sep=tuple(max((p[i] for poly in row.values() for p in poly),default=0) for i in range(3))
        data.append(row);degrees.append(degree);separate.append(sep)
        print('class',cycles,'phases',len(row),'degree',degree,'separate',sep,flush=True)
    ident=data[0][(0,0,0)]
    bounds=tuple(max(s[i] for s in separate) for i in range(3))
    active=[];margins=[];failed=[]
    for order in product(*(range(v+1) for v in bounds)):
        if not any(order):continue
        first=difference(ident,order)
        worst={}
        for size,phases in zip(SIZES[1:],data[1:]):
            cls={}
            for poly in phases.values():
                for p,c in difference(poly,order).items():
                    cls[p]=max(cls.get(p,0),abs(c))
            for p,c in cls.items():worst[p]=worst.get(p,0)+size*c
        if not first and not worst:continue
        active.append(order)
        margin={p:first.get(p,0)-worst.get(p,0) for p in first.keys()|worst.keys()}
        bad={p:c for p,c in margin.items() if c<0}
        entry={'order':order,'constant':str(margin.get((0,0,0),0)),
               'minimum':str(min(margin.values(),default=0)),
               'margin':serialized(margin)}
        margins.append(entry)
        if bad:failed.append({'order':order,'negative':serialized(bad)})
    out={'parameters':'c=1,k=K+3,b=3k-3+B,x=X; X,B,K>=0',
         'degrees':degrees,'separate_degrees':separate,
         'negative_identity':serialized({p:c for p,c in ident.items() if c<0}),
         'active_orders':active,'margins':margins,'failed':failed,
         'phase_polynomials':[{','.join(map(str,key)):serialized(poly)
                               for key,poly in row.items()} for row in data]}
    (HERE/'ONE_TWIST_POLYNOMIALS.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'degrees':degrees,'active':len(active),
                      'negative_identity':out['negative_identity'],
                      'failed':failed,'minimum_constant':str(min(
                          Fraction(e['constant']) for e in margins))},indent=2))


if __name__=='__main__':main()
