#!/usr/bin/env python3
"""T042: exact mixed-residue certificate, independently using fat-point jets."""
from pathlib import Path
from math import comb
import sys,json
import sympy as s
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import character,z
from five_point_positive import LABELS
CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
SIX=((1,1,1,1,1,1),(2,2,2),(2,2,1,1),(3,3),(6,),(4,1,1),(5,1))
LIMIT=240
v=s.symbols('v')
DATA=[]
for cyc,six in zip(CLASSES,SIX):
    raw=[1]+[0]*(2*LIMIT-1)
    for ell in cyc:
        for j in range(ell,len(raw)):raw[j]+=raw[j-ell]
    sym=[raw[0]]+[raw[j]-raw[j-1] for j in range(1,len(raw))]
    # Actual fat-point evaluation: trace of order-k jets is m1 Sym^(k-1)E.
    m1=cyc.count(1)
    c0=[sym[2*k]-(m1*sym[k-1] if k else 0) for k in range(LIMIT)]
    c1=[sym[2*k+1]-(m1*sym[k-1] if k else 0) for k in range(LIMIT)]
    DATA.append((sym,c0,c1))
    eps=(-1)**(5-len(cyc));e=m1-1;u=character((3,2),cyc)
    detE=s.cancel(s.prod(1-v**ell for ell in cyc)/(1-v))
    detU=s.cancel(s.prod(1-eps**ell*v**ell for ell in six)/(1-eps*v))
    factors=(1/detE,v/detE,(1-eps*v**3)/detU,(e-eps*u*v+eps*v**2)/detU)
    for expr in factors:
        num=s.cancel(expr*(1-v**60)**4)
        assert s.denom(num)==1 and s.degree(num,v)<=239
    # Compare jet construction with the exact B(T) presentation rational series.
    for known,expr in ((c0,factors[2]),(c1,factors[3])):
        num,den=s.fraction(s.cancel(expr));num=s.Poly(num,v);den=s.Poly(den,v)
        for k in range(LIMIT):
            assert sum(den.nth(j)*known[k-j] for j in range(min(k,den.degree())+1))==num.nth(k)

def differences(values):
    out=[]
    while values:
        out.append(values[0]);values=[b-a for a,b in zip(values,values[1:])]
    return out

TABLE={};SUMMARY=[];zero_pairs={};entry_count=0
for label in LABELS:
    weights=[120//z(cyc)*character(label,cyc) for cyc in CLASSES]
    values=[]
    for a in range(LIMIT):
        row=[]
        for k in range(LIMIT):
            numerator=sum(weight*(sym[a]*c1[k]-(sym[a-1]*c0[k] if a else 0))
                          for weight,(sym,c0,c1) in zip(weights,DATA))
            assert numerator%120==0 and numerator>=0,(label,a,k,numerator)
            row.append(numerator//120)
        values.append(row)
    table=[];mins=[None]*16;maxs=[0]*16;zeros=[]
    for ra in range(60):
        rtable=[]
        for rk in range(60):
            kd=[differences([values[ra+60*i][rk+60*j] for j in range(4)]) for i in range(4)]
            mixed=[]
            for i in range(4):
                mixed.extend(kd[0]);kd=[[b-a for a,b in zip(row1,row2)] for row1,row2 in zip(kd,kd[1:])]
            for j,c in enumerate(mixed):
                assert c>=0,(label,ra,rk,j,c)
                mins[j]=c if mins[j] is None else min(mins[j],c);maxs[j]=max(maxs[j],c)
            assert mixed[15]==0  # actual total polynomial degree is at most five
            assert mixed[1]>0 and mixed[4]>0
            if mixed[0]==0:zeros.append([ra,rk])
            rtable.append(mixed);entry_count+=16
        table.append(rtable)
    key=','.join(map(str,label));TABLE[key]=table;zero_pairs[key]=zeros
    SUMMARY.append(dict(label=key,minima=mins,maxima=maxs,zero_pairs=zeros))
    print(label,'zeros',zeros,'minima',mins,flush=True)

(HERE/'Q_PLUS_SYMMETRIC_TABLE.json').write_text(json.dumps(dict(
    statement='T-042',period=60,degrees=[3,3],
    index_order='labels[mu][a_mod_60][k_mod_60][4*i+j]',labels=TABLE),separators=(',',':'))+'\n')
(HERE/'Q_PLUS_SYMMETRIC_SUMMARY.json').write_text(json.dumps(dict(
    entries=entry_count,negative_entries=0,zero_pairs=zero_pairs,summary=SUMMARY),indent=2)+'\n')
(HERE/'Q_PLUS_SYMMETRIC_CHECK.txt').write_text(
    'PASS: all28 rational factors have denominator dividing(1-t^60)^4 and numerator degree<=239.\n'
    'PASS: all14 jet-derived scalar series agree with the independently obtained B(T) presentation series through degree239 and by denominator recurrence.\n'
    'PASS: all403200 values on0<=a,k<240 are nonnegative integers.\n'
    'PASS: all403200 mixed Newton coefficients are nonnegative; every(3,3) coefficient is zero; both first directional differences are strictly positive.\n'
    'Consequently every zero pair is in the displayed fixed60-by60 box; no unbounded zero family remains.\n')
print('PASS all',entry_count,'mixed coefficients',flush=True)
