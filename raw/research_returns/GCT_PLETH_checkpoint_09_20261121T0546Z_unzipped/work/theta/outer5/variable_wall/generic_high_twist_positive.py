"""T059 fixed positive formula for normalized k<=c<2k."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction
from itertools import product,combinations
from math import comb,prod
import argparse,json
from positive_wall_chamber import LABELS,CHAR,SIZES,transpose

HERE=Path(__file__).resolve().parent
DATA=json.loads((HERE/'GENERIC_HIGH_TWIST_POLYNOMIALS.json').read_text())
PERIODS=(1,2,2,3,6,4,5)
POLYS=[{tuple(map(int,key.split(','))):
         tuple((tuple(map(int,p.split(','))),Fraction(*v)) for p,v in poly.items())
        for key,poly in row.items()} for row in DATA['phase_polynomials']]
ORDERS=((0,0,0,0),)+tuple(map(tuple,DATA['active_orders']))


@lru_cache(None)
def traces(parameters):
    X,B,K,C=parameters;c=K+2*C+1;k=K+C+1;b=K+B+1;a=b+X
    answer=[]
    for L,row in zip(PERIODS,POLYS):
        value=sum(coef*prod(z**p for z,p in zip(parameters,power))
                  for power,coef in row[(a%L,b%L,k%L,c%L)])
        assert value.denominator==1
        answer.append(value.numerator)
    return tuple(answer)


@lru_cache(None)
def fixed_value(label,parameters):
    total=sum(s*t*v for s,t,v in zip(SIZES,CHAR[LABELS.index(label)],traces(parameters)))
    assert total%120==0
    return total//120


@lru_cache(None)
def constant(label,residue,order):
    total=0
    for h in product(*(range(d+1) for d in order)):
        coefficient=(-1)**(sum(order)-sum(h))*prod(comb(d,j) for d,j in zip(order,h))
        total+=coefficient*fixed_value(label,tuple(r+60*j for r,j in zip(residue,h)))
    assert total>=0,(label,residue,order,total)
    return total


def parameters(x,b,k,c,d,mu):
    if any(type(v)is not int or v<0 for v in (x,b,k,c,d)):
        raise ValueError('All scalar parameters must be nonnegative integers.')
    if c<k or c>=2*k or b+c<2*k:
        raise ValueError('Require k<=c<2k and b+c>=2k.')
    mu=tuple(mu)
    if mu not in LABELS:raise ValueError('Outer label must partition five.')
    Z=(x,b-2*k+c,2*k-c-1,c-k)
    label=transpose(mu) if (d+b+x+c)%2 else mu
    return label,Z,tuple(v%60 for v in Z),tuple(v//60 for v in Z)


def tags(x,b,k,c,d,mu):
    label,Z,residue,quotient=parameters(x,b,k,c,d,mu)
    return [dict(label=label,parameters=Z,residue=residue,quotient=quotient,
                 order=o,constant=constant(label,residue,o)) for o in ORDERS]


def coefficient(x,b,k,c,d=0,mu=(5,)):
    label,Z,residue,quotient=parameters(x,b,k,c,d,mu)
    return sum(constant(label,residue,o)*prod(comb(q,j) for q,j in zip(quotient,o))
               for o in ORDERS if all(q>=j for q,j in zip(quotient,o)))


def constraints(tag):
    order=tag['order'];nv=5+sum(order)
    names=['q_X','q_B','q_K','q_C','selector']
    names += [f'chain_{i}_{j+1}' for i,n in enumerate(order) for j in range(n)]
    eq=[];rhs=[];ge=[];ge_rhs=[]
    for i in range(4):
        row=[0]*nv;row[i]=60;eq.append(row)
        rhs.append(tag['parameters'][i]-tag['residue'][i])
    start=5
    for axis,length in enumerate(order):
        for j in range(length-1):
            row=[0]*nv;row[start+j+1]=1;row[start+j]=-1
            ge.append(row);ge_rhs.append(1)
        if length:
            row=[0]*nv;row[axis]=1;row[start+length-1]=-1
            ge.append(row);ge_rhs.append(1)
        start+=length
    return dict(variables=names,integer=True,lower_bounds=[0]*nv,
                upper_bounds=list(tag['quotient'])+[tag['constant']-1]+
                   [max(0,q-1) for q,n in zip(tag['quotient'],order) for _ in range(n)],
                A_eq=eq,b_eq=rhs,A_ge=ge,b_ge=ge_rhs,order=order)


def witnesses(tag):
    if any(q<n for q,n in zip(tag['quotient'],tag['order'])):return
    for selector in range(tag['constant']):
        for chains in product(*(combinations(range(q),n) for q,n in zip(tag['quotient'],tag['order']))):
            yield tuple(tag['quotient'])+(selector,)+sum(chains,())


def polytopes(x,b,k,c,d=0,mu=(5,)):
    return [constraints(t) for t in tags(x,b,k,c,d,mu) if t['constant']]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('x','b','k','c'):parser.add_argument('--'+name,type=int,required=True)
    parser.add_argument('--d',type=int,default=0);parser.add_argument('--outer',default='5')
    parser.add_argument('--polytopes',action='store_true');v=parser.parse_args()
    mu=tuple(map(int,v.outer.split(',')))
    result={'inner':v.d+v.b+v.x+v.c-v.k,
            'output':[v.d+3*v.b+2*v.x+4*v.c-5*v.k,v.d+v.b+v.x+v.c,v.d+v.b+v.x,v.d+v.x,v.d],
            'coefficient':coefficient(v.x,v.b,v.k,v.c,v.d,mu)}
    if v.polytopes:result['polytopes']=polytopes(v.x,v.b,v.k,v.c,v.d,mu)
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
