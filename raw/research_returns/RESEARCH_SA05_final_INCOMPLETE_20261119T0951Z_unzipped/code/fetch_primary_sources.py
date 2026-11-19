"""Fetch public primary literature; keep exact URL, byte count, SHA256, and status."""
from pathlib import Path
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, subprocess, time
ROOT=Path(__file__).resolve().parents[1]
SOURCES={
'Milne_1994_Finite_fields':'https://www.jmilne.org/math/xnotes/Seattle1.pdf',
'Milne_2003_Gerbes':'https://www.jmilne.org/math/articles/2003b.pdf',
'Milne_2006_Fp':'https://www.jmilne.org/math/articles/2006a.pdf',
'Langlands_Rapoport_1987':'https://publications.ias.edu/sites/default/files/shimuravarietaeten-und-gerben_rpl_0.pdf',
'Langlands_Rapoport_translation_2025':'https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/langlands-rapoport-shimvarplusgerbestranslation.pdf',
'Milne_1992_Points':'https://www.jmilne.org/math/articles/1992aP.pdf',
'Milne_ADT':'https://www.jmilne.org/math/Books/ADTnot.pdf',
}
def fetch(item):
 name,url=item; start=time.monotonic(); dest=ROOT/'sources'/f'{name}.pdf'
 rec={'name':name,'url':url}
 try:
  if not dest.exists():
   data=urlopen(Request(url,headers={'User-Agent':'Mozilla/5.0','Accept':'application/pdf'}),timeout=35).read()
   if not data.startswith(b'%PDF'): raise ValueError('Not PDF')
   dest.write_bytes(data)
  data=dest.read_bytes()
  subprocess.run(['pdftotext','-layout',str(dest),str(dest.with_suffix('.txt'))],check=True,capture_output=True)
  rec.update(status='downloaded and text extracted',bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as e: rec.update(status='failed',error=f'{type(e).__name__}: {e}')
 rec['seconds']=round(time.monotonic()-start,3)
 return rec
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=5) as ex: records=list(ex.map(fetch,SOURCES.items()))
 out=ROOT/'code'/'fetch_primary_sources_output.json'
 out.write_text(json.dumps(records,indent=2))
 for r in records: print(r['name'],r['status'],r.get('bytes',r.get('error')),r['seconds'])
