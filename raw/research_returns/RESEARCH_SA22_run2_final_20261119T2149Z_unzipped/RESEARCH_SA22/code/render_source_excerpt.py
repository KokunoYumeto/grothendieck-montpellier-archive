#!/usr/bin/env python3
"""Render explicitly selected source pages; this does not certify reading."""
from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import time
import fitz
from PIL import Image, ImageDraw

p=argparse.ArgumentParser()
p.add_argument('source')
p.add_argument('--pages',required=True)
p.add_argument('--stem',required=True)
p.add_argument('--scale',type=float,default=1.6)
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
source=(root/a.source).resolve()
assert source.is_relative_to(root/'literature')
assert a.stem and '/' not in a.stem and '..' not in a.stem
out=root/'qa'/a.stem
out.mkdir(parents=True,exist_ok=True)
log=root/'logs'/(a.stem+'_render.json')
assert not log.exists(), 'Use a distinct stem to preserve the earlier render receipt.'
pages=set()
for part in a.pages.split(','):
    ends=[int(x) for x in part.split('-')]
    if len(ends)==1: pages.add(ends[0])
    else:
        assert len(ends)==2 and ends[0]<=ends[1]
        pages.update(range(ends[0],ends[1]+1))
pages=sorted(pages)
started=datetime.now(timezone.utc)
begin=time.perf_counter()
doc=fitz.open(source)
assert pages and min(pages)>=1 and max(pages)<=len(doc)
images=[]
for n in pages:
    path=out/f'page_{n:03d}.png'
    doc[n-1].get_pixmap(matrix=fitz.Matrix(a.scale,a.scale),alpha=False).save(path)
    images.append(str(path.relative_to(root)))
contacts=[]
for offset in range(0,len(images),12):
    subset=images[offset:offset+12]
    tiles=[]
    for i,name in enumerate(subset):
        im=Image.open(root/name).convert('RGB')
        im.thumbnail((340,480))
        tile=Image.new('RGB',(360,510),'#e8e8e8')
        ImageDraw.Draw(tile).text((10,7),f'PDF page {pages[offset+i]}',fill='black')
        tile.paste(im,((360-im.width)//2,27))
        tiles.append(tile)
    sheet=Image.new('RGB',(1080,510*((len(tiles)+2)//3)),'white')
    for i,tile in enumerate(tiles): sheet.paste(tile,((i%3)*360,(i//3)*510))
    target=out/f'contact_{offset//12+1}.png'
    sheet.save(target)
    contacts.append(str(target.relative_to(root)))
record={
 'source':str(source.relative_to(root)),
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'source_pdf_pages':len(doc),
 'rendered_pdf_pages':pages,
 'started_utc':started.isoformat(),
 'finished_utc':datetime.now(timezone.utc).isoformat(),
 'seconds':time.perf_counter()-begin,
 'scale':a.scale,
 'images':images,
 'contact_sheets':contacts,
 'reading_status':'PENDING: rendering alone does not establish actual source reading',
}
log.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
