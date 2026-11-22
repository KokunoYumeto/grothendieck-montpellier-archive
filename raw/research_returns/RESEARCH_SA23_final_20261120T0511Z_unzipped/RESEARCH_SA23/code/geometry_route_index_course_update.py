"""Merge the bounded independent course-copy route into its existing family."""
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
row = next(r for r in rows if r["route"] == "Summa editorial / São Paulo course publications")
row["evidence"] = "Original Fredholm publication note and actual public course links checked; the Circle course link is a request notice. Distinct follow-up opened CiNii 1958 French second-edition and Google Books 1973 English-edition metadata only; neither exposed original preface or contents pages."
row["failed_step"] = "No original course, foreword, contents or Horváth1976 review pages opened. New official IME-USP index request and advertised AMS review returned403 and were stopped. Prior request-notice, dark Archive and denied Geotoppos routes were not retried. Secondary January1953 letter was not treated as an original; no content or sheet-date inference follows."
row["record"] = "notes/geometry_editorial_course_date_audit.md; notes/category_draft_crossreference_audit.md; notes/algebra_course_source_search.md; notes/algebra_course_query_manifest.json"
with path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
record = {"utc": datetime.now(timezone.utc).isoformat(), "activity": "Documentation-only merge; no new source reading, mathematical movement or route count", "routes": len(rows), "path": str(path.relative_to(root)), "before_sha256": before, "after_sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
(root / "logs/geometry_route_index_course_update.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
