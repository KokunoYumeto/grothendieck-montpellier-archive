"""One delayed Fujiwara metadata availability check; one new Lieberman lookup.

No retries, automatic file downloads, authentication, or alternate endpoint.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import hashlib
import json
import time

base = Path(__file__).resolve().parents[1]
jobs = [
    ('fujiwara1995', '10.1215/S0012-7094-95-08002-8', 'One delayed check of the exact previously503 public metadata URL.'),
    ('lieberman1968', '10.2307/2373533', 'One new metadata lookup; existing scripts/notes show no earlier Fatcat query for this DOI.'),
]

def get(job):
    name, doi, scope = job
    url = 'https://api.fatcat.wiki/v0/release/lookup?' + urlencode({'doi': doi})
    record = {'work': name, 'doi': doi, 'url': url, 'scope': scope, 'started_utc': datetime.now(timezone.utc).isoformat()}
    started = time.perf_counter()
    try:
        request = Request(url, headers={'User-Agent': 'ResearchSourceAudit/1.0', 'Accept': 'application/json'})
        with urlopen(request, timeout=35) as response:
            data = response.read()
            record.update(http_status=response.status, final_url=response.url, content_type=response.headers.get('Content-Type'), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        try:
            metadata = json.loads(data)
            raw = base / f'code/part_a567_fatcat_delayed_{name}_raw.json'
            raw.write_bytes(data)
            record['metadata'] = metadata
            record['raw_file'] = str(raw.relative_to(base))
        except ValueError:
            record['body_excerpt'] = data[:2000].decode(errors='replace')
            record['interpretation'] = 'Not JSON; no release/file metadata assumed.'
    except HTTPError as error:
        data = error.read()
        record.update(http_status=error.code, error=str(error), error_body_bytes=len(data), error_body_sha256=hashlib.sha256(data).hexdigest(), body_excerpt=data[:2000].decode(errors='replace'))
    except Exception as error:
        record['error'] = f'{type(error).__name__}: {error}'
    record['elapsed_seconds'] = time.perf_counter() - started
    return record

started = time.perf_counter()
with ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(get, jobs))
out = {'scope': 'Exactly two ordinary public metadata requests; no file content requests and no retries.', 'requests': results, 'batch_wall_seconds': time.perf_counter()-started}
(base / 'code/part_a567_fatcat_delayed_check_output.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(out, ensure_ascii=False, indent=2))
