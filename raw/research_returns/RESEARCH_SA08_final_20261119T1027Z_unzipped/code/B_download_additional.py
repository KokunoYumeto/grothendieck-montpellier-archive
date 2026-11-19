"""Fetch the two additional primary sources requested during the audit."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import Request, urlopen
import hashlib, json, subprocess, time

base = Path(__file__).resolve().parents[1]
items = [
    ('B_cenkl_porter1982', 'https://mat.uab.cat/~pubmat/fitxers/download/FileType%3Apdf/FolderName%3Av26%283%29/FileName%3A26382_01.pdf'),
    ('B_mandell2001', 'https://mmandell.pages.iu.edu/papers/einffinal.pdf'),
]

def fetch(item):
    name, url = item
    started = time.monotonic()
    try:
        with urlopen(Request(url, headers={'User-Agent':'SA08 primary-source verification'}), timeout=55) as response:
            data = response.read()
        pdf = base / 'sources' / (name + '.pdf')
        pdf.write_bytes(data)
        subprocess.run(['pdftotext', '-layout', str(pdf), str(pdf.with_suffix('.txt'))], check=True)
        result = dict(name=name, url=url, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as error:
        result = dict(name=name, url=url, error=repr(error))
    result['seconds'] = time.monotonic() - started
    print(json.dumps(result), flush=True)
    return result

with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(fetch, items))
(base/'logs'/'B_additional_downloads.json').write_text(json.dumps(results, indent=2))
