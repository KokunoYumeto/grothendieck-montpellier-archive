#!/usr/bin/env python3
"""Fetch requested primary literature for inspection, recording identity and timing.

Downloaded copyrighted originals remain research inputs outside the deliverable.
"""
from pathlib import Path
import hashlib, json, subprocess, time, urllib.request

root = Path(__file__).resolve().parents[2]
dest = root / 'primary'
dest.mkdir(exist_ok=True)
sources = {'Goresky_MacPherson_SMT.pdf': 'https://www.math.ias.edu/~goresky/pdf/SMT.pdf'}
for name, url in sources.items():
    start = time.perf_counter()
    path = dest / name
    if not path.exists():
        with urllib.request.urlopen(url, timeout=60) as response:
            path.write_bytes(response.read())
    subprocess.run(['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))], check=True)
    print(json.dumps({'filename': name, 'url': url, 'bytes': path.stat().st_size,
          'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
          'seconds': round(time.perf_counter()-start, 6)}), flush=True)
