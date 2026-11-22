"""Exact public-page request previously run inline on 2026-11-19.

Preserved after the run; do not rerun the denied endpoint.
The existing metadata JSON records the actual execution and timing.
"""
import urllib.request
import time
import json
import hashlib
import re
import datetime
from pathlib import Path

p = Path('/workspace/scratch/9c53b536a97f/RESEARCH_SA22')
url = 'https://albert.ias.edu/search'
t = time.perf_counter()
out = {'url': url, 'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
try:
    with urllib.request.urlopen(url, timeout=35) as r:
        b = r.read()
        out.update(status=r.status, final_url=r.url, bytes=len(b), sha256=hashlib.sha256(b).hexdigest())
        s = b.decode('utf-8', errors='replace')
        (p / 'sources/part_a567_fujiwara_ias_search.html').write_text(s)
        out['forms'] = re.findall(r'<form\b.*?</form>', s, re.S | re.I)
        out['script_srcs'] = re.findall(r'<script[^>]+src=[\"\x27]([^\"\x27]+)', s, re.I)
        out['search_related_snippets'] = [
            s[max(0, m.start()-120):m.end()+250]
            for m in list(re.finditer(r'query|rest/api|search-form|formControlName', s, re.I))[:30]
        ]
except Exception as e:
    out['error'] = repr(e)
out['seconds'] = time.perf_counter() - t
(p / 'code/part_a567_fujiwara_ias_search_metadata.json').write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
