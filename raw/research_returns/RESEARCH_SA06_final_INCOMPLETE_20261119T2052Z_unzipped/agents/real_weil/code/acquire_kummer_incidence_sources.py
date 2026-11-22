from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[3]
items = [
    ('hassett_tschinkel2013_kummer_author2012', 'https://www.math.brown.edu/bhassett/papers/hodge/hodge13.pdf'),
    ('kapfer_menet2018_kummer_integral_v2', 'https://arxiv.org/pdf/1607.03431'),
    ('floccari_varesco2024_kummer_published', 'https://www.math.uni-bielefeld.de/~sfloccari/HCKum2.pdf'),
]
start = time.perf_counter()
result = {'started_utc': datetime.now(timezone.utc).isoformat(), 'sources': []}
for stem, url in items:
    tick = time.perf_counter()
    data = urllib.request.urlopen(url, timeout=45).read()
    target = ROOT / 'sources' / (stem + '.pdf')
    target.write_bytes(data)
    proc = subprocess.run(['pdftotext', '-layout', str(target), str(target.with_suffix('.txt'))], capture_output=True, text=True)
    result['sources'].append({'url': url, 'file': str(target.relative_to(ROOT)), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'seconds': time.perf_counter() - tick, 'pdftotext_returncode': proc.returncode, 'pdftotext_stderr': proc.stderr})
result['finished_utc'] = datetime.now(timezone.utc).isoformat()
result['total_seconds'] = time.perf_counter() - start
output = ROOT / 'agents/real_weil/output/kummer_incidence_sources_acquisition.json'
output.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
