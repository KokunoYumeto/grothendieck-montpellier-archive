"""Crop, enlarge and stack regions of the whole-page scans of block MPL_151_032-075 (scans 32-46).

Usage: python -I -B crops.py OUTNAME SPEC [SPEC ...]
SPEC = scan:x0,y0,x1,y1[:scale[:rot]]   coordinates on the whole page image (1690 x 2361 approx.)
Writes OUTNAME.jpg in this folder: the crops stacked top to bottom, each labelled.
"""
import sys, os
from PIL import Image, ImageDraw, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, '..', '..', 'img', 'MPL_151_032-075')
MAXW = 1900

def one(spec):
    parts = spec.split(':')
    scan = int(parts[0])
    x0, y0, x1, y1 = [int(v) for v in parts[1].split(',')]
    scale = float(parts[2]) if len(parts) > 2 else 2.0
    rot = int(parts[3]) if len(parts) > 3 else 0
    im = Image.open(os.path.join(IMG, 'MPL_151_032-075_151_scan%03d.jpg' % scan)).convert('L')
    c = im.crop((x0, y0, x1, y1))
    if rot:
        c = c.rotate(rot, expand=True, fillcolor=255)
    w, h = c.size
    s = min(scale, MAXW / w)
    c = c.resize((int(w * s), int(h * s)), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    lab = Image.new('L', (c.size[0], 22), 255)
    ImageDraw.Draw(lab).text((4, 4), '%d [%d,%d,%d,%d] x%.1f r%d' % (scan, x0, y0, x1, y1, s, rot), fill=0)
    out = Image.new('L', (c.size[0], c.size[1] + 22), 255)
    out.paste(lab, (0, 0)); out.paste(c, (0, 22))
    return out

def main():
    name = sys.argv[1]
    tiles = [one(s) for s in sys.argv[2:]]
    W = max(t.size[0] for t in tiles)
    H = sum(t.size[1] + 6 for t in tiles)
    canvas = Image.new('L', (W, H), 200)
    y = 0
    for t in tiles:
        canvas.paste(t, (0, y)); y += t.size[1] + 6
    p = os.path.join(HERE, name + '.jpg')
    canvas.save(p, quality=90)
    print(p, canvas.size)

if __name__ == '__main__':
    main()
