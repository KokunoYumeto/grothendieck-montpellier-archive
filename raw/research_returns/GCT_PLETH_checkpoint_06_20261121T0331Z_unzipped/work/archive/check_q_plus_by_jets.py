"""Independent T040 finite certificate from equivariant point jets."""
from pathlib import Path
from math import comb
import json,hashlib
import sympy as s
HERE=Path(__file__).resolve().parent
target_path=HERE.parent/"theta"/"outer5"/"Q_PLUS_NEWTON_TABLE.json"
classes=[(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,)]
sizes=[1,10,15,20,20,30,24]
labels=["5","4,1","3,2","3,1,1","2,2,1","2,1,1,1","1,1,1,1,1"]
chars=[[1,1,1,1,1,1,1],[4,2,0,1,-1,0,-1],[5,1,1,-1,1,-1,0],
       [6,0,-2,0,0,0,1],[5,-1,1,-1,-1,1,0],[4,-2,0,1,1,0,-1],
       [1,-1,1,1,-1,-1,1]]
x,t=s.symbols("x t")
expected=[(15-5*t-t*t)/(1-t)**4,(3-t-t*t)/((1-t)**3*(1+t)),
          -(1+t+t*t)/(1-t*t)**2,t/(1-t**3),-t/(1-t**3),
          -(1-t+t*t)/(1-t**4),-t*t*(1-t)/(1-t**5)]
def even_poly(poly):
    ans=0
    for j,c in s.Poly(poly,x).terms():
        assert j[0]%2==0
        ans+=c*t**(j[0]//2)
    return ans
def square_variable(expr):
    n,d=s.fraction(s.cancel(expr))
    return s.cancel(even_poly(n)/even_poly(d))
traces=[];degrees=[]
for cyc,expected_fun in zip(classes,expected):
    det=s.cancel(s.prod(1-x**l for l in cyc)/(1-x))
    dd=[int(s.Poly(det,x).nth(j)) for j in range(5)]
    h=[1]
    for k in range(1,480):
        h.append(-sum(dd[j]*h[k-j] for j in range(1,min(4,k)+1)))
    fixed=cyc.count(1);e=fixed-1
    trace=[e*h[2*k+1]-h[2*k]-fixed*(e-1)*(h[k-1] if k else 0)
           for k in range(240)]
    traces.append(trace)
    H=1/det
    even=square_variable((H+H.subs(x,-x))/2)
    odd=square_variable((H-H.subs(x,-x))/(2*x))
    exact=e*odd-even-fixed*(e-1)*t*H.subs(x,t)
    assert s.cancel(exact-expected_fun)==0
    num,den=s.fraction(s.cancel(exact*(1-t**60)**4))
    assert den==1 and s.Poly(num,t).degree()<=238
    degrees.append(int(s.Poly(num,t).degree()))

target=json.loads(target_path.read_text())
assert target["period"]==60 and target["max_polynomial_degree"]==3
count=0;zero_sets={};largest=0
for li,label in enumerate(labels):
    values=[]
    for k in range(240):
        numerator=sum(size*char*trace[k] for size,char,trace in zip(sizes,chars[li],traces))
        assert numerator%120==0
        values.append(numerator//120)
    zero_sets[label]=[k for k in range(60) if values[k]==0]
    f,a,b=chars[li][:3]
    for r in range(60):
        actual=[sum((-1)**(i-j)*comb(i,j)*values[r+60*j] for j in range(i+1))
                for i in range(4)]
        assert actual==target["labels"][label][r]
        assert all(v>=0 for v in actual)
        numerator=f*(9*r*r+590*r+12352)+a*(10*r+350)-b*(30 if r%2==0 else 15)
        assert numerator%4==0
        closed=[values[r],numerator//4,f*(270*r+16950)+150*a,16200*f]
        assert closed==actual
        assert min(actual[1:])>0
        largest=max(largest,*actual);count+=4
assert count==1680 and largest==197280
assert zero_sets=={"5":[0],"4,1":[],"3,2":[],"3,1,1":[],
                  "2,2,1":[0],"2,1,1,1":[0],"1,1,1,1,1":[0,1,2]}

A,B,C,D,V=s.symbols("A B C D V")
T=s.Matrix([A,B,C,D,V])
F=A*D*(V-B-C)-B*C*(V-A-D)
BB=s.Matrix([[0,0,D-V,V-C,C-D],[V-B,A-V,0,0,B-A],
             [0,D,0,-B,0],[-C,0,A,0,0]])
assert all(s.expand(v)==0 for v in BB*T)
for i in range(5):
    minor=BB[:,[j for j in range(5) if j!=i]].det()
    assert s.expand((-1)**i*minor+F*T[i])==0
assert s.expand(BB[[1,2,3],[0,1,2]].det()-A*D*(V-B))==0
receipt={"statement":"Independent T040 exact proof-data check","status":"PASS",
         "method":"Fixed-point-jet traces using E only; exact rational even/odd extraction; direct Newton differences.",
         "rational_characters":7,"common_numerator_degrees":degrees,
         "newton_constants":count,"largest_constant":largest,"zero_sets":zero_sets,
         "signed_maximal_minors":5,"rank_three_minor":"A*D*(V-B)",
         "target_sha256":hashlib.sha256(target_path.read_bytes()).hexdigest()}
(HERE/"Q_PLUS_JET_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
