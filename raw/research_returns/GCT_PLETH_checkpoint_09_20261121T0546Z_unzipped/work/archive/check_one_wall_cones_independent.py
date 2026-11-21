"""G034 independent literal-normal reconstruction of both final cones.

No root or theta implementation is imported. Each phase polynomial is recovered
from an independently proved phase-degree simplex of full selected-subset Weyl
traces. Rational differences and residue cubes use unbounded integers.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb,lcm,prod
from pathlib import Path
import hashlib,json,time
import numpy as np
from check_variable_wall_independent import (CLASSES,CHARS,SIZES,PARTITIONS,
    simplex,binomial_basis,decode,encode,margins)
from check_one_twist_independent import SAFE_DEGREES,literal_trace as direct_trace

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/"root"
FILES={"A":("ONE_TWIST_TRIPLE_A_CHECK.json","ONE_TWIST_TRIPLE_A_RECEIPT.json"),
       "B":("ONE_TWIST_TRIPLE_B_CHECK.json","ONE_TWIST_TRIPLE_B_RECEIPT.json")}

def parameters(branch,point):
    X,Y,K=point
    if branch=="A":
        k=Y+7+K;x=Y+X;b=3*k-5-Y
    else:
        k=X+2*Y+9+K;x=X;b=3*k-5-(X+Y+1)
    assert min(k,x,b)>=0 and 2*b+x+3>=5*k
    return x,b,k


def reconstruct(branch,g,phase):
    period=lcm(*CLASSES[g]);degree=SAFE_DEGREES[g]
    points=simplex(degree)
    values={}
    for q in points:
        actual=tuple(phase[i]+period*q[i] for i in range(3))
        x,b,k=parameters(branch,actual)
        values[q]=direct_trace(g,b+x,b,k)
    polynomial=defaultdict(Fraction)
    for order in points:
        constant=0
        for q in product(*(range(i+1) for i in order)):
            multiplier=(-1)**(sum(order)-sum(q))
            for i,j in zip(order,q):multiplier*=comb(i,j)
            constant+=multiplier*values[q]
        if not constant:continue
        bases=[binomial_basis(phase[i],period,order[i]) for i in range(3)]
        for exponents in product(*(range(len(base)) for base in bases)):
            coefficient=Fraction(constant)
            for axis,e in enumerate(exponents):coefficient*=bases[axis][e]
            polynomial[exponents]+=coefficient
    return {p:c for p,c in polynomial.items() if c},len(points)

def cube(data,expected):
    coordinates=np.indices((60,60,60),dtype=np.int64).reshape(3,-1)
    powers=[[axis.astype(object)**i for i in range(6)] for axis in coordinates]
    traces=[]
    for g,phases in enumerate(data):
        period=lcm(*CLASSES[g])
        phase_ids=((coordinates[0]%period)*period+coordinates[1]%period)*period+coordinates[2]%period
        result=np.zeros(60**3,dtype=object)
        for phase,poly in phases.items():
            ids=np.flatnonzero(phase_ids==(phase[0]*period+phase[1])*period+phase[2])
            denominator=lcm(*(c.denominator for c in poly.values())) if poly else 1
            value=np.zeros(len(ids),dtype=object)
            for exponents,coefficient in poly.items():
                term=np.full(len(ids),coefficient.numerator*(denominator//coefficient.denominator),dtype=object)
                for axis,e in enumerate(exponents):term*=powers[axis][e][ids]
                value+=term
            assert not np.any(value%denominator)
            result[ids]=value//denominator
        traces.append(result)
    labels={}
    for mu,chi in zip(PARTITIONS,CHARS):
        label="".join(map(str,mu));reference=expected["label_arrays"][label]
        numerator=np.zeros(60**3,dtype=object)
        for size,c,trace in zip(SIZES,chi,traces):numerator+=size*c*trace
        assert not np.any(numerator%120)
        values=numerator//120
        low=int(values.min());high=int(values.max())
        assert 0<=low<=high<2**63
        zeros=[list(map(int,coordinates[:,i])) for i in np.flatnonzero(values==0)]
        digest=hashlib.sha256(np.ascontiguousarray(values,dtype="<i8").tobytes()).hexdigest()
        assert dict(min=low,max=high,sha256=digest)==reference,(label,low,high,digest,reference)
        assert zeros==expected["zero_parameters"][label]
        labels[label]={"min":low,"max":high,"sha256":digest,"zeros":zeros}
    return {"constants":1512000,"labels":labels,
            "zero_count":sum(len(v["zeros"]) for v in labels.values()),
            "maximum_absolute_traces":[int(np.max(np.abs(t))) for t in traces]}

def main():
    start=time.monotonic()
    results={}
    for branch,(polyfile,cubefile) in FILES.items():
        path=ROOT/polyfile;expected=json.loads(path.read_text())
        data=[];count=0;samples=0
        for g,cycles in enumerate(CLASSES):
            period=lcm(*cycles);phases={}
            for phase in product(range(period),repeat=3):
                poly,n=reconstruct(branch,g,phase)
                key=",".join(map(str,phase))
                assert poly==decode(expected["phase_polynomials"][g][key]),(branch,g,phase)
                phases[phase]=poly;count+=1;samples+=n
            data.append(phases)
            actual_degree=max(sum(e) for poly in phases.values() for e in poly)
            assert actual_degree==(5,2,1,1,0,0,0)[g]
            print("cone",branch,"class",cycles,"PASS",len(phases),"phases",flush=True)
        caps=(3,3,4) if branch=="A" else (3,2,4)
        assert all(all(e<=cap for e,cap in zip(power,caps)) and sum(power)<=5
                   for phases in data for poly in phases.values() for power in poly)
        margin_result=margins(data,expected)
        wanted=427680 if branch=="A" else 29700
        assert Fraction(margin_result["minimum_constant_margin"])==wanted
        assert margin_result["orders"]==(46 if branch=="A" else 33)
        print("cone",branch,"PASS",margin_result["orders"],"margins; minimum",wanted,flush=True)
        cube_result=cube(data,json.loads((ROOT/cubefile).read_text()))
        output=[{",".join(map(str,phase)):encode(poly) for phase,poly in phases.items()} for phases in data]
        (HERE/f"ONE_WALL_CONE_{branch}_POLYNOMIALS_INDEPENDENT.json").write_text(json.dumps(output,indent=2)+"\n")
        results[branch]={"parameter_map":expected["parameter_map"],"phase_polynomials":count,
                         "unisolvent_trace_values":samples,"separate_degree_caps":caps,
                         "margins":margin_result,"residue_cube":cube_result,
                         "input_polynomial_sha256":hashlib.sha256(path.read_bytes()).hexdigest(),
                         "input_cube_sha256":hashlib.sha256((ROOT/cubefile).read_bytes()).hexdigest()}
        print("cone",branch,"PASS1512000 constants;",cube_result["zero_count"],"zeros",flush=True)
    receipt={"statement":"G034 complete one-twist wall independent cone certificates","status":"PASS",
             "method":"full unexpanded rank-three normal-subset Weyl traces; safe-degree phase simplex; exact rational reconstruction; literal translation differences; unbounded Python-integer residue cubes",
             "safe_phase_degrees":SAFE_DEGREES,"cones":results,
             "total_phase_polynomials":898,"total_unisolvent_traces":3494,
             "total_residue_constants":3024000,"elapsed_seconds":time.monotonic()-start}
    (HERE/"ONE_WALL_CONES_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print("PASS both final cones;898 polynomials,79 margins,3024000 constants",flush=True)

if __name__=="__main__":
    main()

