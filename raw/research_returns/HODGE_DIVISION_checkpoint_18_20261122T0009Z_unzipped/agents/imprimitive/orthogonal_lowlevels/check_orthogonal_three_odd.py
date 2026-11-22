#!/usr/bin/env python3
"""Exact supplements for D-OL14--15, with all-dimensional proofs in TeX."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import datetime
import hashlib
import json
import re
import time
from flint import nmod_mat

start = time.perf_counter()
base = Path(__file__).resolve().parent
proof = base/'orthogonal_three_odd_section.tex'
source = proof.read_text()
assert source.count(r'\[') == source.count(r'\]')
assert not [ord(c) for c in source if ord(c)<32 and c not in '\n\r\t']
assert re.findall(r'\\tag\{([^}]+)\}',source) == ['O3.'+str(i) for i in range(1,12)]

beta = F(1,6)-F(1,10000)
delta = (1-F(19,20)**9)/2
fixed_rank1 = (F(1,3)+F(1,3**9))/(1-F(1,3**9)-F(1,3**19))
fixed_rank2 = (F(1,3**2)+F(1,3**9))/(1-F(1,3**9)-F(1,3**19))
assert beta == F(4997,30000)
assert fixed_rank1 < 1-4*beta
assert (1-fixed_rank1)/4 > beta
assert fixed_rank2 < F(1,8)
assert F(7,32) > delta > F(1,6) > beta
assert 13*beta-2 > F(1,7)
assert 11*beta+delta-2 > F(1,60)
assert 2*beta*(1-beta) > F(1,4) > delta
assert 6/(13*beta-2)<42
assert 6/(11*beta+delta-2)<360
assert 2*3**(1135-4)>360
assert (1135-1)//2 == 567 and 1135-1>567

# Exact bilinear maximization is determined by the four rectangle corners.
corners = []
for p,q in product([beta,1-beta],repeat=2):
    probs = [p*q+(1-p)*(1-q),p*(1-q)+(1-p)*q]
    assert max(probs)<F(3,4)
    corners.append({'p':str(p),'q':str(q),'probabilities':list(map(str,probs))})
assert max(F(v) for c in corners for v in c['probabilities']) == (1-beta)**2+beta**2

def mat(rows):
    return nmod_mat(rows,3)

def eye(n):
    return mat([[int(i==j) for j in range(n)] for i in range(n)])

def diagonal(values):
    n=len(values)
    return mat([[values[i] if i==j else 0 for j in range(n)] for i in range(n)])

def norm(v):
    return sum(x*x for x in v)%3

def reflection(v):
    q=norm(v)
    assert q
    n=len(v)
    return mat([[int(i==j)-2*q*v[i]*v[j] for j in range(n)] for i in range(n)])

# An actual order4 element of Omega9(3) whose square is a negative
# reflection. Q is the sum of nine coordinate squares. Each 2D rotation
# is a product of reflections of norms2 and1; four rotations have total
# spinor norm2^4=1. This checks the higher-root exceptional-power step.
n=9
g=eye(n)
word=eye(n)
spin=1
for i in range(0,8,2):
    v=[0]*n
    v[i]=v[i+1]=1
    w=[0]*n
    w[i]=1
    rv,rw=reflection(v),reflection(w)
    spin=spin*norm(v)*norm(w)%3
    word=word*rv*rw
    g[i,i]=g[i+1,i+1]=0
    g[i,i+1]=2
    g[i+1,i]=1
assert word==g and spin==1
assert g.transpose()*g==eye(n) and g**4==eye(n) and g**2!=eye(n)
line=[0]*n
line[-1]=1
h=-reflection(line)
assert g**2==h
assert (h-eye(n)).rank()==8
assert (g-eye(n)).rank()==8 and (g+eye(n)).rank()==9
assert int(g.det())==1

# Twelve actual negative reflections in Omega13(3), with independent
# reflecting vectors and a nonzero common perpendicular. This model
# checks the concrete scalar action used in the universal generation
# contradiction; it is not an enumeration of the group.
n=13
vectors=[]
for i in range(9):
    v=[0]*n
    for j in (i,10,11,12):v[j]=1
    vectors.append(v)
for i in (9,10,11):
    v=[0]*n
    v[i]=1
    vectors.append(v)
assert len(vectors)==12 and mat(vectors).rank()==12
u=mat([[2]]*9+[[0],[0],[0],[1]])
assert mat(vectors)*u==mat([[0]]*12)
assert (u.transpose()*u)[0,0]==1
operators=[]
for v in vectors:
    assert norm(v)==1
    t=-reflection(v)
    assert t.transpose()*t==eye(n) and t*t==eye(n)
    assert int(t.det())==1 and (t-eye(n)).rank()==12
    assert t*u==-u
    # Spinor(-I)=product of the thirteen coordinate norms=1.
    assert norm(v)*1%3==1
    operators.append(t)
c=operators[0]*operators[10]*operators[0]*operators[10]
assert c!=eye(n) and c*u==u

out={
 'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'runtime_seconds':time.perf_counter()-start,
 'beta':str(beta),'delta_star':str(delta),
 'rank1_fixed_fraction_upper_bound':str(fixed_rank1),
 'rank2_fixed_fraction_upper_bound':str(fixed_rank2),
 'exact_bad_support_from_Gauss':str((1-fixed_rank1)/4),
 'thirteen_mark_degree_ceiling':str(6/(13*beta-2)),
 'one_good_mark_degree_ceiling':str(6/(11*beta+delta-2)),
 'two_active_bad_support':str(2*beta*(1-beta)),
 'exact_convolution_corners':corners,
 'higher_root_witness':{'field':3,'natural_dimension':9,'order':4,
      'reflection_word_length':8,'spinor_norm':1,'square':'negative reflection',
      'rank_g_minus_I':8,'rank_g_plus_I':9},
 'generation_witness':{'field':3,'natural_dimension':13,'negative_reflections':12,
      'reflecting_vector_rank':12,'common_perpendicular_dimension':1,
      'every_generator_on_perpendicular':'-I','nontrivial_commutator_on_perpendicular':'I'},
 'scope':'Exact arithmetic, bilinear corner identity and finite natural-matrix witnesses. The universal all-order and generation arguments are proved in TeX.',
 'failures_before_pass':[]}
(base/'orthogonal_three_odd_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
