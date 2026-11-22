"""Follow the public USP PDF with a cookie-aware client and preserve all attempts."""
from pathlib import Path
import urllib.request,http.cookiejar,json,time,hashlib,concurrent.futures,subprocess
root=Path(__file__).resolve().parents[1]
urls=[
'https://revistas.usp.br/resenhasimeusp/en/article/download/74836/78406/100978',
'https://revistas.usp.br/resenhasimeusp/article/download/74836/78406',
'https://www.revistas.usp.br/resenhasimeusp/article/download/74836/78406',
]
def retrieve(pair):
 i,url=pair; start=time.perf_counter();r={'url':url}
 try:
  opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
  with opener.open(url,timeout=25) as f:
   data=f.read();r.update(status=f.status,final_url=f.geturl(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
  p=root/'sources'/f'algebra_history_metric_facsimile_{i}.pdf';p.write_bytes(data);r['file']=str(p.relative_to(root))
  if data.startswith(b'%PDF'):
   subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True,capture_output=True)
   for page in [1,7,54,55,77,78,80]:
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','2000','-png','-singlefile',str(p),str(p.with_suffix(''))+f'_p{page:03d}'],check=True,capture_output=True)
 except Exception as e:r['error']=repr(e)
 r['elapsed_seconds']=round(time.perf_counter()-start,6);return r
start=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:rs=list(pool.map(retrieve,enumerate(urls)))
out={'retrievals':rs,'elapsed_seconds':round(time.perf_counter()-start,6)}
(root/'logs'/'algebra_history_fetch04.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))

