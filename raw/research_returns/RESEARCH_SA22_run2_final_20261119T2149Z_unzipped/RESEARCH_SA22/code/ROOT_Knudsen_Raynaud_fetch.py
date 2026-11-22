#!/usr/bin/env python3
"""Fetch two observed authorized original-source/preview links, without inference of reading."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor
import json
import time
from fetch_sources import fetch

root = Path(__file__).resolve().parents[1]
started = datetime.now(timezone.utc)
begin = time.perf_counter()
jobs = [
    ('https://journals.msp.org/mscand/article/download/2000/1999/2031',
     root / 'literature/ROOT_KnudsenMumford1976.pdf'),
    ('https://page-one.springer.com/pdf/preview/10.1007/BFb0069582',
     root / 'literature/ROOT_Raynaud1970_XI_preview.pdf'),
]
with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(lambda pair: fetch(*pair), jobs))
record = {
    'started_utc': started.isoformat(),
    'scope': 'Observed journal original PDF and explicit public publisher two-page preview only; full Raynaud subscription text not requested',
    'requests': results,
    'seconds': time.perf_counter() - begin,
    'reading_status': 'Downloaded bytes are not themselves evidence of mathematical reading',
}
(root / 'logs/ROOT_Knudsen_Raynaud_fetch.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
