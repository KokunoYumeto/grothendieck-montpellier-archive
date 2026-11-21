#!/usr/bin/env python3
"""T061: the first unstable hook order, by an explicit deleted-point count."""
from pathlib import Path
import sys
import argparse
import json

ROOT=Path(__file__).resolve().parents[2]/'root'
sys.path.append(str(ROOT))
import stable_hook_positive as stable


def target_labels(m,r):
    q=m-1-r
    out=[(q+1,)+(1,)*r,(q,)+(1,)*(r+1)]
    if r>=1 and q>=2:
        out.append((q,2)+(1,)*(r-1))
    return tuple(out)


def parameters(m,a,r,t,mu):
    mu=tuple(mu)
    if any(type(v)is not int for v in (m,a,r,t)) or m<4 or a<2 or not 0<=r<=m-2 or t<0:
        raise ValueError('require m>=4,a>=2,0<=r<=m-2,t>=0')
    if not stable.valid_partition(mu,m) or (m-2)*a<m+r:
        raise ValueError('invalid outer label or first partition gap')
    n=a+t-1
    lam=((m-1)*a+t-m-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
    assert sum(lam)==m*n and lam[0]>=lam[1]
    nu=stable.transpose(mu) if t%2 else mu
    return lam,n,nu


def coefficient(m,a,r,t=0,mu=None):
    if mu is None:mu=(m,)
    _,_,nu=parameters(m,a,r,t,mu)
    if a==2:
        return int(nu==(m-r-2,2)+(1,)*r)
    value=stable.module_coefficient(m,a,r,nu)-int(nu in target_labels(m,r))
    assert value>=0
    return value


def _coins(value):
    if value<0 or value==1:raise ValueError('not a nonnegative combination of2and3')
    three=value%2
    return {2:(value-3*three)//2,3:three}


def canonical_removed_point(m,a,r,nu):
    """A literal stable-hook lattice point in each affected type, a>=3."""
    nu=tuple(nu)
    if a<3 or nu not in target_labels(m,r):raise ValueError('unaffected input')
    D=a+r
    poly=stable.module_polytope(m,a,r,nu)
    point={name:0 for name in poly['variables']}
    if nu==(m,):
        assert r==0
        coins=_coins(D)
        for j,value in coins.items():point[f'b{j}']=value
        point[f'z{min(j for j,value in coins.items() if value)}']=1
        assert stable.valid_witness(poly,point)
        return point
    cell_list=stable.cells(nu)
    tableau={cell:j for j,cell in enumerate(cell_list,1)}
    kept=[cell for cell in cell_list if cell not in ((1,1),(2,1))]
    selected=set(sorted(kept,key=lambda c:(c[1]-c[0]+1,c))[:r])
    lowest=sum(i*v for i,v in enumerate(nu))+sum(j-i+1 for i,j in selected)
    remainder=D-lowest
    if remainder==1:
        q=m-1-r
        if nu==(q+1,)+(1,)*r:
            assert r>=1
            u,v=(1,nu[0]),(2,1)
            tableau[u],tableau[v]=tableau[v],tableau[u]
        else:
            assert nu==(q,2)+(1,)*(r-1)
            if r>=2:
                u,v=(2,2),(3,1)
                tableau[u],tableau[v]=tableau[v],tableau[u]
            elif q==2:
                selected={(1,2)}
            else:
                assert q>=3
                tableau={(1,j):j for j in range(1,q)}
                tableau[(1,q)]=q+2
                tableau[(2,1)]=q
                tableau[(2,2)]=q+1
    rows={j:cell[0] for cell,j in tableau.items()}
    desc={j:int(rows[j+1]>rows[j]) for j in range(1,m)}
    degree=sum((m-j)*v for j,v in desc.items())+sum(j-i+1 for i,j in selected)
    coins=_coins(D-degree)
    for cell,label in tableau.items():point[f'X{cell[0]}_{cell[1]}_{label}']=1
    for j,value in desc.items():point[f'd{j}']=value
    for i,j in selected:point[f'Y{i}_{j}']=1
    for j,value in coins.items():point[f'c{j}']=value
    assert stable.valid_witness(poly,point),(m,a,r,nu,point)
    return point


def polytopes(m,a,r,t=0,mu=None):
    if mu is None:mu=(m,)
    mu=tuple(mu)
    lam,n,nu=parameters(m,a,r,t,mu)
    result={'statement':'T-061','partition':lam,'inner':n,'outer':mu,'effective_label':nu}
    if a==2:
        result['polytopes']=([{'variables':[],'constraints':[],'variable_count':0,'constraint_count':0}]
                             if nu==(m-r-2,2)+(1,)*r else [])
        return result
    base=stable.module_polytope(m,a,r,nu)
    if nu not in target_labels(m,r):
        result['polytopes']=[base]
        return result
    point=canonical_removed_point(m,a,r,nu)
    pieces=[]
    prefix=[]
    for index,name in enumerate(base['variables']):
        for relation,offset in (('<=',-1),('>=',1)):
            rows=base['constraints']+prefix+[{'coefficients':{name:1},'relation':relation,'rhs':point[name]+offset}]
            pieces.append({'tag':{'first_different_coordinate':index,'direction':relation},
                           'variables':base['variables'],'constraints':rows,
                           'variable_count':base['variable_count'],'constraint_count':len(rows)})
        prefix=prefix+[{'coefficients':{name:1},'relation':'=','rhs':point[name]}]
    result['removed_point']=point
    result['polytopes']=pieces
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('m','a','r'):p.add_argument('--'+name,type=int,required=True)
    p.add_argument('--t',type=int,default=0)
    p.add_argument('--outer')
    p.add_argument('--polytopes',action='store_true')
    v=p.parse_args();mu=tuple(map(int,v.outer.split(','))) if v.outer else (v.m,)
    result={'coefficient':coefficient(v.m,v.a,v.r,v.t,mu)}
    if v.polytopes:result.update(polytopes(v.m,v.a,v.r,v.t,mu))
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
