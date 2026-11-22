"""Index the completed Kadison records and early-publication date route."""
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
route = "Kadison public finding aids and original early communications"
assert not any(r["route"] == route for r in rows)
rows.append({"route": route,
    "evidence": "Algebra read exact public entries Penn UPF8.5 box72 folder8, IAS SM box14 folder5 and IAS DO.MEMBERS box70; underlying letters were not opened. Original Fuglede-Kadison1951 pp.425,430,431 and 1952 pp.520,525,530 were visually checked with complete-text searches; every original Kadison1955 report page4-10 was visually read.",
    "failed_step": "No dated Grothendieck supplied proof, enclosure or cote1 identification was found in the opened scopes. Finite-factor trace/determinant statements are distinct from the target Hilbert trace-class proof. Later local IAS preservation requests and Penn publications returned403 and were stopped; no original correspondence was obtained.",
    "next_step": "A public item-level correspondence description or original dated letter explicitly identifying the particular proof; unexamined administrative or biographical folders do not establish such content.",
    "record": "notes/algebra_kadison_source_search.md; notes/algebra_kadison_query_manifest.json"})
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Documentation-only route index update; no new source reading or mathematical movement", "routes": len(rows), "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
(root / "logs/geometry_route_index_kadison_update.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
