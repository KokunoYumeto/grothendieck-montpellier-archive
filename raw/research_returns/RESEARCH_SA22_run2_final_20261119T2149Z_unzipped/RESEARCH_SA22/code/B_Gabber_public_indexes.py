"""Read-only public discovery routes for the exact Gabber1994 original.
No account, author request, subscription or authentication workaround is used.
"""
import concurrent.futures,datetime,json,time,urllib.parse,urllib.request
from pathlib import Path
TASK_ROOT=Path(__file__).resolve().parents[1]
queries={
 'arxiv_exact_title':'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'ti:"Affine analog of the proper base change theorem"','start':0,'max_results':20}),
 'google_books_volume':'https://www.googleapis.com/books/v1/volumes?'+urllib.parse.urlencode({'q':'intitle:"Israel Journal of Mathematics" "87" "1994"','maxResults':40}),
 'core_exact_doi':'https://api.core.ac.uk/v3/search/works?'+urllib.parse.urlencode({'q':'doi:"10.1007/BF02773001"','limit':10}),
}
def fetch(item):
 name,url=item;start=time.perf_counter();d={'name':name,'url':url,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(url,timeout=20) as r:
   data=r.read();d.update(status=r.status,final_url=r.url,content_type=r.headers.get('Content-Type'),body=data.decode('utf-8','replace'))
 except Exception as e:
  d.update(error=repr(e))
 d['elapsed_seconds']=time.perf_counter()-start
 return d
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:results=list(ex.map(fetch,queries.items()))
(TASK_ROOT/'logs/B_Gabber_public_indexes.json').write_text(json.dumps(results,indent=2))
for d in results: print(json.dumps({k:(v[:600] if k=='body' else v) for k,v in d.items()}))
