#!/usr/bin/env python3
"""Recreate the inspection crops beside out/ from the original attached JPGs."""
import argparse,csv
from pathlib import Path
from PIL import Image,ImageEnhance
root=Path(__file__).resolve().parent
ap=argparse.ArgumentParser()
ap.add_argument('scan_directory',type=Path,nargs='?',default=root.parent)
ap.add_argument('--dest',type=Path,default=root.parent/'crops')
args=ap.parse_args();args.dest.mkdir(exist_ok=True,parents=True)
with (root/'crop_coordinates.tsv').open() as f:
 for row in list(csv.reader(f,delimiter='\t'))[1:]:
  n,name,l,t,r,b,*angle=row
  with Image.open(args.scan_directory/f'K58-03_58_scan{int(n):03}.jpg') as im:
   c=im.convert('L').crop(tuple(map(int,(l,t,r,b))))
  if angle and float(angle[0]):c=c.rotate(float(angle[0]),Image.Resampling.BICUBIC,expand=True,fillcolor=255)
  c=ImageEnhance.Contrast(c).enhance(1.35)
  c.resize((c.width*3,c.height*3),Image.Resampling.LANCZOS).save(args.dest/name)

with (root/'crop_details.tsv').open() as f:
 for row in csv.DictReader(f,delimiter='\t'):
  bounds=tuple(int(row[k]) for k in ['left','top','right','bottom'])
  with Image.open(args.dest/row['parent']) as im:
   im.crop(bounds).save(args.dest/row['crop'])
