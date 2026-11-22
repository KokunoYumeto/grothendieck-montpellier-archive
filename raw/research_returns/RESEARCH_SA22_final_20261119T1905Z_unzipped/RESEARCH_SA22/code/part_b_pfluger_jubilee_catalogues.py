#!/usr/bin/env python3
"""Search public IA metadata for the separately catalogued Jubilee volume.

No Indian/Mathematical keyword or year restriction is imposed on the first two
queries. This is public metadata only. All returned rows and exact total counts
are retained; an initial250-row cap is explicit, not treated as exhaustive.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen
import gzip,json,re,time

root=Path(__file__).resolve().parents[1];started=time.monotonic()
queries=[('golden_jubilee_title','title:("Golden Jubilee")'),
         ('jubilee_commemoration_title','title:("Jubilee Commemoration")'),
         ('1907_1958_variant','(title:("1907-1958") OR description:("1907-1958") OR title:("1907–1958") OR description:("1907–1958")) AND (title:(Jubilee) OR description:(Jubilee))')]
fields=['identifier','title','date','creator','description','year','publisher','mediatype']

def search(job):
    name,query=job;start=time.monotonic()
    params=[('q',query),('rows','250'),('page','1'),('output','json')]+[('fl[]',field) for field in fields]
    url='https://archive.org/advancedsearch.php?'+urlencode(params)
    record={'name':name,'query':query,'url':url,'scope':'Public catalogue only; no source file request'}
    try:
        with urlopen(Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'}),timeout=25) as response:
            raw=response.read(6*1024*1024+1)
            record.update(http_status=response.status,bytes=len(raw),final_url=response.url)
        if raw[:2]==b'\x1f\x8b':raw=gzip.decompress(raw)
        if len(raw)>6*1024*1024:
            record['status']='Response cap reached; no catalogue read'
        else:
            data=json.loads(raw);(root/'sources'/('part_b_pfluger_'+name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
            result=data.get('response',{});docs=result.get('docs',[])
            record.update(status='Public metadata read',num_found=result.get('numFound'),returned=len(docs),
                          complete_for_query=result.get('numFound',0)<=len(docs),records=docs)
            record['candidate_identifiers']=[d.get('identifier') for d in docs if re.search(r'1907|1958|1961|mathem|Pfluger|Madras|Poona|Jubilee Commemoration',json.dumps(d),re.I)]
    except Exception as error:record.update(status='Request failed; no retry/bypass',error=str(error))
    record['elapsed_seconds']=time.monotonic()-start;return record

with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(search,queries))
output={'results':results,'elapsed_seconds':time.monotonic()-started,'request_count':len(queries)}
(root/'code/part_b_pfluger_jubilee_catalogues_output.json').write_text(json.dumps(output,indent=2)+'\n')
for result in results:print(json.dumps({k:v for k,v in result.items() if k!='records'},indent=2))
print('whole_elapsed_seconds',output['elapsed_seconds'])
