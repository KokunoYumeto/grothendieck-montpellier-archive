"""Retrieve a public historical research paper as a correspondence finding aid.

This records extraction and keyword locations, not a claim of visual reading.
The PDF's source status and actual read scope are recorded separately.
"""
from pathlib import Path
import datetime, hashlib, json, re, time, urllib.request
import fitz

root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
url='https://www.diva-portal.org/smash/get/diva2%3A1849851/FULLTEXT01.pdf'
record={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,
        'purpose':'Find a concrete original correspondence locator; no mathematical theorem is inferred from this biography.'}
try:
    request=urllib.request.Request(url,headers={'User-Agent':'ResearchSourceVerification/1.0'})
    with urllib.request.urlopen(request,timeout=40) as response:
        data=response.read()
        record.update(http_status=response.status,content_type=response.headers.get('Content-Type'),final_url=response.url)
    path=root/'sources/root_schatten_biography2023.pdf'
    path.write_bytes(data)
    record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    doc=fitz.open(path)
    pages=[page.get_text() for page in doc]
    (root/'sources/root_schatten_biography2023.txt').write_text('\n\f\n'.join(pages))
    needles=['groth','lids','trace','genus','letter','correspond','archive','unpublish','kadison','fredholm','acknowledg']
    hits={}
    for term in needles:
        entries=[]
        for i,text in enumerate(pages,1):
            for match in re.finditer(re.escape(term),text,re.I):
                entries.append({'physical_page':i,'context':text[max(0,match.start()-220):min(len(text),match.end()+460)]})
        hits[term]=entries
    (root/'sources/root_schatten_biography2023_hits.json').write_text(json.dumps(hits,indent=2,ensure_ascii=False)+'\n')
    record.update(pdf_pages=len(pages),extracted_characters=sum(map(len,pages)),
                  hits={key:len(value) for key,value in hits.items()},
                  pages_with_hits=sorted({entry['physical_page'] for values in hits.values() for entry in values}))
except Exception as exc:
    record.update(failed=True,error=repr(exc))
record.update(completed_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-started)
(root/'logs/root_schatten_correspondence18.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
