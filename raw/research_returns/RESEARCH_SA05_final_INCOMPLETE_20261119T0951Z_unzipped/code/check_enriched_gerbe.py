"""Finite square-residue checks for the framed local-gerbe counterexample."""
from pathlib import Path
import json,time
t=time.monotonic()
cases=[(3,5),(-3,5),(6,7),(-6,13)]
rows=[]
for a,l in cases:
 squares=sorted({x*x%l for x in range(1,l)})
 assert a%l not in squares
 rows.append({"rational_square_class":a,"obstructing_prime":l,"residue":a%l,"nonzero_squares":squares})
out={"p":2,"local_twist":"3 at Q_3; trivial at every other odd prime","checks":rows,"seconds":time.monotonic()-t}
Path(__file__).with_name("check_enriched_gerbe_output.json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
