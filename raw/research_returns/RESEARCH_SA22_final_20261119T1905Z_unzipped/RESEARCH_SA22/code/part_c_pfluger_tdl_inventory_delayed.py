"""One delayed ordinary retry of two advertised temporary-503 catalogue pages.

Use cached successful pages and follow only actual pagination anchors. A page
is requested at most once in this run, with at most two concurrent GETs.
Stop new requests on authentication/permission/rate-limit responses. No book
content, guessed catalogue IDs, hidden endpoint, or special header is used.
"""
import concurrent.futures
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
base = 'https://tamildigitallibrary.in/search/Mathematical'

class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.current = None
    def handle_starttag(self, tag, attrs):
        if tag == 'a': self.current = {'url': dict(attrs).get('href', ''), 'text': ''}
    def handle_data(self, data):
        if self.current is not None: self.current['text'] += data
    def handle_endtag(self, tag):
        if tag == 'a' and self.current is not None:
            self.links.append(self.current); self.current = None

def parse(value):
    parser = Links(); parser.feed(value); return parser.links

def fetch(url):
    tick = time.monotonic(); item = {'url': url, 'method': 'GET'}; value = ''
    try:
        with urllib.request.urlopen(url, timeout=35) as response:
            body = response.read(); value = body.decode('utf-8', 'replace')
            page = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)['page'][0]
            dest = root / 'sources' / ('part_c_pfluger_tdl_delayed_page_' + page + '.html')
            dest.write_bytes(body)
            item.update(status=response.status, final_url=response.url, bytes=len(body),
                        sha256=hashlib.sha256(body).hexdigest(), saved_path=str(dest))
    except Exception as error:
        item['error'] = type(error).__name__ + ': ' + str(error)
        if isinstance(error, urllib.error.HTTPError): item['status'] = error.code
    item['seconds'] = time.monotonic() - tick
    return item, parse(value)

started = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.monotonic()
previous = json.loads((root / 'code/part_c_pfluger_tdl_inventory_output.json').read_text())
seen = {base, base + '?page=1'}
cached = [str(root / 'sources/part_c_pfluger_tdl_mathematical.html')]
for item in previous['results']:
    if item.get('status') == 200:
        seen.add(item['url']); cached.append(item['saved_path'])
queued = []; records = {}; results = []; denied = False

def consume(links):
    for item in links:
        url = item['url']
        if url.startswith(base + '?page=') and url not in seen and url not in queued:
            queued.append(url)
        if url.startswith('https://tamildigitallibrary.in/Articles/'):
            records[url] = {'url': url, 'decoded_url': urllib.parse.unquote(url),
                            'title': item['text'].strip()}

for path in cached: consume(parse(pathlib.Path(path).read_text()))
initial_advertised = list(queued)
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    pending = {}
    while queued or pending:
        while queued and len(pending) < 2 and not denied and len(results) + len(pending) < 17:
            url = queued.pop(0); seen.add(url); pending[pool.submit(fetch, url)] = url
        if not pending: break
        done, _ = concurrent.futures.wait(pending, return_when=concurrent.futures.FIRST_COMPLETED)
        for future in done:
            pending.pop(future); item, links = future.result(); results.append(item); consume(links)
            print(json.dumps({'url': item['url'], 'status': item.get('status'),
                              'seconds': item['seconds'], 'records': len(records)}), flush=True)
            if item.get('status') in (401, 403, 429): denied = True
        if denied: queued = []

jims = [r for r in records.values() if 'mathematical society' in r['decoded_url'].lower()]
recent = [r for r in jims if re.search(r'19[6-9][0-9]|Golden|Jubilee', r['decoded_url'], re.I)]
payload = {'started_utc': started, 'elapsed_seconds': time.monotonic() - tick,
           'cached_paths': cached, 'initial_advertised_urls': initial_advertised,
           'requests': len(results), 'results': results, 'records': list(records.values()),
           'jims_count': len(jims), 'possible_post_1959_or_jubilee': recent,
           'remaining_advertised_pages': queued, 'stopped_on_access_denial': denied}
out = root / 'code/part_c_pfluger_tdl_inventory_delayed_output.json'
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
out.with_suffix('.txt').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'requests': len(results), 'elapsed_seconds': payload['elapsed_seconds'],
                  'records': len(records), 'jims_count': len(jims),
                  'possible_post_1959_or_jubilee': recent}, ensure_ascii=False, indent=2))
