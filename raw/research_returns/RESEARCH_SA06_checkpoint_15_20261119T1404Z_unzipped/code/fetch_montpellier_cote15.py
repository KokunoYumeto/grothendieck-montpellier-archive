"""Retrieve the official dossier to inspect the unfinished question on scan70.

The source scan is excluded from research ZIPs; this program and its
retrieval record are retained. No mathematical claim is based on the
success of downloading alone.
"""
from pathlib import Path
import hashlib
import json
import time
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://grothendieck.umontpellier.fr/15.pdf'
start = time.perf_counter()
record = {'url': URL}
try:
    request = urllib.request.Request(URL, method='HEAD')
    with urllib.request.urlopen(request, timeout=45) as response:
        record['head_status'] = response.status
        record['headers'] = dict(response.headers)
    length = int(record['headers'].get('Content-Length', '0'))
    if length > 450_000_000:
        record['outcome'] = 'Not downloaded: over450MB; targeted range retrieval needed'
    else:
        dest = ROOT / 'sources' / 'montpellier_cote15.pdf'
        with urllib.request.urlopen(URL, timeout=55) as response:
            raw = response.read(450_000_001)
        if len(raw) > 450_000_000:
            record['outcome'] = 'Not retained: response exceeds450MB'
        elif not raw.startswith(b'%PDF'):
            record['outcome'] = 'Not a PDF response'
            record['prefix'] = raw[:150].decode(errors='replace')
        else:
            dest.write_bytes(raw)
            record.update(outcome='Downloaded source PDF', bytes=len(raw),
                          sha256=hashlib.sha256(raw).hexdigest(), local=str(dest))
except Exception as error:
    record['outcome'] = 'Retrieval failed'
    record['error'] = repr(error)
record['runtime_seconds'] = time.perf_counter() - start
(ROOT / 'code' / 'fetch_montpellier_cote15_output.json').write_text(
    json.dumps(record, ensure_ascii=False, indent=2))
print(json.dumps(record, ensure_ascii=False, indent=2))
