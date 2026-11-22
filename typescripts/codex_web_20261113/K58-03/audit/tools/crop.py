from pathlib import Path
from PIL import Image, ImageOps, ImageEnhance, ImageDraw
import sys,json
n=int(sys.argv[1]); key=f'{n:03}'; base=Path('crops')
im=Image.open(f'K58-03_58_scan{n:03}.jpg').convert('L')
items=json.load(sys.stdin)
log=Path('out/crop_coordinates.tsv')
if not log.exists(): log.write_text('scan\tcrop\tleft\ttop\tright\tbottom\n')
imgs=[]
with log.open('a') as f:
 for label,box,*angles in items:
  name=f'{key}_{label}.png'
  c=im.crop(tuple(box))
  if angles: c=c.rotate(angles[0],Image.Resampling.BICUBIC,expand=True,fillcolor=255)
  c=ImageEnhance.Contrast(c).enhance(1.35)
  c=c.resize((c.width*3,c.height*3),Image.Resampling.LANCZOS)
  c.save(base/name)
  print(n,name,*box,angles[0] if angles else 0,sep='\t',file=f)
  pr=c.copy(); pr.thumbnail((1350,370))
  imgs.append((name,pr))
width=max(c.width for _,c in imgs)+12
height=sum(c.height+25 for _,c in imgs)
sheet=Image.new('L',(width,height),245); draw=ImageDraw.Draw(sheet); y=0
for label,c in imgs:
 draw.text((4,y),label,fill=0); sheet.paste(c,(4,y+17)); y+=c.height+25
sheet.save(base/f'{key}_details.jpg',quality=94)
