#!/usr/bin/env python3
"""Exact supplementary constants for D-LNW-01; no external arithmetic."""
from fractions import Fraction as F
from pathlib import Path
import json

J=10**30;N=10**61
assert N>=2*J*J+9
assert N>2*J
assert F(1,10**29)*J/4==F(5,2)
assert 8<9
# j^2+j <= 2j^2 iff j(j-1)>=0.
assert 2*(2-1)>0
d=F(4,2**9)
assert d==F(1,128)<F(1,100)
r=(F(1,4)+d)/(1-d)
assert r==F(33,127)<F(26,99)<F(4,15)
assert (1-F(4,15))/4==F(11,60)
assert F(6)/(12*F(11,60)-2)==30
result={'status':'PASS','J':str(J),'N':str(N),
 'tail_error':str(d),'low_level_ratio':str(r),
 'common_ratio':'4/15','normalizer_support':'11/60',
 'total_degree_ceiling':30,
 'scope':'exact supplementary constants; published GLT2020(8.11) and universal proof remain mathematical inputs'}
p=Path(__file__).resolve().parent/'linear_constants_checked.json'
p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
