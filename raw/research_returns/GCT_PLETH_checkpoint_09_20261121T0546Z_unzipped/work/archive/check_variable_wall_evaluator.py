"""T054 literal printed tables, Newton continuation and matrix/witness audit."""
from pathlib import Path
from fractions import Fraction
from itertools import islice
from math import prod,comb,lcm
import sys,json,re
from check_variable_wall_independent import decode,CLASSES,CHARS,SIZES,PARTITIONS
HERE=Path(__file__).resolve().parent
THETA=HERE.parent/"theta"/"outer5"/"variable_wall"
sys.path.insert(0,str(THETA))
import positive_wall_chamber as positive
data=json.loads((HERE/"VARIABLE_WALL_POLYNOMIALS_INDEPENDENT.json").read_text())
polys=[{tuple(map(int,phase.split(","))):decode(raw) for phase,raw in row.items()} for row in data]
receipt=json.loads((HERE/"VARIABLE_WALL_INDEPENDENT_RECEIPT.json").read_text())
report=(THETA/"variable_wall_report.md").read_text()

identity=polys[0][(0,0,0)]
identity_rows=0
part=report.split("The identity polynomial")[1].split("## 4.")[0]
for line in part.splitlines():
    match=re.match(r"\| \((\d+),(\d+)\) \| (.*?) \|",line)
    if not match:continue
    i,j=map(int,match.group(1,2))
    expression=match.group(3).replace("\\(","").replace("\\)","").replace(" ","")
    coeffs={}
    for term in expression.split("+"):
        if "K" not in term:degree=0;coefficient=int(term)
        else:
            before,after=term.split("K")
            coefficient=int(before) if before else 1
            degree=int(after[1:]) if after else 1
        coeffs[degree]=coefficient
    wanted={p[2]:int(12*c) for p,c in identity.items() if p[:2]==(i,j)}
    assert coeffs==wanted,(i,j,coeffs,wanted)
    identity_rows+=1
assert identity_rows==17

margin_rows=0
part=report.split("All coefficients of these nineteen")[1].split("For the other26")[0]
for line in part.splitlines():
    match=re.match(r"\| \((\d+),(\d+),(\d+)\) \| (\d+) \| (\d+) \|",line)
    if not match:continue
    order=tuple(map(int,match.group(1,2,3)))
    margin=decode(receipt["margin_result"]["all_coefficientwise_margins"][",".join(map(str,order))])
    assert margin[(0,0,0)]==int(match.group(4))
    assert min(margin.values())==int(match.group(5))
    margin_rows+=1
assert margin_rows==19

printed_zeros={}
part=report.split("The complete fixed\nresidue enumeration")[1].split("Every other valid")[0]
for line in part.splitlines():
    if not line.startswith("| \\(("):continue
    left,right=[c.strip() for c in line.strip("|").split("|")]
    label=(1,1,1,1,1) if "1^5" in left else tuple(map(int,re.findall(r"\d",left)))
    printed_zeros[label]=[list(map(int,t)) for t in re.findall(r"\((\d+),(\d+),(\d+)\)",right)]
for record in receipt["residue_result"]["labels"]:
    assert printed_zeros[tuple(record["label"])]==record["zeros"]

def independent(parameters):
    X,B,K=parameters;a=3*K+7+B+X;b=3*K+7+B;k=K+3
    traces=[]
    for cycles,row in zip(CLASSES,polys):
        period=lcm(*cycles)
        value=sum(c*prod(z**p for z,p in zip(parameters,powers))
                  for powers,c in row[a%period,b%period,k%period].items())
        assert value.denominator==1;traces.append(value.numerator)
    values=[]
    for chi in CHARS:
        numerator=sum(s*c*t for s,c,t in zip(SIZES,chi,traces))
        assert numerator%120==0;values.append(numerator//120)
    return values

cases=((0,0,1),(1,0,0),(0,1,0),(1,1,0),(2,0,0),
       (61,2,1),(2,61,1),(2,1,61),(63,64,65),(301,302,303))
counts=dict(coefficients=0,matrices=0,witnesses=0)
for parameters in cases:
    X,B,K=parameters;k=K+3;b=3*k-2+B;x=X
    values=independent(parameters)
    for d in (0,1):
        for index,mu in enumerate(PARTITIONS):
            effective=6-index if (d+b+x)%2 else index
            got=positive.coefficient(x,b,k,d,mu)
            assert got==values[effective],(parameters,d,mu,got,values[effective])
            counts["coefficients"]+=1
            tags=positive.tags(x,b,k,d,mu)
            assert len(tags)==46
            recovered=0
            for tag in tags:
                if not tag["constant"]:continue
                matrix=positive.constraints(tag)
                assert len(matrix["variables"])<=9
                term=tag["constant"]*prod(comb(q,j) if q>=j else 0 for q,j in zip(tag["quotient"],tag["order"]))
                recovered+=term
                counts["matrices"]+=1
                for witness in islice(positive.witnesses(tag),3):
                    assert len(witness)==len(matrix["variables"])
                    assert all(lo<=v<=hi for lo,v,hi in zip(matrix["lower_bounds"],witness,matrix["upper_bounds"]))
                    assert all(sum(a*z for a,z in zip(row,witness))==rhs for row,rhs in zip(matrix["A_eq"],matrix["b_eq"]))
                    assert all(sum(a*z for a,z in zip(row,witness))>=rhs for row,rhs in zip(matrix["A_ge"],matrix["b_ge"]))
                    counts["witnesses"]+=1
            assert recovered==got
try:
    positive.tags(0,7,3,0,(5,))
except ValueError:
    pass
else:
    raise AssertionError("invalid origin accepted")
out=dict(statement="T054 printed tables and actual positive evaluator audit",status="PASS",
         identity_rows=identity_rows,margin_rows=margin_rows,support_labels=7,
         parameter_cases=len(cases),both_determinant_parities=True,invalid_origin_rejected=True,**counts)
(HERE/"VARIABLE_WALL_EVALUATOR_RECEIPT.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

