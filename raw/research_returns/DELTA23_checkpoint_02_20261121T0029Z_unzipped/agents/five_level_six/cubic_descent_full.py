#!/usr/bin/env python3
"""Finite permutation normalization and exact eigenlocus factorization, F23."""
from pathlib import Path
import json
import numpy as np
import sympy as sp

HERE=Path(__file__).resolve().parent
S=np.array([[0,1],[1,0]],dtype=np.int64)
R=np.array([[0,1],[1,1]],dtype=np.int64)
I=np.eye(2,dtype=np.int64)
T=S@R%2
def power(a,n):
    out=I.copy()
    for _ in range(n):out=out@a%2
    return out
def inverse(a):
    for n in range(6):
        b=power(a,n)
        if np.array_equal(a@b%2,I):return b
    raise AssertionError('not an S3 matrix')
rows=[]
for lam in [1,5]:
    epsilon=1 if lam%3==1 else -1
    m=(lam-1)//2;b=(1-epsilon)//2
    K=power(T,b)@power(R,m)%2
    assert np.array_equal(K@S@inverse(K)%2,S)
    assert np.array_equal(K@power(R,lam%3)@inverse(K)%2,R)
    rows.append({'lambda_mod6':lam,'m_mod3':m%3,'b':b,'normalizer_in_S3':K.tolist()})
z=sp.symbols('z');d=sp.sqrt(-3)
n=(1+d)/2;nb=(1-d)/2;t=(z-nb)/(z-n);b=1-t**3
left=256*(1-z+z*z)**3/(1728*z*z*(1-z)**2)
assert sp.simplify(left-4*(b-1)/(b*b))==0
result={'statement':'D23.F23','permutation_normalizations':rows,
        'factorization':'j(z)/1728=4(b-1)/b^2, b=1-((z-bar(n))/(z-n))^3',
        'factorization_exact_symbolic_check':True,'result':'PASS'}
(HERE/'cubic_descent_full.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS both multiplier cases in S3 and exact cubic/harmonic/Legendre factorization')
