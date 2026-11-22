"""Retrieve the newly identified public MAST inventory and portal metadata."""
from pathlib import Path
import concurrent.futures, datetime, hashlib, json, time, urllib.request
import fitz
root = Path(__file__).resolve().parents[1]
started = time.perf_counter()
items = [
    ('mast_cnpq_inventory2025', 'https://www.gov.br/mast/pt-br/imagens/publicacoes/2025/InventarioCNPq.pdf/@@display-file/file'),
    ('mast_zenith_portal', 'http://zenith.mast.br/c_home.php'),
    ('mast_archive_news2016', 'https://www.gov.br/mast/pt-br/coordenacao-de-documentacao-e-arquivo/arqvivo-1/arqvivo_2016_02.pdf'),
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
        record['sha256'] = hashlib.sha256(data).hexdigest()
        if data.startswith(b'%PDF'):
            path = root / 'sources' / (stem + '.pdf')
            path.write_bytes(data)
            document = fitz.open(path)
            record['pages'] = len(document)
            texts = [page.get_text() for page in document]
            (root / 'sources' / (stem + '_full.txt')).write_text('\n\f\n'.join(texts))
            hits = [{'pdf_page': number, 'text': text}
                    for number, text in enumerate(texts, 1)
                    if any(term.casefold() in text.casefold()
                           for term in ('Grothendieck', 'Fredholm', 'Nachbin', '6.3.003', 'Zenith'))]
            (root / 'notes' / (stem + '_hits.json')).write_text(json.dumps(hits, ensure_ascii=False, indent=2) + '\n')
            record['hit_pages'] = [hit['pdf_page'] for hit in hits]
        else:
            (root / 'sources' / (stem + '.html')).write_bytes(data)
            record['bounded_preview'] = data[:500].decode(errors='replace')
    except Exception as error:
        record['error'] = str(error)
    record['elapsed_seconds'] = time.perf_counter() - begin
    return record
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, items))
record = {'created_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'results': results, 'elapsed_seconds': time.perf_counter() - started}
(root / 'logs/root_brazil_sources02.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(record, ensure_ascii=False, indent=2))
