"""Record reproducible retrievals; third-party documents stay outside deliverables."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.request import Request, urlopen
from datetime import datetime, timezone
import hashlib, json

BASE = Path('/workspace/scratch/6215ed17d0f0')
TARGET = BASE/'primary_sources'/'part_b'/'post06'
TARGET.mkdir(parents=True, exist_ok=True)
LOG = BASE/'RESEARCH_SA05_work'/'part_b'/'output'/'post06_primary_capture.json'
SOURCES = {
 'silverman2009.pdf':'https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf',
 'fu_vial2023.pdf':'https://irma.math.unistra.fr/~lfu/articles/KuznetsovCubic4fold.pdf',
 'poonen2004.pdf':'https://math.mit.edu/~poonen/papers/bertini.pdf',
 'broe2026.html':'https://arxiv.org/html/2509.03602v3',
 'scavia_suzuki2026.pdf':'https://arxiv.org/pdf/2609.36188',
 'longo_vigni2026.html':'https://link.springer.com/article/10.1007/s40687-026-00646-7',
 'bloch_srinivas_landing.html':'https://repository.ias.ac.in/58969/',
}
def fetch(item):
 name,url=item
 out={'name':name,'url':url,'date':datetime.now(timezone.utc).isoformat()}
 try:
  with urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as r:
   data=r.read(); out.update(status=r.status,content_type=r.headers.get('Content-Type'),bytes=len(data))
  (TARGET/name).write_bytes(data)
  out.update(sha256=hashlib.sha256(data).hexdigest(),saved=str(TARGET/name),pdf_signature=data.startswith(b'%PDF') if name.endswith('.pdf') else None)
 except Exception as exc:
  out['error']=repr(exc)
 return out
with ThreadPoolExecutor(max_workers=7) as pool:
 result=list(pool.map(fetch,SOURCES.items()))
LOG.write_text(json.dumps(result,indent=2)+'\n')
for row in result:
 print(row['name'],row.get('status'),row.get('bytes'),row.get('error',''))
print('RETRIEVALS_COMPLETE',len(result))
