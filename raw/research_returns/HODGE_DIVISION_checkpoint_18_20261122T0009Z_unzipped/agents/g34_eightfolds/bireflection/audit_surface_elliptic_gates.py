#!/usr/bin/env python3
"""Independent exact exterior algebra for E829/E830; geometry is reviewed in prose."""
from pathlib import Path
from itertools import combinations
import hashlib,json,time
import sympy as s

start=time.perf_counter();base=Path(__file__).resolve().parent
V=tuple(range(4));B2=list(combinations(V,2));B3=list(combinations(V,3))
def wedge(a,b):
 if set(a)&set(b):return 0,()
 inversions=sum(x>y for x in a for y in b)
 return (-1)**inversions,tuple(sorted(a+b))
Q=s.Matrix([[wedge(a,b)[0] for b in B2] for a in B2])
assert Q==Q.T and Q.det()==-1 and Q.rank()==6
def zcol(a):return s.Matrix([int(b==tuple(a)) for b in B2])
def stats(cols):
 z=s.Matrix.hstack(*cols) if cols else s.zeros(6,0)
 if cols:z=s.Matrix.hstack(*z.columnspace())
 dim=z.cols; rr=dim-(z.T*Q*z).rank()
 ann=(z.T*Q).nullspace()
 assert len(ann)==6-dim
 return {'z':dim,'radical':rr,'surviving':6-dim-rr}
surfaces={
 'none':stats([]),
 'single':stats([zcol((0,1))]),
 'complementary':stats([zcol((0,1)),zcol((2,3))]),
 'intersecting':stats([zcol((0,1)),zcol((0,2))]),
}
assert [surfaces[k]['surviving'] for k in surfaces]==[6,4,4,2]

# All nondegenerate surface-part ranks >=2 and all possible indices.
# The nonzero line cohomology in degree j is treated as one arbitrary module;
# exterior multiplication acts on its kernel factor. Its multiplicity is irrelevant.
table=[]
for r in (2,3,4):
 K=tuple(range(r,4))
 for ind in range(r+1):
  maps=[]
  for j in (ind,r-ind):
   source=list(combinations(K,1-j)) if 0<=1-j<=len(K) else []
   target=list(combinations(K,3-j)) if 0<=3-j<=len(K) else []
   for a in source:
    for dest in target:
     maps.append([wedge(b,a)[0] if set(b)<=set(K) and wedge(b,a)[1]==dest else 0 for b in B2])
  A=s.Matrix(maps) if maps else s.zeros(0,6)
  ann_dim=6-A.rank()
  exceptional=(r,ind)==(2,1)
  assert ann_dim==(5 if exceptional else 6)
  both_one=(ind<=1 and r-ind<=1)
  assert both_one==exceptional
  table.append({'rank':r,'index':ind,'common_annihilator_dim':ann_dim,'both_H1_possible':both_one})

# Entry-specific positive elliptic coefficient ranks 0..3.
elliptic=[]
for rr in range(4):
 S=tuple(range(1,rr+1)); cols=[zcol((0,j)) for j in S]
 z=s.Matrix.hstack(*cols) if cols else s.zeros(6,0)
 wedge_constraints=[]
 for v in S:
  wedge_constraints.append([wedge(b,(v,))[0] if 0 not in b and wedge(b,(v,))[1]==(1,2,3) else 0 for b in B2])
 A=s.Matrix(wedge_constraints) if wedge_constraints else s.zeros(0,6)
 ZQ=z.T*Q
 assert A.rank()==ZQ.rank()==rr
 assert s.Matrix.vstack(A,ZQ).rank()==rr
 st=stats(cols)
 assert st=={'z':rr,'radical':rr,'surviving':6-2*rr}
 elliptic.append(st)

# Negative elliptic pair: its full three-space is self-perpendicular.
ell_z=s.Matrix.hstack(*(zcol((0,j)) for j in (1,2,3)))
assert ell_z.T*Q*ell_z==s.zeros(3)
assert s.Matrix.hstack(*((ell_z.T*Q).nullspace())).columnspace()==ell_z.columnspace()

# Numerically trivial line, arbitrary actual entry span E of dimension 0..4.
trivial=[]
for rr in range(5):
 cols=[]
 for i in range(rr):
  for j in V:
   sign,pair=wedge((i,),(j,))
   if sign:cols.append(sign*zcol(pair))
 z=s.Matrix.hstack(*cols) if cols else s.zeros(6,0)
 if cols:z=s.Matrix.hstack(*z.columnspace())
 rows=[]
 for i in range(rr):
  for dest in B3:
   rows.append([wedge(b,(i,))[0] if wedge(b,(i,))[1]==dest else 0 for b in B2])
 A=s.Matrix(rows) if rows else s.zeros(0,6)
 assert s.Matrix.vstack(A,z.T*Q).rank()==A.rank()==(z.T*Q).rank()
 trivial.append({'entry_span_dim':rr,**stats(list(z.columnspace()))})

# Complete threshold statements, integer ranges only.
for blocks in range(4,31):
 allowed=[rr for rr in range(4) if (6-2*rr)*blocks<=18]
 if blocks>=10:assert allowed==[3]
 elif blocks>=5:assert min(allowed)==2
 else:assert min(allowed)==1

root=base.parents[1]/'sixfolds'
proofs=['rm_surface_support_wedge_gate_draft.md','rm_actual_elliptic_coupling_gate_draft.md']
out={'status':'PASS','scope':'independent exact exterior algebra and threshold arithmetic; no isogeny, equivariance, or extension gluing computed','wedge_matrix':[[int(x) for x in row] for row in Q.tolist()],'surface_configurations':surfaces,'all_rank_index_cases':table,'positive_elliptic_coefficients':elliptic,'trivial_line_entry_spans':trivial,'proof_hashes':{p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in proofs},'elapsed_seconds':time.perf_counter()-start}
(base/'audit_surface_elliptic_gates.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
