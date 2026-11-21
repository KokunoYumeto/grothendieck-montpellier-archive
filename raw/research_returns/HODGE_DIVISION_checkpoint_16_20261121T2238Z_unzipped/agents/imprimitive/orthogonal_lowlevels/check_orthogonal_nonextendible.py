"""Exact supplement for D-OL-09--11; universal arguments are in the proof.

This is an author certificate, not an independent peer audit.  It uses no
character tables.  The rank-four example deliberately shows why the new
commutator proof cannot reuse a rank-two-only assertion.
"""
from datetime import datetime, timezone
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import time
import sympy as sp
from flint import nmod_mat

started = time.perf_counter()
here = Path(__file__).resolve().parent
proof = here / 'orthogonal_nonextendible_section.tex'

# The two parity endpoints and their +2 induction prove the Gauss exponent
# estimate for every N >= 20. They are not a finite-range extrapolation.
for base in (20, 21):
    assert (base + 1)//2 - (base - 1) == -9
    assert (base + 3)//2 - ((base + 2) - 1) == -10

def fixed_fraction_bound(q):
    return (F(1,q*q)+F(1,q**9))/(1-F(1,q**9)-F(1,q**19))

F2, F3 = fixed_fraction_bound(2), fixed_fraction_bound(3)
assert F3 < F(1,8)
assert F2 < F(5,16)
assert F2 > F(1,4)  # The unjustified stronger endpoint is not used.
assert F(1,2)*F(1,2)*(1-F(1,8)) == F(7,32)
assert F(7,32)/2 == F(7,64)
assert F(1,2)*F(1,2)*(1-F(5,16)) == F(11,64)

# Universal field-descent exponent identity, with each right-hand term
# nonnegative for N>=20 and ell>=2.
N, ell = sp.symbols('N ell', integer=True)
assert sp.expand(-18-(ell-N*(ell-1))
                 -((N-20)*(ell-1)+19*(ell-2))) == 0
field_bound = F(1,2**18)/(1-F(1,4**9)-F(1,4**19))
assert field_bound < F(1,4)
assert F(3,16) > F(11,64) > F(7,64)

c = F(19,20)**9
delta = (1-c)/2
assert delta > F(11,64) > F(1,6)
assert 567 == 7*9**2
assert 1136//2-1 == 567
assert 1136-2 >= 567
assert 1134//2-1 < 567
assert 43*19**2 > 39**2  # 1/(sqrt(43)-1) < 19/20.
assert 6/(1+10*F(7,64)-2) == 64
assert 6/(12*F(11,64)-2) == 96
assert 3**(22-4)*(3-1) > 64
assert 2**(1136-4) > 96

def ident(n, p):
    return nmod_mat([[int(i==j) for j in range(n)] for i in range(n)], p)

def preserves_q(A, half, p):
    size = 2*half
    def Bcol(j,k):
        return sum(int(A[i,j])*int(A[half+i,k])
                   +int(A[half+i,j])*int(A[i,k])
                   for i in range(half)) % p
    for j in range(size):
        assert sum(int(A[i,j])*int(A[half+i,j])
                   for i in range(half)) % p == 0
    for j in range(size):
        for k in range(j+1,size):
            assert Bcol(j,k) == int(k==j+half)

# A commutator of a rank-two line-radical operator with an isometry can
# have rank four. The pair permutation separates the two supports.
witnesses=[]
for p in (2,3,5):
    half=12
    size=2*half
    I=ident(size,p)
    U=I*1
    U[1,half]=1
    U[0,half+1]=-1
    perm=list(range(size))
    for j,k in ((0,2),(1,3),(half,half+2),(half+1,half+3)):
        perm[j],perm[k]=perm[k],perm[j]
    H=nmod_mat([[int(i==perm[j]) for j in range(size)]
                for i in range(size)],p)
    K=H*U*H.inv()*U.inv()
    assert (U-I).rank()==2
    assert (K-I).rank()==4
    assert K**p==I and K!=I
    preserves_q(U,half,p)
    preserves_q(H,half,p)
    preserves_q(K,half,p)
    # The padded fifth hyperbolic pair is fixed pointwise.
    for j in (4,half+4):
        assert all(int(K[i,j])==int(i==j) for i in range(size))
    witnesses.append({'characteristic':p,'dimension':size,
                      'radical_moving_rank':2,'commutator_moving_rank':4,
                      'commutator_order':p,'fixed_hyperbolic_pair':[5,17]})

# Literal TeX hygiene, kept separate from the mathematics.
text=proof.read_text()
assert text.count('\\[')==text.count('\\]')
assert not any(ord(c)<32 and c not in '\n\r\t' for c in text)
out={
    'status':'PASS',
    'actual_utc':datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds':time.perf_counter()-started,
    'scope':'Author exact constants, symbolic exponent identity and rank-four matrix witnesses; universal proof is separate',
    'F_bound_q2':str(F2),'F_bound_q3':str(F3),
    'semilinear_fixed_weight_bound':str(field_bound),
    'published_delta':str(delta),
    'all_q_ge3_normalizer_support':'7/64',
    'nonextendible_even_q_support':'11/64',
    'selfdual_source_degree_ceiling':64,
    'nonextendible_source_degree_ceiling':96,
    'selfdual_q_ge3_surviving_dimension_max':21,
    'ordinary_even_q_surviving_dimension_max':1134,
    'rank_four_witnesses':witnesses,
    'proof_sha256':sha256(proof.read_bytes()).hexdigest(),
    'model':'GPT-6 Astra Pro','effort':'inherited/not exposed',
    'run':'HODGE_DIVISION',
}
(here/'orthogonal_nonextendible_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
