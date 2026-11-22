#!/usr/bin/env python3
"""OCR the publicly available eleven-page original excerpt, outside the archive."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
import os
import subprocess
import fitz

root = Path(__file__).resolve().parents[1]
source = root.parent / 'source_external/LashofRothenberg1978.pdf'
dest = source.parent / 'LashofRothenberg1978_excerpt'
dest.mkdir(exist_ok=True)
with fitz.open(source) as doc:
    count = len(doc)
    for i, page in enumerate(doc):
        page.get_pixmap(dpi=180).save(dest / f'page_{i+1:02d}.png')

def ocr(n):
    stem = dest / f'page_{n:02d}'
    if not stem.with_suffix('.txt').exists() or not stem.with_suffix('.txt').stat().st_size:
        env = dict(os.environ, OMP_THREAD_LIMIT='1')
        subprocess.run(['tesseract', str(stem.with_suffix('.png')), str(stem), '-l', 'eng'],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
                       env=env, timeout=45)
    return {'pdf_page': n, 'png_sha256': hashlib.sha256(stem.with_suffix('.png').read_bytes()).hexdigest(),
            'ocr_sha256': hashlib.sha256(stem.with_suffix('.txt').read_bytes()).hexdigest()}

with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(ocr, range(1, count+1)))
record = {'utc': datetime.now(timezone.utc).isoformat(), 'source': str(source),
          'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
          'pages': count, 'scope': 'Public eleven-page excerpt only; not the whole fifty-six-page article.',
          'output_directory': str(dest), 'records': records}
(root / 'logs/LashofRothenberg_original_OCR.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k != 'records'}, indent=2))
