#!/usr/bin/env python3
"""Exact finite checks of E829--E831 wedge spaces and incidence arithmetic.
This does not verify the infinite Ext theorem or assert realizability of a
hypothetical support graph by a balanced object.
"""
from pathlib import Path
from itertools import combinations
from math import ceil
import hashlib,json,time
import sympy as s
def encode_exact(z):
    if isinstance(z,s.Integer):return int(z)
    raise TypeError(type(z).__name__)
start=time.perf_counter();pairs=list(combinations(range(4),2))
def sign(seq):
    if len(set(seq))!=len(seq):return 0
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
Q=s.Matrix([[sign(p+q) for q in pairs] for p in pairs]);assert Q.det()==-1 and Q.rank()==6
basis=s.eye(6)
def matrix(indices):return basis[:,indices] if indices else s.zeros(6,0)
def inv(Z):
    cols=Z.columnspace();Z=s.Matrix.hstack(*cols) if cols else s.zeros(6,0)
    z=Z.cols;gram=Z.T*Q*Z;rho=z-gram.rank();w=6-z-rho
    ns=(Z.T*Q).nullspace();P=s.Matrix.hstack(*ns) if ns else s.zeros(6,0)
    assert P.cols==6-z and (Z.T*Q*P)==s.zeros(z,P.cols)
    assert (P.T*Q*P).rank()==w
    return {'dimension_Z':z,'radical_dimension':rho,'surviving_dimension':w,'restricted_gram':gram.tolist()}
cases={
 'none':matrix([]),
 'one_surface':matrix([0]),
 'two_complementary_surfaces':matrix([0,5]),
 'two_intersecting_surfaces':matrix([0,1]),
 'common_line_maximal_isotropic':matrix([0,1,2]),
 'three_space_maximal_isotropic':matrix([0,1,3]),
 'elliptic_rank1':matrix([0]),
 'elliptic_rank2':matrix([0,1]),
 'elliptic_rank3':matrix([0,1,2]),
}
checks={name:inv(Z) for name,Z in cases.items()}
expected={'none':6,'one_surface':4,'two_complementary_surfaces':4,'two_intersecting_surfaces':2,'common_line_maximal_isotropic':0,'three_space_maximal_isotropic':0,'elliptic_rank1':4,'elliptic_rank2':2,'elliptic_rank3':0}
assert all(checks[k]['surviving_dimension']==v for k,v in expected.items())
# Hypothetical incidence data: one full elliptic edge on six selected vertices.
# The common-space bound is zero but the blockwise bound is 24.
Zell=cases['elliptic_rank3'];vertex_spaces={'A0':Zell,'B0':Zell,'A1':matrix([]),'A2':matrix([]),'B1':matrix([]),'B2':matrix([])}
local={k:inv(v)['surviving_dimension'] for k,v in vertex_spaces.items()}
assert sum(local.values())==24 and inv(Zell)['surviving_dimension']==0
# Exact closed-form necessary budgets, not a geometric existence search.
budgets=[]
for n in range(4,101):
    full=ceil((n-3)/2);surface=ceil(3*(n-3)/2)
    assert 12*full>=6*n-18 and 4*surface>=6*n-18
    assert 12*(full-1)<6*n-18 and 4*(surface-1)<6*n-18
    budgets.append({'selected_vertices':n,'maximal_elliptic_edge_minimum':full,'rank_one_support_edge_minimum':surface})
assert budgets[28]=={'selected_vertices':32,'maximal_elliptic_edge_minimum':15,'rank_one_support_edge_minimum':44}
out={'status':'PASS','basis_pairs_1_based':[[i+1,j+1] for i,j in pairs],'wedge_gram':Q.tolist(),'spaces':checks,'hypothetical_six_vertex_test':{'vertexwise_survivors':local,'total':24,'common_space_total':0,'scope':'linear-algebra incidence data only; no actual balanced object asserted'},'budgets':budgets,'runtime_seconds':time.perf_counter()-start,'scope':'Exact finite wedge-matrix and arithmetic checks supplement the complete written all-case Ext and incidence proofs. No period rank, finite action, generic product or semiregular seed is certified.'}
p=Path(__file__).with_name('rm_vertexwise_wedge_certificate_output.json');p.write_text(json.dumps(out,indent=2,default=encode_exact)+'\n')
print(json.dumps({k:out[k] for k in ['status','spaces','hypothetical_six_vertex_test','runtime_seconds','scope']},indent=2,default=encode_exact))
