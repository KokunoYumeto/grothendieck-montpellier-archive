#!/usr/bin/env python3
"""Exact comparison maps for the symmetric-square and stabilizer H1 route."""
from datetime import datetime,timezone
from pathlib import Path
from time import perf_counter
import json
import sympy as S
start=datetime.now(timezone.utc).isoformat();t0=perf_counter()
a,h,hbar,c,w,tau,r,s=S.symbols('a h hbar c w tau r s',nonzero=True)
J0=S.Matrix([[0,1],[-1,0]])
T=lambda z:S.Matrix([[2*z,1],[1,0]])
Ja=T(a)*J0
eh=S.Matrix([[0,h],[0,1]])
assert T(h)*J0==2*eh-S.eye(2)
assert Ja.trace()==0 and Ja*Ja==S.eye(2)
C=S.Matrix([[r,a*(s-r)],[0,s]])
assert S.simplify(C*Ja-Ja*C)==S.zeros(2)
assert C.det()==r*s

p,q,u,v=S.symbols('p q u v')
P=S.Matrix([[p,q],[u,v]]);det=P.det()
assert S.simplify(P*T(a)*P.T/det*J0-P*Ja*P.inv())==S.zeros(2)
Pr=S.Matrix([[w,-(h+c)*w],[tau*w,-(h-c)*tau*w]])
assert S.factor(Pr.det())==2*c*tau*w*w
SB=(Pr*T(a)*Pr.T/Pr.det()).applyfunc(S.factor)
expected=S.Matrix([[(a-h-c)/(c*tau),(a-h)/c],[(a-h)/c,(a-h+c)*tau/c]])
assert S.simplify(SB-expected)==S.zeros(2)
assert S.simplify(SB.subs(a,h)-S.diag(-1/tau,tau))==S.zeros(2)
JB=S.Matrix([[0,-1/tau],[-tau,0]])
assert S.simplify(Pr*(2*eh-S.eye(2))*Pr.inv()-JB)==S.zeros(2)
assert S.simplify((Pr*T(a)*Pr.T)[0,1]-2*(a-h)*tau*w*w)==0
assert S.simplify(SB[1,1].subs(a,h)/SB[0,0].subs(a,h)+tau*tau)==0

M=S.Matrix([[-h/c,1/c],[c-h*hbar/c,hbar/c]])
uu,vv=S.symbols('uu vv')
assert S.simplify(M*S.Matrix([uu,h*uu+c*vv])-S.Matrix([vv,hbar*vv+c*uu]))==S.zeros(2,1)
assert S.simplify(M.det()+1)==0
Mbar=M.xreplace({h:hbar,hbar:h})
assert S.simplify(Mbar*M-S.eye(2))==S.zeros(2)
Bh=S.Matrix([[1,0],[-h,1]]);Bhb=S.Matrix([[1,0],[-hbar,1]])
assert S.simplify(Bhb*M*Bh.inv()-S.Matrix([[0,1/c],[c,0]]))==S.zeros(2)
assert M[0,1]==1/c

elapsed=perf_counter()-t0
lines=[
 'PASS: symmetric-square determinant-twist map S -> S J0 is comparison-equivariant',
 'PASS: theta_h maps exactly to 2 e_h - identity',
 'PASS: normalized Betti tensor coordinates are (-1/tau,0,tau)',
 'PASS: mixed period theta_a equals 2(a-h) tau w^2',
 'PASS: projective Betti coordinate ratio is -tau^2',
 'PASS: full de Rham stabilizer matrix [[r,a(s-r)],[0,s]] commutes with J_a',
 'PASS: conjugate universal-extension period map has determinant -1 and c/c^-1 blocks',
 'SCOPE: exact maps and arithmetic applicability only; no H1 gate reduction',
 f'ACTUAL_WALL_SECONDS {elapsed:.9f}'
]
here=Path(__file__).resolve().parent
(here/'check_symmetric_hodge_tensor.out').write_text('\n'.join(lines)+'\n')
(here/'check_symmetric_hodge_tensor.json').write_text(json.dumps(dict(
 start_utc=start,wall_seconds=elapsed,exit_code=0,
 inputs='generic a,h,hbar,c,w,tau; c,w,tau nonzero; formal Legendre determinant2c tau w²',
 assertions=17),indent=2)+'\n')
print('\n'.join(lines))
