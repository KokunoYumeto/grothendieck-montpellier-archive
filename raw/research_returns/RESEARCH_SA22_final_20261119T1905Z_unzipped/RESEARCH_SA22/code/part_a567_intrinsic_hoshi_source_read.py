"""Retrieve the advertised Hoshi preprint and render exact locator pages.

Source-reading utility only; no mathematical computation or certificate.
"""
from pathlib import Path
import urllib.request
import time
import hashlib
import json
import datetime
import fitz

base = Path('/workspace/scratch/9c53b536a97f/RESEARCH_SA22')
url = 'https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf'
start = time.perf_counter()
record = {'url': url, 'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
with urllib.request.urlopen(url, timeout=40) as response:
    data = response.read()
    record.update(status=response.status, final_url=response.url,
                  bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
record['retrieval_seconds'] = time.perf_counter() - start
path = base/'sources/part_a567_hoshi_rims1558.pdf'
path.write_bytes(data)
doc = fitz.open(path)
record['pages'] = len(doc)
record['renders'] = []
for index in (55, 60, 64):
    dest = base/f'notes/original_scans_a567/hoshi_rims1558_pdf_{index+1}.png'
    doc[index].get_pixmap(matrix=fitz.Matrix(1.8, 1.8)).save(dest)
    record['renders'].append({'zero_based_pdf_page': index, 'image': str(dest)})
record['whole_seconds'] = time.perf_counter() - start
(base/'code/part_a567_intrinsic_hoshi_source_read_output.json').write_text(json.dumps(record, indent=2))
print(json.dumps(record, indent=2))
