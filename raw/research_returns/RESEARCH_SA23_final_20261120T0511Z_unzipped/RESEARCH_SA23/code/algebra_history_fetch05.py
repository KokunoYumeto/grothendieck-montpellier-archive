"""Read exact public archive issue metadata and download only public PDF/OCR files."""
from pathlib import Path
import urllib.request,urllib.parse,json,time,hashlib
root=Path(__file__).resolve().parents[1]
identifier='rossiiskaya-akademiya-nauk-doklady_1959-03-21_125_3'
url='https://archive.org/metadata/'+identifier
records=[];start=time.perf_counter()
def get(url,name):
 t=time.perf_counter();r={'url':url}
 try:
  with urllib.request.urlopen(url,timeout=30) as f:data=f.read();r.update(status=f.status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  p=root/'sources'/name;p.write_bytes(data);r['file']=str(p.relative_to(root))
  r['elapsed_seconds']=round(time.perf_counter()-t,6);records.append(r);return data
 except Exception as e:r.update(error=repr(e),elapsed_seconds=round(time.perf_counter()-t,6));records.append(r);return None
data=get(url,'algebra_history_lidskii_issue_metadata.json')
if data:
 d=json.loads(data)
 print(json.dumps({'metadata':d.get('metadata'),'files':d.get('files')},ensure_ascii=False,indent=2))
 for f in d.get('files',[]):
  name=f['name']
  if not f.get('private') and (name.endswith('_text.pdf') or name.endswith('_djvu.txt') or name.endswith('_scandata.xml')):
   get('https://archive.org/download/'+identifier+'/'+urllib.parse.quote(name),'algebra_history_lidskii_'+name.split('/')[-1])
out={'retrievals':records,'elapsed_seconds':round(time.perf_counter()-start,6)}
(root/'logs'/'algebra_history_fetch05.json').write_text(json.dumps(out,indent=2,ensure_ascii=False));print(json.dumps(out,indent=2))

