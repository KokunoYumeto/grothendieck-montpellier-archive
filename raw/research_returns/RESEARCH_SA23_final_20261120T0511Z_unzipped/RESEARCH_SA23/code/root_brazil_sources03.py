"""Inspect public MAST finding-aid links; never query the gated Zenith search."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin
import concurrent.futures, datetime, hashlib, json, time, urllib.request
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
items = [
    ('mast_public_hotsite', 'http://site.mast.br/hotsite_acervo_arquivistico/index.html'),
    ('mast_public_publications', 'https://www.gov.br/mast/pt-br/centrais-de-conteudo/publicacoes'),
]
class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.active = None
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'a':
            self.active = {'href': values.get('href', ''), 'text': ''}
        if tag == 'img' and self.active is not None:
            self.active['text'] += values.get('alt', '')
    def handle_data(self, data):
        if self.active is not None:
            self.active['text'] += data
    def handle_endtag(self, tag):
        if tag == 'a' and self.active is not None:
            self.links.append(self.active); self.active = None
def fetch(item):
    stem, url = item; begin = time.perf_counter(); record = {'name': stem, 'url': url}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read(); encoding = response.headers.get_content_charset() or 'utf-8'
            record.update({'status': response.status, 'final_url': response.url,
                           'content_type': response.headers.get('Content-Type'),
                           'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
        text = data.decode(encoding, errors='replace')
        (root / 'sources' / (stem + '.html')).write_text(text)
        parser = Links(); parser.feed(text)
        relevant = [dict(link, url=urljoin(record['final_url'], link['href']))
                    for link in parser.links
                    if any(term in (link['text'] + link['href']).casefold()
                           for term in ('nachbin', 'gama', 'invent', 'acervo', 'arquivo'))]
        record['relevant_public_links'] = relevant
    except Exception as error:
        record['error'] = str(error)
    record['elapsed_seconds'] = time.perf_counter() - begin
    return record
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    results = list(pool.map(fetch, items))
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'results': results, 'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_brazil_sources03.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
