"""Retrieve the primary logarithmic Tate paper for the fourth review audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request

root = Path(__file__).resolve().parents[1]
target = root / 'sources/root_post07/KatoNakayamaUsui2025.pdf'
url = 'https://arxiv.org/pdf/2502.16974'
start = time.perf_counter()
record = {'url': url, 'recorded_utc': datetime.now(timezone.utc).isoformat()}
try:
    with urllib.request.urlopen(url, timeout=40) as response:
        data = response.read()
    if not data.startswith(b'%PDF'):
        raise ValueError('Response is not PDF data')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    subprocess.run(['pdftotext', '-layout', str(target), str(target.with_suffix('.txt'))], check=True)
    record.update(status='obtained', bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                  path=str(target.relative_to(root)))
except Exception as error:
    record.update(status='failed', error=str(error))
record.update(seconds=round(time.perf_counter()-start, 6),
              scope='Retrieval and text extraction. Actual proof-read scope is recorded separately. Raw source excluded from checkpoint ZIPs.')
(root/'code/fetch_root_log_tate_source_output.json').write_text(json.dumps(record, indent=2)+'\n')
print(json.dumps(record, indent=2))
