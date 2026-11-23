#!/usr/bin/env python3
"""Exact finite convention checks for LIFT62 and its translated supplement.
Q(omega), omega^2+omega+1=0, is used throughout. This is not a formal
verification of Wallach, smooth globalization, or an arithmetic package.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import argparse, hashlib, json

@dataclass(frozen=True)
class Q:
    a:F=F(0)
    b:F=F(0)
    def __post_init__(self):
        object.__setattr__(self,'a',F(self.a));object.__setattr__(self,'b',F(self.b))
    @staticmethod
    def of(x):return x if isinstance(x,Q) else Q(x)
    def __add__(self,x):
        x=Q.of(x);return Q(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return Q(-self.a,-self.b)
    def __sub__(self,x):return self+-Q.of(x)
    def __rsub__(self,x):return Q.of(x)+-self
    def __mul__(self,x):
        x=Q.of(x);return Q(self.a*x.a-self.b*x.b,self.a*x.b+self.b*x.a-self.b*x.b)
    __rmul__=__mul__
    def __truediv__(self,x):return Q(self.a/F(x),self.b/F(x))
    def conj(self):return Q(self.a-self.b,-self.b)
    def norm(self):return self.a*self.a-self.a*self.b+self.b*self.b

Z=Q();ONE=Q(1);OM=Q(0,1);roots=[ONE,OM,OM*OM]
count=0;groups={}
def ck(ok,label):
    global count
    count+=1;groups[label.split(':')[0]]=groups.get(label.split(':')[0],0)+1
    if not ok:raise AssertionError(label)
P=list(permutations(range(3)));e=(0,1,2)
def mulp(p,q):return tuple(p[q[i]] for i in range(3))
def invp(p):return tuple(p.index(i) for i in range(3))
idx={p:i for i,p in enumerate(P)}
kappa=F(7,11);d=F(2,1)/(6*kappa)
w=(ONE,-ONE,Z)
def act(p,v):return tuple(v[invp(p)[i]] for i in range(3))
def addv(x,y):return tuple(a+b for a,b in zip(x,y))
def scv(c,v):return tuple(c*a for a in v)
def ip(x,y):return sum((a.conj()*b for a,b in zip(x,y)),Z)/2
def cv(v,u):return tuple(d*ip(v,act(g,u)).conj() for g in P)
def conv(a,b):
    return tuple(kappa*sum((a[idx[h]]*b[idx[mulp(invp(h),g)]] for h in P),Z) for g in P)
def star(a):return tuple(a[idx[invp(g)]].conj() for g in P)
def op(a,f):
    return tuple(kappa*sum((a[idx[g]]*f[idx[mulp(x,g)]] for g in P),Z) for x in P)
def reg(g,f):return tuple(f[idx[mulp(x,g)]] for x in P)
def ipfun(f,g):return kappa*sum((a.conj()*b for a,b in zip(f,g)),Z)

def matrix_units():
    cyc=(1,2,0);u=act(cyc,w)
    V=[w,u,scv(OM,w),addv(u,scv(OM,w))]
    ck(ip(w,w)==ONE,'matrix:unit vector')
    ck(d==F(11,21),'matrix:actual Haar formal degree')
    C={(i,j):cv(v,u) for i,v in enumerate(V) for j,u in enumerate(V)}
    for i,j in product(range(4),repeat=2):
        ck(star(C[i,j])==C[j,i],'matrix:star')
        for k,l in product(range(4),repeat=2):
            ck(conv(C[i,j],C[k,l])==tuple(ip(V[j],V[k])*x for x in C[i,l]),'matrix:convolution')
    ph=cv(w,w)
    basis=[tuple(ONE if i==j else Z for i in range(6)) for j in range(6)]
    Fv=[op(ph,b) for b in basis]
    for i,F0 in enumerate(Fv):
        ck(op(ph,F0)==F0,'matrix:projection')
        ck(op(cv(w,w),F0)==F0,'matrix:evaluate at w')
        for g in P:
            for v in V:
                ck(reg(g,op(cv(v,w),F0))==op(cv(act(g,v),w),F0),'matrix:equivariance')
        for F1 in Fv:
            for v,u in product(V,repeat=2):
                ck(ipfun(op(cv(v,w),F0),op(cv(u,w),F1))==ip(v,u)*ipfun(F0,F1),'matrix:polarized norm')
    ck(any(any(z!=Z for z in F0) for F0 in Fv),'matrix:nonzero projection')

G=list(product(range(3),P,range(2)));gi={g:i for i,g in enumerate(G)}
GG=list(product(range(3),P));ge=(0,e,0)
def mul(g,h):return ((g[0]+h[0])%3,mulp(g[1],h[1]),g[2]^h[2])
def inv(g):return ((-g[0])%3,invp(g[1]),g[2])
def rr(g,f):return tuple(f[gi[mul(x,g)]] for x in G)
def uf(t,f):return rr(t,f)
def con(f):return tuple(x.conj() for x in f)
def iG(f,g):return kappa*sum((a.conj()*b for a,b in zip(f,g)),Z)
def bcoef(q):
    z,p=q;char=sum(p[i]==i for i in range(3))-1
    return F(char,9)*roots[(-z)%3]
def lift(q):return (q[0],q[1],0)
def rg_raw(f):
    v0=2*kappa
    return tuple(kappa*sum((bcoef((g[0],g[1]))/v0*f[gi[mul(x,g)]] for g in G),Z) for x in G)
def rg_coset(f):
    return tuple(sum((bcoef(q)*f[gi[mul(x,lift(q))]] for q in GG),Z) for x in G)

def translated():
    t=(0,(1,2,0),0);it=inv(t);tau=(1,0,2)
    J=[g for g in G if g[1] in (e,tau)]
    Jp=[mul(mul(t,h),it) for h in J]
    def chi(h):return roots[(-h[0])%3]*(1 if h[1]==e else -1)
    def chip(h):return chi(mul(mul(it,h),t))
    def kap(k):return mul(mul(it,k),t)
    def er(f):return tuple(sum((bcoef(q).conj()*f[gi[mul(x,kap(lift(q)))]] for q in GG),Z) for x in G)
    def levelproj(f):return tuple(sum((chi(h).conj()*f[gi[mul(x,h)]] for h in J),Z)/len(J) for x in G)
    probes=[]
    for q in GG:
        z=tuple(ONE if (g[0],g[1])==q else Z for g in G)
        probes.extend([z,tuple(OM*a for a in z)])
    for g in G:
        ck((g in J)==(mul(mul(t,g),it) in Jp),'translate:ConjLevel inverse')
        if g in J:ck(chip(mul(mul(t,g),it))==chi(g),'translate:character transport')
    for f in probes:
        ck(rg_raw(f)==rg_coset(f),'translate:kernel volume cancellation')
        ck(uf(t,er(f))==con(rg_raw(con(uf(t,f)))),'translate:complex projector identity')
        ck(iG(uf(t,f),uf(t,f))==iG(f,f),'translate:unitarity')
        c=F(5,3)
        ck(c*iG(uf(t,f),uf(t,f))==c*iG(f,f),'translate:retained Haar ratio')
        q=levelproj(f);out=uf(t,q)
        for h in J:
            ck(rr(h,q)==tuple(chi(h)*x for x in q),'translate:source level')
        for h in Jp:
            ck(rr(h,out)==tuple(chip(h)*x for x in out),'translate:target level')
        eq=er(q);row=con(uf(t,eq))
        ck(er(eq)==eq,'translate:source idempotent')
        ck(rg_raw(row)==row,'translate:target good fixed space')
    ck(any(er(levelproj(f))!=levelproj(f) for f in probes),'translate:good cut not vacuous')
    ck(any(any(a!=Z for a in er(levelproj(f))) for f in probes),'translate:good cut nonzero')

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);ap.add_argument('--checked-at',required=True);args=ap.parse_args()
    ck(OM*OM+OM+ONE==Z and OM.norm()==1,'field:cyclotomic arithmetic')
    matrix_units();translated()
    out={'status':'PASS','assertions':count,'groups':groups,'checked_at_utc':args.checked_at,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'models':{'matrix_group':'S3, standard irreducible module with half-dot metric','matrix_Haar_atom':'7/11','formal_degree':'11/21','finite_group':'C3 x S3 x C2','residue_kernel_order':2,'finite_Haar_atom':'7/11','coefficient_field':'Q(omega), omega^2+omega+1=0','target_source_Haar_ratio':'5/3'},'scope':'Exact finite convention checks only: conjugate-linear-first matrix units, reconstruction, complex projector coefficients, inverse-t level transport, coset volumes and Haar ratio. The analytic/source theorems and concrete arithmetic instance are not mechanically certified.'}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
