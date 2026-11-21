"""T051: complete positive evaluator three below the quadratic ray."""
from functools import lru_cache
from itertools import product
from math import comb,prod
import argparse,json
from two_row_positive import (LABELS,ROWS,SIZES,FIRST_ORDERS,transpose,
    _trace,_three_correction,constraints,polytope_tags as old_tags)


def triple(g,x,b,k):
    if (k,b)==(3,0):return (10,-3+(-1)**x,-2*(-1)**x,1,(-1)**x,0,0)[g]
    if (k,b)==(2,1):return (20,2*(-1)**(x+1),0,-1,(-1)**x,0,0)[g]
    if (k,b)==(2,0):return (60,-6,0,0,0,0,0)[g]
    return 0


BRANCHES={}
for _k in range(2,8):
    _need=9-_k;_cut=(_need+1)//2
    BRANCHES[f'k{_k}_bge{_cut}']=(_k,0,_cut,True)
    for _b in range(_cut-1,-1,-1):
        BRANCHES[f'k{_k}_b{_b}']=(_k,_need-2*_b,_b,False)


def endpoint_branch(x,b,k):
    need=9-k;cut=(need+1)//2
    name=f'k{k}_bge{cut}' if b>=cut else f'k{k}_b{b}'
    kk,x0,b0,variable=BRANCHES[name]
    X=(x-x0,b-b0) if variable else (x-x0,)
    assert min(X)>=0
    return name,X


@lru_cache(None)
def fixed_value(branch,label,parameters):
    k,x0,b0,variable=BRANCHES[branch]
    x=x0+parameters[0];b=b0+parameters[1] if variable else b0
    row=ROWS[LABELS.index(label)]
    total=sum(size*chi*(_trace(g,x,b,k,2*k-3)+_three_correction(g,x,b)-triple(g,x,b,k))
              for g,(size,chi) in enumerate(zip(SIZES,row)))
    assert total%120==0
    return total//120


@lru_cache(None)
def fixed_constant(branch,label,residue,order):
    result=0
    for steps in product(*(range(i+1) for i in order)):
        factor=(-1)**(sum(order)-sum(steps))*prod(comb(i,j) for i,j in zip(order,steps))
        result+=factor*fixed_value(branch,label,tuple(r+60*j for r,j in zip(residue,steps)))
    assert result>=0,(branch,label,residue,order,result)
    return result


def polytope_tags(x,b,k,d,mu):
    if any(type(v)is not int or v<0 for v in (x,b,k,d)):
        raise ValueError('parameters must be nonnegative integers')
    if k<2 or 2*b+x+k<9:raise ValueError('requires k>=2 and2b+x+k>=9')
    mu=tuple(mu)
    if mu not in LABELS:raise ValueError('outer must be a partition of five')
    if k>=8:return old_tags('three',x,b,k,d,mu)
    branch,X=endpoint_branch(x,b,k)
    label=transpose(mu) if (d+b+x)%2 else mu
    residue=tuple(z%60 for z in X);quotient=tuple(z//60 for z in X)
    orders=FIRST_ORDERS if len(X)==2 else tuple((i,) for i in range(4))
    return [dict(kind='newton',sector=branch,parameters=X,residue=residue,
        quotient=quotient,order=order,constant=fixed_constant(branch,label,residue,order)) for order in orders]


def coefficient(x,b,k,d,mu):
    return sum(t['constant']*prod(comb(q,i) if q>=i else 0 for q,i in zip(t['quotient'],t['order']))
               for t in polytope_tags(x,b,k,d,mu))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for v in ('x','b','k'):p.add_argument('--'+v,type=int,required=True)
    p.add_argument('--d',type=int,default=0);p.add_argument('--outer',default='5')
    p.add_argument('--polytopes',action='store_true');args=p.parse_args()
    x,b,k,d=args.x,args.b,args.k,args.d;mu=tuple(map(int,args.outer.split(',')))
    tags=polytope_tags(x,b,k,d,mu)
    out=dict(statement='T-051',outer=mu,inner=d+b+x+k-3,
        output=(d+3*b+2*x+3*k-12,d+b+x+2*k-3,d+b+x,d+x,d),
        coefficient=coefficient(x,b,k,d,mu),polytope_tags=len(tags))
    if args.polytopes:out['polytopes']=[dict(tag=t,constraints=constraints(t)) for t in tags]
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
