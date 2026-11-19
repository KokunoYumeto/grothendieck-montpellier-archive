"""Retrieve already discovered public primary texts; no access-wall workaround.
Raw downloads stay in work; manifest and extracted text document each retrieval.
"""
from pathlib import Path
import urllib.request, hashlib, json, subprocess, concurrent.futures
from html.parser import HTMLParser
class Plain(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style','nav'):self.skip+=1
 def handle_endtag(self,tag):
  if tag in ('script','style','nav'):self.skip=max(0,self.skip-1)
 def handle_data(self,data):
  if not self.skip and data.strip():self.parts.append(data.strip())
ROOT=Path(__file__).resolve().parents[4]
WORK=ROOT/'work/p4_primary'; WORK.mkdir(exist_ok=True)
OUT=Path(__file__).resolve().parents[1]/'outputs'
URLS={
 'sga7_vii2.html':'https://grothendiecksga.com/read/sga7/fr/7-2.html',
 'sga7_vii3.html':'https://grothendiecksga.com/read/sga7/fr/7-3.html',
 'sga7_viii1.html':'https://grothendiecksga.com/read/sga7/fr/8-1.html',
 'sga7_ix2.html':'https://grothendiecksga.com/read/sga7/fr/9-2.html',
 'sga7_ix12.html':'https://grothendiecksga.com/read/sga7/fr/9-12.html',
 'raynaud1970.pdf':'https://www.numdam.org/item/PMIHES_1970__38__27_0.pdf',
 'strickland_formal.pdf':'https://strickland1.org/vietnam/formal.pdf',
 'strickland_fpfp.pdf':'https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Strickland-fpfp.pdf',
 'bosch_lorenzini2002.pdf':'https://dinolorenzini.franklinresearch.uga.edu/sites/default/files/inline-files/papers/LorenziniBosch.pdf',
 'chabauty1950.pdf':'https://www.numdam.org/item/10.24033/bsmf.1412.pdf',
 'bourbaki_integration78.pdf':'https://www.devoir.tn/superieur/Doc/Livres/Math%C3%A9matiques/Maths-cours-de-reference-350-livres/Bourbaki/Int%C3%A9gration/4-Bourbaki-El%C3%A9m%C3%A9nts-de-math%C3%A9matique-Int%C3%A9gration-Chapitres-7et-8.pdf',
 'hashimoto_quotients.pdf':'https://www.math.okayama-u.ac.jp/~hashimoto/paper/onoda9.pdf',
 'omalley1972.pdf':'https://projecteuclid.org/journals/rocky-mountain-journal-of-mathematics/volume-2/issue-2/On-the-Weierstrass-preparation-theorem/10.1216/RMJ-1972-2-2-265.pdf'
}
def fetch(pair):
 name,url=pair
 try:
  with urllib.request.urlopen(url,timeout=35) as r: data=r.read(); final=r.url; typ=r.headers.get('Content-Type')
  path=WORK/name;path.write_bytes(data)
  if name.endswith('.pdf'):
   if not data.startswith(b'%PDF'): raise ValueError('Response is not a PDF')
   subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True)
  else:
   plain=Plain();plain.feed(data.decode('utf-8'))
   path.with_suffix('.txt').write_text('\n'.join(plain.parts))
  return dict(file=name,url=url,final_url=final,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),content_type=typ,status='downloaded and extracted')
 except Exception as e:return dict(file=name,url=url,status='failed',error=str(e))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: result=list(pool.map(fetch,URLS.items()))
 (OUT/'primary_download_manifest.json').write_text(json.dumps(result,indent=2)+'\n')
 for r in result:print(r['file'],r['status'],r.get('bytes',r.get('error')))
