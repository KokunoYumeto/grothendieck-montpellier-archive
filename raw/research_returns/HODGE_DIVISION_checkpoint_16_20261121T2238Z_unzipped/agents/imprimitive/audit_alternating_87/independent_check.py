#!/usr/bin/env python3
"""Independent exact polynomial/content audit of HD-ALT-06a/b."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial,prod
import re,json,time,hashlib
t0=time.perf_counter()
# Sparse rational bivariate polynomials in n,k.
def add(p,q):
    r=dict(p)
    for x,a in q.items():
        r[x]=r.get(x,F(0))+a
        if not r[x]:del r[x]
    return r
def sc(p,a):return {x:a*b for x,b in p.items() if a*b}
def sub(p,q):return add(p,sc(q,-1))
def mul(p,q):
    r={}
    for (i,j),a in p.items():
        for (k,l),b in q.items():
            z=(i+k,j+l);r[z]=r.get(z,F(0))+a*b
    return {x:a for x,a in r.items() if a}
def der(p,v):
    r={}
    for powers,a in p.items():
        if powers[v]:
            b=list(powers);b[v]-=1;r[tuple(b)]=a*powers[v]
    return r
def powp(p,n):
    r={(0,0):F(1)}
    for _ in range(n):r=mul(r,p)
    return r
def subst(p,v,q):
    r={}
    for powers,a in p.items():
        mon=list(powers);expo=mon[v];mon[v]=0
        r=add(r,mul({tuple(mon):a},powp(q,expo)))
    return r
one={(0,0):F(1)};n={(1,0):F(1)};k={(0,1):F(1)}
nm1=sub(n,one);nm2=sub(n,sc(one,2));nm3=sub(n,sc(one,3))
m=sub(n,k)
T=sub(sc(mul(n,nm1),F(1,2)),mul(k,add(m,one)))
S0=sc(mul(mul(m,sub(m,one)),sub(sc(m,2),one)),F(1,6))
N=sub(add(mul(T,T),mul(n,nm1)),sc(S0,3))
derivative=add(sc(mul(T,sub(add(n,one),sc(k,2))),-2),
               add(sub(sc(mul(m,m),3),sc(m,3)),sc(one,F(1,2))))
assert der(N,1)==derivative
assert sub(T,sc(mul(n,sub(sub(n,sc(k,2)),one)),F(1,2)))==mul(k,sub(k,one))
c=F(13,100);A=1-2*c+2*c*c;delta=(1-A*A)/4
assert A==F(3869,5000) and delta==F(10030839,100000000)
unumer=sub(mul(sc(n,c),sub(nm1,sc(n,c))),sc(mul(nm1,nm2),c*(1-c)))
assert unumer==sc(sub(sc(n,161),sc(one,174)),F(13,10000))
den=mul(mul(n,nm1),mul(nm2,nm3))
vnum=sub(sc(den,A*A),sc(subst(N,1,sc(n,c)),4))
P=add(sub(sc(mul(n,n),1906518),sc(n,6812633)),sc(one,4129618))
assert vnum==sc(mul(n,P),F(13,25000000))
shift=subst(P,0,add(n,sc(one,15)))
assert shift=={(2,0):F(1906518),(1,0):F(50382907),(0,0):F(330906673)}
derivmajorant=sub(sc(mul(mul(n,n),sub(n,sc(one,14))),F(1,4)),sc(one,F(1,2)))
assert all(v>0 for v in subst(derivmajorant,0,add(n,sc(one,15))).values())
assert c*(1-c)==F(1131,10000)>delta>F(1,10)
assert 6/(10*delta-1)==F(60000000,30839)<2000
assert F(2*30**3,27)==2000
path=Path('HODGE_DIVISION_work/research/ordinary_alternating_87_section.tex')
tex=path.read_text()
frozen='5ab4d6447f1b04c0d5c3b52afc5dbaf1a5450cd1d388034d51e3cd68f251cd79'
assert hashlib.sha256(tex.encode()).hexdigest()==frozen
printed={int(n):(int(k),F(int(a),int(b))) for n,k,a,b in re.findall(r'(\d+)&(\d+)&(\d+)/(\d+)',tex)}
assert set(printed)==set(range(15,30))
rows=[]
def estimates(n,k):
    T=F(n*(n-1),2)-k*(n-k+1)
    S0=sum(j*j for j in range(n-k))
    V=F(4*(T*T+n*(n-1)-3*S0),n*(n-1)*(n-2)*(n-3))
    f=F(k*(n-1-k),(n-1)*(n-2))
    return T,S0,V,f,min(F(1,4),f,(1-V)/4)
for n,(k,want) in sorted(printed.items()):
    assert k==(13*n+99)//100 and k<F(n,4)
    got=estimates(n,k)[-1]
    assert got==want and got>F(1,9)
    rows.append({'n':n,'k0':k,'delta':str(got)})
assert 6/(10*F(1,9)-1)==54<90
assert F(19)>F(6*22,7) and F(19)<=F(87*22,100)

def parts(n,maximum=None):
    if n==0:
        yield ();return
    for first in range(min(n,maximum or n),0,-1):
        for tail in parts(n-first,first):yield (first,)+tail
shape_count=0
min_degree=None
for nn in range(15,41):
    for kk in range((13*nn+99)//100,(nn-1)//4+1):
        for mu in parts(kk):
            lam=(nn-kk,)+mu
            assert all(lam[i]>=lam[i+1] for i in range(len(lam)-1))
            contents=[j-i for i,row in enumerate(lam) for j in range(row)]
            tt=sum(contents); ss=sum(t*t for t in contents)
            T0,S00,V0,f0,d0=estimates(nn,kk)
            assert 0<tt<=T0 and ss>=S00
            uu=F(3*(ss-nn*(nn-1)//2),nn*(nn-1)*(nn-2))
            vv=F(4*(tt*tt+nn*(nn-1)-3*ss),nn*(nn-1)*(nn-2)*(nn-3))
            assert (1-uu)/3>=f0 and vv<=V0
            actual_bound=min(F(1,4),(1-uu)/3,(1-vv)/4)
            assert actual_bound>=d0
            hooks=[]
            for i,row in enumerate(lam):
                for j in range(row):
                    hooks.append(row-j+sum(r>j for r in lam[i+1:]))
            a=factorial(nn)//prod(hooks)
            assert factorial(nn)%prod(hooks)==0
            assert a>=90
            if kk>=3:assert a>=F(2*nn**3,27)
            min_degree=a if min_degree is None else min(a,min_degree)
            shape_count+=1
out={'status':'PASS','proof_sha256':frozen,
 'arithmetic':'Independent sparse Fraction polynomials; no root code imported',
 'uniform_delta':str(delta),'large_degree_ceiling':str(6/(10*delta-1)),
 'small_degree_ceiling':54,'endpoints':rows,'young_diagram_checks_n15_to40':shape_count,
 'minimum_degree_in_finite_range':min_degree,
 'strict_shape':[19,3],'seconds':round(time.perf_counter()-t0,9)}
Path(__file__).with_name('independent_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

