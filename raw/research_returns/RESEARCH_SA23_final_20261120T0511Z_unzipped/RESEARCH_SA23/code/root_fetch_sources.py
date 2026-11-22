"""Fetch explicitly identified primary sources; preserve full status and hashes."""
from pathlib import Path
import urllib.request, hashlib, time
SOURCES = {
    'abramovich_temkin_2018.pdf': 'https://content.algebraicgeometry.nl/2018-1/2018-1-003.pdf',
    'stacks_formal_smooth.html': 'https://stacks.math.columbia.edu/tag/00TH',
    'stacks_fields.html': 'https://stacks.math.columbia.edu/tag/031U',
}
folder = Path(__file__).resolve().parents[1] / 'sources'
folder.mkdir(exist_ok=True)
for name, url in SOURCES.items():
    start = time.perf_counter()
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Research source verification'})
        with urllib.request.urlopen(req,timeout=25) as response:
            data=response.read()
            print(name, response.status, response.headers.get('Content-Type'), len(data), hashlib.sha256(data).hexdigest())
        (folder/name).write_bytes(data)
    except Exception as exc:
        print(name, type(exc).__name__, str(exc))
    print('Elapsed seconds:', round(time.perf_counter()-start,6))
