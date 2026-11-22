"""Extract the retrieved original review and render its relevant printed page."""
from pathlib import Path
import fitz,json,time,datetime
R=Path('RESEARCH_SA23');t=time.monotonic();p=R/'sources/algebra_mendoza_koranyi_review.pdf';d=fitz.open(p)
texts=[page.get_text() for page in d];p.with_suffix('.txt').write_text('\n\f\n'.join(texts))
hits=[]
for i,text in enumerate(texts):
 if 'Segundo' in text or 'Korányi' in text or 'Kor' in text and 'Symposium' in text:
  image=R/f'sources/algebra_mendoza_koranyi_review_pdfpage{i+1:03}.png'
  d[i].get_pixmap(matrix=fitz.Matrix(2,2)).save(image)
  hits.append({'pdf_page':i+1,'text':text,'image':str(image.relative_to(R))})
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'pages':len(d),'hits':hits,'elapsed_seconds':time.monotonic()-t}
s=json.dumps(out,ensure_ascii=False,indent=2);(R/'logs/algebra_mendoza_render58.json').write_text(s+'\n');print(s)
