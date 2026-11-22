"""Fetch the primary mathematical sources used in the root investigation."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, subprocess, hashlib, json, time
ROOT=Path(__file__).resolve().parents[1]
SOURCES={
'SGA6':'https://wstein.org/sga/sga/pdf/sga6.pdf',
'Terakawa1999':'https://msp.org/pjm/1999/187-1/pjm-v187-n1-p09-p.pdf',
'Zhang2022':'https://arxiv.org/pdf/2103.04268',
'Enokizono2021':'https://arxiv.org/pdf/2104.00197',
'Totaro2019':'https://www.math.ucla.edu/~totaro/papers/public_html/kodaira.pdf',
'SGA2':'https://arxiv.org/pdf/math/0511279',
'Kleiman2005':'https://arxiv.org/pdf/math/0504020',
'BhattDeJong2014':'https://www.numdam.org/item/10.24033/asens.2228.pdf',
'LauritzenRao1997':'https://arxiv.org/pdf/alg-geom/9604012',
'Ekedahl1988':'https://www.numdam.org/item/PMIHES_1988__67__97_0.pdf',
'Mukai2013':'https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1505.pdf',
'Mukai2011revised':'https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1736.pdf',
'Zheng2015':'https://arxiv.org/pdf/1509.04993',
'BernasconiValloni2026':'https://arxiv.org/pdf/2605.28278',
'Langer2011':'https://arxiv.org/pdf/0905.4600',
'CotnerZavyalov2024':'https://bogdanzavyalov.com/refs/Lefschetz.pdf',
}
def fetch(pair):
 name,url=pair;start=time.monotonic();p=ROOT/'sources'/(name+'.pdf')
 try:
  if not p.exists():
   with urllib.request.urlopen(url,timeout=50) as r:p.write_bytes(r.read())
  data=p.read_bytes()
  if not data.startswith(b'%PDF'):raise ValueError('not a PDF')
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  return dict(name=name,url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),seconds=round(time.monotonic()-start,3),status='available locally and text extracted')
 except Exception as e:return dict(name=name,url=url,seconds=round(time.monotonic()-start,3),status='failed',error=str(e))
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=4) as e:results=list(e.map(fetch,SOURCES.items()))
 out=json.dumps(results,indent=2)
 (ROOT/'code'/'fetch_sources_output.json').write_text(out+'\n')
 print(out)
