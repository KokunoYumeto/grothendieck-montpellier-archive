#!/usr/bin/env python3
"""Independent exact supplement for SF-E837, not its all-size proof.

Author program was read first. No author code or input file is imported.
The same displayed rational boundary is reconstructed by decomposable
column pairs; polynomial arithmetic uses Sympy, not the author's masks.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import hashlib,json,time,datetime
import sympy as s

t0=time.perf_counter();base=Path(__file__).resolve().parent
proof=base.parent.parent/'sixfolds/rm_square_artin_matrix_obstruction_draft.md'
digest=hashlib.sha256(proof.read_bytes()).hexdigest()
assert digest=='f076fc5a22600fc88b0811b6550951b2c47a42b9e1eef7cf25bbbe5b889a4972'
edges=list(combinations(range(4),2));edge_index={e:i for i,e in enumerate(edges)}
graphs=[]
for chosen in combinations(edges,4):
    missing=[e for e in edges if e not in chosen]
    rows=[]
    for i,j in missing:
        rows.append([int(k==i) for k in range(4)])
        rows.append([int(k==j) for k in range(4)])
    constraints=s.Matrix(rows);ker=constraints.nullspace()
    assert len(ker)<=1
    images=[]
    for v in ker:
        for i in range(4):
            col=s.zeros(6,1)
            for j in range(4):
                if i!=j:col[edge_index[tuple(sorted((i,j)))]]+=v[j]
            images.append(col)
    dim=s.Matrix.hstack(*images).rank() if images else 0
    assert dim<=3<4
    graphs.append({'chosen':chosen,'omitted':missing,'constraint_rank':constraints.rank(),'possible_degree2_dimension':dim})
small=0
for k in range(4):
    for es in combinations(edges,k):
        assert sum(1 for e,f in combinations(es,2) if len(set(e+f))==4)<=1
        small+=1
assert small==42 and len(graphs)==15

u=s.symbols('u1:5');alpha,beta,gamma,eta=s.symbols('alpha beta gamma eta')
def reduce_square(expr):
    P=s.Poly(s.expand(expr),*u)
    return s.expand(sum(c*s.prod(x**e for x,e in zip(u,exp))
                        for exp,c in P.terms() if all(e<=1 for e in exp)))

# Four columns give two decomposable forms and an invertible actual
# constant orientation. These are the rational boundary's coefficients.
a=s.Matrix([1,0,-s.Rational(3,5),-s.Rational(8,5)])
b=s.Matrix([0,1,1,1])
c=s.Matrix([1,0,-s.Rational(9,5),-s.Rational(16,5)])
d=s.Matrix([0,1,2,3])
J0=s.Matrix.hstack(a,b,c,d);assert J0.det()==-s.Rational(4,5)
p=a*b.T-b*a.T;q=c*d.T-d*c.T
def pf(M):return s.expand(M[0,1]*M[2,3]-M[0,2]*M[1,3]+M[0,3]*M[1,2])
def mixed(M,N):
    return reduce_square(M[0,1]*N[2,3]+M[2,3]*N[0,1]
       -M[0,2]*N[1,3]-M[1,3]*N[0,2]
       +M[0,3]*N[1,2]+M[1,2]*N[0,3])
assert pf(p)==pf(q)==0 and mixed(p,q)==J0.det()

# u1=l1+alpha*l2*l3+beta*l2*l4+gamma*l3*l4+eta*l2*l3*l4,
# u2=l2,u3=l3,u4=l4. Express its exact derivative in the u coordinates.
H=s.eye(4)
H[0,1]=alpha*u[2]+beta*u[3]+eta*u[2]*u[3]
H[0,2]=alpha*u[1]+gamma*u[3]+eta*u[1]*u[3]
H[0,3]=beta*u[1]+gamma*u[2]+eta*u[1]*u[2]
assert H.det()==1
pp=H*p*H.T;qq=H*q*H.T
P=s.zeros(4);Q=s.zeros(4)
for i,j in edges:
    P[i,j]=reduce_square(4*u[i]*u[j]*pp[i,j]);P[j,i]=-P[i,j]
    Q[i,j]=reduce_square(4*u[i]*u[j]*qq[i,j]);Q[j,i]=-Q[i,j]
for i,j in edges:
    for k,l in edges:assert reduce_square(P[i,j]*Q[k,l]-Q[i,j]*P[k,l])==0
assert reduce_square(pf(P))==reduce_square(pf(Q))==0
socle=-s.Rational(64,5)*s.prod(u)
assert mixed(P,Q)==socle
ratios=[s.cancel(p[i,j]/(p[i,j]+q[i,j])) for i,j in edges]
assert all(p[i,j]+q[i,j]!=0 for i,j in edges)
assert set(ratios)=={s.Rational(1,2),s.Rational(1,3),s.Rational(1,4)}

out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'proof_sha256':digest,'elapsed_seconds':time.perf_counter()-t0,
 'all_four_edge_graphs':graphs,'small_support_graph_count':small,
 'constraint_rank_histogram':dict(Counter(g['constraint_rank'] for g in graphs)),
 'generic_nonlinear_shear_parameters':['alpha','beta','gamma','eta'],
 'ordered_cross_minors':36,'constant_orientation_determinant':str(J0.det()),
 'socle_coefficient':'-64/5','incompatible_constant_ratios':[str(r) for r in ratios],
 'scope':'Independent exact graph linear algebra and generic4-parameter nonlinear quotient identities; all-size matrix/module/global arguments separately audited in full.'}
(base/'audit_square_artin_matrix.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
