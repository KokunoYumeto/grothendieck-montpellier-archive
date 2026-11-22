"""Complete the last reported catalogue route and freeze the geometry index."""
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
krein = next(r for r in rows if r["route"] == "Krein correspondence: original custodial survey and inventory lead")
krein["failed_step"] += " The distinct 2012 Archives of Ukraine PDF returned403 and was not retried; the National Memory PDF timed out in the web reader, with no local retrieval. Both originals remain unopened."
route = "Krein autographed-book catalogue and possible dated inscriptions"
assert not any(r["route"] == route for r in rows)
rows.append({"route": route,
    "evidence": "Root read NBUV and national-library search-result metadata for the Rikun catalogue, scientific editor Ю. Й. Черський, Odessa2000,60 pages, shelfmarks ВА597677 and А599330. A separate Rikun method-guide search excerpt mentions the catalogue. No original catalogue or inscription was read.",
    "failed_step": "The NBUV catalogue-page opening timed out; the official method-guide PDF timed out in the web reader and returned503 on one ordinary request, producing no PDF/text. Metadata and failed access give no target inscription, proof/enclosure identification or sheet date; no absence claim is made about the originals.",
    "next_step": "A publicly inspectable catalogue entry, inscription or associated enclosure explicitly identifying the particular proof; a generic gift inscription or publication date alone would not decide the gate.",
    "record": "notes/root_krein_correspondence_date_audit.md; logs/root_krein_autographs23.json; notes/root_history_web82.json; notes/root_history_web86.json"})
assert len({row["route"] for row in rows}) == len(rows)
assert all(set(row) == set(fields) and all(row.values()) for row in rows)
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Final documentation-only route update and geometry write freeze; no new source reading or mathematical movement", "routes": len(rows), "unique_routes": True, "five_columns_complete": True, "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "geometry_files_frozen_after_this_record": True, "next_authorized_operation": "Read-only actual final-ZIP manifest audit, writing its output outside the frozen tree after root reports creation"}
(root / "logs/geometry_route_index_final_freeze.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(record, ensure_ascii=False))
