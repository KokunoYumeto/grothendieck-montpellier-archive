"""Index the completed Aronszajn/Price public-inventory route with limits."""
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
route = "Kansas: Aronszajn and G. Baley Price public inventories"
assert not any(r["route"] == route for r in rows)
rows.append({"route": route,
    "evidence": "Category read Aronszajn PP236 resource11 and all five leaf descriptions: three correspondence boxes A-J/K-M/N-Z, publications/index, and notes/documents. No digital instances are advertised. For Price resource3239, all fourteen public waypoints and263 titles were read, with nine selected descriptions and four individual webpages inspected.",
    "failed_step": "Only catalogue metadata was read; no original Aronszajn or Price letter/notebook/enclosure was opened. Coarse descriptions identify no target proof or date. Reset searches and404 submissions were not treated as zero hits. The1976 department-history book remained unread after its repository link timed out.",
    "next_step": "A dated original or public item-level identification in PP236 Box1 A-J correspondence, the relevant Price correspondence/history folders, or a dated duplicate explicitly matching the proof; collection date ranges do not date the Montpellier leaves.",
    "record": "notes/category_aronszajn_kansas_date_audit.md; notes/category_price_inventory_titles.tsv; logs/category_price_public_inventory.json"})
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Documentation-only route index update; no new source reading or mathematical movement", "routes": len(rows), "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
(root / "logs/geometry_route_index_kansas_update.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
