"""Document the completed five-source early-notice route; no new source read."""
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
row = next(r for r in rows if r["route"] == "Original 1951 Comptes rendus announcement (AG5)")
row["route"] = "Early original notices and Bourbaki revisions (AG4, AG5, AG14, AG65, AG67)"
row["evidence"] = "Algebra visually read all 30 original text pages across the five advertised originals: AG4 pp839-841, AG5 pp1556-1558, AG14 pp158-160, Bourbaki69 pp193-200 and Bourbaki113 pp127-139. Geometry independently read all three AG5 pages; root checked p1557. AG5 announces general Hilbert genus zero without proof and promises detailed treatment elsewhere; its starred presentation date is 3 December 1951. Both Bourbaki texts end June1957, distinct from their seminar headers."
row["failed_step"] = "The other notices concern locally convex or Lp spaces, nuclear-space determinants, singular values, normal-operator traces and determinant inequalities. None identifies the particular cote1 proof or a dated enclosure; AG5 establishes an earlier announcement, not the manuscript date. First seminar printings were not collated."
row["record"] = "notes/algebra_earlynotices_source_audit.md; notes/algebra_earlynotices_query_manifest.json; logs/geometry_history_1951_update.json"
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Documentation only; no mathematical movement or new source reading", "source_note_read": "notes/algebra_earlynotices_source_audit.md", "routes": len(rows), "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
(root / "logs/geometry_route_index_earlynotices_update.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
