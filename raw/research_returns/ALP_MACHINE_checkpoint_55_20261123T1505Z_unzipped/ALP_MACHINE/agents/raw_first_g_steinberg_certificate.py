"""Exact finite diagnostic for LIFT20; no Lean or global-datum claim."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json

q, a, b = 3, 2, 3
n_U, d = 1, 3

# Q(zeta_3) = Q[z]/(z^2+z+1), represented exactly.
ZERO, ONE = (F(0), F(0)), (F(1), F(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def mul(x,y):
    return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]-x[1]*y[1])
def conj(x): return (x[0]-x[1],-x[1])
def scale(c,x): return (c*x[0],c*x[1])
def root(k): return (ONE,(F(0),F(1)),(F(-1),F(-1)))[k%3]
def norm(x): return x[0]**2-x[0]*x[1]+x[1]**2
def det(g): return (g[0]*g[3]-g[1]*g[2])%3
def mm(g,h):
    return tuple(sum(g[2*i+k]*h[2*k+j] for k in range(2))%3
                 for i in range(2) for j in range(2))
def inv(g):
    c=pow(det(g),-1,3)
    return tuple((c*x)%3 for x in (g[3],-g[1],-g[2],g[0]))
def line(v):
    c=pow(next(x%3 for x in v if x%3),-1,3)
    return tuple((c*x)%3 for x in v)
def act(g,v): return line((g[0]*v[0]+g[1]*v[1],g[2]*v[0]+g[3]*v[1]))

G=[g for g in product(range(q),repeat=4) if det(g)]
U=[(1,s,0,1) for s in range(q)]
flags=sorted({line(v) for v in product(range(q),repeat=2) if any(v)})
eta=lambda g: 1 if det(g)==1 else -1
chi={g:sum(act(g,L)==L for L in flags)-1 for g in G}
v={L:ZERO for L in flags}
for s in range(q): v[line((s,1))]=root(-s)
assert sum(norm(c) for c in v.values())==d
m={}
for g in G:
    z=ZERO
    for L in flags: z=add(z,mul(conj(v[act(g,L)]),v[L]))
    m[g]=scale(F(1,d),z)
fSt={g:scale(eta(g),m[g]) for g in G}
fU={g:(root(g[1]) if g in U else ZERO) for g in G}
alpha=F(d*d,len(G))
assert alpha==F(3,16)

# Literal residue predicates after the exact entB column scaling:
# the (a+1)st column is e_a, source c'=1, target c=0, r=a+1.
def raw_predicate(X,sharp):
    M=[list(X[brow*a:(brow+1)*a])+[1 if brow==a else 0]
       for brow in range(b)]
    r=a+1
    if any(M[p][pp] for p in range(r,b) for pp in range(r)): return ZERO
    for pp in range(r):
        if M[pp][pp]!=1: return ZERO
        for p in range(r):
            forced=(p>pp) or (sharp and pp==a and p<a)
            if p!=pp and forced and M[p][pp]!=0: return ZERO
    if sharp:
        z=sum(M[i][i+1] for i in range(a-1))
    else:
        z=sum(M[i][i+1] for i in range(r-1))
    # Every accepted leading matrix is unipotent: inverse chi(det)=1.
    return root(z)

V=list(product(range(q),repeat=a*b))
raw={}
for X in V:
    direct=root(X[1]) if X[0]==X[3]==1 and X[2]==X[4]==X[5]==0 else ZERO
    assert raw_predicate(X,False)==direct
    assert raw_predicate(X,True)==direct
    raw[X]=direct

# Full actual-action isotypic projector, including all multiplicities.
# The source action is eta(det g)^(-1) f(Xg).
for t in G:
    central=ZERO
    filtered=ZERO
    for g in G:
        shifted=scale(eta(g),fU[mm(t,g)])
        central=add(central,scale(chi[inv(g)],shifted))
        filtered=add(filtered,mul(conj(m[g]),shifted))
    central=scale(F(d,len(G)),central)
    filtered=scale(F(1,len(G)),filtered)
    assert central==scale(alpha,fSt[t])
    assert filtered==scale(alpha/F(d),fSt[t])

N=q**(a*b)
gammaU=F(d,N)
gammaSt=F(len(G),d*N)
gammaProj=F(d**3,N*len(G))
assert sum(norm(z) for z in raw.values())/N==gammaU
assert sum(norm(z) for z in fSt.values())/N==gammaSt
assert alpha*gammaSt==gammaU
assert alpha**2*gammaSt==gammaProj

# Actual Fourier formula on this finite window, with minus pairing.
coeff=[]
for y in V:
    z=ZERO
    for X,val in raw.items():
        if val!=ZERO:
            z=add(z,mul(val,root(-sum(xx*yy for xx,yy in zip(X,y)))))
    z=scale(F(1,N),z)
    predicted=scale(F(d,N),root(-(y[0]+y[3]))) if y[1]==1 else ZERO
    assert z==predicted
    coeff.append(z)
assert sum(c!=ZERO for c in coeff)==q**(a*b-n_U)
assert sum(norm(c) for c in coeff)==gammaU
assert sum(F(d,N) for c in coeff if c!=ZERO)==1

def vp(n,p):
    e=0
    while n and n%p==0: n//=p; e+=1
    return e

valuation_cases={}
for rank in (6,42,168):
    for prime in (113,281,4615409,5276377):
        val=sum(vp(prime**i-1,11) for i in range(1,rank+1))
        valuation_cases[f'a={rank},q={prime}']=-val

out={
    'status':'PASS',
    'scope':'Exact GL2(F3), b3 diagnostic of raw source predicates and finite projection; no full source rank/global claim.',
    'residue_matrices_checked':len(V),
    'raw_support_size':d,
    'sharp_and_nonsharp_raw_predicates_agree':True,
    'actual_source_isotypic_projection_checks':len(G),
    'actual_source_matrix_coefficient_filter_checks':len(G),
    'projection_scalar':str(alpha),
    'raw_norm_squared':str(gammaU),
    'steinberg_norm_squared':str(gammaSt),
    'projected_norm_squared':str(gammaProj),
    'raw_nonzero_fourier_coefficients':q**(a*b-n_U),
    'fourier_l1_norm':'1',
    'minus_v11_GL_orders':valuation_cases,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
