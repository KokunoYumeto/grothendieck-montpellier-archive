#!/usr/bin/env python3
"""Render a distributed sample and requested pages for human visual inspection.

The output explicitly does not claim inspection merely because rendering ran.
Use --inspected only after opening the rendered images and checking them.
"""
from pathlib import Path
import argparse
import json
import re
import time
import fitz
from PIL import Image, ImageOps, ImageDraw

ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--pages',default='')
parser.add_argument('--inspected',action='store_true')
args=parser.parse_args()
start=time.perf_counter()
doc=fitz.open(ROOT/'RESEARCH_SA05_paper.pdf')
count=len(doc)
pages={1,count}
pages.update(round(1+i*(count-1)/8) for i in range(9))
pages.update(int(x) for x in args.pages.split(',') if x)
pages=sorted(p for p in pages if 1<=p<=count)
out=ROOT/'build/qa';out.mkdir(parents=True,exist_ok=True)
thumbs=[]
for page in pages:
    pix=doc[page-1].get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False)
    target=out/f'page_{page:03d}.png';pix.save(target)
    im=Image.open(target).convert('RGB');im.thumbnail((395,565))
    tile=Image.new('RGB',(415,600),'#dddddd')
    tile.paste(im,((415-im.width)//2,22))
    ImageDraw.Draw(tile).text((12,580),f'Page {page}',fill='black')
    thumbs.append(tile)
cols=3;rows=(len(thumbs)+cols-1)//cols
sheet=Image.new('RGB',(cols*415,rows*600),'white')
for i,im in enumerate(thumbs):sheet.paste(im,((i%cols)*415,(i//cols)*600))
sheet.save(out/'contact_sheet.png')
log=(ROOT/'build/RESEARCH_SA05_paper.log').read_text(errors='replace')
overflows=re.findall(r'Overfull \\[hv]box \(([^)]+)\)',log)
result=dict(pages=count,rendered_pages=pages,overfull_boxes=overflows,
            over_2pt=[v for v in overflows if float(re.search(r'[0-9.]+',v).group())>2],
            visual_inspection_passed=args.inspected,
            note='Inspection status is recorded only after the images have actually been opened.',
            wall_seconds=time.perf_counter()-start)
(ROOT/'code/pdf_qa_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
