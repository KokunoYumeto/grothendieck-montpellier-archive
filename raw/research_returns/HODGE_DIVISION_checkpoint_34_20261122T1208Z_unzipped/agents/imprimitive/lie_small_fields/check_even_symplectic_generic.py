#!/usr/bin/env python3
"""Offline exact reconstruction directly from the retained original entries."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import hashlib,json,time
from parse_generic_bounds import certify

BASE=Path(__file__).resolve().parent
EXPECTED={'Sp4.0.jl':(8,F(1,4),19,196),'Sp6.0.jl':(4,F(17,63),66,378)}

def shift(cs,q):
    cs=list(map(F,cs))
    return [sum(cs[j]*comb(j,k)*q**(j-k) for j in range(k,len(cs))) for k in range(len(cs))]

def main():
    start=time.monotonic();raw=(BASE/'even_symplectic_generic_inputs.json').read_bytes()
    data=json.loads(raw);cert=json.loads((BASE/'even_symplectic_polynomials.json').read_text())
    assert cert['input_sha256']==hashlib.sha256(raw).hexdigest()
    assert {t['name'] for t in data['tables']}==set(EXPECTED)
    nr=nc=0
    for item,stored in zip(data['tables'],cert['tables']):
        q0,bound,n,m=EXPECTED[item['name']]
        assert item['threshold']==q0 and F(item['bound'])==bound
        reconstructed=certify(item,bound=bound);assert reconstructed==stored
        assert stored['character_types']==stored['class_types']==n and not stored['failures']
        ds=[]
        for row in stored['polynomial_input']:
            nr+=1;dc=shift(row['degree_coefficients'],q0)
            assert all(v>=0 for v in dc);ds.append(dc[0])
            for entry in row['entry_coefficient_polynomials']:
                cs=[]
                for poly in entry:
                    for j,c in enumerate(shift(poly,q0)):
                        if j==len(cs):cs.append(F(0))
                        cs[j]+=abs(c)
                assert all(bound*(dc[j] if j<len(dc) else 0)>=(cs[j] if j<len(cs) else 0)
                           for j in range(max(len(dc),len(cs))))
                nc+=1
        assert min(ds)==m
    assert (nr,nc)==(83,4549)
    c=F(17,63);v=(1-c)/4
    assert v==F(23,126) and 6/(12*v-2)==F(63,2)
    assert min(196,378)>F(63,2) and 18**2>F(63,2)
    assert 6/(12*F(2,9)-2)==9 and 8**2>9
    assert 6/(1+10*F(1,7)-2)==14 and 7**2>14
    result={'status':'PASS','input_sha256':cert['input_sha256'],'rows':nr,'cells':nc,
            'polynomial_sha256':hashlib.sha256((BASE/'even_symplectic_polynomials.json').read_bytes()).hexdigest(),
            'seconds':round(time.monotonic()-start,3)}
    (BASE/'check_even_symplectic_generic.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
