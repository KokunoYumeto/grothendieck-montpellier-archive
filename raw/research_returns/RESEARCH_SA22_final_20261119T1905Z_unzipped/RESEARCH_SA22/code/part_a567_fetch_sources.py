"""Download primary sources used by Part A.5--A.7; no mathematical checks."""
from pathlib import Path
import urllib.request, subprocess, concurrent.futures, time
ROOT=Path(__file__).resolve().parents[1]
JOBS={
'RESEARCH_SA22/sources/hoshi_mochizuki_2011.pdf':'https://www.kurims.kyoto-u.ac.jp/~yuichiro/RIMS1677revised.pdf',
'RESEARCH_SA22/sources/mochizuki_2006.pdf':'https://ems.press/content/serial-article-files/40941',
'RESEARCH_SA22/sources/mochizuki_2007.pdf':'https://www.jstage.jst.go.jp/article/tmj/59/3/59_3_455/_pdf/-char/en',
'RESEARCH_SA22/sources/alling_1981_preview.pdf':'https://api.pageplace.de/preview/DT0400.9780080871653_A23529093/preview-9780080871653_A23529093.pdf',
'RESEARCH_SA22/sources/milne_ec2.pdf':'https://www.jmilne.org/math/Books/EC2.pdf',
'RESEARCH_SA22/sources/stukow_2004.pdf':'https://www.numdam.org/item/10.1016/j.crma.2003.12.028.pdf',
'RESEARCH_SA22/sources/bakalov_kirillov_2000.pdf':'https://arxiv.org/pdf/math/9809057',
'reference_cache/cote67.pdf':'https://grothendieck.umontpellier.fr/67.pdf',
}
def fetch(item):
 name,url=item; dest=ROOT.parent/name; start=time.monotonic()
 try:
  dest.parent.mkdir(parents=True,exist_ok=True)
  if not dest.exists(): dest.write_bytes(urllib.request.urlopen(url,timeout=50).read())
  if not dest.read_bytes().startswith(b'%PDF'): return {'file':name,'error':'not PDF'}
  subprocess.run(['pdftotext','-layout',str(dest),str(dest.with_suffix('.txt'))],check=True,capture_output=True)
  return {'file':name,'bytes':dest.stat().st_size,'seconds':round(time.monotonic()-start,3)}
 except Exception as e: return {'file':name,'error':str(e),'seconds':round(time.monotonic()-start,3)}
if __name__=='__main__':
 import json
 for out in concurrent.futures.ThreadPoolExecutor(max_workers=4).map(fetch,JOBS.items()): print(json.dumps(out))
