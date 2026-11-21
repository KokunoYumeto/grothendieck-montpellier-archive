"""Exact norm in Q(sqrt(5),sqrt(41)); no numerical approximations."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime, timezone
import json

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def mul(x,y):
    out=[F(0)]*4
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            c=a*b
            if i&j&1: c*=5
            if i&j&2: c*=41
            out[i^j]+=c
    return tuple(out)
zero=(F(0),)*4
one=(F(1),F(0),F(0),F(0))
poly=[one]
for sa in (-1,1):
    for sb in (-1,1):
        m=tuple(map(F,(205,41*sa,5*sb,5*sa*sb)))
        m=tuple(a/4 for a in m)
        out=[zero]*(len(poly)+1)
        for i,c in enumerate(poly):
            out[i]=add(out[i],mul(c,neg(m)))
            out[i+1]=add(out[i+1],c)
        poly=out
assert all(c[1:]==zero[1:] for c in poly)
coeff=[int(c[0]) for c in poly]
assert all(c[0].denominator==1 for c in poly)
assert coeff==[3404025,-378225,13940,-205,1]
record=dict(statement_id='MT-ART10',date=datetime.now(timezone.utc).isoformat(),
            basis=['1','sqrt(5)','sqrt(41)','sqrt(205)'],
            radicand_coefficients=['205/4','41/4','5/4','5/4'],
            polynomial_coefficients_ascending_in_X_squared=coeff,
            trace_criterion_values=[205,63],trace_residues_mod4=[205%4,63%4],
            scope='Exact rational norm multiplication only; Galois group and integer-ring class are cited classical results.')
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
