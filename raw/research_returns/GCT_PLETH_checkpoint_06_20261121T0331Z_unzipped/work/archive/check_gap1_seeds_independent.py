"""G028: independent JT reconstruction of every minimal strict seed and increment."""
from pathlib import Path
from itertools import product
from math import comb
from fractions import Fraction
import json,hashlib,sys
import check_gap2_seeds_independent as jt

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent/"root"
sys.path.insert(0,str(ROOT))
from five_row_cycle_trace import cycle_trace
CLASSES=jt.CLASSES;LABELS=jt.LABELS
before=dict(jt.counts)
seedfile=ROOT/"FIVE_ROW_GAP1_EXPLORATION.json"
monoidfile=ROOT/"FIVE_ROW_GAP1_MONOID_EXPLORATION.json"
target=json.loads(seedfile.read_text())
expected={(tuple(row["parity"]),tuple(row["increment"])):row for row in target}
monoid=json.loads(monoidfile.read_text())

def weights(u):return sum((i+1)*v for i,v in enumerate(u))
def values(gaps):
    lam=tuple(sum(gaps[i:]) for i in range(4))
    assert sum(lam)%5==0
    n=sum(lam)//5
    traces=tuple(jt.trace(lam,n,cycle) for cycle in CLASSES)
    assert traces==tuple(cycle_trace(lam,n,cycle) for cycle in CLASSES)
    out=[]
    for label in LABELS:
        value=sum(Fraction(jt.character(label,cyc)*v,jt.z(cyc)) for cyc,v in zip(CLASSES,traces))
        assert value.denominator==1 and value>=0
        out.append(int(value))
    return lam,n,traces,tuple(out)

seeds=[]
for parity in product(range(2),repeat=4):
    base=tuple(1+p for p in parity)
    for u in jt.compositions_at_most(4,4):
        if (weights(base)+2*weights(u))%5:continue
        if any((weights(base)+2*weights(v))%5==0
               for v in product(*(range(q+1) for q in u)) if v!=u):continue
        gaps=tuple(a+2*b for a,b in zip(base,u))
        lam,n,traces,mults=values(gaps)
        row=expected[(parity,u)]
        assert gaps==tuple(row["gaps"]) and mults==tuple(row["multiplicities"])
        seeds.append(dict(parity=parity,increment=u,gaps=gaps,partition=lam+(0,),inner=n,
                          traces=traces,multiplicities=mults))
assert len(seeds)==len(expected)==76
bad=[row for row in seeds if min(row["multiplicities"])==0]
assert len(bad)==5
assert all(all(v>0 for v in row["multiplicities"][1:-1]) for row in seeds)

generators=[]
for u in jt.compositions_at_most(5,4):
    if not any(u) or weights(u)%5:continue
    if any(any(v) and v!=u and weights(v)%5==0
           for v in product(*(range(q+1) for q in u))):continue
    generators.append(u)
assert len(generators)==14
assert set(generators)==set(map(tuple,monoid["generators"]))
expected_bad={tuple(row["seed"]["gaps"]):row["failures"] for row in monoid["rows"]}
increments=[]
for seed in bad:
    failures=[]
    for u in generators:
        gaps=tuple(a+2*b for a,b in zip(seed["gaps"],u))
        lam,n,traces,mults=values(gaps)
        increments.append(dict(seed=seed["gaps"],increment=u,gaps=gaps,partition=lam+(0,),
                               inner=n,traces=traces,multiplicities=mults))
        if min(mults)==0:failures.append((u,gaps,mults))
    anticipated={(tuple(row["increment"]),tuple(row["gaps"]),tuple(row["multiplicities"]))
                 for row in expected_bad[seed["gaps"]]}
    assert set(failures)==anticipated
assert len(increments)==70
assert sum(min(row["multiplicities"])==0 for row in increments)==4

# Exact stabilized module sign tensor S_(3,2,1)(h5), using literal JT.
def h(g,n):
    if n<0:return 0
    if g==0:return comb(n+3,3)
    if g==1:return (n//2+1)*((n+1)//2+1)
    if g==2:return n//2+1 if n%2==0 else 0
    if g==3:return n//3+1
    if g==4:return (1,-1,1,0,0,0)[n%6]
    if g==5:return int(n%4==0)
    return (1,-1,0,0,0)[n%5]
ray=[]
for g,cycle in enumerate(CLASSES):
    H=lambda n:h(g,n)
    ray.append((-1)**(5-len(cycle))*jt.determinant([[H(3),H(4),H(5)],
                                                 [H(1),H(2),H(3)],
                                                 [H(-1),H(0),H(1)]]))
ray_mult=[]
for label in LABELS:
    value=sum(Fraction(jt.character(label,cyc)*v,jt.z(cyc)) for cyc,v in zip(CLASSES,ray))
    assert value.denominator==1
    ray_mult.append(int(value))
assert ray[0]==64 and ray_mult==[0,2,3,3,3,2,0]

receipt=dict(statement="G028 independent complete strict-seed and generator checks",status="PASS",
    seeds=76,all_positive_seeds=71,bad_seeds=bad,minimal_zero_sum_generators=generators,
    seed_increment_cases=70,exceptional_increment_cases=[r for r in increments if min(r["multiplicities"])==0],
    class_trace_checks=7*(76+70),irreducible_multiplicities_checked=7*(76+70),
    new_base_computations={key:jt.counts[key]-before[key] for key in before},
    stabilized_ray_dimension=ray[0],stabilized_ray_traces=ray,stabilized_ray_multiplicities=ray_mult,
    all_seed_and_increment_values_sha256=hashlib.sha256(json.dumps([seeds,increments],sort_keys=True).encode()).hexdigest(),
    input_hashes={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (seedfile,monoidfile)},
    method="independent minimal-vector enumeration; literal integer single-cycle JT; two-cycle JT interpolation overF61 with proved signed bounds")
(HERE/"GAP1_SEEDS_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({key:value for key,value in receipt.items() if key not in ("bad_seeds","minimal_zero_sum_generators","exceptional_increment_cases")},indent=2))

