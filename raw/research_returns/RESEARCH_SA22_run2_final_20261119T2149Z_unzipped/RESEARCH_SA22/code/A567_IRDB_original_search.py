"""Bounded, unauthenticated IRDB catalogue searches through its observed form."""
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
    ('gabber_doi', {'doi': '10.1007/BF02773001'}),
    ('fujiwara_doi', {'doi': '10.1215/S0012-7094-95-08002-8'}),
    ('gabber_title', {'title': 'Affine analog of the proper base change theorem'}),
    ('fujiwara_title', {'title': 'tubular neighborhood'}),
]

class TextParser(HTMLParser):
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
    name, fields = item
    url = 'https://irdb.nii.ac.jp/en/search?' + urlencode(
        {'fulltextflg': 'All', **fields, 'op': 'Search'})
    started = time.perf_counter()
    result = {'name': name, 'fields': fields, 'url': url}
    try:
        with urlopen(url, timeout=25) as response:
            data = response.read()
            result.update(http_status=response.status,
                          final_url=response.url,
                          content_type=response.headers.get('Content-Type'),
                          bytes=len(data),
                          sha256=hashlib.sha256(data).hexdigest())
        html = data.decode('utf-8', 'replace')
        path = ROOT / f'literature/A567_IRDB_{name}.html'
        path.write_text(html)
        parser = TextParser()
        parser.feed(html)
        visible = '\n'.join(' '.join(line.split()) for line in
                            ''.join(parser.parts).splitlines() if line.strip())
        path.with_suffix('.txt').write_text(visible)
        result.update(saved_html=str(path.relative_to(ROOT)),
                      visible_text=visible, links=parser.links)
    except Exception as error:
        result.update(error=type(error).__name__ + ': ' + str(error))
    result['elapsed_seconds'] = time.perf_counter() - started
    return result

if __name__ == '__main__':
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, QUERIES))
    report = {
        'date_utc': '2026-11-19',
        'scope': 'Four ordinary public GET queries using IRDB observed advanced-search form; no authentication or alternate full-text endpoint',
        'query_count': len(QUERIES),
        'elapsed_seconds': time.perf_counter() - started,
        'results': results,
    }
    (ROOT / 'logs/A567_IRDB_original_search.json').write_text(
        json.dumps(report, indent=2, ensure_ascii=False))
    for result in results:
        print(json.dumps({key: value for key, value in result.items()
                          if key not in ('links', 'visible_text')}, ensure_ascii=False))
        print(result.get('visible_text', '')[-6500:])
