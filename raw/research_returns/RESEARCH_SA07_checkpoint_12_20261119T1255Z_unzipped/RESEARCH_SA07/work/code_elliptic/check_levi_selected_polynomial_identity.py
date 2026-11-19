#!/usr/bin/env python3
"""Independent Q[s] check of the selected seven-row Levi certificate."""
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path
from time import perf_counter
import json,pickle
import sympy as sp
here=Path(__file__).resolve().parent
src=here.parent/'calc_levi_selected_identity.pickle'
start=datetime.now(timezone.utc).isoformat();t0=perf_counter()
data=pickle.loads(src.read_bytes());s=data['s']
M,K,L,N,d=[data[k] for k in ('M','K','L','numerator','denominator')]
assert M.shape==(7,12) and K.shape==(5,12) and L.shape==(3,5) and N.shape==(3,7)
J=sp.Matrix([[-104,-288],[-26,-72],[104,288],[32,192],[-32,-192]])
assert J.rank()==2 and L.rank()==3 and L*J==sp.zeros(3,2)
assert data['LK']==L*K
defect=N*M-d*L*K
assert all(sp.Poly(value,s,domain=sp.QQ).is_zero for value in defect)
expected=-3057647616*(s-1)*(s+1)*(s+2)*(s+5)*(2*s-1)*(2*s+1)**6*(2*s+3)*(4*s*s+6*s-1)
assert sp.Poly(d-expected,s,domain=sp.QQ).is_zero
cols=data['pivots'];assert len(cols)==7
assert M[:,cols].subs(s,3).det()!=0
print('SHAPES',M.shape,K.shape,L.shape,N.shape)
print('OUTPUT_SUBSPACE: ker(L)=image(J), dimensions2 and2')
print('POLYNOMIAL_DEFECTS',len(defect),'ALL_ZERO')
print('DENOMINATOR',sp.factor(d))
print('DENOMINATOR_NONZERO_FOR_INTEGER_s_GE_3: all linear factors positive; 4s^2+6s-1>=53')
print('PIVOT_MINOR_AT_s3',M[:,cols].subs(s,3).det())
elapsed=perf_counter()-t0
print('PASS: kernel(M(s)) subset kernel(L K(s)) for every integer s>=3')
print('SCOPE: exact polynomial identity using retained verified row polynomials')
print('ACTUAL_WALL_SECONDS',f'{elapsed:.9f}')
(here/'check_levi_selected_polynomial_identity.json').write_text(json.dumps(dict(
start_utc=start,wall_seconds=elapsed,exit_code=0,input_sha256=sha256(src.read_bytes()).hexdigest(),
input=str(src),polynomial_defects=36),indent=2)+'\n')
