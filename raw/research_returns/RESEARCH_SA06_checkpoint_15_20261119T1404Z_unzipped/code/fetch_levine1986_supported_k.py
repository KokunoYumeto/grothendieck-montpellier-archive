#!/usr/bin/env python3
"""Acquire and render Levine's 1986 primary supported-K-theory sequences."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
from urllib.request import Request, urlopen
import fitz

root = Path(__file__).resolve().parents[1]
url = 'https://www.numdam.org/item/CM_1986__59_1_21_0.pdf'
path = root / 'sources' / 'levine1986_supported_k.pdf'
report = {'started_utc': datetime.now(timezone.utc).isoformat(), 'url': url}
started = time.perf_counter()
try:
    with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=35) as response:
        data = response.read()
    if not data.startswith(b'%PDF'):
        raise ValueError('Response is not a PDF')
    path.write_bytes(data)
    doc = fitz.open(path)
    (path.with_suffix('.txt')).write_text('\n'.join(p.get_text() for p in doc))
    pages = [9, 10, 11, 12, 16, 17, 18]
    rendered = []
    for page in pages:
        destination = root / 'rendered' / f'levine1986_pdfpage_{page+1:02d}.png'
        doc[page].get_pixmap(matrix=fitz.Matrix(1.5, 1.5)).save(destination)
        rendered.append(str(destination.relative_to(root)))
    report.update(status='saved', bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                  pdf_pages=len(doc), rendered=rendered)
except Exception as error:
    report.update(status='failed', error=str(error))
report['runtime_seconds'] = time.perf_counter()-started
(root / 'code' / 'fetch_levine1986_supported_k_output.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
