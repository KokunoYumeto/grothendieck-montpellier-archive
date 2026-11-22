#!/usr/bin/env python3
"""One hour-guarded ordinary GET of the previously observed Scholl homepage."""
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from html.parser import HTMLParser
from pathlib import Path
import json
import time
import urllib.parse
import urllib.request

root = Path(__file__).resolve().parents[1]
prior_path = root / 'code/part_c_lieberman_cambridge_http_output.json'
output_path = root / 'code/part_b_lieberman_cambridge_delayed_output.json'
if output_path.exists():
    raise SystemExit('Existing delayed-check output; no repeated request permitted.')
prior = json.loads(prior_path.read_text())
url = prior['url']
assert url == 'https://www.dpmms.cam.ac.uk/~ajs1005/'
assert prior['status'] == 503
eligible = datetime.fromisoformat(prior['started_utc']) + timedelta(hours=1)
now = datetime.now(timezone.utc)
if now < eligible:
    raise SystemExit(f'Not yet eligible; no request made. Eligible UTC: {eligible.isoformat()}')

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.words, self.current = [], [], None
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'a' and 'href' in a:
            self.current = {'href': urllib.parse.urljoin(url, a['href']), 'text': ''}
    def handle_data(self, text):
        self.words.append(text)
        if self.current is not None:
            self.current['text'] += text
    def handle_endtag(self, tag):
        if tag == 'a' and self.current is not None:
            self.links.append(self.current)
            self.current = None

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

started = datetime.now(timezone.utc)
tic = time.perf_counter()
out = {
    'started_utc': started.isoformat(),
    'url': url,
    'prior_record': str(prior_path),
    'prior_started_utc': prior['started_utc'],
    'prior_status': prior['status'],
    'eligible_utc': eligible.isoformat(),
    'elapsed_since_prior_start_seconds': (started - datetime.fromisoformat(prior['started_utc'])).total_seconds(),
    'ordinary_http_requests': 1,
    'automatic_redirects': False,
    'custom_access_headers': False,
    'timeout_seconds': 20,
    'maximum_body_bytes': 2097152,
    'automatic_retries': 0,
    'mathematical_checks': 0,
}
try:
    with urllib.request.build_opener(NoRedirect).open(url, timeout=20) as response:
        raw = response.read(2097153)
        assert len(raw) <= 2097152
        out.update(status=response.status, content_type=response.headers.get('Content-Type'),
                   response_bytes=len(raw), response_sha256=sha256(raw).hexdigest())
        cache = root.parent / 'source_reading/lieberman_cambridge'
        cache.mkdir(parents=True, exist_ok=True)
        destination = cache / 'part_b_scholl_home_delayed.html'
        destination.write_bytes(raw)
        out['raw_cache_path'] = str(destination)
        parser = Parser()
        parser.feed(raw.decode('utf-8', errors='replace'))
        out['advertised_links'] = parser.links
        text = ' '.join(parser.words).lower()
        out['target_literal_hits'] = {word: text.count(word.lower()) for word in ['Lieberman', 'Hodge manifolds', '2373533']}
        out['challenge_indicators'] = [word for word in ['verify you are human', 'captcha', 'access denied', 'just a moment'] if word in text]
except Exception as error:
    out.update(status=getattr(error, 'code', None), error_type=type(error).__name__, error=str(error))
out['completed_utc'] = datetime.now(timezone.utc).isoformat()
out['runtime_seconds'] = time.perf_counter() - tic
output_path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(out, ensure_ascii=False, indent=2))
