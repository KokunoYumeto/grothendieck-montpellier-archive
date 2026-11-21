"""Independent T042 mixed table from the exact B(T) presentation."""
from pathlib import Path
from math import comb,gcd
import json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent
TARGET=HERE.parent/"theta"/"outer5"/"Q_PLUS_SYMMETRIC_TABLE.json"
classes=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
sizes=[1,10,15,20,20,30,24]
labels=["5","4,1","3,2","3,1,1","2,2,1","2,1,1,1","1,1,1,1,1"]
chars=[[1,1,1,1,1,1,1],[4,2,0,1,-1,0,-1],[5,1,1,-1,1,-1,0],
       [6,0,-2,0,0,0,1],[5,-1,1,-1,-1,1,0],[4,-2,0,1,1,0,-1],
       [1,-1,1,1,-1,-1,1]]
t=s.symbols("t")
def power_type(cyc,r):
    out=[]
    for l in cyc:out += [l//gcd(l,r)]*gcd(l,r)
    return out
def determinant_from_traces(power):
    elementary=[1]
    for j in range(1,len(power)):
        num=sum((-1)**(i-1)*elementary[j-i]*power[i] for i in range(1,j+1))
        assert num%j==0
        elementary.append(num//j)
    return [(-1)**j*v for j,v in enumerate(elementary)]
def complete(det):
    out=[1]
    for n in range(1,240):
        out.append(-sum(det[j]*out[n-j] for j in range(1,min(n,len(det)-1)+1)))
    return out
def diffs(values):
    return [[sum((-1)**(i-j)*comb(i,j)*values[r+60*j] for j in range(i+1))
             for i in range(4)] for r in range(60)]
data=[];rational=[]
for cyc in classes:
    eps=(-1)**(5-len(cyc));e=cyc.count(1)-1
    pe=[0];pu=[0]
    for r in range(1,6):
        pp=power_type(cyc,r);m1=pp.count(1);m2=pp.count(2)
        pe.append(m1-1);pu.append(comb(m1,2)+m2-m1)
    de=determinant_from_traces(pe[:5])
    du=determinant_from_traces(pu)
    he=complete(de);hu=complete(du)
    at=lambda n:hu[n] if n>=0 else 0
    c0=[at(k)-eps*at(k-3) for k in range(240)]
    c1=[e*at(k)-eps*pu[1]*at(k-1)+eps*at(k-2) for k in range(240)]
    data.append(tuple(map(diffs,(he,[0]+he[:-1],c0,c1))))
    detE=sum(c*t**j for j,c in enumerate(de));detU=sum(c*t**j for j,c in enumerate(du))
    factors=[1/detE,t/detE,(1-eps*t**3)/detU,(e-eps*pu[1]*t+eps*t**2)/detU]
    degrees=[]
    for fun in factors:
        n,d=s.fraction(s.cancel(fun*(1-t**60)**4))
        assert d==1
        degree=s.Poly(n,t).degree()
        assert degree<=239
        degrees.append(int(degree))
    rational.append({"class":cyc,"degrees":degrees,
                     "scalar_plus":str(s.factor(factors[3]))})
target=json.loads(TARGET.read_text())
assert target["period"]==60 and target["degrees"]==[3,3]
entries=0;summary=[];zero={}
for label,char in zip(labels,chars):
    weights=[c*n for c,n in zip(char,sizes)]
    minima=[None]*16;maxima=[0]*16;zz=[]
    for ra in range(60):
        for rk in range(60):
            values=[]
            for i in range(4):
                for j in range(4):
                    num=sum(weight*(da[ra][i]*d1[rk][j]-db[ra][i]*d0[rk][j])
                            for weight,(da,db,d0,d1) in zip(weights,data))
                    assert num%120==0
                    values.append(num//120)
            assert values==target["labels"][label][ra][rk],(label,ra,rk)
            assert min(values)>=0 and values[15]==0 and values[1]>0 and values[4]>0
            if values[0]==0:zz.append([ra,rk])
            for j,v in enumerate(values):
                minima[j]=v if minima[j] is None else min(minima[j],v)
                maxima[j]=max(maxima[j],v)
            entries+=16
    summary.append({"label":label,"minima":minima,"maxima":maxima})
    zero[label]=zz
assert entries==403200
receipt={"statement":"Independent T042 mixed coefficient reconstruction","status":"PASS",
         "method":"Newton determinant identities for E and U from permutation cycle traces; exact B(T) scalar resolution; separable mixed forward differences. No point-jet computation used.",
         "coefficients_compared":entries,"zero_count":sum(map(len,zero.values())),
         "target_sha256":hashlib.sha256(TARGET.read_bytes()).hexdigest(),
         "rational_factors":rational,"summary":summary,"zero_pairs":zero}
(HERE/"Q_PLUS_SYMMETRIC_PRESENTATION_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":"PASS","entries":entries,"zero_pairs":zero},indent=2))
