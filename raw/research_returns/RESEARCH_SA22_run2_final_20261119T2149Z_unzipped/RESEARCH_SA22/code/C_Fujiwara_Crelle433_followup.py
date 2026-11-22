#!/usr/bin/env python3
"""Bounded public-link follow-up to the actual Crelle 433 catalogue hit.

Fetch exactly one URL already advertised in a supplied saved source file.
No invented endpoint, authentication, retries, or mathematical test. Each
invocation appends its actual request, source and response hashes, timestamps,
and measured runtime. The caller inspects the response before another request.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path
import time
from datetime import datetime, timezone
import urllib.request
import urllib.error

ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / 'logs/C_Fujiwara_Crelle433_followup.json'
OUT = ROOT / 'literature/C_Fujiwara_Crelle433_followup'

def now():
    return datetime.now(timezone.utc).isoformat()

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--url', required=True)
    p.add_argument('--source', required=True)
    p.add_argument('--name', required=True)
    args = p.parse_args()
    source = ROOT / args.source
    raw = source.read_bytes()
    advertised = html.unescape(raw.decode('utf-8', errors='replace')).replace('\\/', '/')
    if args.url not in advertised:
        raise SystemExit('Refusing URL not literally advertised in the supplied source.')
    if datetime.now(timezone.utc) >= datetime(2026, 11, 19, 21, 35, tzinfo=timezone.utc):
        raise SystemExit('Bounded follow-up deadline reached; no request made.')
    OUT.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    rec = dict(started_utc=now(), url=args.url, advertised_in=args.source,
               source_sha256=hashlib.sha256(raw).hexdigest(),
               program_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               scope='One ordinary GET to a literally advertised public link; no retries or mathematics.')
    try:
        try:
            r = urllib.request.urlopen(args.url, timeout=20)
        except urllib.error.HTTPError as e:
            r = e
        body = r.read()
        path = OUT / args.name
        path.write_bytes(body)
        rec.update(status_code=r.status, final_url=r.geturl(),
                   redirect_note='Final URL recorded; intermediate redirect responses not retained by urllib.',
                   content_type=r.headers.get('Content-Type'), bytes=len(body),
                   response_sha256=hashlib.sha256(body).hexdigest(),
                   saved_as=str(path.relative_to(ROOT)))
    except Exception as e:
        rec.update(error_type=type(e).__name__, error=str(e))
    rec.update(finished_utc=now(), elapsed_seconds=time.perf_counter()-start,
               requests_count=1, mathematical_checks_count=0)
    records = json.loads(LOG.read_text()) if LOG.exists() else []
    records.append(rec)
    LOG.write_text(json.dumps(records, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps(rec, indent=2, ensure_ascii=False))

if __name__ == '__main__':
    main()
