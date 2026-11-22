"""Retrieve public inventories/correspondence indexes for manuscript dating."""
from pathlib import Path
import urllib.request,json,time,hashlib,concurrent.futures,re
root=Path(__file__).resolve().parents[1]
urls={
'letters_index':'https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/mathletters.php',
'montpellier_index':'https://grothendieck.umontpellier.fr/archives-grothendieck/',
'montpellier_home':'https://grothendieck.umontpellier.fr/',
'cirm_inventory':'https://www.cirm-math.fr/RepOrga/2095/Slides/DIAPORAMA_V2_RNBM_Groth_nov19.pptx.pdf'}
def fetch(item):
 key,url=item;t=time.perf_counter();r={'key':key,'url':url}
 try:
  with urllib.request.urlopen(url,timeout=25) as f:data=f.read();r.update(status=f.status,final_url=f.geturl(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  ext='.pdf' if data.startswith(b'%PDF') else '.html';p=root/'sources'/('algebra_history_'+key+ext);p.write_bytes(data);r['file']=str(p.relative_to(root))
  if ext=='.html':r['links']=re.findall(r'<a[^>]*href=[\"\x27]([^\"\x27]+)',data.decode(errors='replace'),re.I)
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=round(time.perf_counter()-t,6);return r
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:records=list(p.map(fetch,urls.items()))
out={'retrievals':records,'elapsed_seconds':round(time.perf_counter()-start,6)}
(root/'logs/algebra_history_fetch09.json').write_text(json.dumps(out,indent=2,ensure_ascii=False));print(json.dumps(out,indent=2,ensure_ascii=False))
