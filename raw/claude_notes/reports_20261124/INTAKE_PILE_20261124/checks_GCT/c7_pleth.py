# GCT_PLETH G-031: own computation of p^lambda_{mu,(n)} = <s_lambda, s_mu[h_n]>, mu |- 5, via power sums,
# compared with (i) the run's catalog multiplicities (FIVE_ROW_SUPPORT_INDEX.json) at small catalog vectors and
# (ii) the decision rule NW.1-NW.3 + G028 as stated in the TeX (my own implementation), for every lambda |- 5n, n<=NMAX.
import json, sys, itertools
from collections import defaultdict
from fractions import Fraction
idx=json.load(open(sys.argv[1]))
NMAX=int(sys.argv[2])
V=5
labels=[(5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1)]
classes=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
z={ (1,1,1,1,1):120,(2,1,1,1):12,(2,2,1):8,(3,1,1):6,(3,2):6,(4,1):4,(5,):5}
chi={(5,):[1,1,1,1,1,1,1],(4,1):[4,2,0,1,-1,0,-1],(3,2):[5,1,1,-1,1,-1,0],(3,1,1):[6,0,-2,0,0,0,1],
     (2,2,1):[5,-1,1,-1,-1,1,0],(2,1,1,1):[4,-2,0,1,1,0,-1],(1,1,1,1,1):[1,-1,1,1,-1,-1,1]}
def comps(n,k):
    if k==1: yield (n,); return
    for i in range(n+1):
        for r in comps(n-i,k-1): yield (i,)+r
def hpow(n,r): # h_n(x^r) as dict exponent->coef
    return {tuple(r*e for e in c):1 for c in comps(n,V)}
def mul(a,b):
    c=defaultdict(int)
    for ea,ca in a.items():
        for eb,cb in b.items():
            c[tuple(x+y for x,y in zip(ea,eb))]+=ca*cb
    return c
perms=list(itertools.permutations(range(V)))
def sgn(p):
    s=1
    for i in range(V):
        for j in range(i+1,V):
            if p[i]>p[j]: s=-s
    return s
delta=(4,3,2,1,0)
def schur_coef(f,lam):
    tot=0
    ld=[l+d for l,d in zip(lam,delta)]
    for p in perms:
        e=tuple(ld[p[i]]-delta[i] for i in range(V))
        if min(e)<0: continue
        tot+=sgn(p)*f.get(e,0)
    return tot
def parts(n,k,mx=None):
    if mx is None: mx=n
    if k==0:
        if n==0: yield ()
        return
    for i in range(min(n,mx),-1,-1):
        for r in parts(n-i,k-1,i): yield (i,)+r
cache={}
def pleth_all(n):
    if n in cache: return cache[n]
    P={}
    for rho in classes:
        f={(0,)*V:1}
        for r in rho: f=mul(f,hpow(n,r))
        P[rho]=f
    res={}
    for lam in parts(5*n,V):
        vals=[]
        sc={rho:schur_coef(P[rho],lam) for rho in classes}
        for mu in labels:
            val=sum(Fraction(chi[mu][i]*sc[rho],z[rho]) for i,rho in enumerate(classes))
            assert val.denominator==1 and val>=0
            vals.append(int(val))
        res[lam]=vals
    cache[n]=res; return res
# (i) catalog multiplicities at small vectors
cat={tuple(nd['gaps']):nd['multiplicities'] for nd in idx['nodes']}
ok=bad=0
for g,mults in cat.items():
    a,b,c,e=g
    if (a+2*b+3*c+4*e)%5: continue
    n0=(a+2*b+3*c+4*e)//5
    if n0>NMAX: continue
    lam=(a+b+c+e,b+c+e,c+e,e,0)
    mine=pleth_all(n0)[lam]
    if mine==mults: ok+=1
    else: bad+=1; print("catalog mismatch",g,mults,mine)
print("catalog vectors with n0<=%d: %d agree, %d disagree (of %d in catalog)"%(NMAX,ok,bad,len(cat)))
# (ii) decision rule
conj={(5,):(1,1,1,1,1),(4,1):(2,1,1,1),(3,2):(2,2,1),(3,1,1):(3,1,1),(2,2,1):(3,2),(2,1,1,1):(4,1),(1,1,1,1,1):(5,)}
catzero={g:{labels[i] for i,m in enumerate(ms) if m==0} for g,ms in cat.items()}
def predicted_zero(lam,mu):
    d=lam[4]; g=tuple(lam[i]-lam[i+1] for i in range(4))
    nu=mu if d%2==0 else conj[mu]
    if g==(0,0,0,0): return nu!=(5,)
    if all(x>0 for x in g):
        if nu in [(5,),(1,1,1,1,1)]:
            if (g[1:]==(1,1,1) and g[0]%5==1) or (g[:3]==(1,1,1) and g[3]%5==1): return True
        if nu==(5,) and g in [(1,2,2,1),(2,1,1,2)]: return True
        return False
    a,b,c,e=g
    L1=max(1,3*b+2*c+e); L4=max(1,a+2*b+3*c)
    if a>=L1: N=(L1+(a-L1)%10,b,c,e)
    elif e>=L4: N=(a,b,c,L4+(e-L4)%10)
    else: N=g
    return N in catzero and nu in catzero[N]
mism=0; total=0; notcat=0
for n in range(0,NMAX+1):
    for lam,vals in pleth_all(n).items():
        for i,mu in enumerate(labels):
            total+=1
            if (vals[i]==0)!=predicted_zero(lam,mu):
                mism+=1
                if mism<10: print("rule mismatch n=%d lam=%s mu=%s value=%d"%(n,lam,mu,vals[i]))
print("decision rule vs own coefficients, n<=%d: %d coefficients, %d mismatches"%(NMAX,total,mism))
