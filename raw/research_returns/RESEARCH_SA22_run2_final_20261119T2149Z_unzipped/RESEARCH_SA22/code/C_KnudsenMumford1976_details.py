#!/usr/bin/env python3
"""Render two precise source details for direct reading, not an OCR/proof test."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import fitz

root = Path(__file__).resolve().parents[1]
clock = time.perf_counter()
started = datetime.now(timezone.utc).isoformat()
out = root / "qa/C_KnudsenMumford1976"
out.mkdir(parents=True, exist_ok=True)
jobs = [
    (root / "literature/ROOT_KnudsenMumford1976.pdf", 2,
     fitz.Rect(75, 310, 370, 370), 6, "printed_20_commutativity_detail.png"),
    (root.parent / "sources/cote_68.pdf", 56, None, 1.5, "cote68_scan056.png"),
]
records = []
for source, number, clip, scale, filename in jobs:
    document = fitz.open(source)
    target = out / filename
    document[number-1].get_pixmap(matrix=fitz.Matrix(scale, scale), clip=clip, alpha=False).save(target)
    records.append({"source": str(source), "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                    "pdf_page": number, "clip": list(clip) if clip else None, "scale": scale,
                    "image": str(target.relative_to(root)), "image_sha256": hashlib.sha256(target.read_bytes()).hexdigest()})
record = {"scope": "Two PDF viewport/page renderings for source inspection; no download, OCR, mathematical test or reading certification",
          "started_utc": started, "finished_utc": datetime.now(timezone.utc).isoformat(),
          "rendered_pages_count": len(records), "elapsed_seconds": time.perf_counter()-clock,
          "rendered_pages": records}
(root / "logs/C_KnudsenMumford1976_details.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
