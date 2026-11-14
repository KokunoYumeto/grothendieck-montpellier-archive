#!/usr/bin/env python3
"""Regenerate the observed script-letter/number-ring comparison from scan ZIP images."""
from pathlib import Path
import argparse
from PIL import Image,ImageDraw

CLIPS=[
 ('site5 ell','esq_119_005_b.jpg',(588,402,620,442)),
 ('site8 ell 1','esq_119_008_b.jpg',(559,410,587,447)),
 ('site8 ell 2','esq_119_008_b.jpg',(959,468,988,503)),
 ('site11 ell','esq_119_011_a.jpg',(566,922,595,960)),
 ('site13 ell0','esq_119_013_b.jpg',(600,121,627,154)),
 ('site13 ell1','esq_119_013_b.jpg',(635,121,661,154)),
 ('site13 ell2','esq_119_013_b.jpg',(669,121,696,154)),
 ('site13 ell1 squared','esq_119_013_b.jpg',(1217,207,1246,242)),
 ('site5 Z','esq_119_005_b.jpg',(1218,365,1245,402)),
 ('site8 Z 1','esq_119_008_b.jpg',(617,411,648,448)),
 ('site8 Z 2','esq_119_008_b.jpg',(1019,485,1051,519)),
 ('site11 Z','esq_119_011_a.jpg',(625,925,655,961)),
]

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--images',default='work/images/scans');ap.add_argument('--output',default='work/crops/audit_ell_Z_compare.jpg');args=ap.parse_args()
    canvas=Image.new('RGB',(1300,760),'white');draw=ImageDraw.Draw(canvas)
    for i,(name,file,box) in enumerate(CLIPS):
        im=Image.open(Path(args.images)/file).crop(box)
        im=im.resize((im.width*5,im.height*5))
        x=(i%4)*320+15;y=(i//4)*250+25
        draw.text((x,y-15),name,fill='black');canvas.paste(im,(x,y))
    dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True);canvas.save(dest)

if __name__=='__main__':main()
