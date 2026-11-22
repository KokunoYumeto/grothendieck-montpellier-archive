"""One delayed retry of the two public metadata URLs that returned upstream503.

This is not a retry of an access denial. It is guarded to run at least one hour
after the preceding availability check and makes no retry inside this run.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import hashlib, json, time

ROOT = Path(__file__).resolve().parents[1]
previous_path = ROOT / 'code/root_source_route_followup09_output.json'
previous = json.loads(previous_path.read_text())
earliest = datetime.fromisoformat(previous['started_utc']) + timedelta(hours=1)
assert datetime.now(timezone.utc) >= earliest, 'Wait for the stated delayed availability interval.'
output = ROOT / 'code/root_fatcat_delayed_availability_output.json'
assert not output.exists(), 'Preserve this actual delayed-check record; do not repeat it.'
started = time.perf_counter()
started_utc = datetime.now(timezone.utc).isoformat()
cache = ROOT.parent / 'source_reading/fatcat_availability_after1827'
jobs = previous['network_requests']
assert len(jobs) == 2 and all(j['http_status'] == 503 for j in jobs)

def fetch(job):
    began = time.perf_counter()
    record = dict(work=job['work'], url=job['url'], doi=job['doi'],
                  started_utc=datetime.now(timezone.utc).isoformat())
    try:
        request = Request(job['url'], headers={'User-Agent':'ResearchSourceAudit/1.0', 'Accept':'application/json'})
        with urlopen(request, timeout=25) as response:
            data = response.read()
            record.update(http_status=response.status, final_url=response.url,
                          content_type=response.headers.get('Content-Type'), bytes=len(data),
                          sha256=hashlib.sha256(data).hexdigest())
        cache.mkdir(parents=True, exist_ok=True)
        target = cache / (job['work'] + '.json')
        target.write_bytes(data)
        record['source_cache'] = str(target)
        record['interpretation'] = 'Response obtained; source status stays unchanged pending actual metadata and original-passage inspection.'
    except HTTPError as error:
        data = error.read()
        record.update(http_status=error.code, error=str(error), error_body_bytes=len(data),
                      error_body_sha256=hashlib.sha256(data).hexdigest(),
                      error_excerpt=data[:400].decode(errors='replace'),
                      interpretation='No metadata record obtained; this does not establish absence of an original copy.')
    except Exception as error:
        record.update(error=f'{type(error).__name__}: {error}',
                      interpretation='No metadata record obtained; this does not establish absence of an original copy.')
    record['seconds'] = time.perf_counter() - began
    return record

with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(fetch, jobs))
record = dict(started_utc=started_utc, previous_run=previous['started_utc'],
              earliest_allowed_utc=earliest.isoformat(), requests=records,
              seconds=time.perf_counter()-started,
              scope='Exactly two delayed public metadata GETs; no retry within this run, no original-text or mathematical-status claim.')
output.write_text(json.dumps(record, indent=2) + '\n')
lines = ['# Delayed Fatcat metadata availability check', '',
         'The preceding public DOI lookups failed with an upstream503 response. This later check reuses exactly those two URLs after at least one hour; it does not revisit an access denial or change any authentication, endpoint or header to bypass a restriction.', '',
         'The script and exact measured output are `code/root_fatcat_delayed_availability.py` and its associated output. There are exactly two GETs and no within-run retry.', '',
         '| Work | Actual response | Interpretation |', '|---|---|---|']
for item in records:
    lines.append('| '+item['work']+' | '+str(item.get('http_status', item.get('error')))+' | '+item['interpretation']+' |')
lines += ['', 'No source requirement changes merely because a service is reachable or a metadata record exists. An actual original passage and its hypothesis comparison remain necessary. No mathematical proof or finite certificate was rerun.', '']
(ROOT / 'notes/root_fatcat_delayed_availability.md').write_text('\n'.join(lines))
print(json.dumps(record, indent=2))
