#!/usr/bin/env python3
"""Prepare bounded source inspection of the identified Crelle 433 phrase hit.

Extract the public manifest's contents and render the identified article's
title page and final two pages. This records preparation, not actual reading;
it performs no network request, OCR, or mathematical check.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import html
import json
import re
import time
import fitz

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / 'literature/C_Fujiwara_Crelle433_followup'
QA = ROOT / 'qa/C_Fujiwara_Crelle433'
QA.mkdir(parents=True, exist_ok=True)
start = time.perf_counter()
started = datetime.now(timezone.utc).isoformat()
manifest = json.loads((BASE / 'manifest.json').read_text())
canvases = {c['@id']: c for c in manifest['sequences'][0]['canvases']}
contents = []
for s in manifest['structures']:
    authors = [html.unescape(re.sub('<[^>]+>', '', str(m['value'])))
               for m in s.get('metadata', []) if m['label'] in ['Autor', 'Autoren']]
    rr = s.get('ranges', [])
    contents.append(dict(id=s['@id'], title=s['label'], authors=authors,
                         first_page=canvases[rr[0]]['label'] if rr else None,
                         last_page=canvases[rr[-1]]['label'] if rr else None))
(BASE / 'contents.json').write_text(json.dumps(contents, indent=2, ensure_ascii=False)+'\n')
pdf = BASE / 'Akahori1992.pdf'
doc = fitz.open(pdf)
text = '\n\f\n'.join(page.get_text() for page in doc)
(BASE / 'Akahori1992.txt').write_text(text)
pages = []
for index in [0, len(doc)-2, len(doc)-1]:
    target = QA / f'pdf_page_{index+1:02d}.png'
    doc[index].get_pixmap(matrix=fitz.Matrix(2,2), alpha=False).save(target)
    pages.append(dict(pdf_page=index+1, image=str(target.relative_to(ROOT)),
                      sha256=hashlib.sha256(target.read_bytes()).hexdigest(),
                      reading_status='Rendering alone is not a reading event.'))
result = dict(started_utc=started, finished_utc=datetime.now(timezone.utc).isoformat(),
              elapsed_seconds=time.perf_counter()-start,
              program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              source_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
              manifest_contents_entries_count=len(contents), pdf_pages_count=len(doc),
              rendered_pages_count=len(pages), text_extracted_characters=len(text),
              external_requests_count=0, mathematical_checks_count=0, pages=pages,
              scope='Metadata extraction and three selected-page renders; no OCR or inference of reading.')
(ROOT / 'logs/C_Fujiwara_Crelle433_inspect.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
