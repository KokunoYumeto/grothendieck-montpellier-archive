"""Promote the fully independently audited uniform cubic-component transfer."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, csv, difflib

agent = Path(__file__).resolve().parents[1]
work = agent.parents[1]
candidate = agent / "nonordinary_cubic_component_norm_transfer_candidate.tex"
expected = "fc7cfba6ce2075e9b6fef1ce2dde893b4f40a1c53a72cb18d4e594852a8b89cf"
assert hashlib.sha256(candidate.read_bytes()).hexdigest() == expected
root_audit = work / "outputs/root_cubic_component_transfer_audit.json"
oc_audit = agent.parent / "obstructions_crystals/cubic_component_norm_transfer_independent_audit.json"
assert root_audit.exists() and oc_audit.exists()
canonical = agent / "nonordinary_cubic_component_norm_transfer.tex"
assert not canonical.exists()
s = candidate.read_text()
s = s.replace("% Isolated post-CP26 extension; full independent audits pending.",
              "% Post-CP26 theorem; exact fully audited candidate retained separately.")
s = s.replace("\\status{Candidate; complete symbolic extension submitted for audit.}",
              "\\status{Proved and independently checked.}")
assert s.count("\\textup{[Candidate.]}") == 5
s = s.replace("\\textup{[Candidate.]}", "\\textup{[Proved; independent audits passed.]}")
s = s.replace("Complete independent audits are\nrequired before promotion.",
              "The complete parent proof and dependency audit passed at\n"
              "22:46:04 UTC on 19 November 2026, and the obstruction/crystal\n"
              "reviewer independently passed the full symbolic proof and\n"
              "all changed graph and rank formulas. Neither audit claims\n"
              "a new numerical experiment for this extension.")
canonical.write_text(s)
labels = ["lem:cubic-component-clean-node-product-candidate",
          "prop:cubic-component-weighted-graph-gluing-candidate",
          "thm:cubic-component-arbitrary-odd-norm-transfer-candidate",
          "cor:f0-odd-multiples-three-five-seven-candidate",
          "rem:cubic-component-norm-transfer-scope-candidate"]
changes = []
for rel, old, new in [
    ("code/consolidate.py",
     "                  'monodromy/nonordinary_arbitrary_odd_neighbors.tex']:",
     "                  'monodromy/nonordinary_arbitrary_odd_neighbors.tex',\n"
     "                  'monodromy/nonordinary_cubic_component_norm_transfer.tex']:"),
    ("code/prepare_checkpoint27.py", "for rel in required:\n",
     "required.append('agents/monodromy/nonordinary_cubic_component_norm_transfer.tex')\nfor rel in required:\n"),
]:
    p = work / rel
    before = p.read_text()
    assert before.count(old) == 1, rel
    h = agent / "history" / ("pre_cubic_component_" + rel.replace("/", "__"))
    assert not h.exists()
    h.write_text(before)
    after = before.replace(old, new)
    p.write_text(after)
    diff = h.with_name(h.name + ".diff")
    diff.write_text("".join(difflib.unified_diff(before.splitlines(True), after.splitlines(True), fromfile=h.name, tofile=rel)))
    changes.append({"file": rel, "prior": str(h), "diff": str(diff)})
now = datetime.now(timezone.utc).isoformat()
r = {"status": "PROMOTED", "actual_utc": now, "candidate_sha256": expected,
     "canonical": str(canonical), "canonical_sha256": hashlib.sha256(canonical.read_bytes()).hexdigest(),
     "labels": labels, "root_audit": str(root_audit), "OC_audit": str(oc_audit),
     "integration_changes": changes,
     "scope": "Every known full odd source degree e>=3 transfers through any odd polarized norm. Every fixed f0 odd degree divisible by3,5,or7 is full; all even f0 degrees were already proved. Fixed f0 odd11 and fixed f1 degree5/8 remain."}
(agent / "outputs/cubic_component_norm_transfer_promotion.json").write_text(json.dumps(r, indent=2) + "\n")
with (agent / "CHECK_EVENTS_post_CP16.tsv").open("a", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    for label in labels:
        writer.writerow([label, now, "/root/monodromy", "PROMOTED-root-OC-full-proof-PASS", r["scope"]])
with (agent / "post_CP16_notes.md").open("a") as f:
    f.write("\n## " + now + " — Uniform cubic-component norm transfer promoted\n\n"
            "The exact candidate remains unchanged. The extension uses e cubic components for any already full odd source degree e>=3, "
            "with type size18e², selected S18 pair lifts, and36(e−1) star entries. The source and target ranks drop by(e−1)(2−f); "
            "only clopen finite-Lang intersections are transported. Root and OC independently rederived the complete symbolic proof. "
            "No new numerical experiment or finite extrapolation was used. The resulting fixed f0 odd family is every odd number "
            "divisible by3,5,or7;11 remains the first unresolved odd degree. Exact consolidation/preflight before bytes and diffs are retained.\n")
print(json.dumps(r, indent=2))
