"""Query only the public capture index of Gabber's observed IHES author directory."""
import datetime, hashlib, json, time, urllib.parse, urllib.request
from pathlib import Path
url = 'https://web.archive.org/cdx/search/cdx?' + urllib.parse.urlencode({
    'url':'www.ihes.fr/~/gabber/*','output':'json','filter':'statuscode:200',
    'collapse':'urlkey','fl':'timestamp,original,mimetype,statuscode','limit':'200'})
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(), 'url':url,
     'scope':'Publicly captured author-directory URLs only; not a restricted publisher or journal collection.'}
start=time.perf_counter()
try:
    with urllib.request.urlopen(url,timeout=30) as r:
        body=r.read();out.update(status=r.status,final_url=r.url,bytes=len(body),
                                sha256=hashlib.sha256(body).hexdigest())
    try:out['records']=json.loads(body)
    except Exception:out['text']=body.decode('utf-8','replace')[:5000]
except Exception as e:
    out['error']=f'{type(e).__name__}: {e}'
out['elapsed_seconds']=time.perf_counter()-start
Path(__file__).resolve().parents[1].joinpath('logs/B_Gabber_public_author_archive.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
