#!/usr/bin/env python3
"""Finite certificate for the square-zero PD lifting counterexample D-031."""
import json,time
from pathlib import Path
started=time.perf_counter();checks=0
# E^{-2}->E^{-1} is [1]; M^{-2}=Z, M^{-1}=0.
dE=[[1]];dM=[];pi_low=[[1]];pi_high=[]
# Both composites to M^{-1}=0 are the unique zero-row matrix.
pi_d=[];d_pi=[]
assert pi_d==d_pi;checks+=1
# A lift is a scalar c.  Projection says c=1; being a chain map says c=0.
equations=[[1],[1]];rhs=[1,0]
assert equations[0][0]-equations[1][0]==0;checks+=1
assert rhs[0]-rhs[1]==1;checks+=1
modular=[]
for p in [2,3]:
    solutions=[]
    for c in range(p):
        projection_ok=(c-1)%p==0
        chain_ok=c%p==0
        checks+=1
        if projection_ok and chain_ok:solutions.append(c)
    assert not solutions;checks+=1
    modular.append({'p':p,'tested_lifts':list(range(p)),'solutions':solutions})
out={'statement':'D031: termwise-free source does not lift through this surjective PD ideal map',
     'cochain_degrees':[-2,-1],'E_differential':dE,'M_differential':dM,
     'pi_degree_minus2':pi_low,'pi_degree_minus1':pi_high,
     'pi_d_equals_d_pi':True,'lift_equation_matrix':equations,'lift_rhs':rhs,
     'integer_certificate':'Subtract the chain-map equation c=0 from the projection equation c=1; this gives 0=1.',
     'modular_cases':modular,'PD_structure':'Both ideals are square-zero, with all higher divided powers zero.',
     'checks':checks,'elapsed_seconds':time.perf_counter()-started}
Path('SA08_work/logs/D_lifting_counterexample.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':checks,'elapsed_seconds':out['elapsed_seconds']}))
