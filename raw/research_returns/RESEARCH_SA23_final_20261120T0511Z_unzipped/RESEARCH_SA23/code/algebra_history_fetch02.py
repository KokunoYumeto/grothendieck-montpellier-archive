"""Retrieve and extract two witnesses of Grothendieck's metric tensor Resume."""
from pathlib import Path
import urllib.request,hashlib,json,time,concurrent.futures,subprocess,re
root=Path(__file__).resolve().parents[1]
tasks=[
 ('metric_transcription','https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/AG/AG-22.pdf'),
 ('metric_facsimile','https://revistas.usp.br/resenhasimeusp/en/article/download/74836/78406/100978'),
 ('ams_memoir_official','https://www.ams.org/memo/0016/memo0016.pdf'),
]
def fetch(task):
 name,url=task; start=time.perf_counter();record={'name':name,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=40) as response:
   data=response.read();record.update(status=response.status,final_url=response.geturl(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  path=root/'sources'/('algebra_history_'+name+'.pdf');path.write_bytes(data);record['file']=str(path.relative_to(root))
  if not data.startswith(b'%PDF'): raise ValueError('Not a PDF')
  out=path.with_suffix('.txt')
  result=subprocess.run(['pdftotext','-layout',str(path),str(out)],capture_output=True,text=True)
  record['extract_returncode']=result.returncode;record['extract_stderr']=result.stderr
  text=out.read_text()
  hits=[]
  for i,line in enumerate(text.splitlines(),1):
   if re.search(r'genre|d.terminant|trace|spectr|propre|Weyl|Lidsk|Phrag|secteur',line,re.I):
    hits.append({'line':i,'text':line})
  record['hits']=hits
 except Exception as error:record['error']=repr(error)
 record['elapsed_seconds']=round(time.perf_counter()-start,6)
 return record
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(fetch,tasks))
output={'retrievals':records,'elapsed_seconds':round(time.perf_counter()-start,6)}
(root/'logs'/'algebra_history_fetch02.json').write_text(json.dumps(output,indent=2,ensure_ascii=False))
print(json.dumps(output,indent=2,ensure_ascii=False))

