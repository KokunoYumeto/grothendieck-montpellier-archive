"""Fetch and unpack the exact primary sources consulted for B.6/C.3.

ArXiv source files are preferred. This is a retrieval log, not a proof test.
"""
from pathlib import Path
import concurrent.futures, gzip, io, tarfile, time, urllib.request

ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
SOURCES.mkdir(exist_ok=True)
ITEMS = [
    ("C_berger_fresse", "https://arxiv.org/src/math/0109158v2"),
    ("C_monoidal_models", "https://arxiv.org/src/math/0506624v2"),
    ("C_porter_suciu", "https://arxiv.org/src/2105.10753v2"),
]

def fetch(item):
    name, url = item
    begin = time.monotonic()
    request = urllib.request.Request(url, headers={"User-Agent": "SA08-primary-source-check/1.0"})
    try:
        data = urllib.request.urlopen(request, timeout=50).read()
        (SOURCES / (name + ".source")).write_bytes(data)
        output = SOURCES / name
        output.mkdir(exist_ok=True)
        try:
            with tarfile.open(fileobj=io.BytesIO(data)) as archive:
                archive.extractall(output, filter="data")
        except tarfile.ReadError:
            try:
                data = gzip.decompress(data)
            except OSError:
                pass
            (output / "source.tex").write_bytes(data)
        return name, url, len(data), f"{time.monotonic()-begin:.3f}", "OK"
    except Exception as error:
        return name, url, 0, f"{time.monotonic()-begin:.3f}", repr(error)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    rows = list(pool.map(fetch, ITEMS))
text = "name\turl\tbytes\tseconds\tstatus\n" + "".join("\t".join(map(str, row)) + "\n" for row in rows)
(ROOT / "logs" / "C_more_sources_fetch.tsv").write_text(text)
print(text)
