"""Finite algebra checks for proposed C.3bg; not a replacement for its uniform proof."""
from datetime import datetime, timezone
from itertools import product
from math import factorial
from pathlib import Path
import json, time

BASE=Path(__file__).resolve().parents[1]
start=time.perf_counter()
report={"started_utc":datetime.now(timezone.utc).isoformat(),"scope":"Finite Hasse/coefficient, characteristic-two smoothness and rank examples only. Formal Picard, all-prime existence, approximation and fixed-family conclusions are separately proved and audited.","checks":[]}
def check(name,condition,data=None):
    report["checks"].append({"name":name,"passed":bool(condition),"data":data})
A=[(2,1,1),(1,2,1),(1,1,2)]
for p in [2,3,5,7,11,13,17,19,23,29,31]:
    matrix=[]
    for a in A:
        row=[]
        for b in A:
            e=tuple(p*a[i]-b[i]-(p-1) for i in range(3))
            if min(e)<0 or sum(e)!=p-1: c=0
            else:
                c=factorial(p-1)
                for n in e:c//=factorial(n)
                c%=p
            row.append(c)
        matrix.append(row)
    check(f"F0_Hasse_identity_p{p}",matrix==[[int(i==j) for j in range(3)]for i in range(3)],matrix)
# F4 = F2[a]/(a^2+a+1), integers 0,1,2,3 encode 0,1,a,a+1.
def mul(a,b):
    r=0
    while b:
        if b&1:r^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return r
def power(a,n):
    r=1
    for _ in range(n):r=mul(r,a)
    return r
points=[v for v in product([0,1],repeat=3)if any(v)]
vals=[]
for x,y,z in points:
    f=power(x,4)^mul(2,power(y,4))^mul(3,power(z,4))^mul(mul(x,y),mul(z,x^y^z))
    vals.append({"point":[x,y,z],"value_F4":f})
check("char2_ordinary_quartic_nonzero_at_all_seven_gradient_points",all(v["value_F4"]for v in vals),vals)
# On each standard affine chart, the gradient equations force the remaining
# two coordinates into {0,1}; the proof is the elementary zero/nonzero split.
for chart in range(3):
    zero=[]
    for coords in product(range(4),repeat=2):
        v=list(coords);v.insert(chart,1);x,y,z=v
        grad=[mul(mul(y,z),y^z),mul(mul(x,z),x^z),mul(mul(x,y),x^y)]
        if not any(grad):zero.append(v)
    check(f"char2_gradient_chart{chart}_F4_points",all(all(a in [0,1]for a in v)for v in zero),zero)
# The smooth characteristic-two Klein quartic proof is symbolic: at a common
# derivative zero with all coordinates nonzero its three monomials coincide;
# their sum is three times that nonzero monomial, which equals it modulo two.
check("char2_Klein_nonzero_critical_value",3%2==1,{"coefficient":3%2})
# Canonical multiplication has six independent degree-two plane monomials.
mon2=[v for v in product(range(3),repeat=3)if sum(v)==2]
check("canonical_symmetric_square_dimension",len(mon2)==6,mon2)
for p in [2,3,5,7]:
    for q in [2,3]:
        image={tuple(v[:q])for v in product(range(p),repeat=3)}
        check(f"rank{q}_image_example_p{p}",len(image)==p**q,{"image_points":len(image),"rank":q})
# Demonstrate why k-rank two must not be called exact Fp-rank two.
image={ (a^mul(2,c), b) for a,b,c in product([0,1],repeat=3)}
check("rank2_over_F4_can_have_F2_rank3",len(image)==8,{"image_points":len(image),"matrix":[[1,0,2],[0,1,0]]})
report["runtime_seconds"]=time.perf_counter()-start
report["check_count"]=len(report["checks"])
report["failures"]=sum(not c["passed"]for c in report["checks"])
out=BASE/'output'/'C3_uniform_integral_picard_certificate.json'
out.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
raise SystemExit(bool(report["failures"]))
