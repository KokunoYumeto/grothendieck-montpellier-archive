#!/usr/bin/env python3
"""Independent exact wedge and incidence arithmetic for E831."""
from itertools import combinations
from pathlib import Path
import hashlib,json,time
import sympy as s

t0=time.perf_counter();base=Path(__file__).resolve().parent
pairs=list(combinations(range(4),2))
def alt_sign(seq):
 if len(set(seq))<len(seq):return 0
 return -1 if sum(a>b for i,a in enumerate(seq) for b in seq[i+1:])%2 else 1
Q=s.Matrix([[alt_sign(a+b) for b in pairs] for a in pairs])
assert Q.det()==-1
def wedge(v,w):return s.Matrix([v[i]*w[j]-v[j]*w[i] for i,j in pairs])
def invariant(columns):
 z=s.Matrix.hstack(*columns) if columns else s.zeros(6,0)
 cols=z.columnspace();z=s.Matrix.hstack(*cols) if cols else s.zeros(6,0)
 rad=z.cols-(z.T*Q*z).rank()
 ann=(z.T*Q).nullspace();a=s.Matrix.hstack(*ann) if ann else s.zeros(6,0)
 assert a.cols==6-z.cols
 w=6-z.cols-rad
 assert (a.T*Q*a).rank()==w
 return [z.cols,rad,w]
e=list(s.eye(4).columnspace())
tests={
 'zero':[], 'single':[wedge(e[0],e[1])],
 'complementary':[wedge(e[0],e[1]),wedge(e[2],e[3])],
 'intersecting':[wedge(e[0],e[1]),wedge(e[0],e[2])],
 'alpha':[wedge(e[0],e[i]) for i in (1,2,3)],
 'beta':[wedge(e[i],e[j]) for i,j in ((0,1),(0,2),(1,2))]
}
expected={'zero':[0,0,6],'single':[1,1,4],'complementary':[2,0,4],'intersecting':[2,2,2],'alpha':[3,3,0],'beta':[3,3,0]}
assert {k:invariant(v) for k,v in tests.items()}==expected

# The two isotropic families are checked after several independent basis changes.
changes=[s.eye(4),s.Matrix([[1,2,0,1],[0,1,1,0],[1,0,1,2],[0,0,0,1]]),s.Matrix([[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,2]])]
for g in changes:
 assert g.det()!=0
 v=list(g.columnspace())
 assert invariant([wedge(v[0],v[i]) for i in (1,2,3)])==[3,3,0]
 assert invariant([wedge(v[i],v[j]) for i,j in ((0,1),(0,2),(1,2))])==[3,3,0]

# Abstract six-vertex data only: one rank-three elliptic component.
vertices=[tests['alpha'],tests['alpha'],[],[],[],[]]
local=[invariant(v)[2] for v in vertices]
assert sum(local)==24 and invariant(tests['alpha'])[2]==0

budgets=[]
for n in range(4,101):
 ell=n-3
 maxrank=(ell+1)//2
 rankone=(3*ell+1)//2
 assert 6*maxrank>=3*n-9 and 6*(maxrank-1)<3*n-9
 assert 2*rankone>=3*n-9 and 2*(rankone-1)<3*n-9
 budgets.append([n,maxrank,rankone])
assert next(row for row in budgets if row[0]==32)==[32,15,44]
proof=base.parents[1]/'sixfolds/rm_vertexwise_coupling_gate_draft.md'
out={'status':'PASS','scope':'independent finite exterior and incidence arithmetic; no geometric realization or infinite classification certified by computation','wedge_cases':expected,'maximal_isotropic_basis_changes':len(changes),'hypothetical_vertexwise_survivors':local,'hypothetical_total':sum(local),'hypothetical_common_space':0,'budget_count':len(budgets),'N32_budget':[15,44],'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'elapsed_seconds':time.perf_counter()-t0}
(base/'audit_vertexwise_coupling.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
