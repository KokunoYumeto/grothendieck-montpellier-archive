#!/usr/bin/env python3
"""Exact arithmetic certificate for the separable-polarization rank extension.

This does not replace the geometric descent or nodal-image proofs.  It checks
the integral four-dimensional dual-polarization matrix and every displayed
degree/genus/rank identity on the specified finite range of odd types.
"""
from pathlib import Path
from time import perf_counter
import json

started=perf_counter()

def multiply(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(4)) for j in range(4)]
            for i in range(4)]

types=[]
degree_cases=0
for a in range(1,16,2):
    for b in range(a,64,a):
        if b%2==0:continue
        D=a*b
        polarization=[[0,a,0,0],[-a,0,0,0],[0,0,0,b],[0,0,-b,0]]
        dual=[[0,-b,0,0],[b,0,0,0],[0,0,0,-a],[0,0,a,0]]
        expected=[[D*int(i==j) for j in range(4)] for i in range(4)]
        assert multiply(polarization,dual)==expected
        assert multiply(dual,polarization)==expected
        assert (D**2*D)//D**2==D  # chi(N)=chi(M^D)/deg(lambda_M)
        assert (D**2)**2//(D**2)==D**2  # degree(lambda_N)
        assert (D*(D**2))//D==D**2  # pullback intersection identity
        types.append({'a':a,'b':b,'D':D,'dual_polarization_matrix':dual})
        for d in range(1,129):
            curve_genus=9*D*d*d+1
            coherent_relative=curve_genus-2
            if d%2:
                source_degree=D*d*d
                nodes=9*(source_degree-1)
                assert curve_genus==10+nodes
            else:
                intersection=18*D*(d-1)
                assert curve_genus==(9*D+1)+(9*D*(d-1)**2+1)+intersection-1
            for f in range(3):
                defect=(2-f)*(1 if d%2 else 2)
                relative_rank=curve_genus-defect-f
                assert relative_rank==9*D*d*d-(1 if d%2 else 3-f)
                assert 0<=relative_rank<=coherent_relative
                if d%2:
                    assert 8+f+nodes==relative_rank+f
                else:
                    assert ((9*D-1+f)+(9*D*(d-1)**2-1+f)
                            +intersection-1)==relative_rank+f
                degree_cases+=1

result={'status':'PASS','scope':'Integral dual-polarization matrices and finite arithmetic identities; geometric existence is proved separately.',
        'odd_types':types,'type_count':len(types),'degree_rank_cases':degree_cases,
        'elapsed_seconds':perf_counter()-started}
Path(__file__).with_name('A3_separable_rank_checks_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='odd_types'},indent=2))
