"""Index the Russian book audit and close exact Kansas/search-route details."""
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
kansas = next(r for r in rows if r["route"] == "Kansas: Aronszajn and G. Baley Price public inventories")
kansas["failed_step"] = kansas["failed_step"].replace("after its repository link timed out", "after the web-reader timeout and one ordinary retrieval returning404 without redirects")
krein = next(r for r in rows if r["route"] == "Krein correspondence: original custodial survey and inventory lead")
krein["record"] += "; notes/algebra_gohberg_lidskii_followup_search.md"
route = "Dunford-Schwartz II: original Russian 1966 edition"
assert not any(r["route"] == route for r in rows)
rows.append({"route": route,
    "evidence": "Algebra retrieved the advertised EqWorld original Russian scan and visually read title/imprint1-3, prefaces5-8, complete Fredholm historical subsection328-330, indexed Lidskii passages753/755, complete Grothendieck and Lidskii bibliography entries970-971/993-994, selected index/contents pages and colophon1064. The Russian editor says historical notes were added.",
    "failed_step": "Inspected passages supply ordinary publication references, not a dated proof, letter, enclosure or cote1 identification. The English1963 body and the uninspected remainder of this1064-page edition remain unread; translation additions and literal bibliography date errors are not transferred to the French originals or the target sheets.",
    "next_step": "A specific original historical note or dated communication identifying receipt of the particular proof; edition or printing dates and ordinary publication references are insufficient.",
    "record": "notes/algebra_dunford_ru1966_source_audit.md; notes/algebra_dunford_ru1966_manifest.json; notes/algebra_gohberg_lidskii_followup_search.md"})
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Documentation-only index completion; no new source reading or mathematical movement", "routes": len(rows), "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "updates": ["Kansas official handle404 supplement", "Krein discovery-query provenance", "Original Russian Dunford-SchwartzII bounded reading"]}
(root / "logs/geometry_route_index_translation_completion.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
