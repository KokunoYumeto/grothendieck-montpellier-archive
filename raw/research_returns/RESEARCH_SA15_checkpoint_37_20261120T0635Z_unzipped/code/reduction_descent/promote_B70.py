from pathlib import Path
import datetime,hashlib,json,re
b=Path(__file__).resolve().parents[1]
s=b/"B_next_tame_boundary_candidate.tex"
expected="542f911ef3b58b70f12be51682d4406061330e996c9d06cb05cbebfd18faea75"
raw=s.read_bytes()
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((b.parents[1]/"outputs/root_B70_audit.json").read_text())
comp=json.loads((b.parent/"obstructions_crystals/B70_independent_audit.json").read_text())
for a in (root,comp):
    assert a["candidate_sha256"]==expected
    assert "PASS" in a["status"].upper()
pres=b/"notes/B_next_tame_boundary.prepromotion.tex"
assert not pres.exists()
pres.write_bytes(raw)
text=re.sub(r"\\status\{Candidate[^}]*\}",
  lambda _:r"\status{Proved; complete independent root and companion proof and exact-code audits passed.}",raw.decode())
text=text.replace("% Separate post-CP25 candidate; no finite computation promotes a statement.",
                  "% Proved after full root and companion audits; exact candidate and outputs retained.")
needle="These finite checks supplement the preceding all-prime proofs."
assert needle in text
text=text.replace(needle,
    needle+"\nThe complete independent root and companion audits passed,\n"
    "with author-output-preserving exact reruns in\n"
    "\\(0.16807877800602\\) and \\(0.1444874750013696\\) seconds,\n"
    "respectively. Both full audit records and the exact\n"
    "prepromotion candidate are retained.")
canonical=b/"B_next_tame_boundary.tex"
canonical.write_text(text)
labels=re.findall(r"\\label\{([^}]+)\}",text)
assert len(labels)==6 and r"\status{Candidate" not in text
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={
 "status":"PROVED","promotion_utc":now,
 "canonical":str(canonical),
 "canonical_sha256":hashlib.sha256(canonical.read_bytes()).hexdigest(),
 "audited_candidate_sha256":expected,"preserved_candidate":str(pres),
 "labels":labels,
 "root_audit":"../../outputs/root_B70_audit.json",
 "root_audit_utc":root["actual_utc"],
 "root_runtime_seconds":0.16807877800602,
 "companion_audit":"../obstructions_crystals/B70_independent_audit.json",
 "companion_audit_utc":comp["actual_utc"],
 "companion_runtime_seconds":0.1444874750013696,
 "author_runtime_seconds":0.14006940000399482,
 "scope":"Exact full B4 nu_min(p,(p+2)(p-1),2)=2 for every p>=5, including p5/e28. No p-divisible-e or subsequent (p+3)(p-1) assertion.",
 "history":"Exact candidate, pre-certificate proof, unexecuted malformed draft block and all three finite-run outputs/runtimes retained. No executed numerical failure.",
}
(b/"outputs/B70_promotion.json").write_text(json.dumps(record,indent=2)+"\n")
with (b/"CHECK_EVENTS.tsv").open("a") as f:
 for label in labels:
  f.write("\t".join([now,label,"PROVED_FULL_AUDITS",record["scope"],
   "B_next_tame_boundary.tex;outputs/B70_promotion.json",
   "Root and OC full proof/dependency/code PASS; exact candidate and all runtimes retained"])+"\n")
with (b/"STATUS_CURRENT.md").open("a") as f:
 f.write(f"\n## {now} — B70 promoted: next tame boundary exact\n\n"
  "All six assertions in B_next_tame_boundary.tex are proved after full root and OC audits. "
  "The exact full-monodromy index is nu_min(p,(p+2)(p−1),2)=2 for every p≥5, including p5/e28. "
  "The small {1,p} parameter collision preserves the special character by Frobenius conjugation; the new tame B=p² case is settled by actual residual eigenvalues. "
  "The p5/e20 wild absolute index and next prime-to-p index p5/e32 remain open. "
  "The retained {2,p+1} arithmetic pattern is not an existence assertion. "
  "All exact candidates, code drafts and outputs/runtimes are retained.\n")
print(json.dumps(record,indent=2))
