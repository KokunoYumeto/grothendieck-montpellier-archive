"""Archive the two primary papers checked in the fourth review interval."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'sources/root_post07'
DEST.mkdir(parents=True, exist_ok=True)
SOURCES = [
    ('FlachKrauseMorin2026', 'https://arxiv.org/pdf/2603.21471'),
    ('AwadaBolognesiLaterveerPedrini2025v3', 'https://arxiv.org/pdf/2012.05969'),
]

def obtain(item):
    name, url = item
    start = time.monotonic()
    result = {'name': name, 'url': url}
    try:
        with urllib.request.urlopen(url, timeout=40) as response:
            data = response.read()
        if not data.startswith(b'%PDF'):
            raise ValueError('Response is not a PDF')
        target = DEST / (name+'.pdf')
        target.write_bytes(data)
        subprocess.run(['pdftotext', '-layout', str(target), str(target.with_suffix('.txt'))], check=True)
        result.update(status='obtained', bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), path=str(target.relative_to(ROOT)))
    except Exception as error:
        result.update(status='failed', error=str(error))
    result['seconds'] = round(time.monotonic()-start, 6)
    return result

with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(obtain, SOURCES))
output = {'recorded_utc': datetime.now(timezone.utc).isoformat(), 'sources': records,
          'scope': 'Retrieval and extraction only. Exact actual reads are recorded separately. Raw source PDFs and extracts are excluded from deliverable archives.'}
(ROOT/'code/fetch_root_post07_sources_output.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
