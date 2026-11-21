"""T067: all valid hook tails at every fixed positive ideal order.

Every correction is evaluated through the finite exact restriction complex.
The only highest-space calculations have rank and degree bounded by k.
"""
from pathlib import Path
from functools import lru_cache
from itertools import permutations,product,combinations
from collections import Counter,defaultdict
from fractions import Fraction
from math import comb,factorial
import sys,argparse,json

sys.path.insert(0,str(Path(__file__).resolve().parent))
import fixed_order_hook_positive as fixed
stable=fixed.stable


@lru_cache(None)
def compositions(total,rank):
    if rank==0:return ((),) if total==0 else ()
    return tuple((first,)+rest for first in range(total+1)
                 for rest in compositions(total-first,rank-1))


def parity(permutation):
    return -1 if sum(permutation[i]>permutation[j]
                     for i in range(len(permutation)) for j in range(i+1,len(permutation)))%2 else 1


@lru_cache(None)
def alternant_shifts(rank):
    delta=tuple(range(rank-1,-1,-1))
    return tuple((parity(p),tuple(delta[i]-delta[p[i]] for i in range(rank)))
                 for p in permutations(range(rank)))


def schur_coefficient(polynomial,shape,rank):
    shape=tuple(shape)+(0,)*(rank-len(shape))
    assert len(shape)==rank
    return sum(sign*polynomial.get(tuple(shape[i]+shift[i] for i in range(rank)),0)
               for sign,shift in alternant_shifts(rank))


@lru_cache(None)
def normal_polynomial(q,k,cycles):
    states={(0,)*q:1}
    monomials=tuple(v for degree in range(k) for v in compositions(degree,q))
    for ell in cycles:
        updated=defaultdict(int)
        for current,value in states.items():
            for exponent in monomials:
                new=tuple(current[i]+ell*exponent[i] for i in range(q))
                updated[new]+=value
        states=dict(updated)
    return states


@lru_cache(None)
def normal_trace(q,k,rho,cycles):
    return schur_coefficient(normal_polynomial(q,k,cycles),rho,q)


@lru_cache(None)
def small_character(shape,cycles):
    q=sum(shape);states={(0,)*q:1}
    for ell in cycles:
        updated=defaultdict(int)
        for current,value in states.items():
            for i in range(q):
                exponent=list(current);exponent[i]+=ell
                updated[tuple(exponent)]+=value
        states=dict(updated)
    return schur_coefficient(states,shape,q)


def class_centralizer(cycles):
    answer=1
    for ell,count in Counter(cycles).items():answer*=ell**count*factorial(count)
    return answer


@lru_cache(None)
def normal_multiplicities(q,k,rho):
    answer=[]
    for eta in fixed.partitions(q):
        value=sum(Fraction(small_character(eta,cycles)*normal_trace(q,k,rho,cycles),
                           class_centralizer(cycles)) for cycles in fixed.partitions(q))
        assert value.denominator==1 and value>=0
        if value:answer.append((eta,int(value)))
    return tuple(answer)


@lru_cache(None)
def decorated_permutation_induction(m,eta,j,leg,nu):
    """Ind_{S_q x S_L}: eta tensor Sym^j(Q^L) tensor exterior^leg h_L."""
    if j<0:return 0
    q=sum(eta);L=m-q
    if not 0<=leg<=L-1:return 0
    answer=0
    for orbit in fixed.partitions(j):
        p=len(orbit)
        if p>L:continue
        small=tuple(Counter(orbit)[d] for d in sorted(set(orbit)))
        large=L-p
        for legs in product(*(range(size) for size in small)):
            factors=tuple(fixed.hook(size,s) for size,s in zip(small,legs))+(eta,)
            if large:
                blocks=1+len(small)
                for e in range(blocks):
                    bigleg=leg-e-sum(legs)
                    if 0<=bigleg<large:
                        answer+=comb(blocks-1,e)*fixed.product_coefficient(
                            nu,fixed.hook(large,bigleg),factors)
            else:
                blocks=len(small);e=leg-sum(legs)
                if 0<=e<blocks:
                    answer+=comb(blocks-1,e)*fixed.product_coefficient(nu,(),factors)
    return answer


@lru_cache(None)
def decorated_standard_induction(m,eta,A,leg,nu):
    value=(decorated_permutation_induction(m,eta,A,leg,nu)
           -decorated_permutation_induction(m,eta,A-1,leg,nu))
    assert value>=0
    return value


@lru_cache(None)
def complex_multiplicities(m,k,a,r,nu):
    """All nonambient terms of the actual alpha restriction complex."""
    assert a>k
    bound=min(m-2,(a-1)//(a-k))
    assert bound<=k
    terms=[]
    for q in range(1,bound+1):
        value=0
        for s in range(min(q-1,r)+1):
            leg=r-s
            if leg>m-q-1:continue
            maximum=min(a-1,q*(k-1)-(q-1)*a+s)
            assert maximum<=k-q
            for A in range(maximum+1):
                rho=(a,)*(q-s-1)+(a-1,)*s+((A,) if A else ())
                assert sum(rho)<=q*(k-1) and len(rho)<=q
                for eta,multiplicity in normal_multiplicities(q,k,rho):
                    effective=stable.transpose(eta) if a%2==0 else eta
                    value+=multiplicity*decorated_standard_induction(m,effective,A,leg,nu)
        terms.append(value)
    assert terms[0]==fixed.jet_multiplicity(m,k,r,nu)
    return tuple(terms)


def parameters(m,k,a,r,t,mu):
    mu=tuple(mu)
    if any(type(v)is not int for v in (m,k,a,r,t)) or m<4 or k<1 or a<1 or t<0:
        raise ValueError('require m>=4,k>=1,a>=1,t>=0')
    if not 0<=r<=m-2 or (m-2)*a<m*k+r:
        raise ValueError('require 0<=r<=m-2 and (m-2)a>=mk+r')
    if not stable.valid_partition(mu,m):raise ValueError('outer label must partition m')
    assert a>k
    n=a+t-k;lam=((m-1)*a+t-m*k-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
    assert lam[0]>=lam[1] and sum(lam)==m*n
    return lam,n,stable.transpose(mu) if t%2 else mu


def correction(m,k,a,r,nu):
    terms=complex_multiplicities(m,k,a,r,tuple(nu))
    value=sum((-1)**i*v for i,v in enumerate(terms))
    assert 0<=value<=terms[0]<=fixed.correction_bound(k)
    return value


def coefficient(m,k,a,r,t=0,mu=None):
    if mu is None:mu=(m,)
    _,_,nu=parameters(m,k,a,r,t,mu)
    value=stable.module_coefficient(m,a,r,nu)-correction(m,k,a,r,nu)
    assert value>=0
    return value


@lru_cache(None)
def removed_points(m,k,a,r,nu):
    wanted=correction(m,k,a,r,nu)
    if not wanted:return ()
    if a>=2*k+1:return fixed.removed_points(m,k,a,r,nu)
    D=a+r;answer=[]
    if nu==(m,):
        for beta in fixed.coins(tuple(range(2,min(m,D)+1)),D):
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
        raise AssertionError(('row enumeration incomplete',m,k,a,r,nu,wanted,len(answer)))
    cells=stable.cells(nu);kept=tuple(c for c in cells if c not in ((1,1),(2,1)))
    lowest=sum(i*v for i,v in enumerate(nu))+sum(sorted(j-i+1 for i,j in kept)[:r])
    budget=D-lowest
    assert 0<=budget<=a-1<=2*k-1
    assert max(Counter(j-i for i,j in cells).values())<=k+1
    for raw in fixed.low_comajor_tableaux(nu,budget):
        tab=dict(zip(cells,raw));rows={label:c[0] for c,label in tab.items()}
        desc={j:int(rows[j+1]>rows[j]) for j in range(1,m)}
        comaj=sum((m-j)*v for j,v in desc.items())
        for subset in fixed.bounded_subsets(kept,r,budget,k+1):
            left=D-comaj-sum(j-i+1 for i,j in subset)
            for beta in fixed.coins(tuple(range(2,m+1)),left):
                point={**{f'X{i}_{j}_{h}':int(tab[i,j]==h) for i,j in cells for h in range(1,m+1)},
                       **{f'd{j}':desc[j] for j in desc},
                       **{f'Y{i}_{j}':int((i,j) in subset) for i,j in kept},
                       **{f'c{j}':beta[j-2] for j in range(2,m+1)}}
                answer.append(point)
                if len(answer)==wanted:return tuple(answer)
    raise AssertionError(('nonrow enumeration incomplete',m,k,a,r,nu,wanted,len(answer)))


def polytopes(m,k,a,r,t=0,mu=None):
    if mu is None:mu=(m,)
    mu=tuple(mu);lam,n,nu=parameters(m,k,a,r,t,mu)
    base=stable.module_polytope(m,a,r,nu);pieces=[base]
    points=removed_points(m,k,a,r,nu)
    assert all(stable.valid_witness(base,p) for p in points)
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
    return {'statement':'T-067','partition':lam,'inner':n,'outer':mu,'effective_label':nu,
            'ideal_order':k,'complex_multiplicities':complex_multiplicities(m,k,a,r,nu),
            'correction':len(points),'uniform_correction_bound':fixed.correction_bound(k),
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
