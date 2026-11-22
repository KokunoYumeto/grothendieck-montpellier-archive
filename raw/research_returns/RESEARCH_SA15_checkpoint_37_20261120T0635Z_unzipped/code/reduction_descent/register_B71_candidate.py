from pathlib import Path
import datetime,hashlib,json,re
b=Path(__file__).resolve().parents[1]
s=b/"B_marked_quotient_sector_candidate.tex"
p=b/"code/verify_marked_quotient_sector.py"
o=p.with_suffix(".output.json")
r=json.loads(o.read_text())
assert r["status"]=="PASS"
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
labels=re.findall(r"\\label\{([^}]+)\}",s.read_text())
assert len(labels)==7
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={
 "status":"CANDIDATE_AUTHOR_CHECKED; final independent proof/code audits pending",
 "actual_utc":now,"candidate":str(s),"candidate_sha256":sha(s),"labels":labels,
 "program":str(p),"program_sha256":sha(p),"output":str(o),"output_sha256":sha(o),
 "author_runtime_seconds":r["elapsed_seconds"],"author_run_utc":r["actual_utc"],
 "counts":r["counts"],
 "scope":"Claimed exact full B4 nu_min(p,t(p-1),2)=2 for p>=5,2<=t<=2p+1,p not dividing t; no p-divisible-e or next e=2(p^2-1) assertion.",
 "dependencies":"Complete B69 actual quotient/point-field proofs, B60 lower-break proof, B67 one-slope irreducible result and B63 mixed threshold/lower construction. No new external source retrieval.",
 "history":"Exact pre-certificate proof and all executed code/output retained. No executed numerical failure. A discarded refined-weight outline with a point/ring-action sign mismatch is explicitly retained separately and not used.",
}
(b/"outputs/B71_candidate_record.json").write_text(json.dumps(record,indent=2)+"\n")
with (b/"CHECK_EVENTS.tsv").open("a") as f:
 for label in labels:
  f.write("\t".join([now,label,"CANDIDATE_AUTHOR_CHECKED",record["scope"],
   "B_marked_quotient_sector_candidate.tex;outputs/B71_candidate_record.json",
   "Complete written proof and exact finite supplement; independent full audit records pending; scalar case explicitly tested"])+"\n")
(b/"notes/POST_CP25_B71_SOURCE_CHECKS.md").write_text(
 "# B71 source and dependency scope\n\n"+now+"\n\n"
 "No new external theorem is imported. The proof uses the already fully audited "
 "B69 actual quotient root counts and semilinear descent, the complete B60 "
 "fixed-coefficient lower-break proof, and the previously opened original "
 "Hopkins–Gross/Tate source bridges retained in those audits. "
 "The new prime-parameter statement is explicitly proved at first level; "
 "it is not obtained by silently lowering the hypothesis of the old p^2 comparison lemma. "
 "The common point field is justified from an actual q-denominator and the "
 "R-rational translation torsor (with R=L in this application). "
 "The scalar-safe proof uses the same actual automorphism in both models.\n\n"
 "All finite checks are in verify_marked_quotient_sector.py and passed on the "
 "first author execution. The discarded coefficient-weight lead is separately "
 "recorded in POST_CP25_unpromoted_weight_lead.md and is not used. "
 "No new literature search or primary re-opening is claimed for this candidate.\n")
print(json.dumps({"actual_utc":now,"candidate_sha256":record["candidate_sha256"],"labels":labels,"author_runtime_seconds":r["elapsed_seconds"]},indent=2))
