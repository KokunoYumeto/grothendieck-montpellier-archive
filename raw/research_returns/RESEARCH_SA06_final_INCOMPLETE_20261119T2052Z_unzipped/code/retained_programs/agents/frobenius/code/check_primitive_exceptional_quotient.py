"""Exact bounded checks of the integral primitive quotient in PB Step 3.

The general proof is the integral multigrading argument.  These checks verify
the identical concrete cubic ring in finitely many (s,m) and do not replace it.
"""
from collections import defaultdict
from datetime import datetime, timezone
from itertools import product
from pathlib import Path
import hashlib, json, time

base = Path(__file__).resolve().parents[1]
out = base / "output"
start = time.perf_counter()
record = {"started_utc": datetime.now(timezone.utc).isoformat(),
          "scope": "Exact integer identities in the listed finite Chow lattices; no geometric inference from computation alone.",
          "cases": []}
# Cubic basis: 0=unit; 1=H; 2..7=E1..E6; 8=point.
degree = (0,1,1,1,1,1,1,1,2)
# A=3H-E1-...-E6. Quotient eliminates E6=3H-E1-...-E5.
q = {1:{0:1}, **{i:{i-1:1} for i in range(2,7)},
     7:{0:3,1:-1,2:-1,3:-1,4:-1,5:-1}}
avec = {1:3,2:-1,3:-1,4:-1,5:-1,6:-1,7:-1}
qa = defaultdict(int)
for i,a in avec.items():
    for j,b in q[i].items():
        qa[j] += a*b
assert not any(qa.values())
record["primitive_quotient"] = {
    "basis": ["H","E1","E2","E3","E4","E5"],
    "E6_image": [3,-1,-1,-1,-1,-1],
    "A_image": [qa[i] for i in range(6)],
    "identity_minor_determinant": 1}

def basis(s,m,d):
    return [(h,)+w for h in range(min(m,d)+1)
            for w in product(range(9),repeat=s)
            if h+sum(degree[i] for i in w)==d]

def b_times(x,m):
    ans=defaultdict(int)
    if x[0]<m:
        ans[(x[0]+1,)+x[1:]] += 1
    for j,w in enumerate(x[1:],1):
        if w==0:
            for i,a in avec.items():
                y=list(x);y[j]=i;ans[tuple(y)] += a
        elif w==1:
            y=list(x);y[j]=8;ans[tuple(y)] += 3
        elif 2<=w<=7:
            y=list(x);y[j]=8;ans[tuple(y)] += 1
    return {x:a for x,a in ans.items() if a}

def psi(x):
    if x[0] or any(degree[w]!=1 for w in x[1:]):
        return {}
    ans={():1}
    for w in x[1:]:
        nxt=defaultdict(int)
        for t,c in ans.items():
            for j,a in q[w].items():
                nxt[t+(j,)] += c*a
        ans=dict(nxt)
    return ans

for s,m in product(range(1,4),range(4)):
    src=basis(s,m,s-1);dst=basis(s,m,s)
    dstset=set(dst)
    max_support=0;nonzero_entries=0
    transcript=[]
    for x in src:
        col=b_times(x,m)
        assert set(col)<=dstset
        image=defaultdict(int)
        for y,a in col.items():
            for z,c in psi(y).items():
                image[z] += a*c
                nonzero_entries+=1
        assert not any(image.values()), (s,m,x,image)
        max_support=max(max_support,len(image))
        transcript.append((x,sorted(col.items())))
    # The pure 1-dimensional divisor basis H,E1,...,E5 gives a unit minor
    # onto every tensor coordinate, certifying that this target is integral.
    for z in product(range(6),repeat=s):
        x=(0,)+tuple(j+1 for j in z)
        assert psi(x)=={z:1}
    encoded=json.dumps(transcript,separators=(",",":"),sort_keys=True).encode()
    record["cases"].append({"s":s,"r":s+1,"m":m,
        "source_rank":len(src),"target_Chow_rank":len(dst),
        "primitive_quotient_rank":6**s,
        "checked_b_columns":len(src),"Psi_b_zero":True,
        "primitive_quotient_unit_minor":True,
        "maximum_intermediate_tensor_support":max_support,
        "expanded_integer_terms":nonzero_entries,
        "multiplication_columns_sha256":hashlib.sha256(encoded).hexdigest()})
record["all_passed"]=True
record["case_count"]=len(record["cases"])
record["runtime_seconds"]=time.perf_counter()-start
record["finished_utc"]=datetime.now(timezone.utc).isoformat()
(out/"C3_primitive_exceptional_quotient.json").write_text(json.dumps(record,indent=2)+"\n")
(out/"C3_primitive_exceptional_quotient.out").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record,indent=2))
