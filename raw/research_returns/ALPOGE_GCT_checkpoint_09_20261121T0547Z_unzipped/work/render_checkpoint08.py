from pathlib import Path
import fitz,json
from PIL import Image,ImageDraw
base=Path(__file__).resolve().parent.parent
pdf=fitz.open(base/'deliverable/ALPOGE_GCT.pdf'); out=base/'work/qa7new';out.mkdir(exist_ok=True)
texts=[p.get_text() for p in pdf]
def first(s): return next(i+1 for i,t in enumerate(texts) if i>10 and s in t)
pages={1,2,4,5,6}
pages.update(range(first('P-F52bs'),first('P-F53a')+1))
pages.update(range(first('P-F58a'),first('Disposition of the main request')+3))
pages.update(range(first('O-SH-B'),first('O-THETA')+1))
pages=sorted(p for p in pages if p<=len(pdf)); thumbs=[]
for n in pages:
 pix=pdf[n-1].get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False);target=out/f'page-{n:03}.png';pix.save(target)
 im=Image.open(target).convert('RGB');im.thumbnail((740,1040));frame=Image.new('RGB',(760,1080),'#d9d9d9');frame.paste(im,((760-im.width)//2,25));ImageDraw.Draw(frame).text((12,6),f'Page {n}',fill='black');thumbs.append(frame)
contacts=[]
for j in range(0,len(thumbs),6):
 sheet=Image.new('RGB',(1520,3240),'white')
 for k,im in enumerate(thumbs[j:j+6]):sheet.paste(im,((k%2)*760,(k//2)*1080))
 path=out/f'contact_{42+j//6:02}.png';sheet.save(path);contacts.append({'file':str(path),'pages':pages[j:j+6]})
manifest={'pdf_pages':len(pdf),'contacts':contacts};(out/'manifest.json').write_text(json.dumps(manifest,indent=2));print(json.dumps(manifest,indent=2))
