"""Numerical route search only; all reported zeros require exact verification.

For a cyclic quotient with distinct faithful coordinate characters, its
punctured affine space has a free cyclic action. Primitive-order grading
fixed components are smooth axes. This searches for cancellation of their
simple Molien residues while the group lies in SL.
"""
from cmath import exp, pi
from itertools import combinations
from math import gcd
from random import Random
import json

rng = Random(20261121)
hits=[]
checked=0
for order in range(3,81):
    units=[a for a in range(1,order) if gcd(a,order)==1]
    if len(units)<2:
        continue
    roots=[exp(2j*pi*a/order) for a in range(order)]
    inverses={a:pow(a,-1,order) for a in units}
    for dimension in range(2,min(len(units),14)+1):
        if len(units)<=16:
            population=combinations(units,dimension)
        else:
            population=(tuple(sorted(rng.sample(units,dimension))) for _ in range(3000))
        for weights in population:
            if sum(weights)%order:
                continue
            checked+=1
            pieces=[]
            for a in weights:
                value=1+0j
                for b in weights:
                    if b!=a:
                        value/=1-roots[(1-b*inverses[a])%order]
                pieces.append(value)
            total=sum(pieces)
            scale=sum(abs(value) for value in pieces)
            if abs(total)<=1e-10*scale:
                hits.append({'order':order,'weights':weights,'relative_residue':abs(total)/scale})
                print('CANDIDATE',hits[-1],flush=True)
                if len(hits)>=20:
                    break
        if len(hits)>=20:
            break
    if len(hits)>=20:
        break
print(json.dumps({'checked':checked,'candidate_count':len(hits),'candidates':hits},indent=2))
