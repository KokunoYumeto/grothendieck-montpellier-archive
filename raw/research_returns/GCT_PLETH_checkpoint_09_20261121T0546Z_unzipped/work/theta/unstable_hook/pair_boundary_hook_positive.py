"""T066: positive hook plethysm at a=2k-1 via the exact pair complex."""
from pathlib import Path
from functools import lru_cache
from itertools import combinations
from collections import Counter
import sys,argparse,json

sys.path.insert(0,str(Path(__file__).resolve().parent))
import fixed_order_hook_positive as fixed
import endpoint_hook_positive as endpoint
stable=fixed.stable


def parameters(m,k,r,t,mu):
    mu=tuple(mu)
    if any(type(v)is not int for v in (m,k,r,t)) or m<4 or k<2 or t<0:
        raise ValueError('require m>=4,k>=2,t>=0')
    if not 0<=r<=min(m-2,(m-4)*k-(m-2)):
        raise ValueError('require 0<=r<=min(m-2,(m-4)k-(m-2))')
    if not stable.valid_partition(mu,m):raise ValueError('outer label must partition m')
    a=2*k-1;n=k-1+t
    lam=((m-1)*a+t-m*k-r,a+t)+(t+1,)*r+(t,)*(m-2-r)
    assert lam[0]>=lam[1] and sum(lam)==m*n
    return lam,n,stable.transpose(mu) if t%2 else mu


@lru_cache(None)
def pair_multiplicity(m,r,nu):
    if r==0:return 0
    answer=fixed.lr(tuple(nu),fixed.hook(m-2,r-1),(2,))
    assert answer in (0,1)
    return answer


def correction(m,k,r,nu):
    answer=fixed.jet_multiplicity(m,k,r,tuple(nu))-pair_multiplicity(m,r,tuple(nu))
    assert 0<=answer<=fixed.correction_bound(k)
    return answer


def coefficient(m,k,r,t=0,mu=None):
    if mu is None:mu=(m,)
    _,_,nu=parameters(m,k,r,t,mu)
    answer=stable.module_coefficient(m,2*k-1,r,nu)-correction(m,k,r,nu)
    assert answer>=0
    return answer


@lru_cache(None)
def removed_points(m,k,r,nu):
    wanted=correction(m,k,r,nu)
    if not wanted:return ()
    a=2*k-1;D=a+r;answer=[]
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
        raise AssertionError(('row enumeration incomplete',m,k,r,nu,wanted,len(answer)))
    cells=stable.cells(nu);kept=tuple(c for c in cells if c not in ((1,1),(2,1)))
    lowest=sum(i*v for i,v in enumerate(nu))+sum(sorted(j-i+1 for i,j in kept)[:r])
    budget=D-lowest
    assert 0<=budget<=2*k-2
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
    raise AssertionError(('nonrow enumeration incomplete',m,k,r,nu,wanted,len(answer)))


def polytopes(m,k,r,t=0,mu=None):
    if mu is None:mu=(m,)
    mu=tuple(mu);lam,n,nu=parameters(m,k,r,t,mu)
    base=stable.module_polytope(m,2*k-1,r,nu);pieces=[base]
    points=removed_points(m,k,r,nu)
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
    return {'statement':'T-066','partition':lam,'inner':n,'outer':mu,'effective_label':nu,
            'ideal_order':k,'jet_multiplicity':fixed.jet_multiplicity(m,k,r,nu),
            'pair_multiplicity':pair_multiplicity(m,r,nu),'correction':len(points),
            'removed_points':points,'polytopes':pieces}


def full_coefficient(m,k,a,r,t=0,mu=None):
    if a==2*k-1:return coefficient(m,k,r,t,mu)
    return endpoint.full_coefficient(m,k,a,r,t,mu)


def full_polytopes(m,k,a,r,t=0,mu=None):
    if a==2*k-1:return polytopes(m,k,r,t,mu)
    return endpoint.full_polytopes(m,k,a,r,t,mu)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('m','k','r'):p.add_argument('--'+name,type=int,required=True)
    p.add_argument('--t',type=int,default=0);p.add_argument('--outer');p.add_argument('--polytopes',action='store_true')
    v=p.parse_args();mu=tuple(map(int,v.outer.split(','))) if v.outer else (v.m,)
    answer={'coefficient':coefficient(v.m,v.k,v.r,v.t,mu)}
    if v.polytopes:answer.update(polytopes(v.m,v.k,v.r,v.t,mu))
    print(json.dumps(answer,indent=2))


if __name__=='__main__':main()
