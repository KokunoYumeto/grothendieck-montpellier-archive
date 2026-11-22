#!/usr/bin/env python3
"""Render the already downloaded 37-page original Knudsen--Mumford paper.

This is source-image preparation only: no download, OCR, mathematical test,
or source-reading certification. The actual page-by-page reading is recorded
separately. Source images are excluded from the deliverable ZIP.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import fitz

root = Path(__file__).resolve().parents[1]
source = root / "literature/ROOT_KnudsenMumford1976.pdf"
destination = root / "qa/C_KnudsenMumford1976"
destination.mkdir(parents=True, exist_ok=True)
started = datetime.now(timezone.utc)
clock = time.perf_counter()
document = fitz.open(source)
if len(document) != 37:
    raise RuntimeError("Expected the identified 37-page original, printed19--55")
records = []
for index, page in enumerate(document):
    target = destination / f"printed_{index+19:02d}.png"
    page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5), alpha=False).save(target)
    data = target.read_bytes()
    records.append({"pdf_page": index+1, "printed_page": index+19,
                    "image": str(target.relative_to(root)), "bytes": len(data),
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "reading_status": "Not certified by rendering"})
record = {
    "scope": "Render all37 original source pages; no OCR, download, mathematical test or reading inference",
    "source": str(source.relative_to(root)),
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "started_utc": started.isoformat(),
    "finished_utc": datetime.now(timezone.utc).isoformat(),
    "rendered_pages_count": len(records),
    "elapsed_seconds": time.perf_counter()-clock,
    "scale": 2.5,
    "rendered_pages": records,
}
(root / "logs/C_KnudsenMumford1976_render.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps({key:value for key,value in record.items() if key != "rendered_pages"}, indent=2))
