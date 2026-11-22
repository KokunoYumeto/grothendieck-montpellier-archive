from pathlib import Path
import json,sys,csv
from PIL import Image,ImageEnhance
n=int(sys.argv[1])
with Image.open(f'K58-03_58_scan{n:03}.jpg') as orig:
 for ident,box,*ang in json.load(sys.stdin):
  name=f'{n:03}_w{ident}.png'
  if (Path('crops')/name).exists():raise ValueError(name)
  c=orig.convert('L').crop(box)
  if ang:c=c.rotate(ang[0],Image.Resampling.BICUBIC,expand=True,fillcolor=255)
  c=ImageEnhance.Contrast(c).enhance(1.35);c.resize((c.width*3,c.height*3),Image.Resampling.LANCZOS).save(Path('crops')/name)
  with open('out/crop_coordinates.tsv','a') as f:csv.writer(f,delimiter='\t').writerow([n,name,*box,ang[0] if ang else 0])
