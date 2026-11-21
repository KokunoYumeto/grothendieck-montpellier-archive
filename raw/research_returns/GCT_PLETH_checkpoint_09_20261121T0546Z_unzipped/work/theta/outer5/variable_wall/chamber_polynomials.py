"""Exact class polynomials for k>=3,x>=0,b>=3k-2 on the c=0 wall.

No input-dependent Schur or plethysm routine is used: complete characters,
triangular lattice sums and literal two-subset induction are explicit.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product, combinations
from math import gcd,lcm,factorial,comb
from fractions import Fraction
import json
import hashlib
import sympy as sp
from sympy.functions.combinatorial.numbers import stirling

HERE=Path(__file__).resolve().parent
CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
SIZES=(1,10,15,20,20,30,24)
a,b,k,u,v=sp.symbols('a b k u v')
X,B,K=sp.symbols('X B K')
J=sp.Symbol('J')


def binomial_polynomial(value,degree):
    return sp.prod(value-i for i in range(degree))/factorial(degree)


def complete_values(cycles,cap):
    data=[1]+[0]*cap
    for length in cycles:
        for j in range(length,cap+1):data[j]+=data[j-length]
    return [data[j]-(data[j-1] if j else 0) for j in range(cap+1)]


@lru_cache(None)
def complete_phase(cycles,residue):
    period=lcm(*cycles)
    pole=max(sum(length%d==0 for length in cycles)-(d==1)
             for d in range(1,period+1) if period%d==0)
    degree=pole-1
    data=complete_values(cycles,residue+period*degree)
    q=sp.Symbol('q')
    polynomial=sp.interpolate([(j,data[residue+period*j]) for j in range(degree+1)],q)
    return sp.expand(polynomial.subs(q,(J-residue)/period))


def h(cycles,residue,value):
    return complete_phase(tuple(cycles),residue%lcm(*cycles)).subs(J,value)


@lru_cache(None)
def triangle(cycles,ar,br,kr):
    """Sum_{i,j>=0,i+j<k} s_(a-i,b-j)(standard(cycles))."""
    period=lcm(*cycles);answer=0
    for s,t in product(range(period),repeat=2):
        A=a-s-period*u;BB=b-t-period*v
        expr=sp.Poly(sp.expand(h(cycles,ar-s,A)*h(cycles,br-t,BB)
                  -h(cycles,ar-s+1,A+1)*h(cycles,br-t-1,BB-1)),u,v)
        rem=(kr-1-s-t)%period
        bound=(k-1-s-t-rem)/period
        for (i,j),coefficient in expr.terms():
            for p in range(i+1):
                for q in range(j+1):
                    newton=coefficient*factorial(p)*stirling(i,p,kind=2)*factorial(q)*stirling(j,q,kind=2)
                    if newton:
                        answer+=newton*binomial_polynomial(bound+2,p+q+2)
    return sp.expand(answer)


def permutation(cycles):
    result=[];start=0
    for length in cycles:
        result.extend(start+(i+1)%length for i in range(length));start+=length
    return tuple(result)


def restricted_cycles(p,subset):
    todo=set(subset);out=[]
    while todo:
        start=min(todo);q=start;length=0
        while True:
            todo.remove(q);length+=1;q=p[q]
            if q==start:break
        out.append(length)
    return tuple(sorted(out,reverse=True))


def square_cycles(cycles):
    return tuple(sorted((length//gcd(length,2) for length in cycles
                         for _ in range(gcd(length,2))),reverse=True))


def binary_h(cycles,value,residue):
    if cycles==(1,1,1):return value+1
    if cycles==(2,1):return sp.Integer(residue%2==0)
    if cycles==(3,):return sp.Integer((1,-1,0)[residue%3])
    raise ValueError(cycles)


def binary_truncated(cycles,value,residue):
    if cycles==(1,1,1):return value*(value+1)/2
    if cycles==(2,1):return (value+(residue%2))/2
    if cycles==(3,):return sp.Integer(residue%3==1)
    raise ValueError(cycles)


@lru_cache(None)
def pair_data(cycles):
    p=permutation(cycles);out=[]
    for selected in combinations(range(5),2):
        if set(p[i] for i in selected)!=set(selected):continue
        swapped=p[selected[0]]!=selected[0]
        complement=restricted_cycles(p,set(range(5))-set(selected))
        out.append((swapped,complement))
    return tuple(out)


@lru_cache(None)
def class_polynomial(cycles,ar,br,kr):
    period=lcm(*cycles)
    out=h(cycles,ar,a)*h(cycles,br,b)-h(cycles,ar+1,a+1)*h(cycles,br-1,b-1)
    fixed=cycles.count(1)
    if fixed:
        complement=list(cycles);complement.remove(1);complement=tuple(complement)
        per=lcm(*complement)
        out-=fixed*triangle(complement,ar%per,br%per,kr%per)
    for swapped,complement in pair_data(cycles):
        det=(-1)**((3-len(complement))*br)
        sym=binary_h(complement,a-b,ar-br)
        normal=(binary_truncated(square_cycles(complement),k,kr) if swapped
                else binary_truncated(complement,k,kr)**2)
        out+=(-1 if swapped else 1)*det*sym*normal
    return sp.expand(out)


def dictionary(expr):
    return {powers:Fraction(int(coefficient.p),int(coefficient.q))
            for powers,coefficient in sp.Poly(expr,X,B,K).terms() if coefficient}


def difference(poly,orders,step=60):
    answer={}
    for powers,coefficient in poly.items():
        if any(p<d for p,d in zip(powers,orders)):continue
        for target in product(*(range(p-d+1) for p,d in zip(powers,orders))):
            c=coefficient
            for p,q,d in zip(powers,target,orders):
                c*=comb(p,q)*step**(p-q)*factorial(d)*int(stirling(p-q,d,kind=2))
            if c:answer[target]=answer.get(target,Fraction(0))+c
    return {power:c for power,c in answer.items() if c}


def serialized(poly):
    return {','.join(map(str,powers)):[value.numerator,value.denominator]
            for powers,value in sorted(poly.items())}


def main():
    data=[];max_degrees=[]
    for cycles in CLASSES:
        period=lcm(*cycles);class_data={};degree=0
        for ar,br,kr in product(range(period),repeat=3):
            expr=class_polynomial(cycles,ar,br,kr)
            expr=sp.expand(expr.subs({a:3*K+7+B+X,b:3*K+7+B,k:K+3},simultaneous=True))
            poly=dictionary(expr)
            degree=max(degree,max((sum(power) for power in poly),default=0))
            class_data[(ar,br,kr)]=poly
        data.append(class_data);max_degrees.append(degree)
        print('class',cycles,'phases',len(class_data),'degree',degree,flush=True)
    identity=data[0][(0,0,0)]
    assert max_degrees==[5,3,2,1,0,0,0]
    assert all(coefficient>=0 for coefficient in identity.values())
    print('identity polynomial',serialized(identity),flush=True)
    orders=[d for d in product(range(4),range(5),range(6)) if 0<sum(d)<=5]
    margins=[];failed=[];active=[]
    for order in orders:
        ident=difference(identity,order)
        bounds={}
        for size,phase_data in zip(SIZES[1:],data[1:]):
            worst={}
            for poly in phase_data.values():
                for power,value in difference(poly,order).items():
                    worst[power]=max(worst.get(power,Fraction(0)),abs(value))
            for power,value in worst.items():bounds[power]=bounds.get(power,Fraction(0))+size*value
        if not ident and not bounds:continue
        active.append(order)
        margin={power:ident.get(power,Fraction(0))-bounds.get(power,Fraction(0))
                for power in set(ident)|set(bounds)}
        negative={p:c for p,c in margin.items() if c<0}
        record={'order':order,'constant_margin':str(margin.get((0,0,0),0)),
                'minimum_coefficient':str(min(margin.values(),default=0)),
                'margin':serialized(margin)}
        margins.append(record)
        if negative:failed.append({'order':order,'negative':serialized(negative)})
    expected={(i,j,l) for i in range(4) for j in range(5) for l in range(6)
              if (i==0 and j+l<=4) or (1<=i<=3 and i+j+l<=5)}
    assert set(active)==expected-{(0,0,0)}
    output={'classes':CLASSES,'periods':[lcm(*c) for c in CLASSES],
            'degrees':max_degrees,'phase_polynomials':[
                {','.join(map(str,phase)):serialized(poly) for phase,poly in cls.items()}
                for cls in data], 'active_orders':active,'margins':margins,
            'negative_margins':failed,'status':'PASS' if not failed else 'FAILED'}
    canonical=json.dumps(output,sort_keys=True,separators=(',',':'))
    output['sha256']=hashlib.sha256(canonical.encode()).hexdigest()
    (HERE/'VARIABLE_WALL_POLYNOMIALS.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'status':output['status'],'active':len(active),'failed':failed,
        'minimum_constant_margin':min((Fraction(x['constant_margin']) for x in margins),default=0)},default=str,indent=2))


if __name__=='__main__':main()
