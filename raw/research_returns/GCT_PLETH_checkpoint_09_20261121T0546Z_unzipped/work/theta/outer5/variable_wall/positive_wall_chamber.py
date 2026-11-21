"""T054 positive formula on k>=3,x>=0,b>=3k-2, with literal matrices."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
from itertools import product,combinations
from math import comb,prod
import argparse,json

HERE=Path(__file__).resolve().parent
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
SIZES=(1,10,15,20,20,30,24)
CHAR=((1,1,1,1,1,1,1),(4,2,0,1,-1,0,-1),
      (5,1,1,-1,1,-1,0),(6,0,-2,0,0,0,1),
      (5,-1,1,-1,-1,1,0),(4,-2,0,1,1,0,-1),
      (1,-1,1,1,-1,-1,1))
DATA=json.loads((HERE/'VARIABLE_WALL_POLYNOMIALS.json').read_text())
PERIODS=tuple(DATA['periods'])
POLYS=tuple({tuple(map(int,key.split(','))):
              tuple((tuple(map(int,power.split(','))),Fraction(*value)) for power,value in polynomial.items())
             for key,polynomial in row.items()} for row in DATA['phase_polynomials'])
ORDERS=((0,0,0),)+tuple(map(tuple,DATA['active_orders']))


def transpose(mu):
    return tuple(sum(a>=j for a in mu) for j in range(1,max(mu)+1))


@lru_cache(None)
def traces(parameters):
    X,B,K=parameters;k=K+3;x=X;b=3*k-2+B;a=b+x
    answer=[]
    for period,row in zip(PERIODS,POLYS):
        poly=row[(a%period,b%period,k%period)]
        value=sum(c*prod(z**p for z,p in zip(parameters,powers)) for powers,c in poly)
        assert value.denominator==1
        answer.append(value.numerator)
    return tuple(answer)


@lru_cache(None)
def fixed_value(label,parameters):
    chi=CHAR[LABELS.index(label)]
    value=sum(size*c*t for size,c,t in zip(SIZES,chi,traces(parameters)))
    assert value%120==0
    return value//120


@lru_cache(None)
def constant(label,residue,order):
    answer=0
    for step in product(*(range(d+1) for d in order)):
        c=(-1)**(sum(order)-sum(step))*prod(comb(d,j) for d,j in zip(order,step))
        answer+=c*fixed_value(label,tuple(r+60*j for r,j in zip(residue,step)))
    assert answer>=0,(label,residue,order,answer)
    return answer


def tags(x,b,k,d,mu):
    if any(type(z)is not int or z<0 for z in (x,b,k,d)):
        raise ValueError('Parameters must be nonnegative integers.')
    if k<3 or b<3*k-2 or 2*b+x<5*k:
        raise ValueError('Require k>=3,b>=3k-2,2b+x>=5k.')
    mu=tuple(mu)
    if mu not in LABELS:raise ValueError('Outer label must partition five.')
    parameters=(x,b-3*k+2,k-3)
    label=transpose(mu) if (d+b+x)%2 else mu
    residue=tuple(z%60 for z in parameters);quotient=tuple(z//60 for z in parameters)
    return [dict(label=label,parameters=parameters,residue=residue,quotient=quotient,
                 order=order,constant=constant(label,residue,order)) for order in ORDERS]


def coefficient(x,b,k,d,mu):
    return sum(tag['constant']*prod(comb(q,j) if q>=j else 0
                                   for q,j in zip(tag['quotient'],tag['order']))
               for tag in tags(x,b,k,d,mu))


def constraints(tag):
    order=tag['order'];nv=4+sum(order)
    names=['q_X','q_B','q_K','selector']
    names += [f'chain_{axis}_{j+1}' for axis,length in enumerate(order) for j in range(length)]
    eq=[];rhs=[];ge=[];ge_rhs=[]
    for axis in range(3):
        row=[0]*nv;row[axis]=60;eq.append(row)
        rhs.append(tag['parameters'][axis]-tag['residue'][axis])
    start=4
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
                  [max(0,q-1) for q,length in zip(tag['quotient'],order) for _ in range(length)],
                A_eq=eq,b_eq=rhs,A_ge=ge,b_ge=ge_rhs,order=order)


def witnesses(tag):
    if any(q<j for q,j in zip(tag['quotient'],tag['order'])):
        return
    for selector in range(tag['constant']):
        for chains in product(*(combinations(range(q),j) for q,j in zip(tag['quotient'],tag['order']))):
            yield tuple(tag['quotient'])+(selector,)+sum(chains,())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('x','b','k'):p.add_argument('--'+name,type=int,required=True)
    p.add_argument('--d',type=int,default=0);p.add_argument('--outer',default='5')
    p.add_argument('--polytopes',action='store_true');args=p.parse_args()
    mu=tuple(map(int,args.outer.split(',')));alltags=tags(args.x,args.b,args.k,args.d,mu)
    out={'coefficient':coefficient(args.x,args.b,args.k,args.d,mu)}
    if args.polytopes:out['polytopes']=[constraints(tag) for tag in alltags if tag['constant']]
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
