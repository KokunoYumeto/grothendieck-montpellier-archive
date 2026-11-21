"""G029 independent seed, monoid and full support-graph reconstruction."""
from pathlib import Path
from itertools import product
from collections import deque,defaultdict
from fractions import Fraction
from functools import lru_cache
import json,hashlib
HERE=Path(__file__).resolve().parent
scope={"__file__":str(HERE/"check_gap2_seeds_independent.py")}
text=(HERE/"check_gap2_seeds_independent.py").read_text()
exec(compile(text.split("target=json.loads")[0],scope["__file__"],"exec"),scope)
parts=scope["partitions"];z=scope["z"];character=scope["character"]
trace=scope["trace"];det=scope["determinant"]
classes=scope["CLASSES"];labels=scope["LABELS"]
compositions=scope["compositions_at_most"]
path=HERE.parent/"root/THREE_ROW_SUPPORT_GRAPH.json"
target=json.loads(path.read_text())
weight=lambda x:sum((i+1)*v for i,v in enumerate(x))

def canonical(g):
    a,b,c,_=g
    threshold=3*b+2*c
    return ((a-10*((a-threshold)//10),b,c,0) if a>=threshold else tuple(g))

computed={}
@lru_cache(None)
def values(g):
    lam=tuple(sum(g[i:]) for i in range(4));n=sum(lam)//5
    assert sum(lam)==5*n and n<=13
    tr=tuple(trace(lam,n,cyc) for cyc in classes)
    mult=tuple(sum(Fraction(character(mu,cyc)*q,z(cyc))
                   for cyc,q in zip(classes,tr)) for mu in labels)
    assert all(x.denominator==1 and x>=0 for x in mult)
    mult=tuple(map(int,mult))
    computed[g]=dict(inner=n,traces=tr,multiplicities=mult)
    return mult

expected_seeds={(tuple(s["parity"]),tuple(s["increment"])):s for s in target["initial_seeds"]}
seeds=[]
for parity in product((0,1),repeat=3):
    base=tuple(1+p for p in parity)
    for u in compositions(4,3):
        if (weight(base)+2*weight(u))%5:continue
        if any((weight(base)+2*weight(v))%5==0
               for v in product(*(range(q+1) for q in u)) if v!=u):continue
        g=tuple(a+2*b for a,b in zip(base,u))+(0,)
        row=expected_seeds[(parity,u+(0,))]
        assert g==tuple(row["gaps"])
        assert values(g)==tuple(row["multiplicities"])
        assert computed[g]["traces"]==tuple(row["traces"])
        seeds.append(g)
assert len(seeds)==len(expected_seeds)==30

generators=[]
for u in compositions(5,3):
    if not any(u) or weight(u)%5:continue
    if any(any(v) and v!=u and weight(v)%5==0
           for v in product(*(range(q+1) for q in u))):continue
    generators.append(u+(0,))
assert len(generators)==8 and set(generators)==set(map(tuple,target["generators"]))

expected_edges={(tuple(r["source"]),tuple(r["generator"])):r for r in target["edges"]}
queue=deque(canonical(g) for g in seeds if not all(values(g)))
seen={};edges=[]
while queue:
    g=queue.popleft()
    if g in seen:continue
    value=values(g)
    assert min(value)==0
    seen[g]=value
    for u in generators:
        raw=tuple(x+2*y for x,y in zip(g,u))
        norm=canonical(raw)
        actual=values(raw);normalized=values(norm)
        assert actual==normalized
        assert computed[raw]["traces"]==computed[norm]["traces"]
        row=expected_edges[g,u]
        assert raw==tuple(row["raw_target"]) and norm==tuple(row["target"])
        assert actual==tuple(row["multiplicities"])
        assert computed[norm]["traces"]==tuple(row["traces"])
        assert bool(min(actual)>0)==row["all_positive"]
        edges.append((g,u,raw,norm,actual))
        if not all(actual):queue.append(norm)
assert len(seen)==24 and len(edges)==len(expected_edges)==192
assert seen=={tuple(r["gaps"]):tuple(r["multiplicities"]) for r in target["nodes"]}
assert all(computed[tuple(r["gaps"])]["traces"]==tuple(r["traces"]) for r in target["nodes"])

@lru_cache(None)
def standard_h(cyc,n):
    if n<0:return 0
    q=[1]+[0]*n
    for c in cyc:
        for i in range(c,n+1):q[i]+=q[i-c]
    return q[n]-(q[n-1] if n else 0)

ray_groups=defaultdict(list)
for g,v in seen.items():
    a,b,c,_=g
    if a<3*b+2*c:continue
    alpha=(b+c,b+c,b)
    tr=tuple((-1)**((5-len(cyc))*(b+c))*
             det([[standard_h(cyc,alpha[i]-i+j) for j in range(3)] for i in range(3)])
             for cyc in classes)
    assert tr==computed[g]["traces"]
    plusfive=(a+5,b,c,0)
    assert values(plusfive)==v
    ray_groups[b,c].append((a,v))
assert len(ray_groups)==6 and sum(map(len,ray_groups.values()))==12
rays=[]
for (b,c),rows in sorted(ray_groups.items()):
    rows=sorted(rows)
    assert len(rows)==2 and rows[1][0]-rows[0][0]==5 and rows[0][1]==rows[1][1]
    a0=3*b+2*c+(-2*b-3*c-(3*b+2*c))%5
    assert rows[0][0]==a0
    rays.append(dict(first_gap=a0,second_gap=b,third_gap=c,step=5,multiplicities=rows[0][1]))
finite=[dict(gaps=g,multiplicities=v) for g,v in sorted(seen.items()) if g[0]<3*g[1]+2*g[2]]
assert len(finite)==12
receipt=dict(statement="G029 complete three-row face support graph",status="PASS",
 independent_minimal_seeds=30,independent_monoid_generators=8,
 deficient_nodes=24,edge_cases=192,
 seed_and_normalized_edge_multiplicity_comparisons=7*(30+192),
 raw_normalized_edge_class_trace_comparisons=7*192,
 distinct_gap_vectors_computed=len(computed),
 distinct_class_traces_computed=7*len(computed),
 maximum_inner_degree=max(r["inner"] for r in computed.values()),
 stable_fixed_Schur_character_checks=12*7,
 finite_exceptions=finite,stable_step_five_rays=rays,
 base_computations=scope["counts"],
 input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
 values_sha256=hashlib.sha256(json.dumps(sorted(computed.items()),separators=(",",":")).encode()).hexdigest(),
 method="independent parity-minimal and zero-sum enumeration; integer JT and exact F61 interpolation; BFS with direct raw/normalized equality checks; literal fixed-Schur ray determinants",
 scope="The finite graph data are independently verified. Exhaustion uses the actual G024 injections and G027 k0 isomorphisms, reviewed separately.")
(HERE/"THREE_ROW_SUPPORT_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps({k:v for k,v in receipt.items() if k not in ("finite_exceptions","stable_step_five_rays")},indent=2))
