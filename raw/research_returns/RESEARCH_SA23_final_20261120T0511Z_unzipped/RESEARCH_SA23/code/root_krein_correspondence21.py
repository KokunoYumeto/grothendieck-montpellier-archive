"""Fetch and render the custodial Krein correspondence survey; no letter-content claim."""
from pathlib import Path
import datetime, hashlib, json, re, subprocess, time
import fitz
root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
url='https://irbis-nbuv.gov.ua/cgi-bin/irbis_nbuv/cgiirbis_64.exe?C21COM=2&I21DBN=UJRN&IMAGE_FILE_DOWNLOAD=1&Image_file_name=PDF%2Fnpnbuimviv_2013_37_58.pdf&P21DBN=UJRN'
path=root/'sources/root_krein_correspondence2013.pdf'
command=['curl','--location','--fail','--silent','--show-error','--max-time','35','--output',str(path),url]
result=subprocess.run(command,capture_output=True,text=True,timeout=40)
record={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,
        'command':command,'returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr}
if result.returncode==0:
    data=path.read_bytes()
    record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    with fitz.open(path) as doc:
        pages=[page.get_text() for page in doc]
        (root/'sources/root_krein_correspondence2013.txt').write_text('\n\f\n'.join(pages))
        hits={}
        for term in ['грот','groth','лід','лид','фред','1953','1957','гoхбер','гохбер']:
            hits[term]=[{'physical_page':i,'context':text[max(0,m.start()-150):m.end()+260]}
                for i,text in enumerate(pages,1) for m in re.finditer(re.escape(term),text,re.I)]
        (root/'sources/root_krein_correspondence2013_hits.json').write_text(json.dumps(hits,indent=2,ensure_ascii=False)+'\n')
        images=[]
        for number,page in enumerate(doc,1):
            target=root/'sources'/f'root_krein_correspondence2013_p{number:03d}.png'
            page.get_pixmap(matrix=fitz.Matrix(2400/page.rect.width,2400/page.rect.width),alpha=False).save(target)
            images.append(str(target.relative_to(root)))
        record.update(pdf_pages=len(doc),extracted_characters=sum(map(len,pages)),
            hit_counts={term:len(items) for term,items in hits.items()},rendered_pages=list(range(1,len(doc)+1)),images=images,
            visual_inspection='Not implied by rendering; actual inspection recorded separately.')
record['elapsed_seconds']=time.perf_counter()-started
(root/'logs/root_krein_correspondence21.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
