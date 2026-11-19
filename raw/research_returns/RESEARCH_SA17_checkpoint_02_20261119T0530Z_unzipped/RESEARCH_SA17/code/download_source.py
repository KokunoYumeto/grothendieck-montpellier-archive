#!/usr/bin/env python3
"""Fetch public sources; preserve URL, SHA256, elapsed time and errors."""
from pathlib import Path
from urllib.request import urlopen
from datetime import datetime, timezone
import sys, time, json, hashlib
root = Path(__file__).resolve().parents[1]
target_dir = root.parent / 'external_sources'
target_dir.mkdir(exist_ok=True)
for url, name in zip(sys.argv[1::2], sys.argv[2::2]):
    started = time.perf_counter()
    record = {'utc': datetime.now(timezone.utc).isoformat(), 'url': url, 'file': name}
    try:
        data = urlopen(url, timeout=55).read()
        dest = target_dir / name
        dest.write_bytes(data)
        record.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), status='success')
    except Exception as exc:
        record.update(status='error', error=repr(exc))
    record['seconds'] = time.perf_counter()-started
    with (root / 'logs/source_downloads.jsonl').open('a') as handle:
        handle.write(json.dumps(record)+'\n')
    print(json.dumps(record), flush=True)
