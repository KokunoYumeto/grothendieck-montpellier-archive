"""Exact positive strip b=3k-4,k>=5,c=1: fixed rational certificate."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb,prod
import json
from chamber_polynomials import difference,serialized,SIZES
from positive_wall_chamber import LABELS,CHAR,transpose,constraints,witnesses

HERE=Path(__file__).resolve().parent
PERIODS=(1,2,2,3,6,4,5)


def change(raw):
    answer={}
    for key,value in raw.items():
        i,j,k=map(int,key.split(','));c=Fraction(*value)*(-1)**j
        for h in range(k+1):
            p=(i,0,h)
            answer[p]=answer.get(p,0)+c*comb(k,h)*2**(k-h)
    return {p:c for p,c in answer.items() if c}


def build():
    raw=json.loads((HERE/'ONE_TWIST_POLYNOMIALS.json').read_text())
    data=[{key:change(poly) for key,poly in row.items()}
          for row in raw['phase_polynomials']]
    identity=data[0]['0,0,0'];active=[];margins=[];failed=[]
    assert all(c>=0 for c in identity.values())
    for ix,ik in product(range(4),range(5)):
        order=(ix,0,ik)
        if not any(order):continue
        first=difference(identity,order);worst={}
        for size,row in zip(SIZES[1:],data[1:]):
            bound={}
            for poly in row.values():
                for p,c in difference(poly,order).items():
                    bound[p]=max(bound.get(p,0),abs(c))
            for p,c in bound.items():worst[p]=worst.get(p,0)+size*c
        if not first and not worst:continue
        active.append(order)
        margin={p:first.get(p,0)-worst.get(p,0) for p in first.keys()|worst.keys()}
        bad={p:c for p,c in margin.items() if c<0}
        if bad:failed.append({'order':order,'negative':serialized(bad)})
        margins.append({'order':order,'constant':str(margin.get((0,0,0),0)),
                        'minimum':str(min(margin.values())),
                        'margin':serialized(margin)})
    result={'parameters':'x=X,k=K+5,b=3k-4,c=1; X,K>=0',
            'active_orders':active,'margins':margins,'failed':failed,
            'phase_polynomials':[{key:serialized(poly) for key,poly in row.items()}
                                 for row in data]}
    (HERE/'ONE_TWIST_STRIP_POLYNOMIALS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'active':len(active),'failed':failed,
                      'minimum_constant':str(min(Fraction(e['constant']) for e in margins))}))
    return result


@lru_cache(None)
def data():
    raw=json.loads((HERE/'ONE_TWIST_STRIP_POLYNOMIALS.json').read_text())
    polynomials=[{tuple(map(int,key.split(','))):
                   tuple((tuple(map(int,p.split(','))),Fraction(*v)) for p,v in poly.items())
                 for key,poly in row.items()} for row in raw['phase_polynomials']]
    return polynomials,((0,0,0),)+tuple(map(tuple,raw['active_orders']))


@lru_cache(None)
def traces(parameters):
    X,zero,K=parameters
    assert zero==0
    k=K+5;b=3*k-4;a=b+X
    answer=[]
    for L,row in zip(PERIODS,data()[0]):
        value=sum(c*prod(z**d for z,d in zip(parameters,p))
                  for p,c in row[(a%L,b%L,k%L)])
        assert value.denominator==1
        answer.append(value.numerator)
    return tuple(answer)


@lru_cache(None)
def value(label,parameters):
    total=sum(s*c*t for s,c,t in zip(SIZES,CHAR[LABELS.index(label)],traces(parameters)))
    assert total%120==0
    return total//120


@lru_cache(None)
def constant(label,residue,order):
    answer=0
    for h in product(*(range(v+1) for v in order)):
        answer+=(-1)**(sum(order)-sum(h))*prod(comb(v,j) for v,j in zip(order,h))*value(
            label,tuple(r+60*j for r,j in zip(residue,h)))
    assert answer>=0
    return answer


def tags(x,k,d,mu):
    if any(type(v)is not int or v<0 for v in (x,k,d)) or k<5:
        raise ValueError('Require x,d>=0 and k>=5.')
    mu=tuple(mu)
    if mu not in LABELS:raise ValueError('Outer label must partition five.')
    b=3*k-4;parameters=(x,0,k-5)
    label=transpose(mu) if (d+b+x+1)%2 else mu
    residue=tuple(v%60 for v in parameters);quotient=tuple(v//60 for v in parameters)
    return [dict(label=label,parameters=parameters,residue=residue,quotient=quotient,
                 order=o,constant=constant(label,residue,o)) for o in data()[1]]


def coefficient(x,k,d=0,mu=(5,)):
    return sum(t['constant']*prod(comb(q,j) if q>=j else 0 for q,j in zip(t['quotient'],t['order']))
               for t in tags(x,k,d,mu))


def polytopes(x,k,d=0,mu=(5,)):
    return [constraints(t) for t in tags(x,k,d,mu) if t['constant']]


if __name__=='__main__':build()
