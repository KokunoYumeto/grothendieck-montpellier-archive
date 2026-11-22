"""Index the completed, explicitly partial Krein custodial-survey route."""
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
route = "Krein correspondence: original custodial survey and inventory lead"
assert not any(r["route"] == route for r in rows)
rows.append({"route": route,
    "evidence": "Root read the original Yurii Bulgakov survey's returned header and partial text pp.651-657, ending mid-spread; no visual PDF collation. It identifies Institute of Archival Studies fonds346 inventory3, 319 files/1118 documents1943-1989, including six Gohberg letters1957-1969.",
    "failed_step": "Pages658-659 and all underlying letters remain unread. Further web opens/finds timed out; the local request returned522 and produced no PDF, extraction, images or hash. Failed finds do not certify zero hits. No opened passage identifies the target proof or dates the leaves; similarly numbered unrelated fonds were excluded.",
    "next_step": "A publicly inspectable original inventory or named Gohberg letter identifying a supplied proof/enclosure, or the unread end of the survey; date ranges alone are insufficient.",
    "record": "notes/root_krein_correspondence_date_audit.md; logs/root_krein_source_record22.json"})
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Documentation-only route index update; no new source reading or mathematical movement", "routes": len(rows), "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
(root / "logs/geometry_route_index_krein_update.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
