"""Open the actual new1959 catalogue link returned by the public date form.

Read public record metadata and report its advertised anchors, frames, image
sources and embedded objects. Do not infer or request any content URL.
"""
import datetime
import hashlib
import html.parser
import json
import pathlib
import time
import urllib.error
import urllib.request

root = pathlib.Path(__file__).resolve().parents[1]
class Links(html.parser.HTMLParser):
    def __init__(self): super().__init__(); self.items = []; self.current = None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'a': self.current = {'tag': tag, 'url': a.get('href', ''), 'text': ''}
        if tag in ('iframe', 'img', 'object', 'embed', 'script'):
            self.items.append({'tag': tag, 'attrs': a})
    def handle_data(self, value):
        if self.current is not None: self.current['text'] += value
    def handle_endtag(self, tag):
        if tag == 'a' and self.current is not None:
            self.items.append(self.current); self.current = None

started = datetime.datetime.now(datetime.timezone.utc).isoformat(); tick = time.monotonic()
result_path = root / 'sources/part_c_pfluger_tdl_delayed_periodical_session_results.txt'
response = json.loads(result_path.read_text())
parser = Links(); parser.feed(response['html'])
url = next(r['url'] for r in parser.items if r.get('tag') == 'a' and '-26669-' in r.get('url', ''))
record = {'url': url, 'method': 'GET', 'from_actual_result_file': str(result_path)}
try:
    with urllib.request.urlopen(url, timeout=40) as page:
        body = page.read(); destination = root / 'sources/part_c_pfluger_tdl_1959_record.html'
        destination.write_bytes(body); document = Links(); document.feed(body.decode('utf-8', 'replace'))
        record.update(status=page.status, final_url=page.url, bytes=len(body),
                      sha256=hashlib.sha256(body).hexdigest(), saved_path=str(destination),
                      advertised_elements=document.items)
except Exception as error:
    record['error'] = type(error).__name__ + ': ' + str(error)
    if isinstance(error, urllib.error.HTTPError): record['status'] = error.code
payload = {'started_utc': started, 'elapsed_seconds': time.monotonic() - tick,
           'requests': 1, 'result': record}
output = root / 'code/part_c_pfluger_tdl_1959_record_output.json'
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
output.with_suffix('.txt').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
summary = {k: v for k, v in record.items() if k != 'advertised_elements'}
summary['advertised_relevant'] = [r for r in record.get('advertised_elements', [])
                                 if any(t in json.dumps(r).lower() for t in ('pdf', 'read', 'download', '26669', '00586', 'related'))]
print(json.dumps({'started_utc': started, 'elapsed_seconds': payload['elapsed_seconds'], 'result': summary}, ensure_ascii=False, indent=2))
