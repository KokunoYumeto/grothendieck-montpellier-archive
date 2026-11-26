#!/usr/bin/env python3
"""Independent exact Bolza Hessian and numerical theta comparison.

Numerics are diagnostic, not the mathematical identification proof.
"""
from pathlib import Path
import json
from itertools import product
import sympy as sp
import mpmath as mp

BASE = Path(__file__).resolve().parent
x, t, a = sp.symbols('x t a')
phi = sum(a**i for i in range(7))

def red(v):
    return sp.Poly(sp.rem(sp.Poly(sp.expand(v), a), sp.Poly(phi, a)), a).as_expr()

Qx = sp.prod(x-a**j for j in (1,3,5))
Rx = sp.prod(x-a**j for j in (0,2,4,6))
Fx = x**3*t**3*(x+t)-2
numerator = sp.Poly(sp.expand(Fx-Qx*Rx.subs(x,t)-Qx.subs(x,t)*Rx), x,t)
numerator = sum(red(c)*x**m[0]*t**m[1] for m,c in numerator.terms())
quotient, remainder = sp.div(numerator, 4*(x-t)**2, x, t)
assert sp.expand(remainder) == 0
W = sp.Matrix(3,3,lambda i,j: red(sp.expand(quotient).coeff(x,i).coeff(t,j)))
assert W == W.T
s1=red(sum(a**j for j in (1,3,5)))
s2=red(sum(a**j*a**k for j,k in ((1,3),(1,5),(3,5))))
s3=red(a**9)
assert sp.simplify(W[2,2]-s1/4) == 0
assert sp.simplify(W[1,2]+s2/4) == 0
assert sp.simplify(W[0,2]-s3/4) == 0

mp.mp.dps=65
zeta=mp.exp(2*mp.pi*mp.j/7)
A=mp.matrix([[zeta**(2*(i+1)*j) for j in range(3)] for i in range(3)])
B=mp.matrix([[sum(zeta**((i+1)*(2*k+1)) for k in range(j,3)) for j in range(3)] for i in range(3)])
c=[-2*mp.j/7*mp.beta(mp.mpf(i)/7,mp.mpf('0.5'))*(zeta**i-1) for i in (1,2,3)]
P=mp.diag(c)*A
tau=A**-1*B
Y=mp.matrix([[mp.im(tau[i,j]) for j in range(3)] for i in range(3)])
theta=mp.mpc(0)
H=mp.zeros(3)
directions=[P**-1*mp.matrix([int(i==j) for i in range(3)]) for j in range(3)]
moments=[[mp.mpc(0) for _ in range(9)] for _ in range(3)]
for n in product(range(-11,12), repeat=3):
    q=sum(n[i]*tau[i,j]*n[j] for i in range(3) for j in range(3))
    term=mp.exp(mp.pi*mp.j*q)
    theta+=term
    for d in range(3):
        v=2*mp.pi*mp.j*sum(n[i]*directions[d][i] for i in range(3))
        for m in (0,2,4,6,8):moments[d][m]+=term*v**m
    for i in range(3):
        for j in range(3):
            H[i,j]-=4*mp.pi**2*n[i]*n[j]*term
Fh=P.T**-1*(mp.pi*Y**-1+H/theta)*P**-1
Wn=mp.matrix([[sum(mp.mpf(str(coef))*zeta**power[0] for power,coef in sp.Poly(W[i,j],a).terms()) for j in range(3)] for i in range(3)])
error=max(abs(Fh[i,j]+Wn[i,j]) for i in range(3) for j in range(3))
assert error<mp.mpf('1e-37'), error
exact_jets=json.loads((BASE/'jacobian_theta_direction_jets.json').read_text())
jet_errors={}
for d in range(3):
    v=directions[d]
    q=(mp.pi/2*(v.T*Y**-1*v))[0]
    for n in (2,4,6,8):
        numerical=mp.factorial(n)*sum(q**k/mp.factorial(k)*moments[d][n-2*k]/mp.factorial(n-2*k) for k in range(n//2+1))/theta
        coefficients=exact_jets['directions'][str(d+1)]['theta_derivatives'][str(n)]
        algebraic=sum(mp.mpf(int(sp.Rational(c).p))/int(sp.Rational(c).q)*zeta**i for i,c in enumerate(coefficients))
        err=abs(numerical-algebraic)
        assert err<mp.mpf('1e-36'),(d,n,err)
        jet_errors[str((d+1,n))]=mp.nstr(err,15)
result={
    'description':'Exact Bolza Hessian for D=P1+P3+P5-infinity; numerical independent comparison with R004 F1.',
    'W_exact':[[str(W[i,j]) for j in range(3)] for i in range(3)],
    'hessian_F1_exact':'negative of W_exact, with a=zeta_7',
    'theta_0_numeric':mp.nstr(theta,55),
    'max_numeric_hessian_error':mp.nstr(error,15),
    'independent_theta_vs_algebraic_direction_jet_errors':jet_errors,
    'cube_bound':11,
    'numeric_precision_decimal_digits':65,
    'numeric_claim_scope':'Diagnostic comparison only; exact equality is proved by invariant bidifferential and Kleinian identities.',
}
delta=[mp.mpf('0.5')]*3
epsilon=[mp.mpf('0.5'),mp.mpf('0'),mp.mpf('0.5')]
thetaK=mp.mpc(0)
H13=mp.mpc(0)
H22=mp.mpc(0)
kmom=[[mp.mpc(0) for _ in range(7)] for _ in range(3)]
for n in product(range(-11,12),repeat=3):
    w=[n[i]+delta[i] for i in range(3)]
    phase=sum(w[i]*tau[i,j]*w[j] for i in range(3) for j in range(3))+2*sum(w[i]*epsilon[i] for i in range(3))
    term=mp.exp(mp.pi*mp.j*phase)
    thetaK+=term
    a=[2*mp.pi*mp.j*sum(w[i]*directions[d][i] for i in range(3)) for d in range(3)]
    H13+=term*a[0]*a[2]
    H22+=term*a[1]*a[1]
    for d in range(3):
        for m in (0,2,4,6):kmom[d][m]+=term*a[d]**m
def kjet(d,n):
    v=directions[d]
    q=(mp.pi/2*(v.T*Y**-1*v))[0]
    return mp.factorial(n)*sum(q**k/mp.factorial(k)*kmom[d][n-2*k]/mp.factorial(n-2*k) for k in range(n//2+1))/H13
standard_checks={'thetaK_zero':abs(thetaK),'q_H22_equals_minus2':abs(H22/H13+2),'direction1_order4_equals2':abs(kjet(0,4)-2),'direction3_order6_equals1':abs(kjet(2,6)-1)}
assert max(standard_checks.values())<mp.mpf('1e-36'),standard_checks
result['standard_sigma_independent_numeric_checks']={k:mp.nstr(v,15) for k,v in standard_checks.items()}
(BASE/'jacobian_theta_hessian_check.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
