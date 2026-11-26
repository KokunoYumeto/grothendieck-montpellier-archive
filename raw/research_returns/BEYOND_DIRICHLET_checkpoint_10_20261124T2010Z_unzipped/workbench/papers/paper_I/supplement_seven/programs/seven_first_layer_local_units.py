#!/usr/bin/env python3
"""Exact first-layer one-prime local-unit index; finite ring modulo pi^16.

Run from any directory with Python 3 and Sympy. This is a research certificate;
the abstract local basis and global seven-saturation are separate proof inputs.
No floating point, p-adic library, or BNF output is used.
"""
from pathlib import Path
import json, hashlib, time
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

W=Path(__file__).resolve().parents[1]
DATA=W/'certificates/seven_compact_units.json'
data=json.loads(DATA.read_text())
N=16
# q(pi-1)=pi^7-7pi^6+49pi^4-98pi^2-49pi+7.
q=[7,-49,-98,0,49,0,-7,1]
mulpi=Matrix(7,7,lambda i,j: (1 if j<6 and i==j+1 else -q[i] if j==6 else 0))
H=hermite_normal_form(mulpi**N)
H=[[int(H[i,j]) for j in range(7)] for i in range(7)]
assert all(H[i][i]>0 for i in range(7))
assert all(H[i][j]==0 for i in range(7) for j in range(i))
assert Matrix(H).det()==7**N
assert all(H[i][i] <=343 for i in range(7))

def canon(v):
    v=list(v)
    for a in range(3):
        for j in range(6,-1,-1):
            c=v[3*j+a]//H[j][j]
            if c:
                for i in range(j+1):v[3*i+a]-=c*H[i][j]
    return tuple(v)

ZERO=(0,)*21
ONE=canon([1]+[0]*20)
ALPHA=canon([0,1]+[0]*19)
PI=canon([0,0,0,1]+[0]*17)

def add(a,b):return canon([x+y for x,y in zip(a,b)])
def neg(a):return canon([-x for x in a])
def scale(a,c):return canon([x*c for x in a])
def sub(a,b):return add(a,neg(b))
def const(c):return scale(ONE,c)
def mul(a,b):
    v=[[0]*3 for _ in range(13)]
    for j in range(7):
        for i in range(3):
            aa=a[3*j+i]
            if not aa:continue
            for l in range(7):
                for k in range(3):
                    bb=b[3*l+k]
                    if bb:v[j+l][(i+k)%3]+=aa*bb*(269 if i+k>=3 else 1)
    for j in range(12,6,-1):
        for i in range(3):
            c=v[j][i]
            if c:
                for l in range(7):v[j-7+l][i]-=c*q[l]
    return canon([v[j][i] for j in range(7) for i in range(3)])
def power(a,n):
    assert n>=0
    r=ONE
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r
def poly(coeff,x):
    r=ZERO
    for c in reversed(coeff):r=add(mul(r,x),const(c))
    return r
def evaluate_tower(coeff,alpha,beta,den=1):
    aa=[ONE,alpha,power(alpha,2)]
    bb=[power(beta,j) for j in range(7)]
    r=ZERO
    for j in range(7):
        for i in range(3):r=add(r,scale(mul(aa[i],bb[j]),int(coeff[3*j+i])))
    return scale(r,pow(int(den),-1,343))

BETA=sub(PI,ONE)
assert power(PI,N)==ZERO
assert power(PI,N-1)!=ZERO
assert power(ALPHA,3)==const(269)
assert poly(q,PI)==ZERO
assert poly(list(reversed(data['period_polynomial_descending'])),BETA)==ZERO
zeta=next(z for z in range(343) if z%7==2 and (z*z+z+1)%343==0)
assert pow(zeta,3,343)==1 and zeta%7!=1

def delta(v,j=1):
    return canon([c*pow(zeta,j*(k%3),343) for k,c in enumerate(v)])
def project(v,a):
    inv3=pow(3,-1,343)
    r=ONE
    for j in range(3):
        coeff=inv3*pow(zeta,(-a*j)%3,343)%343
        r=mul(r,power(delta(v,j),coeff))
    return r

def lead(v,grade):
    """Coefficient of pi^grade for v divisible by pi^grade, in F_343."""
    vv=[int(t) for t in v]
    for _ in range(grade):
        new=[0]*21
        for a in range(3):
            assert vv[a]%7==0,('nondivisible',grade,_,a,vv[:3])
            c=vv[a]//7
            for j in range(6):new[3*j+a]=vv[3*(j+1)+a]-c*q[j+1]
            new[18+a]=-c
        vv=new
    return tuple(x%7 for x in vv[:3])

# Global units: epsilon followed by eta,tau(eta),...,tau^5(eta).
epsilon=poly(data['cubic_unit_numerator_ascending'],ALPHA)
eta_coeff=data['orbit_seed_numerators_alpha_first']
beta_images=[]
b=BETA
for j in range(7):
    beta_images.append(b)
    b=scale(poly(data['period_automorphism_numerator_ascending'],b),
            pow(data['period_automorphism_denominator'],-1,343))
assert b==BETA
etas=[evaluate_tower(eta_coeff,ALPHA,b,data['orbit_seed_denominator']) for b in beta_images]
norm=ONE
for e in etas:norm=mul(norm,e)
assert norm==ONE
global_units=[epsilon]+etas[:6]
principal=[power(u,342) for u in global_units]
assert all(lead(sub(u,ONE),0)==(0,0,0) for u in principal)

answers=[]
for a in (1,2):
    began=time.time()
    alpha_a=power(ALPHA,a)
    grades=[1,2,3,4,5,6,8]
    orders=[343]+[49]*6
    basis=[project(add(ONE,mul(alpha_a,power(PI,j))),a) for j in grades]
    assert all(power(g,o)==ONE for g,o in zip(basis,orders))
    assert all(power(g,o//7)!=ONE for g,o in zip(basis,orders))
    assert all(delta(g)==power(g,pow(zeta,a,343)) for g in basis)
    pivots={}
    pivot_data=[]
    for i,g in enumerate(basis):
        for k in range(3 if i==0 else 2):
            v=power(g,7**k)
            grade=next(j for j in range(1,N) if lead(sub(v,ONE),j)!=(0,0,0))
            lc=lead(sub(v,ONE),grade)
            assert lc[a]!=0 and all(lc[i]==0 for i in range(3) if i!=a)
            assert grade not in pivots
            pivots[grade]=(i,k,lc[a],power(v,orders[i]//(7**k)-1))
            pivot_data.append([i,k,grade,list(lc)])
    assert sorted(pivots)==list(range(1,N))

    def coordinates(u):
        original=u
        exps=[0]*7
        for grade in range(1,N):
            lc=lead(sub(u,ONE),grade)
            assert all(lc[i]==0 for i in range(3) if i!=a),('noncharacter',a,grade,lc)
            i,k,pivot,inverse=pivots[grade]
            digit=lc[a]*pow(pivot,-1,7)%7
            exps[i]+=digit*7**k
            u=mul(u,power(inverse,digit))
        assert u==ONE
        rec=ONE
        for b,e in zip(basis,exps):rec=mul(rec,power(b,e))
        assert rec==original
        return exps

    # Recheck every local basis vector and its seventh power by the coordinate algorithm.
    for i,b in enumerate(basis):
        e=[0]*7;e[i]=1;assert coordinates(b)==e
        e[i]=7;assert coordinates(power(b,7))==e
    columns=[coordinates(project(u,a)) for u in principal]
    matrix=[[columns[j][i]%49 for j in range(7)] for i in range(7)]
    determinant=int(Matrix(matrix).det())
    mod49=determinant%49
    result={'character_exponent':a,'local_basis_grades':grades,'local_orders':orders,
            'pivot_data':pivot_data,'global_coordinate_columns':columns,
            'matrix_mod49':matrix,'determinant_mod49':mod49,
            'valuation_exactly_one':mod49%7==0 and mod49!=0,
            'all_units_reconstructed_exactly':True,'elapsed_seconds':time.time()-began}
    answers.append(result)
    print(json.dumps(result),flush=True)

out={'description':'Exact local units at the first cyclotomic seven layer',
     'modulus_uniformizer_power':N,'uniformizer_polynomial_ascending':q,
     'basis_ideal_HNF':H,'residue_field_polynomial':'A^3-269 mod7',
     'zeta3_mod343':zeta,'finite_ring_order':7**(3*N),
     'input_sha256':hashlib.sha256(DATA.read_bytes()).hexdigest(),
     'eta_relative_norm_mod_pi16':1,'results':answers,
     'both_local_indices_exactly_seven':all(r['valuation_exactly_one'] for r in answers)}
target=W/'certificates/seven_first_layer_local_unit_index.json'
target.write_text(json.dumps(out,indent=2)+'\n')
print('BOTH_LOCAL_INDICES_EXACTLY_SEVEN='+str(int(out['both_local_indices_exactly_seven'])))
