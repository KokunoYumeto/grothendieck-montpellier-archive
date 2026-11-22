"""Independent exact exterior/associative supplement for SF-E836.

Uses small integer polynomial dictionaries, not the author's SymPy code.
The full module-deformation and source proof audit is a separate record.
"""
from collections import defaultdict
from datetime import datetime, timezone
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json
import time

started=time.perf_counter()
here=Path(__file__).resolve().parent
sibling=here.parent.parent/'sixfolds'
proof=sibling/'rm_ci_point_quantization_obstruction_draft.md'
assert sha256(proof.read_bytes()).hexdigest()=='e63e9b1cc184b675d6a141673b9fb0d6a3c9fa512af7346378d42eaac03f035b'

def clean(p): return {k:v for k,v in p.items() if v}
def const(c,n): return {(0,)*n:c} if c else {}
def variable(i,n):
    e=[0]*n;e[i]=1
    return {tuple(e):1}
def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items():out[k]+=v
    return clean(out)
def scale(p,c):return clean({k:c*v for k,v in p.items()})
def mul(p,q):
    out=defaultdict(int)
    for a,x in p.items():
        for b,y in q.items():out[tuple(i+j for i,j in zip(a,b))]+=x*y
    return clean(out)
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
def det(M):
    n=len(M);out={}
    for p in permutations(range(n)):
        value=const(sign(p),len(next(iter(M[0][0]),(0,)*16)))
        for i in range(n):value=mul(value,M[i][p[i]])
        out=add(out,value)
    return out
def determinant(M,width):
    out={}
    for p in permutations(range(len(M))):
        v=const(sign(p),width)
        for i,j in enumerate(p):v=mul(v,M[i][j])
        out=add(out,v)
    return out
def bracket(J,c,d):
    return [[add(mul(J[i][c],J[j][d]),scale(mul(J[i][d],J[j][c]),-1))
             for j in range(4)] for i in range(4)]
def wedge(P,Q):
    out={}
    for i in range(4):
        for j in range(i+1,4):
            rest=[k for k in range(4) if k not in (i,j)]
            k,l=rest
            out=add(out,scale(mul(P[i][j],Q[k][l]),sign((i,j,k,l))))
    return out

# All sixteen derivatives are independent in this check, unlike a check
# only after the generator-elimination substitution.
J=[[variable(4*i+j,16) for j in range(4)] for i in range(4)]
P,Q=bracket(J,0,1),bracket(J,2,3)
W=wedge(P,Q)
assert W==determinant(J,16)
assert len(W)==24
assert wedge(P,P)=={} and wedge(Q,Q)=={}

def eliminated(p):
    out=defaultdict(int)
    for e,c in p.items():
        if e[4] or e[8] or e[12]:continue
        ee=list(e);ee[0]=0
        out[tuple(ee)]+=c
    return clean(out)

assert all(eliminated(P[i][j])=={} for i in range(1,4) for j in range(i+1,4))
We=eliminated(W)
assert all(not any(e[k] for k in (0,1,2,3,4,8,12)) for e in We)
assert len(We)==6
cross={}
for i,j,k,l,s in ((0,1,2,3,1),(0,2,1,3,-1),(0,3,1,2,1)):
    z=add(mul(P[i][j],Q[k][l]),scale(mul(Q[i][j],P[k][l]),-1))
    cross=add(cross,scale(z,s))
assert eliminated(cross)==We

# A free-associative algebra over Z[alpha,beta,gamma,delta].
# Keys consist of the central monomial and the noncommutative word.
def ac(c=1,central=(0,0,0,0),word=()):return {(central,word):c}
def aa(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items():out[k]+=v
    return clean(out)
def am(p,q):
    out=defaultdict(int)
    for (a,u),x in p.items():
        for (b,v),y in q.items():
            out[(tuple(i+j for i,j in zip(a,b)),u+v)]+=x*y
    return clean(out)
def an(p):return {k:-v for k,v in p.items()}
alpha,beta,gamma,delta=[ac(central=tuple(int(i==j) for i in range(4))) for j in range(4)]
X,Y,B,D=[ac(word=(s,)) for s in ('Cplus','Cminus','Bij','Bkl')]
syzygy=aa(am(aa(alpha,an(am(X,B))),delta),
           am(am(X,B),aa(delta,an(am(Y,D)))),
           am(am(X,aa(am(B,Y),an(beta))),D),
           am(beta,aa(am(X,D),an(gamma))),
           an(am(alpha,delta)),am(beta,gamma))
assert syzygy=={}

def derivative(p,i):
    out={}
    for e,c in p.items():
        if e[i]:
            ee=list(e);ee[i]-=1
            out[tuple(ee)]=c*e[i]
    return out
def residue(p,mixed):
    out=defaultdict(int)
    for e,c in p.items():
        ee=list(e)
        if mixed:
            c*=(-1)**ee[0]
            ee[2]+=ee[0];ee[0]=0
        if any(a>=2 for a in ee):continue
        out[tuple(ee)]+=c
    return clean(out)

x,y,z,w=[variable(i,4) for i in range(4)]
examples=[]
for mixed,fs in ((True,[add(x,z),mul(y,y),mul(z,z),mul(w,w)]),
                 (False,[mul(x,x),mul(y,y),mul(z,z),mul(w,w)])):
    jac=[[derivative(f,i) for i in range(4)] for f in fs]
    socle=residue(determinant(jac,4),mixed)
    pp,qq=bracket(jac,0,1),bracket(jac,2,3)
    minor=residue(add(mul(pp[0][1],qq[2][3]),scale(mul(qq[0][1],pp[2][3]),-1)),mixed)
    assert minor==socle and socle
    for coord in (y,z,w) if mixed else (x,y,z,w):assert residue(mul(coord,socle),mixed)=={}
    expected={(0,1,1,1):8} if mixed else {(1,1,1,1):16}
    assert socle==expected
    length=8 if mixed else 16
    examples.append({'mixed_linear_conormal':mixed,'length':length,
                     'socle':[[list(e),c] for e,c in socle.items()],
                     'Ext1_per_m_squared':6*length})

out={'status':'PASS','actual_utc':datetime.now(timezone.utc).isoformat(),
     'elapsed_seconds':time.perf_counter()-started,
     'author_arithmetic_imported':False,'author_code_previously_read':True,
     'universal_Jacobian_variables':16,'determinant_terms':24,
     'eliminated_determinant_terms':6,'free_associative_syzygy':True,
     'examples':examples,'proof_sha256':sha256(proof.read_bytes()).hexdigest(),
     'scope':'Exact algebraic supplement only; module lifting, formal generator changes, global geometry and cited theorem checked in the separate whole-proof audit',
     'model':'GPT-6 Astra Pro','effort':'inherited/not exposed','run':'HODGE_DIVISION'}
(here/'independent_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
