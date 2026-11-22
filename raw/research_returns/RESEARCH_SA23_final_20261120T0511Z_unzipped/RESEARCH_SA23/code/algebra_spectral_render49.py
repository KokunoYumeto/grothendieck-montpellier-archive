"""Render exactly the public Schatten source pages selected for documentary reading."""
import datetime
import hashlib
import json
import pathlib
import fitz

base = pathlib.Path(__file__).resolve().parents[1]
records=[]
for name,pages in [('schatten1960_front',[1,5,6]),('schatten1960_back',[1,2]),('schatten1960_preview',[1,2])]:
 path=base/f'sources/algebra_spectral_{name}.pdf'
 doc=fitz.open(path)
 for physical in pages:
  out=base/f'sources/algebra_spectral_{name}_p{physical:03}.png'
  doc[physical-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(out)
  records.append({'pdf':str(path.relative_to(base)),'physical_page':physical,'image':str(out.relative_to(base)),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'native_text':doc[physical-1].get_text()})
data={'utc_rendered':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pages':records,'scope':'Rendering is not itself a claim of direct visual inspection; actual readings recorded separately.'}
payload=json.dumps(data,ensure_ascii=False,indent=2)
(base/'logs/algebra_spectral_render49.json').write_text(payload+'\n')
print(payload)
