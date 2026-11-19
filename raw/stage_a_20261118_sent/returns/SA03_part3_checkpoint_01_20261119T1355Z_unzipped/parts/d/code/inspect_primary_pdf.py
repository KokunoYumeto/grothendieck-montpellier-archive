"""Reproduce primary-PDF retrieval and selected-page visual inspection.

Downloaded full texts stay in work/, outside the deliverable. The short manifest
records URLs and locators; images were inspected with the image viewer.
"""
from pathlib import Path
import urllib.request, json, sys, datetime
import fitz
root=Path(__file__).resolve().parents[4]
out=Path(__file__).resolve().parents[1]/'outputs'
work=root/'work';work.mkdir(exist_ok=True)
sources={
 'barsottitate':('https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/barsottitate.pdf',range(103,115)),
 'katz1972':('https://web.math.princeton.edu/~nmk/old/algsoln.pdf',[23,41]),
}
name=sys.argv[1] if len(sys.argv)>1 else 'katz1972'
url,pages=sources[name];path=work/(name+'.pdf')
if not path.exists():
    with urllib.request.urlopen(url,timeout=45) as r:path.write_bytes(r.read())
doc=fitz.open(path)
records=[]
for page in pages:
    p=doc[page-1];image=work/f'{name}-{page}.png'
    p.get_pixmap(matrix=fitz.Matrix(1.6,1.6)).save(image)
    records.append({'pdf_page_1_based':page,'render':str(image),'extracted_text_length':len(p.get_text())})
manifest={'date':datetime.datetime.now(datetime.timezone.utc).isoformat(),'url':url,'pdf_pages':len(doc),'pages':records,'scope':'Visual inspection locators; no assertion of proof review merely from download.'}
(out/f'{name}_inspection.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(manifest,indent=2))
