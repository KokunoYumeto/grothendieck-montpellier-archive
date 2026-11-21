"""Independent T048 exact phase reconstruction and coefficient domination."""
from pathlib import Path
from itertools import product
from fractions import Fraction
from math import comb,factorial
import json,hashlib
import sympy as s

HERE=Path(__file__).resolve().parent
x,B,K=s.symbols("x B K");variables=(x,B,K)
b=B+1;k=K+8;a=x+b;c=2*k-3
def res(n,p,m):return int(s.sympify(n).subs(dict(zip(variables,p))))%m
def h(n,g,p):
    n=s.sympify(n)
    if g==0:return (n+1)*(n+2)*(n+3)/6
    if g==1:return ((n+2)**2-res(n,p,2))/4
    if g==2:return s.Integer(0) if res(n,p,2) else (n+2)/2
    if g==3:return (n+3-res(n,p,3))/3
    if g==4:return s.Integer((1,-1,1,0,0,0)[res(n,p,6)])
    if g==5:return s.Integer(int(res(n,p,4)==0))
    return s.Integer((1,-1,0,0,0)[res(n,p,5)])
def asdict(expr):
    return {tuple(e):Fraction(int(v.p),int(v.q))
            for e,v in s.Poly(s.expand(expr),*variables).terms() if v}
def polynomial(g,p):
    H=lambda n:h(n,g,p)
    determinant=H(a+c)*(H(a)*H(x)-H(a+1)*H(x-1))-H(a+c+1)*(H(a-1)*H(x)-H(a+1)*H(x-2))+H(a+c+2)*(H(a-1)*H(x-1)-H(a)*H(x-2))
    if g in (1,4,5):determinant*=(-1)**res(a,p,2)
    HW=lambda n:H(n)-H(n-1)
    fiber=HW(a)*HW(b)-HW(a+1)*HW(b-1)
    fixed=(5,3,1,2,0,1,0)[g]
    correction=60*(x+1) if g==0 else 6*(-1)**res(b,p,2)*int(res(x,p,2)==0) if g==1 else 0
    return asdict(determinant-fixed*H(k-1)*fiber+correction)
identity=polynomial(0,(0,0,0))
compact=(x+1)*(B+x+3)*(B+2)*((2*K+14)*(B+2*K+16)*(B+x+2*K+17)-5*(K+8)*(K+9)*(K+10))/12+60*(x+1)
assert identity==asdict(compact)
assert all(v>0 for v in identity.values())
downset=set()
for e in identity:downset.update(product(*(range(q+1) for q in e)))
assert len(downset)==55
phases={}
for g,m,deg in ((1,2,3),(2,2,2),(3,3,1)):
    phases[g]=[polynomial(g,p) for p in product(range(m),repeat=3)]
    assert max((sum(e) for poly in phases[g] for e in poly),default=-1)<=deg
    print("phases",g,len(phases[g]),flush=True)
# The signs in classes32,4 have period dividing6,4 respectively, including a.
periodic={}
for g,m in ((4,6),(5,4),(6,5)):
    values=[]
    for p in product(range(m),repeat=3):
        poly=polynomial(g,p)
        assert all(e==(0,0,0) for e in poly)
        values.append(poly.get((0,0,0),Fraction(0)))
    periodic[g]=max(map(abs,values))
    print("periodic maximum",g,periodic[g],flush=True)
stirling=[[0]*7 for _ in range(7)];stirling[0][0]=1
for n in range(1,7):
    for r in range(1,n+1):stirling[n][r]=stirling[n-1][r-1]+r*stirling[n-1][r]
def difference(poly,order):
    out={}
    for exponent,value in poly.items():
        choices=[]
        for power,number in zip(exponent,order):
            if power<number:break
            if number==0:choices.append([(power,1)])
            else:choices.append([(power-j,comb(power,j)*60**j*factorial(number)*stirling[j][number]) for j in range(number,power+1)])
        else:
            for terms in product(*choices):
                e=tuple(q[0] for q in terms);v=value
                for _,factor in terms:v*=factor
                out[e]=out.get(e,Fraction(0))+v
    return {e:v for e,v in out.items() if v}
checks=[];failures=[]
for order in sorted(downset):
    dom=difference(identity,order);subtract={}
    for g,weight in ((1,10),(2,15),(3,20)):
        maxima={}
        for poly in phases[g]:
            for e,v in difference(poly,order).items():maxima[e]=max(maxima.get(e,Fraction(0)),abs(v))
        for e,v in maxima.items():subtract[e]=subtract.get(e,Fraction(0))+weight*v
    if order==(0,0,0):
        subtract[(0,0,0)]=subtract.get((0,0,0),Fraction(0))+20*periodic[4]+30*periodic[5]+24*periodic[6]
    margins={e:dom.get(e,Fraction(0))-subtract.get(e,Fraction(0)) for e in set(dom)|set(subtract)}
    minimum=min(margins.values(),default=Fraction(0))
    constant=margins.get((0,0,0),Fraction(0))
    ok=minimum>=0 and constant>0
    record=dict(order=order,pass_bound=ok,constant=str(constant),minimum=str(minimum),
                margins={str(e):str(v) for e,v in sorted(margins.items())})
    checks.append(record)
    if not ok:failures.append(order)
receipt=dict(statement="T048 independent ambient-Schur coefficient domination",
    identity_positive_terms=len(identity),active_orders=len(downset),
    failures=failures,checks=checks,periodic_bounds={str(g):str(v) for g,v in periodic.items()},
    identity={str(e):str(v) for e,v in sorted(identity.items())},
    phases={str(g):[{str(e):str(v) for e,v in sorted(poly.items())} for poly in pp] for g,pp in phases.items()})
(HERE/"THREE_DEFECT_DOMINATION_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(dict(failures=failures,minimum_constant=min(Fraction(row["constant"]) for row in checks)),default=str),flush=True)

