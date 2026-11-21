"""G-023: exact small Ehrhart interpolation and all fixed Newton constants."""
from pathlib import Path
from math import comb
import json
from staircase_five_trace import trace,CLASSES,SIZES,LABELS,CHARS

HERE=Path(__file__).resolve().parent
initial=[trace(0,r) for r in range(7)]
work=initial[:];newton=[]
while work:
    newton.append(work[0]);work=[b-a for a,b in zip(work,work[1:])]

def closed(g,r):
    if g==0:return sum(v*comb(r,j) for j,v in enumerate(newton))
    if g==1:
        if r%2:return 0
        h=r//2;return (h+1)**3+h**3
    if g==2:
        if r%2:return 0
        h=r//2;return 3*h*h+3*h+1
    if g==3:
        h,s=divmod(r,3)
        return h+1 if s==0 else (-h if s==1 else 0)
    if g==4:return (1,0,0,0,-1,0)[r%6]
    if g==5:return (1,0,-1,0)[r%4]
    return (1,-1,-1,1,0)[r%5]

# These samples exceed the exact Ehrhart degree and period requirements.
for g in range(7):
    limit=10 if g==0 else 16
    for r in range(limit):assert trace(g,r)==closed(g,r),(g,r)

def multiplicity(label,r):
    numerator=sum(SIZES[g]*CHARS[label][g]*closed(g,r) for g in range(7))
    assert numerator%120==0
    return numerator//120

table={};mins={};maxs={};zeros={}
for label,name in enumerate(LABELS):
    table[name]=[];mins[name]=[None]*7;maxs[name]=[None]*7;zeros[name]=[]
    for residue in range(60):
        values=[multiplicity(label,residue+60*q) for q in range(7)]
        constants=[]
        while values:
            constants.append(values[0]);values=[b-a for a,b in zip(values,values[1:])]
        assert all(v>=0 for v in constants)
        assert all(v>0 for v in constants[1:])
        table[name].append(constants)
        for j,v in enumerate(constants):
            mins[name][j]=v if mins[name][j] is None else min(mins[name][j],v)
            maxs[name][j]=v if maxs[name][j] is None else max(maxs[name][j],v)
        if not constants[0]:zeros[name].append(residue)

result={'statement':'G-023','identity_initial':initial,'identity_newton':newton,
        'table':table,'minimum_by_order':mins,'maximum_by_order':maxs,
        'zero_parameters':zeros,'checked_constants':7*60*7}
(HERE/'STAIRCASE_FIVE_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS',result['checked_constants'],'constants; identity Newton',newton,flush=True)
print('zeros',zeros,flush=True)
print('min positive',min(min(v[1:]) for v in mins.values()),flush=True)
