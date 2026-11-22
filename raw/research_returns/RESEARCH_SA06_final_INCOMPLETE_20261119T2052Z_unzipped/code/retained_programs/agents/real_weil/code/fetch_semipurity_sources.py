#!/usr/bin/env python3
"""Retain primary PDFs already opened during the semipurity investigation."""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess, urllib.request

base = Path(__file__).resolve().parents[1]
destination = base / 'sources'
destination.mkdir(exist_ok=True)
sources = [
    ('weber2012_boundary_purity.pdf',
     'https://www.journalofsing.org/volume4/weber.pdf'),
    ('dayton_weibel1980_hyperplanes.pdf',
     'https://sites.math.rutgers.edu/~weibel/archive/papers-dir/DaytonWeibel-1980.pdf'),
]
started = datetime.now(timezone.utc).isoformat()
clock = perf_counter()

def acquire(item):
    name, url = item
    start = perf_counter()
    record = {'file': name, 'url': url,
              'started_utc': datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=40) as response:
            content = response.read()
        if not content.startswith(b'%PDF'):
            raise ValueError('The returned content is not a PDF.')
        path = destination / name
        path.write_bytes(content)
        conversion = subprocess.run(
            ['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))],
            capture_output=True, text=True)
        record.update(status='saved', bytes=len(content),
                      sha256=hashlib.sha256(content).hexdigest(),
                      pdftotext_returncode=conversion.returncode)
    except Exception as error:
        record.update(status='failed', error=str(error))
    record['runtime_seconds'] = perf_counter() - start
    return record

with ThreadPoolExecutor(max_workers=2) as executor:
    records = list(executor.map(acquire, sources))
result = {'started_utc': started,
          'finished_utc': datetime.now(timezone.utc).isoformat(),
          'runtime_seconds': perf_counter() - clock,
          'sources': records,
          'scope': 'Source acquisition only; no mathematical certificate.'}
(base / 'output/semipurity_sources_manifest.json').write_text(
    json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
