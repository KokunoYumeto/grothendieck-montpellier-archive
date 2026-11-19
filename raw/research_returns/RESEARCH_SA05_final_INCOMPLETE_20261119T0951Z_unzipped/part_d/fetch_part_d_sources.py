"""Reproduce Part D primary-source retrieval and PDF text extraction.

Existing valid PDFs are preserved. A failed HTTP response is never labelled PDF.
CCO2008 was read through web retrieval of an author-uploaded full-text page; this
script separately tries to archive that page and records its actual HTTP result.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, urllib.error, subprocess, json, hashlib, time
P=Path(__file__).resolve().parent; S=P/'sources';S.mkdir(exist_ok=True)
items=[
('Anantharaman1973','https://www.numdam.org/article/MSMF_1973__33__5_0.pdf'),
('Milne2003b','https://www.jmilne.org/math/articles/2003b.pdf'),
('MilneShih1982','https://www.jmilne.org/math/articles/1982c.pdf'),
('MilneCM2020','https://www.jmilne.org/math/CourseNotes/CM.pdf'),
('MilnePedestrians','https://www.jmilne.org/math/articles/1981dT.pdf'),
('DeligneTaniyama','https://publications.ias.edu/sites/default/files/Number45.pdf'),
('Deligne1982Hodge','https://www.jmilne.org/math/Documents/Deligne82_2003.pdf'),
('Serre1968','https://www.math.mcgill.ca/darmon/courses/18-19/gs/serre-mcgill.pdf'),
('Andre1996','https://www.numdam.org/article/PMIHES_1996__83__5_0.pdf'),
('Oort2009','https://webspace.science.uu.nl/~oort0109/Biel3-VI-2009.pdf'),
('KahnOtsubo2026','https://arxiv.org/pdf/2611.13723'),
('VanHoftenSempliner2026','https://polvanhoften2.github.io/Pol%20van%20Hoften%20and%20Jack%20Sempliner%20-%20The%20Hodge%20conjecture%20for%20CM%20abelian%20varieties.pdf'),
('CCO2023Application','https://pure.mpg.de/rest/items/item_3490978_3/component/file_3501139/content'),
('CCO2008','https://www.researchgate.net/publication/245676682_CM_liftings_of_abelian_varieties')]
def fetch(it):
 name,url=it;t=time.monotonic();p=S/(name+'.pdf');out={'name':name,'url':url}
 try:
  if p.exists() and p.read_bytes().startswith(b'%PDF'):
   out['status']='existing_valid_pdf_preserved'
  else:
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (research source verification)'})
   with urllib.request.urlopen(req,timeout=15) as r:
    content=r.read();status=r.status;content_type=r.headers.get('content-type')
   out['http_status']=status
   if status==200 and content.startswith(b'%PDF'):
    p.write_bytes(content);out['status']='downloaded_pdf'
   elif name=='CCO2008' and status==200:
    p=S/(name+'.html');p.write_bytes(content);out['status']='downloaded_html'
   else:
    out['status']='not_obtained';out['response_content_type']=content_type;out['response_bytes']=len(content)
  if p.exists():
   out.update(path=str(p.relative_to(P)),bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
   if p.suffix=='.pdf':
    txt=p.with_suffix('.txt')
    if not txt.exists():
     rr=subprocess.run(['pdftotext','-layout',str(p),str(txt)],capture_output=True,text=True)
     out['pdftotext_exit']=rr.returncode
    out['text_bytes']=txt.stat().st_size if txt.exists() else None
 except Exception as e:out.update(status='not_obtained',error=str(e))
 out['seconds']=round(time.monotonic()-t,3);return out
with ThreadPoolExecutor(max_workers=4) as pool: result=list(pool.map(fetch,items))
(P/'fetch_part_d_sources_output.json').write_text(json.dumps(result,indent=2)+'\n')
for x in result: print(x['name'],x['status'],x.get('bytes',x.get('response_bytes')),x['seconds'])
