#!/usr/bin/env python3
"""Render the commutativity formula viewport after locating it on the page.

Source inspection only, with the initial higher viewport preserved separately.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import fitz

root = Path(__file__).resolve().parents[1]
source = root / "literature/ROOT_KnudsenMumford1976.pdf"
target = root / "qa/C_KnudsenMumford1976/printed_20_sign_formula.png"
clock = time.perf_counter()
started = datetime.now(timezone.utc).isoformat()
clip = fitz.Rect(75, 360, 370, 440)
fitz.open(source)[1].get_pixmap(matrix=fitz.Matrix(6, 6), clip=clip, alpha=False).save(target)
record = {"scope": "Render one original formula viewport; no OCR, mathematical test or source correction inferred",
          "source": str(source.relative_to(root)), "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
          "pdf_page": 2, "printed_page": 20, "clip": list(clip), "scale": 6,
          "image": str(target.relative_to(root)), "image_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
          "started_utc": started, "finished_utc": datetime.now(timezone.utc).isoformat(),
          "rendered_pages_count": 1, "elapsed_seconds": time.perf_counter()-clock}
(root / "logs/C_KnudsenMumford1976_formula.json").write_text(json.dumps(record, indent=2)+"\n")
print(json.dumps(record, indent=2))
