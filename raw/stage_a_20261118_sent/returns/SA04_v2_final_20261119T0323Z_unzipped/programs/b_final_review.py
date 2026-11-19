"""Preserve manually source-checked locator proposals and structural final checks.

No mathematical verdict or reading is inferred by this program.  It does not
change root or final registers.  The replacements below were chosen after
reading the numbered source passages; only the directions were edited directly
with the root agent's explicit authorization.
"""
from pathlib import Path
import ast
import csv
import datetime
import json
import re

WORK = Path(__file__).resolve().parents[1]
DEST = WORK / "parts/b"
FINAL = WORK / "final"

locator_decisions = [
    ("codex/K93-11_transcription.tex:ordinary normal form", "codex/K93-11_transcription.tex:5–11", "The ordinary characteristic-two equation is on line7."),
    ("codex/K93-10_transcription.tex:Proposition6.1 proof", "codex/K93-10_transcription.tex:394–400", "Both references to equation(6.2) occur in this proof range."),
    ("codex/K93-10_transcription.tex:duality paragraph", "codex/K93-10_transcription.tex:121", "The duality display is on line121."),
    ("codex/K93-02_transcription.tex:final factorization", "codex/K93-02_transcription.tex:222–224", "The intervening differential and Delta-prime domain are displayed together."),
    ("codex/K93-02_transcription.tex:Gauss–Manin spectral sequence", "codex/K93-02_transcription.tex:272–286", "The p-minus-one target is on274; the later p-plus-one formula is on282."),
    ("codex/K93-03_transcription.tex:base differential expression", "codex/K93-03_transcription.tex:27–33", "Both base connection expressions occur in this range."),
    ("codex/K93-03_transcription.tex:Cartier canonical map", "codex/K93-03_transcription.tex:165–200", "The Z-valued construction, ring-map assertion, and cohomology quotient are retained together."),
    ("codex/K93-03_transcription.tex:Cartier splitting", "codex/K93-03_transcription.tex:239–247", "The splitting and subsequent canonical cohomology inverse occur here."),
    ("codex/K93-03_transcription.tex:Cartier axioms", "codex/K93-03_transcription.tex:258–278", "The closed-form axiom is on264 and the uniqueness claim on278."),
    ("codex/K93-03_transcription.tex:p-curvature tensor target", "codex/K93-03_transcription.tex:387–407", "Both displayed ordinary tensor-power targets are included."),
    ("codex/K93-04_transcription.tex:determinant paragraph", "codex/K93-04_transcription.tex:214–219", "The determinant-one assertion is on219."),
    ("codex/K93-04_transcription.tex:imperfect-field conic paragraph", "codex/K93-04_transcription.tex:208–212", "The universally quantified imperfect-field example is on212."),
]

with (WORK / "parts/root/readings.tsv").open() as f:
    reader = csv.DictReader(f, delimiter="\t")
    fields = reader.fieldnames
    original = list(reader)
replacement_map = {old: (new, explanation) for old, new, explanation in locator_decisions}
patches = []
corrected = []
for physical_row, row in enumerate(original, 2):
    updated = dict(row)
    if row["line"] in replacement_map:
        new, explanation = replacement_map[row["line"]]
        patches.append({"root_tsv_row": physical_row, "cote": row["cote"], "scan": row["scan"], "old_line": row["line"], "new_line": new, "source_check": explanation})
        updated["line"] = new
    corrected.append(updated)
assert len(patches) == 12, "Root readings changed: review patch alignment before applying."
with (DEST / "root_reading_locator_patch.tsv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(patches[0]), delimiter="\t")
    writer.writeheader()
    writer.writerows(patches)
with (DEST / "root_reading_rows_corrected.tsv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
    writer.writeheader()
    writer.writerows(corrected)

pro = "pro/MPL_93_047-091_transcription.tex:"
second = "pro/MPL_93_221-236+161-5_transcription.tex:"
item_locator_decisions = {
    268: [pro + "990–1095;1149–1205;1429–1597", "codex/K93-01_transcription.tex:2–273"],
    269: [pro + "990–1095;1149–1205", "codex/K93-01_transcription.tex:274–630", "codex/K93-02_transcription.tex:2–231"],
    270: [pro + "2–51", "codex/K93-02_transcription.tex:232–322", "codex/K93-03_transcription.tex:2–105"],
    271: [pro + "713–982", "codex/K93-03_transcription.tex:114–357"],
    272: [pro + "713–982", "codex/K93-05_transcription.tex:10–112"],
    273: [pro + "713–982", "codex/K93-05_transcription.tex:113–249"],
    274: [pro + "1055–1090", "codex/K93-05_transcription.tex:250–294", "codex/K93-06_transcription.tex:2–231"],
    275: [pro + "1055–1090;2111–2254", "codex/K93-06_transcription.tex:232–404"],
    276: ["codex/K93-06_transcription.tex:405–432"],
    277: [pro + "713–982;1206–1597", second + "31–223"],
    278: [pro + "2217–2254", second + "224–315"],
    279: [pro + "2–51", second + "318–461"],
}
items = json.loads((FINAL / "SA04_items.json").read_text())
by_item = {item["id"]: item for item in items}
item_patches = []
for number, new in item_locator_decisions.items():
    item_id = f"SA04-{number}"
    item_patches.append({"item_id": item_id, "old_lines_json": json.dumps(by_item[item_id]["lines"], ensure_ascii=False), "new_lines_json": json.dumps(new, ensure_ascii=False), "reason": "Expand the existing source/target locator; no change to the item's statement or verdict."})
with (DEST / "cross_reference_item_locator_patch.tsv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(item_patches[0]), delimiter="\t")
    writer.writeheader()
    writer.writerows(item_patches)

claims = json.loads((FINAL / "SA04_claims.json").read_text())
problems = json.loads((FINAL / "SA04_problems.json").read_text())
known = {row["id"] for rows in (items, claims, problems) for row in rows}
text = (FINAL / "SA04_directions.md").read_text()
sections = re.split(r"^## (\d+)\. ", text, flags=re.M)
direction_results = []
for index in range(1, len(sections), 2):
    number = int(sections[index])
    section = sections[index + 1]
    ids = set(re.findall(r"\b(?:MP-|C-)?SA04-\d+\b", section))
    required_fields = ["**Starting records:**", "**Provenance:**", "**Establish:**", "**Known limits:**", "**First step:**", f"Interest {number};", "feasibility"]
    direction_results.append({"rank": number, "unknown_ids": sorted(ids - known), "has_item": any(re.fullmatch(r"SA04-\d+", x) for x in ids), "has_claim": any(x.startswith("C-") for x in ids), "has_problem": any(x.startswith("MP-") for x in ids), "missing_fields": [x for x in required_fields if x not in section]})
assert [row["rank"] for row in direction_results] == list(range(1, 31))
assert all(not row["unknown_ids"] and not row["missing_fields"] and row["has_item"] and row["has_claim"] and row["has_problem"] for row in direction_results)

root_items = json.loads((WORK / "parts/root/items.json").read_text())
manifest = json.loads((FINAL / "SOURCE_MANIFEST.json").read_text())
bad_markers = [{"file": row["file"], "marker": marker} for row in manifest for marker in row.get("scan_markers", []) if not marker["scan"].isdigit()]
alias_dict = {}
for node in ast.walk(ast.parse((WORK / "programs/assemble.py").read_text())):
    if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "ref_alias" for target in node.targets):
        alias_dict = ast.literal_eval(node.value)
old_ref_occurrences = []
for row in claims:
    for key, value in row.items():
        if not isinstance(value, str):
            continue
        for old, new in alias_dict.items():
            if re.search(r"(?<![\w-])" + re.escape(old) + r"(?![\w-])", value):
                old_ref_occurrences.append({"claim": row["id"], "field": key, "old": old, "canonical": new})
proof_programs = ["a_computations", "b_computations", "b_supplement_computations", "b_tits_check", "c_computations", "c_manin_check", "c_review_genus2", "root_computations", "root_git_computation"]
computation_output_check = {name: {"program": (WORK / "programs" / (name + ".py")).exists(), "saved_outputs": [str(p.relative_to(WORK)) for p in sorted((WORK / "outputs").glob(name + ".*"))]} for name in proof_programs}
absolute_workspace_programs = [p.name for p in sorted((WORK / "programs").glob("*.py")) if "/workspace/scratch/594d1dc856a9" in p.read_text()]
result = {
    "review_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "scope": "Structural final checks and preservation of manually source-checked locator proposals; no new mathematical verdicts.",
    "root_reading_locator_patches": len(patches),
    "cross_reference_item_locator_patches": len(item_patches),
    "directions": len(direction_results),
    "direction_details": direction_results,
    "active_direction_unknown_ids": sorted({item for row in direction_results for item in row["unknown_ids"]}),
    "introductory_aliases": {"C-SA04-217": "C-SA04-122", "MP-SA04-201": "MP-SA04-164", "MP-SA04-204": "MP-SA04-168"},
    "root_unindexed_items": len(root_items),
    "root_items_with_empty_sources": sum(not row["sources"] for row in root_items),
    "root_items_missing_locators": [row["id"] for row in root_items if not row.get("lines")],
    "manifest_non_numeric_scan_markers": bad_markers,
    "free_text_old_reference_keys": old_ref_occurrences,
    "checked_computation_programs_and_outputs": computation_output_check,
    "absolute_workspace_programs": absolute_workspace_programs,
    "assembly_pending_at_review": [name for name in ("SA04_dossier.md", "progress.log") if not (FINAL / name).exists()],
}
out = WORK / "outputs/b_final_review.json"
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
summary = {key: value for key, value in result.items() if key not in {"direction_details", "checked_computation_programs_and_outputs", "absolute_workspace_programs"}}
summary["absolute_workspace_program_count"] = len(absolute_workspace_programs)
summary["checked_computation_program_count"] = len(proof_programs)
summary["computation_programs_missing_saved_output"] = [name for name, row in computation_output_check.items() if not row["saved_outputs"]]
stdout = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
(WORK / "outputs/b_final_review_stdout.json").write_text(stdout)
print(stdout, end="")
