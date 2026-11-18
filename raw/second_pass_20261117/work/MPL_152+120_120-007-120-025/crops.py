# Crop helper for the second pass of block MPL_152+120_120-007-120-025 (cote 120, scans 7-25).
# Usage: python -I -B crops.py OUTNAME "scan,x0,y0,x1,y1,angle,scale" ["..."]
# Coordinates are in the whole-page image (scanNNN.jpg). angle in degrees (counter-clockwise, PIL),
# scale = enlargement factor. All crops are stacked vertically into one labelled montage OUTNAME.jpg.
import sys, os
from PIL import Image, ImageDraw, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, '..', '..', 'img', 'MPL_152+120')
MAXW = 1700

def one(spec):
    scan, x0, y0, x1, y1, ang, sc = spec.split(',')
    scan = int(scan); x0, y0, x1, y1 = map(int, (x0, y0, x1, y1)); ang = float(ang); sc = float(sc)
    im = Image.open(os.path.join(IMG, 'MPL_152+120_120_scan%03d.jpg' % scan)).convert('L')
    c = im.crop((x0, y0, x1, y1))
    if ang:
        c = c.rotate(ang, expand=True, fillcolor=255, resample=Image.BICUBIC)
    c = c.resize((max(1, int(c.width * sc)), max(1, int(c.height * sc))), Image.LANCZOS)
    c = ImageOps.autocontrast(c, cutoff=1)
    if c.width > MAXW:
        r = MAXW / c.width
        c = c.resize((MAXW, int(c.height * r)), Image.LANCZOS)
    lab = 's%d [%d,%d,%d,%d] rot%g x%g' % (scan, x0, y0, x1, y1, ang, sc)
    return c, lab

def main():
    out = sys.argv[1]
    parts = [one(s) for s in sys.argv[2:]]
    W = max(p[0].width for p in parts)
    H = sum(p[0].height + 22 for p in parts)
    m = Image.new('L', (W, H), 255)
    d = ImageDraw.Draw(m)
    y = 0
    for c, lab in parts:
        d.rectangle((0, y, W, y + 20), fill=200)
        d.text((4, y + 4), lab, fill=0)
        m.paste(c, (0, y + 22))
        y += c.height + 22
    p = os.path.join(HERE, out + '.jpg')
    m.save(p, quality=92)
    print(p, m.size)

if __name__ == '__main__':
    main()
