"""Promote only the exact independently audited nine-theta proof."""
from datetime import datetime, timezone
from pathlib import Path
import csv
import difflib
import hashlib
import json

agent = Path(__file__).resolve().parents[1]
work = agent.parents[1]
candidate = agent / "nonordinary_nine_theta_norm_transfer_candidate.tex"
expected = "aacebbc578d130a62ef4413cece1c89a2dc4ac581bbbe3f3a504fcacc0368ca9"
assert hashlib.sha256(candidate.read_bytes()).hexdigest() == expected
root_audit = work / "outputs/root_nine_theta_transfer_audit.json"
companion_audit = agent.parent / "obstructions_crystals/nine_theta_norm_transfer_independent_audit.json"
assert root_audit.is_file() and companion_audit.is_file()
assert json.loads(root_audit.read_text())["candidate_sha256"] == expected
canonical = agent / "nonordinary_nine_theta_norm_transfer.tex"
assert not canonical.exists()
source = candidate.read_text()
source = source.replace(
    "% Post-CP26 isolated candidate. No claim is promoted before full audits.",
    "% Post-CP26 theorem; exact fully audited candidate retained separately.")
source = source.replace(
    "\\status{Candidate; complete proof submitted for independent audit.}",
    "\\status{Proved and independently checked.}")
assert source.count("\\textup{[Candidate.]}") == 7
source = source.replace("\\textup{[Candidate.]}",
                        "\\textup{[Proved; independent audits passed.]}")
source = source.replace(
    "monodromy by the proved cubic-section quasireflexivity/jet lemma.",
    "monodromy by\nLemma~\\ref{lem:nonordinary-ppav-two-lifted-intersections-candidate}.")
source = source.replace("This theorem would not classify every odd degree:",
                        "This theorem does not classify every odd degree:")
source = source.replace(
    "The proof must\nreceive full independent audits before any promotion; the raw\npre-archive outline and unrelated norm-eleven experiments remain\nretained separately.",
    "The raw pre-archive outline, the exact audited candidate, and\n"
    "unrelated norm-eleven experiments remain retained separately.\n"
    "The complete parent proof/dependency/code audit passed at\n"
    "22:33:07 UTC, and the complete obstruction/crystal audit passed\n"
    "at 22:32:21 UTC on 19 November 2026. Their independent exact\n"
    "graph reruns took $0.306819334$ and $0.322610496$ seconds,\n"
    "respectively, with the author output preserved. No new\n"
    "classification-source or geometric computation is claimed by\n"
    "these bounded graph runs.")
canonical.write_text(source)
now = datetime.now(timezone.utc).isoformat()
labels = [
    "lem:nine-theta-clean-cubic-contacts-candidate",
    "lem:nine-theta-node-product-candidate",
    "lem:nine-theta-weighted-graph-candidate",
    "prop:nine-theta-full-gluing-candidate",
    "thm:nine-theta-arbitrary-odd-norm-candidate",
    "cor:f0-all-even-nine-theta-transfer-candidate",
    "rem:nine-theta-transfer-scope-candidate",
]
changes = []
for relative, old, new in [
    ("code/consolidate.py",
     "                  'monodromy/nonordinary_rank_one_bad_five_kernel.tex']:",
     "                  'monodromy/nonordinary_rank_one_bad_five_kernel.tex',\n"
     "                  'monodromy/nonordinary_nine_theta_norm_transfer.tex']:"),
    ("code/prepare_checkpoint27.py",
     "for rel in required:\n",
     "required.append('agents/monodromy/nonordinary_nine_theta_norm_transfer.tex')\n"
     "for rel in required:\n"),
]:
    path = work / relative
    before = path.read_text()
    assert before.count(old) == 1, relative
    backup = agent / "history" / ("pre_nine_theta_" + relative.replace("/", "__"))
    assert not backup.exists()
    backup.write_text(before)
    after = before.replace(old, new)
    path.write_text(after)
    difference = "".join(difflib.unified_diff(
        before.splitlines(True), after.splitlines(True),
        fromfile=backup.name, tofile=relative))
    diff_path = backup.with_name(backup.name + ".diff")
    diff_path.write_text(difference)
    changes.append({"file": relative, "prior": str(backup), "diff": str(diff_path)})

record = {
    "status": "PROMOTED", "actual_utc": now,
    "candidate": str(candidate), "candidate_sha256": expected,
    "canonical": str(canonical),
    "canonical_sha256": hashlib.sha256(canonical.read_bytes()).hexdigest(),
    "labels": labels, "root_audit": str(root_audit),
    "companion_audit": str(companion_audit), "integration_changes": changes,
    "scope": "Arbitrary odd norm transfer from nine theta; every fixed f0 odd degree divisible by three and every even degree. Fixed f0 odd11 and fixed f1 odd5 remain separate.",
    "preservation": "Exact candidate and every prior draft, program, output and failure retained. Canonical changes status, explicit dependency locator and audit/scope wording only.",
}
(agent / "outputs/nine_theta_norm_transfer_promotion.json").write_text(json.dumps(record, indent=2) + "\n")
with (agent / "CHECK_EVENTS_post_CP16.tsv").open("a", newline="") as handle:
    writer = csv.writer(handle, delimiter="\t")
    for label in labels:
        writer.writerow([label, now, "/root/monodromy",
                         "PROMOTED-full-root-and-OC-proof-code-PASS",
                         record["scope"] + " " + str(canonical)])
with (agent / "post_CP16_notes.md").open("a") as handle:
    handle.write("\n## " + now + " — Nine-theta norm transfer promoted\n\n"
                 "The exact seven-label audited candidate and all earlier versions remain unchanged. "
                 "The canonical proof replaces the individual-theta nodality hypothesis with three movable cubic components. "
                 "All selected18-edge pair lifts and the72/90 stars are justified over the full normal Lang scheme, without identifying stable fibres at rank drop. "
                 "The complete root and OC audits passed. Every even degree on every fixed f0 principal surface is now proved; "
                 "the fixed f0 odd11 and fixed f1 odd5 gates remain. The bounded graph and5000-degree arithmetic checks are supplements only. "
                 "Consolidation and CP27 preflight now include the canonical file; exact prior bytes and diffs are retained.\n")
print(json.dumps(record, indent=2))
