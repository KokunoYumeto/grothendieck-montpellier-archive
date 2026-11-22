"""Audit whole-source keyword coverage and render selected original Dunford pages."""
import datetime
import hashlib
import json
import pathlib
import re
import fitz
base=pathlib.Path(__file__).resolve().parents[1]
path=base/'sources/algebra_spectral_dunford1958_survey.pdf'
doc=fitz.open(path)
texts=[page.get_text() for page in doc]
output={'utc_recorded':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'pdf_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'pdf_pages':len(doc),'text_characters_by_page':list(map(len,texts)),
 'searches':{},'selected_pages':[]}
for term in ['groth','grot','lidsk','schatten','trace','genus','communicat','unpublish','letter','acknowledg']:
 output['searches'][term]=[{'physical_page':i+1,'count':len(re.findall(term,text,re.I))} for i,text in enumerate(texts) if re.search(term,text,re.I)]
for physical in [1,5,7,9,56,57,58]:
 image=base/f'sources/algebra_spectral_dunford1958_p{physical:03}.png'
 doc[physical-1].get_pixmap(matrix=fitz.Matrix(1.7,1.7)).save(image)
 output['selected_pages'].append({'physical_page':physical,'printed_page':216+physical,'image':str(image.relative_to(base)),'native_text':texts[physical-1]})
output['source_access_correction']={'file':'sources/algebra_spectral_dunford_schwartz_I_public_ocr.html','classification':'HTTP200 JavaScript/cookie verification challenge, 6182 bytes; not book text. No challenge attempted. Web-reader cached OCR snippets had been opened separately; not a direct original-page inspection.'}
payload=json.dumps(output,ensure_ascii=False,indent=2)
(base/'logs/algebra_spectral_analyze51.json').write_text(payload+'\n')
print(payload)
