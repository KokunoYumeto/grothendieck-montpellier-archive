"""Reconstruct all T048 positive-b Newton constants from ambient phase polynomials."""
from pathlib import Path
from itertools import product
from fractions import Fraction
import ast,json,hashlib,sys
import numpy as np
from check_three_defect_domination import identity,phases,difference,polynomial

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"rectangular"))
from verify_rectangular import character,z
LABELS=((5,),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1))
CLASSES=((1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(3,2),(4,1),(5,))
WEIGHTS=tuple(tuple((120//z(cyc))*character(label,cyc) for cyc in CLASSES) for label in LABELS)
TARGET=HERE.parent/"theta"/"outer5"/"TWO_ROW_THREE_DEFECT_SUMMARY.json"
target=json.loads(TARGET.read_text())

def integer_poly(poly):
    output={}
    for exponent,coefficient in poly.items():
        value=24*coefficient
        assert value.denominator==1
        output[exponent]=int(value)
    return output

def evaluate(poly,axes):
    a=[np.array(v,dtype=np.int64) for v in axes]
    out=np.zeros(tuple(map(len,axes)),dtype=np.int64)
    powers=[[v**j for j in range(7)] for v in a]
    bound=sum(abs(coefficient)*59**sum(exponent) for exponent,coefficient in poly.items())
    assert bound<2**63
    for (i,j,k),coefficient in poly.items():
        out+=coefficient*powers[0][i][:,None,None]*powers[1][j][None,:,None]*powers[2][k][None,None,:]
    return out,bound

periodic={}
for g,m in ((4,6),(5,4),(6,5)):
    small=np.zeros((m,m,m),dtype=np.int64)
    for phase in product(range(m),repeat=3):
        poly=polynomial(g,phase)
        assert all(exponent==(0,0,0) for exponent in poly)
        value=24*poly.get((0,0,0),Fraction(0));assert value.denominator==1
        small[phase]=int(value)
    periodic[g]=np.tile(small,(60//m,60//m,60//m))

keys=[",".join(map(str,label)) for label in LABELS]
hashes={key:hashlib.sha256() for key in keys}
total=0;zero_orders=[];zero_sets={};bounds=[];minimum=None;maximum=0
for order in product(range(4),range(5),range(4)):
    arrays=[];classbounds=[]
    array,bound=evaluate(integer_poly(difference(identity,order)),(range(60),)*3)
    arrays.append(array);classbounds.append(bound)
    for g,m in ((1,2),(2,2),(3,3)):
        array=np.zeros((60,60,60),dtype=np.int64);maxbound=0
        for phase,poly in zip(product(range(m),repeat=3),phases[g]):
            value,bound=evaluate(integer_poly(difference(poly,order)),
                                 tuple(range(p,60,m) for p in phase))
            array[phase[0]::m,phase[1]::m,phase[2]::m]=value
            maxbound=max(maxbound,bound)
        arrays.append(array);classbounds.append(maxbound)
    for g in (4,5,6):
        array=periodic[g] if order==(0,0,0) else np.zeros((60,60,60),dtype=np.int64)
        arrays.append(array);classbounds.append(int(np.abs(array).max()))
    worst=max(sum(abs(weight)*bound for weight,bound in zip(row,classbounds)) for row in WEIGHTS)
    assert worst<2**63
    bounds.append(worst)
    slot=",".join(map(str,order));allzero=True
    for key,row in zip(keys,WEIGHTS):
        values=sum(weight*array for weight,array in zip(row,arrays))
        assert np.all(values%2880==0)
        values//=2880
        low=int(values.min());high=int(values.max())
        assert low==target["minima"][key][slot],(key,order,"minimum",low,target["minima"][key][slot])
        assert high==target["maxima"][key][slot]
        assert low>=0
        if high:allzero=False
        if order!=(0,0,0) and high:
            assert low>0
            minimum=low if minimum is None else min(minimum,low)
        maximum=max(maximum,high)
        hashes[key].update(values.astype("<i8",copy=False).tobytes(order="C"))
        total+=values.size
        if order==(0,0,0):
            zeros=np.argwhere(values==0).tolist();assert not zeros
            zero_sets[key]=zeros
    if allzero:zero_orders.append(list(order))
    if order[1:]==(0,0):print("independent x order",order[0],"entries",total,flush=True)
actual_hashes={key:value.hexdigest() for key,value in hashes.items()}
assert actual_hashes==target["table_sha256"]
assert zero_orders==target["identically_zero_orders"]
assert total==120960000
receipt=dict(statement="T048 positive-b independent complete constant reconstruction",status="PASS",
    verified_entries=total,minimum_positive_order=minimum,maximum=maximum,
    identically_zero_orders=zero_orders,zero_residue_triples=zero_sets,
    table_sha256=actual_hashes,signed64_intermediate_bound=max(bounds),
    method="ambient3x3 Jacobi-Trudi minus actual jets plus literal defect correction; symbolic phases; direct Stirling differences",
    target_sha256=hashlib.sha256(TARGET.read_bytes()).hexdigest())
(HERE/"THREE_DEFECT_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({k:v for k,v in receipt.items() if k not in ("table_sha256","zero_residue_triples","identically_zero_orders")},indent=2))

