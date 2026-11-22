from pathlib import Path
import datetime
import hashlib
import json
import re

b=Path(__file__).resolve().parents[1]
candidate=b/"B_one_slope_quotient_candidate.tex"
expected="d43b8cd138f2a854caedb5b92da4dfc37bc0c5aad11a004320fbdc39b2de2f17"
raw=candidate.read_bytes()
assert hashlib.sha256(raw).hexdigest()==expected
root=json.loads((b.parents[1]/"outputs/root_B69_audit.json").read_text())
comp=json.loads((b.parent/"obstructions_crystals/B69_independent_audit.json").read_text())
for audit in (root,comp):
    assert audit["candidate_sha256"]==expected
    assert "PASS" in audit["status"].upper()
preserved=b/"notes/B_one_slope_quotient.prepromotion.tex"
assert not preserved.exists()
preserved.write_bytes(raw)
text=re.sub(r"\\status\{Candidate[^}]*\}",
            lambda _:r"\status{Proved; complete independent root and companion proof, source and exact-code audits passed.}",
            raw.decode())
text=text.replace("% Separate post-CP25 candidate. No assertion is promoted by finite checks.",
                  "% Proved after full root and companion audits; exact candidate and outputs retained.")
needle=("proofs; they do not establish existence or nonexistence of\n"
        "formal-group comparisons by enumeration alone.")
assert needle in text
text=text.replace(needle,
    "proofs; they do not establish existence or nonexistence of\n"
    "formal-group comparisons by enumeration alone.\n"
    "The complete independent root and companion audits passed.\n"
    "Their author-output-preserving exact reruns took\n"
    "\\(6.916882791992975\\) and \\(7.527760954006226\\) seconds,\n"
    "respectively. The exact audited candidate remains preserved.")
canonical=b/"B_one_slope_quotient.tex"
canonical.write_text(text)
labels=re.findall(r"\\label\{([^}]+)\}",text)
assert len(labels)==6 and r"\status{Candidate" not in text
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
record={
 "status":"PROVED",
 "promotion_utc":now,
 "canonical":str(canonical),
 "canonical_sha256":hashlib.sha256(canonical.read_bytes()).hexdigest(),
 "audited_candidate_sha256":expected,
 "preserved_candidate":str(preserved),
 "labels":labels,
 "root_audit":"../../outputs/root_B69_audit.json",
 "root_audit_utc":root["actual_utc"],
 "root_runtime_seconds":root["independent_runtime_seconds"],
 "companion_audit":"../obstructions_crystals/B69_independent_audit.json",
 "companion_audit_utc":comp["actual_utc"],
 "companion_runtime_seconds":comp["code"]["runtime_seconds"],
 "author_runtime_seconds":7.471134923995123,
 "scope":"Exact full B4 nu_min(p,p^2-1,2)=2 for all p>=5, including p5/e24. Upper recovery at actual p^3 for all (p-1)|e, p not dividing e, e<p^2. No p-divisible ramification or larger two-slope upper bound inferred.",
 "checkpoint_scope":"Promoted only after CP25 archive release; frozen CP25 PDF was not altered.",
}
(b/"outputs/B69_promotion.json").write_text(json.dumps(record,indent=2)+"\n")
with (b/"CHECK_EVENTS.tsv").open("a") as f:
    for label in labels:
        f.write("\t".join([now,label,"PROVED_FULL_AUDITS",record["scope"],
            "B_one_slope_quotient.tex;outputs/B69_promotion.json",
            "Complete root and OC proof/dependency/exact-code PASS; exact candidate and all three runtimes retained"])+"\n")
with (b/"STATUS_CURRENT.md").open("a") as f:
    f.write(f"\n## {now} — B69 promoted: first tame boundary exact\n\n"
        "All six assertions in B_one_slope_quotient.tex are proved after full root and OC audits. "
        "The exact full-monodromy index is nu_min(p,p^2−1,2)=2 for every p≥5, including p5/e24. "
        "The proof handles actual one-slope stable-line quotients and removes the determinant normalization from the two-slope comparison below p^2. "
        "The p5/e20 wild absolute index remains open; the next p5/e28 prime-to-p boundary is a separate unpromoted lead. "
        "The exact candidate, source-read scope, full certificate and all independent preserved-output runs are retained. "
        "Promotion followed CP25 archival release and does not modify that immutable checkpoint.\n")
print(json.dumps(record,indent=2))
