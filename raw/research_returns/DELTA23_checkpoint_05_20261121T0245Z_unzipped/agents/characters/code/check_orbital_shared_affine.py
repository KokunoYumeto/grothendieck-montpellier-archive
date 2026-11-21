#!/usr/bin/env python3
"""Exact 96-case replay of the C20 affine shared-conjugacy identity."""
from pathlib import Path
import json,numpy as np
HERE=Path(__file__).resolve().parents[1]
I=np.eye(3,dtype=np.int64)
def m(*args):
    out=I.copy()
    for a in args:out=out@a%3
    return out
def pw(a,n):
    if n<0:
        # All group elements here have finite order dividing 24.
        out=I.copy()
        for k in range(1,25):
            out=m(out,a)
            if np.array_equal(out,I):return pw(a,n%k)
        raise AssertionError('unexpected order')
    out=I.copy()
    while n:
        if n&1:out=m(out,a)
        a=m(a,a);n//=2
    return out
def aff(v,A):
    out=I.copy();out[:2,:2]=A;out[:2,2]=v
    return out%3
def conj(a,b):return m(a,b,pw(a,-1))
U=np.array([[1,1],[0,1]],dtype=np.int64)
L=np.array([[1,0],[2,1]],dtype=np.int64)
a=aff([0,0],U);b0=aff([0,0],L);c=aff([1,0],U)
r=m(a,b0);s=m(a,b0,a);K=pw(c,2);Z=pw(r,3);P=pw(m(a,b0,c),2)
dE=m(r,K);dH=m(s,c)
assert np.array_equal(conj(P,dH),dE)
assert np.array_equal(pw(Z,2),I)
R0=aff([0,0],-(U@L)%3)
T_values=[m(pw(Z,e),pw(R0,j)) for e in range(2) for j in range(3)]
W_values=[pw(s,j) for j in range(4)]
cases=0
for T in T_values:
    for W in W_values:
        for half3 in range(2):
            for psi2 in range(2):
                C_E=m(pw(Z,-half3),T);C_H=m(pw(Z,-psi2),W)
                E=conj(C_E,dE);H=conj(C_H,dH)
                common=m(C_E,P,pw(C_H,-1))
                assert np.array_equal(E,conj(common,H))
                cases+=1
assert cases==96
out={'statement':'D23.C20','independent_frame_pairs':24,'all_b_p_parities':4,
     'checked_cases':cases,'eta_rK':dE.tolist(),'eta_sc':dH.tolist(),
     'eta_P':P.tolist(),'result':'PASS',
     'scope':'Shared conjugacy under affine covariance only; full common-word orbital equations not asserted automatic.'}
(HERE/'records/orbital_shared_affine.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
