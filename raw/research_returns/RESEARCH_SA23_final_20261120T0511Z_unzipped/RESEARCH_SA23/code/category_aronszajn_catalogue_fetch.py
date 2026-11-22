"""Read public KU catalogue pages and record their advertised links/forms."""
from pathlib import Path
from datetime import datetime, timezone
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import hashlib, json, urllib.request

ROOT = Path(__file__).resolve().parents[1]
pages = {
    'resource11': 'https://archives.lib.ku.edu/repositories/3/resources/11',
    'publications43': 'https://archives.lib.ku.edu/repositories/3/archival_objects/43',
    'notes44': 'https://archives.lib.ku.edu/repositories/3/archival_objects/44',
    'homepage': 'https://archives.lib.ku.edu/',
}
def get(job):
    name, url = job
    row = {'name': name, 'url': url, 'utc': datetime.now(timezone.utc).isoformat()}
    class PublicRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            if urlparse(newurl).hostname != 'archives.lib.ku.edu':
                raise ValueError('Unexpected redirect host')
            return super().redirect_request(req, fp, code, msg, headers, newurl)
    try:
        with urllib.request.build_opener(PublicRedirect).open(url, timeout=35) as r:
            data = r.read(); row.update(status=r.status, final_url=r.url)
        file = ROOT / 'sources' / f'category_aronszajn_{name}.html'
        file.write_bytes(data)
        row.update(path=str(file.relative_to(ROOT)), sha256=hashlib.sha256(data).hexdigest())
        soup = BeautifulSoup(data, 'html.parser')
        row['links'] = [{'text': a.get_text(' ', strip=True), 'href': a['href']} for a in soup.select('a[href]')]
        row['forms'] = [{'action': f.get('action'), 'method': f.get('method'),
                         'inputs': [{k: i.get(k) for k in ['name','value','type']} for i in f.select('input')],
                         'selects': [{k: s.get(k) for k in ['name','id']} for s in f.select('select')]}
                        for f in soup.select('form')]
        row['data_attributes'] = [{'tag': e.name, 'attributes': e.attrs} for e in soup.find_all()
                                  if any(k.startswith('data-') for k in e.attrs)]
        file.with_suffix('.txt').write_text(soup.get_text('\n', strip=True))
    except Exception as error: row['error'] = repr(error)
    return row
rows=[]
with ThreadPoolExecutor(max_workers=4) as pool:
    for future in as_completed([pool.submit(get, job) for job in pages.items()]):
        row=future.result(); rows.append(row)
        print(json.dumps(row, ensure_ascii=False), flush=True)
        (ROOT/'logs/category_aronszajn_catalogue_fetch.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
