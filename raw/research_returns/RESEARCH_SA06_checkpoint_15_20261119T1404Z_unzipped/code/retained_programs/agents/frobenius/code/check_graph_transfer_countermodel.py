#!/usr/bin/env python3
"""Exact finite identities for the ppav-surface transfer countermodel.

This checks the terminal modulo-four obstruction and elementary lattices.
The arbitrary-level reduction is the written homotopy proof, not a finite test.
"""
from datetime import datetime, timezone
from time import perf_counter
from pathlib import Path
import json
import sympy as S

started = datetime.now(timezone.utc).isoformat()
t0 = perf_counter()
L = S.Matrix([[1,0],[0,1],[2,1]])
R = S.Matrix([[-2,-1,1]])
assert R*L == S.zeros(1,2)
assert L[:2,:].det() == 1
checks = []
for x in range(4):
    for axis in range(3):
        displacement = int(R[0,axis])
        flow = int(L[axis,0])
        difference = ((x+displacement)**2-x*x) % 4
        actual = flow*difference % 4
        expected = 2 if axis == 2 else 0
        assert actual == expected
        checks.append(dict(vertex=x,axis=axis+1,flow=flow,
                           displacement=displacement,difference=difference,
                           contribution=actual))
forms = [L[i,:].T*L[i,:] for i in range(3)]
coordinates = S.Matrix([[Q[0,0],Q[0,1],Q[1,1]] for Q in forms])
assert coordinates.det() == -2
result = dict(started_utc=started, seconds=perf_counter()-t0,
              checks=len(checks),passed=True,
              L=L.tolist(),R=R.tolist(),RL=(R*L).tolist(),
              first_two_rows_determinant=int(L[:2,:].det()),
              monodromy_forms=[Q.tolist() for Q in forms],
              symmetric_coordinate_determinant=int(coordinates.det()),
              terminal_checks=checks,
              scope="Exact terminal identities only; arbitrary levels use the written rounding proof; no C4 surface counterexample inferred.")
output=Path(__file__).resolve().parents[1]/'output'/'check_graph_transfer_countermodel.json'
output.write_text(json.dumps(result,indent=2,default=int)+'\n')
print(json.dumps(result,indent=2,default=int))
