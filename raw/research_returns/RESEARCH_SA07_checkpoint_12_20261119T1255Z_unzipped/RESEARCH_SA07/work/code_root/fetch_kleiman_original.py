"""Retain primary-source access results; no mathematical computation."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from time import perf_counter
from urllib.request import Request, urlopen
import json
import fitz

HERE = Path(__file__).resolve().parent
DEST = HERE.parent / 'sources_root_after11'
DEST.mkdir(exist_ok=True)
sources = [
    ('Kleiman1968', 'https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf'),
    ('Lieberman1968_JSTOR_attempt', 'https://www.jstor.org/stable/pdf/2373533.pdf'),
]

def retrieve(item):
    name, url = item
    start = datetime.now(timezone.utc).isoformat()
    tick = perf_counter()
    record = {'name': name, 'url': url, 'actual_start_utc': start}
    try:
        request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(request, timeout=30) as response:
            raw = response.read()
            record.update(status=response.status, final_url=response.geturl(),
                          content_type=response.headers.get('Content-Type', ''),
                          bytes=len(raw), sha256=sha256(raw).hexdigest())
        is_pdf = raw.startswith(b'%PDF-')
        record['actual_pdf'] = is_pdf
        if is_pdf:
            path = DEST / (name + '.pdf')
            path.write_bytes(raw)
            pdf = fitz.open(path)
            record['pages'] = len(pdf)
            path.with_suffix('.txt').write_text('\n'.join(page.get_text() for page in pdf))
            if name == 'Kleiman1968':
                for pageno in [18, 21]:
                    pdf[pageno].get_pixmap(matrix=fitz.Matrix(1.5, 1.5)).save(
                        DEST / f'{name}_p{359+pageno}.png')
    except Exception as error:
        record['error'] = type(error).__name__ + ': ' + str(error)
    record['elapsed_seconds'] = perf_counter() - tick
    return record

with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(retrieve, sources))
output = json.dumps(records, indent=2) + '\n'
HERE.joinpath('fetch_kleiman_original.json').write_text(output)
HERE.joinpath('fetch_kleiman_original.out').write_text(output)
print(output)
