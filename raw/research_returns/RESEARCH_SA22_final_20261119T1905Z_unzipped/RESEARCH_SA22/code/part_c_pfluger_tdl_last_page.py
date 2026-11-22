"""One delayed ordinary request for the sole unread advertised catalogue page.

The earlier page6 request returned temporary503. This records its later
availability separately and merges only actually read metadata records.
"""
import datetime
import hashlib
import html.parser
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request

root = pathlib.Path(__file__).resolve().parents[1]
prior = json.loads((root / 'code/part_c_pfluger_tdl_inventory_delayed_output.json').read_text())
failed = [r for r in prior['results'] if r.get('status') == 503]
assert len(failed) == 1
url = failed[0]['url']
class Links(html.parser.HTMLParser):
    def __init__(self): super().__init__(); self.links = []; self.current = None
    def handle_starttag(self, tag, attrs):
        if tag == 'a': self.current = {'url': dict(attrs).get('href', ''), 'text': ''}
    def handle_data(self, value):
        if self.current is not None: self.current['text'] += value
    def handle_endtag(self, tag):
        if tag == 'a' and self.current is not None:
            self.links.append(self.current); self.current = None

start = datetime.datetime.now(datetime.timezone.utc).isoformat(); tick = time.monotonic()
result = {'url': url, 'method': 'GET'}; links = []
try:
    with urllib.request.urlopen(url, timeout=40) as response:
        body = response.read(); destination = root / 'sources/part_c_pfluger_tdl_final_page_6.html'
        destination.write_bytes(body); parser = Links(); parser.feed(body.decode('utf-8', 'replace')); links = parser.links
        result.update(status=response.status, final_url=response.url, bytes=len(body),
                      sha256=hashlib.sha256(body).hexdigest(), saved_path=str(destination))
except Exception as error:
    result['error'] = type(error).__name__ + ': ' + str(error)
    if isinstance(error, urllib.error.HTTPError): result['status'] = error.code
records = {r['url']: r for r in prior['records']}
for link in links:
    if link['url'].startswith('https://tamildigitallibrary.in/Articles/'):
        records[link['url']] = {'url': link['url'], 'decoded_url': urllib.parse.unquote(link['url']),
                                'title': link['text'].strip()}
parent_ids = set(re.findall(r'tdl\.(\d+)', (root / 'code/root_pfluger_public_ocr_inventory_output.json').read_text()))
jims = []
for record in records.values():
    if 'mathematical society' not in record['decoded_url'].lower(): continue
    match = re.search(r'/Articles/[^-]+-(\d+)-', record['decoded_url']); item_id = match.group(1) if match else None
    jims.append(record | {'tdl_id': item_id, 'in_parent_ia_inventory': item_id in parent_ids})
payload = {'started_utc': start, 'elapsed_seconds': time.monotonic() - tick, 'requests': 1,
           'result': result, 'successfully_read_pages': 16 + int(result.get('status') == 200),
           'records': list(records.values()), 'jims_count': len(jims),
           'new_jims_ids': [r for r in jims if not r['in_parent_ia_inventory']],
           'post1959_or_jubilee_candidates': [r for r in jims if re.search(r'19[6-9]\d|Golden|Jubilee', r['decoded_url'], re.I)]}
output = root / 'code/part_c_pfluger_tdl_last_page_output.json'
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
output.with_suffix('.txt').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in payload.items() if k != 'records'} | {'record_count': len(records)}, ensure_ascii=False, indent=2))
