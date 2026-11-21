"""T064: positive fixed-order hook plethysm in the explicit jet range."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations,product
from collections import Counter
from math import comb,factorial
import sys,argparse,json

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'root'))
import stable_hook_positive as stable
from second_unstable_hook_positive import low_comajor_tableaux,coins


def partitions(n,maximum=None):
    if n==0:
        yield ();return
    if maximum is None:maximum=n
    for first in range(min(n,maximum),1-1,-1):
        for rest in partitions(n-first,first):yield (first,)+rest


def inside(inner,outer):
    return len(inner)<=len(outer) and all(a<=outer[i] for i,a in enumerate(inner))


@lru_cache(None)
def lr(outer,inner,weight):
    """Literal LR tableaux; the skew shape has at most k cells in this use."""
    if not inside(inner,outer) or sum(outer)-sum(inner)!=sum(weight):return 0
    cells=[(i,j) for i,a in enumerate(outer,1)
           for j in range(a,inner[i-1] if i<=len(inner) else 0,-1)]
    used=[0]*len(weight);filled={}
    def visit(pos):
        if pos==len(cells):return 1
        i,j=cells[pos];answer=0
        lower=filled.get((i-1,j),0)+1
        upper=filled.get((i,j+1),len(weight))
        for value in range(lower,upper+1):
            h=value-1
            if used[h]==weight[h] or (h and used[h]+1>used[h-1]):continue
            used[h]+=1;filled[i,j]=value
            answer+=visit(pos+1)
            used[h]-=1
        filled.pop((i,j),None)
        return answer
    return visit(0)


@lru_cache(None)
def intermediate_shapes(inner,outer,size):
    if not inside(inner,outer) or not sum(inner)<=size<=sum(outer):return ()
    lower=inner+(0,)*(len(outer)-len(inner));result=[];prefix=[]
    suffix=[0]*(len(outer)+1)
    for i in range(len(outer)-1,-1,-1):suffix[i]=suffix[i+1]+lower[i]
    def visit(i,left,previous):
        if i==len(outer):
            if not left:
                shape=tuple(prefix)
                while shape and not shape[-1]:shape=shape[:-1]
                result.append(shape)
            return
        hi=min(outer[i],previous,left-suffix[i+1])
        for value in range(lower[i],hi+1):
            prefix.append(value);visit(i+1,left-value,value);prefix.pop()
    visit(0,size,size)
    return tuple(result)


@lru_cache(None)
def product_coefficient(nu,base,factors):
    if not inside(base,nu):return 0
    states={base:1}
    for factor in factors:
        updated={}
        for current,coefficient in states.items():
            for shape in intermediate_shapes(current,nu,sum(current)+sum(factor)):
                mult=lr(shape,current,factor)
                if mult:updated[shape]=updated.get(shape,0)+coefficient*mult
        states=updated
    return states.get(nu,0)


def hook(size,leg):
    assert size>=1 and 0<=leg<size
    return (size-leg,)+(1,)*leg


@lru_cache(None)
def jet_multiplicity(m,k,r,nu):
    """Positive monomial-orbit / restricted-exterior / bounded LR formula."""
    N=m-1;answer=0
    for rho in partitions(k-1):
        p=len(rho)
        if p>N:continue
        small=tuple(Counter(rho)[d] for d in sorted(set(rho)))
        large=N-p
        for legs in product(*(range(n) for n in small)):
            smallhooks=tuple(hook(n,s) for n,s in zip(small,legs))+((1,),)
            if large:
                blocks=1+len(small)
                for exterior_trivial in range(blocks):
                    bigleg=r-exterior_trivial-sum(legs)
                    if 0<=bigleg<large:
                        answer+=comb(blocks-1,exterior_trivial)*product_coefficient(
                            nu,hook(large,bigleg),smallhooks)
            else:
                blocks=len(small)
                exterior_trivial=r-sum(legs)
                if 0<=exterior_trivial<blocks:
                    answer+=comb(blocks-1,exterior_trivial)*product_coefficient(nu,(),smallhooks)
    return answer


def correction_bound(k):
    row=[1]
    for n in range(1,k):
        row=[0]+[ (row[p-1] if p-1<len(row) else 0)+
                  p*(row[p] if p<len(row) else 0) for p in range(1,n+1)]
    return sum(value*2**p*factorial(p+1) for p,value in enumerate(row))


def parameters(m,k,a,r,t,mu):
    mu=tuple(mu)
    if any(type(v)is not int for v in (m,k,a,r,t)) or m<4 or k<1 or a<2*k+1 or not 0<=r<=m-2 or t<0:
        raise ValueError('require m>=4,k>=1,a>=2k+1,0<=r<=m-2,t>=0')
    if not stable.valid_partition(mu,m):raise ValueError('outer label must partition m')
    n=a+t-k
    lam=((m-1)*a+t-m*k-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
    assert lam[0]>=lam[1] and sum(lam)==m*n
    return lam,n,stable.transpose(mu) if t%2 else mu


def coefficient(m,k,a,r,t=0,mu=None):
    if mu is None:mu=(m,)
    _,_,nu=parameters(m,k,a,r,t,mu)
    value=stable.module_coefficient(m,a,r,nu)-jet_multiplicity(m,k,r,nu)
    assert value>=0
    return value


def bounded_subsets(cells,r,budget,width):
    weights=sorted((j-i+1,(i,j)) for i,j in cells)
    if r==0:
        yield ();return
    if r==len(cells):
        yield tuple(cells);return
    low=sum(w for w,_ in weights[:r]);cut=weights[r-1][0]
    forced=tuple(c for w,c in weights if w<cut-budget)
    middle=tuple(c for w,c in weights if cut-budget<=w<=cut+budget)
    assert len(middle)<=(2*budget+1)*width
    for choice in combinations(middle,r-len(forced)):
        chosen=forced+choice
        if sum(j-i+1 for i,j in chosen)-low<=budget:yield chosen


@lru_cache(None)
def base_points(m,k,a0,r,nu):
    wanted=jet_multiplicity(m,k,r,nu);assert wanted
    D=a0+r
    if nu==(m,):
        answer=[]
        for beta in coins(tuple(range(2,min(m,D)+1)),D):
            beta=beta+(0,)*(m-1-len(beta))
            support=[j for j in range(2,m+1) if beta[j-2]]
            if not support:continue
            least=support[0]
            for subset in combinations(support[1:],r):
                point={**{f'z{j}':int(j==least) for j in range(2,m+1)},
                       **{f'y{j}':int(j in subset) for j in range(2,m+1)},
                       **{f'b{j}':beta[j-2] for j in range(2,m+1)}}
                answer.append(point)
                if len(answer)==wanted:return tuple(answer)
        raise AssertionError(('row enumeration incomplete',m,k,a0,r,wanted,len(answer)))
    C=stable.cells(nu);kept=tuple(c for c in C if c not in ((1,1),(2,1)))
    lowest=sum(i*v for i,v in enumerate(nu))+sum(sorted(j-i+1 for i,j in kept)[:r])
    budget=D-lowest
    assert 0<=budget<=2*k+1
    diagonal=Counter(j-i for i,j in C)
    assert max(diagonal.values())<=k+1
    answer=[]
    for raw in low_comajor_tableaux(nu,budget):
        tab=dict(zip(C,raw));rows={label:c[0] for c,label in tab.items()}
        desc={j:int(rows[j+1]>rows[j]) for j in range(1,m)}
        comaj=sum((m-j)*v for j,v in desc.items())
        for subset in bounded_subsets(kept,r,budget,k+1):
            left=D-comaj-sum(j-i+1 for i,j in subset)
            for beta in coins(tuple(range(2,m+1)),left):
                point={**{f'X{i}_{j}_{h}':int(tab[i,j]==h) for i,j in C for h in range(1,m+1)},
                       **{f'd{j}':desc[j] for j in desc},
                       **{f'Y{i}_{j}':int((i,j) in subset) for i,j in kept},
                       **{f'c{j}':beta[j-2] for j in range(2,m+1)}}
                answer.append(point)
                if len(answer)==wanted:return tuple(answer)
    raise AssertionError(('nonrow enumeration incomplete',m,k,a0,r,nu,wanted,len(answer)))


def removed_points(m,k,a,r,nu):
    nu=tuple(nu);wanted=jet_multiplicity(m,k,r,nu)
    if not wanted:return ()
    a0=2*k+1+(a%2==0)
    shift=(a-a0)//2;answer=[]
    for original in base_points(m,k,a0,r,nu):
        point=dict(original)
        if nu==(m,):
            point['b2']+=shift
            if shift:
                for j in range(2,m+1):point[f'z{j}']=int(j==2)
        else:point['c2']+=shift
        answer.append(point)
    P=stable.module_polytope(m,a,r,nu)
    assert len(answer)==wanted and len({tuple(p[v] for v in P['variables']) for p in answer})==wanted
    assert all(stable.valid_witness(P,p) for p in answer)
    return tuple(answer)


def polytopes(m,k,a,r,t=0,mu=None):
    if mu is None:mu=(m,)
    mu=tuple(mu);lam,n,nu=parameters(m,k,a,r,t,mu)
    base=stable.module_polytope(m,a,r,nu);pieces=[base]
    points=removed_points(m,k,a,r,nu)
    for number,point in enumerate(points):
        owners=[i for i,P in enumerate(pieces) if stable.valid_witness(P,point)]
        assert len(owners)==1
        old=pieces.pop(owners[0]);prefix=[]
        for index,name in enumerate(old['variables']):
            for relation,step in (('<=',-1),('>=',1)):
                rows=old['constraints']+prefix+[{'coefficients':{name:1},'relation':relation,'rhs':point[name]+step}]
                pieces.append({'tag':{'deleted_point':number,'first_difference':index,'direction':relation},
                               'variables':old['variables'],'constraints':rows,'variable_count':old['variable_count'],
                               'constraint_count':len(rows)})
            prefix=prefix+[{'coefficients':{name:1},'relation':'=','rhs':point[name]}]
    assert len(pieces)==1+len(points)*(2*base['variable_count']-1)
    return {'statement':'T-064','partition':lam,'inner':n,'outer':mu,'effective_label':nu,
            'ideal_order':k,'correction':len(points),'uniform_correction_bound':correction_bound(k),
            'removed_points':points,'polytopes':pieces}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('m','k','a','r'):p.add_argument('--'+name,type=int,required=True)
    p.add_argument('--t',type=int,default=0);p.add_argument('--outer');p.add_argument('--polytopes',action='store_true')
    v=p.parse_args();mu=tuple(map(int,v.outer.split(','))) if v.outer else (v.m,)
    answer={'coefficient':coefficient(v.m,v.k,v.a,v.r,v.t,mu)}
    if v.polytopes:answer.update(polytopes(v.m,v.k,v.a,v.r,v.t,mu))
    print(json.dumps(answer,indent=2))


if __name__=='__main__':main()

