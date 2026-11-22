#!/usr/bin/env python3
"""Exact finite algebra underlying A5.011's TOP counterexample.

No numerical arithmetic is used.  The topology is proved in the TeX;
this certificate verifies the explicit projective module and Bass matrix.
"""
from pathlib import Path
import json
from datetime import datetime, timezone
from time import perf_counter
from sympy import Matrix, symbols, Poly, expand, cyclotomic_poly
from sympy.matrices.normalforms import hermite_normal_form

started_utc=datetime.now(timezone.utc).isoformat()
started_clock=perf_counter()
P = 23
Z = (0,) * P
ONE = (1,) + (0,) * (P - 1)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def scale(a,c): return tuple(c*x for x in a)
def mul(a,b):
    c=[0]*P
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[(i+j)%P]+=x*y
    return tuple(c)
def bar(a): return tuple(a[(-i)%P] for i in range(P))
def mm(a,b):
    return [[add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)] for i in range(2)]
def madd(a,b): return [[add(a[i][j],b[i][j]) for j in range(2)] for i in range(2)]
def msub(a,b): return [[sub(a[i][j],b[i][j]) for j in range(2)] for i in range(2)]
I2=[[ONE,Z],[Z,ONE]]
ZERO2=[[Z,Z],[Z,Z]]
QR=sorted({(i*i)%P for i in range(1,P)})
r=tuple(int(i==0 or i in QR) for i in range(P))
N=(1,)*P
assert len(QR)==11
assert add(sub(mul(r,r),r),scale(ONE,6)) == scale(N,6)
assert bar(r)==sub(add(N,ONE),r)
E=[[sub(ONE,r),scale(sub(ONE,N),3)],[scale(ONE,2),r]]
assert mm(E,E)==E
assert add(E[0][0],E[1][1])==ONE
assert sub(mul(E[0][0],E[1][1]),mul(E[0][1],E[1][0]))==Z
Ed=[[bar(E[j][i]) for j in range(2)] for i in range(2)]
assert mm(Ed,Ed)==Ed
# Laurent coefficient dictionaries for A(z)=1-E+zE and its inverse.
A={0:msub(I2,E),1:E}
Ai={0:msub(I2,E),-1:E}
def laurent_product(a,b):
    out={}
    for i,x in a.items():
        for j,y in b.items():
            out[i+j]=madd(out.get(i+j,ZERO2),mm(x,y))
    return {i:x for i,x in out.items() if x!=ZERO2}
assert laurent_product(A,Ai)=={0:I2}
assert laurent_product(Ai,A)=={0:I2}
# Independent polynomial remainder check of the group-ring identities.
g,z=symbols('g z')
rp=1+sum(g**a for a in QR)
Np=sum(g**a for a in range(P))
mod=g**P-1
Ep=Matrix([[1-rp,3*(1-Np)],[2,rp]])
assert all(Poly(e,g).rem(Poly(mod,g)).is_zero for e in Ep*Ep-Ep)
Ap=Matrix.eye(2)-Ep+z*Ep
Aip=Matrix.eye(2)-Ep+Ep/z
assert all(Poly(expand(z*e),g,z).rem(Poly(mod,g,z)).is_zero for e in Ap*Aip-Matrix.eye(2))
phi=Poly(cyclotomic_poly(P,g),g)
shift=Poly(phi.as_expr().subs(g,g+1),g)
assert shift.LC()==1
assert all(c%P==0 for c in shift.all_coeffs()[1:])
assert shift.TC()%P**2 != 0
assert Poly(rp**2-rp+6,g).rem(phi).is_zero
# Quadratic arithmetic: omega^2=omega-6, p=(2,omega), alpha=2-omega.
def qmul(a,b):
    x,y=a;u,v=b
    return (x*u-6*y*v,x*v+y*u+y*v)
def qnorm(a):
    x,y=a
    return x*x+x*y+6*y*y
p_basis=[(2,0),(0,1)]
p3gens=[qmul(qmul(a,b),c) for a in p_basis for b in p_basis for c in p_basis]
p3hnf=hermite_normal_form(Matrix(2,len(p3gens),lambda i,j:p3gens[j][i]))
alpha=(2,-1)
alphahnf=hermite_normal_form(Matrix.hstack(Matrix(alpha),Matrix(qmul(alpha,(0,1)))))
assert p3hnf==alphahnf and abs(int(p3hnf.det()))==8
assert qnorm(alpha)==8
# For norm=2: 4*N=(2a+b)^2+23b^2 forces b=0, then a^2=2.
assert 23>4*2
assert all(a*a!=2 for a in range(-2,3))
assert 11%3==2
# p * conjugate(p)=(2): conjugate omega=1-omega.
pbar_basis=[(2,0),(1,-1)]
prod=[qmul(a,b) for a in p_basis for b in pbar_basis]
prodhnf=hermite_normal_form(Matrix(2,len(prod),lambda i,j:prod[j][i]))
assert prodhnf==2*Matrix.eye(2)
report={
 'prime':P,'quadratic_residues':QR,'r_coefficients':r,
 'gauss_identity':'r^2-r+6=6*(1+g+...+g^22)',
 'idempotent':E,'dual_idempotent':Ed,
 'bass_matrix_coefficients':A,'bass_inverse_coefficients':Ai,
 'quadratic_p3_hnf':p3hnf.tolist(),'alpha_ideal_hnf':alphahnf.tolist(),
 'p_times_conjugate_hnf':prodhnf.tolist(),
 'quadratic_norm_form':'a^2+a*b+6*b^2',
 'nonprincipal_reason':'4*norm=(2*a+b)^2+23*b^2; norm 2 forces b=0 and a^2=2',
 'ideal_class_order':3,'extension_degree':11,
 'extension_nonzero_reason':'A principal extended ideal would make p^11 principal; 11 is coprime to 3',
 'dual_class_image':'[conjugate(J)^(-1)]=[J]',
 'end_obstruction_image':'plus or minus 2[J], nonzero because [J] has order 3',
 'independent_verification':'tuple convolution and SymPy polynomial remainders both pass',
}
base=Path(__file__).resolve().parents[1]/'logs'
report['started_utc']=started_utc
report['elapsed_seconds']=perf_counter()-started_clock
(base/'A5_top_normal_cancellation.json').write_text(json.dumps(report,indent=2,default=int))
lines=[
 'Started UTC: '+started_utc,
 'Elapsed seconds: '+format(report['elapsed_seconds'],'.6f'),
 'Cyclic group order: 23.',
 'Quadratic residues: '+str(QR),
 'Gauss relation r^2-r+6=6*N: PASS.',
 'E is an integral 2-by-2 idempotent of rank one: PASS.',
 'Conjugate transpose E* is idempotent: PASS.',
 'Bass matrix (1-E)+z*E has inverse (1-E)+z^(-1)*E: PASS.',
 'Independent polynomial-remainder verification: PASS.',
 'Phi_23(g+1) is Eisenstein at 23: PASS.',
 'p^3=(2-omega), both ideal lattices have index 8: PASS.',
 'p*conjugate(p)=(2): PASS.',
 'Norm-2 impossibility certificate: 23 > 8; b=0; a^2 != 2.',
 'Nonzero order-3 ideal class persists under extension of degree 11.',
 'Image of x+x* is 2[J] != 0.',
 'PASS: explicit projective module and Bass torsion data verified exactly.',
 'Topological realization, end obstruction, and axis extension are proved in A5.011.',
]
output='\n'.join(lines)+'\n'
(base/'A5_top_normal_cancellation.txt').write_text(output)
print(output,end='')
