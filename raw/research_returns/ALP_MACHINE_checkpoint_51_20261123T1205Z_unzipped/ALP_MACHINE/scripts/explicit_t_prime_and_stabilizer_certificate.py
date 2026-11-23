#!/usr/bin/env python3
"""Exact certificates for AM-R-017. No probable-prime decision is used.

Candidate discovery was separate. This replay uses trial division on the
small factors, Pocklington modular equalities/gcds, and integer arithmetic.
"""
from pathlib import Path
from math import gcd,isqrt,prod
import json

ROOT=Path(__file__).resolve().parents[1]

def trial_prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def valuation(n,p):
    k=0
    while n%p==0:
        n//=p;k+=1
    return k

cases=[
 dict(name='J14',f=42,a=42,b=1802,c=3562,cond=812,g0=4615409,g1=5276377,n=3,
      factors={2:3,7:1,29:1,293:1,4615409:2,5276377:2}),
 dict(name='J56',f=168,a=168,b=1802,c=3436,cond=52780,g0=22285932761,g1=64072175441,n=16,
      factors={2:4,5:1,7:1,11:1,13:1,29:1,22285932761:2,64072175441:2})]

out=[]
for c in cases:
    mod=c['cond']*(c['g0']*c['g1'])**2
    A=1+c['n']*mod
    q=A*A+7*mod*mod
    factors=c['factors'];known=prod(p**e for p,e in factors.items())
    assert all(trial_prime(p) for p in factors)
    assert (q-1)%known==0 and known*known>q
    witnesses={p:3 if p==2 else 2 for p in factors}
    checks={}
    for p,z in witnesses.items():
        residue=pow(z,(q-1)//p,q)
        assert pow(z,q-1,q)==1 and gcd(residue-1,q)==1
        checks[p]={'base':z,'full_power_residue':1,'reduced_power_residue':residue,'gcd':1}
    assert q%c['cond']==1 and gcd(q,2*A)==1
    assert gcd(q,2*mod)==1 and q not in (c['g0'],c['g1'],11,29)
    assert (q-1)//28>c['a']
    # The class of 2 in F_q^*/mu_28 has order >a. A primitive root
    # or the unknown complete factorization of q-1 is unnecessary.
    powers=[pow(2,28*j,q) for j in range(1,c['a']+1)]
    assert all(x!=1 for x in powers)
    C=(c['a']+1+2*(c['b']-c['a']-1))**3+c['b']+10
    # Same C as the K031/K032 construction, via r+mt and N_(m-1).
    assert C=={'J14':45156049293,'J56':40530339687}[c['name']]
    u0_twice=2*(2*c['a']+1)*C+1
    size_a=u0_twice+2*c['f']*c['c']+1
    assert 2*c['f']*c['c']+1<4*size_a and 4*size_a<q
    order11=next(j for j in range(1,11) if pow(q,j,11)==1)
    va=valuation(q**c['a']-1,11)
    vb=valuation(q-1,11)
    out.append({**{k:v for k,v in c.items() if k!='factors'},'L_T':mod,
                'pi_real':A,'pi_imag':mod,'T':q,'T_digits':len(str(q)),
                'factor_F':known,'F_factorization':factors,'unfactored_cofactor':(q-1)//known,
                'Pocklington':checks,'F_squared_greater_T':known*known>q,
                'coprime_pi_conjugate_gcd':gcd(q,2*A),
                'quotient_order_2_greater_a':True,'quotient_power_nonidentity_checks':len(powers),
                'C':C,'source_size_parameter':size_a,'four_size_parameter':4*size_a,
                'T_mod11':q%11,'T_order_mod11':order11,
                'v11_T_minus1':vb,'v11_T_power_a_minus1':va,
                'v11_projective_line_index':va-vb})

dest=ROOT/'checks/explicit_t_prime_and_stabilizer_certificate.json'
dest.write_text(json.dumps({'statement_id':'AM-R-017','scope':'exact arithmetic certificate; not proof of the global theta assertion','cases':out},indent=2)+'\n')
print(json.dumps({'certificate':str(dest),'cases':[{k:c[k] for k in ['name','T','C','source_size_parameter','v11_projective_line_index']} for c in out]},indent=2))
