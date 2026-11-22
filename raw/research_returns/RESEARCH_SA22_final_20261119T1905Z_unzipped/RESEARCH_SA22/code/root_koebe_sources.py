from pathlib import Path
import urllib.request,json,time,hashlib,concurrent.futures,subprocess
R=Path(__file__).resolve().parents[1];T=time.perf_counter();d=json.loads((R/'sources/koebe1907_volume_manifest.json').read_text());jobs=[]
for s in d['structures']:
 if 'beliebiger' in s.get('label',''):
  name='koebe1907_second.pdf' if 'Zweite' in s['label'] else 'koebe1907_first.pdf';jobs.append((name,s['rendering'][0]['@id']))
def fetch(job):
 name,u=job;t=time.perf_counter();out={'file':name,'url':u}
 try:
  with urllib.request.urlopen(u,timeout=50) as f:b=f.read();out.update(status=f.status,bytes=len(b),pdf=b.startswith(b'%PDF'),sha256=hashlib.sha256(b).hexdigest())
  (R/'sources'/name).write_bytes(b)
  if out['pdf']:
   r=subprocess.run(['pdftotext','-layout',str(R/'sources'/name),str(R/'sources'/name.replace('.pdf','.txt'))],capture_output=True,text=True);out['text_extract_exit']=r.returncode
 except Exception as e:out['error']=repr(e)
 out['seconds']=time.perf_counter()-t;return out
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:res=list(ex.map(fetch,jobs))
out={'attempts':len(jobs),'seconds':time.perf_counter()-T,'results':res}
(R/'code/root_koebe_sources_output.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
