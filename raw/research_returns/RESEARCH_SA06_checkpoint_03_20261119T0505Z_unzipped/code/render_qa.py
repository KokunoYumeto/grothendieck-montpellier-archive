#!/usr/bin/env python3
"""Render named PDF pages and contact sheets for manual visual inspection."""
from pathlib import Path
import argparse, json
import fitz
from PIL import Image, ImageOps, ImageDraw

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('label')
parser.add_argument('pages', nargs='+', type=int)
args = parser.parse_args()
out = root / 'rendered'
out.mkdir(exist_ok=True)
doc = fitz.open(root / 'RESEARCH_SA06_paper.pdf')
thumbs = []
for number in args.pages:
    page = doc[number - 1]
    path = out / f'{args.label}_page_{number:03}.png'
    page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25), alpha=False).save(path)
    im = Image.open(path).convert('RGB')
    im.thumbnail((470, 665))
    cell = Image.new('RGB', (490, 705), '#e5e7eb')
    cell.paste(im, ((490-im.width)//2, 27))
    ImageDraw.Draw(cell).text((10, 8), f'Page {number}', fill='black')
    thumbs.append(cell)
contacts=[]
for j in range(0,len(thumbs),9):
    batch=thumbs[j:j+9]
    sheet=Image.new('RGB',(1470,705*((len(batch)+2)//3)),'white')
    for k,im in enumerate(batch):sheet.paste(im,((k%3)*490,(k//3)*705))
    path=out/f'{args.label}_contact_{j//9+1:02}.png'
    sheet.save(path);contacts.append(str(path))
print(json.dumps({'pdf_pages':len(doc),'rendered_pages':args.pages,'contact_sheets':contacts}))
