"""One authorized promotion/include operation after complete independent audits.

This changes statuses and preserves candidates, exact prior shared files and diffs.
It does not build, refresh current tables, or run a checkpoint finalizer.
"""
from pathlib import Path
from datetime import datetime, timezone
import ast
import difflib
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / "agents/obstructions_crystals"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
specs = [
    {
        "name": "full_radical_structure",
        "candidate": "notes/A_full_radical_image_structure_candidate.tex",
        "sha256": "9d2e7f21840ef9025ee5c9a22d2f7ef5614876ccf55866d028697f6786b1d7f3",
        "canonical": "sections/A_full_radical_image_structure.tex",
        "count": 4,
        "audits": [
            "agents/obstructions_crystals/full_radical_image_structure_independent_audit.json",
            "agents/monodromy/outputs/independent_full_radical_image_structure_audit.json",
            "outputs/root_full_radical_image_structure_audit.json",
        ],
        "scope": "Exact pointwise-stabilizer and block structure; K remains undetermined. The root record is an author check; OC and monodromy are independent full proof audits.",
    },
    {
        "name": "Lang_polar_irreducibility",
        "candidate": "agents/obstructions_crystals/post_CP32_Lang_polar_irreducibility_candidate.tex",
        "sha256": "4226990b44304d3d26f45f20faad1f14046806fbb502318106f105860ac20058",
        "canonical": "agents/obstructions_crystals/A4_Lang_polar_irreducibility.tex",
        "count": 4,
        "audits": [
            "outputs/root_Lang_polar_irreducibility_audit.json",
            "agents/reduction_descent/outputs/independent_Lang_polar_irreducibility_audit.json",
            "agents/monodromy/outputs/independent_Lang_polar_irreducibility_audit.json",
        ],
        "scope": "Geometric irreducibility of the reduced Lang polar and the unique maximal-dual-rank Lang component; exceptional lower-rank components are not excluded.",
    },
    {
        "name": "Lang_main_orbit",
        "candidate": "agents/obstructions_crystals/post_CP32_Lang_main_orbit_candidate.tex",
        "sha256": "d3637b2c6536b126b86c70ec2ee13eb59547ba15e8d7e0005a9386ca38268d80",
        "canonical": "agents/obstructions_crystals/A4_Lang_main_orbit.tex",
        "count": 2,
        "audits": [
            "outputs/root_Lang_main_orbit_audit.json",
            "agents/reduction_descent/outputs/independent_Lang_main_orbit_audit.json",
        ],
        "scope": "The unique maximal-dual-rank component is the large orbit V minus K, of degree 2^r minus 2^dimK. No parity or K=0 conclusion.",
    },
]

# Validate every gate and destination before making any mutation.
for spec in specs:
    src = root / spec["candidate"]
    dest = root / spec["canonical"]
    assert sha(src) == spec["sha256"], spec["candidate"]
    assert not dest.exists(), spec["canonical"]
    labels = re.findall(r"\\label\{((?:lem|prop|cor|thm|rem):[^}]+)\}", src.read_text())
    assert len(labels) == spec["count"], (spec["name"], labels)
    spec["labels"] = labels
    for name in spec["audits"]:
        data = json.loads((root / name).read_text())
        assert "PASS" in data["status"].upper(), name
        seen_hashes = {
            v for k, v in data.items()
            if isinstance(v, str) and ("sha" in k.lower())
        }
        assert spec["sha256"] in seen_hashes, (name, seen_hashes)

consolidate = root / "code/consolidate.py"
old = consolidate.read_text()
anchor = "   out.write('\\n\\\\input{sections/A_nonordinary_ppav_covectors}\\n')\n"
assert old.count(anchor) == 1
assert all(Path(x["canonical"]).name not in old for x in specs)
addition = """   full_radical_structure=s/'A_full_radical_image_structure.tex'
   if full_radical_structure.exists() and '\\\\status{Candidate' not in full_radical_structure.read_text():
    out.write('\\n\\\\input{sections/A_full_radical_image_structure}\\n')
   lang_polar=a/'obstructions_crystals/A4_Lang_polar_irreducibility.tex'
   if lang_polar.exists() and '\\\\status{Candidate' not in lang_polar.read_text():
    out.write('\\n'+lang_polar.read_text()+'\\n')
   lang_main_orbit=a/'obstructions_crystals/A4_Lang_main_orbit.tex'
   if lang_main_orbit.exists() and '\\\\status{Candidate' not in lang_main_orbit.read_text():
    out.write('\\n'+lang_main_orbit.read_text()+'\\n')
"""
new = old.replace(anchor, anchor + addition)
ast.parse(new)
config = root / "notes/checkpoint33_promoted_inputs.json"
config_old = config.read_text()
inputs = json.loads(config_old)
assert isinstance(inputs, list)
ph2 = "agents/monodromy/birational_Pfaffian_height_two_counterexample.tex"
assert (root / ph2).exists() and "\\status{Candidate" not in (root / ph2).read_text()
for p in [x["canonical"] for x in specs] + [ph2]:
    if p not in inputs:
        inputs.append(p)
assert len(inputs) == len(set(inputs))

history = own / "notes/CP33_Lang_structure_promotion"
history.mkdir(exist_ok=False)
(history / "consolidate.before.py").write_bytes(consolidate.read_bytes())
(history / "checkpoint33_promoted_inputs.before.json").write_bytes(config.read_bytes())
now = datetime.now(timezone.utc).isoformat()
records = []
for spec in specs:
    src, dest = root / spec["candidate"], root / spec["canonical"]
    before = src.read_text()
    assert len(re.findall(r"\\status\{Candidate[^}]*\}", before)) == spec["count"]
    after = re.sub(r"\\status\{Candidate[^}]*\}", r"\\status{Proved; full independent proof audits passed.}", before)
    after = re.sub(r"\A%[^\n]*", "% Promoted after complete independent proof audits; exact candidate retained.", after)
    assert "\\status{Candidate" not in after
    (history / (spec["name"] + ".candidate.tex")).write_bytes(src.read_bytes())
    (history / (spec["name"] + ".diff")).write_text("".join(difflib.unified_diff(
        before.splitlines(True), after.splitlines(True), fromfile=spec["candidate"], tofile=spec["canonical"])))
    with dest.open("x") as f:
        f.write(after)
    record = {
        "status": "PROMOTED AFTER COMPLETE INDEPENDENT PROOF AUDITS",
        "actual_utc": now,
        **spec,
        "canonical_sha256": sha(dest),
        "changes": "Short proved statuses and initial provenance comment only; mathematical text unchanged.",
        "computation_scope": "No numerical computation needed or claimed for these direct proofs.",
    }
    records.append(record)
    with (own / (spec["name"] + "_promotion.json")).open("x") as f:
        json.dump(record, f, indent=2)
        f.write("\n")

consolidate.write_text(new)
config_new = json.dumps(inputs, indent=2) + "\n"
config.write_text(config_new)
(history / "consolidate.diff").write_text("".join(difflib.unified_diff(
    old.splitlines(True), new.splitlines(True), fromfile="consolidate.before.py", tofile="consolidate.py")))
(history / "checkpoint33_promoted_inputs.diff").write_text("".join(difflib.unified_diff(
    config_old.splitlines(True), config_new.splitlines(True), fromfile="inputs.before.json", tofile="inputs.json")))
for spec in specs:
    assert sha(root / spec["candidate"]) == spec["sha256"]
with (own / "CHECK_EVENTS.tsv").open("a") as f:
    for record in records:
        rp = "agents/obstructions_crystals/" + record["name"] + "_promotion.json"
        for label in record["labels"]:
            f.write("\t".join([now, label, "promotion_after_full_independent_audits", record["canonical"],
                              record["scope"], "PROVED; exact stated scope", rp]) + "\n")
with (own / "D_results.md").open("a") as f:
    f.write("\n\n## Exact group structure, irreducible Lang polar, and the main orbit — " + now + "\n\n")
    for record in records:
        f.write("`" + record["canonical"] + "`: " + record["scope"] + "\n\n")
    f.write("All mathematical candidate text is retained unchanged. The coordinated include and CP33-input edit preserves the exact prior files and diffs. No build, current-table refresh, or checkpoint finalizer was executed.\n")
result = {"status": "PASS", "actual_utc": now, "promotions": records,
          "checkpoint33_inputs": inputs, "history": str(history.relative_to(root)),
          "consolidate_sha256": sha(consolidate), "config_sha256": sha(config)}
with (own / "CP33_Lang_structure_promotion.json").open("x") as f:
    json.dump(result, f, indent=2)
    f.write("\n")
print(json.dumps({"status": result["status"], "actual_utc": now,
                  "canonicals": [{"path": r["canonical"], "sha256": r["canonical_sha256"]} for r in records],
                  "config": "notes/checkpoint33_promoted_inputs.json", "history": result["history"]}, indent=2))
