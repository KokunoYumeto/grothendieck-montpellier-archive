"""Archive the exact primary sources opened for the conditional C.1 audit."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from urllib.request import Request, urlopen

root = Path(__file__).resolve().parent
out = root/'sources'
out.mkdir(exist_ok=True)
sources = [
    ('Heidersdorf2018MixedTensors', 'https://arxiv.org/pdf/1406.0444', 'pdf'),
    ('MasuokaShibata2016Supergroups', 'https://arxiv.org/pdf/1304.0531', 'pdf'),
    ('Masuoka2012HarishChandra', 'https://arxiv.org/pdf/1111.2387', 'pdf'),
    ('LehrerZhang2021SuperFFT', 'https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/second-fundamental-theorem-of-invariant-theory-for-the-orthosymplectic-supergroup/C0A3AB442E2DAB0D9F7EECD88DF8AE3E', 'html'),
]

def fetch(item):
    name,url,suffix=item
    record={'name':name,'url':url,'started_utc':datetime.now(timezone.utc).isoformat()}
    try:
        request=Request(url, headers={'User-Agent':'Mozilla/5.0 (mathematical source verification)'})
        with urlopen(request, timeout=30) as response:
            record['http_status']=response.status
            data=response.read()
        if suffix=='pdf' and not data.startswith(b'%PDF'):
            raise ValueError('Response is not a PDF')
        path=out/f'{name}.{suffix}'
        path.write_bytes(data)
        record.update(path=str(path.relative_to(root)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
        if suffix=='pdf':
            textpath=path.with_suffix('.txt')
            run=subprocess.run(['pdftotext','-layout',str(path),str(textpath)],capture_output=True,text=True)
            record['pdftotext_exit']=run.returncode
            record['pdftotext_stderr']=run.stderr
            if run.returncode:
                raise RuntimeError('pdftotext failed')
        record['status']='archived'
    except Exception as error:
        record.update(status='failed',error=repr(error))
    return record

with ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(fetch,sources))
manifest={'retrieved_utc':datetime.now(timezone.utc).isoformat(),
          'initial_attempt':'The first invocation failed at import requests (ModuleNotFoundError); revised to Python standard-library urllib without installing anything.',
          'sources':results}
(root/'fetch_super_audit_sources_output.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
