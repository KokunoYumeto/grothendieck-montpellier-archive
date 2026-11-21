"""T065: the closed a=2k endpoint of fixed-order hook plethysm."""
from pathlib import Path
import sys,argparse,json

sys.path.insert(0,str(Path(__file__).resolve().parent))
import fixed_order_hook_positive as fixed
stable=fixed.stable


def parameters(m,k,r,t,mu):
    mu=tuple(mu)
    if any(type(v)is not int for v in (m,k,r,t)) or m<4 or k<1 or t<0 or not 0<=r<=min(m-2,(m-4)*k):
        raise ValueError('require m>=4,k>=1,t>=0,0<=r<=min(m-2,(m-4)k)')
    if not stable.valid_partition(mu,m):raise ValueError('outer label must partition m')
    lam=((m-2)*k+t-r,2*k+t)+(t+1,)*r+(t,)*(m-2-r)
    n=k+t
    assert lam[0]>=lam[1] and sum(lam)==m*n
    return lam,n,stable.transpose(mu) if t%2 else mu


def coefficient(m,k,r,t=0,mu=None):
    if mu is None:mu=(m,)
    _,_,nu=parameters(m,k,r,t,mu)
    value=stable.module_coefficient(m,2*k,r,nu)-fixed.jet_multiplicity(m,k,r,nu)
    assert value>=0
    return value


def polytopes(m,k,r,t=0,mu=None):
    if mu is None:mu=(m,)
    mu=tuple(mu);lam,n,nu=parameters(m,k,r,t,mu)
    base=stable.module_polytope(m,2*k,r,nu);pieces=[base]
    count=fixed.jet_multiplicity(m,k,r,nu)
    points=fixed.base_points(m,k,2*k,r,nu) if count else ()
    assert len(points)==count and all(stable.valid_witness(base,p) for p in points)
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
    assert len(pieces)==1+count*(2*base['variable_count']-1)
    return {'statement':'T-065','partition':lam,'inner':n,'outer':mu,'effective_label':nu,
            'ideal_order':k,'correction':count,'removed_points':points,'polytopes':pieces}


def full_coefficient(m,k,a,r,t=0,mu=None):
    if a==2*k:return coefficient(m,k,r,t,mu)
    return fixed.coefficient(m,k,a,r,t,mu)


def full_polytopes(m,k,a,r,t=0,mu=None):
    if a==2*k:return polytopes(m,k,r,t,mu)
    return fixed.polytopes(m,k,a,r,t,mu)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('m','k','r'):p.add_argument('--'+name,type=int,required=True)
    p.add_argument('--t',type=int,default=0);p.add_argument('--outer');p.add_argument('--polytopes',action='store_true')
    v=p.parse_args();mu=tuple(map(int,v.outer.split(','))) if v.outer else (v.m,)
    answer={'coefficient':coefficient(v.m,v.k,v.r,v.t,mu)}
    if v.polytopes:answer.update(polytopes(v.m,v.k,v.r,v.t,mu))
    print(json.dumps(answer,indent=2))


if __name__=='__main__':main()

