"""R031 low-degree table reconstructed from the exact fat-arrangement complex."""
from pathlib import Path
from fractions import Fraction
from functools import lru_cache
import csv,json,hashlib
HERE=Path(__file__).resolve().parent
# Reuse the previously independently checked pure restriction-complex functions;
# do not execute their prior whole-run receipt writer.
namespace={"__file__":str(HERE/"check_fat_arrangement_independent.py")}
text=(HERE/"check_fat_arrangement_independent.py").read_text()
exec(compile(text.split("totals={};rows=[];")[0],namespace["__file__"],"exec"),namespace)
partitions=namespace["partitions"]; z=namespace["z"]
arrangement_trace=namespace["arrangement_trace"]

@lru_cache(None)
def coefficient(m,n,lam):
    lam=tuple(x for x in lam if x)
    if len(lam)>m:return 0
    if m==1:return int(lam==(n,))
    if m==2:
        return int(len(lam)<=2 and (lam+(0,))[1]%2==0)
    padded=lam+(0,)*(m-len(lam))
    alpha=tuple(padded[1]-padded[m-1-i] for i in range(m-2))
    k=max(0,padded[1]-n)
    result=sum(Fraction((-1)**((m-len(cyc))*padded[1])
                        *arrangement_trace(m,k,alpha,cyc),z(cyc))
               for cyc in partitions(m))
    assert result.denominator==1 and result>=0
    return int(result)

path=HERE.parent/"rectangular/OUTER5_CANONICAL_LOW_DEGREE_CHECK.tsv"
with path.open(newline="") as f:rows=list(csv.DictReader(f,delimiter="\t"))
expected={(n,lam+(0,)*(5-len(lam))) for n in range(1,5)
          for lam in partitions(5*n) if len(lam)<=5}
actual=set();strict=[];encoded=[]
for row in rows:
    n=int(row["n"]);lam=tuple(map(int,row["output"].split(",")))
    actual.add((n,lam))
    source=coefficient(n,5,lam);target=coefficient(5,n,lam)
    assert source==int(row["source_MN"])==int(row["actual_image_multiplicity"])
    assert target==int(row["target_MN"])
    assert target-source==int(row["actual_cokernel_multiplicity"])
    encoded.append((n,lam,source,target))
    if all(lam[i]>lam[i+1] for i in range(4)):
        strict.append((n,lam,source,target))
assert len(rows)==len(actual)==len(expected)==313 and actual==expected
assert len(strict)==38
by_n={}
for n in range(1,5):
    subset=[r for r in strict if r[0]==n]
    by_n[n]=dict(strict_cases=len(subset),positive_images=sum(r[2]>0 for r in subset),
                 positive_targets=sum(r[3]>0 for r in subset),
                 reached_nonzero_targets=sum(r[3]>0 and r[2]==r[3] for r in subset))
assert by_n[4]==dict(strict_cases=30,positive_images=16,positive_targets=27,reached_nonzero_targets=4)
receipt=dict(statement="R031 complete low-degree multiplicity table",status="PASS",
 partitions=313,source_and_target_comparisons=626,strict_cases=38,strict_summary=by_n,
 method="literal selected-subset restriction complex and orientation/Weyl extraction; m1 identity and m2 balanced determinant parity",
 input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
 values_sha256=hashlib.sha256(json.dumps(encoded,separators=(",",":")).encode()).hexdigest(),
 note="Map ranks use proved canonical injectivity; this calculation checks all multiplicities and table bookkeeping.")
(HERE/"OUTER5_CANONICAL_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
