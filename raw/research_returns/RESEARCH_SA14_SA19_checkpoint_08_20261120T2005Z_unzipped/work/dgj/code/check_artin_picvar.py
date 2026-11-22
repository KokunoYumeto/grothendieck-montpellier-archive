#!/usr/bin/env python3
"""Exact dual-number certificate for D4a; geometric ST proof is in the text."""
from pathlib import Path
import json,time
start=time.perf_counter()
# F_2[epsilon]/epsilon^2: (constant, epsilon coefficient).
def mul(x,y):return ((x[0]*y[0])%2,(x[0]*y[1]+x[1]*y[0])%2)
one=(1,0); q=(1,1)
assert mul(q,q)==one and q!=one
matrix=[[one,q],[one,one]]
dual=[[matrix[j][i] for j in range(2)] for i in range(2)]
assert dual[1][0]==q
assert matrix[1]==[one,one]
result={'base':'F_2[epsilon]/epsilon^2','q_matrix':[['1','1+epsilon'],['1','1']],
'dual_q_matrix':[['1','1'],['1+epsilon','1']],
'involution_square_condition':list(mul(q,q)),
'affine_norm_second_row':['1','1'],
'picvar_lift_criterion':{'left':'1','right':'1+epsilon','difference':'epsilon != 0'},
'scope':'Certifies the finite ring arithmetic. The written proof supplies Serre-Tate existence and nonexistence of an abelian Picvar lift.',
'runtime_seconds':round(time.perf_counter()-start,6)}
p=Path(__file__).with_name('check_artin_picvar_output.json');p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
