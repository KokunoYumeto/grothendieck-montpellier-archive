#!/usr/bin/env python3
"""Rigorous explicit-formula bound for a hypothetical unramified cubic of M.

The prime-ideal counts are a separate mathematical input. This program
certifies the analytic inequality using the separately verified principality input;
it does not infer principality from PARI bnfinit or from GRH.
The intended exact principality witnesses and replay are separate files.

Source: Odlyzko (1990), JTNB 2(1), p.122, equations (2.3)--(2.4).
M has degree56, signature(2,27), |disc|=3^55*7^62. A cyclic cubic
unramified extension has degree168 and signature(6,81).
For b=14 and F(x)=H(x/b)/cosh(x/2), H is the normalized
autocorrelation of 1+cos(pi*t) on [-1,1], zero elsewhere.
This is an unconditional admissible explicit-formula kernel.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from fractions import Fraction

import flint
from flint import acb, arb, ctx

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('counts',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--b',type=Fraction,default=Fraction(14))
    parser.add_argument('--precision',type=int,default=192)
    args=parser.parse_args()
    with args.counts.open() as f:
        rows=[(int(r['norm']),int(r['count'])) for r in csv.DictReader(f,delimiter='\t')]
    assert rows and len({q for q,_ in rows})==len(rows)
    assert all(q>=2 and c>0 for q,c in rows)

    assert args.b in (Fraction(14),Fraction(27,2)) and args.precision>=128
    ctx.prec=args.precision
    pi=arb.pi();b=arb(args.b.numerator)/args.b.denominator;eps=arb(1)/(2**14)
    def H(t):
        return ((2-t)*(1+(pi*t).cos()/2)/3+(pi*t).sin()/(2*pi))
    def i_integrand(z,analytic):
        return (1-H(z/b)/(z/2).cosh())/(2*(z/2).sinh())
    middle=acb.integral(i_integrand,eps,2*b,
                       rel_tol=arb(2)**-120,abs_tol=arb(2)**-120)
    assert middle.is_finite() and middle.imag.contains(0)
    # |H''|<=6 gives 0 <= the omitted integrand <= x for b>=2.
    # The exact tail is -log(tanh(b/2)). Thus this is an upper bound.
    I_upper=middle.real-(b/2).tanh().log()+eps*eps/2

    def a_integrand(z,analytic):
        return H(z/b)/(2*(z/2).cosh()**2)
    A=acb.integral(a_integrand,0,2*b,
                   rel_tol=arb(2)**-120,abs_tol=arb(2)**-120)
    assert A.is_finite() and A.imag.contains(0)

    prime_sum=arb(0);number_terms=0
    for q,count in rows:
        logq=arb(q).log()
        for m in range(1,41):
            argument=m*logq
            if argument>2*b:
                break
            assert argument<2*b  # no ambiguous boundary comparisons
            term=4*logq*H(argument/b)/(q**m+1)
            assert term>0
            prime_sum+=count*term
            number_terms+=1

    logarithm=((8*pi).log()+arb.const_euler()-I_upper+A.real/28
               -b/63+prime_sum/56)
    lower=logarithm.exp()
    rd_M=((55*arb(3).log()+62*arb(7).log())/56).exp()
    # This program also remains useful for partial witness sets. Only
    # certify a contradiction if the interval comparison proves it.
    contradicted=bool(lower>rd_M)
    if sum(c for _,c in rows)==592 and len(rows)==204:
        assert lower>arb(2541)/100
        assert rd_M<arb(12683)/500
        assert contradicted

    out={
        'kind':'certified analytic inequality with separately checked prime-ideal input',
        'principality_is_a_separate_required_input':True,
        'no_GRH_used_in_analytic_bound':True,
        'python_flint_version':flint.__version__,
        'precision_bits':ctx.prec,
        'base_degree':56,'extension_degree':168,
        'extension_signature':[6,81],
        'b_exact':str(args.b),'epsilon_exact':'1/16384',
        'candidate_ideal_count':sum(c for _,c in rows),
        'distinct_norm_count':len(rows),'prime_power_terms':number_terms,
        'I_upper_ball':str(I_upper),'A_ball':str(A.real),
        'prime_sum_ball':str(prime_sum),
        'root_discriminant_lower_ball':str(lower),
        'root_discriminant_M_ball':str(rd_M),
        'gap_ball':str(lower-rd_M),
        'contradiction_if_input_principality_is_certified':contradicted,
        'counts_sha256':hashlib.sha256(args.counts.read_bytes()).hexdigest(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    text=json.dumps(out,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    print(text,end='')

if __name__=='__main__':main()
