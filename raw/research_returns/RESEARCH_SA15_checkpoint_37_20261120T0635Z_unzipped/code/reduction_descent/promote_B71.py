from pathlib import Path
import datetime,hashlib,json,re
b=Path(__file__).resolve().parents[1]
work=b.parents[1]
s=b/"B_marked_quotient_sector_candidate.tex"
expected="dcb305d9e9012a4af8d1fe69a9ce5311e3a58bfd48a6f8ea0c2505a2b93159f0"
raw=s.read_bytes()
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((work/"outputs/root_B71_audit.json").read_text())
comp=json.loads((b.parent/"obstructions_crystals/B71_independent_audit.json").read_text())
for a in (root,comp):
    assert a["candidate_sha256"]==expected and "PASS" in a["status"].upper()
pres=b/"notes/B_marked_quotient_sector.prepromotion.tex"
assert not pres.exists()
pres.write_bytes(raw)
text=re.sub(r"\\status\{Candidate[^}]*\}",
    lambda _:r"\status{Proved; complete independent root and companion proof and exact-code audits passed.}",raw.decode())
text=text.replace("% Separate post-CP25 candidate. Exact point-field proofs precede finite checks.",
                  "% Proved after full root and companion audits; exact candidate and outputs retained.")
needle="These finite checks supplement the complete all-prime proofs."
assert needle in text
text=text.replace(needle,needle+"\nThe complete independent root and companion audits passed.\n"
 "Their author-output-preserving exact reruns took\n"
 "\\(1.4025961040024413\\) and \\(1.4007752400066238\\) seconds,\n"
 "respectively. The exact audited candidate and all full audit\n"
 "records are preserved.")
canonical=b/"B_marked_quotient_sector.tex"
canonical.write_text(text)
labels=re.findall(r"\\label\{([^}]+)\}",text)
assert len(labels)==7 and r"\status{Candidate" not in text
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={
 "status":"PROVED","promotion_utc":now,
 "canonical":str(canonical),
 "canonical_sha256":hashlib.sha256(canonical.read_bytes()).hexdigest(),
 "audited_candidate_sha256":expected,"preserved_candidate":str(pres),"labels":labels,
 "root_audit":"../../outputs/root_B71_audit.json","root_audit_utc":root["actual_utc"],
 "root_runtime_seconds":root["independent_runtime_seconds"],
 "companion_audit":"../obstructions_crystals/B71_independent_audit.json",
 "companion_audit_utc":comp["actual_utc"],
 "companion_runtime_seconds":1.4007752400066238,
 "author_runtime_seconds":1.3819726219953736,
 "scope":"Exact full B4 nu_min(p,t(p-1),2)=2 for p>=5,2<=t<=2p+1,p not dividing t; new p5 indices32,36,44. No p-divisible-e or e=2(p^2-1) claim.",
 "wiring_authorization":"Root explicitly authorized adding canonical source to consolidate.py and prepare_checkpoint26.py required list.",
}
backup=b/"notes/CP26_before_B71_wiring"
backup.mkdir(exist_ok=False)
changes=[]
for path,old,new in [
 (work/"code/consolidate.py",
  "                    'B_next_tame_boundary.tex']:",
  "                    'B_next_tame_boundary.tex',\n                    'B_marked_quotient_sector.tex']:"),
 (work/"code/prepare_checkpoint26.py",
  "required.append('agents/monodromy/nonordinary_uniform_seven_theta_geometry.tex')",
  "required.append('agents/monodromy/nonordinary_uniform_seven_theta_geometry.tex')\nrequired.append('agents/reduction_descent/B_marked_quotient_sector.tex')"),
]:
    before=path.read_bytes()
    before_text=before.decode()
    assert before_text.count(old)==1
    (backup/path.name).write_bytes(before)
    after=before_text.replace(old,new).encode()
    path.write_bytes(after)
    changes.append({"path":str(path),"before_sha256":hashlib.sha256(before).hexdigest(),
      "after_sha256":hashlib.sha256(after).hexdigest(),"preserved":str(backup/path.name)})
record["wiring_changes"]=changes
(b/"outputs/B71_promotion.json").write_text(json.dumps(record,indent=2)+"\n")
with (b/"CHECK_EVENTS.tsv").open("a") as f:
 for label in labels:
  f.write("\t".join([now,label,"PROVED_FULL_AUDITS",record["scope"],
   "B_marked_quotient_sector.tex;outputs/B71_promotion.json",
   "Root and OC full proof/dependency/code PASS; exact candidate and all runtimes retained"])+"\n")
with (b/"STATUS_CURRENT.md").open("a") as f:
 f.write(f"\n## {now} — B71 promoted: scalar-safe marked-quotient sector\n\n"
  "All seven assertions in B_marked_quotient_sector.tex are proved after full root and OC audits. "
  "The full-monodromy exact index is nu_min(p,t(p−1),2)=2 for p≥5,2≤t≤2p+1,p∤t; new p5 indices32,36,44. "
  "The common degree-p² point field identifies quotient high lines even in the scalar case. "
  "The second quotient requires only first-level prime-parameter recovery, separately proved. "
  "Root-authorized CP26 wiring was made in consolidate.py and prepare_checkpoint26.py; prior versions and hashes are preserved. "
  "The p-divisible absolute indices and next prime-to-p e=2(p²−1) remain outside this theorem. "
  "No code run failed; the discarded weight-sign outline is retained separately and unused.\n")
print(json.dumps(record,indent=2))
