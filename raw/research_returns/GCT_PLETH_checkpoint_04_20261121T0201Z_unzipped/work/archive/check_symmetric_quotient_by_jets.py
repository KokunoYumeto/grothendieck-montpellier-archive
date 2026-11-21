"""Independent G019 certificate from actual fixed-point jets, without U."""
from pathlib import Path
from math import comb
import json, hashlib
import sympy as s

HERE=Path(__file__).resolve().parent
TARGET=HERE.parent/"root"/"FIVE_POINT_SYMMETRIC_QUOTIENT_TABLE.json"
classes=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
sizes=[1,10,15,20,20,30,24]
labels=["5","4,1","3,2","3,1,1","2,2,1","2,1,1,1","1,1,1,1,1"]
chars=[
 [1,1,1,1,1,1,1],[4,2,0,1,-1,0,-1],
 [5,1,1,-1,1,-1,0],[6,0,-2,0,0,0,1],
 [5,-1,1,-1,-1,1,0],[4,-2,0,1,1,0,-1],
 [1,-1,1,1,-1,-1,1]]

def characteristic(cyc):
    # det(1-tg|E)=det(1-tg|Perm_5)/(1-t).
    p=[1]
    for length in cyc:
        nxt=p+[0]*length
        for j,a in enumerate(p):nxt[j+length]-=a
        p=nxt
    assert len(p)==6 and sum(p)==0
    d=[];carry=0
    for a in p[:-1]:carry+=a;d.append(carry)
    return d

def complete_traces(d,n):
    h=[1]
    for k in range(1,n+1):
        h.append(-sum(d[j]*h[k-j] for j in range(1,min(4,k)+1)))
    return h

def diffs(values):
    return [[sum((-1)**(i-j)*comb(i,j)*values[r+60*j]
                 for j in range(i+1)) for i in range(4)]
            for r in range(60)]

classdata=[];rational=[]
x,t=s.symbols("x t")
common=(1-t**60)**4
def even_substitute(poly):
    p=s.Poly(poly,x)
    assert all(j[0]%2==0 for j,_ in p.terms())
    return sum(c*t**(j[0]//2) for j,c in p.terms())
def square_variable(expr):
    n,d=s.fraction(s.cancel(expr))
    return s.cancel(even_substitute(n)/even_substitute(d))

for cyc in classes:
    d=characteristic(cyc)
    h=complete_traces(d,478)
    at=lambda n: h[n] if n>=0 else 0
    fixed=cyc.count(1)
    ha=[at(a) for a in range(240)]
    hb=[at(a-1) for a in range(240)]
    # Euler characteristics from the equivariant Taylor/jet sequence.
    aa=[at(2*k)-fixed*at(k-1) for k in range(240)]
    bb=[fixed*at(k-1)-at(2*k-1) for k in range(240)]
    classdata.append(tuple(map(diffs,(ha,hb,aa,bb))))
    H=1/s.Poly.from_list(list(reversed(d)),gens=x).as_expr()
    even=square_variable((H+H.subs(x,-x))/2)
    odd=square_variable((H-H.subs(x,-x))/(2*x))
    ht=H.subs(x,t)
    factors=[ht,t*ht,even-fixed*t*ht,fixed*t*ht-t*odd]
    degs=[]
    for fun in factors:
        num,den=s.fraction(s.cancel(fun*common))
        assert den==1
        degree=s.Poly(num,t).degree()
        assert degree<=239
        degs.append(int(degree))
    rational.append({"class":cyc,"factor_degrees":degs,
                     "A":str(s.factor(factors[2])),
                     "correction":str(s.factor(factors[3]))})

target=json.loads(TARGET.read_text())
assert target["period"]==60 and target["degrees"]==[3,3]
assert set(target["labels"])==set(labels)
entries=0;zeros=[];summary=[]
for row,label in enumerate(labels):
    mins=[None]*16;maxs=[0]*16
    weights=[n*c for n,c in zip(sizes,chars[row])]
    for ra in range(60):
        for rk in range(60):
            coeff=[]
            for i in range(4):
                for j in range(4):
                    num=sum(weight*(da[ra][i]*dc[rk][j]+db[ra][i]*de[rk][j])
                            for weight,(da,db,dc,de) in zip(weights,classdata))
                    assert num%120==0,(label,ra,rk,i,j,num)
                    value=num//120
                    assert value>=0,(label,ra,rk,i,j,value)
                    coeff.append(value);entries+=1
            assert coeff==target["labels"][label][ra][rk],(label,ra,rk)
            if coeff[0]==0:zeros.append([label,ra,rk])
            for j,value in enumerate(coeff):
                mins[j]=value if mins[j] is None else min(mins[j],value)
                maxs[j]=max(maxs[j],value)
    assert mins[1]>0 and mins[4]>0
    summary.append({"label":label,"minima":mins,"maxima":maxs})
assert entries==403200
assert len(zeros)==44
receipt={
 "statement":"Independent G019 fixed-point-jet reconstruction",
 "status":"PASS","coefficients_compared":entries,
 "method":"Characteristic-polynomial recurrence for Sym(E); fixed-point jets; separable mixed forward differences; no use of U or the six-letter presentation.",
 "target_sha256":hashlib.sha256(TARGET.read_bytes()).hexdigest(),
 "rational_factor_checks":rational,
 "summary":summary,"exact_zero_triples":zeros,
 "global_zero_argument":"Every label has strictly positive (i,j)=(1,0) and (0,1) coefficients on all residues, so the listed zero triples in 0<=a,k<60 are the complete zero set.",
 "index_order":"label,a_mod_60,k_mod_60,4*i+j"
}
(HERE/"SYMMETRIC_QUOTIENT_JET_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({"status":"PASS","compared":entries,"zero_count":len(zeros),
                  "target_sha256":receipt["target_sha256"],
                  "zero_triples":zeros},indent=2))
