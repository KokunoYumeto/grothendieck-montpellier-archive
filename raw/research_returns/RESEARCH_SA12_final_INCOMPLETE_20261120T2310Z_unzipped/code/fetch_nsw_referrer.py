"""Retry the authors' public electronic edition using its download-page referrer."""
from pathlib import Path
from datetime import datetime,timezone
import urllib.request,hashlib,json,time
root=Path(__file__).resolve().parents[1];base='https://www.mathi.uni-heidelberg.de/~schmidt/NSW2e/'
dest=root/'sources/NSW/NSW2.3.pdf';start=time.perf_counter()
if dest.exists() and not dest.read_bytes().startswith(b'%PDF'):
    dest.rename(dest.with_name('NSW_index_received.html'))
req=urllib.request.Request(base+'NSW2.3.pdf',headers={'User-Agent':'Mozilla/5.0','Referer':base})
with urllib.request.urlopen(req,timeout=45) as response:
    data=response.read();final=response.url;ct=response.headers.get('Content-Type')
if not data.startswith(b'%PDF'):
    path=dest.with_name('NSW_retry_received.html');path.write_bytes(data)
    print({'outcome':'public server returned HTML again','url':final,'content_type':ct,'bytes':len(data),'seconds':time.perf_counter()-start})
    raise SystemExit(2)
dest.write_bytes(data)
meta={'requested_url':base+'NSW2.3.pdf','final_url':final,'utc':datetime.now(timezone.utc).isoformat(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'seconds':time.perf_counter()-start}
dest.with_name(dest.name+'.provenance.json').write_text(json.dumps(meta,indent=2)+'\n');print(meta)
