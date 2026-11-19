#!/usr/bin/env python3
"""Render selected PDF pages for visual inspection; images are temporary."""
from pathlib import Path
import sys,fitz
from PIL import Image,ImageDraw
pdfpath=Path(sys.argv[1]);dest=Path(sys.argv[2]);dest.mkdir(parents=True,exist_ok=True)
pdf=fitz.open(pdfpath);nums=list(map(int,sys.argv[3:])) or [1,len(pdf)]
tiles=[]
for n in nums:
 pix=pdf[n-1].get_pixmap(matrix=fitz.Matrix(1.2,1.2));p=dest/f'page_{n:03d}.png';pix.save(p)
 im=Image.open(p).convert('RGB');im.thumbnail((397,562));tile=Image.new('RGB',(420,595),'#ddd');tile.paste(im,((420-im.width)//2,20));ImageDraw.Draw(tile).text((12,578),f'Page {n}',fill='black');tiles.append(tile)
sheet=Image.new('RGB',(420*4,595*((len(tiles)+3)//4)),'white')
for j,im in enumerate(tiles):sheet.paste(im,((j%4)*420,(j//4)*595))
sheet.save(dest/'contact.png');print('Rendered pages',nums,'of',len(pdf))
