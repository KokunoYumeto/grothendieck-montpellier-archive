#!/usr/bin/env python3
from pathlib import Path
import argparse, subprocess, json, math
from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader
p=argparse.ArgumentParser(); p.add_argument('pdf',type=Path); p.add_argument('out',type=Path); a=p.parse_args()
a.out.mkdir(parents=True,exist_ok=True)
prefix=a.out/'page'
cmd=['pdftoppm','-scale-to','1600','-png',str(a.pdf),str(prefix)]
r=subprocess.run(cmd,capture_output=True,text=True,timeout=150)
(a.out/'render.log').write_text(r.stdout+r.stderr)
if r.returncode:raise SystemExit(r.returncode)
files=sorted(a.out.glob('page-*.png')); pages=len(PdfReader(a.pdf).pages); assert len(files)==pages
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',18)
thumb_w,thumb_h=390,552; cell_w,cell_h=420,592
sheets=[]
for start in range(0,pages,9):
 chunk=files[start:start+9]; rows=math.ceil(len(chunk)/3)
 canvas=Image.new('RGB',(3*cell_w+20,rows*cell_h+20),'#e8e8e8'); draw=ImageDraw.Draw(canvas)
 for j,f in enumerate(chunk):
  im=Image.open(f).convert('RGB'); im.thumbnail((thumb_w,thumb_h))
  x=20+(j%3)*cell_w; y=20+(j//3)*cell_h
  canvas.paste(im,(x,y)); draw.text((x,y+thumb_h+4),f'Page {start+j+1}',fill='black',font=font)
 out=a.out/f'contact_{start//9+1:02d}.png'; canvas.save(out); sheets.append(str(out))
report={'pdf':str(a.pdf),'pages':pages,'render_command':cmd,'contact_sheets':sheets,'page_images':[str(x) for x in files]}
(a.out/'RENDER_MANIFEST.json').write_text(json.dumps(report,indent=2)+'\n'); print(json.dumps(report,indent=2))
