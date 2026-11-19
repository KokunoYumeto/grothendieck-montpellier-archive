#!/usr/bin/env python3
"""Fetch publicly accessible primary sources and record byte provenance."""
import argparse, concurrent.futures, hashlib, json, time, urllib.request
from pathlib import Path

def fetch(pair):
    url, dest = pair
    start = time.perf_counter()
    p = Path(dest)
    p.parent.mkdir(parents=True, exist_ok=True)
    try:
        if p.exists() and p.stat().st_size:
            data = p.read_bytes()
            status = 'already present'
        else:
            with urllib.request.urlopen(url, timeout=80) as r:
                data = r.read()
            p.write_bytes(data)
            status = 'downloaded'
        return dict(url=url, path=str(p), status=status, bytes=len(data),
                    sha256=hashlib.sha256(data).hexdigest(),
                    seconds=round(time.perf_counter()-start,3))
    except Exception as e:
        return dict(url=url, path=str(p), status='failed', error=str(e),
                    seconds=round(time.perf_counter()-start,3))

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('manifest')
    parser.add_argument('log')
    args=parser.parse_args()
    pairs=json.loads(Path(args.manifest).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        results=list(ex.map(fetch,pairs))
    Path(args.log).write_text(json.dumps(results,indent=2)+'\n')
    for r in results:
        print(r['status'],r['path'],r.get('bytes',r.get('error')),r['seconds'])
