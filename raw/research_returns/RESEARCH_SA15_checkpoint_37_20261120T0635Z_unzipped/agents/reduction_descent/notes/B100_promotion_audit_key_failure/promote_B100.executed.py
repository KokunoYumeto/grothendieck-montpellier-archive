from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, re
own = Path(__file__).resolve().parents[1]
root = own.parents[1]
stem = "B_second_wild_trace_arc"
expected = "f0fb542a2cbd9ee40f0144f1ae4f8dd209ec0f0bd92153b70cb8d511d7ae0950"
sha = lambda b: hashlib.sha256(b).hexdigest()
candidate = own/(stem+"_candidate.tex")
raw = candidate.read_bytes()
assert sha(raw) == expected
rp = root/"outputs/root_B100_audit.json"
cp = own.parent/"monodromy/outputs/independent_B100_second_wild_trace_arc_audit.json"
r, c = json.loads(rp.read_text()), json.loads(cp.read_text())
for audit in (r, c):
    assert "PASS" in audit["status"] and audit["candidate_sha256"] == expected
assert r["author_inputs_preserved"] and r["all_mathematical_output_identical"]
run = c["literal_isolated_rerun"]
assert run["author_bytes_unchanged"] and run["all_mathematical_output_identical"]
rr, cr = r["checker_runtime_seconds"], run["runtime_seconds"]
can = own/(stem+".tex")
prior = own/"notes"/(stem+".prepromotion.tex")
record_path = own/"outputs/B100_promotion.json"
assert not can.exists() and not prior.exists() and not record_path.exists()
prior.write_bytes(raw)
new = re.sub(r"\\status\{Candidate[^}]*\}", lambda _: r"\status{Proved; full independent root and companion audits passed.}", raw.decode())
new = new.replace(new.splitlines()[0], "% Proved after complete root and companion audits; exact candidate retained.", 1)
para = r"""
\smallskip
\noindent\emph{Independent audits.}
The complete root and monodromy companion mathematical,
source-scope and exact-code audits passed. Literal isolated
reruns took \(%s\) and \(%s\) seconds, respectively,
with every mathematical output identical and all author
bytes unchanged. Both rederived every strict Newton branch,
the actual Eisenstein ring and marked-point descent,
finite quotient and compatible cocycle lift, and the
full actual-target upper bound. Both freshly reopened
the exact Hopkins--Gross recurrence, coefficient and
deformation passages, with the original text's
Hazewinkel attribution kept explicit. The companion
also reread the retained original Kisin determinant
dependencies; no such fresh Kisin read is attributed
to the root or author. No new Bondarko or Tate
primary reading is claimed. Exact source-access
failures, the successful original-source reads,
candidates, all executed outputs and promotion
diff are retained in the audit records.
""" % (rr, cr)
assert new.count(r"\end{remark}") == 1
new = new.replace(r"\end{remark}", para+r"\end{remark}")
can.write_text(new)
labels = re.findall(r"\\label\{([^}]+)\}", new)
assert len(labels) == 5 and labels == r["labels"] == [x["label"] for x in c["per_label"]]
now = datetime.now(timezone.utc).isoformat()
scope = "Actual p³ ambiguity for p>=5, p(p−1)|e, e>p², with one whole potentially good group and one allowed filtered group. The existential mixed threshold is exact at vp(e)=1. Full exact height-two family ν_min(p,2p(p−1),2)=3; in particular ν_min(5,40,2)=3."
record = {"status":"PROVED", "promotion_utc":now,
          "canonical":str(can), "canonical_sha256":sha(can.read_bytes()),
          "audited_candidate_sha256":expected, "preserved_candidate":str(prior),
          "labels":labels, "scope":scope,
          "root_audit":str(rp), "root_audit_utc":r["actual_utc"], "root_runtime_seconds":rr,
          "companion_audit":str(cp), "companion_audit_utc":c["actual_utc"], "companion_runtime_seconds":cr,
          "author_runtime_seconds":0.15055808699980844,
          "canonical_change_scope":"Statuses, leading provenance comment and exact audit paragraph only; mathematical proof unchanged.",
          "source_scope":"Author/root/companion freshly opened exact original HG passages; companion additionally reread retained original Kisin proofs. Full B62/B64/B76 chains checked. No new Hazewinkel book, Tate/Bondarko primary reading or page-image claim.",
          "retained_failures":"No mathematical checker failure; root and companion original-source access failures retained in their full audit records.",
          "shared_wiring":"Root explicitly owns B100 wiring; no shared file modified."}
record_path.write_text(json.dumps(record, indent=2)+"\n")
(own/"notes/B100_promotion.diff").write_text("".join(difflib.unified_diff(raw.decode().splitlines(True), new.splitlines(True), fromfile=candidate.name, tofile=can.name)))
with (own/"CHECK_EVENTS.tsv").open("a") as f:
    for label in labels:
        f.write("\t".join([now,label,"PROVED_FULL_AUDITS",scope,stem+".tex;outputs/B100_promotion.json","Complete root and monodromy proof/source/code audits; actual construction and exact upper/lower bounds independently rederived"])+"\n")
with (own/"STATUS_CURRENT.md").open("a") as f:
    f.write(f"\n## {now} — B100 promoted\n\n{scope}\n")
assert sha(candidate.read_bytes()) == expected
print(json.dumps(record, indent=2))
