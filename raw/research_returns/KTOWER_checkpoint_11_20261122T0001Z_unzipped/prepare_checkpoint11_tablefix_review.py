from pathlib import Path
import json,hashlib
import fitz
from PIL import Image,ImageDraw
B=Path(__file__).resolve().parent;D=B/'pdf_review11_tablefix';D.mkdir(exist_ok=True)
old=json.loads((B/'pdf_review11_postnotes/render_manifest.json').read_text())
oldhash={x['page']:x['pixels_sha256'] for x in old['page_pixel_hashes']}
doc=fitz.open(B/'KTOWER.pdf');hs=[];changed=[]
for i,p in enumerate(doc,1):
 pix=p.get_pixmap(matrix=fitz.Matrix(.8,.8),alpha=False)
 h=hashlib.sha256(pix.samples).hexdigest();hs.append({'page':i,'pixels_sha256':h})
 if oldhash.get(i)!=h:changed.append(i)
sheets=[]
for start in range(0,len(changed),6):
 ns=changed[start:start+6];can=Image.new('RGB',(1500,2190),'#ddd');dr=ImageDraw.Draw(can)
 for j,n in enumerate(ns):
  pix=doc[n-1].get_pixmap(matrix=fitz.Matrix(.8,.8),alpha=False);im=Image.frombytes('RGB',(pix.width,pix.height),pix.samples);im.thumbnail((730,700));x=(j%2)*750+(750-im.width)//2;y=(j//2)*730+24;can.paste(im,(x,y));dr.text(((j%2)*750+15,(j//2)*730+6),f'Page {n}',fill='black')
 path=D/f'changed_{start//6+1:02d}.png';can.save(path);sheets.append({'path':str(path.relative_to(B)),'pages':ns})
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
r={'tex_sha256':h(B/'KTOWER.tex'),'pdf_sha256':h(B/'KTOWER.pdf'),'pages':len(doc),'predecessor_pdf_sha256':old['pdf_sha256'],'changed_pages':changed,'identical_pages':[i for i in range(1,len(doc)+1) if i not in changed],'page_pixel_hashes':hs,'sheets':sheets}
(D/'render_manifest.json').write_text(json.dumps(r,indent=2)+'\n')
print({k:r[k] for k in ['tex_sha256','pdf_sha256','pages','changed_pages','sheets']})
