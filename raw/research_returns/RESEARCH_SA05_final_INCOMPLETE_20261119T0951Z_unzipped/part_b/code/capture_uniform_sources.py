"""Archive exact primary versions for the uniform B.3 extension.

Raw external PDFs stay outside the deliverable tree. This script and its
small provenance log are checkpointed, including failed responses.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import time
from urllib.request import Request, urlopen

BASE = Path('/workspace/scratch/6215ed17d0f0')
DEST = BASE / 'primary_sources' / 'part_b'
DEST.mkdir(parents=True, exist_ok=True)
LOG = BASE / 'RESEARCH_SA05_work' / 'part_b' / 'output' / 'uniform_primary_capture.json'
SOURCES = [
    ('qin2021_uniform', 'https://arxiv.org/pdf/2012.01681'),
    ('ertl_keller_qin2025', 'https://arxiv.org/pdf/2012.01337'),
    ('robert2023_abelian_schemes', 'https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/books/avtheory.pdf'),
    ('moonen_duality2011', 'https://www.math.ru.nl/personal/bmoonen/BookAV/DualAV2.pdf'),
    ('blr1990', 'https://www.math.stonybrook.edu/~kamenova/homepage_files/Bosch_Raynaud_Neron_Model_tc.pdf'),
    ('yuan2021_hodge_author', 'https://faculty.bicmr.pku.edu.cn/~yxy/preprints/positivity_hodge_bundle.pdf'),
]

def fetch(source):
    key, url = source
    start = time.monotonic()
    row = dict(key=key, url=url, time_utc=datetime.now(timezone.utc).isoformat())
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request, timeout=90) as response:
            row.update(http_status=response.status, final_url=response.url,
                       content_type=response.headers.get('Content-Type'))
            content = response.read()
        if not content.startswith(b'%PDF'):
            raise ValueError('Response is not a PDF')
        target = DEST / (key + '.pdf')
        target.write_bytes(content)
        row.update(status='downloaded', path=str(target), bytes=len(content),
                   sha256=hashlib.sha256(content).hexdigest())
    except Exception as exc:
        row.update(status='not obtained by this request', error=repr(exc))
    row['elapsed_seconds'] = round(time.monotonic() - start, 6)
    return row

if __name__ == '__main__':
    started = time.monotonic()
    with ThreadPoolExecutor(max_workers=6) as pool:
        records = list(pool.map(fetch, SOURCES))
    result = {'retrievals': records,
              'total_elapsed_seconds': round(time.monotonic() - started, 6)}
    LOG.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))
