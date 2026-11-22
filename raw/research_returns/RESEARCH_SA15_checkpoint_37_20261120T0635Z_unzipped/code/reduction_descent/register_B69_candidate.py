from pathlib import Path
import datetime
import hashlib
import json
import re

b=Path(__file__).resolve().parents[1]
source=b/"B_one_slope_quotient_candidate.tex"
program=b/"code/verify_one_slope_boundary.py"
output=program.with_suffix(".output.json")
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
labels=re.findall(r"\\label\{([^}]+)\}",source.read_text())
assert len(labels)==6
r=json.loads(output.read_text())
assert r["status"]=="PASS"
record={
 "status":"CANDIDATE; author complete proof and exact supplement checked; root and companion full audit records pending",
 "actual_utc":now,
 "candidate":str(source),
 "candidate_sha256":sha(source),
 "labels":labels,
 "program":str(program),
 "program_sha256":sha(program),
 "output":str(output),
 "output_sha256":sha(output),
 "author_elapsed_seconds":r["elapsed_seconds"],
 "author_run_utc":r["actual_utc"],
 "counts":r["counts"],
 "preserved_before_certificate":"notes/B_one_slope_quotient.before_certificate.tex",
 "source_scope":"Re-read complete B49 Newton/inertia proofs, B60 lower-break proof, B63 cyclic threshold and B68 sector proof; original primary passages are reused from their retained complete source audits. No fresh web/source read or new numerical existence claim is made.",
 "claimed_new_gate":"nu_min(p,p^2-1,2)=2 for every p>=5; whole-formal upper bound for (p-1)|e, p not dividing e, e<p^2",
 "failures":"No failed finite run or superseded mathematical claim in this candidate; its critical B=e case was explicitly included before the first written candidate.",
}
(b/"outputs/B69_candidate_record.json").write_text(json.dumps(record,indent=2)+"\n")
with (b/"CHECK_EVENTS.tsv").open("a") as f:
 for label in labels:
  f.write(f"{now}\t{label}\tCANDIDATE_AUTHOR_CHECKED\tB69 complete proof and exact finite supplement; independent complete audits pending\tB_one_slope_quotient_candidate.tex;outputs/B69_candidate_record.json\tAuthor {r['elapsed_seconds']}s; exact source and output hashes retained; no promotion\n")
(b/"notes/POST_CP25_B69_SOURCE_CHECKS.md").write_text(
 "# B69 source and dependency scope\n\n"
 f"Recorded {now}.\n\n"
 "This is a new direct quotient argument. No new external theorem is imported. "
 "The original Hopkins–Gross Proposition 5.7 and Proposition 12.10/full proof "
 "are used through the freshly re-read B49 coefficient/Newton proof and "
 "the exact inverse polygons in B63. Integral Tate extension and quotient "
 "descent use the already opened original Tate 1967 Theorem 4 and "
 "Corollaries 1–2, pp.181–182, with the full proof and Proposition 12 "
 "re-read for B67. Fixed-coefficient break estimates use B60 and the "
 "already retained original Serre/Colmez and Stacks 032A proof audits. "
 "The entire B68 proof was re-read before removing its determinant normalization; "
 "all arguments that previously depended on nonsquare determinant have been "
 "replaced by an explicit polygon hypothesis or the one-slope scalar/irreducible analysis. "
 "No new web search or primary-source re-opening is claimed for B69.\n\n"
 "All finite computations are in verify_one_slope_boundary.py. "
 "They reconstruct lower convex hulls and exact root multiplicities, "
 "rather than infer formal-group existence from arithmetic enumeration. "
 "No run failed. The original proof before its finite-certificate paragraph is preserved.\n"
)
print(json.dumps({"actual_utc":now,"candidate_sha256":record["candidate_sha256"],"labels":labels,"author_elapsed_seconds":r["elapsed_seconds"]},indent=2))
