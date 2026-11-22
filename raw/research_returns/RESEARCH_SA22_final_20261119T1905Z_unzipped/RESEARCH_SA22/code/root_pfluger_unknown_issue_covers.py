"""Inspect advertised public covers of three undated scans and one1958 volume.

The journal OCR was produced with a Tamil language setting. A negative
Latin-title search therefore cannot establish absence. This ordinary public
file retrieval is a metadata/cover check, not a mathematical source reading.
"""
from pathlib import Path
import concurrent.futures, hashlib, json, re, time, urllib.parse, urllib.request

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
data=json.loads((ROOT/'code/root_pfluger_public_ocr_inventory_output.json').read_text())
jobs=[]
for row in data['results']:
    if not row['identifier'].startswith('tdl.'): continue
    payload=json.loads((ROOT/'sources'/('metadata_'+row['identifier']+'.json')).read_text())
    meta=payload.get('metadata',{})
    if str(meta.get('access-restricted-item','')).lower()=='true': continue
    pdfs=[f['name'] for f in payload['files'] if f.get('format') in ('Image Container PDF','Text PDF','Additional Text PDF')]
    years=sorted(set(re.findall(r'19[0-9]{2}',str(pdfs))))
    if years and not any(int(y)>=1957 for y in years): continue
    covers=[f for f in payload['files'] if f['name']=='cover.jpg' and str(f.get('private','')).lower()!='true']
    for cover in covers:
        jobs.append(dict(identifier=row['identifier'],filename=cover['name'],pdf_filenames=pdfs,filename_years=years))

def fetch(job):
    t=time.perf_counter(); out=dict(job)
    url='https://archive.org/download/'+urllib.parse.quote(job['identifier'],safe='')+'/'+urllib.parse.quote(job['filename'],safe='')
    out['url']=url
    try:
        with urllib.request.urlopen(url,timeout=30) as response:
            body=response.read(); out.update(status=response.status,content_type=response.headers.get('content-type'))
        target=ROOT/'sources'/('pfluger_cover_'+job['identifier'].split('-')[0]+'.jpg')
        target.write_bytes(body)
        out.update(bytes=len(body),sha256=hashlib.sha256(body).hexdigest(),saved=str(target.relative_to(ROOT)))
    except Exception as exc: out['error']=str(exc)
    out['seconds']=time.perf_counter()-t
    return out

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    rows=list(pool.map(fetch,jobs))
out=dict(scope='Public advertised covers only; no title-absence inference from bad OCR',requested=len(rows),results=rows,seconds=time.perf_counter()-START)
(ROOT/'code/root_pfluger_unknown_issue_covers_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
