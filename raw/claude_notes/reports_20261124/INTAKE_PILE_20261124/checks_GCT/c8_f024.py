# GCT_KRON F-024: a_lambda(d[n]) = <s_lambda, h_d[h_n]> = 1 for lambda=(d(n-2)+3,3,2^(d-3)); own code:
# h_d[h_n] in power sums via exp(sum_k p_k[h_n]/k), p_k[h_n] = sum_{mu|-n} p_{k mu}/z_mu; chi^lambda by Murnaghan-Nakayama.
import sys
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from math import factorial
def partitions(n,mx=None):
    if mx is None: mx=n
    if n==0: yield (); return
    for i in range(min(n,mx),0,-1):
        for r in partitions(n-i,i): yield (i,)+r
def zee(mu):
    from collections import Counter
    z=1
    for k,m in Counter(mu).items(): z*=k**m*factorial(m)
    return z
def pmul(a,b,maxdeg):
    c=defaultdict(F)
    for pa,ca in a.items():
        da=sum(pa)
        for pb,cb in b.items():
            if da+sum(pb)>maxdeg: continue
            c[tuple(sorted(pa+pb,reverse=True))]+=ca*cb
    return c
def hd_of_hn(d,n):
    D=d*n
    # L = sum_k p_k[h_n]/k  (only terms of degree k*n <= D)
    L=defaultdict(F)
    for k in range(1,d+1):
        for mu in partitions(n):
            L[tuple(sorted([k*x for x in mu],reverse=True))]+=F(1,k*zee(mu))
    # exp(L) graded: E_j = degree j*n part; use E = sum L^m/m!
    total=defaultdict(F); total[()]=F(1)
    term={():F(1)}
    for m in range(1,d+1):
        term=pmul(term,L,D)
        for p,c in term.items(): total[p]+=c/factorial(m)
    return {p:c for p,c in total.items() if sum(p)==D and c!=0}
@lru_cache(maxsize=None)
def mn(shape,rho):
    # chi^shape(rho) via border strips; shape as tuple, rho as tuple (remove rho[0])
    if not rho: return 1 if sum(shape)==0 else 0
    k=rho[0]; rest=rho[1:]
    # beta-numbers
    L=len(shape); beta=[shape[i]+L-1-i for i in range(L)]; bs=set(beta)
    tot=0
    for b in beta:
        if b-k>=0 and (b-k) not in bs:
            sgn=(-1)**sum(1 for x in beta if b-k<x<b)
            nb=sorted([x for x in beta if x!=b]+[b-k],reverse=True)
            ns=tuple(nb[i]-(L-1-i) for i in range(L))
            ns=tuple(x for x in ns if x>0)
            tot+=sgn*mn(ns,rest)
    return tot
n=int(sys.argv[1])
for d in range(3,int(sys.argv[2])+1):
    lam=(d*(n-2)+3,3)+(2,)*(d-3)
    H=hd_of_hn(d,n)
    a=sum(c*mn(lam,p) for p,c in H.items())
    # sanity: total dimension check <h_d[h_n], h_{dn}> = 1
    triv=sum(c*mn((d*n,),p) for p,c in H.items())
    print(f"n={n} d={d} lambda={lam}: a_lambda={a}  (trivial-rep coefficient {triv})")
