from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import urljoin, urlparse, parse_qs
import re, hashlib, time
root=Path('RESEARCH_SA23')
archive='https://grothendieck.umontpellier.fr/archives-grothendieck/'
s=(root/'sources/category_archive_index.html').read_text()
for cote in ['161-5','162-5','161-2']:
 m=re.search(r'data-target="'+re.escape(cote)+r'" data-src="([^"]+)"',s)
 assert m, cote
 viewer=urljoin(archive,m.group(1))
 path=parse_qs(urlparse(viewer).query)['file'][0]
 url=urljoin(viewer,path)
 print('COTE',cote,'viewer',viewer,'source',url,flush=True)
 t=time.monotonic()
 try:
  b=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=90).read()
  assert b.startswith(b'%PDF'),b[:100]
  p=root/'sources'/('category_manuscript_'+cote+'.pdf')
  p.write_bytes(b)
  print('SAVED',p,'bytes',len(b),'sha256',hashlib.sha256(b).hexdigest(),'seconds',time.monotonic()-t,flush=True)
 except Exception as exc:
  print('FAILED',repr(exc),'seconds',time.monotonic()-t,flush=True)
