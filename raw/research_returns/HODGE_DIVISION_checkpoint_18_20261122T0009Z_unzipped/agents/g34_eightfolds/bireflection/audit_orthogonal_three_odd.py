#!/usr/bin/env python3
"""Independent E839-era audit supplement for D-OL14--15.

The author code was read first, but none is imported. This reconstruction
uses an order-eight root in dimension17, twelve reflections with a
three-dimensional common perpendicular in dimension15, and exact norm
distributions by convolution, rather than the author's9/13-dimensional
witnesses. Universal claims remain proof checks.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import datetime,hashlib,json,time
from flint import nmod_mat

start=time.perf_counter();base=Path(__file__).resolve().parent
proof=base.parent.parent/'imprimitive/orthogonal_lowlevels/orthogonal_three_odd_section.tex'
phash=hashlib.sha256(proof.read_bytes()).hexdigest()
assert phash=='7d0e8c1e9e9023e0840b306642696c942020cc870c2460f5265a1a9feb947e5b'
beta=F(4997,30000);delta=(1-F(19,20)**9)/2
den=1-F(1,3**9)-F(1,3**19)
c1=(F(1,3)+F(1,3**9))/den
c2=(F(1,9)+F(1,3**9))/den
assert (1-c1)/4>beta and c2<F(1,8)
assert F(7,32)>delta>F(1,6)>beta
assert 13*beta-2>F(1,7) and 11*beta+delta-2>F(1,60)
ceiling13=6/(13*beta-2);ceilinggood=6/(11*beta+delta-2)
assert ceiling13<42 and ceilinggood<360
cornermax=max(max(p*q+(1-p)*(1-q),p*(1-q)+(1-p)*q)
              for p,q in product((beta,1-beta),repeat=2))
assert cornermax==1-2*beta*(1-beta)<F(3,4)<1-delta
assert 2*3**(1135-4)>360 and (1135-1)//2==7*9**2

# Exact diagonal quadratic counts, without using a Gauss-sum formula.
def counts(coeffs):
    dist=[1,0,0]
    for c in coeffs:
        nxt=[0,0,0]
        for z in range(3):
            for r,n in enumerate(dist):nxt[(r+c*z*z)%3]+=n
        dist=nxt
    return dist
samples=0;maxfraction=F(0)
for N,tail,normal in product(range(20,41),(1,2),(1,2)):
    fixed=counts([1]*(N-2)+[tail])
    total=counts([1]*(N-2)+[tail,normal])
    for u in range(3):
        num=fixed[u]-int(u==0);dem=total[u]-int(u==0)
        frac=F(num,dem);assert frac<c1
        maxfraction=max(maxfraction,frac);samples+=1
assert samples==252

def M(rows):return nmod_mat(rows,3)
def eye(n):return M([[int(i==j) for j in range(n)] for i in range(n)])
def putblock(target,A,offset):
    for i in range(A.nrows()):
        for j in range(A.ncols()):target[offset+i,offset+j]=A[i,j]

# The paired reciprocal F9-primary matrix A has order8; its fourth
# power is -I. Four identical4D hyperbolic embeddings have spinor
# norm a fourth power, hence1, independently of the individual norm.
A=M([[0,1],[1,1]]);assert A**4==-eye(2) and A**8==eye(2)
block=eye(4);putblock(block,A,0);putblock(block,A.inv().transpose(),2)
H=M([[0,0,1,0],[0,0,0,1],[1,0,0,0],[0,1,0,0]])
assert block.transpose()*H*block==H and int(block.det())==1
g=eye(17);B=M([[0]*17 for _ in range(17)])
for off in (0,4,8,12):putblock(g,block,off);putblock(B,H,off)
B[16,16]=2
assert g.transpose()*B*g==B and g**8==eye(17) and g**4!=eye(17)
line=[0]*17;line[-1]=1
rv=eye(17);rv[16,16]=2
assert g**4==-rv
assert (g-eye(17)).rank()==16 and (g+eye(17)).rank()==17

# Twelve independent norm-one vectors in a 12-space, embedded in a
#15-space, give a common3-space. This is not a generation claim.
n=15;vectors=[]
for i in range(12):
    v=[0]*n
    for j in (range(i,i+4) if i<9 else [i]):v[j]=1
    assert sum(x*x for x in v)%3==1
    vectors.append(v)
V=M(vectors);assert V.rank()==12
U=M([[int(i==j+12) for j in range(3)] for i in range(n)])
assert V*U==M([[0]*3 for _ in range(12)])
ops=[]
for v in vectors:
    r=M([[int(i==j)-2*v[i]*v[j] for j in range(n)] for i in range(n)])
    t=-r
    assert t*t==eye(n) and t.transpose()*t==eye(n) and int(t.det())==1
    assert t*U==-U
    # With Q=sum x_i^2, theta(-I)=1 and theta(r_v)=Q(v)=1.
    ops.append(t)
comm=ops[0]*ops[2]*ops[0]*ops[2]
assert comm!=eye(n) and comm*U==U

out={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-start,'proof_sha256':phash,
 'beta':str(beta),'delta_star':str(delta),'rank1_fraction_bound':str(c1),
 'rank2_fraction_bound':str(c2),'two_active_support':str(1-cornermax),
 'ceiling_thirteen':str(ceiling13),'ceiling_one_good':str(ceilinggood),
 'exact_norm_distributions':samples,'maximum_sampled_fixed_fraction':str(maxfraction),
 'higher_root':{'order':8,'dimension':17,'ranks_minus_plus':[16,17],
                'spinor_argument':'four identical orthogonal blocks, hence fourth power1'},
 'generation_witness':{'dimension':15,'reflecting_rank':12,'common_perpendicular_dimension':3,
                       'all_negative_reflections_on_common_space':'-I'},
 'scope':'Exact arithmetic and finite natural-matrix supplements only; all-order classification, full-normalizer scope and universal perfectness/generation contradiction checked as proofs.'}
(base/'audit_orthogonal_three_odd.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
