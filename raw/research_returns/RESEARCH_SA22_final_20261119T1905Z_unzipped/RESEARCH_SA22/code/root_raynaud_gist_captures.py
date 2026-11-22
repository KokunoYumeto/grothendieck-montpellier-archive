"""Check only the Raynaud chapter URLs actually advertised in an opened gist.

Two normal publisher requests and bounded exact public archive metadata reads.
No restricted content is requested after a denial; no headers/authentication are
changed. An archive metadata hit is not an original-text reading.
"""
from pathlib import Path
import concurrent.futures,hashlib,html,json,re,time,urllib.error,urllib.parse,urllib.request
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
line=next(s for s in (ROOT/'sources/raynaud_lnm_gist_raw.html').read_text().splitlines() if s.startswith('Faisceaux amples'))
links=[dict(url=html.unescape(u),title=html.unescape(t)) for u,t in re.findall(r'<a href="([^"]+)" title="([^"]+)"',line)]
chapters=[r for r in links if '10.1007' in r['url']]
jobs=[]
for row in chapters:
    code=re.search(r'BFb[0-9]+',row['url'])[0]
    params=dict(url=row['url'],matchType='exact',output='json',filter='statuscode:200',fl='timestamp,original,mimetype,statuscode,digest',collapse='digest',limit=10)
    jobs.append(dict(kind='public exact archive metadata',name=code+'_cdx',chapter=row['title'],url='https://web.archive.org/cdx/search/cdx?'+urllib.parse.urlencode(params)))
    if code in ('BFb0059505','BFb0059509'):
        jobs.append(dict(kind='normal publisher link',name=code+'_publisher',chapter=row['title'],url=row['url'].replace('http://','https://',1)))

def read(job):
    start=time.perf_counter();out=dict(job)
    try:
        try:response=urllib.request.urlopen(job['url'],timeout=30)
        except urllib.error.HTTPError as exc:response=exc
        body=response.read(2_000_001)
        out.update(status=response.status,final_url=response.url,content_type=response.headers.get('content-type'),bytes=len(body),sha256=hashlib.sha256(body).hexdigest())
        if len(body)>2_000_000:out['bounded_response']='response exceeds2MiB; not parsed'
        dest=ROOT/'sources'/('root_raynaud_'+job['name']+('.json' if job['kind'].endswith('metadata') else '.bin'))
        dest.write_bytes(body);out['saved']=str(dest.relative_to(ROOT))
        if job['kind'].endswith('metadata') and len(body)<=2_000_000:
            try:out['captures']=json.loads(body)
            except ValueError:out['parse']='not JSON'
        else:out['pdf_magic']=body.startswith(b'%PDF-')
    except Exception as exc:out['error']=str(exc)
    out['seconds']=time.perf_counter()-start
    return out
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    rows=list(pool.map(read,jobs))
out=dict(advertised_links=len(links),mathematical_chapters=len(chapters),requests=len(jobs),seconds=time.perf_counter()-START,results=rows)
(ROOT/'code/root_raynaud_gist_captures_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
