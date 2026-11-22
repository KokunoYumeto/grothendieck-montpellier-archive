#!/usr/bin/env python3
"""Read public bibliographic APIs for legitimately advertised original locations."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json,time,urllib.request,urllib.parse

root=Path(__file__).resolve().parents[1]
tasks=[]
for doi in ['10.2307/1970720','10.2307/1970785']:
    tasks.append(('openalex',doi,'https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':'doi:https://doi.org/'+doi})))
    tasks.append(('semanticscholar',doi,'https://api.semanticscholar.org/graph/v1/paper/DOI:'+doi+'?fields=title,openAccessPdf,url'))
def run(task):
    service,doi,url=task
    row={'service':service,'doi':doi,'url':url}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'ResearchSourceVerification/1.0'})
        with urllib.request.urlopen(req,timeout=15) as response:
            data=json.load(response)
        if service=='openalex':
            row['results']=[{'title':x.get('title'),'open_access':x.get('open_access'),'locations':x.get('locations')} for x in data.get('results',[])]
        else:
            row['results']=data
        row['status']='metadata_read'
    except Exception as exc:
        row.update(status='unavailable',error=type(exc).__name__+': '+str(exc))
    return row
start=time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as pool:
    rows=list(pool.map(run,tasks))
record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,'results':rows,'original_theorem_text_read':False}
destination=root/'logs/C_original_location_api_probe.json'
if destination.exists():
    raise SystemExit('Refusing to overwrite the recorded first API probe')
destination.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
