#!/usr/bin/env python3
"""Parent-authorized narrow CCI promotion after two complete proof audits."""
from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json
import re

agent = Path(__file__).resolve().parents[1]
root = agent.parents[1]
candidate = agent / "post_CP33_compatible_cyclic_intermediates_candidate.tex"
canonical = agent / "compatible_cyclic_intermediates.tex"
expected = "a40f648e4c968f2b3a2cd105b4866d7ba992361b46de9b62a514ff77535103ae"
digest = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert digest(candidate) == expected and not canonical.exists()
audits = [root / "outputs/root_compatible_cyclic_intermediates_audit.json",
          root / "agents/obstructions_crystals/compatible_cyclic_intermediates_independent_audit.json"]
for audit in audits:
    assert expected in audit.read_text() and "PASS" in audit.read_text()

before = candidate.read_text()
after, count = re.subn(r"\\status\{Candidate[^}]*\}",
    lambda _: r"\status{Proved; independent audits passed.}", before)
assert count == 5
after = after.replace(
    "% Isolated post-CP33 candidate. No canonical or shared-input mutation.",
    "% Promoted after complete independent root and obstruction/crystal proof audits."
)
after = after.replace(
    "No numerical experiment or new external theorem is used here.",
    "No numerical experiment or new external theorem is used here. "
    "The complete proof was independently rederived by the root and "
    "obstruction/crystal reviewers; their full passes were recorded on "
    "20 November 2026 at 03:59:09 and 04:02:19 UTC, respectively. "
    "The exact candidate and audit records are retained."
)
history = agent / "notes/CP34_compatible_intermediates_promotion"
history.mkdir(parents=True, exist_ok=True)
(history / "candidate.tex").write_text(before)
(history / "promotion.diff").write_text("".join(difflib.unified_diff(
    before.splitlines(True), after.splitlines(True),
    fromfile=str(candidate.relative_to(root)), tofile=str(canonical.relative_to(root)))))

consolidate = root / "code/consolidate.py"
shared_before = consolidate.read_text()
anchor = "    out.write('\\n'+general_odd_source.read_text()+'\\n')\n"
assert shared_before.count(anchor) == 1 and canonical.name not in shared_before
addition = (
    "   compatible_intermediates=a/'monodromy/compatible_cyclic_intermediates.tex'\n"
    "   if compatible_intermediates.exists() and '\\\\status{Candidate' not in compatible_intermediates.read_text():\n"
    "    out.write('\\n'+compatible_intermediates.read_text()+'\\n')\n"
)
shared_after = shared_before.replace(anchor, anchor + addition)
config = root / "notes/checkpoint34_promoted_inputs.json"
config_before = config.read_text()
inputs = json.loads(config_before)
path = str(canonical.relative_to(root))
assert path not in inputs
position = inputs.index("agents/obstructions_crystals/A4_general_odd_source_Cartier.tex") + 1
inputs.insert(position, path)
config_after = json.dumps(inputs, indent=2) + "\n"
for name, prior, final in [("consolidate.py", shared_before, shared_after),
                           ("checkpoint34_promoted_inputs.json", config_before, config_after)]:
    (history / ("prior_" + name)).write_text(prior)
    (history / (name + ".diff")).write_text("".join(difflib.unified_diff(
        prior.splitlines(True), final.splitlines(True), fromfile="retained-prior/"+name,
        tofile=name)))

canonical.write_text(after)
consolidate.write_text(shared_after)
config.write_text(config_after)
now = datetime.now(timezone.utc).isoformat()
labels = re.findall(r"\\label\{([^}]+)\}", before)
record = {"status":"PROMOTED", "actual_utc":now,
          "candidate":str(candidate.relative_to(root)), "candidate_sha256":expected,
          "canonical":path, "canonical_sha256":digest(canonical),
          "labels":labels, "audits":[str(p.relative_to(root)) for p in audits],
          "consolidate_sha256":digest(consolidate), "config_sha256":digest(config),
          "scope":"Conditional compatible-intermediate criterion; full type(1,ell) cubic source images remain explicit unproved hypotheses. No new unconditional degree.",
          "new_computation":False}
(agent / "outputs/compatible_cyclic_intermediates_promotion.json").write_text(
    json.dumps(record, indent=2) + "\n")
with (agent / "CHECK_EVENTS_post_CP16.tsv").open("a") as stream:
    for label in labels:
        if not label.startswith("subsec:"):
            stream.write("\t".join([label,now,"/root/monodromy",
                "PROMOTED-ROOT-OC-FULL-PROOF-PASS",record["scope"]])+"\n")
assert digest(candidate) == expected
print(json.dumps(record, indent=2))
