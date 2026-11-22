"""Index the completed bounded Schwartz first-person source route."""
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
route = "Schwartz first-person memoir, lectures and interview"
assert not any(r["route"] == route for r in rows)
rows.append({"route": route,
    "evidence": "Category read the complete Grothendieck memoir subsection pp.282-286 and adjacent p.287 in a public English transcription; full native text of the 1982 Patras lecture with opening/end visual collation; all four PDF pages of the 1994 Dieudonné recollection; and the complete Schwartz interview pp.1-6 in the publisher's free 2015 Bouleau edition.",
    "failed_step": "None of these passages identifies the target trace/genus-zero leaves or a dated enclosure. Tensor-product letters, Nancy recollections and an unrelated Dixmier trace passage do not date them. Original memoir scan was not collated; later pages of the 1981 Notice remain unread. Edition and transcription limits are explicit.",
    "next_step": "An original dated letter, lecture enclosure or specific first-person manuscript identification matching the target proof; consult the uncollated original memoir or remaining Notice only within that bounded question.",
    "record": "notes/category_schwartz_firstperson_date_audit.md"})
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Documentation-only route index update; no new source reading or mathematical movement", "routes": len(rows), "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
(root / "logs/geometry_route_index_schwartz_firstperson_update.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
