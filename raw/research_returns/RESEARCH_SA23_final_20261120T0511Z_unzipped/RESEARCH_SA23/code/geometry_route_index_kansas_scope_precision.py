"""Root-authorized precision correction, preserving the earlier freeze record."""
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
path = root / "notes/manuscript_date_attempts.tsv"
before = hashlib.sha256(path.read_bytes()).hexdigest()
with path.open(newline="") as f:
    reader = csv.DictReader(f, delimiter="\t")
    fields, rows = reader.fieldnames, list(reader)
row = next(r for r in rows if r["route"] == "Kansas: Aronszajn and G. Baley Price public inventories")
old = "all fourteen public waypoints and263 titles were read, with nine selected descriptions and four individual webpages inspected"
new = "all fourteen public waypoints were retrieved and all 263 titles were read, with nine selected descriptions and four individual webpages inspected"
assert row["evidence"].count(old) == 1
row["evidence"] = row["evidence"].replace(old, new, 1)
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
freeze = root / "logs/geometry_route_index_final_freeze.json"
prior = root / "logs/geometry_route_index_final_freeze_initial.json"
with prior.open("xb") as stream:
    stream.write(freeze.read_bytes())
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Root-authorized documentation-only precision correction and renewed geometry write freeze", "correction": "Fourteen Price waypoints were retrieved; all263 titles were read, while complete descriptive reading was limited to nine selected descriptions and four individual record webpages. Machine search of all supplied metadata is not promoted to manual reading.", "routes": len(rows), "unique_routes": len({r["route"] for r in rows}) == len(rows), "five_columns_complete": all(set(r) == set(fields) and all(r.values()) for r in rows), "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "previous_freeze_record": str(prior.relative_to(root)), "geometry_files_frozen_after_this_record": True, "source_scope_or_date_gate_changed": False, "next_authorized_operation": "Read-only actual final-ZIP manifest audit, writing its output outside the frozen tree after root reports creation"}
freeze.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
(root / "logs/geometry_route_index_kansas_scope_precision.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(record, ensure_ascii=False))
