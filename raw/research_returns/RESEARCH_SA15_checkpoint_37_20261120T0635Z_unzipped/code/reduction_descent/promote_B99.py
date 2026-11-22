from pathlib import Path
from datetime import datetime, timezone
import difflib, hashlib, json, re
own = Path(__file__).resolve().parents[1]
root = own.parents[1]
stem = "B_valuation_one_irreducible"
expected = "d765be51b4c7dac477933a2849b045aa23f50928ffef86488805d88c80b31095"
sha = lambda b: hashlib.sha256(b).hexdigest()
candidate = own/(stem+"_candidate.tex")
raw = candidate.read_bytes()
assert sha(raw) == expected
rp = root/"outputs/root_B99_audit.json"
cp = own.parent/"obstructions_crystals/B99_independent_audit.json"
r, c = json.loads(rp.read_text()), json.loads(cp.read_text())
for audit in (r, c):
    assert "PASS" in audit["status"] and audit["candidate_sha256"] == expected
assert r["author_inputs_preserved"] and r["all_mathematical_output_identical"]
assert c["author_hashes_before"] == c["author_hashes_after"]
assert c["program_run"]["all_mathematical_output_identical"]
rr, cr = r["checker_runtime_seconds"], c["program_run"]["internal_runtime_seconds"]
can = own/(stem+".tex")
prior = own/"notes"/(stem+".prepromotion.tex")
record_path = own/"outputs/B99_promotion.json"
assert not can.exists() and not prior.exists() and not record_path.exists()
prior.write_bytes(raw)
new = re.sub(r"\\status\{Candidate[^}]*\}", lambda _: r"\status{Proved; full independent root and companion audits passed.}", raw.decode())
new = new.replace(new.splitlines()[0], "% Proved after complete root and companion audits; exact candidate retained.", 1)
para = r"""
\smallskip
\noindent\emph{Independent audits.}
The complete root and obstruction/crystal companion
proof, source and exact-code audits passed. Their
unchanged isolated reruns took \(%s\) and \(%s\)
seconds, respectively; every mathematical field agreed
with the author output and all author bytes were
preserved. Both rederived the actual point fields,
both critical-coefficient cases, full terminal dual
spanning, and the scaled cyclotomic intersections and
different bounds. Both freshly read the retained
original Colmez ramification and different proofs on
pp.~14--18, with the exact dependency scopes in their
audit records. No new primary-source image inspection
or priority claim is made. The exact candidates,
typographical repairs, executed programs and outputs,
failed pre-write editing guards, and promotion diff
are retained.
""" % (rr, cr)
assert new.count(r"\end{remark}") == 1
new = new.replace(r"\end{remark}", para+r"\end{remark}")
can.write_text(new)
labels = re.findall(r"\\label\{([^}]+)\}", new)
assert len(labels) == 4 and labels == r["labels"] == list(c["labels"])
now = datetime.now(timezone.utc).isoformat()
scope = "Whole potentially supersingular height-two irreducible-residual finite special characters are recovered from actual p³ for every e=t p(p−1), p not dividing t. No reducible/mixed comparison or new full least-index equality is asserted."
record = {"status":"PROVED", "promotion_utc":now,
          "canonical":str(can), "canonical_sha256":sha(can.read_bytes()),
          "audited_candidate_sha256":expected, "preserved_candidate":str(prior),
          "labels":labels, "scope":scope,
          "root_audit":str(rp), "root_audit_utc":r["actual_utc"], "root_runtime_seconds":rr,
          "companion_audit":str(cp), "companion_audit_utc":c["actual_utc"], "companion_runtime_seconds":cr,
          "author_runtime_seconds":4.479122429998824,
          "canonical_change_scope":"Statuses, leading provenance comment and exact audit paragraph only. Audited mathematical proof unchanged.",
          "retained_failures":"Two aborted pre-write expected-count guards in spacing editing scripts, plus companion's pre-checker controller syntax failure; exact prior bytes/stderr retained. No mathematical checker failure.",
          "shared_wiring":"Root explicitly owns B99 wiring. No shared file modified."}
record_path.write_text(json.dumps(record, indent=2)+"\n")
(own/"notes/B99_promotion.diff").write_text("".join(difflib.unified_diff(raw.decode().splitlines(True), new.splitlines(True), fromfile=candidate.name, tofile=can.name)))
with (own/"CHECK_EVENTS.tsv").open("a") as f:
    for label in labels:
        f.write("\t".join([now, label, "PROVED_FULL_AUDITS", scope, stem+".tex;outputs/B99_promotion.json", "Complete root and companion actual-field/source/code audits; exact author-preserving reruns"])+"\n")
with (own/"STATUS_CURRENT.md").open("a") as f:
    f.write(f"\n## {now} — B99 promoted\n\n{scope}\n")
assert sha(candidate.read_bytes()) == expected
print(json.dumps(record, indent=2))
