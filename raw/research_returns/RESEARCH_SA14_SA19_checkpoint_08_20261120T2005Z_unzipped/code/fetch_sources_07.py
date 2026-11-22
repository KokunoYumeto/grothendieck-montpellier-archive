"""Preserve the exact source-fetch procedure used for checkpoint07 scope checks."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import datetime, hashlib, json, subprocess, time, urllib.request

root=Path(__file__).resolve().parents[1]
sources={
 'JMathSocJapan1980_153':'https://www.jstage.jst.go.jp/article/jmath1948/32/1/32_1_153/_pdf',
 'LiShentu2014':'https://www.numdam.org/item/CRMATH_2014__352_7-8_639_0.pdf'
}
def fetch(pair):
 name,url=pair
 p=root/'sources'/(name+'.pdf');start=time.monotonic()
 try:
  existed=p.exists()
  if not existed:
   with urllib.request.urlopen(url,timeout=30) as response:p.write_bytes(response.read())
  data=p.read_bytes()
  if not data.startswith(b'%PDF'):raise ValueError('not a PDF')
  subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
  return dict(name=name,url=url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),seconds=round(time.monotonic()-start,3),status='opened locally and text extracted',reused_existing_download=existed)
 except Exception as exc:
  return dict(name=name,url=url,seconds=round(time.monotonic()-start,3),status='failed',error=str(exc))
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(fetch,sources.items()))
 result=dict(time_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sources=results)
 (root/'code/fetch_sources_07_output.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
