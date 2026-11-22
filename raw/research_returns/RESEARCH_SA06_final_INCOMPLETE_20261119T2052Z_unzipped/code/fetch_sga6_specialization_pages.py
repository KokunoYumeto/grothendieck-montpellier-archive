#!/usr/bin/env python3
"""Acquire original page scans and OCR a bounded SGA6 specialization range."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen
from time import perf_counter
import hashlib, json, subprocess

root=Path(__file__).resolve().parents[1]
out=root/'sources/sga6_specialization';out.mkdir(exist_ok=True,parents=True)
started=datetime.now(timezone.utc).isoformat();tick=perf_counter()
def fetch(n):
    page=f'6t_{n:03}'
    url=f'https://wstein.org/sga/sga/6/{page}.jpeg'
    rec={'printed_page':n,'url':url};t0=perf_counter()
    try:
        with urlopen(url,timeout=30) as r:data=r.read()
        target=out/(page+'.jpeg');target.write_bytes(data)
        rec.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),path=str(target))
        proc=subprocess.run(['tesseract',str(target),str(out/page),'-l','eng'],capture_output=True,text=True,timeout=30)
        rec.update(ocr_returncode=proc.returncode,ocr_stderr=proc.stderr)
    except Exception as e:rec['error']=str(e)
    rec['runtime_seconds']=perf_counter()-t0
    return rec
with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(fetch,range(570,585)))
record={'started_utc':started,'completed_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':perf_counter()-tick,'pages':records,'scope':'Acquisition and OCR only. Original images must be read before any source-audit claim.'}
(root/'logs/sga6_specialization_acquisition.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
