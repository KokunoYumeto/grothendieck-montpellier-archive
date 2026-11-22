"""Static creation preflight and guide update; creates no archive or estimate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import importlib.util
import json

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("packager", root / "code/geometry_final_package.py")
packager = importlib.util.module_from_spec(spec)
spec.loader.exec_module(packager)
included, _ = packager.current_inventory(detailed_omissions=False)
paths = {str(relative): path for relative, path in included}
required = ["checkpoint_history.json", "logs/root_checkpoint06_receipt.json", "logs/root_checkpoint06_receipt.txt", "logs/checkpoint06_creation.txt", "notes/geometry_final_package_README.md", "code/restore_checkpoint_from_final.py", "PROGRESS_LEDGER.md", "REPORT.md", "RESULTS.csv", "CHECK_EVENTS.tsv", "CORRECTIONS.tsv", "paper.tex", "paper.pdf", "references.bib"]
assert all(name in paths for name in required), [name for name in required if name not in paths]
history = json.loads(paths["checkpoint_history.json"].read_text())
assert [row["checkpoint"] for row in history] == [1, 2, 3, 4, 5, 6]
assert history[-1]["library_file_id"] == "libfile_ebacd78ffe708191b77c010a5b852403"
assert [number for number, _ in packager.checkpoint_paths()] == [1, 2, 3, 4, 5, 6]
guide_path = root / "notes/geometry_final_package_README.md"
guide = guide_path.read_text()
before = hashlib.sha256(guide_path.read_bytes()).hexdigest()
anchor = "## Preservation and deduplication\n"
assert guide.count(anchor) == 1 and "## Checkpoints 01–06: refreshed preparation audit" not in guide
section = """## Checkpoints 01–06: refreshed preparation audit

The 04:40:42 UTC plan includes **all six checkpoints**, with respectively
106, 256, 473, 1,240, 2,125 and 2,573 original member entries: **6,773
historical entries in total**. That snapshot also contains 2,575 current
logical files and 2,645 canonical regular-file payloads. Its estimate is
**287,607,776 bytes**, or **289,607,776 bytes with reserve**, leaving
**210,392,224 bytes** below the 500,000,000-byte limit.

The 04:41:28 UTC audit independently checked the six actual checkpoint ZIP
hashes and every one of their 6,773 original file payloads against the new
restoration mapping. See `notes/geometry_final_package_audit_cp06.md`,
`notes/geometry_final_package_plan_cp06.json`,
`notes/geometry_final_package_estimate_cp06.json` and
`logs/geometry_restore_checkpoint_mapping_cp06.json`. No final ZIP or
restored tree was created during that audit. Earlier snapshots remain
available under their dated names.

The current `checkpoint_history.json` records all six saved checkpoints,
including checkpoint 06's delivery receipt. That file and the receipt and
creation records under `logs/` are ordinary included current files. Final
creation discovers the then-current report, ledger, receipts and logs
afresh; the preparation estimates are never substituted for that fresh
inventory. The final creation result and any later delivery receipt are
produced after the immutable archive is written and must be retained
separately rather than written into the frozen tree during creation.

"""
guide_path.write_text(guide.replace(anchor, section + anchor, 1))
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Static packaging preflight and guide clarification; no mathematical movement", "archive_creation_invoked": False, "fresh_estimate_invoked": False, "checkpoint_numbers": [row["checkpoint"] for row in history], "cp06_receipt_in_current_history": True, "required_current_files_included": required, "included_current_log_count": sum(name.startswith("logs/") for name in paths), "guide_before_sha256": before, "guide_after_sha256": hashlib.sha256(guide_path.read_bytes()).hexdigest(), "packager_sha256": hashlib.sha256((root / "code/geometry_final_package.py").read_bytes()).hexdigest(), "root_creation_command_after_freeze": "python /workspace/scratch/a7ef7e55112c/RESEARCH_SA23/code/geometry_final_package.py --create-final /workspace/scratch/a7ef7e55112c/RESEARCH_SA23_final.zip > /workspace/scratch/a7ef7e55112c/RESEARCH_SA23_final_creation.json 2> /workspace/scratch/a7ef7e55112c/RESEARCH_SA23_final_creation.stderr.txt", "postcreation_list_command": "python /workspace/scratch/a7ef7e55112c/RESEARCH_SA23/code/restore_checkpoint_from_final.py /workspace/scratch/a7ef7e55112c/RESEARCH_SA23_final.zip --list > /workspace/scratch/a7ef7e55112c/RESEARCH_SA23_final_inventory.json", "postcreation_independent_check": "Read actual final manifest/member inventory once; confirm six checkpoint counts and canonical recovery mappings, current receipt/log paths, size and verified creation receipt. Do not repeat all historical source-payload checks."}
(root / "logs/geometry_final_package_static_preflight.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
