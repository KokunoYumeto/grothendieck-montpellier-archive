#!/usr/bin/env python3
"""Bounded public catalogue reads for two still-unopened requested books.

This script reads metadata only. It makes no request for restricted book
files and does not initiate borrowing, authentication, or an author contact.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import json
import time
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'literature/ROOT_classical_books_catalogue'
OUT.mkdir(exist_ok=True)

def fetch(job):
    name,url=job
    row={'name':name,'requested_url':url,'started_utc':datetime.now(timezone.utc).isoformat()}
    start=time.perf_counter()
    try:
        with urlopen(url,timeout=30) as response:
            data=response.read()
            row.update(status=response.status,final_url=response.url,content_type=response.headers.get('Content-Type'))
    except HTTPError as error:
        data=error.read()
        row.update(status=error.code,final_url=error.url,error=str(error))
    except Exception as error:
        row.update(error=repr(error),elapsed_seconds=time.perf_counter()-start,finished_utc=datetime.now(timezone.utc).isoformat())
        return row
    destination=OUT/(name+'.json')
    destination.write_bytes(data)
    row.update(bytes=len(data),sha256=sha256(data).hexdigest(),response_path=str(destination.relative_to(ROOT)))
    try:
        row['response']=json.loads(data)
    except (ValueError,UnicodeError):
        row['response_text']=data.decode('utf-8',errors='replace')
    row.update(elapsed_seconds=time.perf_counter()-start,finished_utc=datetime.now(timezone.utc).isoformat())
    return row

if __name__=='__main__':
    start=time.perf_counter()
    query='title:(Foundations of the theory of Klein surfaces) AND mediatype:texts'
    jobs=[
      ('lehto_openlibrary','https://openlibrary.org/books/OL5430919M.json'),
      ('lehto_archive_metadata','https://archive.org/metadata/quasiconformalma00leht'),
      ('alling_archive_search','https://archive.org/advancedsearch.php?'+urlencode({'q':query,'fl[]':['identifier','title','creator','year'],'rows':30,'page':1,'output':'json'},doseq=True)),
    ]
    with ThreadPoolExecutor(max_workers=3) as pool:
        results=list(pool.map(fetch,jobs))
    record={'recorded_utc':datetime.now(timezone.utc).isoformat(),'scope':'Three ordinary public metadata queries; any private/restricted full-text flags are respected and no full-text file is requested by this program.','request_count':3,'elapsed_seconds':time.perf_counter()-start,'results':results}
    (ROOT/'logs/ROOT_classical_books_catalogue.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
    for row in results:
        summary={k:row.get(k) for k in ['name','status','bytes','elapsed_seconds','error']}
        response=row.get('response',{})
        if row['name']=='lehto_archive_metadata':
            summary['metadata']=response.get('metadata')
            summary['files']=[{k:f.get(k) for k in ['name','format','private','size']} for f in response.get('files',[])]
        else:
            summary['response']=response
        print(json.dumps(summary,ensure_ascii=False))
