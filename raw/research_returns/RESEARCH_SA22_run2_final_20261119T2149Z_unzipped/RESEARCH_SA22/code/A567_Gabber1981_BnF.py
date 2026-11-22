"""Historical Gabber1981 preprint search through the observed public BnF form."""
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parents[1]
QUERIES = [
    ('exact_1981_title', '"Affine analog of proper base change theorem"'),
    ('title_variant', 'Gabber "Affine analogue"'),
    ('author_year', 'Gabber 1981'),
]

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []
        self.links = []
    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag in ('div', 'p', 'h1', 'h2', 'h3', 'li', 'tr', 'br'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
        if tag in ('div', 'p', 'h1', 'h2', 'h3', 'li', 'tr'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def fetch(item):
    name, query = item
    url = 'https://catalogue.bnf.fr/rechercher.do?' + urlencode({
        'motRecherche': query, 'critereRecherche': '0', 'depart': '0',
        'facetteModifiee': 'ok'})
    start = time.perf_counter()
    result = {'name': name, 'query': query, 'url': url}
    try:
        with urlopen(url, timeout=25) as response:
            data = response.read()
            result.update(http_status=response.status,
                          final_url=response.url,
                          content_type=response.headers.get('Content-Type'),
                          bytes=len(data),
                          sha256=hashlib.sha256(data).hexdigest())
        text = data.decode('utf-8', 'replace')
        path = ROOT / f'literature/A567_Gabber1981_BnF_{name}.html'
        path.write_text(text)
        parser = Parser()
        parser.feed(text)
        visible = '\n'.join(' '.join(line.split()) for line in
                            ''.join(parser.parts).splitlines() if line.strip())
        path.with_suffix('.txt').write_text(visible)
        result.update(saved_html=str(path.relative_to(ROOT)),
                      visible_text=visible, links=parser.links)
    except Exception as error:
        result['error'] = type(error).__name__ + ': ' + str(error)
    result['elapsed_seconds'] = time.perf_counter() - start
    return result

if __name__ == '__main__':
    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as pool:
        results = list(pool.map(fetch, QUERIES))
    report = {'date_utc': '2026-11-19', 'query_count': len(QUERIES),
              'elapsed_seconds': time.perf_counter() - start,
              'scope': 'Historical1981 preprint catalogue discovery only; ordinary public form; no account or requests to restricted full text',
              'results': results}
    (ROOT / 'logs/A567_Gabber1981_BnF.json').write_text(
        json.dumps(report, indent=2, ensure_ascii=False))
    for result in results:
        print(json.dumps({k: v for k, v in result.items()
                          if k not in ('links', 'visible_text')}, ensure_ascii=False))
        print(result.get('visible_text', '')[-6500:])
