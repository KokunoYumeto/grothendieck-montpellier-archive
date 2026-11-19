"""Check byte-range support for targeted inspection of an official scan."""
from pathlib import Path
import json
import time
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
url='https://grothendieck.umontpellier.fr/15.pdf'
start=time.perf_counter()
record={'url':url,'range':'bytes=0-511'}
try:
    req=urllib.request.Request(url,headers={'Range':'bytes=0-511'})
    with urllib.request.urlopen(req,timeout=20) as r:
        record['status']=r.status
        record['headers']=dict(r.headers)
        data=r.read(512)
        record['bytes_read']=len(data)
        record['pdf_signature']=data.startswith(b'%PDF')
except Exception as e:
    record['error']=repr(e)
record['runtime_seconds']=time.perf_counter()-start
(ROOT/'code/probe_montpellier_range_output.json').write_text(
    json.dumps(record,indent=2))
print(json.dumps(record,indent=2),flush=True)
