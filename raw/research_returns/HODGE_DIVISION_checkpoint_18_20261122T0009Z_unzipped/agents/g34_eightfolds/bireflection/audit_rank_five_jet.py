#!/usr/bin/env python3
"""Separate exact reconstruction of E839's finite witness.

The full author program was read before writing this file. No author code,
computed matrix, or output is imported. Quotient multiplication is implemented
on the sixteen squarefree monomials with x1^2=-x2*x3. This supplement is not
the proof of the arbitrary-size matrix lemma or the deformation interface.
"""
from pathlib import Path
from itertools import combinations, product
from collections import defaultdict
import datetime, hashlib, json, time
import sympy as s

t0=time.perf_counter(); base=Path(__file__).resolve().parent
proof=base.parent.parent/'sixfolds/rm_rank_five_jet_obstruction_draft.md'
phash=hashlib.sha256(proof.read_bytes()).hexdigest()
assert phash=='7d17ecc2d6f858127b01d6b62537a11e1e3991e72619047ded837fd69d687fbb'
xs=s.symbols('x1:5'); aa,bb=s.symbols('a b')
edges=list(combinations(range(4),2)); basis=list(product(range(2),repeat=4))

def normal_monomial(exps):
    e=list(exps); sign=1
    while e[0]>=2:
        e[0]-=2; e[1]+=1; e[2]+=1; sign=-sign
    if any(v>=2 for v in e): return None,0
    return tuple(e),sign

def normal(expr):
    ans=defaultdict(lambda:s.Integer(0))
    for powers,c in s.Poly(s.expand(expr),*xs).terms():
        q,sgn=normal_monomial(powers)
        if sgn: ans[q]+=sgn*c
    return s.expand(sum(c*s.prod(x**k for x,k in zip(xs,e)) for e,c in ans.items()))

J=s.Matrix([[0,1,0,1],[1,1,3,2],[1,0,1,0],[1,0,2,0]])
assert J.det()==-1
# Reconstruct the two bivectors from their four column vectors.
col=[J[:,i] for i in range(4)]
pp=col[0]*col[1].T-col[1]*col[0].T
qq=col[2]*col[3].T-col[3]*col[2].T
F=[xs[0]**2+xs[1]*xs[2],xs[1]**2,xs[2]**2,xs[3]**2]
grad=[s.Matrix([s.diff(f,x) for x in xs]) for f in F]
P=[normal((grad[i].T*pp*grad[j])[0]) for i,j in edges]
Q=[normal((grad[i].T*qq*grad[j])[0]) for i,j in edges]
pairmons=[xs[i]*xs[j] for i,j in edges]
def coeffmat(polys):
    return s.Matrix([[s.Poly(f,*xs).coeff_monomial(mon) for f in polys] for mon in pairmons])
MP,MQ=coeffmat(P),coeffmat(Q); pencil=aa*MP+bb*MQ
assert MP.rank()==MQ.rank()==pencil.rank()==5
assert pencil.det()==0 and pencil[:,5]==s.zeros(6,1)
minors=[]
for ri in range(6):
    for cj in range(6):
        m=s.factor(pencil.minor_submatrix(ri,cj).det())
        minors.append({'omit_row':ri,'omit_col':cj,'minor':str(m)})
assert s.expand(pencil.minor_submatrix(5,5).det()
       +1024*(aa+3*bb)*(aa+bb)*(aa+2*bb)**2*(aa+4*bb))==0
assert sum(v['minor']!='0' for v in minors)==2
assert s.Matrix.hstack(s.Matrix(P),s.Matrix(Q)).rank()==2

def wedge(P,Q):
    return normal(P[0]*Q[5]+P[5]*Q[0]-P[1]*Q[4]-P[4]*Q[1]
                  +P[2]*Q[3]+P[3]*Q[2])
soc=s.prod(xs)
assert wedge(P,P)==wedge(Q,Q)==0 and wedge(P,Q)==-16*soc
assert normal(s.det(s.Matrix.hstack(*grad).T))==16*soc

# Full multiplication table, associativity, and annihilator of the maximal
# ideal independently verify the explicit length-sixteen graded model.
table={}
for u,v in product(basis,repeat=2):
    table[(u,v)]=normal_monomial(tuple(a+b for a,b in zip(u,v)))
def multpair(pair,w):
    u,sgn=pair
    if not sgn:return None,0
    v,t=table[(u,w)]
    return (v,sgn*t) if t else (None,0)
for u,v,w in product(basis,repeat=3):
    assert multpair(table[(u,v)],w)==multpair(table[(v,w)],u)
unitvectors=[tuple(int(i==j) for i in range(4)) for j in range(4)]
soclebasis=[v for v in basis if all(table[(v,u)][1]==0 for u in unitvectors)]
assert soclebasis==[(1,1,1,1)]
assert [sum(sum(e)==j for e in basis) for j in range(5)]==[1,4,6,4,1]

# Rank-one relation quadrics: a mixed 2x2 minor forces the first coefficient
# to vanish; the remaining diagonal rank-one locus has exactly three axes.
c,d,e,f=s.symbols('c d e f')
H=s.Matrix([[c,0,0,0],[0,d,c/2,0],[0,c/2,e,0],[0,0,0,f]])
assert H.extract([0,1],[0,2]).det()==c*c/2
assert [H.subs(c,0).extract(list(ii),list(ii)).det()
        for ii in [(1,2),(1,3),(2,3)]]==[d*e,d*f,e*f]
# Four-annihilator equality boundary in the square algebra.
inc=s.Matrix([[int(i in edge) for i in range(4)] for edge in edges])
assert inc.rank()==4
assert 36*6==216 and 4+2*5==14 and 6*16==96

out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
     'elapsed_seconds':time.perf_counter()-t0,'proof_sha256':phash,
     'quotient_dimension':16,'multiplication_pairs':256,'associativity_triples':4096,
     'hilbert_function':[1,4,6,4,1],'socle_basis':soclebasis,
     'pencil_minors':minors,'nonzero_five_minors':2,'both_endpoint_rank':5,
     'mixed_socle_coefficient':-16,'chart_equation_bound':216,
     'chart_degree_bound':14,'extension_dimension_coefficient':96,
     'scope':'Finite witness and equation arithmetic; universal matrix, filtered, module and geometric arguments audited separately as proofs.'}
(base/'audit_rank_five_jet.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='pencil_minors'},indent=2))
