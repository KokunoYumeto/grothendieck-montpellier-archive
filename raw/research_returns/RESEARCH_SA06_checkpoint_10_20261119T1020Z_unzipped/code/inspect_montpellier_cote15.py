"""Render selected official manuscript scans for direct visual verification.

Scans are numbered from one; PDF indexes are numbered from zero.  Rendering
does not supply a transcription.  Readings are recorded separately after
visual inspection.  Neither the source PDF nor routine images are packaged.
"""
from pathlib import Path
import hashlib
import json
import time
import fitz

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "sources" / "montpellier_cote15_ranges.pdf"
destination = ROOT / "rendered" / "original_cote15"
destination.mkdir(parents=True, exist_ok=True)
start = time.perf_counter()
doc = fitz.open(source)
record = {"source": str(source), "source_sha256": hashlib.file_digest(source.open("rb"), "sha256").hexdigest(),
          "page_count": len(doc), "pages": []}
for scan in [48, 50, 52, 54, 56, 68, 69, 70, 71, 72, 191, 193, 195, 197, 199, 201, 203, 205]:
    page = doc[scan - 1]
    path = destination / f"scan_{scan:03d}.png"
    page.get_pixmap(dpi=160).save(path)
    record["pages"].append({"scan": scan, "pdf_index": scan - 1,
                            "points": list(page.rect), "dpi": 160,
                            "image": str(path), "extracted_text": page.get_text()})
record["runtime_seconds"] = time.perf_counter() - start
(ROOT / "code" / "inspect_montpellier_cote15_output.json").write_text(json.dumps(record, indent=2))
print(json.dumps(record, indent=2))
