#!/usr/bin/env python3
"""Recheck every retained polynomial inequality using only Python Fraction.

This validates the polynomial certificate, not the correctness of the
published character-table inputs.  parse_generic_bounds.py separately
reconstructs these polynomial lists from the original retained expressions.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib,json,time

BASE=Path(__file__).resolve().parent
EXPECTED={'G2.01.jl':(27,5,126),'G2.02.jl':(27,5,124),
 'G2.101.jl':(28,5,280),'G2.103.jl':(28,5,280),
 'G2.111.jl':(31,5,126),'G2.113.jl':(31,5,126),
 'G2.121.jl':(31,5,124),'G2.123.jl':(31,5,124),
 '3D4.0.jl':(29,3,219),'3D4.11.jl':(33,3,219),
 '3D4.13.jl':(33,3,219)}

def shift(cs,q0):
    cs=list(map(F,cs))
    return [sum(cs[j]*comb(j,k)*q0**(j-k)
                for j in range(k,len(cs))) for k in range(len(cs))]

def main():
    start=time.monotonic()
    raw=(BASE/'generic_polynomial_bounds.json').read_bytes();data=json.loads(raw)
    original=(BASE/'generic_character_entries.json').read_bytes()
    assert data['input_sha256']==hashlib.sha256(original).hexdigest()
    assert {t['name'] for t in data['tables']}==set(EXPECTED)
    nr=nc=0;checks=[]
    for t in data['tables']:
        n,q0,mindeg=EXPECTED[t['name']]
        assert t['character_types']==t['class_types']==n and t['threshold']==q0
        assert len(t['polynomial_input'])==n-1
        actualmin=None
        for i,row in enumerate(t['polynomial_input'],2):
            assert row['row']==i
            dc=shift(row['degree_coefficients'],q0)
            assert dc[0]>1 and all(c>=0 for c in dc)
            actualmin=dc[0] if actualmin is None else min(actualmin,dc[0])
            assert len(row['entry_coefficient_polynomials'])==n-1
            nr+=1
            for entry in row['entry_coefficient_polynomials']:
                bounds=[]
                for poly in entry:
                    for j,c in enumerate(shift(poly,q0)):
                        if j==len(bounds):bounds.append(F(0))
                        bounds[j]+=abs(c)
                for j in range(max(len(dc),len(bounds))):
                    assert (dc[j] if j<len(dc) else 0)>=4*(bounds[j] if j<len(bounds) else 0)
                nc+=1
        assert actualmin==mindeg
        checks.append({'name':t['name'],'threshold':q0,'minimum_degree':mindeg})
    assert (nr,nc)==(318,9242)
    # The final all-field/tensor budget is strict at every surviving endpoint.
    assert F(12)*F(3,16)-2==F(1,4)
    assert F(6)/(F(12)*F(3,16)-2)==24
    assert 12**2>24 and min(124,219)>24 and min(12,14,26)>6
    result={'status':'PASS','rows':nr,'cells':nc,'input_sha256':data['input_sha256'],
            'polynomial_sha256':hashlib.sha256(raw).hexdigest(),
            'tables':checks,'seconds':round(time.monotonic()-start,3)}
    (BASE/'check_generic_polynomials.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
