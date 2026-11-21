#!/usr/bin/env python3
"""T043: exact mixed certificate for all hook quotient powers and point orders."""
from pathlib import Path
import sys,json
import sympy as s
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent.parent/'rectangular'))
from verify_rectangular import character,z
from five_point_positive import LABELS
CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
LIMIT=240
v,t=s.symbols('v t');DATA=[];FACTORS=[]
for cyc in CLASSES:
    raw=[1]+[0]*(2*LIMIT-1)
    for ell in cyc:
        for j in range(ell,len(raw)):raw[j]+=raw[j-ell]
    sym=[raw[0]]+[raw[j]-raw[j-1] for j in range(1,len(raw))]
    m1=cyc.count(1);e=m1-1
    ideal=[]
    for offset in (0,-1,-2):
        ideal.append([(sym[2*k+offset] if 2*k+offset>=0 else 0)-(m1*sym[k-1] if k else 0) for k in range(LIMIT)])
    C,B,A=ideal
    hook=[e*sym[b+1]-sym[b+2] for b in range(LIMIT)]
    extra=[A[k]-e*B[k] for k in range(LIMIT)]
    DATA.append((sym,hook,C,extra))
    D=s.Poly(s.cancel(s.prod(1-v**ell for ell in cyc)/(1-v)),v)
    DS=s.Poly(s.expand(D.as_expr()*D.as_expr().subs(v,-v)),v)
    den_squared=sum(DS.nth(2*j)*t**j for j in range(5))
    even=sum(D.nth(2*j)*t**j for j in range(3))/den_squared
    odd=-sum(D.nth(2*j+1)*t**j for j in range(2))/den_squared
    HE=1/D.as_expr();jet=m1*t*HE.subs(v,t)
    cg=even-jet;eg=t*even-e*t*odd+(e-1)*jet
    hg=s.cancel(((e-1/v)*HE+1/v)/v)
    factors=((HE,v),(hg,v),(cg,t),(eg,t))
    for expr,var in factors:
        num=s.cancel(expr*(1-var**60)**4)
        assert s.denom(num)==1 and s.degree(num,var)<=239
        FACTORS.append(str(s.factor(expr)))
    for known,expr in ((C,cg),(extra,eg)):
        num,den=s.fraction(s.cancel(expr));num=s.Poly(num,t);den=s.Poly(den,t)
        for k in range(LIMIT):
            assert sum(den.nth(j)*known[k-j] for j in range(min(k,den.degree())+1))==num.nth(k)

def differences(values):
    out=[]
    while values:
        out.append(values[0]);values=[b-a for a,b in zip(values,values[1:])]
    return out

TABLE={};SUMMARY=[];ZEROS={};entries=0
for label in LABELS:
    weights=[120//z(cyc)*character(label,cyc) for cyc in CLASSES]
    values=[]
    for b in range(LIMIT):
        row=[]
        for k in range(LIMIT):
            num=sum(weight*(hook[b]*C[k]+sym[b]*extra[k])
                    for weight,(sym,hook,C,extra) in zip(weights,DATA))
            assert num%120==0 and num>=0,(label,b,k,num)
            row.append(num//120)
        values.append(row)
    table=[];mins=[None]*16;maxs=[0]*16;zeros=[]
    for rb in range(60):
        rtable=[]
        for rk in range(60):
            kd=[differences([values[rb+60*i][rk+60*j] for j in range(4)]) for i in range(4)]
            mixed=[]
            for i in range(4):
                mixed.extend(kd[0]);kd=[[b-a for a,b in zip(r1,r2)] for r1,r2 in zip(kd,kd[1:])]
            assert mixed[15]==0
            for index,c in enumerate(mixed):
                assert c>=0,(label,rb,rk,index,c)
                mins[index]=c if mins[index] is None else min(mins[index],c);maxs[index]=max(maxs[index],c)
            assert mixed[1]>0 and mixed[4]>0
            if not mixed[0]:zeros.append([rb,rk])
            rtable.append(mixed);entries+=16
        table.append(rtable)
    key=','.join(map(str,label));TABLE[key]=table;ZEROS[key]=zeros
    SUMMARY.append(dict(label=key,minima=mins,maxima=maxs,zero_pairs=zeros))
    print(label,'zeros',zeros,'minima',mins,flush=True)

(HERE/'HOOK_ALL_POWERS_TABLE.json').write_text(json.dumps(dict(
    statement='T-043',period=60,degrees=[3,3],
    index_order='labels[mu][(a-1)_mod_60][k_mod_60][4*i+j]',labels=TABLE),separators=(',',':'))+'\n')
(HERE/'HOOK_ALL_POWERS_SUMMARY.json').write_text(json.dumps(dict(
    entries=entries,negative_entries=0,zero_pairs=ZEROS,summary=SUMMARY,rational_factors=FACTORS),indent=2)+'\n')
(HERE/'HOOK_ALL_POWERS_CHECK.txt').write_text(
    'PASS: all28 rational factor bounds and14 even/odd versus direct-cycle recurrence checks.\n'
    'PASS: all403200 actual module multiplicities for0<=a-1,k<240 are nonnegative integers.\n'
    'PASS: all403200 mixed Newton constants are nonnegative; every(3,3)coefficient is zero and both first directional differences are positive.\n')
print('PASS all',entries,'mixed coefficients',flush=True)
