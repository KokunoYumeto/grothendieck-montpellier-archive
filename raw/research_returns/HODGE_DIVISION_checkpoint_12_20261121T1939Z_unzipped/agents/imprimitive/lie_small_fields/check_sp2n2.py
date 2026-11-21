#!/usr/bin/env python3
"""Exact endpoint and all-rank elementary arithmetic for Sp(2n,2).

The unverified-primary-source gate of the companion mathematical draft is not a
computational assertion. This program does not claim to prove that input.
"""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
import hashlib, importlib.util, json, time

BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cyc',BASE.parent/'sporadic/verify_quarter_bound.py')
cyc=importlib.util.module_from_spec(spec);spec.loader.exec_module(cyc)
@lru_cache(None)
def is_real(z):
    if isinstance(z,int):return True
    n,c=z;v=[0]*n
    for j,a in enumerate(c):v[j]+=a;v[-j%n]-=a
    return (cyc.fmpz_poly(v)%cyc.phi(n)).is_zero()
raw=(BASE/'sp2n2_character_inputs.json').read_bytes()
data=json.loads(raw);ts={t['name']:t for t in data['tables']}
assert set(ts)=={'S8(2)','S10(2)','S12(2)'}
start=time.monotonic();records=[];count=0
for name,n,expected_rows,minimum in [('S8(2)',4,81,35),('S10(2)',5,198,155),('S12(2)',6,477,651)]:
    t=ts[name];rows=t['characters']
    order=2**(n*n)
    for i in range(1,n+1):order*=2**(2*i)-1
    assert t['order']==order==sum(t['sizes'])
    assert len(rows)==len(t['sizes'])==expected_rows
    assert sum(c[0]**2 for c in rows)==order
    assert min(c[0] for c in rows if c[0]>1)==minimum
    best=Fraction(0);witness=[]
    for i,c in enumerate(rows):
        a=c[0]
        if a==1:continue
        for j,z in enumerate(c):
            k=cyc.key(z)
            assert is_real(k)
            if j==0:continue
            # The triangle estimate on the RETAINED root-of-unity expression
            # is valid even when GAP's ordering on cyclotomics is not real order.
            bound=abs(z) if isinstance(z,int) else sum(abs(x) for x in z[1])
            ratio=Fraction(bound,a);count+=1
            if ratio>best:best=ratio;witness=[]
            if ratio==best:witness.append({'row':i+1,'class':j+1,'degree':a,
                'value':z,'order':t['orders'][j]})
    assert best==({'S8(2)':Fraction(3,5),'S10(2)':Fraction(17,31),'S12(2)':Fraction(11,21)}[name])
    assert best<=Fraction(3,5)
    assert any(isinstance(w['value'],int) and Fraction(abs(w['value']),w['degree'])==best for w in witness)
    records.append({'table':name,'complete_rows':len(rows),'minimum_degree':minimum,
                    'certified_max_absolute_ratio':str(best),'attaining_witnesses':witness,
                    'source_information':t['information'],'extension_info':t['extension_info']})

# Elliptic centralizer <=3^n and the elementary degree floor
# max(155,2^(n-1)-1) for n>=5: check the finite beginning and monotonic step.
assert 36*3**5 < 25*155**2
assert 36*3**6 < 25*155**2
assert 36*3**7 < 25*(2**6-1)**2
# For x=2^(n-1)>=64, (2x-1)^2 >3(x-1)^2; identity x^2+2x-2>0.
assert 64**2+2*64-2>0
assert Fraction(1)+10*Fraction(1,9)-2==Fraction(1,9)
assert Fraction(1)+10*Fraction(1,5)-2==1
assert Fraction(6)/Fraction(1,9)==54<155
assert Fraction(6)<35
out={'status':'PASS','input_sha256':hashlib.sha256(raw).hexdigest(),
     'complete_rows':sum(len(t['characters']) for t in ts.values()),
     'nontrivial_row_nonidentity_entries':count,'records':records,
     'elliptic_ratio_bound':'sqrt(3^n)/max(155,2^(n-1)-1)<5/6 for n>=5',
     'symbolic_induction':'(2x-1)^2-3(x-1)^2=x^2+2x-2>0 for x>=64',
     'conditional_Hurwitz_degree_ceiling':54,
     'source_gate':'GM1998 proper-parabolic semisimple 5/6 input requires primary verification',
     'seconds':round(time.monotonic()-start,3)}
(BASE/'check_sp2n2.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
