#!/usr/bin/env python3
"""Exact arithmetic certificate for the terminal contradiction in A-024."""
from pathlib import Path
import json,time
import sympy as s
start=time.perf_counter();T=s.Symbol('T');checks=0
beta=lambda n:s.prod(T-j for j in range(n))/s.factorial(n)
for n in range(2,17):
 assert s.expand(n*beta(n)-(T-n+1)*beta(n-1))==0
 checks+=1
assert s.expand(2*beta(2)-(T*T-T))==0;checks+=1
residues=[{'h_beta2_mod2':a,'left':(2*a)%2,'right':(-1)%2,'solves':(2*a+1)%2==0} for a in (0,1)]
assert not any(r['solves'] for r in residues);checks+=1
# Formal shuffle faces after the simplicial identities and normalization:
# d0=s0(f) z-u s0(0)=fz; d1=uz-uz=0; d2=u s0(0)-s0(0)z=0.
shuffle_faces={'d0':{'f*z':1},'d1':{},'d2':{}}
result={'statement':'A-024','scope':'Exact polynomial identities n=2..16 and exhaustive modulo-two contradiction; structural shuffle proof is written in the paper',
        'residue_cases':residues,'normalized_shuffle_faces':shuffle_faces,'assertions_passed':checks,
        'elapsed_seconds':time.perf_counter()-start}
p=Path(__file__).resolve().parents[1]/'logs/D_first_stage_obstruction.json'
p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
