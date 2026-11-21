"""Finite symbolic corroboration of I39; not a replacement for its proof."""
from datetime import datetime, timezone
from pathlib import Path
import json
import sympy as sp

ell1,ell2,ell3,ell4,s,u,v,t,T=sp.symbols('L1 L2 L3 L4 s u v t T')
eye=sp.eye(3)
E21=sp.zeros(3); E21[1,0]=1
E32=sp.zeros(3); E32[2,1]=1
E31=sp.zeros(3); E31[2,0]=1
PL=sp.diag(0,1,1); PR=sp.diag(1,1,0)
middle=(eye-ell1*E21)*(eye-ell2*E32)*(eye-ell3*E21)*(eye-ell4*E32)
A=ell1+ell3; B=ell2+ell4; C=ell2*ell3
Q=ell1*ell2+ell1*ell4+ell3*ell4
assert sp.simplify(middle-(eye-A*E21-B*E32+C*E31))==sp.zeros(3)
corner=PL*middle*PR
assert corner==sp.Matrix([[0,0,0],[-A,1,0],[C,-B,0]])
assert sp.expand(corner[1:3,0:2].det()-Q)==0
JL=(eye+u*E32)*PL; JR=PR*(eye+v*E21)
interval=sp.expand(JL*middle*JR)
assert interval[1,1]==1
assert sp.expand(interval[1:3,0:2].det()-Q)==0
output=((eye+s*E32)*interval*(eye+t*E21))[2,0]
assert sp.expand(output-((s+u-B)*(t+v-A)-Q))==0

a=sp.sqrt(sp.Rational(3,2))
P1=T**4-1;P2=T**2-a;P3=-2*(T**2+a);P4=T**4-2
R1=P2/P1;R2=1/P2;R3=1/P3;R4=P3/P4
assert sp.simplify(R1*R2+R1*R4+R3*R4)==0
node_polynomial=T*(T**4-1)*(T**4-sp.Rational(3,2))*(T**4-2)*(T**2-9)*(T**2-16)
assert sp.degree(node_polynomial,T)==17
assert sp.expand(node_polynomial.subs(T,-T)+node_polynomial)==0
derivative=sp.diff(node_polynomial,T)
assert sp.expand(derivative.subs(T,-T)-derivative)==0
assert sp.gcd(node_polynomial,derivative)==1
H=sp.hessian(Q,(ell1,ell2,ell3,ell4))
aa=[1,0,1,0];bb=[0,1,0,1]
assert all(H[i,j]==aa[i]*bb[j] for i in range(4) for j in range(i+1,4))

record={'time_utc':datetime.now(timezone.utc).isoformat(),
        'all_checks_pass':True,
        'checks':['four-block affine matrix product','projected rank-two minor Q',
                  'variable-anchor minor and unit entry','irreducible-scalar displayed identity',
                  'rational pole identity','degree17 squarefree odd node polynomial and even derivative',
                  'four-group upper semiseparable Hessian'],
        'scope':'Exact finite symbolic identities only; irreducibility, residue parity, all-interval ranks and the general Hessian constraints are proved in the manuscript, not certified by this script.'}
out=Path('/workspace/scratch/64674c0aa6e9/work/isolation/I39_matrix_checks.json')
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
