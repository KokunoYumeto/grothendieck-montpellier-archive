"""Ordinary public metadata/preview requests; no login or challenge handling."""
from pathlib import Path
import concurrent.futures,json,time,urllib.request,urllib.error
root=Path(__file__).resolve().parents[1]
urls={
 'google_books_metadata':'https://www.googleapis.com/books/v1/volumes/pvKdD74g6UEC',
 'google_books_preview':'https://books.google.com/books?id=pvKdD74g6UEC&pg=PA41',
 'ams_chapter':'https://www.ams.org/books/conm/575/11411/conm575-11411.pdf',
 'ams_volume':'https://www.ams.org/books/conm/575/conm575.pdf',
}
def fetch(item):
 name,url=item;t=time.perf_counter()
 try:
  request=urllib.request.Request(url,headers={'User-Agent':'SA22 scholarly source verification; ordinary public request'})
  try:r=urllib.request.urlopen(request,timeout=25)
  except urllib.error.HTTPError as err:r=err
  content=r.read();ctype=r.headers.get('Content-Type','')
  ext='.pdf' if content.startswith(b'%PDF') else '.json' if 'json' in ctype else '.html'
  path=root/'sources'/('root_'+name+ext);path.write_bytes(content)
  result=dict(name=name,url=url,status=r.status,final_url=r.geturl(),content_type=ctype,bytes=len(content),saved=str(path.relative_to(root)),seconds=time.perf_counter()-t)
  if ext=='.json':
   data=json.loads(content);result['accessInfo']=data.get('accessInfo',data.get('error'))
  return result
 except Exception as exc:return dict(name=name,url=url,error=str(exc),seconds=time.perf_counter()-t)
t=time.perf_counter()
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=list(pool.map(fetch,urls.items()))
out=dict(requests=len(results),results=results,seconds=time.perf_counter()-t)
(root/'code/root_public_preview_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
