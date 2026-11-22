"""Exact finite arithmetic for NN-G034.

The paper proves completeness, arbitrary-degree exclusions and divisibility.
This script independently audits the numerical bounds and residual coefficients;
it does not search through all possible exponent locations.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as sp

D,q,z0,z1,z2=sp.symbols('D q z0 z1 z2')
C=D-1;H=2*D*(D-2);G1=D*H
def laurent(p):
    return sp.expand(p.subs(D,q+2+q**-1))
def coeff(p,k):
    return sp.expand(laurent(p)).coeff(q,k)
def mass_bound(w,d,a):
    return (2856+440*w+Fraction(75,4)*w*w
            +(26-Fraction(5,4)*w)*d+(14-Fraction(5,16)*w)*a)

cap=9912
assert 3584+440*16>cap
assert 2856+440*12+Fraction(75,4)*12**2==10836>cap
v1_rows=[]
for V in [5*D,7*D-8,2*D**2-3*D]:
    A=D**2*H-D*C*V
    v1_rows.append({'V1_D':str(V),'A1_central':int(coeff(A,0))})
assert [r['A1_central'] for r in v1_rows]==[-10,-6,2]

w8_scores={str(a):int((mass_bound(8,8,a)-4424)/2) for a in [64,192]}
assert w8_scores=={'64':2008,'192':2744}
W8=2*D**2-7*D+4
w8_z=[]
for z in [3,5]:
    for a in range(0,z-2,2):
        Z=z-2*a+a*(D-2)
        V=W8*Z;A=D**2*W8*C-G1*Z
        row={'Z_mass':z,'q1_coefficient':a,
             'V2_central':int(coeff(V,0)),
             'A2_central':int(coeff(A,0))}
        w8_z.append(row)
assert [(r['Z_mass'],r['q1_coefficient'],r['V2_central'],r['A2_central'])
        for r in w8_z]==[(3,0,6,22),(5,0,10,-10),(5,2,6,-2)]

w10=[]
for d in range(4,30,2):
    u=Fraction(5,8)*(30-d)
    if u.denominator!=1 or u<4 or u%2:continue
    for a in range(16,481,2):
        v=Fraction(5,32)*(480-a)
        if v.denominator!=1 or v<16 or v%2:continue
        T=mass_bound(10,d,a)
        if T<=cap:w10.append([d,int(u),a,int(v),int(T)])
assert w10==[[14,10,32,70,9668]]
assert mass_bound(10,14,96)==10364>cap

T3=D**3-6*D**2+9*D-2
W3=D+2+2*T3
Z=z0+z1*(D-2)+z2*(D**2-4*D+2)
assert coeff(D**2*W3*C,2)==54
assert sp.expand(coeff(G1*Z,2))==8*z0+16*z1+16*z2
assert sp.expand(coeff(D**2*W3*C-G1*Z,2).subs(z0,7-2*z1-2*z2))==-2

W2=2*D**2-7*D+6;B=2*D-3
A=D**2*(W2*C-2*Z)
expressions={k:sp.expand(coeff(A,k).subs(z0,14-2*z1-2*z2)) for k in [1,2,4]}
assert expressions=={1:-25+2*z1+8*z2,2:32-4*z1-8*z2,4:11-2*z2}
assert sp.expand(coeff(B*Z,0))==z0+4*z1
residual=[]
for zz2 in [0,2,4]:
    for zz1 in range(14-4*zz2,8-2*zz2):
        if zz1%2!=1:continue
        zz0=14-2*zz1-2*zz2
        residual.append([zz0,zz1,zz2,zz0+4*zz1])
assert residual==[[8,-1,4,4]]

out={'mass_cap':cap,'first_cell_equality_candidates':v1_rows,
     'w8_scalar_scores':w8_scores,'w8_quotient_candidates':w8_z,
     'w10_competitive_scalar_rows':w10,
     'w10_j3_forced_A2_q2':-2,
     'w10_j2_unique_residual_Z_and_V2_central':residual,
     'scope':'Exact finite arithmetic only. Uniform support, parity and polynomial-divisibility exclusions are proved in NN-G034.'}
Path('work/gct/fixed_first_cell_optimum_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
