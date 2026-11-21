"""Exact bivariate G-019 certificate for all Sym^a(Q) and all point powers."""
from pathlib import Path
from math import comb
import sys, json, csv
import sympy as sym

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'rectangular'))
from verify_rectangular import partitions,character,z

labels=list(partitions(5))
classes=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
sixclasses=((1,1,1,1,1,1),(2,2,2),(2,2,1,1),(3,3),(6,),(4,1,1),(5,1))
s,t=sym.symbols('s t');period=60;limit=240
classdata=[];identities={}
for cyc,six in zip(classes,sixclasses):
    eps=(-1)**(5-len(cyc));e=cyc.count(1)-1;u=character((3,2),cyc)
    detE=sym.cancel(sym.prod(1-s**c for c in cyc)/(1-s))
    detU=sym.cancel(sym.prod(1-eps**c*t**c for c in six)/(1-eps*t))
    cseries=(1-eps*t**3)/detU
    extra=(t-u*t**2+eps*e*t**3)/detU
    for name,expr,var in [('E',1/detE,s),('sE',s/detE,s),('C',cseries,t),('extra',extra,t)]:
        num=sym.cancel(expr*(1-var**60)**4)
        assert sym.denom(num)==1
        assert sym.degree(num,var)<=239
        identities[str(cyc)+':'+name]=str(sym.factor(expr))
    raw=[1]+[0]*(limit-1)
    for length in cyc:
        for degree in range(length,limit):raw[degree]+=raw[degree-length]
    se=[raw[0]]+[raw[i]-raw[i-1] for i in range(1,limit)]
    raw=[1]+[0]*(limit-1)
    for length in six:
        for degree in range(length,limit):raw[degree]+=eps**length*raw[degree-length]
    su=[raw[0]]+[raw[i]-eps*raw[i-1] for i in range(1,limit)]
    cs=[su[k]-(eps*su[k-3] if k>=3 else 0) for k in range(limit)]
    ex=[(su[k-1] if k>=1 else 0)-(u*su[k-2] if k>=2 else 0)+(eps*e*su[k-3] if k>=3 else 0) for k in range(limit)]
    classdata.append((se,cs,ex))

tables={};summary=[];bad=[];entry_count=0
for mu in labels:
    factors=[120//z(cyc)*character(mu,cyc) for cyc in classes]
    values=[]
    for a in range(limit):
        row=[]
        for k in range(limit):
            value=sum(factor*(se[a]*cs[k]+(se[a-1]*ex[k] if a else 0))
                      for factor,(se,cs,ex) in zip(factors,classdata))
            assert value%120==0 and value>=0,(mu,a,k,value)
            row.append(value//120)
        values.append(row)
    table=[];minima=[None]*16;maxima=[0]*16
    for ra in range(60):
        rtable=[]
        for rk in range(60):
            block=[[values[ra+60*i][rk+60*j] for j in range(4)] for i in range(4)]
            # Differences in k first, then in a.
            kdiff=[]
            for row in block:
                coeff=[]
                while row:
                    coeff.append(row[0]);row=[b-a for a,b in zip(row,row[1:])]
                kdiff.append(coeff)
            coeffs=[]
            for i in range(4):
                coeffs.extend(kdiff[0]);kdiff=[[b-a for a,b in zip(row1,row2)] for row1,row2 in zip(kdiff,kdiff[1:])]
            for j,c in enumerate(coeffs):
                entry_count+=1
                minima[j]=c if minima[j] is None else min(minima[j],c)
                maxima[j]=max(maxima[j],c)
                if c<0:bad.append((mu,ra,rk,j,c))
            rtable.append(coeffs)
        table.append(rtable)
    tables[','.join(map(str,mu))]=table
    summary.append({'label':','.join(map(str,mu)),'minima':minima,'maxima':maxima})
    print(mu,'minima',minima,'negative_count',len(bad),flush=True)

print('TOTAL',entry_count,'NEGATIVE',len(bad),'first',bad[:20],flush=True)
(HERE/'FIVE_POINT_SYMMETRIC_QUOTIENT_SUMMARY.json').write_text(json.dumps({
    'entries':entry_count,'negative_entries':len(bad),'negative_examples':bad[:20],
    'summary':summary,'rational_factors':identities},indent=2)+'\n')
if not bad:
    (HERE/'FIVE_POINT_SYMMETRIC_QUOTIENT_TABLE.json').write_text(json.dumps({
        'statement':'G-019','period':60,'degrees':[3,3],
        'index_order':'labels[mu][a_mod_60][k_mod_60][4*i+j]',
        'labels':tables},separators=(',',':'))+'\n')
    (HERE/'FIVE_POINT_SYMMETRIC_QUOTIENT_CHECK.txt').write_text(
        'PASS: all28 exact one-variable rational factors have common denominator(1-t^60)^4 and numerator degree<=239.\n'
        'PASS: all403200 irreducible values in0<=a,k<240 are nonnegative integers.\n'
        'PASS: all403200 mixed Newton coefficients on3600 residue pairs and7 labels are nonnegative integers.\n'
        'Exact rational identities extend each tensor Newton polynomial to all nonnegative quotient parameters.\n')
