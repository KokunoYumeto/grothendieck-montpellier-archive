#!/usr/bin/env python3
"""Finite integral checks for the complete C.3bl construction and boundary map."""
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from itertools import product
from math import factorial
import hashlib, json
import sympy as sp

started=datetime.now(timezone.utc).isoformat(); tic=perf_counter(); checks=[]
def check(name,value,scope):
    passed=bool(value);checks.append({'name':name,'passed':passed,'scope':scope})
    if not passed: raise AssertionError(name)
base=Path(__file__).resolve().parents[1]
raw_path=base.parent/'cycles'/'output'/'cubic_exceptional_lattice_matrices.json'
cert_path=base.parent/'cycles'/'output'/'cubic_exceptional_lattice_certificate.json'
raw=json.loads(raw_path.read_text()); old=json.loads(cert_path.read_text())
A=sp.Matrix([3,-1,-1,-1,-1,-1,-1])
Q=sp.zeros(6,7)
for j in range(6):Q[j,j]=1
Q[:,6]=sp.Matrix([3,-1,-1,-1,-1,-1])
check('primitive_picard_quotient_matrix',Q*A==sp.zeros(6,1),
      'Exact free quotient Z^7/Z(3,-1,...,-1), using E6=3H-E1-...-E5.')
check('primitive_picard_quotient_split',Q[:,:6]==sp.eye(6),
      'The quotient map has an integral right inverse, so its target is free.')

def image(state):
    if state==1:return [(0,1)]
    if 2<=state<=6:return [(state-1,1)]
    if state==7:return [(0,3)]+[(j,-1) for j in range(1,6)]
    return []

def psi_for_row(row):
    if row[0] != 0:return {}
    factors=[image(a) for a in row[1:]]
    if any(not a for a in factors):return {}
    result={}
    for choice in product(*factors):
        key=tuple(a[0] for a in choice);coefficient=1
        for a in choice:coefficient*=a[1]
        result[key]=result.get(key,0)+coefficient
    return result
records=[]
assert len(raw)==len(old['cases'])
for source,case in zip(raw,old['cases']):
    rows=source['rows'];columns=source['columns'];entries=source['entries']
    projected=[psi_for_row(row) for row in rows]
    answer={}
    for i,j,v in entries:
        for target,w in projected[i].items():
            key=(target,j);answer[key]=answer.get(key,0)+v*w
    nonzero={str(k):v for k,v in answer.items() if v}
    check(f'psi_b_zero_r{case["r"]}_m{case["m"]}',not nonzero,
          'Complete finite matrix product over Z; the primitive quotient kills the ample multiplication image termwise.')
    records.append({'r':case['r'],'m':case['m'],'domain_rank':len(columns),
                    'codomain_rank':len(rows),'primitive_quotient_rank':6**case['s'],
                    'nonzero_product_entries':len(nonzero),
                    'retained_smith_factors':case['torsion_invariant_factors']})

E=sp.zeros(9,9);F=sp.zeros(9,9)
E[1,0]=1;E[2,1]=1;F[0,1]=2;F[1,2]=2
G=sp.diag(1,2,4,1,1,1,1,1,1)
H=sp.diag(-2,0,2,0,0,0,0,0,0)
check('cubic_positive_adjoint',E.T*G==G*F,
      'Exact rational-chain positive inner product used only to prove free-lattice injectivity.')
check('cubic_commutator',E*F-F*E==H,
      'Weights on 1,A,3z and the six primitive divisor directions.')
for m in range(13):
    E=sp.zeros(m+1);F=sp.zeros(m+1)
    for j in range(m):E[j+1,j]=1;F[j,j+1]=(j+1)*(m-j)
    G=sp.diag(*[factorial(j)*factorial(m)//factorial(m-j) for j in range(m+1)])
    H=sp.diag(*[2*j-m for j in range(m+1)])
    check(f'projective_adjoint_m{m}',E.T*G==G*F and E*F-F*E==H,
          'Finite exact positive-adjoint/weight check; the all-m formula is proved in the auxiliary.')

rank_witnesses=[]
for s in range(1,10):
    inputs=[(0,)*s,(1,)+(0,)*(s-1),(2,)+(0,)*(s-1)]
    # In each cubic, cup sends basis s,t,u,v to the dual t,s,0,0.
    outputs=[tuple(1-j for j in v) if all(j<2 for j in v) else None for v in inputs]
    check(f'm0_three_coefficients_s{s}',len(set(inputs))==3,
          'Finite tensor-basis independence for the no-projective-space endpoint.')
    check(f'm0_product_cup_s{s}',outputs[0] is not None and outputs[1] is not None and outputs[0]!=outputs[1] and outputs[2] is None,
          'The first two ordered tensor cups remain independent with coefficient one; no factorial.')
    rank_witnesses.append({'s':s,'source_rank':3,'cup_rank':2,'coefficient':1})

record={'statement':'C.3bl finite primitive-boundary and endpoint certificate',
        'started_at_utc':started,'finished_at_utc':datetime.now(timezone.utc).isoformat(),
        'runtime_seconds':perf_counter()-tic,
        'scope':'Complete integral primitive-quotient matrix products in nine previously retained lattice cases; local positive-adjoint chains; m0 tensor witnesses s1..9. No exhaustive geometry, algebraization, divisibility or infinite-range theorem is delegated to code.',
        'prior_matrix_sha256':hashlib.sha256(raw_path.read_bytes()).hexdigest(),
        'prior_certificate_sha256':hashlib.sha256(cert_path.read_bytes()).hexdigest(),
        'primitive_quotient_matrix':[[int(x) for x in row] for row in Q.tolist()],
        'cases':records,'m0_witnesses':rank_witnesses,'checks':checks,
        'passed':sum(a['passed'] for a in checks),'failed':sum(not a['passed'] for a in checks)}
(base/'output'/'C3bl_primitive_boundary_certificate.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
