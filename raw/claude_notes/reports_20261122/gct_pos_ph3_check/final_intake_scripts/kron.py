import sys
from fractions import Fraction as Fr
from functools import lru_cache
from math import factorial
from collections import Counter
def partitions(m,mx=None):
    if mx is None: mx=m
    if m==0: yield (); return
    for k in range(min(m,mx),0,-1):
        for p in partitions(m-k,k): yield (k,)+p
@lru_cache(None)
def mn(lam,rho):
    if not rho: return 1 if sum(lam)==0 else 0
    k=rho[0]; rest=rho[1:]
    L=len(lam); beta=[lam[i]+L-1-i for i in range(L)]
    tot=0
    for b in beta:
        nb=b-k
        if nb<0 or nb in beta: continue
        sign=(-1)**sum(1 for x in beta if nb<x<b)
        newb=sorted([x for x in beta if x!=b]+[nb],reverse=True)
        newlam=tuple(x for x in (newb[j]-(L-1-j) for j in range(L)) if x>0)
        tot+=sign*mn(newlam,rest)
    return tot
def zee(rho):
    z=1
    for k,c in Counter(rho).items(): z*=k**c*factorial(c)
    return z
def kron(l1,l2,l3):
    N=sum(l1); tot=Fr(0)
    for rho in partitions(N):
        tot+=Fr(mn(l1,rho)*mn(l2,rho)*mn(l3,rho),zee(rho))
    return tot
for n,smax in ((3,5),(4,4)):
    vals=[]
    for s in range(0,smax+1):
        if s==0: vals.append(1); continue
        lam=tuple([s]*n); vals.append(int(kron(lam,lam,lam)))
    print('n',n,'k_n(s), s=0..',smax,':',vals)
# n=3 series 1/((1-t^2)(1-t^3)(1-t^4))
c=[0]*12; c[0]=1
for a in (2,3,4):
    for i in range(a,12): c[i]+=c[i-a]
print('n=3 series coefficients:',c[:6])
