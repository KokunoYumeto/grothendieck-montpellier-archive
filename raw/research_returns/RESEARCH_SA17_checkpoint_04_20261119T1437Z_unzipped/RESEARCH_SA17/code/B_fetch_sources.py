"""Fetch Part B's primary sources; preserve downloads outside the deliverable tree."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json, time, urllib.request

DEST = Path('/workspace/scratch/b00be283d10d/fetched/B')
SOURCES = {
    'lau_relations.pdf': 'https://arxiv.org/pdf/1006.2720',
    'zink_display.pdf': 'https://www.math.uni-bielefeld.de/~zink/display.pdf',
    'kothari_mundinger_2026.pdf': 'https://arxiv.org/pdf/2609.30586',
    'mondal_2024.pdf': 'https://arxiv.org/pdf/2405.12967',
    'gardner_madapusi.pdf': 'https://arxiv.org/pdf/2412.10226',
    'lau_divided.tex.tar': 'https://arxiv.org/src/1811.09439v2',
    'anschutz_lebras.tex.tar': 'https://arxiv.org/src/1907.10525',
    'breuil_2000.pdf': 'https://arxiv.org/pdf/math/0009252',
    'kisin_crystals.dvi': 'https://www.math.harvard.edu/~kisin/dvifiles/wam.dvi',
}

def fetch(pair):
    name, url = pair
    path = DEST / name
    start = time.monotonic()
    if path.exists(): return {'file': name, 'status': 'already present', 'bytes':path.stat().st_size}
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            data = r.read()
        path.write_bytes(data)
        return {'file':name,'url':url,'bytes':len(data),'seconds':time.monotonic()-start,'status':'downloaded'}
    except Exception as e:
        return {'file':name,'url':url,'error':str(e),'seconds':time.monotonic()-start,'status':'failed'}

if __name__ == '__main__':
    DEST.mkdir(parents=True, exist_ok=True)
    for result in ThreadPoolExecutor(7).map(fetch, SOURCES.items()):
        print(json.dumps(result),flush=True)
