"""Crop regions of full-page scans of MPL_149_001-090 and stack them in one montage.

Usage: python -I -B crop.py OUTNAME spec [spec ...]
  spec = SCAN:x0,y0,x1,y1[:scale[:rot]]   (full-page pixel coordinates; rot in degrees, counter-clockwise)
The montage is written to this folder as OUTNAME.png, each crop labelled with its spec.
"""
import os
import sys

from PIL import Image, ImageDraw, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, '..', '..', 'img', 'MPL_149_001-090')


def one(spec):
    parts = spec.split(':')
    scan = int(parts[0])
    x0, y0, x1, y1 = (int(v) for v in parts[1].split(','))
    scale = float(parts[2]) if len(parts) > 2 and parts[2] else 2.0
    rot = float(parts[3]) if len(parts) > 3 else 0.0
    im = Image.open(os.path.join(IMG, 'MPL_149_001-090_scan%03d.jpg' % scan)).convert('L')
    c = im.crop((x0, y0, x1, y1))
    c = ImageOps.autocontrast(c, cutoff=1)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    return c


def main():
    out = sys.argv[1]
    specs = sys.argv[2:]
    crops = [(s, one(s)) for s in specs]
    w = max(c.width for _, c in crops)
    h = sum(c.height + 22 for _, c in crops)
    m = Image.new('L', (w, h), 255)
    d = ImageDraw.Draw(m)
    y = 0
    for s, c in crops:
        d.text((4, y + 4), s, fill=0)
        y += 22
        m.paste(c, (0, y))
        y += c.height
    m.save(os.path.join(HERE, out + '.png'))
    print(out, m.size)


if __name__ == '__main__':
    main()
