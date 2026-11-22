"""Read public CSG Dixmier correspondence and ENS inventory; preserve PDFs/text/renders."""
from pathlib import Path
import urllib.request,json,time,hashlib,concurrent.futures,subprocess,re
root=Path(__file__).resolve().parents[1]
urls={
'dixmier_19501120_scan':'https://csg.igrothendieck.org/wp-content/uploads/2025/11/L33.pdf',
'dixmier_19501210_scan':'https://csg.igrothendieck.org/wp-content/uploads/2024/05/L34u.pdf',
'dixmier_19510607_scan':'https://csg.igrothendieck.org/wp-content/uploads/2025/11/L35.pdf',
'dixmier_19540628_scan':'https://csg.igrothendieck.org/wp-content/uploads/2025/11/L37.pdf',
'dixmier_19540813_scan':'https://csg.igrothendieck.org/wp-content/uploads/2025/11/L39.pdf',
'dixmier_19550124_scan':'https://csg.igrothendieck.org/wp-content/uploads/2025/10/L40.pdf',
'ens_inventory2019':'https://www.math.ens.psl.eu/wp-content/uploads/2021/07/Dixmier_Plan_Classement_201902.pdf',
'ens_inventory2014':'https://www.math.ens.psl.eu/wp-content/uploads/2021/07/Archive_Dixmier_Annexe1.pdf',
}
for number,date in [(34,'19501210'),(35,'19510607'),(36,'19520502'),(37,'19540628'),(38,'19540718'),(39,'19540813'),(40,'19550124')]:
 urls['dixmier_'+date+'_transcription']='https://csg.igrothendieck.org/wp-content/uploads/2025/10/L%sd.pdf'%number
def fetch(item):
 key,url=item;t=time.perf_counter();r={'key':key,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=25) as f:data=f.read();r.update(status=f.status,final_url=f.geturl(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  p=root/'sources'/('algebra_history_'+key+'.pdf');p.write_bytes(data);r['file']=str(p.relative_to(root))
  if data.startswith(b'%PDF'):
   c=subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,text=True);r['text_extraction_returncode']=c.returncode
   r['hits']=[{'line':i+1,'text':line} for i,line in enumerate(p.with_suffix('.txt').read_text(errors='replace').splitlines()) if re.search(r'genre|Fredholm|Weyl|trace|Lidsk|déterminant|determinant|Grothendieck',line,re.I)]
   if key.endswith('_scan'):
    c=subprocess.run(['pdftoppm','-scale-to','1800','-png',str(p),str(p.with_suffix(''))],capture_output=True,text=True);r['render_returncode']=c.returncode;r['render_stderr']=c.stderr
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=round(time.perf_counter()-t,6);return r
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:records=list(p.map(fetch,urls.items()))
out={'retrievals':records,'elapsed_seconds':round(time.perf_counter()-start,6)}
(root/'logs/algebra_history_fetch10.json').write_text(json.dumps(out,indent=2,ensure_ascii=False));print(json.dumps(out,indent=2,ensure_ascii=False))
