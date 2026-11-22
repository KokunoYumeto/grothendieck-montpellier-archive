from pathlib import Path
import datetime,hashlib,json,re
b=Path(__file__).resolve().parents[1]
s=b/"B_next_tame_boundary_candidate.tex"
p=b/"code/verify_next_tame_boundary.py"
o=p.with_suffix(".output.json")
r=json.loads(o.read_text())
assert r["status"]=="PASS"
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
labels=re.findall(r"\\label\{([^}]+)\}",s.read_text())
assert len(labels)==6
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={
 "status":"CANDIDATE_AUTHOR_CHECKED; independent full audits pending",
 "actual_utc":now,
 "candidate":str(s),"candidate_sha256":sha(s),"labels":labels,
 "program":str(p),"program_sha256":sha(p),
 "output":str(o),"output_sha256":sha(o),
 "author_runtime_seconds":r["elapsed_seconds"],"author_run_utc":r["actual_utc"],
 "counts":r["counts"],
 "scope":"Claimed exact full B4 nu_min(p,(p+2)(p-1),2)=2 for every p>=5. No later tame or p-divisible-e extension.",
 "dependencies":"Complete B69 rules/quotients/one-slope proof reread, with its retained original-source audits; B63 full mixed threshold and lower construction reused. No new external source retrieval.",
 "history":"Exact pre-certificate proof retained. An unused malformed draft list-comprehension block was caught in review before execution; exact unexecuted draft notes/verify_next_tame_boundary.draft_before_cleanup.py is retained. No numerical execution failed.",
}
(b/"outputs/B70_candidate_record.json").write_text(json.dumps(record,indent=2)+"\n")
with (b/"CHECK_EVENTS.tsv").open("a") as f:
 for label in labels:
  f.write("\t".join([now,label,"CANDIDATE_AUTHOR_CHECKED",record["scope"],
     "B_next_tame_boundary_candidate.tex;outputs/B70_candidate_record.json",
     "Complete written proof and exact finite supplement; independent audits pending; pre-execution draft cleanup retained"])+"\n")
(b/"notes/POST_CP25_B70_SOURCE_CHECKS.md").write_text(
 "# B70 source and computation scope\n\n"+now+"\n\n"
 "No new external theorem or literature search is used. The proof reuses the fully audited "
 "B69 actual Newton, quotient and point-field lemmas at their stated unrestricted prime-to-p "
 "absolute indices. The new inputs are the explicit {1,p} Frobenius-orbit identity and "
 "the two residual eigenvalue congruences giving (p-1)|(B1+B2). "
 "The full monodromy reduction uses the existing B63 mixed threshold and lower construction.\n\n"
 "The exact finite supplement does not infer formal-group existence. Its output retains "
 "the later {2,p+1} arithmetic pattern as unexcluded, with no realization claim. "
 "An unused malformed draft comprehension was removed before any execution and its exact "
 "source retained; the first and only author run passed.\n")
print(json.dumps({"actual_utc":now,"candidate_sha256":record["candidate_sha256"],"labels":labels,"author_runtime_seconds":r["elapsed_seconds"]},indent=2))
