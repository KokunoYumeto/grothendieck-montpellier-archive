"""Exploratory LP vertex search, with exact rational certificates.

No absence of a counterexample is treated as a theorem.  A rational axial
array is not automatically a balanced SL_n^3 tensor: the no-two-slot-overlap
condition is recorded separately, and no full stabilizer is computed here.
"""
import json
import math
from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
import sympy as sp

OUT = Path(__file__).with_name("tensor_denominator_experiments.json")
rng = np.random.default_rng(20261121)
report = {"seed": 20261121, "trials_per_n": 300, "status": "exploratory", "by_n": []}

def two_part(d):
    return d & -d

def linear_support(edges):
    for a,b in [(0,1),(0,2),(1,2)]:
        pairs=[(e[a],e[b]) for e in edges]
        if len(set(pairs)) != len(pairs):
            return False
    return True

for n in range(4,11):
    edges=list(product(range(n), repeat=3))
    row=[]; col=[]
    for t,(i,j,k) in enumerate(edges):
        row.append(i); col.append(t)
        if j<n-1: row.append(n+j); col.append(t)
        if k<n-1: row.append(2*n-1+k); col.append(t)
    A=coo_matrix((np.ones(len(row)),(row,col)),shape=(3*n-2,n**3)).tocsr()
    stats={"n":n,"solved":0,"fractional":0,"linear":0,
           "max_two_part":1,"max_linear_two_part":1,"certificates":[]}
    for trial in range(300):
        cost=rng.normal(size=n**3)
        ans=linprog(cost,A_eq=A,b_eq=np.ones(3*n-2),bounds=(0,None),method="highs-ds")
        if not ans.success: continue
        stats["solved"]+=1
        supp=np.flatnonzero(ans.x>1e-8)
        vals=[Fraction(float(ans.x[i])).limit_denominator(2**22) for i in supp]
        den=math.lcm(*(x.denominator for x in vals))
        if den==1: continue
        stats["fractional"]+=1
        selected=[edges[i] for i in supp]
        linear=linear_support(selected)
        stats["linear"]+=int(linear)
        d2=two_part(den)
        if d2<=stats["max_two_part"] and not(linear and d2>stats["max_linear_two_part"]):
            continue
        # Certify the complete rational array and column independence exactly.
        B=sp.Matrix(3*n,len(supp),lambda r,c:int(r in (selected[c][0],n+selected[c][1],2*n+selected[c][2])))
        v=sp.Matrix([sp.Rational(x.numerator,x.denominator) for x in vals])
        if B*v!=sp.ones(3*n,1) or any(x<=0 for x in vals):
            continue
        if B.rank()!=len(supp):
            continue
        stats["max_two_part"]=max(stats["max_two_part"],d2)
        if linear: stats["max_linear_two_part"]=max(stats["max_linear_two_part"],d2)
        cert={"trial":trial,"denominator":den,"two_part":d2,
              "exceeds_chain":d2>2**(n-1),"no_two_slot_overlap":linear,
              "support":[[i+1,j+1,k+1] for i,j,k in selected],
              "weights":[[v.numerator,v.denominator] for v in vals],
              "exact_all_marginals_one":True,"exact_columns_independent":True}
        stats["certificates"].append(cert)
        print("certificate",n,trial,den,d2,"linear",linear,"exceeds",cert["exceeds_chain"],flush=True)
    report["by_n"].append(stats)
    OUT.write_text(json.dumps(report,indent=2))
    print("summary",n,{k:v for k,v in stats.items() if k!="certificates"},flush=True)
