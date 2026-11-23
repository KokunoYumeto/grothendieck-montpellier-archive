#!/usr/bin/env python3
"""Deterministic AM-DO-040 certificate. No probable-prime test is used."""
from pathlib import Path
from math import gcd, isqrt, prod
from datetime import datetime, timezone
import hashlib
import json

A_WEIGHT=2**960
CONFIGS=[
 dict(host='J14',conductor=812,g0=4615409,g1=5276377,a=42,f=42,B=392,m=263,
      factor_F={2:396,7:1,29:1,263:1,4615409:2,5276377:2},
      witnesses={2:5,7:2,29:2,263:2,4615409:2,5276377:2}),
 dict(host='J56',conductor=52780,g0=22285932761,g1=64072175441,a=168,f=168,B=334,m=54,
      factor_F={2:339,3:3,5:1,7:1,13:1,29:1,22285932761:2,64072175441:2},
      witnesses={2:11,3:3,5:2,7:2,13:2,29:2,22285932761:2,64072175441:2})]


def prime_trial(n):
    assert n>=2
    if n==2:return dict(prime=n,method='trial_division',bound=1,odd_divisors_tested=0)
    assert n%2
    bound=isqrt(n)
    tested=0
    for p in range(3,bound+1,2):
        assert n%p, (n,p)
        tested+=1
    return dict(prime=n,method='trial_division',bound=bound,odd_divisors_tested=tested)


def valuation(n,p):
    assert n
    e=0
    while n%p==0:n//=p;e+=1
    return e


def run(cfg):
    c,g0,g1,B,m=(cfg[k] for k in ['conductor','g0','g1','B','m'])
    base=c*(g0*g1)**2
    D=base*2**B*m
    N=11*D*D+4*D+1
    F=4*D
    assert D%4==0 and D>=2**490
    assert N>16*A_WEIGHT and N%2
    assert prod(q**e for q,e in cfg['factor_F'].items())==F
    assert set(cfg['factor_F'])==set(cfg['witnesses'])
    assert (N-1)%F==0 and (N-1)//F==1+11*D//4
    assert F*F>N and F*F-N==(5*D+1)*(D-1)
    prime_proofs=[prime_trial(q) for q in cfg['factor_F']]
    pock=[]
    for q,e in cfg['factor_F'].items():
        witness=cfg['witnesses'][q]
        fermat=pow(witness,N-1,N)
        quotient_residue=pow(witness,(N-1)//q,N)
        common=gcd(quotient_residue-1,N)
        assert fermat==1 and common==1,(cfg['host'],q)
        pock.append(dict(prime=q,exponent_in_F=e,witness=witness,
                         fermat_residue=fermat,
                         quotient_power_residue=str(quotient_residue),gcd=common))
    # The general proof in DO040 now proves N prime from these facts.
    pi_real=1+2*D; pi_imag=D
    assert pi_real*pi_real+7*pi_imag*pi_imag==N
    assert (pi_real-1)%base==0 and pi_imag%base==0
    assert N%c==1 and gcd(N,2*pi_real)==1
    assert gcd(N,11*g0*g1*c)==1
    assert N%28==1
    order_checks=[]
    for j in range(1,cfg['a']+1):
        residue=pow(2,28*j,N)
        assert residue!=1
        order_checks.append(dict(j=j,exponent=28*j,residue=str(residue)))
    order_mod11=next(j for j in range(1,11) if pow(N,j,11)==1)
    assert valuation(N-1,11)==0
    if cfg['host']=='J14':
        assert N%11==9 and order_mod11==5 and cfg['a']%5
        vdt=0
    else:
        assert N%11==10 and order_mod11==2
        assert valuation(N+1,11)==2
        vdt=valuation(N+1,11)+valuation(cfg['a']//2,11)
        assert vdt==2
    # Independent direct modular check of the exact parabolic-index valuation.
    va=valuation(pow(N,cfg['a'])-1,11)-valuation(N-1,11)
    assert va==vdt
    return dict(host=cfg['host'],conductor=c,g0=g0,g1=g1,a=cfg['a'],f=cfg['f'],
                B=B,m=m,D=str(D),D_bits=D.bit_length(),T=str(N),T_bits=N.bit_length(),
                T_decimal_digits=len(str(N)),piT_real=str(pi_real),piT_sqrt_minus7=str(D),
                F=str(F),factor_F={str(q):e for q,e in cfg['factor_F'].items()},
                complementary_factor=str((N-1)//F),F_squared_minus_T=str(F*F-N),
                prime_factor_certificates=prime_proofs,pocklington_certificates=pock,
                T_over_4A_floor=N//(4*A_WEIGHT),T_greater_than_16A=True,
                norm_identity=True,piT_congruence_modulus=str(base),
                conjugate_coprimality_gcd=gcd(N,2*pi_real),
                all_T_places_degree_one=True,
                quotient_order_2_greater_than_a_certificates=order_checks,
                T_mod11=N%11,T_order_mod11=order_mod11,
                v11_T_minus1=0,v11_projective_index=vdt,
                v11_product_projective_index=cfg['f']*vdt)


if __name__=='__main__':
    rows=[run(c) for c in CONFIGS]
    out=Path(__file__).with_suffix('.json')
    report=dict(finding='AM-DO-040',status='DETERMINISTIC_CERTIFICATE_PASS',
                checked_at=datetime.now(timezone.utc).isoformat(),
                A_weight=str(A_WEIGHT),rows=rows,
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                scope='Exact trial division of every factor prime; specified Pocklington witnesses; norm/congruence/coprimality; projective residue-vector order; local11 mass valuations. No probable-prime result is used by this replay.')
    out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(status=report['status'],checked_at=report['checked_at'],
                         hosts=[dict(host=r['host'],bits=r['T_bits'],digits=r['T_decimal_digits'],
                                     quotient_order_tests=len(r['quotient_order_2_greater_than_a_certificates']),
                                     v11_T_projective_mass=-r['v11_product_projective_index']) for r in rows],
                         output=str(out))))
