"""Read-only retrieval of public candidate Lean files for K17 source recovery.

Input manifest records Git blob SHA-1 identifiers from the public mirror API.
The script verifies every response against its blob ID. It does not execute Lean.
"""
from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json
import time
import sys

ROOT = Path(__file__).resolve().parent
REV = (ROOT / 'lean_mirror_commit.txt').read_text().strip() if (ROOT / 'lean_mirror_commit.txt').exists() else 'main'
BASE = 'https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/' + REV + '/'
MANIFEST = sys.argv[1] if len(sys.argv) > 1 else 'lean_candidate_manifest.json'
FILES = json.loads((ROOT / MANIFEST).read_text())

def fetch(item):
    path = item['path']
    out = ROOT / 'lean_candidates' / path
    last_error = None
    for attempt in range(2):
        try:
            with urlopen(Request(BASE + path, headers={'User-Agent': 'K17-source-review'}), timeout=25) as response:
                data = response.read()
            blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
            if blob != item['sha']:
                raise ValueError('Git blob mismatch')
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(data)
            return dict(item, status='verified', size=len(data), sha256=hashlib.sha256(data).hexdigest())
        except Exception as error:
            last_error = type(error).__name__ + ': ' + str(error)
    return dict(item, status='failed', error=last_error)

if __name__ == '__main__':
    results = []
    with ThreadPoolExecutor(max_workers=12) as pool:
        for future in as_completed([pool.submit(fetch, item) for item in FILES]):
            results.append(future.result())
            if len(results) % 50 == 0:
                print('Retrieved', len(results), 'of', len(FILES), flush=True)
    results.sort(key=lambda item: item['path'])
    (ROOT / (Path(MANIFEST).stem + '_results.json')).write_text(json.dumps(results, indent=2))
    print('Verified:', sum(item['status']=='verified' for item in results), 'of', len(results))
    for item in results:
        if item['status'] != 'verified':
            print(item['path'], item['error'])
