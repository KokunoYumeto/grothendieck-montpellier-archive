"""Retain compact metadata for two executed, bounded repository query batches."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib, json, re, time

ROOT = Path(__file__).resolve().parents[1]
started = time.perf_counter()
started_utc = datetime.now(timezone.utc).isoformat()
raw_path = ROOT.parent / 'source_reading/recorded_web_search/root_fujiwara_japan_repositories_1816.json'
raw_bytes = raw_path.read_bytes()
raw = json.loads(raw_bytes)
records = []
for cell in raw:
    body = '\n'.join(x.get('text', '') for x in cell['raw'].get('content', []) if x.get('type') == 'text')
    records.append({
        'started_utc': cell['started_utc'], 'seconds': cell['seconds'],
        'request': cell['query'],
        'returned_references': list(dict.fromkeys(re.findall(r'turn\w+(?:search|view)\d+', body))),
        'returned_urls': list(dict.fromkeys(re.findall(r'https?://[^\s)<>]+', body))),
        'raw_text_sha256': hashlib.sha256(body.encode()).hexdigest(),
        'assessment': 'Only later bibliography, different dissertation and repository browsing records were returned; no target original or advertised target-copy link was exposed.'
    })
output = dict(started_utc=started_utc, scope='Two public web-query batches: four targeted queries, zero page opens or direct HTTP requests. No mathematical check.',
              raw_cache=str(raw_path), raw_bytes=len(raw_bytes), raw_sha256=hashlib.sha256(raw_bytes).hexdigest(),
              records=records, source_status_changed=False, mathematical_status_changed=False)
note = '''# Bounded Nagoya and Kyoto repository discovery for Fujiwara1995

The remaining target is Kazuhiro Fujiwara, *Theory of tubular neighborhood in étale topology*, Duke Mathematical Journal80(1995),15–57, specifically original Corollary6.6.4 or an equally explicit original comparison.

Two executed query batches targeted the official Nagoya and Kyoto repositories. The exact four queries and measured tool times are retained in `code/root_fujiwara_japan_repository_queries_output.json`, with the actual executed JavaScript transcript beside it.

The indexed Nagoya item was a later thesis, *A study on Fontaine’s perfectoid rings and their algebraizations*, whose bibliography cites the target. Kyoto results concerned rigid-analytic geometry, another author’s2011 dissertation, a later RIMS bibliography, and a2009 title-browsing page. None was the1995 original or exposed a distinct original-copy link. No later thesis or bibliography was downloaded merely to confirm that already visible distinction. No repository search form, complete catalogue, or exhaustive absence was inspected or inferred.

Counts: four search queries in two calls; no page opens, direct HTTP requests, access retries, or mathematical certificate executions. The call times were0.898s and0.469s. The local record-generation duration is recorded separately and is not substituted for a search duration.

**Outcome:** Fujiwara1995 remains NOT OPENED in its required original mathematical passage. This bounded negative discovery does not change a source gate, mathematical statement, or hourly movement assessment.
'''
(ROOT / 'notes/root_fujiwara_japan_repositories.md').write_text(note)
output['seconds'] = time.perf_counter() - started
(ROOT / 'code/root_fujiwara_japan_repository_queries_output.json').write_text(json.dumps(output, indent=2) + '\n')
(ROOT / 'code/root_fujiwara_japan_repository_records_output.json').write_text(json.dumps({'started_utc': started_utc, 'seconds': output['seconds'], 'scope': 'Offline compact record and note generation; network calls were not rerun.'}, indent=2) + '\n')
print(json.dumps({k: output[k] for k in ['started_utc', 'seconds', 'source_status_changed', 'mathematical_status_changed']}, indent=2))
