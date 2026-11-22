#!/usr/bin/env python3
"""Render and OCR specified requested-source pages; actual reading is recorded separately."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import argparse
import os
import subprocess
import time
import fitz

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--ocr', action='store_true', help='Optional OCR; page images are sufficient for direct reading.')
args = parser.parse_args()
begin = time.perf_counter()
started = datetime.now(timezone.utc)
jobs = []
records = []
for stem, pages in [
    ('ROOT_KnudsenMumford1976', [1, 2, 3, 4, 5, 22, 23, 24, 25]),
    ('ROOT_Raynaud1970_XI_preview', [1, 2]),
]:
    source = root / f'literature/{stem}.pdf'
    doc = fitz.open(source)
    text_pages = []
    for n in pages:
        image = root / f'qa/{stem}_page_{n:03d}.png'
        doc[n - 1].get_pixmap(matrix=fitz.Matrix(2, 2)).save(image)
        output = root / f'literature/{stem}_page_{n:03d}'
        jobs.append((image, output, n, stem))
    records.append({
        'source': str(source.relative_to(root)),
        'sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'pdf_pages': len(doc),
        'selected_pdf_pages': pages,
        'reading_status': 'PENDING: images and OCR must still be inspected',
    })

def ocr(job):
    image, output, page, stem = job
    start = time.perf_counter()
    try:
        run = subprocess.run(['tesseract', str(image), str(output), '--psm', '3'],
                             capture_output=True, text=True, timeout=55,
                             env={**os.environ, 'OMP_THREAD_LIMIT': '1'})
        result = {'returncode': run.returncode, 'stderr': run.stderr}
    except subprocess.TimeoutExpired as error:
        result = {'returncode': None, 'error': str(error), 'outcome': 'OCR timed out; no reading inferred'}
    return {'image': str(image.relative_to(root)), 'text': str(output.relative_to(root)) + '.txt',
            'pdf_page': page, 'stem': stem,
            **result, 'seconds': time.perf_counter() - start}

if args.ocr:
    with ThreadPoolExecutor(max_workers=2) as pool:
        outputs = list(pool.map(ocr, jobs))
else:
    outputs = []
record = {'started_utc': started.isoformat(), 'sources': records, 'ocr_pages': outputs,
          'mode': 'render and OCR' if args.ocr else 'render only; no OCR attempted in this execution',
          'seconds': time.perf_counter() - begin}
(root / 'logs/ROOT_requested_source_pages.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
