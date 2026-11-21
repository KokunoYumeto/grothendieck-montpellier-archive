#!/usr/bin/env python3
"""Exact finite search for balanced signed exponential characters.

This tests only the pair-Euler divisibility necessary condition.  It neither
constructs an equivariant object nor verifies any derived gluing or trace map.
For X0=x+y, Y=sqrt(d)(x-y), x^3=y^3=0 and integral x^2 y^2=4,
the class e^(a X0+b Y) has pair Euler Nm(a+b sqrt(d))^2.
Each orbit used here is stable under (a,b)->(-a,-b) and (a,b)->(a,-b).
The three moment equalities below verify the entire balanced character.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from itertools import combinations
from math import gcd, isqrt, lcm
from pathlib import Path
import json
import time


def orbit(a: int, b: int):
    return tuple(sorted({(a,b),(a,-b),(-a,b),(-a,-b)}))


def evaluate(d, orbits, weights):
    # The moment denoted A is N*q, and C is N*q^2.
    A=sum((len(o)*w*(o[0][0]**2+d*o[0][1]**2)
           for o,w in zip(orbits,weights)), F(0))
    B=sum((len(o)*w*(o[0][0]**2-d*o[0][1]**2)
           for o,w in zip(orbits,weights)), F(0))
    C=sum((len(o)*w*(o[0][0]**2-d*o[0][1]**2)**2
           for o,w in zip(orbits,weights)), F(0))
    if B or A<=0 or C<=0:
        return None
    N=A*A/C
    q=C/A
    n0=N-sum((len(o)*w for o,w in zip(orbits,weights)),F(0))
    scale=lcm(N.denominator,n0.denominator,
              *(w.denominator for w in weights))
    points={p:int(scale*w) for o,w in zip(orbits,weights) for p in o if w}
    if n0:
        points[(0,0)]=int(scale*n0)
    # Remove a common scalar from all virtual coefficients, exactly.
    common=0
    for n in points.values():common=gcd(common,abs(n))
    if common>1:
        points={p:n//common for p,n in points.items()}
    multiplier=F(scale,common)
    actual_N=N*multiplier
    actual_A=A*multiplier
    actual_C=C*multiplier
    assert actual_N.denominator==1 and actual_A.denominator==1
    assert sum(points.values())==actual_N
    assert sum(n*(a*a-d*b*b) for (a,b),n in points.items())==0
    assert sum(n*(a*a+d*b*b) for (a,b),n in points.items())==actual_A
    assert sum(n*(a*a-d*b*b)**2 for (a,b),n in points.items())==actual_C
    assert actual_N*q==actual_A and actual_N*q*q==actual_C
    euler=int(4*actual_A*actual_A)
    divisor=0
    pairs=[]
    for ((a,b),n),((c,e),m) in combinations(points.items(),2):
        pair=n*m*((a-c)**2-d*(b-e)**2)**2
        divisor=gcd(divisor,abs(pair))
        pairs.append(pair)
    assert divisor>0 and 2*sum(pairs)==euler and euler%divisor==0
    return {
        'd':d,'rank':int(actual_N),'q':str(q),
        'points':[{'a':a,'b':b,'virtual_rank':n}
                  for (a,b),n in sorted(points.items())],
        'ordinary_self_Euler':euler,'pair_Euler_gcd':divisor,
        'minimum_invariant_Euler_allowed_by_pair_divisibility':euler//divisor,
        'negative_virtual_weights':sum(n<0 for n in points.values()),
        'full_character_moments':{'N':str(actual_N),'Nq':str(actual_A),
                                   'Nq2':str(actual_C),'norm_moment':0},
        'actual_object_constructed':False,'finite_action_constructed':False,
        'semiregularity_checked':False,
    }


def search(d,bound,tbound,four=False):
    data=[]
    for a in range(bound+1):
        for b in range(bound+1):
            if a or b:
                o=orbit(a,b)
                data.append((o,len(o)*(a*a-d*b*b)))
    ts=sorted({F(a,b) for a in range(-tbound,tbound+1) if a
               for b in range(1,tbound+1)})
    best=None
    eligible=0
    attempted=0
    passing=[]
    for pair in combinations(data,2):
        attempted+=1
        (o1,b1),(o2,b2)=pair
        for sign in (1,-1):
            result=evaluate(d,(o1,o2),(F(sign),F(-sign*b1,b2)))
            if result is None:continue
            eligible+=1
            score=result['minimum_invariant_Euler_allowed_by_pair_divisibility']
            if best is None or score<best['minimum_invariant_Euler_allowed_by_pair_divisibility']:
                best=result
            if score<=4:passing.append(result)
    for triple in combinations(data,3):
        (o1,b1),(o2,b2),(o3,b3)=triple
        for t in ts:
            attempted+=1
            for sign in (1,-1):
                result=evaluate(d,(o1,o2,o3),(F(sign),sign*t,
                                 F(-sign*b1,b3)-sign*t*F(b2,b3)))
                if result is None:continue
                eligible+=1
                score=result['minimum_invariant_Euler_allowed_by_pair_divisibility']
                if best is None or score<best['minimum_invariant_Euler_allowed_by_pair_divisibility']:
                    best=result
                if score<=4:passing.append(result)
    if four:
        four_parameters=(F(-2),F(-1),F(1),F(2))
        for quadruple in combinations(data,4):
            (o1,b1),(o2,b2),(o3,b3),(o4,b4)=quadruple
            for t in four_parameters:
                for u in four_parameters:
                    attempted+=1
                    for sign in (1,-1):
                        result=evaluate(d,(o1,o2,o3,o4),
                            (F(sign),sign*t,sign*u,
                             F(-sign*b1,b4)-sign*t*F(b2,b4)-sign*u*F(b3,b4)))
                        if result is None:continue
                        eligible+=1
                        score=result['minimum_invariant_Euler_allowed_by_pair_divisibility']
                        if best is None or score<best['minimum_invariant_Euler_allowed_by_pair_divisibility']:
                            best=result
                        if score<=4:passing.append(result)
    # A passing list here would be only a necessary arithmetic candidate list.
    return {'d':d,'coordinate_bound':bound,'rational_weight_parameter_bound':tbound,
            'four_orbits_included':four,
            'four_orbit_free_parameters':[-2,-1,1,2] if four else [],
            'attempted_parameter_rows':attempted,'eligible_positive_rank_q_cases':eligible,
            'best':best,'passing_necessary_candidates':passing[:100],
            'passing_count':len(passing)}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--bound',type=int,default=3)
    parser.add_argument('--t-bound',type=int,default=3)
    parser.add_argument('--d',default='2,3,5,6,10,13,17')
    parser.add_argument('--four',action='store_true')
    parser.add_argument('--output',default='rm_signed_class_search_output.json')
    args=parser.parse_args()
    ds=[int(x) for x in args.d.split(',')]
    assert all(d>1 and isqrt(d)**2!=d for d in ds)
    start=time.monotonic()
    results=[]
    for d in ds:
        r=search(d,args.bound,args.t_bound,args.four);results.append(r)
        print(json.dumps({'d':d,'eligible':r['eligible_positive_rank_q_cases'],
                          'best_minimum_Euler':r['best']['minimum_invariant_Euler_allowed_by_pair_divisibility'],
                          'passing_count':r['passing_count']}),flush=True)
    out={'status':'EXACT FINITE EXPLORATION ONLY','elapsed_seconds':time.monotonic()-start,
         'scope':'Two or three sign/conjugation orbits plus zero, and optionally four with the separately recorded parameter set; integer coordinates within bound; finite rational weight parameters; no universal exclusion inferred.',
         'results':results}
    Path(__file__).with_name(args.output).write_text(json.dumps(out,indent=2)+'\n')


if __name__=='__main__':main()
