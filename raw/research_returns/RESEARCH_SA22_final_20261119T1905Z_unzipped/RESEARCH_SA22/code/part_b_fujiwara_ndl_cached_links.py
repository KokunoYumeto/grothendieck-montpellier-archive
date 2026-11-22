#!/usr/bin/env python3
"""Inspect existing public-record cache; make no network requests."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import time

started = datetime.now(timezone.utc).isoformat()
tic = time.perf_counter()
base = Path('/workspace/scratch/9c53b536a97f')
cache = base / 'source_reading/recorded_web_prose_second_pass/part_a567_fujiwara_distinct_search_1633.json'
output = base / 'RESEARCH_SA22/code/part_b_fujiwara_ndl_cached_links_output.json'
raw = cache.read_bytes()
data = json.loads(raw)
result = data.get('result', data)
texts = [c['text'] for c in result.get('content', []) if c.get('type') == 'text']
blocks = re.split(r'\n-{10,}\n', '\n'.join(texts))
targets = [
    'https://ndlsearch.ndl.go.jp/books/R100000136-I1363107369908715904',
    'https://cir.nii.ac.jp/crid/1363107369908715904',
]
records = []
for url in targets:
    selected = [b for b in blocks if b.strip() and url in b.strip().splitlines()[0]]
    for block in selected:
        print(block.strip())
        records.append({
            'record_url': url,
            'header': block.strip().splitlines()[0],
            'reference_ids': re.findall(r'【([^】]+)】', block),
            'observed_urls': sorted(set(re.findall(r'https?://[^\s)<>]+', block))),
            'source_block_sha256': sha256(block.encode()).hexdigest(),
            'source_block_characters': len(block),
            'mathematical_original_text': False,
        })
    if not selected:
        records.append({'record_url': url, 'error': 'No exact header block found'})
metadata = {
    'started_utc': started,
    'completed_utc': datetime.now(timezone.utc).isoformat(),
    'elapsed_seconds': time.perf_counter() - tic,
    'network_requests': 0,
    'new_search_queries': 0,
    'mathematical_tests': 0,
    'cache_files_read': 1,
    'target_records': len(targets),
    'matched_record_blocks': sum('error' not in r for r in records),
    'raw_cache_path': str(cache),
    'raw_cache_sha256': sha256(raw).hexdigest(),
    'prior_outer_metadata': {k: v for k, v in data.items() if k != 'result' and isinstance(v, (str, int, float, bool, type(None)))},
    'records': records,
    'outcome': 'Both exact record URLs occurred previously. NDL cached links expose DOI and known Euclid Download only; CiNii is separately recorded as challenged, so neither record was requested anew.',
}
output.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(metadata, indent=2, ensure_ascii=False))
