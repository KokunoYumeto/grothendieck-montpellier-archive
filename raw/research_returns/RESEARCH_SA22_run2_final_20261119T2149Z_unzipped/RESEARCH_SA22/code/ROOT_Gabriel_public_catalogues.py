#!/usr/bin/env python3
"""Read-only Gabriel1932/LMS GDZ catalogue queries using the observed form.

The prior Wiley/OUP challenge and first-page403 routes are not retried.
This does not obtain, imply, or claim access to protected full text.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import json
import time
import B_Gabber_GDZ_catalogue as catalogue

ROOT = Path(__file__).resolve().parents[1]
catalogue.OUT = ROOT / 'literature/ROOT_Gabriel_GDZ_catalogue'
catalogue.OUT.mkdir(exist_ok=True)

if __name__ == '__main__':
    started = time.perf_counter()
    jobs = [('exact_article', '"The rearrangement of positive Fourier coefficients"'),
            ('journal', '"Proceedings of the London Mathematical Society"')]
    with ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(catalogue.fetch, jobs))
    record = {
        'recorded_utc': datetime.now(timezone.utc).isoformat(),
        'scope': 'Two actual public GDZ metadata catalogue queries, not an inference from web-engine absence; no original theorem body claimed.',
        'query_count': len(jobs),
        'elapsed_seconds': time.perf_counter() - started,
        'form_provenance': 'B_Gabber_GDZ_catalogue.py and C_Fujiwara_catalogues_1943.json: observed GET /suche with search[q] and search[searchType]=metadata.',
        'results': results,
    }
    (ROOT / 'logs/ROOT_Gabriel_public_catalogues.json').write_text(json.dumps(record, indent=2, ensure_ascii=False)+'\n')
    for row in results:
        print(json.dumps({k: row.get(k) for k in ['name','query','status','byte_count','elapsed_seconds','error','text','links']}, ensure_ascii=False))
