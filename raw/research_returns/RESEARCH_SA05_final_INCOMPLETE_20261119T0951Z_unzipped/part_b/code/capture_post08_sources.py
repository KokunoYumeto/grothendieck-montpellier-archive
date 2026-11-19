"""Primary-source retrieval; raw third-party documents stay outside deliverables."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import time
import urllib.request

BASE = Path('/workspace/scratch/6215ed17d0f0')
RAW = BASE / 'primary_sources/part_b/post08'
OUT = BASE / 'RESEARCH_SA05_work/part_b/output/post08_primary_capture.json'
TASKS = [
 ('schreieder2024_moving.pdf', 'https://arxiv.org/pdf/2207.08297v3'),
 ('ct_schreieder2026_divisibility.pdf', 'https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/CTSchreieder21May26.pdf'),
 ('schreieder2024_milnor_tate.pdf', 'https://www.iag.uni-hannover.de/fileadmin/iag/homepages/schreieder/publications/Milnor_K-theory_and_Tate.pdf'),
 ('scavia_suzuki2026_unramified.pdf', 'https://arxiv.org/pdf/2609.36188'),
]
RAW.mkdir(parents=True, exist_ok=True)
OUT.parent.mkdir(parents=True, exist_ok=True)
records = json.loads(OUT.read_text()) if OUT.exists() else []
for name, url in TASKS:
    if any(row.get('url') == url and row.get('obtained') for row in records):
        continue
    began = time.monotonic()
    row = {'file': name, 'url': url, 'utc': datetime.now(timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=25) as response:
            data = response.read()
            row.update(status=response.status, final_url=response.url,
                       content_type=response.headers.get('Content-Type', ''))
        (RAW / name).write_bytes(data)
        row.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                   raw_path=str(RAW / name), obtained=data.startswith(b'%PDF-'))
        if row['obtained']:
            text_path = (RAW / name).with_suffix('.txt')
            subprocess.run(['pdftotext', '-layout', str(RAW / name), str(text_path)], check=True)
            row['text_path'] = str(text_path)
    except Exception as exc:
        row.update(obtained=False, error=f'{type(exc).__name__}: {exc}')
    row['seconds'] = round(time.monotonic() - began, 6)
    records.append(row)
OUT.write_text(json.dumps(records, indent=2) + '\n')
print(json.dumps(records, indent=2))
