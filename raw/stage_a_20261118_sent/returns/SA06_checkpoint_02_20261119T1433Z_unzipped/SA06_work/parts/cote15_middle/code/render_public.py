"""Render selected already-downloaded primary-source PDF pages for visual checks."""
from pathlib import Path
import fitz,sys,json
P=Path('/workspace/scratch/a5176e5b5d45/SA06_work/parts/cote15_middle/research')
name=sys.argv[1]
doc=fitz.open(P/name)
pages=[int(x)-1 for x in sys.argv[2:]]
if not pages and 'Topology' in name:
    pages=[i for i,p in enumerate(doc) if 'lusinien' in p.get_text().lower() and 'dyadique' in p.get_text().lower()]
for i in pages:
    output=P/(Path(name).stem+f'_page-{i+1}.png')
    doc[i].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(output)
    print(json.dumps({'pdf':name,'pdf_page':i+1,'output':str(output),'total_pages':len(doc)}))
