"""Capture the exact primary PDFs used in the final B3 descent audit."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import time
import urllib.request

DEST = Path('/workspace/scratch/6215ed17d0f0/primary_sources/part_b')
LOG = Path('/workspace/scratch/6215ed17d0f0/RESEARCH_SA05_work/part_b/output/b3_primary_capture.json')
ITEMS = [
 ('bhatt_scholze2017_witt.pdf', 'https://people.mpim-bonn.mpg.de/scholze/Witt.pdf'),
 ('jaffe1994.pdf', 'https://arxiv.org/pdf/alg-geom/9410009'),
 ('riou2014.pdf', 'https://www.numdam.org/item/AST_2014__363-364__301_0.pdf'),
 ('geisser_morin2022.pdf', 'https://www.math.u-bordeaux.fr/~bmorin/Brauer_for_print.pdf'),
 ('ct_skorobogatov2019.pdf', 'https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf'),
]

def capture(item):
    name, url = item
    start = time.monotonic()
    try:
        target = DEST / name
        if target.exists():
            data = target.read_bytes()
            status = 'already present'
        else:
            request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(request, timeout=35) as response:
                data = response.read()
            if not data.startswith(b'%PDF'):
                raise ValueError('Endpoint did not return a PDF')
            target.write_bytes(data)
            status = 'downloaded'
        return {'name': name, 'url': url, 'status': status, 'bytes': len(data),
                'sha256': hashlib.sha256(data).hexdigest(),
                'seconds': round(time.monotonic()-start, 3)}
    except Exception as exc:
        return {'name': name, 'url': url, 'status': 'not obtained',
                'reason': str(exc), 'seconds': round(time.monotonic()-start, 3)}

DEST.mkdir(parents=True, exist_ok=True)
LOG.parent.mkdir(parents=True, exist_ok=True)
with ThreadPoolExecutor(max_workers=5) as pool:
    records = list(pool.map(capture, ITEMS))
LOG.write_text(json.dumps(records, indent=2) + '\n')
print(json.dumps(records, indent=2))
