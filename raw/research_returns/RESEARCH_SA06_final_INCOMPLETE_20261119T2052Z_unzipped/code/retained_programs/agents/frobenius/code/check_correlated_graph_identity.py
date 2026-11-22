#!/usr/bin/env python3
"""Exact finite certificate for the abstract C.4z graph obstruction.

The all-level topological descent is proved in the text, not by enumeration.
"""
from pathlib import Path
from datetime import datetime,timezone
from time import perf_counter
from itertools import product,combinations
import json
import sympy as S

tic=perf_counter();started=datetime.now(timezone.utc).isoformat()
L=S.Matrix([[1,0,1,0],[1,0,0,0],[0,1,0,1],[0,0,0,1],
            [2,1,1,1],[0,0,1,1]])
R=S.Matrix([[-1,-1,-1,0,1,0],[-1,1,0,-1,0,1]])
assert R*L==S.zeros(2,4)
assert abs(L[:4,:].det())==1 and R[:,4:]==S.eye(2)
minors=[]
for s in range(3):
    ms=[int(L[2*s:2*s+2,list(cols)].det()) for cols in combinations(range(4),2)]
    assert 1 in ms or -1 in ms;minors.append(ms)
f=lambda x,y:x-x*x+y*y-2*x*y
checks=0
for x,y in product(range(4),repeat=2):
  for s,a,b in product(range(3),range(2),range(2)):
    flux=S.eye(2)[:,b];step=R[:,2*s+a]
    flow=L[2*s:2*s+2,:].T*flux
    delta=f(x+int(step[0]),y+int(step[1]))-f(x,y)
    actual=int(delta*flow[0])%4
    expected=(1 if s==0 else 2 if s==2 and a==1 and b==0 else 0)
    assert actual==expected,(x,y,s,a,b,actual,expected)
    checks+=1
# Reconstruct the three forms from the type-(1,2) symplectic calculation.
D=S.diag(1,2);B=[S.diag(1,0),S.diag(0,2),2*S.ones(2)]
forms=[]
for s,Bs in enumerate(B):
    Q=(2*D.inv()*Bs*D.inv()).row_join(D.inv()*Bs).col_join((Bs*D.inv()).row_join(Bs))
    assert Q==L[2*s:2*s+2,:].T*L[2*s:2*s+2,:]
    forms.append(Q.tolist())
E=S.zeros(2).row_join(D).col_join((-D).row_join(S.zeros(2)))
Omega=E.row_join(S.eye(4)).col_join((-S.eye(4)).row_join(-2*E.inv()))
assert Omega.det()==1
out={'started_utc':started,'runtime_seconds':perf_counter()-tic,
     'scope':'Exact lattice and relaxed-axis mod4 identity; no geometric transfer or numerical proof of level descent',
     'RL_zero':True,'first_four_rows_determinant':int(L[:4,:].det()),
     'block_two_by_two_minors':minors,'relaxed_axis_basis_flux_checks':checks,
     'all_relaxed_axis_checks_pass':True,'principal_form_determinant':int(Omega.det()),
     'three_correlated_forms':forms,'odd_scalar_target_mod4':2}
p=Path(__file__).resolve().parents[1]/'output'/'check_correlated_graph_identity.json'
p.write_text(json.dumps(out,indent=2,default=int)+'\n');print(json.dumps(out,indent=2,default=int))
