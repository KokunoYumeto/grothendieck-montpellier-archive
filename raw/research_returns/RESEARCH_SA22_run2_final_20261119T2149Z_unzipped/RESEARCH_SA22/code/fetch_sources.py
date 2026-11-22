#!/usr/bin/env python3
"""Fetch explicitly listed primary sources; log URL, status, bytes and elapsed time."""
from pathlib import Path
import argparse, hashlib, json, time, urllib.request

def fetch(url, target):
    start=time.monotonic()
    target=Path(target); target.parent.mkdir(parents=True, exist_ok=True)
    record={'url':url,'target':str(target),'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Research-SA22/1.0'})
        with urllib.request.urlopen(req,timeout=55) as r:
            payload=r.read(); record['http_status']=r.status
        target.write_bytes(payload)
        record.update(bytes=len(payload),sha256=hashlib.sha256(payload).hexdigest(),outcome='downloaded')
    except Exception as e:
        record.update(outcome='failed',error=f'{type(e).__name__}: {e}')
    record['seconds']=round(time.monotonic()-start,4)
    print(json.dumps(record),flush=True)
    return record

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('url');parser.add_argument('target');a=parser.parse_args()
    fetch(a.url,a.target)
