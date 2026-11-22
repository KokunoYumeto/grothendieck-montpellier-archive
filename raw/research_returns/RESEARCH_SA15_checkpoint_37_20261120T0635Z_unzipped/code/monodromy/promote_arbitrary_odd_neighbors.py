"""Promote the exact root/OC audited arbitrary-odd-neighbour proof."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, csv, difflib

agent = Path(__file__).resolve().parents[1]
work = agent.parents[1]
candidate = agent / "nonordinary_arbitrary_odd_neighbors_candidate.tex"
expected = "64cd5e486bbebf0b879c737fa16ffbecbb0a8bab91563c2e437585953befb52a"
assert hashlib.sha256(candidate.read_bytes()).hexdigest() == expected
root_audit = work / "outputs/root_arbitrary_odd_neighbors_audit.json"
oc = agent.parent / "obstructions_crystals/arbitrary_odd_neighbors_independent_audit.json"
precision = agent.parent / "obstructions_crystals/arbitrary_odd_neighbors_arithmetic_precision.json"
assert root_audit.exists() and oc.exists() and precision.exists()
canonical = agent / "nonordinary_arbitrary_odd_neighbors.tex"
assert not canonical.exists()
s = candidate.read_text()
s = s.replace("% Isolated post-CP26 candidate; no promotion before complete audits.",
              "% Post-CP26 theorem; exact independently audited candidate retained.")
s = s.replace("\\status{Candidate; complete proof submitted for independent audit.}",
              "\\status{Proved and independently checked.}")
assert s.count("\\textup{[Candidate.]}") == 4
s = s.replace("\\textup{[Candidate.]}", "\\textup{[Proved; independent audits passed.]}")
s = s.replace("The\ncomplete complement/duality, quotient, and composition arguments\nmust pass independent audits before promotion.",
              "The complete complement/duality, quotient, and composition\n"
              "arguments passed the parent full proof/source audit at\n"
              "22:41:22 UTC and the obstruction/crystal audit at 22:39:59 UTC\n"
              "on 19 November 2026; the latter also checked the final\n"
              "pointwise arithmetic-descent precision. No numerical run\n"
              "was needed or claimed for this symbolic proof.")
canonical.write_text(s)
labels = ["lem:nonordinary-mixed-principal-complement-candidate",
          "thm:nonordinary-arbitrary-odd-neighbor-candidate",
          "cor:nonordinary-all-odd-multiples-three-candidate",
          "rem:nonordinary-arbitrary-odd-neighbor-scope-candidate"]
changes = []
for rel, old, new in [
    ("code/consolidate.py",
     "                  'monodromy/nonordinary_nine_theta_norm_transfer.tex']:",
     "                  'monodromy/nonordinary_nine_theta_norm_transfer.tex',\n"
     "                  'monodromy/nonordinary_arbitrary_odd_neighbors.tex']:"),
    ("code/prepare_checkpoint27.py", "for rel in required:\n",
     "required.append('agents/monodromy/nonordinary_arbitrary_odd_neighbors.tex')\nfor rel in required:\n"),
]:
    p = work / rel
    before = p.read_text()
    assert before.count(old) == 1
    h = agent / "history" / ("pre_arbitrary_odd_neighbors_" + rel.replace("/", "__"))
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
     "labels": labels, "root_audit": str(root_audit), "OC_audit": str(oc),
     "OC_final_precision": str(precision), "integration_changes": changes,
     "scope": "Nonproduct incoming source for every odd multiplier; all fixed nonordinary odd multiples of three and even degrees0,4mod6 plus2. Fixed f1 degree5/8 and fixed f0 odd11 remain."}
(agent / "outputs/arbitrary_odd_neighbors_promotion.json").write_text(json.dumps(r, indent=2) + "\n")
with (agent / "CHECK_EVENTS_post_CP16.tsv").open("a", newline="") as f:
    writer = csv.writer(f, delimiter="\t")
    for label in labels:
        writer.writerow([label, now, "/root/monodromy", "PROMOTED-root-OC-full-proof-source-PASS", r["scope"]])
with (agent / "post_CP16_notes.md").open("a") as f:
    f.write("\n## " + now + " — Arbitrary odd nonproduct neighbours promoted\n\n"
            "The exact candidate and initial arithmetic wording remain preserved. Full scheme-theoretic dual-kernel connectedness is explicitly proved, "
            "rather than attributed to the weaker exercise statement. Unique mixed elliptic axes and their common principal degree imply at most one bad "
            "product quotient at each odd prime. Composition and polarized duality give every incoming odd multiplier. Root and OC full proof/source "
            "audits passed; no numerical check was necessary. Consolidation and CP27 preflight are wired with prior bytes and diffs retained.\n")
print(json.dumps(r, indent=2))
