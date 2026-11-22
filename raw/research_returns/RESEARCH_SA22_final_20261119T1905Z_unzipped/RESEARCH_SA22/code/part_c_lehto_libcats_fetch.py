"""Fetch one actual advertised public book link into private reading storage."""
import datetime
import hashlib
import json
from pathlib import Path
import time
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
READING=ROOT.parent/'source_reading'
READING.mkdir(exist_ok=True)
url='https://libcats.org/dl/1088544/c81b4b'
begin=time.perf_counter()
result={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'scope':'One ordinary publicly advertised download, without credentials, tokens, mirrors, or challenge workaround; full book kept outside deliverable.'}
try:
    request=urllib.request.Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'})
    with urllib.request.urlopen(request,timeout=55) as response:
        data=response.read()
        result.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),md5=hashlib.md5(data).hexdigest(),magic=data[:24].hex())
    suffix='.djvu' if data.startswith(b'AT&TFORM') else ('.pdf' if data.startswith(b'%PDF') else '.html')
    path=READING/('lehto_virtanen1973'+suffix)
    path.write_bytes(data)
    result['saved']=str(path)
except Exception as error:
    result['error']=repr(error)
result['elapsed_seconds']=time.perf_counter()-begin
text=json.dumps(result,indent=2)
(ROOT/'code'/'part_c_lehto_libcats_fetch_output.json').write_text(text+'\n')
print(text)
