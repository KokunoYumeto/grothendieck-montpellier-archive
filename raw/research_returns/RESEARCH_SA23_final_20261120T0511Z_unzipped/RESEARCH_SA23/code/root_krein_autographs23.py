"""Retrieve one advertised public bibliographic guide; not the autograph catalogue."""
from pathlib import Path
import datetime, hashlib, json, subprocess, time

root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
url='https://catalog.odnb.odessa.ua/ONNB_ec/NashiVid/sNaykVidan/rikunBiblioPokagch.pdf'
dest=root/'sources/root_rikun_bibliographic_guide.pdf'
record={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'url':url,'scope':'One advertised public guide; the original 2000 autograph catalogue remains distinct.'}
result=subprocess.run(['curl','--location','--fail','--max-time','35','--connect-timeout','12',
                       '--silent','--show-error','--output',str(dest),url],capture_output=True,text=True)
record.update(returncode=result.returncode,stderr=result.stderr,
              elapsed_seconds=time.perf_counter()-started)
if result.returncode==0:
    data=dest.read_bytes()
    record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
    import fitz
    with fitz.open(dest) as document:
        record['pages']=len(document)
        texts=[page.get_text() for page in document]
    (root/'sources/root_rikun_bibliographic_guide.txt').write_text('\n\f\n'.join(texts))
    hits=[]
    for number,page in enumerate(texts,1):
        if any(term in page.lower() for term in ['крейн','гротен','grothendieck']):
            hits.append({'pdf_page':number,'text':page})
    (root/'sources/root_rikun_bibliographic_hits.json').write_text(json.dumps(hits,ensure_ascii=False,indent=2)+'\n')
    record['matching_pages']=[hit['pdf_page'] for hit in hits]
(root/'logs/root_krein_autographs23.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
