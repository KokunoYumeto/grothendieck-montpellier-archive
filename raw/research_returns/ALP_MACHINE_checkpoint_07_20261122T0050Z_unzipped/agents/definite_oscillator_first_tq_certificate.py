"""Exact finite diagnostics for AM-DO-035, not a Lean/formal proof.

T: GL2(F5), quartic character, checks the source action and averaging
orientation on every residue row. Q: GL2(F3), b=4, nontrivial determinant
character, checks cancellation on all residue matrices. All arithmetic
is in Z, Q or Q(i); no floating-point assertions.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

def gl2(q):
    return [g for g in product(range(q), repeat=4)
            if (g[0]*g[3]-g[1]*g[2]) % q]

def row_mul(r,g,q):
    return ((r[0]*g[0]+r[1]*g[2])%q,
            (r[0]*g[1]+r[1]*g[3])%q)

def addi(a,b): return (a[0]+b[0],a[1]+b[1])
def muli(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def conji(a): return (a[0],-a[1])

# T. Generator 2 of F5^times has nu(2)=i.
q=5
nu={1:(1,0),2:(0,1),4:(-1,0),3:(0,-1)}
G=gl2(q)
P=[g for g in G if g[2]==0]
assert len(G)==480 and len(P)==80
assert addi(addi(nu[1],nu[2]),addi(nu[3],nu[4]))==(0,0)
T_checks=0
for r in product(range(q),repeat=2):
    total=(0,0)
    for g in P:
        if row_mul(r,g,q)==(0,1): total=addi(total,nu[g[3]])
    lhs=(Fraction(total[0],len(G)),Fraction(total[1],len(G)))
    val=conji(nu[r[1]]) if r[0]==0 and r[1] else (0,0)
    rhs=(Fraction(val[0],q*q-1),Fraction(val[1],q*q-1))
    assert lhs==rhs,(r,lhs,rhs)
    T_checks+=1
assert Fraction(len(P),len(G))==Fraction(1,6)
T_raw_norm=Fraction(1,q*q)
T_aux_norm=Fraction(q-1,q*q)
assert T_aux_norm==Fraction(4,25)

# Exact finite Gauss-sum product using the cyclotomic group ring modulo
# Phi20(x)=x^8-x^6+x^4-x^2+1. zeta5=x^4, i=x^5.
MOD=(1,0,-1,0,1,0,-1,0,1)
def red(p):
    p=list(p)+[0]*max(0,9-len(p))
    for k in range(len(p)-1,7,-1):
        c=p[k]
        if c:
            for j in range(9): p[k-8+j]-=c*MOD[j]
    return tuple(p[:8])
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
def times(a,b):
    p=[0]*15
    for i,x in enumerate(a):
        for j,y in enumerate(b): p[i+j]+=x*y
    return red(p)
def zp(e):
    p=[0]*(e%20+1);p[e%20]=1
    return red(p)
def star(a):
    ans=(0,)*8
    for j,c in enumerate(a): ans=plus(ans,tuple(c*x for x in zp(-j)))
    return ans
log2={1:0,2:1,4:2,3:3}
nonzero=0
for ell in product(range(5),repeat=2):
    # u=(0,1), so ell dot u=ell[1].
    gauss=(0,)*8
    for s in range(1,5):
        gauss=plus(gauss,zp(-5*log2[s]-4*s*ell[1]))
    if ell[1]==0: assert gauss==(0,)*8
    else:
        assert times(gauss,star(gauss))==(5,0,0,0,0,0,0,0)
        nonzero+=1
assert nonzero==20
assert Fraction(nonzero*5,25**2)==T_aux_norm

# Q. q=3,a=2,b=4,t=1; chi is the quadratic residue character.
q=3
G=gl2(q)
chi={1:1,2:-1}
def fQ(X):
    if X[6] or X[7]: return 0
    det=(X[0]*X[3]-X[1]*X[2])%q
    return chi.get(det,0)
Q_checks=0
Q_support=0
for X in product(range(q),repeat=8):
    fx=fQ(X)
    Q_support+=bool(fx)
    for g in G:
        Xg=tuple(z for i in range(4) for z in row_mul(X[2*i:2*i+2],g,q))
        detg=(g[0]*g[3]-g[1]*g[2])%q
        assert chi[detg]*fQ(Xg)==fx
        Q_checks+=1
Q_norm=Fraction(Q_support,q**8)
assert Q_support==48*9
assert Q_norm==Fraction(1,q**2)*(1-Fraction(1,q))*(1-Fraction(1,q**2))

out={
    'description':'Exact finite diagnostic, not a proof by enumeration of the general theorem',
    'T':{'q':5,'a':2,'source_row_checks':T_checks,'GL_order':480,'P_order':80,
         'filter_scalar':'1/24','source_norm_squared':'1/6',
         'raw_norm_squared':str(T_raw_norm),'filtered_aux_norm_squared':str(T_aux_norm),
         'fourier_nonzero':nonzero,'Gauss_norm_squared':5},
    'Q':{'q':3,'a':2,'b':4,'t':1,'action_checks':Q_checks,
         'support_size':Q_support,'norm_squared':str(Q_norm),
         'common_label_cancellation':True},
    'status':'PASS'
}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
