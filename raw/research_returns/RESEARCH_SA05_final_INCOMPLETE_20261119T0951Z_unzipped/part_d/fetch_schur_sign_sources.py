"""Archive the exact primary sources used in the sign/Schur audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import urllib.request
from concurrent.futures import ThreadPoolExecutor

root=Path(__file__).resolve().parent
destination=root/'sources'
destination.mkdir(exist_ok=True)
items=[
 ('del_padrone_mazza2005.pdf','https://www.numdam.org/item/10.1016/j.crma.2005.07.010.pdf'),
 ('del_padrone_mazza2010.pdf','https://arxiv.org/pdf/1010.3929'),
 ('andre_kahn2002.pdf','https://webusers.imj-prg.fr/~bruno.kahn/preprints/a.k.os.pdf'),
 ('andre_kahn2005_erratum.pdf','https://www.numdam.org/item/RSMUP_2005__113__125_0.pdf'),
]
def fetch(item):
    name,url=item
    result={'filename':name,'url':url}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(request,timeout=35) as response:
            data=response.read()
        if not data.startswith(b'%PDF'):
            raise ValueError('Response is not a PDF')
        path=destination/name
        path.write_bytes(data)
        subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
        result.update(status='archived',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    except Exception as error:
        result.update(status='failed',error=str(error))
    return result

with ThreadPoolExecutor(max_workers=4) as pool:
    results=list(pool.map(fetch,items))
manifest={'created_utc':datetime.now(timezone.utc).isoformat(),'sources':results}
(root/'fetch_schur_sign_sources_output.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
