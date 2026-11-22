#!/usr/bin/env python3
"""Additional primary-source retrieval; every failure is retained in the manifest."""
import concurrent.futures, hashlib, json, subprocess, time, urllib.request
from pathlib import Path
root=Path(__file__).resolve().parents[1]
jobs=[
 ('milne_adt.pdf','https://www.jmilne.org/math/Books/ADTnot.pdf'),
 ('gabber1994.pdf','https://link.springer.com/content/pdf/10.1007/BF02773001.pdf'),
 ('fujiwara1995.pdf','https://projecteuclid.org/journalArticle/Download?urlid=10.1215/S0012-7094-95-08002-8'),
 ('deligne_tannakian1990.pdf','https://www.math.columbia.edu/~dejong/tannakian/Deligne-Categories-tannakiennes.pdf'),
 ('raynaud_ogg1966.pdf','https://www.numdam.org/article/SB_1964-1966__9__129_0.pdf'),
 ('ramis_ruget1970.pdf','https://www.numdam.org/item/PMIHES_1970__38__77_0.pdf'),
 ('contou_carrere1979.pdf','https://csg.igrothendieck.org/wp-content/uploads/2024/04/jacgenscan.pdf'),
 ('contou_carrere2013.pdf','https://www.numdam.org/item/RSMUP_2013__130__1_0.pdf'),
 ('blr_neron1990.pdf','https://www.math.stonybrook.edu/~kamenova/homepage_files/Bosch_Raynaud_Neron_Model_tc.pdf'),
]
def fetch(job):
 name,url=job; p=root/'sources'/name; start=time.perf_counter()
 try:
  status='existing'
  if not p.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
   with urllib.request.urlopen(req,timeout=45) as r:b=r.read()
   if not b.startswith(b'%PDF'):return {'file':name,'url':url,'status':'non-PDF','bytes':len(b)}
   p.write_bytes(b); status='downloaded'
  b=p.read_bytes()
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],capture_output=True,check=True)
  return {'file':name,'url':url,'status':status,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'seconds':time.perf_counter()-start}
 except Exception as e:return {'file':name,'url':url,'status':'error','error':str(e),'seconds':time.perf_counter()-start}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:results=list(ex.map(fetch,jobs))
(root/'code'/'part_b_fetch_more_output.json').write_text(json.dumps(results,indent=2)+'\n')
for r in results:print(r['file'],r['status'],r.get('bytes',r.get('error')))
