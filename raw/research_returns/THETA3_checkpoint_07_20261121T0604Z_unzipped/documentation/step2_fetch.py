"""Recover only named public pinned modules; never execute their contents."""
import concurrent.futures
import datetime
import hashlib
import json
from pathlib import Path
import sys
import urllib.request

root = Path(__file__).resolve().parent
repo = root / 'alpoge_mirror'
commit = json.loads((repo / 'provenance.json').read_text())['commit']
paths = [p.strip().removeprefix('src/') for p in Path(sys.argv[1]).read_text().splitlines() if p.strip()]
manifest = root / 'step2_archive_manifest.json'
old = json.loads(manifest.read_text()) if manifest.exists() else {}

def fetch(path):
    dest = repo / path
    url = f'https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/{commit}/src/{path}'
    if dest.exists():
        data = dest.read_bytes()
    else:
        data = urllib.request.urlopen(url, timeout=35).read()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    return path, {'url': url, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                  'git_blob_sha1': hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),
                  'observed_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    futures = {pool.submit(fetch,p):p for p in paths}
    for future in concurrent.futures.as_completed(futures):
        path = futures[future]
        try:
            path, entry = future.result()
            old[path] = entry
            print(path, entry['bytes'], flush=True)
        except Exception as exc:
            old[path] = {'error': str(exc)}
            print(path, 'ERROR', str(exc), flush=True)
manifest.write_text(json.dumps(old, indent=2))
