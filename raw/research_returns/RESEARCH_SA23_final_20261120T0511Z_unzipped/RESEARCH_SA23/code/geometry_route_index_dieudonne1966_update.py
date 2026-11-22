"""Record the completed original Dieudonne 1966 appreciation route."""
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
route = "Dieudonné 1966 ICM original appreciation"
assert not any(r["route"] == route for r in rows)
rows.append({"route": route,
    "evidence": "Algebra retrieved the official IMU proceedings facsimile and individually read all four article pages21-24 plus title/imprint pages. The 1966 congress volume was published by Mir in1968. Page24 second paragraph gives a broad1950-55 recollection of topological-vector-space memoirs and nuclear spaces; the final Hilbert comparison concerns mathematical style.",
    "failed_step": "No Hilbert operator trace/genus-zero claim, distinctive proof, letter, enclosure or identification of the cote1 sheets appears in the four-page article. The broad career period does not date those leaves. Earlier Dieudonné1989 and Serre1965 routes were not repeated.",
    "next_step": "An original first-person report, letter or dated enclosure explicitly identifying the particular proof sheets rather than a general research period.",
    "record": "notes/algebra_dieudonne1966_source_audit.md; notes/algebra_dieudonne_query_manifest.json"})
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Documentation-only route index update; no new source reading or mathematical movement", "routes": len(rows), "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
(root / "logs/geometry_route_index_dieudonne1966_update.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
