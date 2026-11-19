"""Archive the primary texts used in the 05:05 checkpoint endpoint update."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
import hashlib
import json
import subprocess
import time

root = Path(__file__).resolve().parents[2]
sources = [
    ('Yamamura2026', 'https://arxiv.org/pdf/2608.01089v1'),
    ('RapoportZink1982', 'https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/UeberdielokaleZetafunktion.pdf'),
    ('KatzDeligne1973niveau', 'https://web.math.princeton.edu/~nmk/old/niveaucoho.pdf'),
    ('Procesi2021', 'https://arxiv.org/pdf/2011.10820'),
    ('Yin2015_published', 'https://ems.press/content/serial-article-files/43396'),
]

def fetch(item):
    name, url = item
    start = time.perf_counter()
    path = root / 'part_c/sources' / (name + '.pdf')
    result = dict(name=name, url=url)
    try:
        if not path.exists():
            with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=25) as response:
                data = response.read()
            assert data.startswith(b'%PDF'), 'not a PDF'
            path.write_bytes(data)
        data = path.read_bytes()
        subprocess.run(['pdftotext', '-layout', str(path), str(path.with_suffix('.txt'))], check=True)
        result.update(status='saved', bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as error:
        result.update(status='failed', error=str(error))
    result['runtime_seconds'] = time.perf_counter()-start
    return result

start = time.perf_counter()
with ThreadPoolExecutor(max_workers=5) as pool:
    results = list(pool.map(fetch, sources))
output = dict(sources=results, runtime_seconds=time.perf_counter()-start)
(root/'code/part_c/fetch_endpoint_sources_output.json').write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(output, indent=2))
