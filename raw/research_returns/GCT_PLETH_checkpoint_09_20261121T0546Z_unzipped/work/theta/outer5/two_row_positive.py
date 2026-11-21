#!/usr/bin/env python3
"""T044/T045/T046/T048: positive evaluator and bounded polytope exporter.

Only fixed elementary arithmetic is used to construct the bounded constants.
No representation library, coefficient oracle or elimination is called.
"""
from functools import lru_cache
from math import comb,prod
from itertools import product
import argparse,json
from five_point_positive import LABELS,transpose
from five_point_hook_positive import FOUR,THREE

CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
SIZES=(1,10,15,20,20,30,24)
ROWS=((1,1,1,1,1,1,1),(4,2,0,1,-1,0,-1),(5,1,1,-1,1,-1,0),
      (6,0,-2,0,0,0,1),(5,-1,1,-1,-1,1,0),(4,-2,0,1,1,0,-1),
      (1,-1,1,1,-1,-1,1))
A0=((0,0),(1,0),(0,1),(2,0),(0,2),(1,1),(2,1),(1,2))
A1=((3,0),(0,3),(3,1),(2,2),(1,3))
A2=((0,4),(1,4),(2,3),(3,2))
ORDERS=tuple(sorted((i,j,l) for pairs,cap in ((A0,3),(A1,2),(A2,1)) for i,j in pairs for l in range(cap+1)))
FIRST_ORDERS=tuple(sorted(A0+A1+A2))
BIVARIATE_ORDERS=tuple((i,j) for i in range(4) for j in range(4) if (i,j)!=(3,3))

def h(g,n):
    if n<0:return 0
    if g==0:return comb(n+3,3)
    if g==1:return (n*n+4*n+4-n%2)//4
    if g==2:return n//2+1 if n%2==0 else 0
    if g==3:return n//3+1
    if g==4:return (1,-1,1,0,0,0)[n%6]
    if g==5:return int(n%4==0)
    return (1,-1,0,0,0)[n%5]

def _trace(g,x,b,k,c):
    a=b+x;H=lambda n:h(g,n);J=CLASSES[g].count(1)*H(k-1)
    A=H(a)*H(b)-H(a+1)*H(b-1)
    B=H(a-1)*H(b)-H(a+1)*H(b-2)
    C=H(a-1)*H(b-1)-H(a)*H(b-2)
    return A*(H(c)-J)-B*(H(c-1)-J)+C*(H(c-2)-J)

def _line_correction(g,x,b):
    if g==0:return 10*(x+1)
    if g==1:return 3*(-1)**b*int(x%2==0)-(x+1)
    if g==2:return -2*(-1)**b*int(x%2==0)
    if g==3:return (1,-1,0)[x%3]
    if g==4:return -(1,-1,0)[x%3]
    return 0

def _three_correction(g,x,b):
    if b:
        if g==0:return 60*(x+1)
        if g==1:return 6*(-1)**b*int(x%2==0)
        return 0
    if g==0:return 50*x+40
    if g==1:return 1+3*int(x%2==0)-x
    if g==2:return 2*int(x%2==1)
    if g in (3,4):return -(1,-1,0)[(x+1)%3]
    return 0

@lru_cache(None)
def _fixed_value(sector,label,parameters):
    if sector=='quadratic':x,b,k=parameters;c=2*k
    elif sector=='below':x,b,K=parameters;k=K+2;c=2*k-1
    elif sector=='first':x,B=parameters;b=B+1;k=c=1
    elif sector=='line':x,b,K=parameters;k=K+5;c=2*k-2
    elif sector=='three_positive_b':x,B,K=parameters;b=B+1;k=K+8;c=2*k-3
    elif sector=='three_zero_b':x,K=parameters;b=0;k=K+8;c=2*k-3
    else:raise ValueError(sector)
    row=ROWS[LABELS.index(label)]
    correction=(_line_correction if sector=='line' else _three_correction if sector.startswith('three_') else lambda g,x,b:0)
    value=sum(size*chi*(_trace(g,x,b,k,c)+correction(g,x,b))
              for g,(size,chi) in enumerate(zip(SIZES,row)))
    assert value%120==0
    return value//120

@lru_cache(None)
def fixed_constant(sector,label,residue,order):
    value=0
    for steps in product(*(range(j+1) for j in order)):
        weight=(-1)**(sum(order)-sum(steps))*prod(comb(j,u) for j,u in zip(order,steps))
        value+=weight*_fixed_value(sector,label,tuple(r+60*u for r,u in zip(residue,steps)))
    assert value>=0,(sector,label,residue,order,value)
    return value

@lru_cache(None)
def _coin_numerator(weights):
    values=[1]
    for w in weights:
        new=[0]*(len(values)+60-w)
        for n,v in enumerate(values):
            for shift in range(0,60,w):new[n+shift]+=v
        values=new
    return tuple(values)

def coin_count(weights,R):
    if R<0:return 0
    q,r=divmod(R,60);d=len(weights);num=_coin_numerator(tuple(weights))
    return sum(num[r+60*j]*comb(q-j+d-1,d-1) for j in range(d)
               if q>=j and r+60*j<len(num))

def polytope_tags(ray,x,b,k,d,mu):
    if ray not in ('quadratic','below','line','three'):raise ValueError('unknown ray')
    if any(type(v) is not int or v<0 for v in (x,b,k,d)):
        raise ValueError('x,b,k,d must be nonnegative integers')
    mu=tuple(mu)
    if mu not in LABELS:raise ValueError('outer must be a partition of five')
    if ray=='below' and (k<1 or 2*b+x+k<3):
        raise ValueError('below ray requires k>=1 and2b+x+k>=3')
    if ray=='line' and (k<5 or 2*b+x+k<6):
        raise ValueError('line ray requires k>=5 and2b+x+k>=6')
    if ray=='three' and (k<8 or 2*b+x+k<9):
        raise ValueError('three ray requires k>=8 and2b+x+k>=9')
    nu=transpose(mu) if (d+b+x)%2 else mu
    if ray=='below' and k==1 and b==0:
        return [dict(kind='coins',weights=weights,shift=shift,R=x-1-shift,copy=i)
                for weights,shifts in (((2,3,4,5),FOUR[nu]),((2,3,5),THREE.get(nu,())))
                for i,shift in enumerate(shifts)]
    if ray=='quadratic':sector=ray;X=(x,b,k);orders=ORDERS
    elif ray=='line':sector=ray;X=(x,b,k-5);orders=ORDERS
    elif ray=='three' and b:sector='three_positive_b';X=(x,b-1,k-8);orders=ORDERS
    elif ray=='three':sector='three_zero_b';X=(x,k-8);orders=BIVARIATE_ORDERS
    elif k>=2:sector='below';X=(x,b,k-2);orders=ORDERS
    else:sector='first';X=(x,b-1);orders=FIRST_ORDERS
    residue=tuple(v%60 for v in X);quotient=tuple(v//60 for v in X)
    return [dict(kind='newton',sector=sector,parameters=X,residue=residue,
                 quotient=quotient,order=order,
                 constant=fixed_constant(sector,nu,residue,order)) for order in orders]

def coefficient(ray,x,b,k,d,mu):
    total=0
    for tag in polytope_tags(ray,x,b,k,d,mu):
        if tag['kind']=='coins':total+=coin_count(tag['weights'],tag['R'])
        else:total+=tag['constant']*prod(comb(q,j) if q>=j else 0 for q,j in zip(tag['quotient'],tag['order']))
    return total

def constraints(tag):
    if tag['kind']=='coins':
        names=[f'z{w}' for w in tag['weights']];n=len(names)
        return dict(variables=names,A_eq=[list(tag['weights'])],b_eq=[tag['R']],
                    A_ub=[[-int(i==j) for j in range(n)] for i in range(n)],b_ub=[0]*n)
    rank=len(tag['parameters']);names=[f'q{i}' for i in range(rank)]+['y']
    chains=[]
    for i,length in enumerate(tag['order']):
        chain=[]
        for j in range(length):chain.append(len(names));names.append(f'z{i}_{j}')
        chains.append(chain)
    n=len(names);Aeq=[];beq=[];A=[];bb=[]
    def inequality(terms,rhs):
        row=[0]*n
        for index,value in terms.items():row[index]=value
        A.append(row);bb.append(rhs)
    for i,(value,r) in enumerate(zip(tag['parameters'],tag['residue'])):
        row=[0]*n;row[i]=60;Aeq.append(row);beq.append(value-r)
        inequality({i:-1},0)
    inequality({rank:-1},0);inequality({rank:1},tag['constant']-1)
    for i,chain in enumerate(chains):
        if not chain:continue
        inequality({chain[0]:-1},0)
        for left,right in zip(chain,chain[1:]):inequality({left:1,right:-1},-1)
        inequality({chain[-1]:1,i:-1},-1)
    return dict(variables=names,A_eq=Aeq,b_eq=beq,A_ub=A,b_ub=bb)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--ray',choices=('quadratic','below','line','three'),required=True)
    for name in ('x','b','k'):parser.add_argument('--'+name,type=int,required=True)
    parser.add_argument('--d',type=int,default=0);parser.add_argument('--outer',default='5')
    parser.add_argument('--polytopes',action='store_true')
    args=parser.parse_args();x,b,k,d=args.x,args.b,args.k,args.d;mu=tuple(map(int,args.outer.split(',')))
    tags=polytope_tags(args.ray,x,b,k,d,mu);delta={'quadratic':0,'below':1,'line':2,'three':3}[args.ray]
    answer=dict(statement={'quadratic':'T-044','below':'T-045','line':'T-046','three':'T-048'}[args.ray],outer=list(mu),
                inner=d+b+x+k-delta,
                output=[d+3*b+2*x+3*k-4*delta,d+b+x+2*k-delta,d+b+x,d+x,d],
                coefficient=coefficient(args.ray,x,b,k,d,mu),active_tags=len(tags))
    if args.polytopes:answer['polytopes']=[dict(tag,constraints=constraints(tag)) for tag in tags]
    print(json.dumps(answer,indent=2))

if __name__=='__main__':main()
