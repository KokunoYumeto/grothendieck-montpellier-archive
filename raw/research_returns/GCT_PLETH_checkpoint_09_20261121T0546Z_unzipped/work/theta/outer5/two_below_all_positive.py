"""T050: positive evaluator for c=2k-2 and every valid k>=2."""
from functools import lru_cache
from itertools import product
from math import comb,prod
import argparse,json
from two_row_positive import (LABELS,ROWS,SIZES,FIRST_ORDERS,transpose,
    _trace,_line_correction,constraints,polytope_tags as old_tags)

BRANCHES={
 'k2_bge2':(2,0,2,True),'k2_b1':(2,2,1,False),'k2_b0':(2,4,0,False),
 'k3_bge2':(3,0,2,True),'k3_b1':(3,1,1,False),'k3_b0':(3,3,0,False),
 'k4_bge1':(4,0,1,True),'k4_b0':(4,2,0,False),
}


def endpoint_branch(x,b,k):
    if k==2:name='k2_bge2' if b>=2 else 'k2_b1' if b else 'k2_b0'
    elif k==3:name='k3_bge2' if b>=2 else 'k3_b1' if b else 'k3_b0'
    elif k==4:name='k4_bge1' if b else 'k4_b0'
    else:raise ValueError('endpoint k must be2,3,4')
    kk,x0,b0,variable=BRANCHES[name]
    X=(x-x0,b-b0) if variable else (x-x0,)
    assert min(X)>=0
    return name,X


@lru_cache(None)
def fixed_value(branch,label,parameters):
    k,x0,b0,variable=BRANCHES[branch]
    x=parameters[0]+x0;b=parameters[1]+b0 if variable else b0
    row=ROWS[LABELS.index(label)]
    total=sum(size*chi*(_trace(g,x,b,k,2*k-2)+_line_correction(g,x,b))
              for g,(size,chi) in enumerate(zip(SIZES,row)))
    assert total%120==0
    return total//120


@lru_cache(None)
def fixed_constant(branch,label,residue,order):
    value=0
    for steps in product(*(range(i+1) for i in order)):
        factor=(-1)**(sum(order)-sum(steps))*prod(comb(i,j) for i,j in zip(order,steps))
        value+=factor*fixed_value(branch,label,tuple(r+60*j for r,j in zip(residue,steps)))
    assert value>=0,(branch,label,residue,order,value)
    return value


def polytope_tags(x,b,k,d,mu):
    if any(type(v)is not int or v<0 for v in (x,b,k,d)):
        raise ValueError('parameters must be nonnegative integers')
    if k<2 or 2*b+x+k<6:raise ValueError('requires k>=2 and2b+x+k>=6')
    mu=tuple(mu)
    if mu not in LABELS:raise ValueError('outer must be a partition of five')
    if k>=5:return old_tags('line',x,b,k,d,mu)
    branch,X=endpoint_branch(x,b,k)
    label=transpose(mu) if (d+b+x)%2 else mu
    residue=tuple(z%60 for z in X);quotient=tuple(z//60 for z in X)
    orders=FIRST_ORDERS if len(X)==2 else tuple((i,) for i in range(4))
    return [dict(kind='newton',sector=branch,parameters=X,residue=residue,
        quotient=quotient,order=order,constant=fixed_constant(branch,label,residue,order))
        for order in orders]


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
    out=dict(statement='T-050',outer=mu,inner=d+b+x+k-2,
        output=(d+3*b+2*x+3*k-8,d+b+x+2*k-2,d+b+x,d+x,d),
        coefficient=coefficient(x,b,k,d,mu),polytope_tags=len(tags))
    if args.polytopes:out['polytopes']=[dict(tag=t,constraints=constraints(t)) for t in tags]
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
