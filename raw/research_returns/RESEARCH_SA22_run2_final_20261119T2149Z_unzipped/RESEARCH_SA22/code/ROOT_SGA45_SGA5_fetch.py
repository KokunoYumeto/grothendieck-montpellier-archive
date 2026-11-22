#!/usr/bin/env python3
"""Acquire the two actual public SGA scan links observed in the SLMath catalogue."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import time
from fetch_sources import fetch

root=Path(__file__).resolve().parents[1]
started=datetime.now(timezone.utc)
begin=time.perf_counter()
jobs=[
 ('https://library.slmath.org/nonmsri/sga/sga/pdf/sga4h.pdf',
  root/'literature/ROOT_SGA45_1977.pdf'),
 ('https://library.slmath.org/nonmsri/sga/sga5/SGA5.pdf',
  root/'literature/ROOT_SGA5_1977.pdf'),
]
with ThreadPoolExecutor(max_workers=2) as pool:
    results=list(pool.map(lambda pair: fetch(*pair),jobs))
record={
 'started_utc':started.isoformat(),
 'finished_utc':datetime.now(timezone.utc).isoformat(),
 'seconds':time.perf_counter()-begin,
 'scope':'Two actual publicly linked complete original scans; web-reader rejection was file size, not authorization. Download does not by itself establish mathematical reading.',
 'observed_catalogue_urls':[
  'https://library.slmath.org/nonmsri/sga/sga/pdf/index.html',
  'https://library.slmath.org/nonmsri/sga/sga5/index.html'],
 'requests':results,
}
(root/'logs/ROOT_SGA45_SGA5_fetch.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
