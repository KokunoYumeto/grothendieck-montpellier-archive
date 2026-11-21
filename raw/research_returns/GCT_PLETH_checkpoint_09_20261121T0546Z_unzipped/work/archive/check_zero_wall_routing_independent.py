"""G033 independent full-wall routing and new-cone matrix checks."""
from pathlib import Path
from fractions import Fraction
from itertools import islice
from math import comb,prod,lcm
import sys,json
from check_zero_wall_cones_independent import direct_trace,parameters,CLASSES,CHARS,SIZES,PARTITIONS,decode

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/"root"
sys.path.insert(0,str(ROOT))
import zero_twist_all_positive as positive

def actual_values(x,b,k):
    traces=[direct_trace(g,b+x,b,k) for g in range(7)]
    values=[]
    for chi in CHARS:
        numerator=sum(s*c*t for s,c,t in zip(SIZES,chi,traces))
        assert numerator%120==0
        values.append(numerator//120)
    return values

cases=set()
for k in range(4):
    for b in sorted(set((0,k,2*k,(5*k+1)//2,3*k))):
        for offset in (0,1):
            cases.add((max(0,5*k-2*b)+offset,b,k))
for k in (4,7,8,12):
    bs={0,k-1,k,2*k-1,2*k,2*k+1,2*k+2,2*k+3,2*k+4,3*k-3,3*k-2,3*k}
    for b in bs:
        for offset in (0,1,3):
            cases.add((max(0,5*k-2*b)+offset,b,k))
counts=dict(parameter_cases=len(cases),class_traces=0,coefficients=0,partition_wrapper=0,
            complementary_wall=0,stable_extension=0,cone_coefficients=0,matrices=0,witnesses=0)
branches=set()
saved={}
for x,b,k in sorted(cases):
    values=actual_values(x,b,k);saved[x,b,k]=values;counts["class_traces"]+=7
    for d in (0,1):
        lam=(d+3*b+2*x-5*k,d+b+x,d+b+x,d+x,d)
        for index,mu in enumerate(PARTITIONS):
            effective=6-index if (d+b+x)%2 else index
            wanted=values[effective]
            branch,_=positive.route(x,b,k,d,mu);branches.add(branch)
            assert positive.coefficient(x,b,k,d,mu)==wanted,(x,b,k,d,mu,branch)
            counts["coefficients"]+=1
            assert positive.coefficient_partition(lam,mu)==wanted
            counts["partition_wrapper"]+=1
            if k==0:
                for extension in (1,4):
                    enlarged=(lam[0]+5*extension,)+lam[1:]
                    assert positive.coefficient_partition(enlarged,mu)==wanted
                    counts["stable_extension"]+=1
    if k in (0,4,8,12) and b in (0,k,2*k,3*k):
        for d in (0,1):
            lam=(d+3*b+2*x-5*k,d+b+x,d+b+x,d+x,d)
            H=lam[0];complement=tuple(H-v for v in reversed(lam))
            for index,mu in enumerate(PARTITIONS):
                effective=6-index if (d+b+x+H)%2 else index
                assert positive.coefficient_partition(complement,mu)==values[effective]
                counts["complementary_wall"]+=1
assert branches=={"bulk","first","second","third","one_below","two_below","three_below","upper","A","B"},branches

polys={}
for branch in ("A","B"):
    raw=json.loads((HERE/f"ZERO_WALL_CONE_{branch}_POLYNOMIALS_INDEPENDENT.json").read_text())
    polys[branch]=[{tuple(map(int,phase.split(","))):decode(p) for phase,p in row.items()} for row in raw]
def cone_values(branch,point):
    traces=[]
    for cycles,row in zip(CLASSES,polys[branch]):
        L=lcm(*cycles);poly=row[tuple(z%L for z in point)]
        value=sum(c*prod(z**e for z,e in zip(point,powers)) for powers,c in poly.items())
        assert value.denominator==1;traces.append(value.numerator)
    result=[]
    for chi in CHARS:
        numerator=sum(s*c*t for s,c,t in zip(SIZES,chi,traces))
        assert numerator%120==0;result.append(numerator//120)
    return result

for branch in ("A","B"):
    points=((0,0,1),(1,1,1),(61,62,63),(301,302,303)) if branch=="A" else ((0,0,0),(1,1,1),(61,62,63),(301,302,303))
    for point in points:
        x,b,k=parameters(branch,point)
        values=cone_values(branch,point)
        for d in (0,1):
            for index,mu in enumerate(PARTITIONS):
                effective=6-index if (d+b+x)%2 else index
                coefficient=positive.coefficient(x,b,k,d,mu)
                assert coefficient==values[effective]
                counts["cone_coefficients"]+=1
                label=PARTITIONS[effective]
                tags=positive.cone_tags(branch,label,point)
                packet=positive.polytopes(x,b,k,d,mu)
                assert packet["branch"]==branch
                matrix_by_order={tuple(m["order"]):m for m in packet["polytopes"]}
                total=0
                for tag in tags:
                    if not tag["constant"]:continue
                    matrix=matrix_by_order[tuple(tag["order"])]
                    assert len(matrix["variables"])<=9
                    total+=tag["constant"]*prod(comb(q,j) if q>=j else 0 for q,j in zip(tag["quotient"],tag["order"]))
                    counts["matrices"]+=1
                    for witness in islice(positive.upper.witnesses(tag),2):
                        assert len(witness)==len(matrix["variables"])
                        assert all(lo<=z<=hi for lo,z,hi in zip(matrix["lower_bounds"],witness,matrix["upper_bounds"]))
                        assert all(sum(a*z for a,z in zip(row,witness))==rhs for row,rhs in zip(matrix["A_eq"],matrix["b_eq"]))
                        assert all(sum(a*z for a,z in zip(row,witness))>=rhs for row,rhs in zip(matrix["A_ge"],matrix["b_ge"]))
                        counts["witnesses"]+=1
                assert total==coefficient
for lam in ((1,)*10,(2,)*5+(1,)*5):
    for mu in PARTITIONS:assert positive.coefficient_partition(lam,mu)==0

out=dict(statement="G033 independent exhaustive-routing sample and literal new-cone evaluator audit",
         status="PASS",branches=sorted(branches),both_determinant_parities=True,
         greater_than_five_row_zeros=14,**counts)
(HERE/"ZERO_WALL_ROUTING_EVALUATOR_RECEIPT.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))

