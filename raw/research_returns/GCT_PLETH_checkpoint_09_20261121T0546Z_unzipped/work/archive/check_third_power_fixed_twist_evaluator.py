"""G032 independent catalog, continuation and actual polytope/witness checks."""
from pathlib import Path
from math import comb
import sys,json,re
from check_third_power_fixed_twist_independent import independent_grid,LABELS
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent/"root"
sys.path.insert(0,str(ROOT))
import third_power_fixed_twist_positive as positive

reference=json.loads((ROOT/"THIRD_POWER_FIXED_TWIST_CERTIFICATE.json").read_text())
text=(ROOT/"third_power_fixed_twist_report.md").read_text().split("## 5.")[1].split("## 6.")[0]
catalog={}
for line in text.splitlines():
    if not re.match(r"^\| [012] \|",line):continue
    columns=[s.strip() for s in line.strip("|").split("|")]
    c,b,q=map(int,columns[:3])
    label="11111" if "1^5" in columns[3] else "".join(re.findall(r"\d",columns[3]))
    catalog[c,b,label]=(q,list(map(int,columns[4].split(","))))
expected={}
for c,data in reference["twists"].items():
    for b,entry in data["boundaries"].items():
        for label,zeros in entry["zero_residues"].items():
            if zeros:expected[int(c),int(b),label]=(entry["x_shift"],zeros)
assert catalog==expected

counts={"parameter_cases":0,"coefficients":0,"matrices":0,"witnesses":0}
seen_branches=set()
for c in range(3):
    cases=[(301+19*c,428+23*c)]
    for b in range(8):
        shift=max(0,15-3*c-2*b)
        cases.append((shift+301+2*b+c,b))
    for x,b in cases:
        independent,_=independent_grid((x,),(b,),c)
        values=tuple(int(v) for v in independent[:,0,0])
        counts["parameter_cases"]+=1
        seen_branches.add((c,"bulk" if b>=8 else b))
        for d in (0,1):
            for label,outer in enumerate(LABELS):
                effective=6-label if (d+b+x+c)%2 else label
                answer=positive.coefficient(x,b,c,d,outer)
                assert answer==values[effective],(x,b,c,d,outer,answer,values)
                counts["coefficients"]+=1
                polys=positive.polytopes(x,b,c,d,outer)
                assert len(polys)<=(17 if b>=8 else 4)
                lookup={tuple(p["order"]):p for p in polys}
                total=0
                for poly in polys:
                    quotients=[]
                    for slot,(row,rhs) in enumerate(poly["equalities"]):
                        assert row[slot]==60 and sum(abs(v) for v in row)==60
                        assert rhs%60==0 and rhs>=0
                        quotients.append(rhs//60)
                    term=poly["constant"]
                    for q,j in zip(quotients,poly["order"]):term*=comb(q,j)
                    total+=term
                    assert len(poly["variables"])<=(8 if b>=8 else 5)
                    counts["matrices"]+=1
                assert total==answer
                for witness in positive.witnesses(x,b,c,d,outer,limit=3):
                    poly=lookup[tuple(witness["order"])]
                    coordinates=witness["coordinates"]
                    assert len(coordinates)==len(poly["variables"])
                    assert all(sum(a*z for a,z in zip(row,coordinates))==rhs for row,rhs in poly["equalities"])
                    assert all(sum(a*z for a,z in zip(row,coordinates))<=rhs for row,rhs in poly["inequalities"])
                    counts["witnesses"]+=1
assert len(seen_branches)==27
receipt=dict(statement="G032 independent continuation, catalog and polytope transport",
             status="PASS",**counts,branches=len(seen_branches),
             boundary_catalog_rows=len(catalog),
             boundary_zeros=sum(len(v[1]) for v in catalog.values()),
             bulk_zeros=2,
             both_determinant_parities=True,
             method="independent normal-monomial/Weyl character evaluation beyond the interpolation grids; literal integer matrix constraints and bounded witnesses")
(HERE/"THIRD_POWER_FIXED_TWIST_EVALUATOR_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))

