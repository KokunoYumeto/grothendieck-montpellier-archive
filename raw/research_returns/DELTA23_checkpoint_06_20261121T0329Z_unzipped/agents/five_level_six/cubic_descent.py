#!/usr/bin/env python3
"""Exact signed finite identities for the universal cubic descent, D23.F22."""
from pathlib import Path
import json
import numpy as np

HERE=Path(__file__).resolve().parent
I=np.eye(2,dtype=np.int64)
U=np.array([[1,1],[0,1]],dtype=np.int64)
L=np.array([[1,0],[2,1]],dtype=np.int64)
S=np.array([[0,1],[2,0]],dtype=np.int64)
R=np.array([[0,2],[1,2]],dtype=np.int64)

def mul(*args):
    out=I.copy()
    for a in args:out=out@a%3
    return out
def power(a,n):
    if n<0:a=inv(a);n=-n
    out=I.copy()
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
def inv(a):
    det=int(a[0,0]*a[1,1]-a[0,1]*a[1,0])%3
    return pow(det,-1,3)*np.array([[a[1,1],-a[0,1]],[-a[1,0],a[0,0]]])%3

V=mul(S,R,inv(S))
EX=mul(inv(R),inv(V))
EY=mul(inv(V),inv(R))
assert np.array_equal(EX,-power(U,2)%3)
assert np.array_equal(EY,-power(L,2)%3)
assert np.array_equal(R,mul(power(U,2),power(L,2),power(U,-2)))
rows=[]
for rho in range(3):
    M=np.array([[1,rho],[rho,1+rho*rho]],dtype=np.int64)%3
    C=mul(power(U,2),M,power(U,-2))
    allowed=[]
    for rho_d in range(3):
        T=mul(C,power(U,2*rho_d))
        if np.array_equal(mul(T,R),mul(R,T)):
            allowed.append(rho_d)
    assert allowed==[rho]
    assert np.array_equal(mul(C,power(U,2*rho)),power(R,rho))
    signs=[]
    for half in [0,1]:
        t=3*half
        A=mul(power(EX,-t),inv(C))
        T=mul(inv(A),power(U,2*rho))
        assert np.array_equal(T,((-1)**half)*power(R,rho)%3)
        signs.append(T.tolist())
    rows.append({'rho':rho,'C':C.tolist(),'rho_descent':rho,'T_for_half_0_1':signs})
result={'E_r':R.tolist(),'E_srs':V.tolist(),'E_x':EX.tolist(),'E_y':EY.tolist(),'cases':rows}
(HERE/'cubic_descent.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS signed E-images, conjugate pure pair, all three shear residues and both half-character signs')
