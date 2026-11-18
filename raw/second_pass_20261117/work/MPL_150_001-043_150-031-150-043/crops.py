"""Crop/enlarge/rotate helper for the second pass of MPL_150_001-043, scans 31-43.

Usage: python -I -B crops.py SCAN OUTNAME SCALE BOX [BOX ...]
  BOX = x0,y0,x1,y1[,rot]  in full-page pixel coordinates (rot in degrees, counter-clockwise)
Crops are enlarged by SCALE, stacked vertically with a red separator, and saved in this folder.
"""
import sys, os
from PIL import Image, ImageDraw, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, '..', '..', 'img', 'MPL_150_001-043')

def main():
    scan = int(sys.argv[1]); out = sys.argv[2]; scale = float(sys.argv[3])
    page = Image.open(os.path.join(IMG, 'MPL_150_001-043_150_scan%03d.jpg' % scan)).convert('L')
    pieces = []
    for spec in sys.argv[4:]:
        v = [float(t) for t in spec.split(',')]
        x0, y0, x1, y1 = [int(t) for t in v[:4]]
        rot = v[4] if len(v) > 4 else 0
        c = page.crop((x0, y0, x1, y1))
        if rot:
            c = c.rotate(rot, expand=True, fillcolor=255, resample=Image.BICUBIC)
        c = c.resize((max(1, int(c.width * scale)), max(1, int(c.height * scale))), Image.LANCZOS)
        c = ImageOps.autocontrast(c, cutoff=1)
        pieces.append(c)
    W = max(p.width for p in pieces); H = sum(p.height for p in pieces) + 6 * (len(pieces) - 1)
    canvas = Image.new('RGB', (W, H), 'white'); y = 0
    d = ImageDraw.Draw(canvas)
    for i, p in enumerate(pieces):
        canvas.paste(p.convert('RGB'), (0, y)); y += p.height
        if i < len(pieces) - 1:
            d.rectangle((0, y, W, y + 5), fill=(220, 0, 0)); y += 6
    path = os.path.join(HERE, out + '.png'); canvas.save(path)
    print(path, canvas.size)

if __name__ == '__main__':
    main()
