#!/usr/bin/env python3
"""Render the article's actual title page after discovering the GDZ cover.

The prior three-page render included a repository cover as PDF page 1.
This supplemental run renders PDF page 2 (printed 45) only; no network,
OCR, mathematical test, or automatic reading certification.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import time
import fitz
root=Path(__file__).resolve().parents[1]
source=root/'literature/C_Fujiwara_Crelle433_followup/Akahori1992.pdf'
target=root/'qa/C_Fujiwara_Crelle433/pdf_page_02.png'
start=time.perf_counter()
started=datetime.now(timezone.utc).isoformat()
doc=fitz.open(source)
doc[1].get_pixmap(matrix=fitz.Matrix(2,2),alpha=False).save(target)
record=dict(started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),
 elapsed_seconds=time.perf_counter()-start,rendered_pages_count=1,pdf_page=2,
 printed_page=45,image=str(target.relative_to(root)),
 source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
 image_sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
 program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 external_requests_count=0,mathematical_checks_count=0,
 scope='Supplemental title-page render only; actual reading is recorded separately.')
(root/'logs/C_Fujiwara_Crelle433_title_render.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
