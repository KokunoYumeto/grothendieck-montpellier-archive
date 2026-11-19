#!/usr/bin/env python3
"""Independent small exact check supporting the U13 code review.

Does not rerun or modify the root U13 program. Retains output alongside this
review and checks only the two explicit polynomials and the finite pair count.
"""
from pathlib import Path
import json
import sympy as s

T=s.symbols('T')
Q=s.Poly((T*T+5*T+13)*(T**4+7*T**3+20*T*T+19*T+1)**3,T)
F=s.Poly((T*T+5*T+13)*(T**4+247*T**3+3380*T*T+15379*T+28561)**3,T)
fricke=s.expand(T**14*F.as_expr().subs(T,13/T)-13**13*Q.as_expr())
assert fricke==0
coefficient_checks={r:int(F.nth(14-r)-13**(r-1)*Q.nth(r)) for r in range(2,15)}
assert all(v==0 for v in coefficient_checks.values())
assert F.nth(13)==746
assert F.nth(1)==2*F.nth(0)
primes=[2,3,5,7,11,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
old=sum(len(range(1,min(1000//ell,5300//ell))) for ell in primes)
new=sum(len(range(1,min(1000//ell,5299//ell)+1)) for ell in primes)
assert (old,new)==(1691,1715)
out={'scope':'Independent polynomial identities and finite-loop pair counts; not a rerun of c63_u13.py',
     'fricke_residual':str(fricke),'F_coefficient_T13':int(F.nth(13)),
     'coefficient_residuals_r2_to_r14':coefficient_checks,
     'reciprocal_root_sum':str(-F.nth(1)/F.nth(0)),
     'old_Hecke_pair_count':old,'inclusive_Hecke_pair_count':new}
outpath=Path(__file__).resolve().parents[1]/'outputs/c63_u13_polynomial_review.json'
outpath.parent.mkdir(parents=True,exist_ok=True)
outpath.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
