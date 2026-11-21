#!/usr/bin/env python3
"""Exact endomorphism-ring identities for A40, over Z[T]/(T^2+T-1).

The coefficient ring is integral characteristic zero, as required for
Jacobians' endomorphism groups; it is deliberately not reduced modulo two.
This checks the finite algebra in the written proof, not its geometry.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

t=s.symbols('t')
relation=t*t+t-1
def red(x): return s.rem(s.expand(x),relation,t)
def mr(m): return m.applyfunc(red)
identity=s.eye(2)
tau1=s.Matrix([[1,t],[0,-1]])
tau2=s.Matrix([[-1,0],[t,1]])
sigma=mr(tau1*tau2)
assert mr(tau1*tau1)==identity
assert mr(tau2*tau2)==identity
assert sigma==s.Matrix([[-t,t],[-t,-1]])
assert mr(sigma*sigma)==s.Matrix([[0,-1],[1,t]])
assert red(sigma.det())==1
assert red(s.trace(sigma))==-1-t
cyclotomic=s.zeros(2)
for j in range(5): cyclotomic+=sigma**j
assert mr(cyclotomic)==s.zeros(2)
assert mr(sigma**5)==identity
assert mr(tau1*sigma*tau1)==mr(sigma**4)
N1=s.Matrix([[2,t]])
U1=s.Matrix([[1],[0]])
assert mr(N1*sigma*sigma*U1)==s.Matrix([[t]])
normmatrix=s.Matrix([[2,t],[t,2]])
assert red(normmatrix.det())==3+t
assert red((3+t)*(2-t))==5
assert red((t+1)*t)==1
assert red((-1-t)**2+(-1-t)-1)==0
data={
 'ring':'Z[t]/(t^2+t-1), not the characteristic-two scalar field',
 'tau1_squared_identity':True,
 'tau2_squared_identity':True,
 'sigma_matrix':[[str(x) for x in row] for row in sigma.tolist()],
 'sigma_squared_matrix':[['0','-1'],['1','t']],
 'Phi5_sigma_zero':True,
 'sigma_fifth_power_identity':True,
 'dihedral_conjugation_identity':True,
 'N1_sigma_squared_U1':'t',
 'norm_matrix_determinant':'3+t',
 'determinant_times_2_minus_t':5,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'scope':'Exact symbolic verification of the finite matrix identities only. Integrality, smoothness, genus and finite-field realization are proved in the accompanying text. No formal verification claim.',
}
Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data,indent=2))
