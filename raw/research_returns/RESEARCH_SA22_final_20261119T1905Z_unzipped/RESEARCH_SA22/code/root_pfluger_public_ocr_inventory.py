"""Search advertised public journal OCR to test potentially incorrect metadata.

Only files explicitly listed in previously read Internet Archive metadata are
eligible. Private/restricted records are excluded. No PDF or page-image file
is requested. This is discovery, not mathematical proof or palaeographic QA.
"""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()
catalogue = json.loads((ROOT/'sources/indian_mathematical_broad.json').read_text())['response']['docs']
jobs = []
excluded = []
for doc in catalogue:
    ident = doc['identifier']
    p = ROOT/'sources'/('metadata_'+ident+'.json')
    if not p.exists():
        excluded.append(dict(identifier=ident, reason='no previously saved full metadata'))
        continue
    payload = json.loads(p.read_text())
    meta = payload.get('metadata', {})
    if str(meta.get('access-restricted-item','')).lower() == 'true':
        excluded.append(dict(identifier=ident, reason='access-restricted-item=true'))
        continue
    files = [f for f in payload.get('files', [])
             if f.get('format') == 'DjVuTXT' and str(f.get('private','')).lower() != 'true']
    if not files:
        excluded.append(dict(identifier=ident, reason='no advertised nonprivate OCR file'))
        continue
    for f in files:
        jobs.append(dict(identifier=ident, filename=f['name'],
                         bytes_advertised=f.get('size'), title=meta.get('title')))

cache = ROOT/'sources/pfluger_public_journal_ocr'
cache.mkdir(exist_ok=True)
pattern = re.compile(r'pfl[uü]g[eë]r|pflu.{0,3}ger|verheft|konstruktion.{0,60}riemann|golden.{0,20}jubilee', re.I)

def fetch(job):
    before = time.perf_counter()
    result = dict(job)
    url = 'https://archive.org/download/'+urllib.parse.quote(job['identifier'],safe='')+'/'+urllib.parse.quote(job['filename'],safe='')
    result['url'] = url
    target = cache/(hashlib.sha256(url.encode()).hexdigest()[:20]+'.txt')
    try:
        if target.exists():
            body=target.read_bytes(); result['cached']=True
        else:
            with urllib.request.urlopen(url,timeout=35) as response:
                result['status']=response.status
                body=response.read()
            target.write_bytes(body); result['cached']=False
        text=body.decode('utf-8','replace')
        matches=list(pattern.finditer(text))
        result.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest(),
                      saved=str(target.relative_to(ROOT)),
                      matched_terms=len(matches),
                      excerpts=[text[max(0,m.start()-250):m.end()+350] for m in matches[:30]],
                      frontmatter=text[:1600],
                      frontmatter_years=sorted(set(re.findall(r'\b19\d\d\b',text[:6000]))))
    except Exception as exc:
        result['error']=str(exc)
    result['seconds']=time.perf_counter()-before
    return result

rows=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    for row in executor.map(fetch,jobs):
        rows.append(row)
        if len(rows)%20==0:
            print(json.dumps(dict(completed=len(rows),total=len(jobs),elapsed_seconds=time.perf_counter()-START)),flush=True)
out=dict(catalogue_records=len(catalogue), eligible_ocr_files=len(jobs),
         requested=sum(not x.get('cached',False) for x in rows),
         excluded=excluded, seconds=time.perf_counter()-START,
         errors=[x for x in rows if 'error' in x],
         candidate_files=[x['identifier'] for x in rows if x.get('matched_terms',0)],results=rows)
(ROOT/'code/root_pfluger_public_ocr_inventory_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('results','excluded','errors')},indent=2))
