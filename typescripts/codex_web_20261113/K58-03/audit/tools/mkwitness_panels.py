from PIL import Image,ImageDraw
from pathlib import Path
import csv,collections
groups=collections.defaultdict(list)
for row in csv.DictReader(open('out/audit/frozen_places.tsv'),delimiter='\t'):groups[row['scan']].append(row)
for n,rows in groups.items():
 for k in range(0,len(rows),8):
  part=rows[k:k+8];out=Image.new('L',(1120,((len(part)+1)//2)*154),253);d=ImageDraw.Draw(out)
  for j,r in enumerate(part):
   x=(j%2)*560;y=(j//2)*154
   new=Path('crops')/(r['scan'].zfill(3)+'_w'+r['id'].split('.')[1]+'.png');p=Image.open(new if new.exists() else Path('crops')/r['crop']);p.thumbnail((549,132))
   label=r['id']+'  '+r['frozen reading'];d.text((x+3,y+1),label.encode('latin-1','replace').decode('latin-1'),fill=0)
   out.paste(p,(x+3,y+18))
  out.save(f'work/wpanel_{n}_{k//8}.jpg',quality=94)
