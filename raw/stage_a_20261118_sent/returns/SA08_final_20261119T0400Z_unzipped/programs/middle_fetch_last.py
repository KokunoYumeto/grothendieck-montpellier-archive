"""Final public-source retrieval attempts, with successes and failures retained."""
from pathlib import Path
import urllib.request,json,hashlib,subprocess,datetime
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'work/middle/references'
urls={
 'Coleman2000.pdf':'https://intlpress.com/site/pub/files/_fulltext/journals/ajm/2000/0004/0002/AJM-2000-0004-0002-a002.pdf',
 'BanicaStoia1979.pdf':'https://imar.ro/~increst/1979/31_1979.pdf',
}
for name,url in urls.items():
 r={'file':str(D/name),'url':url,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  data=urllib.request.urlopen(url,timeout=40).read()
  if not data.startswith(b'%PDF'):raise ValueError('Response is not a PDF')
  (D/name).write_bytes(data)
  r.update(status='downloaded',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  p=subprocess.run(['pdftotext','-layout',str(D/name),str((D/name).with_suffix('.txt'))],capture_output=True,text=True)
  r.update(pdftotext_returncode=p.returncode,pdftotext_stderr=p.stderr)
 except Exception as e:r.update(status='failed',error=str(e))
 print(json.dumps(r,ensure_ascii=False))
