"""Download identified public primary PDFs for inspection; external/ is not a deliverable."""
from pathlib import Path
import urllib.request,sys,json,hashlib,datetime
import fitz
OUT=Path(__file__).resolve().parents[1]
EXTERNAL=OUT.parents[2]/'public_sources'/'agent45'
EXTERNAL.mkdir(parents=True,exist_ok=True)
url,name=sys.argv[1:]
record={'url':url,'name':name,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
try:
    req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (research source verification)'})
    with urllib.request.urlopen(req,timeout=25) as response:
        raw=response.read()
        record['resolved_url']=response.url.split('?')[0]
    if not raw.startswith(b'%PDF'):
        raise ValueError('The returned object is not a PDF')
    dest=EXTERNAL/name
    dest.write_bytes(raw)
    doc=fitz.open(dest)
    dest.with_suffix('.txt').write_text('\n'.join(page.get_text() for page in doc))
    record.update(status='opened',pages=len(doc),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
except Exception as exc:
    record.update(status='failed',error=type(exc).__name__+': '+str(exc))
print(json.dumps(record))
