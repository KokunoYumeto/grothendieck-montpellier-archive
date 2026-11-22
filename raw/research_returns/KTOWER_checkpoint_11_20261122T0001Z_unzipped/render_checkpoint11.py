"""Render every current paper page to six-page contact sheets for visual review."""
from pathlib import Path
import hashlib, json
import fitz
from PIL import Image, ImageDraw
B=Path(__file__).resolve().parent
D=B/'pdf_review11';D.mkdir(exist_ok=True)
doc=fitz.open(B/'KTOWER.pdf')
page_hashes=[];sheets=[]
for start in range(0,len(doc),6):
 canvas=Image.new('RGB',(1500,2190),'#dddddd');draw=ImageDraw.Draw(canvas)
 for k,n in enumerate(range(start,min(start+6,len(doc)))):
  pix=doc[n].get_pixmap(matrix=fitz.Matrix(0.8,0.8),alpha=False)
  im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
  page_hashes.append({'page':n+1,'pixels_sha256':hashlib.sha256(pix.samples).hexdigest()})
  im.thumbnail((730,700));x=(k%2)*750+(750-im.width)//2;y=(k//2)*730+24
  canvas.paste(im,(x,y));draw.text(((k%2)*750+15,(k//2)*730+6),f'Page {n+1}',fill='black')
 path=D/f'checkpoint11_{start//6+1:02d}.png';canvas.save(path)
 sheets.append({'path':str(path.relative_to(B)),'pages':list(range(start+1,min(start+6,len(doc))+1))})
manifest={'tex_sha256':hashlib.sha256((B/'KTOWER.tex').read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256((B/'KTOWER.pdf').read_bytes()).hexdigest(),'pages':len(doc),'sheets':sheets,'page_pixel_hashes':page_hashes}
(D/'render_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({k:manifest[k] for k in ['pages','tex_sha256','pdf_sha256']}))
