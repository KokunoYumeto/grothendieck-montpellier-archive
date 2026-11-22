"""Authorized owned-file promotion; shared integration remains with root."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / "agents/obstructions_crystals"
src = own / "post_CP36_type_1_5_evaluation_fibres_candidate.tex"
dst = own / "A4_type_1_5_evaluation_fibres.tex"
expected = "0e741584e1093eacc160cd9b7a7a2cccc97fff69696c7528f00902093dff13bd"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(src) == expected and not dst.exists()
audits = [
    "outputs/root_type15_evaluation_fibres_audit.json",
    "agents/monodromy/outputs/independent_type_1_5_evaluation_fibres_audit.json",
]
for path in audits:
    record = json.loads((root / path).read_text())
    assert "PASS" in record["status"] and record["candidate_sha256"] == expected
before = src.read_text()
labels = re.findall(r"\\label\{([^}]+)\}", before)
after, count = re.subn(r"\\status\{Candidate[^}]*\}",
                       r"\\status{Proved; full independent proof audits passed.}", before)
assert count == len(labels) == 3
old_header = "% Isolated post-CP36 candidate. No canonical or checkpoint input is changed."
new_header = "% Promoted after complete independent root and companion proof audits."
assert after.count(old_header) == 1
after = after.replace(old_header, new_header, 1)
clean = lambda s: re.sub(r"\\status\{[^}]*\}", "", "\n".join(s.splitlines()[1:]))
assert clean(before) == clean(after)
history = own / "notes/CP37_type_1_5_evaluation_fibres_promotion"
history.mkdir(exist_ok=False)
(history / "candidate.tex").write_bytes(src.read_bytes())
(history / "promotion.diff").write_text("".join(difflib.unified_diff(
    before.splitlines(True), after.splitlines(True), fromfile="candidate", tofile="canonical")))
with dst.open("x") as f:
    f.write(after)
assert sha(src) == expected
now = datetime.now(timezone.utc).isoformat()
scope = (
    "For any ample globally generated type-(1,5) line in characteristic two, the actual "
    "rank-four Frobenius evaluation kernel map is generically finite exactly when there "
    "is no elliptic curve of line degree two. If such an elliptic quotient exists, the "
    "map factors through it via an injective-on-geometric-points curve map. In the "
    "nonordinary case the actual theta evaluation image lies in the polar quintic. "
    "No separability of that kernel map, exceptional coefficient exclusion, common wall, "
    "full monodromy or embedding assertion is made."
)
record = {
    "status": "PROMOTED AFTER TWO COMPLETE INDEPENDENT PROOF AUDITS",
    "actual_utc": now,
    "candidate": str(src.relative_to(root)),
    "candidate_sha256": expected,
    "canonical": str(dst.relative_to(root)),
    "canonical_sha256": sha(dst),
    "labels": labels,
    "audits": audits,
    "changes": "Three status lines and the opening comment only; mathematical text identical.",
    "history": str(history.relative_to(root)),
    "scope": scope,
    "new_numerical_run": None,
    "shared_files_changed": [],
    "integration": "Root retains ownership of consolidate, checkpoint config, report and bibliography integration.",
}
rp = own / "type_1_5_evaluation_fibres_promotion.json"
with rp.open("x") as f:
    json.dump(record, f, indent=2)
    f.write("\n")
with (own / "CHECK_EVENTS.tsv").open("a") as f:
    for label in labels:
        f.write("\t".join([now, label, "promotion-after-two-full-proof-audits",
                            str(dst.relative_to(root)), scope, "PROVED",
                            str(rp.relative_to(root))]) + "\n")
with (own / "D_results.md").open("a") as f:
    f.write("\n\n## Actual type-(1,5) evaluation fibres — " + now + "\n\n" + scope
            + "\n\nCanonical: `" + dst.name + "`. The exact candidate and status-only mathematical "
              "promotion are retained. Shared checkpoint integration is reserved to root.\n")
print(json.dumps({"status": record["status"], "actual_utc": now,
                  "canonical": record["canonical"], "canonical_sha256": record["canonical_sha256"],
                  "record": str(rp.relative_to(root)), "shared_files_changed": []}))
