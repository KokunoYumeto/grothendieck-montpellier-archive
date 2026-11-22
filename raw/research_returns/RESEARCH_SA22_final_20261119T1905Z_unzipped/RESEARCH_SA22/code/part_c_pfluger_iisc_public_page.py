"""Read one observed public institutional catalogue page and its actual links.

Arguments are a previously observed URL and a provenance tag. This utility
does not submit login forms, solve challenges, infer endpoints or fetch files.
"""
import datetime
import hashlib
import html.parser
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

root = pathlib.Path(__file__).resolve().parents[1]
url, tag = sys.argv[1:3]
assert re.fullmatch(r'[a-z0-9_]+', tag)
class Inspect(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.forms = []; self.scripts = []; self.text = []; self.current = None; self.form = None
    def handle_starttag(self, name, attrs):
        a = dict(attrs)
        if name == 'a': self.current = {'url': a.get('href', ''), 'text': ''}
        if name == 'form': self.form = {'attrs': a, 'controls': []}
        if self.form is not None and name in ('input', 'button', 'select', 'option'):
            self.form['controls'].append({'tag': name, 'attrs': a})
        if name in ('script', 'iframe') and a.get('src'): self.scripts.append({'tag': name, 'src': a['src']})
    def handle_data(self, data):
        self.text.append(data)
        if self.current is not None: self.current['text'] += data
    def handle_endtag(self, name):
        if name == 'a' and self.current is not None:
            self.current['text'] = ' '.join(self.current['text'].split()); self.links.append(self.current); self.current = None
        if name == 'form' and self.form is not None: self.forms.append(self.form); self.form = None

start = datetime.datetime.now(datetime.timezone.utc).isoformat(); tick = time.monotonic()
record = {'url': url, 'method': 'GET'}
try:
    with urllib.request.urlopen(url, timeout=40) as response:
        body = response.read(); value = body.decode('utf-8', 'replace')
        destination = root / 'sources' / ('part_c_pfluger_iisc_' + tag + '.html'); destination.write_bytes(body)
        parser = Inspect(); parser.feed(value)
        record.update(status=response.status, final_url=response.url, bytes=len(body),
                      sha256=hashlib.sha256(body).hexdigest(), saved_path=str(destination),
                      links=parser.links, forms=parser.forms, scripts=parser.scripts)
        (destination.with_suffix('.txt')).write_text('\n'.join(x.strip() for x in parser.text if x.strip()))
except Exception as error:
    record['error'] = type(error).__name__ + ': ' + str(error)
    if isinstance(error, urllib.error.HTTPError): record['status'] = error.code
payload = {'started_utc': start, 'elapsed_seconds': time.monotonic() - tick, 'requests': 1, 'result': record}
output = root / 'code' / ('part_c_pfluger_iisc_' + tag + '_output.json')
output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
output.with_suffix('.txt').write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
summary = {k: v for k, v in record.items() if k != 'links'}
summary['relevant_links'] = [r for r in record.get('links', []) if re.search(r'catalog|opac|eprint|digital|journ|search', str(r), re.I)]
print(json.dumps({'started_utc': start, 'elapsed_seconds': payload['elapsed_seconds'], 'result': summary}, ensure_ascii=False, indent=2))
