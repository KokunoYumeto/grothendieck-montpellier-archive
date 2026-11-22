#!/usr/bin/env python3
"""Export compact provenance for one already executed search batch."""
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import time

started = datetime.now(timezone.utc).isoformat()
tic = time.perf_counter()
base = Path('/workspace/scratch/9c53b536a97f')
cache = base / 'source_reading/lieberman_course/part_b_lieberman_course_queries_raw.json'
raw = cache.read_bytes()
data = json.loads(raw)
body = '\n'.join(c['text'] for c in data['result']['content'] if c.get('type') == 'text')
decisions = {
    'turn553039752search0': 'Known JSTOR issue metadata; excluded previously tried route, not opened.',
    'turn553039752search1': 'Known MaRDI metadata links only the same DOI; not an original host.',
    'turn553039752search2': 'UiB seminar concerns a different Liebermann/contact-transformations topic; no target title or original-copy link exposed.',
    'turn553039752search3': 'Later Filtrations on algebraic cycles and homology article bibliography; not Lieberman1968.',
    'turn553039752search4': 'Second NUMDAM representation of the same later article; not Lieberman1968.',
    'turn553039752search5': 'Secondary encyclopedia entry; not original text and not used as a theorem source.',
}
records = []
for block in re.split(r'\n-{10,}\n', body):
    if not block.strip():
        continue
    refs = re.findall(r'【([^】]+)】', block)
    records.append({
        'header': block.strip().splitlines()[0],
        'reference_ids': refs,
        'observed_urls': sorted(set(re.findall(r'https?://[^\s)<>]+', block))),
        'source_block_sha256': sha256(block.encode()).hexdigest(),
        'source_block_characters': len(block),
        'decision': decisions.get(refs[0], 'No classified reference') if refs else 'No reference',
        'opened_after_search': False,
    })
out = {
    'search_started_utc': data['started_utc'],
    'search_elapsed_seconds': data['elapsed_seconds'],
    'queries': data['queries'],
    'query_count': data['query_count'],
    'returned_source_blocks': len(records),
    'count_scope': 'Returned source blocks, not total search-engine hits or exhaustive directory holdings.',
    'followup_page_opens': 0,
    'file_downloads': 0,
    'mathematical_tests': 0,
    'original_mathematical_passages_obtained': 0,
    'raw_cache_path': str(cache),
    'raw_cache_sha256': sha256(raw).hexdigest(),
    'raw_cache_bytes': len(raw),
    'records': records,
    'metadata_export_started_utc': started,
    'metadata_export_completed_utc': datetime.now(timezone.utc).isoformat(),
    'metadata_export_elapsed_seconds': time.perf_counter() - tic,
    'metadata_export_network_requests': 0,
    'outcome': 'No distinct course or seminar page advertising the Lieberman1968 original was exposed by this three-query batch; stop without source-status change.',
}
path = base / 'RESEARCH_SA22/code/part_b_lieberman_course_queries_output.json'
path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(out, ensure_ascii=False, indent=2))
