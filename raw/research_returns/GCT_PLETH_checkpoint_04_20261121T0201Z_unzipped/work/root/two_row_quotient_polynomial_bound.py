"""Exact polynomial domination for general two-row quotient sections."""
from pathlib import Path
from itertools import product
from math import comb
from fractions import Fraction
import sympy as s
import json

HERE=Path(__file__).resolve().parent
x,b,k,t=s.symbols('x b k t');variables=(x,b,k,t)
a=x+b;c=2*k+t


def phase(n,p,modulus):
    return int(n.subs(dict(zip(variables,p))))%modulus


def h(n,kind,p):
    n=s.sympify(n)
    if kind=='id':return (n+1)*(n+2)*(n+3)/6
    if kind=='trans':
        q=phase(n,p,2)
        return (n*n+4*n+4-q)/4
    if kind=='double':
        return s.Integer(0) if phase(n,p,2) else (n+2)/2
    if kind=='three':return (n+3-phase(n,p,3))/3
    raise ValueError(kind)


def schur(A,B,kind,p):
    return h(A,kind,p)*h(B,kind,p)-h(A+1,kind,p)*h(B-1,kind,p)


def polynomial(kind,p):
    S0=schur(a,b,kind,p)
    S1=schur(a-1,b,kind,p)+schur(a,b-1,kind,p)
    S2=schur(a-1,b-1,kind,p)
    fixed={'id':5,'trans':3,'double':1,'three':2}[kind]
    R=S0-S1+S2;T=S1-2*S2
    expr=R*(h(c,kind,p)-fixed*h(k-1,kind,p))
    expr+=T*(h(c,kind,p)-h(c-1,kind,p))
    expr+=S2*(h(c,kind,p)-2*h(c-1,kind,p)+h(c-2,kind,p))
    poly=s.Poly(s.expand(expr),*variables)
    return {tuple(e):Fraction(int(v.p),int(v.q)) for e,v in poly.terms() if v}


def diff(poly,axis,step=60):
    result={}
    for exponent,value in poly.items():
        n=exponent[axis]
        for j in range(n):
            ee=list(exponent);ee[axis]=j;ee=tuple(ee)
            result[ee]=result.get(ee,Fraction(0))+value*comb(n,j)*step**(n-j)
    return {e:v for e,v in result.items() if v}


def multi(poly,order):
    for axis,n in enumerate(order):
        for _ in range(n):poly=diff(poly,axis)
    return poly


identity=polynomial('id',(0,0,0,0))
print('identity degree',max(map(sum,identity)),'monomials',len(identity),
      'negative coefficients',[(e,str(v)) for e,v in identity.items() if v<0],flush=True)
assert all(v>0 for v in identity.values())
nonidentity={}
for kind,modulus in [('trans',2),('double',2),('three',3)]:
    polynomials=[polynomial(kind,p) for p in product(range(modulus),repeat=4)]
    degree=max((sum(e) for poly in polynomials for e in poly),default=-1)
    print(kind,'phase_count',len(polynomials),'degree',degree,flush=True)
    nonidentity[kind]=polynomials
    assert degree<=3 if kind!='three' else degree<=1

orders=[v for v in product(range(4),repeat=4) if 1<=sum(v)<=3]
rows=[];failures=[]
for order in orders:
    dominant=multi(identity,order)
    bounds={}
    for kind,weight in [('trans',10),('double',15),('three',20)]:
        maxima={}
        for poly in nonidentity[kind]:
            for exponent,value in multi(poly,order).items():
                maxima[exponent]=max(maxima.get(exponent,Fraction(0)),abs(value))
        for exponent,value in maxima.items():
            bounds[exponent]=bounds.get(exponent,Fraction(0))+weight*value
    keys=set(dominant)|set(bounds)
    margins={e:dominant.get(e,Fraction(0))-bounds.get(e,Fraction(0)) for e in keys}
    negative={e:v for e,v in margins.items() if v<0}
    constant=margins.get((0,0,0,0),Fraction(0))
    row={'order':order,'minimum_coefficient_margin':str(min(margins.values())),
         'constant_margin':str(constant),'negative_coefficients':{str(e):str(v) for e,v in negative.items()}}
    rows.append(row)
    if negative or constant<=0:failures.append(row)
    print(order,'constant margin',constant,'negative',len(negative),flush=True)

downset=set()
for exponent in identity:
    downset.update(product(*(range(n+1) for n in exponent)))
output={'statement':'G-021','identity_polynomial':{str(e):str(v) for e,v in identity.items()},
        'identity_total_degree':max(map(sum,identity)),
        'downset':sorted(downset),'downset_size':len(downset),
        'positive_order_checks':rows,'failures':failures,
        'phase_counts':{'transposition':16,'double_transposition':16,'three_cycle':81}}
(HERE/'TWO_ROW_QUOTIENT_POLYNOMIAL_BOUND.json').write_text(json.dumps(output,indent=2)+'\n')
print('DOWNSET',len(downset),'FAILURES',len(failures),flush=True)
assert not failures
