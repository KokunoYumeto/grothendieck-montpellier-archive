#!/usr/bin/env python3
"""Independent exact supplement to the whole OL09--11 peer review.

No author program or input is imported. The author program was read
before this code was written. Universal representation arguments are
audited separately, not inferred from these finite matrices.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import Counter
import hashlib,json,time,datetime
from flint import nmod_mat

t0=time.perf_counter()
base=Path(__file__).resolve().parent
proof=base.parent.parent/'imprimitive/orthogonal_lowlevels/orthogonal_nonextendible_section.tex'
digest=hashlib.sha256(proof.read_bytes()).hexdigest()
assert digest=='5f7e898c37be40cb4a17cd8ccbfdce9fa48b90d3c3beb40d0637fed620ae5bd4'

# Prove endpoint rational inequalities; all negative nonconstant
# coefficients make the respective numerators decreasing for x>=0.
x=Q(1,3)
p3=1-8*x*x-9*x**9-x**19
assert p3>0
x=Q(1,2)
p2=5-16*x*x-21*x**9-5*x**19
assert p2>0
f3=(Q(1,9)+Q(1,3**9))/(1-Q(1,3**9)-Q(1,3**19))
f2=(Q(1,4)+Q(1,2**9))/(1-Q(1,2**9)-Q(1,2**19))
assert f3<Q(1,8) and Q(1,4)<f2<Q(5,16)

# Coefficient dictionaries verify the universal exponent identity,
# without substituting a finite set of N or ell values.
# ell-N(ell-1)+18+(N-20)(ell-1)+19(ell-2) == 0.
poly=Counter()
for term in [{(0,1):1,(1,1):-1,(1,0):1,(0,0):18},
             {(1,1):1,(1,0):-1,(0,1):-20,(0,0):20},
             {(0,1):19,(0,0):-38}]: poly.update(term)
assert all(v==0 for v in poly.values())
field=Q(1,2**18)/(1-Q(1,4**9)-Q(1,4**19))
assert field<Q(1,4)
assert 1-Q(1,2)*Q(1,4)-Q(1,2)==Q(3,8)  # simple mass arithmetic check

c=Q(19,20)**9
delta=(1-c)/2
assert delta>Q(11,64)>Q(1,6)
assert 567==7*9**2 and 1136//2-1==567
assert 1134//2-1==566
assert 43*19**2>39**2
assert Q(1,2)*Q(1,2)*Q(7,8)==Q(7,32)
assert Q(1,2)*Q(7,32)==Q(7,64)
assert Q(1,2)*Q(1,2)*Q(11,16)==Q(11,64)
assert Q(6)/(Q(1)+10*Q(7,64)-2)==64
assert Q(6)/(12*Q(11,64)-2)==96

def mat(rows,p):return nmod_mat(rows,p)
def eye(n,p):return mat([[int(i==j) for j in range(n)] for i in range(n)],p)
def embed_upper(B,p,extra=1):
    # Embed the upper radical on five actual hyperbolic pairs.
    n=B.nrows()+extra
    A=eye(2*n,p)
    for i in range(B.nrows()):
        for j in range(B.ncols()): A[i,n+j]=B[i,j]
    return A
def preserves_split(A,p):
    n=A.nrows()//2
    for i in range(2*n):
        assert sum(int(A[j,i])*int(A[n+j,i]) for j in range(n))%p==0
        for k in range(i+1,2*n):
            v=sum(int(A[j,i])*int(A[n+j,k])+int(A[j,k])*int(A[n+j,i]) for j in range(n))%p
            assert v==int(k==n+i)

# Distinct finite reconstruction: every alternating4-form, conjugated
# by a four-cycle in a Levi subgroup, rather than the author's one
# disjoint-support pair-permutation witness in dimension24.
summary=[]
for p in (2,3,5):
    P=mat([[int(i==(j+1)%4) for j in range(4)] for i in range(4)],p)
    hist=Counter(); eligible=0; sample=None
    positions=[(i,j) for i in range(4) for j in range(i+1,4)]
    for coeff in product(range(p),repeat=6):
        rows=[[0]*4 for _ in range(4)]
        for (i,j),v in zip(positions,coeff): rows[i][j]=v;rows[j][i]=-v%p
        B=mat(rows,p)
        if B.rank()!=2:continue
        eligible+=1
        C=P*B*P.transpose()-B
        hist[C.rank()]+=1
        assert C.rank() in (0,2,4)
        if sample is None and C.rank()==4:sample=(B,C,list(coeff))
    assert sample is not None
    B,C,coeff=sample
    U=embed_upper(B,p); K=embed_upper(C,p); I=eye(10,p)
    Hp=eye(5,p)
    for i in range(4):
        for j in range(4):Hp[i,j]=P[i,j]
    H=eye(10,p)
    for i in range(5):
        for j in range(5):H[i,j]=Hp[i,j];H[5+i,5+j]=Hp.inv().transpose()[i,j]
    assert H*U*H.inv()*U.inv()==K
    assert (U-I).rank()==2 and (K-I).rank()==4
    assert K**p==I and K!=I
    for A in (U,H,K):preserves_split(A,p)
    assert all(int(K[i,4])==int(i==4) and int(K[i,9])==int(i==9) for i in range(10))
    summary.append({'p':p,'alternating_forms_total':p**6,'rank_two_forms':eligible,
                    'commutator_rank_histogram':dict(sorted(hist.items())),
                    'rank_four_witness_coefficients':coeff,
                    'natural_dimension':10,'prime_order':p,'fixed_pair':[4,9]})

out={'status':'PASS','proof_sha256':digest,'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-t0,
 'q3_bound':str(f3),'q2_bound':str(f2),'semilinear_fixed_fraction':str(field),
 'published_support_delta':str(delta),'source_ceilings':[64,96],
 'surviving_natural_dimension_bounds':[21,1134],
 'alternating_matrix_reconstructions':summary,
 'scope':'Independent arithmetic, formal coefficient identity, complete small alternating-matrix enumeration and direct orthogonal commutator checks; universal proof separately read in full.'}
(base/'audit_orthogonal_nonextendible.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
