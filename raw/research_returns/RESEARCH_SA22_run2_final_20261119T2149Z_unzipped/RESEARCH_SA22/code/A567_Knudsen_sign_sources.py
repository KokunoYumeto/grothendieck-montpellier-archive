"""Fetch two observed public primary sources and render only sign passages.

This is source provenance, not a mathematical or finite-certificate test.
Actual page reading must be recorded separately after viewing the images.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
import urllib.request

import fitz

root = Path(__file__).resolve().parents[1]
started_utc = datetime.now(timezone.utc).isoformat()
started = time.perf_counter()
jobs = [
    (
        'A567_Knudsen2002_draft',
        'https://pnp.mathematik.uni-stuttgart.de/lexmath/kuenzer/knudsen_determinant_functors.pdf',
        [40, 41, 42],
    ),
    (
        'A567_AbdurrahmanVenkatesh_RT',
        'https://www.math.ias.edu/~akshay/research/RT.pdf',
        [68, 69],
    ),
]


def fetch(job):
    stem, url, pages = job
    clock = time.perf_counter()
    with urllib.request.urlopen(url, timeout=35) as response:
        data = response.read()
        status = response.status
        final_url = response.url
        content_type = response.headers.get('Content-Type')
    if not data.startswith(b'%PDF'):
        raise ValueError('Observed public URL did not return a PDF: ' + url)
    path = root / 'literature' / (stem + '.pdf')
    with path.open('xb') as stream:
        stream.write(data)
    document = fitz.open(path)
    images = []
    for number in pages:
        output = root / 'qa' / f'{stem}_page_{number:03d}.png'
        document[number - 1].get_pixmap(matrix=fitz.Matrix(1.7, 1.7)).save(output)
        images.append(str(output.relative_to(root)))
    return {
        'url': url,
        'final_url': final_url,
        'status': status,
        'content_type': content_type,
        'local_pdf': str(path.relative_to(root)),
        'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest(),
        'pdf_pages': len(document),
        'selected_pdf_pages': pages,
        'rendered_images': images,
        'actual_reading_status': 'PENDING: rendering alone does not establish reading',
        'elapsed_seconds': time.perf_counter() - clock,
    }


with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(fetch, jobs))
receipt = {
    'scope': 'Two observed public primary-source PDFs; five selected sign-context pages rendered; no mathematical check or certificate executed',
    'started_utc': started_utc,
    'completed_utc': datetime.now(timezone.utc).isoformat(),
    'requests_count': len(jobs),
    'rendered_pages_count': sum(len(record['selected_pdf_pages']) for record in records),
    'records': records,
    'elapsed_seconds': time.perf_counter() - started,
}
with (root / 'logs/A567_Knudsen_sign_sources.json').open('x') as stream:
    json.dump(receipt, stream, indent=2)
    stream.write('\n')
print(json.dumps(receipt, indent=2))
