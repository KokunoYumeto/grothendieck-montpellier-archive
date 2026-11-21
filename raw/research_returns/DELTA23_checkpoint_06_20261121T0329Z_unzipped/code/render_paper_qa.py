#!/usr/bin/env python3
"""Render the full paper and labeled contact sheets for visual layout review."""
from pathlib import Path
import fitz,json,sys
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[2];work=root/'work'
label=sys.argv[1] if len(sys.argv)>1 else 'current'
out=work/'private'/('pdfqa_'+label);out.mkdir(parents=True,exist_ok=True)
doc=fitz.open(work/'package/DELTA23.pdf');thumbs=[];stats=[]
for i,p in enumerate(doc):
 pix=p.get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False);pix.save(out/f'page_{i+1:03d}.png')
 im=Image.open(out/f'page_{i+1:03d}.png');im.thumbnail((300,430));thumbs.append(im.copy())
 stats.append({'page':i+1,'characters':len(p.get_text()),'text_blocks':len(p.get_text('blocks'))})
for j in range(0,len(thumbs),16):
 sh=Image.new('RGB',(4*324,4*464),'#d9dde2');draw=ImageDraw.Draw(sh)
 for k,im in enumerate(thumbs[j:j+16]):
  x=(k%4)*324+12;y=(k//4)*464+24;sh.paste(im,(x,y));draw.text((x,y-18),f'Page{j+k+1}',fill='black')
 sh.save(out/f'contact_{j//16+1}.png')
(work/'records'/f'pdfqa_{label}_stats.json').write_text(json.dumps(stats,indent=2)+'\n')
print(json.dumps({'pages':len(doc),'sheets':(len(doc)+15)//16,'directory':str(out),'short_pages':[x for x in stats if x['characters']<100]},indent=2))
