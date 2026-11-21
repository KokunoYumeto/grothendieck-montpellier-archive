"""Independent T054 phase reconstruction and complete residue/support audit.

Reconstructs each exact polynomial from unexpanded normal-subset Weyl traces
on a unisolvent simplex, using proved safe phase-degree bounds. No theta/root
Python implementation is imported. Finite differences use literal translations.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb,factorial,lcm
from pathlib import Path
import hashlib,json,time
import numpy as np
from check_third_power_fixed_twist_independent import CLASSES,CHARS,SIZES,PARTITIONS

HERE=Path(__file__).resolve().parent
THETA=HERE.parent/"theta"/"outer5"/"variable_wall"
ROOT=HERE.parent/"root"
SAFE_DEGREES=(5,3,3,2,0,2,0)

@lru_cache(None)
def h(cycles,n):
    if n<0:return 0
    if cycles==(1,1):return 1
    if cycles==(2,):return (-1)**n
    if cycles==(1,1,1):return n+1
    if cycles==(2,1):return int(n%2==0)
    if cycles==(3,):return (1,-1,0)[n%3]
    if cycles==(1,1,1,1):return (n+1)*(n+2)//2
    if cycles==(2,1,1):return n//2+1
    if cycles==(2,2):return (-1)**n*(n//2+1)
    if cycles==(3,1):return int(n%3==0)
    if cycles==(4,):return (1,-1,0,0)[n%4]
    if cycles==(1,1,1,1,1):return (n+1)*(n+2)*(n+3)//6
    if cycles==(2,1,1,1):return (n//2+1)*((n+1)//2+1)
    if cycles==(2,2,1):return n//2+1 if n%2==0 else 0
    if cycles==(3,1,1):return n//3+1
    if cycles==(3,2):return (1,-1,1,0,0,0)[n%6]
    if cycles==(4,1):return int(n%4==0)
    if cycles==(5,):return (1,-1,0,0,0)[n%5]
    raise AssertionError(cycles)

@lru_cache(None)
def selected_types(cycles):
    result=defaultdict(int)
    for flags in product((0,1),repeat=len(cycles)):
        selected=tuple(v for v,s in zip(cycles,flags) if s)
        if sum(selected)>3:continue
        rest=tuple(v for v,s in zip(cycles,flags) if not s)
        result[selected,rest]+=(-1)**len(selected)
    return tuple((selected,rest,count) for (selected,rest),count in result.items())

@lru_cache(None)
def normal(cycles,k):
    polynomial={(0,0):1}
    for length in cycles:
        next_poly=defaultdict(int)
        for old,value in polynomial.items():
            for total in range(k):
                for i in range(total+1):
                    next_poly[old[0]+length*i,old[1]+length*(total-i)]+=value
        polynomial=dict(next_poly)
    return tuple(polynomial.items())

@lru_cache(None)
def literal_trace(g,X,B,K):
    k=K+3;b=3*k-2+B;a=b+X
    value=0
    for selected,rest,orientation in selected_types(CLASSES[g]):
        for (p,q),coefficient in normal(selected,k):
            value+=orientation*coefficient*(h(rest,a-p)*h(rest,b-q)-h(rest,a+1-p)*h(rest,b-1-q))
    return value

def simplex(degree):
    return [(i,j,k) for i in range(degree+1) for j in range(degree-i+1)
            for k in range(degree-i-j+1)]

@lru_cache(None)
def binomial_basis(residue,period,degree):
    # binom((Z-residue)/period, degree), in ordinary Z powers.
    out=[Fraction(1)]
    for j in range(degree):
        next_poly=[Fraction(0)]*(len(out)+1)
        for i,c in enumerate(out):
            next_poly[i]-=c*(residue+period*j)
            next_poly[i+1]+=c
        out=next_poly
    denominator=period**degree*factorial(degree)
    return tuple(c/denominator for c in out)

def reconstruct(g,phase):
    period=lcm(*CLASSES[g]);ar,br,kr=phase
    rK=(kr-3)%period;rB=(br-3*rK-7)%period;rX=(ar-br)%period
    residue=(rX,rB,rK);degree=SAFE_DEGREES[g]
    points=simplex(degree)
    values={q:literal_trace(g,*(residue[i]+period*q[i] for i in range(3))) for q in points}
    polynomial=defaultdict(Fraction)
    for order in points:
        constant=0
        for q in product(*(range(j+1) for j in order)):
            factor=(-1)**(sum(order)-sum(q))
            for d,u in zip(order,q):factor*=comb(d,u)
            constant+=factor*values[q]
        if not constant:continue
        bases=[binomial_basis(residue[i],period,order[i]) for i in range(3)]
        for powers in product(*(range(len(base)) for base in bases)):
            coefficient=Fraction(constant)
            for i,p in enumerate(powers):coefficient*=bases[i][p]
            polynomial[powers]+=coefficient
    return {p:c for p,c in polynomial.items() if c},len(points)

def decode(raw):
    return {tuple(map(int,p.split(","))):Fraction(*c) for p,c in raw.items() if c[0]}

def encode(poly):
    return {",".join(map(str,p)):[c.numerator,c.denominator] for p,c in sorted(poly.items()) if c}

@lru_cache(None)
def one_difference(items,axis):
    out=defaultdict(Fraction)
    for powers,c in items:
        p=powers[axis]
        for q in range(p):
            target=list(powers);target[axis]=q
            out[tuple(target)]+=c*comb(p,q)*60**(p-q)
    return tuple(sorted((p,c) for p,c in out.items() if c))

def difference(poly,order):
    items=tuple(sorted(poly.items()))
    for axis,degree in enumerate(order):
        for _ in range(degree):items=one_difference(items,axis)
    return dict(items)

def margins(data,expected):
    identity=data[0][(0,0,0)]
    assert all(c>=0 for c in identity.values())
    records=[];active=[]
    for order in product(range(4),range(5),range(6)):
        if not 0<sum(order)<=5:continue
        ident=difference(identity,order)
        bounds=defaultdict(Fraction)
        for size,phases in zip(SIZES[1:],data[1:]):
            worst={}
            for poly in phases.values():
                for power,value in difference(poly,order).items():
                    worst[power]=max(worst.get(power,Fraction(0)),abs(value))
            for power,value in worst.items():bounds[power]+=size*value
        if not ident and not bounds:continue
        active.append(order)
        margin={p:ident.get(p,Fraction(0))-bounds.get(p,Fraction(0)) for p in set(ident)|set(bounds)}
        assert all(c>=0 for c in margin.values())
        assert margin.get((0,0,0),0)>0
        records.append((order,margin))
    assert [list(o) for o in active]==expected["active_orders"]
    table={tuple(row["order"]):row for row in expected["margins"]}
    for order,margin in records:
        assert {p:c for p,c in margin.items() if c}==decode(table[order]["margin"])
        assert Fraction(table[order]["constant_margin"])==margin[(0,0,0)]
    return {"orders":len(active),"minimum_constant_margin":str(min(m[(0,0,0)] for _,m in records)),
            "all_coefficientwise_margins":{",".join(map(str,o)):encode(m) for o,m in records}}

def residue_cube(data,expected):
    coordinates=np.indices((60,60,60),dtype=np.int64).reshape(3,-1)
    X,B,K=coordinates
    powers=[[axis.astype(object)**i for i in range(6)] for axis in coordinates]
    traces=[]
    for g,phases in enumerate(data):
        period=lcm(*CLASSES[g])
        denominator=lcm(*(c.denominator for poly in phases.values() for c in poly.values()))
        ar=(3*K+7+B+X)%period;br=(3*K+7+B)%period;kr=(K+3)%period
        phase_id=(ar*period+br)*period+kr
        result=np.zeros(X.size,dtype=object)
        for phase,poly in phases.items():
            ids=np.flatnonzero(phase_id==(phase[0]*period+phase[1])*period+phase[2])
            value=np.zeros(len(ids),dtype=object)
            for exponents,coefficient in poly.items():
                term=np.full(len(ids),coefficient.numerator*(denominator//coefficient.denominator),dtype=object)
                for axis,p in enumerate(exponents):term*=powers[axis][p][ids]
                value+=term
            assert not np.any(value%denominator)
            result[ids]=value//denominator
        assert int(np.max(np.abs(result)))==expected["class_bounds"][g]["maximum_absolute_trace"]
        traces.append(result)
    records=[]
    for mu,chi,reference in zip(PARTITIONS,CHARS,expected["labels"]):
        numerator=np.zeros(X.size,dtype=object)
        for size,c,trace in zip(SIZES,chi,traces):numerator+=size*c*trace
        assert not np.any(numerator%120)
        values=numerator//120
        assert int(values.min())>=0
        assert values[0]==0
        zero=[list(map(int,coordinates[:,i])) for i in np.flatnonzero(values==0) if i]
        assert zero==reference["zeros"]
        assert int(values.max())==reference["maximum"]
        assert int(values[1:].min())==reference["minimum_valid"]
        assert int(values.max())<2**63
        digest=hashlib.sha256(np.ascontiguousarray(values,dtype="<i8").tobytes()).hexdigest()
        assert digest==reference["sha256_le_int64"]
        records.append({"label":mu,"zeros":zero,"maximum":int(values.max()),"sha256":digest})
    assert sum(len(r["zeros"]) for r in records)==13
    return {"constants":1512000,"labels":records,"valid_zeros":13,"formal_origin_traces":[int(t[0]) for t in traces]}

def main():
    start=time.monotonic()
    source=THETA/"VARIABLE_WALL_POLYNOMIALS.json"
    expected=json.loads(source.read_text())
    enlarged=json.loads((ROOT/"VARIABLE_WALL_ENLARGEMENT_CHECK.json").read_text())
    data=[];samples=0;phases_count=0
    for g,cycles in enumerate(CLASSES):
        period=lcm(*cycles);phases={}
        for phase in product(range(period),repeat=3):
            poly,number=reconstruct(g,phase)
            key=",".join(map(str,phase))
            assert poly==decode(expected["phase_polynomials"][g][key]),(g,phase)
            assert poly==decode(enlarged["phase_polynomials"][g][key]),(g,phase,"root")
            phases[phase]=poly;samples+=number;phases_count+=1
        data.append(phases)
        degree=max((sum(p) for poly in phases.values() for p in poly),default=0)
        assert degree==expected["degrees"][g]
        print("class",cycles,"PASS",len(phases),"phase polynomials; degree",degree,flush=True)
    polynomial_output=[{",".join(map(str,phase)):encode(poly) for phase,poly in phases.items()} for phases in data]
    (HERE/"VARIABLE_WALL_POLYNOMIALS_INDEPENDENT.json").write_text(json.dumps(polynomial_output,indent=2)+"\n")
    margin_result=margins(data,expected)
    print("PASS",margin_result["orders"],"coefficientwise margins; minimum",margin_result["minimum_constant_margin"],flush=True)
    residue_result=residue_cube(data,json.loads((THETA/"VARIABLE_WALL_RESIDUE_RECEIPT.json").read_text()))
    receipt={"statement":"T054 enlarged variable-order chamber independent audit","status":"PASS",
             "method":"unexpanded rank-two normal-subset Weyl traces; unisolvent phase simplex with proved safe degree bounds; rational binomial-basis reconstruction; literal step60 translations; Python-integer residue cube",
             "safe_phase_degrees":SAFE_DEGREES,"phase_polynomials":phases_count,"unisolvent_trace_values":samples,
             "actual_degrees":expected["degrees"],"margin_result":margin_result,"residue_result":residue_result,
             "theta_polynomial_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
             "root_enlargement_sha256":hashlib.sha256((ROOT/"VARIABLE_WALL_ENLARGEMENT_CHECK.json").read_bytes()).hexdigest(),
             "elapsed_seconds":time.monotonic()-start}
    (HERE/"VARIABLE_WALL_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print("PASS",phases_count,"phase polynomials;",samples,"unisolvent traces;1512000 zeroth constants;13 valid zeros",flush=True)

if __name__=="__main__":
    main()

