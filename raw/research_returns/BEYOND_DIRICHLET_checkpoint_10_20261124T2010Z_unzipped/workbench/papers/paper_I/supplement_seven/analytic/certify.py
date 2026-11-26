#!/usr/bin/env python3
"""Rigorous order-seven twists of the 269 cubic Artin L-function at s=1.

Requires python-flint. All outputs are written beside this script.
No stored coefficient or numerical-value file is read.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform
import time

import flint
from flint import arb, acb, ctx

HERE=Path(__file__).resolve().parent
N=217083
MODULUS=49

def euler_coefficients(limit):
    """Exact coefficients, independently spelled out from all local factors."""
    spf=list(range(limit+1))
    for p in range(2,math.isqrt(limit)+1):
        if spf[p]==p:
            for n in range(p*p,limit+1,p):
                if spf[n]==n: spf[n]=p
    a=[0]*(limit+1)
    a[1]=1
    for n in range(2,limit+1):
        p=spf[n]
        rest=n
        k=0
        while rest%p==0:
            rest//=p
            k+=1
        if p==269:
            local=0
        elif p==3:
            local=1
        elif p%3==2:
            local=int(k%2==0)
        elif pow(269,(p-1)//3,p)==1:
            local=k+1
        else:
            local=(1,-1,0)[k%3]
        a[n]=a[rest]*local
    return a

def real_error(ball,radius):
    return ball+arb(0,radius.upper())

def complex_error(ball,radius):
    err=arb(0,radius.upper())
    return acb(ball.real+err,ball.imag+err)

def theta_tail(c,t,cutoff):
    ct=c*t
    r=(-ct).exp()
    den=-(-ct).expm1()
    return (-ct*(cutoff+1)).exp()*((cutoff+1)/den+r/den**2)

def weighted_tail(c,cutoff):
    """Joint L(1) tail: |a_n|<=d(n)<=n and E1(x)<=exp(-x)/x."""
    return 2*(-c*(cutoff+1)).exp()/(-(-c).expm1())

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--precision",type=int,default=300)
    parser.add_argument("--cutoff",type=int,default=550000)
    parser.add_argument("--base-cutoff",type=int,default=14000)
    args=parser.parse_args()
    ctx.prec=args.precision
    started=time.perf_counter()

    assert N==3*269**2 and math.gcd(N,49)==1
    assert len({pow(3,k,49) for k in range(42)})==42
    logs={pow(3,k,49):k%7 for k in range(42)}
    assert len(logs)==42 and logs[48]==0 and logs[N%49]==5
    # An order-7 nontrivial character cannot factor through the order-6
    # unit group modulo 7. All six nontrivial powers have conductor 49.
    zeta7=(acb(0,2)*arb.pi()/7).exp()
    zeta49=(acb(0,2)*arb.pi()/49).exp()
    roots=[zeta7**k for k in range(7)]
    gauss={}
    eps={}
    for j in range(1,7):
        gauss[j]=sum((roots[(j*logs[r])%7]*zeta49**r
                      for r in range(1,49) if r%7),acb(0))
        eps[j]=roots[(5*j)%7]*gauss[j]**2/49
        assert abs(gauss[j]).contains(arb(7))
        assert abs(eps[j]).contains(arb(1))
    for j in range(1,7):
        assert eps[j].overlaps(eps[7-j].conjugate())

    cutoff=max(args.cutoff,args.base_cutoff)
    a=euler_coefficients(cutoff)
    coeff_sha=hashlib.sha256(
        (",".join(map(str,a[1:]))+"\n").encode()).hexdigest()
    assert all(abs(a[n])<=n for n in range(1,len(a)))
    print(f"Exact coefficients ready through {cutoff}; "
          f"{sum(v!=0 for v in a)} nonzero.",flush=True)

    c=2*arb.pi()/(49*arb(N).sqrt())
    first=[arb(0) for _ in range(7)]
    second=[arb(0) for _ in range(7)]
    theta_one=[arb(0) for _ in range(7)]
    theta_two=[arb(0) for _ in range(7)]
    theta_half=[arb(0) for _ in range(7)]
    used=0
    for n in range(1,args.cutoff+1):
        if a[n] and n%7:
            r=logs[n%49]
            z=c*n
            w=(-z).exp()
            first[r]+=a[n]*w/n
            second[r]+=a[n]*c*z.expint(1)
            theta_one[r]+=a[n]*w
            theta_two[r]+=a[n]*w*w
            theta_half[r]+=a[n]*w.sqrt()
            used+=1
        if n%50000==0:
            print(f"Twists: n={n}, used={used}, "
                  f"seconds={time.perf_counter()-started:.1f}",flush=True)

    error=weighted_tail(c,args.cutoff)
    theta_errors={name:theta_tail(c,t,args.cutoff)
                  for name,t in (("one",arb(1)),("two",arb(2)),("half",arb(1)/2))}
    def transform(group,j):
        return sum((group[r]*roots[(r*j)%7] for r in range(7)),acb(0))
    values={}
    theta_checks={}
    for j in range(1,7):
        finite=transform(first,j)+eps[j]*transform(second,-j)
        values[j]=complex_error(finite,error)
        th1=complex_error(transform(theta_one,j),theta_errors["one"])
        th2=complex_error(transform(theta_two,j),theta_errors["two"])
        thh=complex_error(transform(theta_half,-j),theta_errors["half"])
        res1=th1-eps[j]*th1.conjugate()
        res2=th2-eps[j]*thh/2
        assert res1.contains(0), ("theta t=1",j,res1)
        assert res2.contains(0), ("theta t=2",j,res2)
        theta_checks[j]={
            "t1_residual":str(res1),
            "t2_residual":str(res2),
            "both_enclose_zero":True
        }
    for j in range(1,7):
        assert values[j].overlaps(values[7-j].conjugate())

    c0=2*arb.pi()/arb(N).sqrt()
    base_finite=arb(0)
    for n in range(1,args.base_cutoff+1):
        if a[n]:
            z=c0*n
            base_finite+=a[n]*((-z).exp()/n+c0*z.expint(1))
    base_error=weighted_tail(c0,args.base_cutoff)
    base=real_error(base_finite,base_error)
    assert base>0
    product=base
    for j in range(1,4):
        norm=values[j].real**2+values[j].imag**2
        assert norm>0
        product*=norm
    assert product>0

    # Establish a genuinely rigorous decimal precision target, not a printed
    # digit count. The interval diameters are also exported below.
    assert product.rad()<arb("1e-55")
    report={
        "python_version":platform.python_version(),
        "python_flint_version":flint.__version__,
        "precision_bits":ctx.prec,
        "base_conductor":N,
        "twisted_conductor":N*49**2,
        "gamma_factor":"Gamma_C(s)",
        "psi_definition":"psi(3)=exp(2*pi*i/7) modulo49; zero on multiples of7",
        "primitive_root_mod49":3,
        "psi_N_exponent_mod7":5,
        "coefficient_count":cutoff,
        "coefficient_sha256":coeff_sha,
        "twist_cutoff":args.cutoff,
        "nonzero_twist_terms":used,
        "base_cutoff":args.base_cutoff,
        "c_twisted":str(c),
        "c_base":str(c0),
        "base_L1":str(base),
        "base_tail_bound":str(base_error),
        "twist_joint_tail_bound":str(error),
        "root_numbers":{str(j):str(eps[j]) for j in range(1,7)},
        "gauss_sums":{str(j):str(gauss[j]) for j in range(1,7)},
        "twisted_L1":{str(j):str(values[j]) for j in range(1,7)},
        "product_L1_j0_to_j6":str(product),
        "product_radius":str(product.rad()),
        "first_weighted_sums_by_character_exponent":[str(x) for x in first],
        "second_weighted_sums_by_character_exponent":[str(x) for x in second],
        "theta_inversion_checks":theta_checks,
        "theta_tail_bounds":{name:str(v) for name,v in theta_errors.items()},
        "all_checks_passed":True,
        "elapsed_seconds":round(time.perf_counter()-started,3)
    }
    rendered=json.dumps(report,indent=2)+"\n"
    (HERE/"certificate.json").write_text(rendered)
    print(rendered,end="",flush=True)

if __name__=="__main__":
    main()

