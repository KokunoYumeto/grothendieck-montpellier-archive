#!/usr/bin/env python3
"""Open identified public PDFs in memory, retaining only retrieval metadata.

Optional pages (zero-based) are printed for inspection; copyrighted source
text/PDFs are not saved into the deliverable. Temporary page images, if any,
must be removed after viewing.
"""
import sys,urllib.request,hashlib,json,datetime
from pathlib import Path
import fitz
url=sys.argv[1];pages=[int(n) for n in sys.argv[2:]]
out=Path('/workspace/scratch/c38eb4e8f07f/SA18_work/parts/agent46')
event=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),url=url,pdf_page_indices_requested=pages)
try:
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (mathematical source verification)'}),timeout=25) as r:
        raw=r.read();event['final_url']=r.url;event['http_status']=r.status
    doc=fitz.open(stream=raw,filetype='pdf')
    event.update(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),pages=len(doc),opened=True)
    print(json.dumps(event))
    for n in pages:
        tx=doc[n].get_text()
        print('PDF_PAGE_INDEX',n,'TEXT_LENGTH',len(tx))
        for i,line in enumerate(tx.splitlines(),1):print(f'P{n}:L{i}: {line}')
        if not tx.strip():
            d=out/'temporary_public';d.mkdir(exist_ok=True)
            dest=d/f'page_{n}.png';doc[n].get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(dest);print('IMAGE',dest)
except Exception as e:
    event.update(opened=False,error=type(e).__name__+': '+str(e));print(json.dumps(event))
with (out/'outputs'/'public_pdf_open_events.jsonl').open('a') as f:f.write(json.dumps(event)+'\n')
