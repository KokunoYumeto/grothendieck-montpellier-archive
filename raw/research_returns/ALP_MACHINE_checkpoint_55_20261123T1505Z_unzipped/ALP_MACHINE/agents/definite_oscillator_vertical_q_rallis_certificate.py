#!/usr/bin/env python3
"""Exact diagnostics for AM-DO-047; no automorphic numerical evaluation."""
from fractions import Fraction as F
from itertools import product
from datetime import datetime, timezone
from pathlib import Path
import json

checks=0
groups={}
def check(x, group):
    global checks
    assert x, (group, checks)
    checks+=1
    groups[group]=groups.get(group,0)+1

def kap(n,q):
    ans=F(1)
    for i in range(1,n+1):
        ans*=1-F(1,q**i)
    return ans

def rank(rows,q):
    a=[list(x) for x in rows]
    if not a:return 0
    m,n=len(a),len(a[0]);r=0
    for j in range(n):
        pivot=next((i for i in range(r,m) if a[i][j]%q),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        z=pow(a[r][j],-1,q)
        a[r]=[(x*z)%q for x in a[r]]
        for i in range(m):
            if i!=r:
                z=a[i][j]
                a[i]=[(a[i][k]-z*a[r][k])%q for k in range(n)]
        r+=1
        if r==m:break
    return r

# Independent finite counting of the disintegration orbit normalizer.
for q,m,n in [(2,1,1),(2,2,1),(2,2,2),(2,3,1),(2,3,2),
              (2,3,3),(2,4,1),(2,4,2),(3,1,1),(3,2,1),
              (3,2,2),(3,3,1),(3,3,2),(5,2,1)]:
    count=0
    for xs in product(range(q),repeat=m*n):
        count+=rank([xs[i*n:(i+1)*n] for i in range(m)],q)==n
    check(F(count,q**(m*n))==kap(m,q)/kap(m-n,q),"finite full-rank orbit")
    if m>n:
        gindex=q**(n*(m-n))*kap(m,q)/(kap(n,q)*kap(m-n,q))
        check(gindex.denominator==1,"finite parabolic index")

# Count the actual raw residue predicates, not only their product formula.
for q,r,t in [(2,1,1),(3,1,1),(2,1,2)]:
    b=r+t;N=r+2*t
    for m,n,lower in [(b,r,t),(N,b,2*t)]:
        count=0
        for xs in product(range(q),repeat=m*n):
            rows=[xs[i*n:(i+1)*n] for i in range(m)]
            good=rank([row[:r] for row in rows[:r]],q)==r
            good=good and all(rows[i][j]==0 for i in range(r,m) for j in range(r))
            count+=good
        check(F(count,q**(m*n))==kap(r,q)*F(1,q**(lower*r)),"actual raw Q support")

# Rational points on the unit circle give exact Euler absolute squares.
phases=[(F(1),F(0)),(F(-1),F(0)),(F(0),F(1)),
        (F(3,5),F(4,5)),(F(-5,13),F(12,13))]
for q in [2,3,5,7,11]:
    for r in range(1,7):
        for t in range(r,10):
            b=r+t;N=r+2*t
            kr,kt,kb,kN,k2t=[kap(j,q) for j in [r,t,b,N,2*t]]
            A=q**(r*t)*kb/(kr*kt)
            B=q**(2*r*t)*kN/(kr*k2t)
            C0=kb/kt;C1=kN/kt
            f0=kr/F(q**(r*t));f1=kr/F(q**(2*r*t))
            F0=1/A
            c=F(1,q**(r*t))*kr*k2t/kb
            check(C0*F0==f0,"first Gram normalization")
            check(F(1,16*q**(r*t))<c<F(1,q**(r*t)),"uniform normalized cost")
            check(F(1)<1/(c*q**(r*t))<16,"squared inverse bound")
            for x,y in phases:
                check(x*x+y*y==1,"unitary phase")
                labs=F(1)
                for i in range(1,t+1):
                    z=F(1,q**i)
                    labs/=1-2*x*z+z*z
                F2=labs/(A*A*B)
                Z1=C1*F2
                displayed=F(1,q**(4*r*t))*kr**3*kt*k2t/kb**2*labs
                check(Z1==displayed,"second raw Gram")
                check(Z1/(f1*F0)==c*labs,"actual previous-image normalization")
                check(C0*C1*F2/(f0*f1*labs)==c,"both Rallis factors retained")
                check(C0*C1*F2/(f0*f1)>F(1,144*q**(r*t)),
                      "unnormalized lower bound")
                for nu0,nu1 in [(F(2,3),F(7,5)),(F(11),F(1,13))]:
                    # q_i scale by nu_i, disintegration factors by nu_i^-1.
                    transformed=(C0/nu0)*(C1/nu1)*(nu0*nu1)**2*F2
                    check(transformed==nu0*nu1*C0*C1*F2,"Haar scaling")

actual=[]
for a,t in [(42,1759),(168,1633)]:
    r=a+1;b=r+t;N=r+2*t
    check(t>=r,"actual rank range")
    check((-N+(b-1)+(t-1))==-2,"actual Cartan convergence margin")
    check(F(t+1,2)>F(r-1,2),"initial zeta holomorphy margin")
    check(F(N,2)<=b-1,"naive second Bochner bound fails")
    actual.append(dict(a=a,r=r,t=t,b=b,N=N,rt=r*t,
                       inverse_leading_log_q=F(r*t,2).__str__(),
                       cartan_margin_exponent=-1))
out=dict(result="PASS",time_utc=datetime.now(timezone.utc).isoformat(),
         checks=checks,groups=groups,actual_ranks=actual,
         scope="Exact finite orbit/raw support counts and Hermitian normalization algebra; no local representation or global L-value numerical computation.")
dest=Path(__file__).with_suffix(".json")
dest.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

