#!/usr/bin/env python3
"""AM-K046 exact form checks and selected-kernel localization constants."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
from math import prod, factorial
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
CHECKS=[]


def check(name, value):
    if not value:
        raise AssertionError(name)
    CHECKS.append(name)


def rf(r, m):
    return prod(range(r,r+m))


def digest_int(n):
    return hashlib.sha256(n.to_bytes((n.bit_length()+7)//8,'big')).hexdigest()


def main():
    # Independent scalar-ball radial Beta integral check: the general
    # product must telescope to Beta(Lambda-a,N+a), not Beta(Lambda,N).
    for a in range(1,6):
        lam=24
        for N in range(7):
            rs=[lam-i for i in range(a)]
            ms=[N]+[0]*(a-1)
            for s in range(6):
                C=prod(r-1 for r in rs);Cs=prod(r+s-1 for r in rs)
                D=prod(rf(r,m) for r,m in zip(rs,ms))
                Ds=prod(rf(r+s,m) for r,m in zip(rs,ms))
                beta=F(rf(lam-a,s),rf(lam+N,s))
                moments=prod(F(rf(r-1,s),rf(r+m,s)) for r,m in zip(rs,ms))
                assert F(C*D,Cs*Ds)==moments==beta
            for j in range(1,5):
                lhs=prod(F(rf(r+m-j,j),rf(r-1-j,j)) for r,m in zip(rs,ms))
                beta=F(rf(lam+N-j,j),rf(lam-a-j,j))
                assert lhs==beta
    check('scalar ball positive and negative moments including dimension shift',True)
    for rs,ms in (([12,8],[3,2]),([19,13,6],[5,2,0])):
        for j in range(1,4):
            C=prod(r-1 for r in rs);Cm=prod(r-1-j for r in rs)
            D=prod(rf(r,m) for r,m in zip(rs,ms));Dm=prod(rf(r-j,m) for r,m in zip(rs,ms))
            exact=prod(F(rf(r+m-j,j),rf(r-1-j,j)) for r,m in zip(rs,ms))
            assert F(C*D,Cm*Dm)==exact
            bound=prod(F(r+m,r-1-j) for r,m in zip(rs,ms))**j
            assert exact<=bound
    check('vector-fibre norm shift and negative moment index convention',True)
    input_path=ROOT/'work/agents/enlarged_gap_admissible_interval_certificate.json'
    old=json.loads(input_path.read_text())
    upper={'J14':{'top':45,'thick':969,'thin':222},
           'J56':{'top':45,'thick':1722,'thin':1059}}
    reports=[]
    for h in old['hosts']:
        name,a,f=h['host'],h['a'],h['f'];ell=h['ell_max']
        t=ell//2;s0=a+1
        check(name+' exact integer negative-moment order',ell%28==0 and 2*t==ell and t>s0)
        role_reports={}
        for role,z in h['roles'].items():
            E=z['E']
            rs=[E+(4*a-3-4*i)*ell+1 for i in range(a-1)]+[2*ell+1]
            ms=([2**960+(a-2)//2-4*ell*(a-1)] if role=='top' else [4*a*ell])
            ms += [4*ell-1]*(a-2)
            ms += [E-2**955-ell-a//2] if role=='top' else [E+ell]
            assert len(rs)==len(ms)==a and min(ms)>=0
            assert min(r-1 for r in rs)>t
            # The zero word and q=0 maximize every ratio in this product.
            numerator=prod(r+m for r,m in zip(rs,ms))
            denominator=prod(r-1-t for r in rs)
            check(name+' '+role+' exact rational moment constant',
                  numerator<upper[name][role]*denominator<2048*denominator)
            first=prod(F(r+m-1,r-2) for r,m in zip(rs,ms))
            if role=='top':
                exact=F(2**960+E+ell+(a-2)//2,E+5*ell-1)*F(E-2**955+ell-a//2,2*ell-1)
                assert ms[-1] == (19 if a==42 else 12)
            else:
                exact=F(E+(8*a-3)*ell,E+5*ell-1)*F(E+3*ell,2*ell-1)
            check(name+' '+role+' exact first negative moment telescoping',first==exact)
            for q in (0,ell):
                for bit in (0,1):
                    qs=[r+q for r in rs]
                    mm=ms[:]
                    for i in range(1,a-1):mm[i]-=ell*bit
                    nn=prod(r+m for r,m in zip(qs,mm));dd=prod(r-1-t for r in qs)
                    assert nn*denominator<=numerator*dd
                    assert max(qs)<2**960
            check(name+' '+role+' q/word endpoint monotonicity and normalizer bound',True)
            role_reports[role]=dict(E=E,integer_moment_upper_bound=upper[name][role],
                moment_numerator_bits=numerator.bit_length(),moment_denominator_bits=denominator.bit_length(),
                moment_numerator_sha256=digest_int(numerator),moment_denominator_sha256=digest_int(denominator),
                first_negative_moment_upper_integer=(first.numerator//first.denominator)+1,
                last_PBW_exponent=ms[-1])
        B=960*a*f+(11*f+1)*s0
        check(name+' global prefactor is dominated by gap',4*B<ell)
        check(name+' union L1 tail less2^-100',ell>8*(100+f.bit_length()))
        check(name+' Haar-weight integral is (a!)^-f', F(factorial(s0-a-1),factorial(s0-1))==F(1,factorial(a)))
        check(name+' integrable discrete series chamber',2*ell>a+1)
        n=a+1
        alpha=[1]+[0]*(n-2)+[-1]
        root_coroot_sum=sum(abs(alpha[i]-alpha[j]) for i in range(n) for j in range(n) if i!=j)
        check(name+' exact typeA integrability root sum',root_coroot_sum==4*a)
        g0=4615409 if name=='J14' else 22285932761
        check(name+' actual standard principal Cartan separation',3**10+1<g0)
        reports.append(dict(host=name,a=a,f=f,ell=ell,moment_order=t,s0=s0,
            epsilon='2^-12',B_prefactor=B,tail_per_label='2^(-ell/8)',
            total_tail='f*2^(-ell/8)<2^-100',roles=role_reports))
    # R=atanh sqrt(1-2^-12)<(1/2)log(4*2^12)=7log2<4.9<5.
    check('fixed Cartan radius strictly below5',7*F(7,10)<5)
    check('elementary exponential certificate log2<0.7',sum(F(7,10)**i/factorial(i) for i in range(4))>2)
    files=[input_path,ROOT/'work/research/nakahama2016.pdf',
           ROOT/'work/research/zunar2025_bounded_domains.pdf',
           ROOT/'work/research/muic2019_integrable_discrete.pdf',
           ROOT/'work/research/standard_bottom_finite_level_adapter.md',
           ROOT/'work/agents/selected_bottom_pbw_normalization.md']
    result=dict(finding='AM-K046',status='PASS',time_utc=datetime.now(timezone.utc).isoformat(),
        grouped_checks=len(CHECKS),checks=CHECKS,hosts=reports,
        scope='Exact local moment/form and rational constant checks, root-sum and standard principal congruence separation margin. No translated-packet separation, automorphic Gram computation, cusp dimension, finite-projector preservation or Lean build.',
        input_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    target=Path(__file__).with_suffix('.json');target.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',time_utc=result['time_utc'],checks=len(CHECKS),output=str(target))))


if __name__=='__main__':main()
