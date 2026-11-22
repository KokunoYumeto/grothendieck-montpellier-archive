"""Follow the observed public TDL search handler and advertised JS file.
Observed in saved index-search HTML lines1899–1907 and3520 respectively.
The only dynamic request is a read-only journal-title search.
"""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

root=pathlib.Path(__file__).resolve().parents[1]
started=datetime.datetime.now(datetime.timezone.utc).isoformat(); tick=time.monotonic()
tasks=[
 ('journal_search','https://tamildigitallibrary.in/search/'+urllib.parse.quote('Journal of Indian Mathematical Society',safe='')),
 ('advance_js','https://tamildigitallibrary.in/assets/js/advance_search/advance_search.js')
]
def fetch(task):
    name,url=task; now=time.monotonic(); item={'name':name,'url':url,'method':'GET'}
    try:
        with urllib.request.urlopen(url,timeout=35) as response:
            body=response.read()
            suffix='.js' if name.endswith('_js') else '.html'
            dest=root/'sources'/('part_c_pfluger_tdl_'+name+suffix); dest.write_bytes(body)
            item.update(status=response.status,final_url=response.url,bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),content_type=response.headers.get('Content-Type'),saved_path=str(dest))
    except Exception as error:
        item['error']=type(error).__name__+': '+str(error)
        if isinstance(error,urllib.error.HTTPError):item['status']=error.code
    item['seconds']=time.monotonic()-now
    return item
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool: results=list(pool.map(fetch,tasks))
payload={'started_utc':started,'elapsed_seconds':time.monotonic()-tick,'requests':len(results),'results':results}
out=root/'code/part_c_pfluger_tdl_search_output.json';out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n');out.with_suffix('.txt').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(payload,ensure_ascii=False,indent=2))
