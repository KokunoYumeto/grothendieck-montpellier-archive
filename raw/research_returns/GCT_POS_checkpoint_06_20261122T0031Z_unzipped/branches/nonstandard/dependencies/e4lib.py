# Nonstandard Hecke algebra r=4: dual-KL-cone (C x C) positivity of P-words, incl. F57's omega.
# Laurent polys: dict exp->int. Convention (T-v)(T+1/v)=0, C'_s=T+1/v, C_s=T-v.
import itertools, sys
from collections import defaultdict
def padd(a,b,s=1):
    r=dict(a)
    for e,c in b.items():
        r[e]=r.get(e,0)+s*c
        if r[e]==0: del r[e]
    return r
def pmul(a,b):
    r=defaultdict(int)
    for e,c in a.items():
        for f,d in b.items(): r[e+f]+=c*d
    return {e:c for e,c in r.items() if c}
import os
n=int(os.environ.get("HN","4"))
G=list(itertools.permutations(range(n)))
def comp(a,b): return tuple(a[b[i]] for i in range(n))
def length(w): return sum(1 for i in range(n) for j in range(i+1,n) if w[i]>w[j])
S=[tuple(list(range(i))+[i+1,i]+list(range(i+2,n))) for i in range(n-1)]
ONE={0:1}; VMV={1:1,-1:-1}  # v - 1/v
def mulTs(x,s):  # x * T_s, x dict perm->poly
    out={}
    for w,c in x.items():
        ws=comp(w,s)
        if length(ws)>length(w): out[ws]=padd(out.get(ws,{}),c)
        else:
            out[ws]=padd(out.get(ws,{}),c); out[w]=padd(out.get(w,{}),pmul(c,VMV))
    return {k:p for k,p in out.items() if p}
def hadd(x,y,s=1):
    out=dict(x)
    for k,p in y.items():
        out[k]=padd(out.get(k,{}),p,s)
        if not out[k]: del out[k]
    return out
def hscale(x,p): return {k:pmul(q,p) for k,q in x.items()}
def mulCp(x,s): return hadd(mulTs(x,s),hscale(x,{-1:1}))
# reduced words
red={G[0] if False else tuple(range(n)):[]}
frontier=[tuple(range(n))]
while frontier:
    nf=[]
    for w in frontier:
        for i,s in enumerate(S):
            ws=comp(w,s)
            if ws not in red and length(ws)==length(w)+1: red[ws]=red[w]+[i]; nf.append(ws)
    frontier=nf
def hmulT(x,w):
    for i in red[w]: x=mulTs(x,S[i])
    return x
# KL basis C'_w: coefficients of T_y (y<w) in v^{-1}Z[v^{-1}]
order=sorted(G,key=length)
Cp={tuple(range(n)):{tuple(range(n)):ONE}}
for w in order[1:]:
    i=red[w][-1]; wp=comp(w,S[i])  # w = wp * s_i
    x=mulCp(Cp[wp],S[i])
    changed=True
    while changed:
        changed=False
        for z in sorted(x,key=length,reverse=True):
            if z==w: continue
            c0=x[z].get(0,0)
            if c0 or any(e>0 for e in x[z]):
                assert not any(e>0 for e in x[z]), (w,z,x[z])
                x=hadd(x,hscale(Cp[z],{0:c0}),-1); changed=True; break
    Cp[w]=x
# inverse: T_y in C' basis
def toCp(x):
    x=dict(x); co={}
    while x:
        z=max(x,key=length); c=x[z]; co[z]=c
        x=hadd(x,hscale(Cp[z],c),-1)
    return co
Tinv={w:toCp({w:ONE}) for w in G}
# tensor elements: dict (a,b)->poly ; multiply on right by P_s = C's(x)C's + Cs(x)Cs
def tmulP(X,s):
    # x(x)y * (A(x)B) for A,B in {C's, Cs}: C's = T+1/v, Cs = T - v
    out={}
    for (a,b),c in X.items():
        for shift in ({-1:1},{1:-1}):
            L=hadd(mulTs({a:ONE},s),{a:shift}); R=hadd(mulTs({b:ONE},s),{b:shift})
            for k,p in L.items():
                for l,q in R.items():
                    key=(k,l); out[key]=padd(out.get(key,{}),pmul(c,pmul(p,q)))
                    if not out[key]: del out[key]
    return out
def tcoordsKL(X):
    out={}
    for (a,b),c in X.items():
        for y,p in Tinv[a].items():
            for z,q in Tinv[b].items():
                key=(y,z); out[key]=padd(out.get(key,{}),pmul(c,pmul(p,q)))
                if not out[key]: del out[key]
    return out
def dualpos(X):
    co=tcoordsKL(X); bad=0; neg=0
    for (y,z),p in co.items():
        sgn=(-1)**(length(y)+length(z))
        if any(sgn*c<0 for c in p.values()): bad+=1
        if any(c<0 for c in p.values()): neg+=1
    return len(co),bad,neg
e=tuple(range(n)); I={(e,e):ONE}
# ---- added for the E(4) task ----
e=tuple(range(n))
ONE_T={(e,e):{0:1}}
def tadd(X,Y,s=1):
    out=dict(X)
    for k,p in Y.items():
        out[k]=padd(out.get(k,{}),p,s)
        if not out[k]: del out[k]
    return out
def tscale(X,p): return {k:pmul(q,p) for k,q in X.items() if pmul(q,p)}
def word_elt(ws):
    X=ONE_T
    for i in ws: X=tmulP(X,S[i-1])
    return X
def comb(terms):
    """terms: list of (laurent dict, word tuple) -> tensor element"""
    X={}
    for c,ws in terms: X=tadd(X,tscale(word_elt(ws),c))
    return X
def rmul_comb(X,terms):
    """X * sum c * P_word"""
    out={}
    for c,ws in terms:
        Y=X
        for i in ws: Y=tmulP(Y,S[i-1])
        out=tadd(out,tscale(Y,c))
    return out
def dualcoords(X):
    """C(x)C coordinates of an element of nsH (= (-1)^{l(x)+l(y)} x C'(x)C' coordinates, INT-NSRH-1)"""
    co=tcoordsKL(X)
    return {(y,z):{k:(-1)**(length(y)+length(z))*c for k,c in p.items()} for (y,z),p in co.items()}
def tensorCp(w1,w2):
    return {(a,b):pmul(p,q) for a,p in Cp[w1].items() for b,q in Cp[w2].items()}
