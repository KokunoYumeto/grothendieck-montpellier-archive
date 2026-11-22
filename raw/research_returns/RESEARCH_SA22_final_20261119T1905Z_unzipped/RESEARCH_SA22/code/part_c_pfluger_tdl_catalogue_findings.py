"""Summarize actual public query results and advertised related records.

This performs no network requests and makes no article-absence conclusion.
"""
import datetime
import html.parser
import json
import pathlib
import re
import time
import urllib.parse

root = pathlib.Path(__file__).resolve().parents[1]
start = datetime.datetime.now(datetime.timezone.utc).isoformat(); tick = time.monotonic()
parent_ids = set(re.findall(r'tdl\.(\d+)', (root / 'code/root_pfluger_public_ocr_inventory_output.json').read_text()))
date_response = json.loads((root / 'sources/part_c_pfluger_tdl_delayed_periodical_session_results.txt').read_text())
jubilee = json.loads((root / 'code/part_c_pfluger_tdl_jubilee_inventory_output.json').read_text())
record = json.loads((root / 'code/part_c_pfluger_tdl_1959_record_output.json').read_text())
related = []
for item in record['result'].get('advertised_elements', []):
    url = item.get('url', '')
    if not url.startswith('https://tamildigitallibrary.in/Articles/'): continue
    decoded = urllib.parse.unquote(url)
    match = re.search(r'/Articles/[^-]+-(\d+)-', decoded)
    item_id = match.group(1) if match else None
    related.append({'url': url, 'decoded_url': decoded, 'tdl_id': item_id,
                    'text': ' '.join(item.get('text', '').split()),
                    'in_parent_ia_inventory': item_id in parent_ids})
payload = {'started_utc': start, 'elapsed_seconds': time.monotonic() - tick, 'network_requests': 0,
           'date_filter': {'count': date_response.get('count'), 'limit': date_response.get('limit'),
                           'pagination': date_response.get('pagination'), 'record_id': '26669',
                           'record_in_parent_ia_inventory': '26669' in parent_ids},
           'jubilee': {'read_pages': 1 + sum(r.get('status') == 200 for r in jubilee['results']),
                       'records': len(jubilee['records']),
                       'mathematical_title_matches': [r for r in jubilee['records'] if 'mathemat' in r['decoded_url'].lower()],
                       'all_records': jubilee['records']},
           'advertised_related_count': len(related),
           'related_mathematical': [r for r in related if 'mathemat' in r['decoded_url'].lower()],
           'advertised_related': related}
output = root / 'code/part_c_pfluger_tdl_catalogue_findings_output.json'
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
output.with_suffix('.txt').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
summary = dict(payload); summary.pop('advertised_related'); summary['jubilee'] = dict(summary['jubilee']); summary['jubilee'].pop('all_records')
print(json.dumps(summary, ensure_ascii=False, indent=2))
