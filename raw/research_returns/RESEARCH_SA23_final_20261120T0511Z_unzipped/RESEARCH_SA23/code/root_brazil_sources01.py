"""Fetch publicly cited Brazilian archival material; retain failures as failures."""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, time
import urllib.request
import fitz

root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
items = [
    ('mast_lelio_inventory', 'https://www.mast.br/inventarios/inventarios_lelio_gama.pdf'),
    ('brazil_alcaires2021', 'https://www.crephimat.com.br/docs/T/T-HEdM/2021%20-%20T%20-%20Raphael%20Alcaires.pdf'),
    ('brazil_azevedo2009', 'https://rmu.sbm.org.br/wp-content/uploads/sites/27/2018/03/n44_Artigo04.pdf'),
]

def fetch(item):
    stem, url = item
    begin = time.perf_counter()
    record = {'name': stem, 'url': url}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            data = response.read()
            record.update({'status': response.status, 'final_url': response.url,
                           'content_type': response.headers.get('Content-Type'),
                           'bytes': len(data)})
        if record['status'] == 200 and data.startswith(b'%PDF'):
            path = root / 'sources' / (stem + '.pdf')
            path.write_bytes(data)
            record['sha256'] = hashlib.sha256(data).hexdigest()
            document = fitz.open(path)
            record['pages'] = len(document)
            texts = [page.get_text() for page in document]
            (root / 'sources' / (stem + '_full.txt')).write_text('\n\f\n'.join(texts))
            terms = ('Grothendieck', 'Fredholm', 'Nachbin', 'Summa', '6 de dezembro de 1954')
            hits = []
            for number, text in enumerate(texts, 1):
                if any(term.casefold() in text.casefold() for term in terms):
                    hits.append({'pdf_page': number, 'text': text})
            (root / 'notes' / (stem + '_hits.json')).write_text(json.dumps(hits, ensure_ascii=False, indent=2) + '\n')
            record['hit_pages'] = [item['pdf_page'] for item in hits]
        else:
            record['opened_original'] = False
            record['bounded_failure'] = data[:350].decode(errors='replace')
    except Exception as error:
        record['error'] = str(error)
    record['elapsed_seconds'] = time.perf_counter() - begin
    return record

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, items))
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'results': results, 'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_brazil_sources01.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
