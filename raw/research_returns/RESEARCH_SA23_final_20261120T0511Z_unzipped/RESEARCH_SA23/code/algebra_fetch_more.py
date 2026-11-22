"""Reproducible parallel downloads of original EGA and Montpellier scans."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.request import urlopen
import hashlib
import time

root = Path(__file__).resolve().parents[1]
items = [
    ("algebra_manuscript23.pdf", "https://grothendieck.umontpellier.fr/23.pdf"),
    ("algebra_EGAIV4_mirror.pdf", "https://www.williamstein.org/sga/circle/EGAIV.4.pdf"),
    ("algebra_EGAIII1_mirror.pdf", "https://www.williamstein.org/sga/circle/EGAIII.1.pdf"),
]

def fetch(item):
    name, url = item
    start = time.perf_counter()
    try:
        with urlopen(url, timeout=35) as response:
            data = response.read()
            content_type = response.headers.get("Content-Type")
        (root / "sources" / name).write_bytes(data)
        return dict(file=name, url=url, content_type=content_type,
                    bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                    seconds=time.perf_counter()-start)
    except Exception as error:
        return dict(file=name, url=url, error=repr(error),
                    seconds=time.perf_counter()-start)

if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(fetch, items):
            print(result, flush=True)
