#!/usr/bin/env python3
"""Direct cup calculation on the tuple actually realized by the fresh M proof.

This author reconstruction uses the previously authored exact cup implementation.
It is not an independent duplicate of that implementation.  No transpose/inverse
identification with the Appendix A tuple is used.
"""
from pathlib import Path
import json
import sympy as S
import e8_parabolic_determinant as P
from e8_group_and_tuple import a,b,c,d,ser

actual=[S.I*a**5]
for k in range(4,-1,-1):actual.extend([a**(-k)*b*a**k,a**(-k)*c*a**k])
actual.append(-S.I*d**5)
data=json.loads((Path(__file__).parents[2]/'g34/e8/actual_pullback_tuple.json').read_text())
assert list(map(ser,actual))==data['tuple']
product=S.eye(8)
for g in actual:product=product*g
assert product==S.eye(8)
assert [(S.eye(8)-g).rank() for g in actual]==[4]+[1]*10+[8]
P.gs=[[[P.K(P.F(x),P.F(y)) for x,y in row] for row in M] for M in data['tuple']]
report=P.main(Path(__file__).with_suffix('.json'),
 'Actual positive-orientation Fuchsian pullback tuple; words independently reconstructed')
assert report['odd_inert_valuations']=={'3':1}
print('ACTUAL realized tuple determinant class [−3] PASS')
