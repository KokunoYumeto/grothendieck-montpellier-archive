"""Render a spread of pages, including every reported problematic page, for manual QA."""
from pathlib import Path
import json
import fitz
from PIL import Image,ImageOps,ImageDraw
w=Path(__file__).resolve().parents[1]; d=fitz.open(w/'RESEARCH_SA15_paper.pdf')
problem=[i+1 for i,p in enumerate(d) if any(q in p.get_text() for q in ['product order and the Hodge-first order','verify_nonfinite_reduction'])]
new_results=[i+1 for i,p in enumerate(d) if any(q in p.get_text() for q in ['Determinants in the two initial degrees','an elementary exact group calculation','dual-number coefficient'])]
pages=sorted(set([1,14,24,28,39,55,70,85,len(d)]+problem+new_results))
folder=w/'outputs/qa';folder.mkdir(exist_ok=True)
ims=[]
for num in pages:
 p=d[num-1].get_pixmap(matrix=fitz.Matrix(1.1,1.1));path=folder/f'page_{num:03d}.png';p.save(path)
 im=Image.open(path).convert('RGB'); im=ImageOps.expand(im,border=(2,24,2,2),fill='white');ImageDraw.Draw(im).text((8,5),f'Page {num}',fill='black');ims.append(im)
for j in range(0,len(ims),4):
 block=ims[j:j+4];ww=max(im.width for im in block);hh=max(im.height for im in block);sheet=Image.new('RGB',(ww*2,hh*2),'#cccccc')
 for i,im in enumerate(block):sheet.paste(im,((i%2)*ww,(i//2)*hh))
 sheet.save(folder/f'montage_{j//4+1}.png')
(w/'outputs/visual_qa_pending.json').write_text(json.dumps({'pages_in_pdf':len(d),'pages_rendered':pages,'prior_overflow_pages':problem},indent=2)+'\n')
print({'pages':len(d),'rendered':pages,'montages':(len(ims)+3)//4})
