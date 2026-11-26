import sys,itertools
from fractions import Fraction as Fr
from collections import defaultdict
sys.path.insert(0,sys.argv[1])
import shp
exec(open('w5.py').read().split('k=5')[0])
# general S_m characters via Murnaghan-Nakayama (m<=5)
def partitions(m,mx=None):
    if mx is None: mx=m
    if m==0: yield (); return
    for k in range(min(m,mx),0,-1):
        for p in partitions(m-k,k): yield (k,)+p
def mn_char(lam,rho):
    # Murnaghan-Nakayama via border strips using beta-sets
    if not rho: return 1 if sum(lam)==0 else 0
    k=rho[0]; rest=rho[1:]
    L=len(lam); beta=[lam[i]+L-1-i for i in range(L)]
    tot=0
    for i,b in enumerate(beta):
        nb=b-k
        if nb<0 or nb in beta: continue
        sign=(-1)**sum(1 for x in beta if nb<x<b)
        newb=sorted([x for x in beta if x!=b]+[nb],reverse=True)
        newlam=tuple(newb[j]-(L-1-j) for j in range(L))
        newlam=tuple(x for x in newlam if x>0)
        tot+=sign*mn_char(newlam,rest)
    return tot
from math import factorial
def zee(rho):
    from collections import Counter
    z=1
    for k,c in Counter(rho).items(): z*=k**c*factorial(c)
    return z
def mul(a,b):
    r=defaultdict(int)
    for w1,c1 in a.items():
        for w2,c2 in b.items(): r[tuple(x+y for x,y in zip(w1,w2))]+=c1*c2
    return r
cache={}
def schurW(mu,n,k):
    key=(mu,n,k)
    if key in cache: return cache[key]
    m=sum(mu)
    base=[w for w in itertools.product(range(n+1),repeat=k) if sum(w)==n]
    pk={}
    for kk in range(1,m+1):
        d=defaultdict(int)
        for w in base: d[tuple(kk*x for x in w)]+=1
        pk[kk]=d
    tot=defaultdict(Fr)
    for rho in partitions(m):
        c=mn_char(mu,rho)
        if c==0: continue
        prod={tuple([0]*k):1}
        for part in rho: prod=mul(prod,pk[part])
        for w,cc in prod.items(): tot[w]+=Fr(c*cc,zee(rho))
    res={w:int(c) for w,c in tot.items() if c}
    cache[key]=res; return res
checked=bad=0
for m in (3,4,5):
    maxn={3:5,4:4,5:3}[m]
    for n in range(1,maxn+1):
        for a in range(1,n+1):
            for t in range(0,n-a+1):
                for r in range(0,m-1):
                    A=m*n-a-(m-1)*t-r
                    if A<a+t: continue
                    lam=(A,a+t)+(t+1,)*r+(t,)*(m-2-r)
                    k=len([x for x in lam if x>0]) or 1
                    k=max(k,2)
                    for mu in partitions(m):
                        theirs=shp.coefficient(m,a,r,t,n,mu)
                        mine=mult(schurW(mu,n,k),[x for x in lam if x>0],k)
                        checked+=1
                        if mine!=theirs: bad+=1; print('MISMATCH',m,n,a,t,r,mu,lam,mine,theirs)
print('checked',checked,'mismatches',bad)
