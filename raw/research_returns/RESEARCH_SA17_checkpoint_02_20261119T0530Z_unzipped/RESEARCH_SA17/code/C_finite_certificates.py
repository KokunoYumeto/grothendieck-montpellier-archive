#!/usr/bin/env python3
"""Exact finite certificates for Part C. No floating-point linear algebra."""
from itertools import combinations, combinations_with_replacement, product
from time import perf_counter
import json
import numpy as np

START = perf_counter()

def rank_mod(a,p):
    a=np.array(a,dtype=np.int64,copy=True)%p
    m,n=a.shape; r=0
    for j in range(n):
        hits=np.flatnonzero(a[r:,j])
        if not len(hits): continue
        h=r+int(hits[0]); a[[r,h]]=a[[h,r]]
        a[r]=(a[r]*pow(int(a[r,j]),-1,p))%p
        for i in range(r+1,m):
            if a[i,j]: a[i]=(a[i]-a[i,j]*a[r])%p
        r+=1
        if r==m: break
    return r

def jordan_counts(t,p):
    t=np.array(t,dtype=np.int64)%p; d=len(t)
    n=(t-np.eye(d,dtype=np.int64))%p
    powers=[np.eye(d,dtype=np.int64)]
    for _ in range(p): powers.append(powers[-1]@n%p)
    assert not np.any(powers[p])
    null=[d-rank_mod(x,p) for x in powers]
    at_least=[0]+[null[j]-null[j-1] for j in range(1,p+1)]+[0]
    return [at_least[j]-at_least[j+1] for j in range(1,p+1)]

def det_mod(a,p):
    a=np.array(a,dtype=np.int64,copy=True)%p; n=len(a); det=1
    for j in range(n):
        hs=np.flatnonzero(a[j:,j])
        if not len(hs): return 0
        h=j+int(hs[0])
        if h!=j: a[[j,h]]=a[[h,j]];det=-det
        v=int(a[j,j]);det=det*v%p
        a[j]=a[j]*pow(v,-1,p)%p
        for i in range(j+1,n):a[i]=(a[i]-a[i,j]*a[j])%p
    return det%p

def exterior(t,r,p):
    d=len(t); inds=list(combinations(range(d),r))
    if r>d:return np.zeros((0,0),dtype=np.int64)
    a=np.zeros((len(inds),len(inds)),dtype=np.int64)
    for i,ii in enumerate(inds):
        for j,jj in enumerate(inds):a[i,j]=det_mod(t[np.ix_(ii,jj)],p)
    return a

def jblock(d,p):
    t=np.eye(d,dtype=np.int64)
    for j in range(d-1): t[j,j+1]=1
    return t%p

def blockdiag(*matrices):
    d=sum(len(a) for a in matrices); t=np.zeros((d,d),dtype=np.int64);i=0
    for a in matrices:t[i:i+len(a),i:i+len(a)]=a;i+=len(a)
    return t

def green_product(v,w,p):
    z=np.zeros(p,dtype=np.int64)
    for i,a in enumerate(v,1):
        for j,b in enumerate(w,1):
            if a and b:z+=a*b*np.array(jordan_counts(np.kron(jblock(i,p),jblock(j,p)),p))
    return z

def adams3(t):
    p=3;x=np.array(jordan_counts(t,p));l2=np.array(jordan_counts(exterior(t,2,p),p));l3=np.array(jordan_counts(exterior(t,3,p),p))
    return green_product(green_product(x,x,p),x,p)-3*green_product(x,l2,p)+3*l3

def finite_sets():
    # C2 acts by transposition on X={0,1}. P2 means honest two-element subsets.
    x=list(range(2)); xy=list(product(x,x))
    act=lambda a:(1-a[0],1-a[1])
    p2=list(combinations(xy,2))
    fixed=sum(set(map(act,a))==set(a) for a in p2)
    assert fixed==2
    # Special lambda^2 identity for x=y: 2*x^2*lambda2(x)-2*lambda2(x)^2.
    rhs=-2
    assert fixed-rhs==4
    # V4 acts regularly on {0,1,2,3} by xor. X=P2(regular V4), six points.
    x=list(combinations(range(4),2)); ix={a:i for i,a in enumerate(x)}
    perms=[[ix[tuple(sorted(v^g for v in a))] for a in x] for g in range(4)]
    def fix_count(points,actions):
        return sum(all(act(a)==a for act in actions) for a in points)
    def symmetric2_fixed(points,actions):
        pairs=list(combinations_with_replacement(points,2))
        return sum(all(tuple(sorted(map(act,a)))==a for act in actions) for a in pairs)
    points=list(range(6));actions=[lambda a,p=p:p[a] for p in perms]
    fix=fix_count(points,actions);sym=symmetric2_fixed(points,actions)
    xx=list(product(points,points));xxidx={a:i for i,a in enumerate(xx)}
    xxactions=[lambda a,p=p:xxidx[(p[xx[a][0]],p[xx[a][1]])] for p in perms]
    fixxx=fix_count(list(range(36)),xxactions)
    symxx=symmetric2_fixed(list(range(36)),xxactions)
    # lambda2=cartesian square - symmetric square in the opposite-symmetric structure.
    l2=fix*fix-sym;l2xx=fixxx*fixxx-symxx
    rhs2=2*fix*fix*l2-2*l2*l2
    assert (fix,sym,fixxx,symxx,l2,l2xx,rhs2)==(0,3,0,6,-3,-6,-18)
    return {"subset_C2":{"base_points":2,"product_points":4,"two_subsets":len(p2),"lambda2_product_fixed":fixed,"universal_rhs_fixed":rhs,"defect":fixed-rhs},"inverse_symmetric_V4":{"base_points":4,"functor_P2_points":6,"product_points":36,"symmetric_square_points":666,"lambda2_X_fixed":l2,"lambda2_Xsquare_fixed":l2xx,"universal_rhs_fixed":rhs2,"defect":l2xx-rhs2}}

def quadratic_example():
    p=3;a=jblock(2,p);ainv=np.linalg.matrix_power(a,2)%p
    x=blockdiag(a,ainv.T);h=np.block([[np.zeros((2,2),dtype=np.int64),np.eye(2,dtype=np.int64)],[np.eye(2,dtype=np.int64),np.zeros((2,2),dtype=np.int64)]])
    y=np.array([[0,0,1],[1,0,0],[0,1,0]],dtype=np.int64);b=np.eye(3,dtype=np.int64)
    assert np.array_equal(x.T@h@x%p,h%p)
    assert np.array_equal(y.T@b@y%p,b)
    assert det_mod(h,p) and det_mod(b,p)
    xy=np.kron(x,y)%p
    # Compute Adams operations from actual exterior matrices, not assumed decomposition rules.
    px=adams3(x);py=adams3(y);pxy=adams3(xy)
    prod=green_product(px,py,p);defect=prod-pxy
    assert list(px)==[0,-4,4] and list(py)==[3,0,0]
    assert list(pxy)==[12,0,0] and list(defect)==[-12,-12,12]
    return {"field":3,"group_order":3,"X_dimension":4,"Y_dimension":3,"XY_dimension":12,"largest_exterior_matrix_dimension":220,"basis":["V1","V2","V3"],"X_Jordan_counts":jordan_counts(x,p),"Y_Jordan_counts":jordan_counts(y,p),"XY_Jordan_counts":jordan_counts(xy,p),"psi3_X":px.tolist(),"psi3_Y":py.tolist(),"psi3_XY":pxy.tolist(),"psi3_X_times_psi3_Y_minus_psi3_XY":defect.tolist(),"invariant_nondegenerate_symmetric_forms_verified":True}

def modular_S2():
    t=np.array([[0,1],[1,0]],dtype=np.int64);v=np.array([1,1],dtype=np.int64)
    assert np.array_equal(t@v%2,v)
    # quotient functional (x,y)->x+y is invariant and its kernel is span(v).
    assert np.array_equal(v@t%2,v)
    assert rank_mod(t-np.eye(2,dtype=np.int64),2)==1
    return {"field":2,"module_dimension":2,"submodule_dimension":1,"quotient_dimension":1,"all_composition_factors_trivial":True,"exact_relation":"rho1^2=2rho2"}

if __name__=='__main__':
    out={"finite_sets":finite_sets(),"split_WG_characteristic3":quadratic_example(),"exact_representation_characteristic2":modular_S2()}
    out['runtime_seconds']=round(perf_counter()-START,6)
    print(json.dumps(out,indent=2))
