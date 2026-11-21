"""T063: positive varying-degree hook coefficients at second ideal order."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
from collections import Counter
import sys
import argparse
import json

ROOT=Path(__file__).resolve().parents[2]/'root'
sys.path.insert(0,str(ROOT))
import stable_hook_positive as stable


def add_box(lam):
    for i in range(len(lam)+1):
        if i and (i==len(lam) or lam[i]==lam[i-1]):
            if i<len(lam):continue
        if i==len(lam):yield lam+(1,)
        elif i==0 or lam[i]<lam[i-1]:
            yield lam[:i]+(lam[i]+1,)+lam[i+1:]


@lru_cache(None)
def target_multiplicities(m,r):
    q=m-1-r
    smaller=[]
    if q>=2:smaller.append((q-1,)+(1,)*r)
    if r>=1:smaller.append((q,)+(1,)*(r-1))
    out=Counter()
    for beta in smaller:
        for gamma in add_box(beta):
            for nu in add_box(gamma):out[nu]+=1
    assert out and max(out.values())<=4
    return dict(out)


def parameters(m,a,r,t,mu):
    mu=tuple(mu)
    if any(type(v)is not int for v in (m,a,r,t)) or m<4 or a<5 or not 0<=r<=m-2 or t<0:
        raise ValueError('require m>=4,a>=5,0<=r<=m-2,t>=0')
    if not stable.valid_partition(mu,m):raise ValueError('outer label must partition m')
    n=a+t-2
    lam=((m-1)*a+t-2*m-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
    assert lam[0]>=lam[1] and sum(lam)==m*n
    return lam,n,stable.transpose(mu) if t%2 else mu


def coefficient(m,a,r,t=0,mu=None):
    if mu is None:mu=(m,)
    _,_,nu=parameters(m,a,r,t,mu)
    result=stable.module_coefficient(m,a,r,nu)-target_multiplicities(m,r).get(nu,0)
    assert result>=0
    return result


@lru_cache(None)
def low_comajor_tableaux(nu,budget):
    """Standardize all SSYT whose excess above row minima is <=budget."""
    cells=stable.cells(nu);values={};found=set();answer=[]
    def visit(j,left):
        if j==len(cells):
            order=sorted(cells,key=lambda c:(values[c],c[1],c[0]))
            tab={cell:i for i,cell in enumerate(order,1)}
            key=tuple(tab[c] for c in cells)
            if key not in found:
                found.add(key);answer.append(key)
            return
        i,k=cells[j];base=i-1
        lo=max(base,values.get((i,k-1),base),values.get((i-1,k),base-1)+1)
        for value in range(lo,base+left+1):
            values[i,k]=value
            visit(j+1,left-(value-base))
        values.pop((i,k),None)
    visit(0,budget)
    return tuple(answer)


def low_subsets(cells,r,budget):
    weighted=sorted((j-i+1,(i,j)) for i,j in cells)
    if r==0:
        yield ();return
    if r==len(cells):
        yield tuple(cells);return
    lowest=sum(w for w,_ in weighted[:r]);cut=weighted[r-1][0]
    forced=tuple(c for w,c in weighted if w<cut-budget)
    middle=tuple(c for w,c in weighted if cut-budget<=w<=cut+budget)
    assert len(middle)<=4*budget+2
    for choice in combinations(middle,r-len(forced)):
        chosen=forced+choice
        if sum(j-i+1 for i,j in chosen)-lowest<=budget:yield chosen


def coins(weights,degree):
    if degree<0:return
    if not weights:
        if degree==0:yield ()
        return
    for value in range(degree//weights[0]+1):
        for rest in coins(weights[1:],degree-weights[0]*value):yield (value,)+rest


@lru_cache(None)
def base_removed_points(m,base_a,r,nu):
    needed=target_multiplicities(m,r).get(nu,0)
    assert base_a in (5,6) and nu!=(m,) and needed
    C=stable.cells(nu);kept=tuple(c for c in C if c not in ((1,1),(2,1)))
    b=sum(i*v for i,v in enumerate(nu));low=b+sum(sorted(j-i+1 for i,j in kept)[:r])
    D=base_a+r;budget=D-low
    assert 0<=budget<=5
    result=[]
    for raw in low_comajor_tableaux(nu,budget):
        tab=dict(zip(C,raw));rows={v:c[0] for c,v in tab.items()}
        descent={j:int(rows[j+1]>rows[j]) for j in range(1,m)}
        comaj=sum((m-j)*value for j,value in descent.items())
        for subset in low_subsets(kept,r,budget):
            left=D-comaj-sum(j-i+1 for i,j in subset)
            for beta in coins(tuple(range(2,m+1)),left):
                point={**{f'X{i}_{j}_{h}':int(tab[i,j]==h) for i,j in C for h in range(1,m+1)},
                       **{f'd{j}':descent[j] for j in descent},
                       **{f'Y{i}_{j}':int((i,j) in subset) for i,j in kept},
                       **{f'c{j}':beta[j-2] for j in range(2,m+1)}}
                result.append(point)
                if len(result)==needed:return tuple(result)
    raise AssertionError(('proved surjection requires more witnesses',m,base_a,r,nu,needed,len(result)))


def removed_points(m,a,r,nu):
    nu=tuple(nu);needed=target_multiplicities(m,r).get(nu,0)
    if not needed:return ()
    poly=stable.module_polytope(m,a,r,nu)
    if nu==(m,):
        assert needed==1 and r in (0,1)
        D=a+r;point={name:0 for name in poly['variables']};point['z2']=1
        if r==0:
            threes=D%2;point['b3']=threes;point['b2']=(D-3*threes)//2
        else:
            j=3 if D%2 else 4
            point[f'b{j}']=1;point[f'y{j}']=1;point['b2']=(D-j)//2
        points=(point,)
    else:
        base_a=5 if a%2 else 6
        points=tuple({**point,'c2':point['c2']+(a-base_a)//2}
                     for point in base_removed_points(m,base_a,r,nu))
    assert len(points)==needed
    assert len({tuple(p[v] for v in poly['variables']) for p in points})==needed
    assert all(stable.valid_witness(poly,point) for point in points),(m,a,r,nu,points)
    return points


def polytopes(m,a,r,t=0,mu=None):
    if mu is None:mu=(m,)
    mu=tuple(mu);lam,n,nu=parameters(m,a,r,t,mu)
    base=stable.module_polytope(m,a,r,nu);pieces=[base]
    deleted=removed_points(m,a,r,nu)
    for number,point in enumerate(deleted):
        owners=[i for i,piece in enumerate(pieces) if stable.valid_witness(piece,point)]
        assert len(owners)==1
        old=pieces.pop(owners[0]);prefix=[]
        for index,name in enumerate(old['variables']):
            for relation,step in (('<=',-1),('>=',1)):
                rows=old['constraints']+prefix+[{'coefficients':{name:1},'relation':relation,'rhs':point[name]+step}]
                pieces.append({'tag':{'deleted_point':number,'first_difference':index,'direction':relation},
                               'variables':old['variables'],'constraints':rows,
                               'variable_count':old['variable_count'],'constraint_count':len(rows)})
            prefix=prefix+[{'coefficients':{name:1},'relation':'=','rhs':point[name]}]
    assert len(pieces)==1+len(deleted)*(2*base['variable_count']-1)
    return {'statement':'T-063','partition':lam,'inner':n,'outer':mu,'effective_label':nu,
            'removed_points':deleted,'polytopes':pieces}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('m','a','r'):p.add_argument('--'+name,type=int,required=True)
    p.add_argument('--t',type=int,default=0);p.add_argument('--outer');p.add_argument('--polytopes',action='store_true')
    v=p.parse_args();mu=tuple(map(int,v.outer.split(','))) if v.outer else (v.m,)
    answer={'coefficient':coefficient(v.m,v.a,v.r,v.t,mu)}
    if v.polytopes:answer.update(polytopes(v.m,v.a,v.r,v.t,mu))
    print(json.dumps(answer,indent=2))


if __name__=='__main__':main()
