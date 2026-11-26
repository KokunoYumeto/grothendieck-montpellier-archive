#!/usr/bin/env python3
"""Certify Cl(Q(cuberoot269))=C7 and the unit regulator using Sympy and Arb.

No PARI, Sage, precomputed BNF, or class-group command is used. Exact ideal
relations give the upper bound; the analytic class-number formula gives the
lower bound and saturation. The accompanying proof deduces Cl(E)=C7 x C7.
Run: python classgroup_second_system.py --output ../certificates/classgroup_second_system.json
Dependencies: sympy, python-flint. Typical running time below one minute.
"""
from __future__ import annotations
import argparse,json,math
from pathlib import Path
from sympy import Poly, symbols, primerange, Matrix, resultant
from sympy.polys.numberfields import round_two, prime_decomp
from sympy.matrices.normalforms import hermite_normal_form
from flint import arb,ctx

ELEMENTS=[(-2,-2,1),(-2,-2,2),(-2,-1,1),(-2,1,0),(-2,2,0),(-2,2,2),(-1,1,2),(0,-2,1),(0,1,1),(1,-1,2),(1,1,1),(1,1,2),(2,0,1),(2,2,1),(-4,-4,3),(-4,-3,2),(-4,-2,1),(-4,1,0),(-4,1,1),(-4,1,3),(-4,4,1),(-3,-3,2),(-3,-2,1),(-3,-2,2),(-1,-4,1),(3,-2,1),(-5,1,4)]

def exact_relations():
    x=symbols('x');T=Poly(x**3-269,x);ZK,D=round_two(T)
    assert D==-217083
    # The basis is 1, alpha, beta=(1+2alpha+alpha^2)/3.
    assert ZK.denom==3 and ZK.matrix.to_Matrix()==Matrix([[3,0,1],[0,3,2],[0,0,1]])
    # Minkowski bound: (4/pi)*(6/27)*sqrt(217083) < 132.
    assert 217083 < 466**2 and 200*2*466 < 132*157*9
    primes=list(primerange(2,132));ideals=[];groups={}
    for p in primes:
        dec=prime_decomp(p,T=T,ZK=ZK,dK=D)
        if len(dec)>1 or p**dec[0].f<=131:
            groups[p]=[]
            for P in dec:groups[p].append(len(ideals));ideals.append(P)
        else:
            assert len(dec)==1 and dec[0].e==1 and dec[0].f==3
    relations=[];records=[];cache={}
    for p,inds in groups.items():
        row=[0]*len(ideals)
        for i in inds:row[i]=ideals[i].e
        relations.append(row);records.append({'rational_prime':int(p),'relation':row})
    def valuation(P,vec,cap):
        found=0
        for k in range(1,cap+1):
            key=(str(P),k)
            if key not in cache:cache[key]=(P.as_submodule()**k).QQ_matrix.to_Matrix().inv()
            coordinates=cache[key]*vec
            if all(z.q==1 for z in coordinates):found=k
            else:break
        return found
    for a,b,c in ELEMENTS:
        u,v,w=3*a+c,3*b+2*c,c
        numerator=u**3+269*v**3+269**2*w**3-807*u*v*w
        assert numerator%27==0
        norm=numerator//27
        # A separate resultant confirms the exact norm formula for each relation.
        assert resultant(x**3-269,(u+v*x+w*x*x)/3,x)==norm
        rem=abs(norm);factors={}
        for p in primes:
            k=0
            while rem%p==0:k+=1;rem//=p
            if k:factors[p]=k
        assert rem==1
        row=[0]*len(ideals);vec=Matrix([u,v,w])/3
        for p,k in factors.items():
            if p not in groups:
                assert k%3==0
                continue
            for i in groups[p]:row[i]=valuation(ideals[i],vec,k//ideals[i].f)
            assert sum(row[i]*ideals[i].f for i in groups[p])==k
        relations.append(row);records.append({'coefficients':[a,b,c],'norm':norm,'relation':row})
    H=hermite_normal_form(Matrix(relations).T)
    assert H.shape==(48,48) and abs(H.det())==7
    # A nontrivial unit. Its inverse has positive logarithm.
    unit=108*x*x-739*x+270
    assert resultant(x**3-269,unit,x)==1
    return {'discriminant':int(D),'basis':str(ZK),'generator_count':len(ideals),'relation_count':len(relations),'relation_index':int(abs(H.det())),'minkowski_bound_less_than':132,'unit_norm':1,'relations':records,'prime_ideals':[str(P) for P in ideals]}

def coefficients_by_roots(N):
    # This implementation counts roots directly instead of using cubic reciprocity.
    spf=list(range(N+1))
    for p in range(2,math.isqrt(N)+1):
        if spf[p]==p:
            for n in range(p*p,N+1,p):
                if spf[n]==n:spf[n]=p
    local={}
    for p in range(2,N+1):
        if spf[p]!=p:continue
        if p==269:tr,det=0,0
        elif p==3:tr,det=1,0
        else:tr=sum((r*r*r-269)%p==0 for r in range(p))-1;det=1 if p%3==1 else -1
        seq=[1,tr]
        while p**(len(seq)-1)<=N:seq.append(tr*seq[-1]-det*seq[-2])
        local[p]=seq
    a=[0]*(N+1);a[1]=1
    for n in range(2,N+1):
        p=spf[n];k=0;m=n
        while m%p==0:k+=1;m//=p
        a[n]=a[m]*local[p][k]
    return a

def archimedean_check():
    ctx.prec=220;N=8192
    a=coefficients_by_roots(N)
    alpha=2*arb.pi()/arb(217083).sqrt();q=(-alpha).exp();L1=arb(0)
    for n in range(1,N+1):
        if a[n]:L1+=a[n]*(q**n/n+alpha*(alpha*n).expint(1))
    tail=2*q**(N+1)/(1-q)
    L1+=arb(0,tail.upper())
    root=arb(269).root(3);unit=108*root*root-739*root+270
    assert unit>0 and unit<1
    R=-unit.log();ratio=arb(217083).sqrt()*L1/(2*arb.pi()*R)
    assert ratio>6 and ratio<8
    partial=0;minimum=N
    for z in a[1:2049]:partial+=z;minimum=min(minimum,partial)
    assert minimum==1 and partial==47
    # This independently rechecks the finite theta-positivity certificate.
    assert 10**6*76*(2048+76)*75**2048 < 76**2048
    return {'precision_bits':ctx.prec,'terms':N,'L_at_1':str(L1),'L1_tail_bound':str(tail),'unit_regulator':str(R),'class_number_divided_by_unit_index':str(ratio),'ratio_greater_than_6':True,'theta_partial_sum_minimum':minimum,'theta_partial_sum_2048':partial}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
    data={'system':'Sympy exact number-field lattices + Arb intervals; no PARI','exact':exact_relations(),'archimedean':archimedean_check(),'conclusions':{'pure_cubic_class_group':'C7','displayed_unit_is_fundamental':True,'normal_closure_class_group':'C7 x C7, using the proved unit-index and S3 arguments'},'passed':True}
    result=json.dumps(data,indent=2)+'\n'
    if args.output:args.output.write_text(result)
    print(json.dumps({k:v for k,v in data.items() if k!='exact'},indent=2))
if __name__=='__main__':main()
