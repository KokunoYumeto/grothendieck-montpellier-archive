from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request

root = Path(__file__).resolve().parents[3]
start = time.perf_counter()
result = {'started_utc': datetime.now(timezone.utc).isoformat(), 'sources': []}
for stem, url in [
    ('kapfer_menet2018_kummer_integral_published', 'https://content.algebraicgeometry.nl/2018-5/2018-5-014.pdf'),
    ('kapfer_menet2019_kummer_erratum_v1', 'https://arxiv.org/pdf/1907.07031'),
]:
    tick = time.perf_counter()
    data = urllib.request.urlopen(url, timeout=45).read()
    target = root / 'sources' / (stem + '.pdf')
    target.write_bytes(data)
    proc = subprocess.run(['pdftotext', '-layout', str(target), str(target.with_suffix('.txt'))], capture_output=True, text=True)
    result['sources'].append({'url': url, 'file': str(target.relative_to(root)), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'seconds': time.perf_counter()-tick, 'pdftotext_returncode': proc.returncode, 'pdftotext_stderr':proc.stderr})
result['finished_utc'] = datetime.now(timezone.utc).isoformat()
result['total_seconds'] = time.perf_counter()-start
target = root / 'agents/real_weil/output/kummer_published_sources_acquisition.json'
target.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
